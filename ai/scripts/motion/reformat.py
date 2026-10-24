"""reformat.py - convert duplicated comps to a new frame size (e.g. 16:9 -> 9:16)
with a per-region layout, inside one .carverproj.

Why: `comp.format {width,height}` changes ONLY the frame. Positions are normalised
per axis, sizes are fractions of frame width and path points are per-axis
normalised, so after 1920x1080 -> 1080x1920 everything shrinks and paths stretch.
This tool re-maps every element through pixel-space maps you choose per region.

Workflow
  1. In the app: comp.duplicate each comp, comp.move_to_bin to a 'Vertical' bin,
     edit.save. (Do NOT reformat in the app; this tool sets width/height.)
  2. Write a layout spec (example: reformat_example.json) and run
       python reformat.py project.carverproj spec.json
  3. edit.open {path, force:true}; look at every comp; fix by hand what the
     review list prints (full-frame keys, iris sizes, hand-off points).
  4. This tool also renames ids in the duplicated comps so no two timelines share
     clip ids (sharing them made the editor ~6x slower).

Spec (all coordinates in OLD pixels, y UP, origin bottom-left):
{
 "old": [1920,1080], "new": [1080,1920],
 "comps": {
   "<dup timeline id>": {
      "source": "<original timeline id>",          (optional, for reporting)
      "name": "V 02 Visual workspace",              (optional rename)
      "bin": "bin_2",                               (optional)
      "default": {"from": [1286,540], "to": [540,1320], "scale": 0.88},
      "regions": [ {"clips": ["clip_79","clip_80"], "from": [108,650], "to": [130,880], "scale": 1.1} ],
      "keep_fullwidth": true      (rects >= 99% wide keep normalised position, height x new_h/new_w / (old_h/old_w))
   }
 },
 "assemblies": {"<dup assembly id>": {"map": {"tl1":"tl_10"}, "name": "V 00 Full"}}
}
"""
import json, re, sys
sys.path.insert(0, __import__('os').path.dirname(__file__))
import carverproj as cp

SIZE_RE = r'(rectangle_%s\.(width|height|cornerRadius)|ellipse_%s\.(width|height)|stroke_%s\.(width|dashGap|dashLength)|font_%s\.size|layout_%s\.(width|height))$'

def convert(doc, spec):
    OW, OH = spec['old']; NW, NH = spec['new']
    T = {t['id']: t for t in doc['timelines']}
    review = []
    def fullwidth(c):
        k, p = cp.prop(c, 'rectangle.width')
        if not p: return False
        vals = [p.get('static')] + [x['value'] for x in p.get('keyframes', [])]
        return max(v for v in vals if isinstance(v, (int, float))) >= 0.99
    def apply_map(c, M, group_offset=False):
        (ox, oy), (nx, ny), s = M['from'], M['to'], M['scale']
        fw = OW * s / NW; fy = OH * s / NH
        def mpos(a):
            if group_offset: return [0.5 + (a[0] - 0.5) * OW * s / NW, 0.5 + (a[1] - 0.5) * OH * s / NH]
            return [(nx + (a[0] * OW - ox) * s) / NW, (ny + (a[1] * OH - oy) * s) / NH]
        def each(p, f):
            for kf in p.get('keyframes', []):
                if not isinstance(kf['value'], str): kf['value'] = f(kf['value'])
            if p.get('static') is not None and not isinstance(p['static'], (str, bool)): p['static'] = f(p['static'])
        cid = c['id']
        for k, p in c.get('properties', {}).items():
            if not isinstance(p, dict): continue
            if re.search(r'placement_%s\.position$' % re.escape(cid), k): each(p, mpos)
            elif re.search(SIZE_RE % ((re.escape(cid),) * 5), k): each(p, lambda a: a * fw)
        tp = c.get('textProps')
        if tp:
            for kk in ('size', 'boxWidth', 'boxHeight'):
                if isinstance(tp.get(kk), (int, float)): tp[kk] *= fw
        sh = c.get('shape')
        if sh and sh.get('kind') == 'path':
            pts = list(sh['params'].get('points', []))
            for cont in sh['params'].get('contours') or []: pts += cont.get('points', [])
            for pt in pts:
                pt['x'] = 0.5 + (pt['x'] - 0.5) * fw; pt['y'] = 0.5 + (pt['y'] - 0.5) * fy
                for a_, f in (('inX', fw), ('outX', fw), ('inY', fy), ('outY', fy)):
                    if a_ in pt: pt[a_] *= f
    def apply_full(c):
        for k, p in c.get('properties', {}).items():
            if re.search(r'rectangle_%s\.height$' % re.escape(c['id']), k):
                for kf in p.get('keyframes', []): kf['value'] *= (NH / NW) / (OH / OW)
                if isinstance(p.get('static'), (int, float)): p['static'] *= (NH / NW) / (OH / OW)
        review.append('%s: full-width shape %s kept full-frame; check its keyed sizes' % (tl['name'], c['id']))
    def walk(clips, L, inherited=None):
        for c in clips:
            M = inherited
            if not M:
                M = L['default']
                for r in L.get('regions', []):
                    if c['id'] in r['clips']: M = r
            if not inherited and L.get('keep_fullwidth', True) and fullwidth(c) and not c.get('tracks') and c['id'] not in L.get('no_fullwidth', []):
                apply_full(c); continue
            if c.get('tracks'):
                apply_map(c, M, group_offset=True)
                for t in c['tracks']: walk(t['clips'], L, M)
            else:
                apply_map(c, M)
    for tid, L in spec.get('comps', {}).items():
        tl = T[tid]; s = tl['scene']
        s['width'] = s['timelineWidth'] = NW; s['height'] = s['timelineHeight'] = NH
        for tr in s['tracks']: walk(tr['clips'], L)
        if L.get('name'): tl['name'] = L['name']
        if L.get('bin'): tl['bin'] = L['bin']
    for tid, A in spec.get('assemblies', {}).items():
        tl = T[tid]; s = tl['scene']
        s['width'] = s['timelineWidth'] = NW; s['height'] = s['timelineHeight'] = NH
        for c, _, _ in cp.all_clips(tl):
            if c.get('nestedTimelineId') in A['map']: c['nestedTimelineId'] = A['map'][c['nestedTimelineId']]
        if A.get('name'): tl['name'] = A['name']
    for tid in list(spec.get('comps', {})) + list(spec.get('assemblies', {})):
        n = cp.make_ids_unique(doc, tid, prefix='clip%s_' % re.sub(r'\W', '', tid))
        review.append('%s: %d id references renamed (no shared ids across comps)' % (tid, n))
    return review

if __name__ == '__main__':
    proj, specf = sys.argv[1], sys.argv[2]
    doc = cp.load(proj); spec = json.load(open(specf))
    for line in convert(doc, spec): print('review:', line)
    cp.save(doc, proj); print('saved', proj)
