"""Named, revision-safe native component updates. Namespace is explicit ownership."""
from cc_client import CarvercatError
from cc_scene import linear_hex

class Component:
    def __init__(self,scene,name,*,remove_missing=False):
        if not isinstance(name,str) or not name.strip():raise ValueError('Component name is required')
        self.scene=scene;self.prefix=name+' / ';self.used=set();self.remove_missing=remove_missing
    def __enter__(self):return self
    def __exit__(self,kind,*args):
        if kind is None:self.finish()
    def name(self,child):
        if not isinstance(child,str) or not child:raise ValueError('Child name is required')
        name=self.prefix+child
        if len(name.encode('utf8'))>80:raise ValueError('Component child name exceeds native alias limit')
        if name in self.scene.ambiguous:raise CarvercatError(f'Ambiguous component child {name}')
        self.used.add(name);return name
    def _item(self,child,kind,*,start=None,duration=None):
        name=self.name(child)
        if name in self.scene.ids or name in self.scene.pending_objects:
            info=self.scene.objects.get(name,self.scene.pending_objects.get(name,{}))
            if str(info.get('kind','')).lower()!=kind.lower():raise CarvercatError(f'Component child type changed: {name}; replace deliberately')
            if duration is not None:self.scene.command('clip.trim',{'id':self.scene.target(name),'duration':duration})
            if start is not None:self.scene.command('clip.move',{'id':self.scene.target(name),'frame':start})
            return name,False
        self.scene.create(name,kind,start=0 if start is None else start,duration=90 if duration is None else duration);return name,True
    def rectangle(self,child,box,*,fill=None,alpha=None,radius=None,start=None,duration=None):
        name,new=self._item(child,'rectangle',start=start,duration=duration)
        self.scene.set(name,'shape.geometry.rectangle.width',box.w/self.scene.width)
        self.scene.set(name,'shape.geometry.rectangle.height',box.h/self.scene.width)
        if radius is not None or new:self.scene.set(name,'shape.geometry.rectangle.cornerRadius',.2 if radius is None else radius)
        if fill is not None or new:
            rgba=linear_hex(fill or '#151B2A');self.scene.set(name,'shape.fill.paint','solid').set(name,'shape.fill.color',rgba[:3]+[rgba[3] if len(rgba)==4 and alpha is None else (1 if alpha is None else alpha)])
        elif alpha is not None:self.scene.paint(name,opacity=alpha)
        if new:self.scene.paint(name,layer='shape.stroke',mode='none')
        self.scene.position(name,*box.center);return name
    def text(self,child,content,*,x=None,y=None,size=None,family=None,style=None,color=None,start=None,duration=None,require_font=False):
        name=self.name(child)
        existing=self.scene.objects.get(name,self.scene.pending_objects.get(name,{}))
        new=name not in self.scene.ids and name not in self.scene.pending_objects
        if family is not None or style is not None or new:
            if not new:
                controls=self.scene.bindings(name)['parameters']
                get=lambda param:next(p['value'] for p in controls if p['alias']=='text.font.'+param)
                family=family or get('family');style=style or get('style')
            family=family or 'Open Sans';style=style or 'Regular'
            self.scene.check_font(family,style,content,require=require_font)
        name,new=self._item(child,'text',start=start,duration=duration)
        self.scene.set(name,'text.content.content',content)
        if family is not None:self.scene.set(name,'text.font.family',family)
        if style is not None:self.scene.set(name,'text.font.style',style)
        if size is not None or new:self.scene.set(name,'text.font.size',(64 if size is None else size)/(self.scene.width*self.scene.text_factor))
        if color is not None or new:self.scene.paint(name,layer='text.fill',color=color or '#FFFFFF')
        if x is not None or y is not None:
            if x is None or y is None:raise ValueError('Position requires both x and y')
            self.scene.position(name,x,y)
        return name
    def path(self,child,points,*,closed=True,fill=None,stroke='auto',start=None,duration=None):
        name=self.name(child)
        if name not in self.scene.ids and name not in self.scene.pending_objects:
            self.scene.path(name,points,closed=closed,fill=fill,stroke=stroke,start=0 if start is None else start,duration=90 if duration is None else duration)
        else:
            info=self.scene.objects.get(name,self.scene.pending_objects.get(name,{}))
            if str(info.get('kind','')).lower()!='path':raise CarvercatError('Existing child is not a path')
            geometry={'closed':closed,'points':[{'x':x/self.scene.width,'y':y/self.scene.height,'inX':0,'inY':0,'outX':0,'outY':0,'corner':True} for x,y in points]}
            frame=info.get('start',0) if start is None else start
            self.scene.replace_keys(name,'path.geometry',[(frame,geometry)],ease=False)
            if fill is not None:self.scene.paint(name,mode='solid',color=fill)
            if closed and stroke=='auto' or stroke is None:self.scene.paint(name,layer='shape.stroke',mode='none')
            elif stroke!='auto':self.scene.paint(name,layer='shape.stroke',mode='solid',color=stroke)
            if duration is not None:self.scene.command('clip.trim',{'id':self.scene.target(name),'duration':duration})
        return name
    def modify(self,child,*,properties=None,keys=None):
        name=self.name(child);self.scene.target(name)
        for key,value in (properties or {}).items():self.scene.set(name,key,value)
        for key,pairs in (keys or {}).items():self.scene.replace_keys(name,key,pairs)
        return name
    def effect(self,child,cap,*,properties=None,entry=None):
        name=self.name(child);self.scene.ensure_effect(name,cap,alias=name+' '+cap,properties=properties,entry=entry);return name+' '+cap
    def retain(self,child):self.scene.target(self.name(child));return self
    def finish(self):
        if self.remove_missing:
            ambiguous=[n for n in self.scene.ambiguous if n.startswith(self.prefix)]
            if ambiguous:raise CarvercatError('Cannot prune an ambiguous component namespace')
            for name,id in list(self.scene.ids.items()):
                if name.startswith(self.prefix) and name not in self.used:
                    self.scene.command('edit.delete',{'id':id});self.scene.pending_removals.add(name)
        return self.scene
