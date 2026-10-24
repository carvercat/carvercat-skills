"""Pixel-first editable scene plans, native measurement and optional components.
All times are comp frames. Plans patch explicit IDs; no document clearing.
"""
from dataclasses import dataclass, field
import json
import math
from functools import lru_cache
from pathlib import Path
from cc_client import Client, CarvercatError

@lru_cache(maxsize=1)
def _control_declarations():
    path=Path(__file__).resolve().parent.parent/'references/app/native-controls.json'
    return json.loads(path.read_text(encoding='utf8'))['caps']

def finite(*values):
    if not all(isinstance(v,(int,float)) and math.isfinite(v) for v in values):raise ValueError("Expected finite numbers")
def linear_hex(value):
    value=value.lstrip("#")
    if len(value) not in (6,8):raise ValueError("Use #RRGGBB or #RRGGBBAA")
    rgb=[int(value[i:i+2],16)/255 for i in (0,2,4)]
    # Carvercat uses the established BT.709 transfer conversion (matches cc_build.lin).
    return [v/4.5 if v<0.081 else ((v+0.099)/1.099)**(1/0.45) for v in rgb]+([int(value[6:8],16)/255] if len(value)==8 else [])

@dataclass
class Box:
    x:float;y:float;w:float;h:float
    def __post_init__(self):
        finite(self.x,self.y,self.w,self.h)
        if self.w<0 or self.h<0:raise ValueError("Negative box size")
    @property
    def center(self):return self.x+self.w/2,self.y+self.h/2
    def inset(self,padding):
        finite(padding)
        if padding<0 or padding*2>min(self.w,self.h):raise ValueError("Padding does not fit")
        return Box(self.x+padding,self.y+padding,self.w-2*padding,self.h-2*padding)
    def overlaps(self,other):return self.x<other.x+other.w and self.x+self.w>other.x and self.y<other.y+other.h and self.y+self.h>other.y
    def contains(self,other):return self.x<=other.x and self.y<=other.y and self.x+self.w>=other.x+other.w and self.y+self.h>=other.y+other.h

@dataclass
class Scene:
    client:Client
    width:float=1920
    height:float=1080
    ids:dict=field(default_factory=dict)
    steps:list=field(default_factory=list)
    revision:str=None
    def __post_init__(self):
        state=self.client.state();self.width=state['comp']['width'];self.height=state['comp']['height'];self.revision=state['revision'];self.comp=state['comp']['name'];self.text_factor=state['authoringUnits']['textSizeToPixels'];self.document=state['document'];self.effects={};self.effect_owners={};self.scales={};self.pending_scales={};self.effect_removals=set();self.font_units={};self.pending_fonts={}
        listed=self.client.tool('carvercat_list');self.scope=[(c['index'],c['name'],c['open']) for c in listed['comps']]
        self.objects={};self.ambiguous={};self.pending_objects={};self.pending_removals=set();self.font_resolutions={}
        grouped={}
        for obj in listed.get('objects',[]):grouped.setdefault(obj['name'],[]).append(obj)
        for name,objects in grouped.items():
            if len(objects)==1:
                self.objects[name]=objects[0];self.ids.setdefault(name,objects[0]['id'])
            else:self.ambiguous[name]=[o['id'] for o in objects]
    def target(self,name):
        if name in self.ambiguous and name not in self.ids:raise CarvercatError(f"Ambiguous object name {name}; bind one stable ID deliberately")
        if name in self.ids:return self.ids[name]
        if any(s.get('as')==name for s in self.steps):return {'$ref':name}
        raise KeyError(f"Unknown scene object {name}")
    def command(self,command,args=None,*,frame=None,alias=None):
        step={'command':command,'args':args or {}}
        if frame is not None:finite(frame);step['frame']=frame
        if alias is not None:step['as']=alias
        self.steps.append(step);return self
    def create(self,name,kind,*,start=0,duration=90,track=None):
        if name in self.ambiguous or name in self.ids or name in self.effect_owners or any(s.get('as')==name for s in self.steps):raise ValueError(f"Duplicate scene name {name}")
        if duration<=0:raise ValueError("Duration must be positive")
        args={'kind':kind,'duration':duration}
        if track is not None:args['track']=track
        self.pending_objects[name]={'name':name,'kind':kind,'start':start,'length':duration}
        self.command('object.new',args,frame=start,alias=name)
        self.command('clip.rename',{'id':self.target(name),'name':name})
        return self.set(name,'transform.placement.scale',[1,1])
    def set(self,name,key,value):
        if key=='transform.placement.scale':self.pending_scales[name]=value
        if key=='text.font.size':self.pending_fonts[name]=value
        return self.command('property.set',{'id':self.target(name),'key':key,'value':value})
    def position(self,name,x,y):
        finite(x,y);return self.set(name,'transform.placement.position',[x/self.width,1-y/self.height])
    def rectangle(self,name,box,*,fill='#151B2A',alpha=1,radius=.2,start=0,duration=90,track=None):
        self.create(name,'rectangle',start=start,duration=duration,track=track)
        self.set(name,'shape.geometry.rectangle.width',box.w/self.width).set(name,'shape.geometry.rectangle.height',box.h/self.width)
        self.set(name,'shape.geometry.rectangle.cornerRadius',radius)
        color=linear_hex(fill);self.set(name,'shape.fill.paint','solid').set(name,'shape.fill.color',color[:3]+[color[3] if len(color)==4 else alpha])
        return self.position(name,*box.center)
    def text(self,name,content,*,x=960,y=540,size=64,family='Open Sans',style='Regular',color='#FFFFFF',direction='auto',start=0,duration=90,track=None,require_font=False):
        self.check_font(family,style,content,require=require_font)
        self.create(name,'text',start=start,duration=duration,track=track)
        for key,value in {'text.content.content':content,'text.font.family':family,'text.font.style':style,'text.font.size':size/(self.width*self.text_factor),'text.fill.color':linear_hex(color)[:3],}.items():self.set(name,key,value)
        if direction!='auto':
            self.command('param.promote',{'id':self.target(name),'path':'text.typography.readingDirection','on':True})
            self.set(name,'text.typography.readingDirection',direction)
        return self.position(name,x,y)
    def keys(self,name,key,pairs,*,ease=True):
        # Repeated frame values have one deterministic last value; one key gets no handle.
        pairs=sorted(dict(pairs).items())
        if not pairs:raise ValueError('Empty animation')
        for frame,value in pairs:self.command('key.set',{'id':self.target(name),'key':key,'value':value},frame=frame)
        if ease:
            for (a,_),(b,_) in zip(pairs,pairs[1:]):
                self.command('key.handle',{'id':self.target(name),'path':key,'frame':a,'side':'out','x':.2,'y':.8,'tied':False})
                self.command('key.handle',{'id':self.target(name),'path':key,'frame':b,'side':'in','x':.4,'y':1,'tied':False})
        return self
    def entrance(self,names,*,start=0,frames=12,stagger=0,scale=.94):
        if frames<1:raise ValueError('Entrance needs at least one frame')
        for i,name in enumerate(names):
            f=start+i*stagger
            self.keys(name,'transform.placement.opacity',[(f,0),(f+frames,1)])
            base=self.pending_scales.get(name,self.scales.get(name))
            if base is None:
                params=self.parameters(name)
                base=json.loads(next(p['value'] for p in params if p['cap']=='transform.placement' and p['path'].endswith('.scale')))
            self.keys(name,'transform.placement.scale',[(f,[base[0]*scale,base[1]*scale]),(f+frames,base)])
        return self
    def envelope(self,name,*,start,hold_end,end,fade=8):
        if not start<=start+fade<=hold_end<end:raise ValueError('Invalid visibility envelope')
        return self.keys(name,'transform.placement.opacity',[(start,0),(start+fade,1),(hold_end,1),(end,0)])
    def discard(self):
        """Discard an unapplied/rejected plan; never use this to replay an unknown outcome."""
        self.steps.clear();self.pending_objects.clear();self.pending_removals.clear();self.pending_scales.clear();self.pending_fonts.clear();self.effect_removals.clear();self.effect_owners={a:n for a,n in self.effect_owners.items() if a in self.effects};return self
    def _observe(self,name,mode,frame=0,query=None):
        target=self.target(name);args={'mode':mode,'id':target,'frame':frame}
        if query is not None:args['query']=query
        if self.steps:
            receipt=self.client.batch(self.steps,expected_revision=self.revision,expected_document=self.document,dry_run=True,observe=[args])
            if not receipt.get('validated') or not receipt.get('rolled_back') or receipt['revision']!=self.revision:raise CarvercatError('Plan observation did not restore its original revision')
            return receipt['observations'][0]
        result=self.client.tool('carvercat_authoring',**args)
        if result['revision']!=self.revision or result['document']!=self.document:raise CarvercatError('Scene changed during discovery; rebind deliberately')
        return result
    def bindings(self,name,*,frame=0,query=None):return self._observe(name,'controls',frame,query)
    def check_font(self,family,style='Regular',content='Aa09',*,require=False):
        sample='Aa09'+''.join(sorted(set(c for c in content if ord(c)>127)))
        cache=(family,style,sample)
        if cache not in self.font_resolutions:
            data=self.client.tool('carvercat_authoring',mode='fonts',query=family,family=family,style=style,sample=sample)
            self.font_resolutions[cache]=data.get('resolution',{'available':False})
        result=self.font_resolutions[cache]
        if require and not (result.get('exact_family') and result.get('exact_style')):raise CarvercatError(f'Font substitution: requested {family} / {style}; resolved {result}')
        return result
    def component(self,name,*,remove_missing=False):
        from cc_components import Component
        return Component(self,name,remove_missing=remove_missing)
    def place_center(self,name,x,y,*,frame=0):
        box=self.measure(name,frame)
        return self.place_bounds(name,x-box.w/2,y-box.h/2,frame)
    def ensure_effect(self,name,cap,*,alias=None,properties=None,entry=None):
        alias=alias or name+' '+cap
        if alias in self.effects:
            if self.effect_owners[alias]!=name:raise CarvercatError('Effect alias belongs to another object')
        elif any(step.get('as')==alias for step in self.steps):
            if self.effect_owners.get(alias)!=name:raise CarvercatError('Pending effect belongs to another object')
        else:
            parameters=self.bindings(name)['parameters']
            entries={p['entry'] for p in parameters if p['cap']==cap and (entry is None or p['entry']==entry)}
            if len(entries)>1:raise CarvercatError('Repeated effects are ambiguous; supply a specific entry')
            if entries:
                self.effects[alias]='fx.'+next(iter(entries));self.effect_owners[alias]=name
            elif entry is not None:raise CarvercatError('Requested effect entry is not on this object')
            else:return self.effect(name,cap,alias=alias,properties=properties)
        for key,value in (properties or {}).items():self.fx_set(alias,key,value)
        return self
    def fx_color(self,alias,color,*,alpha=None):
        rgba=linear_hex(color)
        if alpha is not None:finite(alpha);rgba=rgba[:3]+[alpha]
        return self.fx_set(alias,'color',rgba)
    def parameters(self,name):
        if name not in self.ids:raise ValueError('Apply object creation before discovery')
        return self.client.run('param.list',id=self.ids[name])['readings'][0]['params']
    def resolve_parameter(self,name,cap,parameter):
        matches=[p for p in self.parameters(name) if p['cap']==cap and p['path'].endswith('.'+parameter)]
        if len(matches)!=1:raise CarvercatError('Missing or ambiguous parameter; use a specific native effect entry')
        if not matches[0].get('available',True):raise CarvercatError(matches[0].get('unavailable_reason','Unavailable native parameter'))
        live=[p for p in self.bindings(name)['parameters'] if p['path']==matches[0]['path']]
        if len(live)!=1 or not live[0]['writable']:raise CarvercatError('Parameter has no writable native binding')
        return matches[0]
    def effect(self,name,cap,*,alias,properties=None):
        if alias in self.effects or alias in self.effect_owners or alias in self.ids:raise ValueError('Duplicate effect alias')
        self.effect_owners[alias]=name
        self.command('effect.add',{'id':self.target(name),'cap':cap},alias=alias)
        for parameter,value in (properties or {}).items():self.fx_set(alias,parameter,value)
        return self
    def fx_key(self,alias,parameter):
        if alias not in self.effect_owners:raise KeyError(alias)
        if alias in self.effects:return self.effects[alias]+'.'+parameter
        return {'$param':[alias,parameter]}
    def _fx_live(self,alias,parameter,*,animate=False):
        if alias not in self.effects:
            step=next((s for s in self.steps if s.get('as')==alias and s['command']=='effect.add'),None)
            if step:
                cap=step['args']['cap'];declared=next((p for p in _control_declarations().get(cap,[]) if p['param']==parameter),None)
                if declared is not None:return {'requires_promotion':not declared.get('factoryPromote') and not declared.get('absorbedBy')}
            return
        owner=self.effect_owners[alias];path=self.effects[alias]+'.'+parameter
        live=[p for p in self.bindings(owner)['parameters'] if p['path']==path]
        if len(live)!=1 or not (live[0]['writable'] or live[0].get('requires_promotion')) or animate and not live[0]['keyframeable']:raise CarvercatError('Effect parameter has no supported native binding; discover controls first')
        return live[0]
    def fx_set(self,alias,parameter,value,*,promote=False):
        live=self._fx_live(alias,parameter)
        key=self.fx_key(alias,parameter)
        if promote or live and live.get('requires_promotion'):self.command('param.promote',{'id':self.target(self.effect_owners[alias]),'path':key,'on':True})
        return self.set(self.effect_owners[alias],key,value)
    def fx_keys(self,alias,parameter,pairs,*,ease=True,promote=False):
        live=self._fx_live(alias,parameter,animate=True)
        key=self.fx_key(alias,parameter)
        if promote or live and live.get('requires_promotion'):self.command('param.promote',{'id':self.target(self.effect_owners[alias]),'path':key,'on':True})
        return self.keys(self.effect_owners[alias],key,pairs,ease=ease)
    def remove_effect(self,alias):
        if alias not in self.effects:raise ValueError('Apply effect creation before removal')
        self.effect_removals.add(alias)
        return self.command('effect.remove',{'id':self.target(self.effect_owners[alias]),'entry':self.effects[alias].split('.',1)[1]})
    def blur(self,name,*,size=10,alias=None):return self.effect(name,'blur',alias=alias or name+' blur',properties={'size':size})
    def glow(self,name,*,size=10,amount=.8,blend=.2,alias=None):return self.effect(name,'glow',alias=alias or name+' glow',properties={'size':size,'amount':amount,'blend':blend})
    def shadow(self,name,*,x_px=8,y_px=8,softness_px=12,opacity=.38,color='#000000',alias=None):
        color=linear_hex(color)
        return self.effect(name,'shadow',alias=alias or name+' shadow',properties={'x':x_px/self.width,'y':-y_px/self.height,'softness':softness_px/self.width,'opacity':opacity,'red':color[0],'green':color[1],'blue':color[2]})
    def trim_path(self,name,*,start=0,end=1,offset=0,alias=None):return self.effect(name,'trim',alias=alias or name+' trim',properties={'start':start,'end':end,'offset':offset})
    def paint(self,name,*,layer='shape.fill',color=None,opacity=None,mode=None,gradient=None,width_px=None):
        if mode is not None:self.set(name,layer+'.paint',mode)
        if color is not None:
            rgb=linear_hex(color);self.set(name,layer+'.color',rgb[:3])
            if len(rgb)==4:self.command('param.promote',{'id':self.target(name),'path':layer+'.opacity','on':True});self.set(name,layer+'.opacity',rgb[3])
        if opacity is not None:self.command('param.promote',{'id':self.target(name),'path':layer+'.opacity','on':True});self.set(name,layer+'.opacity',opacity)
        if gradient is not None:self.set(name,layer+'.gradient',gradient)
        if width_px is not None:
            if layer=='text.outline':
                font=self.pending_fonts.get(name,self.font_units.get(name))
                if font is None:font=float(self.resolve_parameter(name,'text.font','size')['value'])
                self.set(name,layer+'.thickness',width_px/(font*self.width))
            else:self.set(name,layer+'.width',width_px/self.width)
        return self
    def transform(self,name,*,position=None,scale=None,rotation=None,opacity=None,anchor=None):
        if position is not None:self.position(name,*position)
        for parameter,value in [('scale',scale),('rotation',rotation),('opacity',opacity)]:
            if value is not None:self.set(name,'transform.placement.'+parameter,value)
        if anchor is not None:self.set(name,'transform.placement.anchor',list(anchor))
        return self
    def stagger(self,name,*,by='word',gap=4,order='forward',channels=('text.position','fill.opacity')):
        self.command('stagger.new',{'id':self.target(name)})
        for channel in channels:self.command('stagger.connect',{'id':self.target(name),'param':channel})
        return self.command('stagger.set',{'id':self.target(name),'by':by,'gap':gap,'order':order})
    def path(self,name,points,*,closed=False,start=0,duration=90,track=None,handles=None,fill=None,stroke='auto'):
        if name in self.ids or name in self.ambiguous or any(s.get('as')==name for s in self.steps):raise ValueError('Path name already exists')
        finite(start,duration)
        if duration<=0:raise ValueError('Duration must be positive')
        if track is not None and (type(track) is not int or track<0):raise ValueError('Track must be a nonnegative native index')
        native=[]
        for x,y in points:finite(x,y);native.append([x/self.width,y/self.height])
        if not 2<=len(native)<=4096:raise ValueError('Path requires 2..4096 points')
        args={'points':native,'closed':closed,'duration':duration}
        if track is not None:args['track']=track
        if handles is not None:
            if len(handles)!=len(native):raise ValueError('One handle pair required per point')
            converted=[]
            for h in handles:
                ix,iy=h['in'];ox,oy=h['out'];finite(ix,iy,ox,oy)
                if type(h.get('corner',False)) is not bool:raise ValueError('Corner must be Boolean')
                converted.append({'in':[ix/self.width,iy/self.height],'out':[ox/self.width,oy/self.height],'corner':h.get('corner',False)})
            args['handles']=converted
        self.pending_objects[name]={'name':name,'kind':'path','start':start,'length':duration}
        self.command('object.path',args,frame=start,alias=name)
        self.command('clip.rename',{'id':self.target(name),'name':name})
        if closed and stroke=='auto' or stroke is None:self.paint(name,layer='shape.stroke',mode='none')
        elif stroke!='auto':self.paint(name,layer='shape.stroke',mode='solid',color=stroke)
        if fill is not None:self.paint(name,mode='solid',color=fill)
        return self
    def replace_keys(self,name,key,pairs,*,ease=True):
        target=self.target(name)
        retained=[]
        for step in self.steps:
            same=step['args'].get('id')==target and step['args'].get('key',step['args'].get('path'))==key
            if not (same and step['command'] in ('key.set','key.remove','key.handle')):retained.append(step)
        frames=[]
        if name in self.ids:
            listed=self.client.run('key.list',id=self.ids[name],key=key)['readings'][0];frames=listed['frames']
        self.steps=retained
        for frame in frames:self.command('key.remove',{'id':target,'key':key},frame=frame)
        return self.keys(name,key,pairs,ease=ease)
    def extend_hold(self,name,*,duration,start,hold_end,end,fade=8):
        if self.steps:raise ValueError('Apply pending plan before extending hold')
        # Inspect and deliberately remove the obsolete relative text envelope, then replace placement keys.
        listed=self.client.run('key.list',id=self.ids[name],key='text.relative.opacity')['readings'][0]
        for frame in listed['frames']:self.command('key.remove',{'id':self.ids[name],'key':'text.relative.opacity'},frame=frame)
        params=self.client.run('param.list',id=self.ids[name])['readings'][0]['params']
        relative=next(p for p in params if p['cap']=='text.relative' and p['path'].endswith('.opacity'))
        if relative['on']!='panel':self.command('param.promote',{'id':self.ids[name],'path':relative['path'],'on':True})
        self.set(name,relative['path'],1)
        placement=self.client.run('key.list',id=self.ids[name],key='transform.placement.opacity')['readings'][0]
        for frame in placement['frames']:self.command('key.remove',{'id':self.ids[name],'key':'transform.placement.opacity'},frame=frame)
        self.command('clip.trim',{'id':self.ids[name],'duration':duration})
        return self.envelope(name,start=start,hold_end=hold_end,end=end,fade=fade)
    def patch(self,objects):
        # Properties/timing are explicit; unmentioned channels and user edits remain untouched.
        for name,spec in objects.items():
            if name not in self.ids:raise KeyError(name)
            for key,value in spec.get('properties',{}).items():self.set(name,key,value)
            for key,pairs in spec.get('keys',{}).items():self.keys(name,key,pairs)
        return self
    def anchor(self,name,box,*,horizontal='center',vertical='center',frame=0):
        size=self.measure(name,frame)
        x={'left':box.x,'center':box.x+(box.w-size.w)/2,'right':box.x+box.w-size.w}[horizontal]
        y={'top':box.y,'center':box.y+(box.h-size.h)/2,'bottom':box.y+box.h-size.h}[vertical]
        return self.place_bounds(name,x,y,frame)
    def baseline(self,names,y,*,frame=0):
        # Native point-text bottom alignment anchors the last baseline, not the glyph ink bottom.
        for name in names:
            params=self.client.run('param.list',id=self.ids[name])['readings'][0]['params']
            mode=next(p for p in params if p['cap']=='text.layout' and p['path'].endswith('.mode'))
            if mode['value']!='titles':raise CarvercatError('Baseline helper requires point text, not paragraph boxes')
            placement=next(p for p in params if p['cap']=='transform.placement' and p['path'].endswith('.position'))
            x=json.loads(placement['value'])[0]*self.width
            self.set(name,'text.layout.vAlign','bottom');self.position(name,x,y)
        return self
    def spec(self,description):
        for name,item in description['objects'].items():
            if name not in self.ids:self.create(name,item['kind'],start=item.get('start',0),duration=item.get('duration',90),track=item.get('track'))
            for key,value in item.get('properties',{}).items():self.set(name,key,value)
            for key,pairs in item.get('keys',{}).items():self.keys(name,key,pairs)
        return self
    def apply(self,*,dry_run=False):
        if not self.steps:return {'applied':False,'steps':[]}
        # Expected revision protects both user changes and accidental cross-comp application.
        state=self.client.state()
        if state['comp']['name']!=self.comp or state['revision']!=self.revision or state['document']!=self.document:raise CarvercatError('Scene context changed; deliberately rebind before patching')
        receipt=self.client.batch(self.steps,expected_revision=self.revision,expected_document=self.document,dry_run=dry_run)
        if not dry_run:
            self.ids.update(receipt['aliases']);self.effects.update(receipt.get('effects',{}));
            for name,obj in self.pending_objects.items():self.objects[name]={**obj,'id':self.ids[name]}
            self.pending_objects.clear()
            for name in self.pending_removals:self.ids.pop(name,None);self.objects.pop(name,None)
            self.pending_removals.clear()
            for alias in self.effect_removals:self.effects.pop(alias,None);self.effect_owners.pop(alias,None)
            self.effect_removals.clear();self.scales.update(self.pending_scales);self.font_units.update(self.pending_fonts);self.pending_fonts.clear();self.pending_scales.clear();self.revision=receipt['revision'];self.steps.clear()
        return receipt
    def rebind(self):
        state=self.client.state();listed=self.client.tool('carvercat_list')
        if state['comp']['name']!=self.comp or [(c['index'],c['name'],c['open']) for c in listed['comps']]!=self.scope:raise CarvercatError('Comp scope changed')
        objects={o['id']:o for o in listed['objects']}
        for name,id in self.ids.items():
            if id not in objects or objects[id]['name']!=name:raise CarvercatError(f'Object identity changed: {name}')
        self.revision=state['revision'];self.document=state['document'];return self
    def manifest(self,path):
        Path(path).write_text(json.dumps({'version':1,'comp':self.comp,'scope':self.scope,'ids':self.ids,'revision':self.revision,'document':self.document,'effects':self.effects,'effect_owners':self.effect_owners,'scales':self.scales},indent=2),encoding='utf8')
    def load_manifest(self,path):
        saved=json.loads(Path(path).read_text(encoding='utf8'))
        if saved['comp']!=self.comp or saved['scope']!=[list(c) for c in self.scope]:raise CarvercatError('Manifest belongs to another comp scope')
        if saved.get('document',{}).get('path') and saved['document']!=self.document:raise CarvercatError('Manifest belongs to another project file')
        self.ids=saved['ids'];self.effects=saved.get('effects',{});self.effect_owners=saved.get('effect_owners',{});self.scales=saved.get('scales',{});return self.rebind()
    def measure(self,name,frame=0):
        bounds=self._observe(name,'geometry',frame)['bounds']
        return Box(bounds['x'],bounds['y'],bounds['w'],bounds['h'])
    def place_bounds(self,name,x,y,frame=0):
        geometry=self._observe(name,'geometry',frame)
        b=geometry['bounds'];box=Box(b['x'],b['y'],b['w'],b['h'])
        # Native glyph bounds may be offset from the placement anchor; preserve that offset.
        params=self.bindings(name,frame=frame)['parameters']
        p=next(p for p in params if p['alias']=='transform.placement.position')
        if p['keyframes']:raise CarvercatError('Bounds placement on animated position requires a deliberate curve revision')
        native=p['value'];cx=native[0]*self.width;cy=(1-native[1])*self.height
        basis=geometry.get('placement_basis',[[1,0],[0,1]])
        a,b=basis[0];c,d=basis[1];det=a*d-b*c
        if abs(det)<1e-8:raise CarvercatError('Cannot place bounds through a zero-scale parent')
        dx,dy=x-box.x,y-box.y
        self.position(name,cx+(d*dx-b*dy)/det,cy+(-c*dx+a*dy)/det);return self
    def fit(self,name,box,*,frame=0,minimum_px=20,max_iterations=4):
        for _ in range(max_iterations):
            measured=self.measure(name,frame)
            if measured.w<=box.w+.5 and measured.h<=box.h+.5:return measured
            params=self.client.run('param.list',id=self.ids[name])['readings'][0]['params']
            font=next(p for p in params if p['cap']=='text.font' and p['path'].endswith('.size'))
            old=float(font['value'])*self.width*self.text_factor;new=old*min(box.w/max(measured.w,1),box.h/max(measured.h,1))*.98
            if new<minimum_px:raise CarvercatError('Text cannot fit without violating minimum size')
            self.rebind();self.set(name,'text.font.size',new/(self.width*self.text_factor));self.apply()
        raise CarvercatError('Text fitting did not converge')
    def flow(self,names,box,*,axis='row',gap=24,padding=0,rtl=False,align='center',frame=0):
        if axis not in ('row','column') or align not in ('start','center','end'):raise ValueError('Invalid flow mode')
        area=box.inset(padding);sizes={n:self.measure(n,frame) for n in names};ordered=list(reversed(names)) if rtl and axis=='row' else list(names)
        total=sum((sizes[n].w if axis=='row' else sizes[n].h) for n in ordered)+gap*max(0,len(names)-1)
        span=area.w if axis=='row' else area.h
        if total>span+.5:raise CarvercatError('Flow overflows its available span')
        cursor=(area.x if axis=='row' else area.y)+(span-total)/2
        for name in ordered:
            size=sizes[name];cross=(area.h-size.h) if axis=='row' else (area.w-size.w)
            if cross<0:raise CarvercatError('Flow overflows cross axis')
            offset={'start':0,'center':cross/2,'end':cross}[align]
            # Queue positions directly after individual native reads; one batch commits the group.
            self.place_bounds(name,cursor if axis=='row' else area.x+offset,area.y+offset if axis=='row' else cursor,frame)
            cursor+=(size.w if axis=='row' else size.h)+gap
        return self
    def check_zones(self,names,*,safe=None,avoid=(),frame=0):
        safe=safe or Box(self.width*.05,self.height*.05,self.width*.9,self.height*.9)
        bounds={n:self.measure(n,frame) for n in names}
        for name,b in bounds.items():
            if not safe.contains(b):raise CarvercatError(f'{name} leaves safe area')
            if any(b.overlaps(zone) for zone in avoid):raise CarvercatError(f'{name} overlaps a protected zone')
        return bounds
    def review(self,path,*,frames=(0,12,45,80),checks=()):
        if self.steps:raise ValueError('Apply plan before review')
        lint=self.client.tool('carvercat_inspect',mode='lint')
        expectation=self.client.tool('carvercat_inspect',mode='expect',checks=list(checks)) if checks else None
        look=self.client.look(path,looks=[{'from':f,'to':f,'count':1,'ground':'checker','overlay':['ids','safe'],'force':True} for f in frames])
        return {'lint':lint,'expect':expectation,'look':look,'font_resolutions':list(self.font_resolutions.values())}

def title_pair(scene,title,subtitle,*,box,start=0,duration=90,accent='#F0BD35'):
    scene.text('title',title,x=box.center[0],y=box.y+box.h*.35,size=76,color=accent,start=start,duration=duration)
    scene.text('subtitle',subtitle,x=box.center[0],y=box.y+box.h*.7,size=36,start=start,duration=duration)
    return scene

def number_highlight(scene,name,number,label,*,box,start=0,duration=90):
    scene.rectangle(name+' plate',box,start=start,duration=duration)
    scene.text(name+' number',number,size=68,direction='ltr',start=start,duration=duration)
    scene.text(name+' label',label,size=40,family='Almarai',style='ExtraBold',direction='rtl',start=start,duration=duration)
    return scene

def caption(scene,name,content,*,box,start=0,duration=90,direction='auto',background=True):
    if background:scene.rectangle(name+' plate',box,start=start,duration=duration)
    scene.text(name,content,x=box.center[0],y=box.center[1],size=48,family='Almarai' if direction=='rtl' else 'Open Sans',style='ExtraBold' if direction=='rtl' else 'Regular',direction=direction,start=start,duration=duration)
    return scene

def card_group(scene,name,title,label,*,box,start=0,duration=90):
    scene.rectangle(name+' card',box,start=start,duration=duration)
    scene.text(name+' title',title,x=box.center[0],y=box.y+box.h*.35,size=52,start=start,duration=duration)
    scene.text(name+' label',label,x=box.center[0],y=box.y+box.h*.7,size=30,start=start,duration=duration)
    return scene

def icon_label(scene,icon_name,label_name,label,*,box,start=0,duration=90):
    """Reuse a native icon already in Scene.ids; preserves the original icon geometry."""
    scene.target(icon_name)
    scene.text(label_name,label,x=box.center[0],y=box.center[1],size=36,start=start,duration=duration)
    return scene

def image_card(scene,name,media,*,box,start=0,duration=90,radius=.2):
    """Place an existing project-pool asset, measure cover scale and create its native mask.
    Import assets explicitly before this helper; import may auto-place objects.
    """
    if name in scene.ids:raise ValueError('Image already exists; patch it instead')
    scene.command('pool.place',{'media':media,'frame':start},alias=name)
    scene.command('clip.rename',{'id':scene.target(name),'name':name})
    scene.command('clip.trim',{'id':scene.target(name),'duration':duration});scene.apply()
    measured=scene.measure(name,start)
    if not measured.w or not measured.h:raise CarvercatError('Media has no measurable native bounds')
    scale=max(box.w/measured.w,box.h/measured.h)
    scene.set(name,'transform.placement.scale',[scale,scale]);scene.position(name,*box.center)
    scene.rectangle(name+' mask',box,fill='#FFFFFF',radius=radius,start=start,duration=duration);scene.apply()
    # Primary selection is the mask; image is the other selected member.
    scene.command('mask.make',{'ids':[scene.ids[name+' mask'],scene.ids[name]]});scene.apply()
    return scene

def gradient(stops,*,mode='linear',start=(0,.5),end=(1,.5)):
    """Normalized object-local gradient coordinates; explicit linear/radial native mode."""
    if mode not in ('linear','radial'):raise ValueError('Unsupported gradient mode')
    values=[]
    for position,color in stops:
        finite(position)
        if not 0<=position<=1:raise ValueError('Gradient stops must lie in 0..1')
        value=linear_hex(color);values.append({'p':position,'color':value[:3],'a':value[3] if len(value)==4 else 1})
    if len(values)<2:raise ValueError('At least two gradient stops required')
    return {'mode':mode,'start':list(start),'end':list(end),'stops':sorted(values,key=lambda s:s['p'])}
