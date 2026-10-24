"""Programmatic object builders on top of cc_client. Tested 2026-09-30 on a caption + highlight job.
All positions are y-UP 0..1 (0.5,0.5 = centre). Shape width/height are fractions of frame WIDTH.
Colours are LINEAR light; pass hex through lin(). Commands target stable IDs; animation uses atomic native batches.
"""
from cc_client import run, tool

def lin(h):
    h = h.lstrip('#'); out = []
    for i in (0, 2, 4):
        v = int(h[i:i+2], 16) / 255
        out.append(v / 4.5 if v < 0.081 else ((v + 0.099) / 1.099) ** (1 / 0.45))
    return [round(x, 5) for x in out]
def rgba(h, a=1): return lin(h) + [a]
def grad(c1, c2, mode='linear', start=(0, 0.5), end=(1, 0.5)):
    return {"mode": mode, "start": list(start), "end": list(end),
            "stops": [{"p": 0, "color": lin(c1), "a": 1}, {"p": 1, "color": lin(c2), "a": 1}]}

class Obj:
    CAPS = {'tr':'transform.placement','fill':'shape.fill','stroke':'shape.stroke',
            'geo':'shape.geometry.rectangle','ell':'shape.geometry.ellipse','font':'text.font',
            'tfill':'text.fill','tout':'text.outline','rel':'text.relative'}
    def __init__(s, id): s.id = id
    def k(s, cat, name): return f"{s.CAPS[cat]}.{name}"
    def idx(s):
        matches=[o['index'] for o in tool('carvercat_list')['objects'] if o['id']==s.id]
        if len(matches)!=1:raise ValueError('Object no longer exists')
        return matches[0]
    def sel(s): return run('param.list', id=s.id, quiet=True)
    def set(s, cat, name, v): return run('property.set',id=s.id,key=s.k(cat,name),value=v,quiet=True)
    def key(s, cat, name, frame, v):
        from cc_client import _default
        return _default.batch([{'command':'key.set','args':{'id':s.id,'key':s.k(cat,name),'value':v},'frame':frame}])
    def ease(s, cat, name, f0, f1):
        from cc_client import _default
        return _default.batch([{'command':'key.handle','args':{'id':s.id,'path':s.k(cat,name),'frame':f,'side':side,'x':x,'y':y}} for f,side,x,y in [(f0,'out',.32,0),(f1,'in',.68,1)]])
    def anim(s, cat, name, pairs):
        from cc_scene import Scene
        from cc_client import _default
        plan=Scene(_default);plan.ids['target']=s.id;plan.keys('target',s.k(cat,name),pairs);return plan.apply()

def new(kind, track, start, dur):
    """track = VIDEO row index (never the audio row). Placed at `start` via view.seek."""
    run('view.seek', frame=start, quiet=True)
    j = run('object.new', kind=kind, track=track, duration=dur, quiet=True)
    return Obj(j['touched'][0])

def card(track, start, dur, cx, cy, w, h, radius=0.3, fill='#0A0F1F', fa=0.72, g=('#20D6C7', '#7A5CFF'), sw=0.003):
    o = new('rectangle', track, start, dur)
    o.set('geo', 'width', w); o.set('geo', 'height', h); o.set('geo', 'cornerRadius', radius)
    o.set('fill', 'paint', 'solid'); o.set('fill', 'color', rgba(fill, fa))
    o.set('stroke', 'paint', 'gradient'); o.set('stroke', 'width', sw)
    o.set('stroke', 'gradient', grad(*g, start=(0, 0), end=(1, 1)))
    o.set('tr', 'position', [cx, cy])
    run('effect.add', id=o.id, cap='shadow', quiet=True)
    return o

def text(track, start, dur, s, cx, cy, size, fam='Poppins', style='Bold', color='#FFFFFF', gr=None, tracking=None):
    o = new('text', track, start, dur)
    run('property.set', id=o.id, key='text', value=s, quiet=True)
    o.set('font', 'family', fam); o.set('font', 'style', style); o.set('font', 'size', size)
    if tracking is not None: o.set('font', 'tracking', tracking)  # units unclear: garbled at 0.12 / 6, so leave unset
    o.set('tfill', 'color', lin(color))
    if gr: o.set('tfill', 'gradient', gr)
    o.set('tr', 'position', [cx, cy])
    return o

def clear():
    while tool('carvercat_list')['objects']:
        run('select.clip', index=0, quiet=True); run('edit.delete', quiet=True)

def stagger_caption(track, ts, t_out, s, gap, cy=0.28, size=0.088):
    """Word-by-word slide-up caption with no background box. gap = frames between words (3..12)."""
    t = text(track, ts, t_out - ts, s, 0.5, cy, size)
    run('stagger.new', quiet=True)
    run('stagger.connect', param='text.position', quiet=True); run('stagger.connect', param='fill.opacity', quiet=True)
    run('stagger.set', by='word', gap=gap, order='forward', quiet=True)
    t.anim('rel', 'position', [(ts, [0, -0.04]), (ts + 9, [0, 0])])
    t.anim('tfill', 'opacity', [(ts, 0), (ts + 9, 1)])
    t.anim('tr', 'opacity', [(t_out - 8, 1), (t_out - 2, 0)])
    t.sel(); run('effect.add', cap='shadow', quiet=True)  # readability without a box
    return t