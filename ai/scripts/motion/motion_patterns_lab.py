"""Motion Patterns lab comps in design units (cc2.py: px, y down, degrees clockwise, '#RRGGBB', CSS easing, frames).

    import motion_patterns_lab as L; doc = L.build(); doc.send(client, PROJECT.carverproj)

Group 1 (templates): the five comps the pack's templates are extracted from. Their names slug to the template file stems
(`MP TR iris` -> mp_tr_iris), which is how regen_templates.py finds them. The instance-face parameters of the old templates
(colours, text) are raised again after the apply (MPDoc.send, `param.raise`).
Text is Open Sans, as in the v1 templates.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author"))
from cc2 import Doc, css, BEZ, HOLD

W, H = 1920, 1080
BG, ACCENT, BRAND, PAPER, WHITE = css('070912'), css('F9B71E'), css('173695'), css('F2F2EF'), css('FFFFFF')
EXPO, ACCEL, STD, INOUT = BEZ['expo'], BEZ['accel'], BEZ['std'], BEZ['inout']
EASE_IN = (1 / 3, 0, 2 / 3, 1 / 3)       # the old kit's "Ease in" / "Ease out", as the app reads them
EASE_OUT = (1 / 3, 2 / 3, 2 / 3, 1)
SPRING_UP = (0.2, 0.0, 0.4, 1.0)         # first leg of a gentle spring: to the overshoot peak
SPRING_STAMP = (0.35, 0.2, 0.35, 1.0)
FONT = 'Open Sans'
POST = {}                                 # (comp name, object name) -> anim.set key lists sent after the apply
FACE = {}                                 # comp name -> [(object name, 'fill' | 'content')] raised onto the instance face


def otext(k, name, s, left, top, px, col, width, weight=700, f0=0, dur=None):
    """Left-aligned Open Sans text whose box starts at (left, top); one line, line height 1.34."""
    h = round(px * 1.34)
    t = k.text(name, s, left + width / 2, top + h / 2, px, col, f0=f0, dur=dur, weight=weight, family=FONT, align='left', width=width)
    t.box = (left + width / 2, top + h / 2, width, h); t.base = (t.box[0], t.box[1]); t.set('lineHeight', 1.34)
    return t


def ctext(k, name, s, cx, top, px, col, width, weight=700, f0=0, dur=None, tracking=None):
    h = round(px * 1.34)
    t = k.text(name, s, cx, top + h / 2, px, col, f0=f0, dur=dur, weight=weight, family=FONT, width=width, tracking=tracking)
    t.box = (cx, top + h / 2, width, h); t.base = (cx, top + h / 2); t.set('lineHeight', 1.34)
    return t


def stand_ins(k, n, cut, b=None):
    a = k.rect('Scene A', 0, 0, W, H, BG, f0=0, dur=cut)
    s = k.rect('Scene B', 0, 0, W, H, b or PAPER, f0=cut, dur=n - cut)
    return a, s


# ---------------------------------------------------------------- templates
def two_tone_wipe(d):
    n = 48
    k = d.comp('MP TR Two-Tone Wipe', n, 'mtt'); stand_ins(k, n, 24)
    for name, col, f0, ks in (('Wipe 1 (accent)', ACCENT, 12, (12, 22, 28, 41)), ('Wipe 2 (brand)', BRAND, 14, (15, 24, 25, 36))):
        p = k.rect(name, -19.2, -16.8, 1958.4, 1113.6, col, f0=f0, dur=(30 if f0 == 12 else 23))   # 2 % bigger than the frame: no seam
        bx, by = p.base; off = 1958.4
        p.pos([(ks[0], (bx - off, by), 'Linear'), (ks[1], (bx, by), EASE_IN), (ks[2], (bx, by), 'Linear'), (ks[3], (bx + off, by), EASE_OUT)])
    FACE[k.name] = [('Wipe 1 (accent)', 'fill'), ('Wipe 2 (brand)', 'fill')]


def iris(d):
    n = 48
    k = d.comp('MP TR Iris', n, 'mir'); stand_ins(k, n, 30, ACCENT)
    c = k.ell('Iris (Scene B colour)', 960, 540, 1056, 1056, ACCENT, f0=12, dur=19)
    c.scale([(12, 0.0, 'Linear'), (30, 2.2, INOUT)])
    FACE[k.name] = [('Iris (Scene B colour)', 'fill')]


def logo_stamp_reveal(d):
    n = 90
    k = d.comp('MP Logo stamp reveal', n, 'mlg')
    k.rect('Background', 0, 0, W, H, BG, f0=0, dur=n)
    m = k.ell('Logo mark', 960, 432, 384, 384, ACCENT, f0=4, dur=84)
    m.scale([(4, 1.045, 'Linear'), (12, 0.527, SPRING_STAMP), (18, 0.55, EXPO)])      # stamp: slams from 190 % of 0.55, one small rebound
    m.op([(4, 0.0, 'Linear'), (7, 1.0, 'Linear')])
    w = ctext(k, 'Wordmark', 'CARVERCAT', 960.1, 633.69, 86, WHITE, 760, f0=12, dur=76, tracking=21.6)
    # (the text positions are set so the drawn letters land where the v1 template's did: the harness compares ink boxes)
    # every letter plays this tween, 2 f after the one before (the ease on a row leads out of it): it drops in from 38 px above the rest
    # position (y values here are the text's top edge in px: the last row is where it rests), overshoots by 1.7 px and settles; the fade rides the same first leg
    w.stagger(by='chars', each=2, keyframes=[(0, {'opacity': 0.0, 'y': 595.69}, SPRING_UP), (11, {'opacity': 1.0, 'y': 635.39}, EXPO), (20, {'y': 633.69}, None)])
    u = k.rect('Underline', 749, 773.76, 422.4, 7.68, ACCENT, f0=20, dur=70)
    u.set('transformOrigin', '0% 50%')                       # draws from its left edge
    u.scale([(20, [0.0, 1.0], 'Linear'), (38, [1.0, 1.0], EXPO)])
    FACE[k.name] = [('Logo mark', 'fill'), ('Wordmark', 'content'), ('Underline', 'fill')]


def lt_accent_bar(d):
    n = 120
    k = d.comp('MP LT Accent bar', n, 'mlt')
    k.rect('Background', 0, 0, W, H, css('303641'), f0=0, dur=n)
    b = k.rect('LT bar', 167.04, 792, 11.52, 144, ACCENT, f0=6, dur=96)
    b.scale([(6, [1.0, 0.0], 'Linear'), (22, [1.0, 1.0], EXPO), (92, [1.0, 1.0], 'Linear'), (101, [1.0, 0.0], EASE_IN)])
    r = otext(k, 'LT role', 'Senior Motion Designer', 196.0, 873.94, 29.8, css('DDDDDD'), 520, weight=400, f0=13, dur=88)
    cy = r.base[1]
    r.pos([(13, (r.base[0], cy + 48.6), 'Linear'), (31, (r.base[0], cy), EXPO)])
    r.op([(13, 0.0, 'Linear'), (21, 1.0, STD), (92, 1.0, 'Linear'), (100, 0.0, ACCEL)])
    nm = otext(k, 'LT name', 'Alex Morgan', 196.0, 814.44, 51.6, WHITE, 520, f0=9, dur=92)
    cx, cy = nm.base
    # entrance: every word rises on its own (the stagger tween); the exit moves the whole name, as the v1 template did
    nm.stagger(by='words', each=3, keyframes=[(0, {'opacity': 0.0, 'y': 846.84}, EXPO), (16, {'opacity': 1.0, 'y': 814.44}, None)])
    POST[(k.name, 'LT name')] = [[dict(at=79, y=814.44, ease='cubic-bezier(0.3, 0, 0.8, 0.15)'), dict(at=91, y=868.44)],
                                 [dict(at=79, opacity=1.0, ease='cubic-bezier(0.3, 0, 0.8, 0.15)'), dict(at=91, opacity=0.0)]]
    FACE[k.name] = [('LT bar', 'fill'), ('LT role', 'content'), ('LT name', 'content')]


def info_bar_chart(d):
    n = 120
    k = d.comp('MP INFO Bar chart', n, 'mib')
    k.rect('Background', 0, 0, W, H, BG, f0=0, dur=n)
    bl = k.rect('Baseline', 538, 807.12, 864, 2.88, css('8A8A8A'), f0=0, dur=n)
    bl.set('transformOrigin', '0% 50%')
    bl.scale([(0, [0.0, 1.0], 'Linear'), (18, [1.0, 1.0], EXPO)])
    for i, (x, top, h) in enumerate(((566.4, 578.6, 230.4), (783.4, 463.4, 345.6), (1002.2, 348.2, 460.8), (1219.2, 156.2, 652.8))):
        f0 = 6 + 3 * i
        hero = i == 3
        b = k.rect('Bar %d%s' % (i + 1, ' (hero)' if hero else ''), x, top, 134.4, h, ACCENT if hero else css('7D7D85'), f0=f0, dur=n - f0)
        b.set('transformOrigin', '50% 100%')
        b.scale([(f0, [1.0, 0.0], 'Linear'), (f0 + 16, [1.0, 1.0], EXPO)])
    FACE[k.name] = [('Bar 4 (hero)', 'fill')]


# ---------------------------------------------------------------- group 2: benches, recipes, template test, stored demo scenes
import json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cc2 import Comp

SPRING_PEAK = (0.2, 0.0, 0.4, 1.0)

BENCH = [  # (preset name, rect centre) on "Preset bench": every object preset of the pack is applied in MPDoc.send
]
OBJ_PRESETS = ['Rise - expo', 'Pop - spring', 'Pop - gentle', 'Stamp', 'Drop - bounce', 'Swing in', 'Flip in (X)',
               'Exit shrink - anticipate', 'Exit zoom through']
TEXT_PRESETS = [('Motion that feels made by hand', 'Words rise - expo', 104, 54), ('Cascade', 'Letters cascade - spring', 80, 217),
                ('Pop goes every word', 'Words pop - spring', 80, 368), ('Line one reveals\nthen line two', 'Lines reveal - decelerate', 69, 512),
                ('Quiet shimmer', 'Letters shimmer in', 80, 736), ('Swing those words', 'Words swing in', 80, 895)]
S_CURVE = 'cubic-bezier(0.333333, 0, 0.666667, 1)'
EASE_IN_CSS = 'cubic-bezier(0.333333, 0, 0.666667, 0.333333)'
# keys scene.get does not report for a comp instance (the camera's zoom on the Dubai base map), read from the v1 comp
INSTANCE_EXTRA = {'Map camera (Dubai base)': [[
    dict(at=62, scale=1.0, ease=S_CURVE), dict(at=94, scale=1.9, ease='steps(1, jump-end)'), dict(at=116, scale=1.9, ease=S_CURVE),
    dict(at=146, scale=1.0, ease='linear'), dict(at=226, scale=1.0, ease=EASE_IN_CSS), dict(at=240, scale=1.06)]]}
PRESETS = {}      # comp name -> [(object name, preset name)] applied after the scene


def preset_bench(d):
    k = d.comp('Preset bench', 60, 'mpb')
    k.rect('Background', 0, 0, W, H, BG, f0=0, dur=60)
    PRESETS[k.name] = []
    for i, pn in enumerate(OBJ_PRESETS):
        r = k.rect('Bench %d' % (i + 1), 960, 540, 384, 384, css('DB0000'), f0=0, dur=60)
        PRESETS[k.name].append((r.name, pn))


def text_lab(d):
    k = d.comp('Text Lab', 90, 'mtl')
    k.rect('Background', 0, 0, W, H, BG, f0=0, dur=90)
    PRESETS[k.name] = []
    for s, pn, px, top in TEXT_PRESETS:
        t = ctext(k, s.split('\n')[0], s, 960, top, px, WHITE, 1800 if px > 100 else 1100, weight=700 if px > 100 else 400, f0=0, dur=90)
        if '\n' in s: t.set('height', round(px * 1.34) * 2); t.box = (960, top + round(px * 1.34), 1100, round(px * 1.34) * 2)
        PRESETS[k.name].append((t.name, pn))
    t = ctext(k, 'Words leave', 'Words leave upward', 960, 1005, 50, WHITE, 900, weight=400, f0=0, dur=90)
    PRESETS[k.name].append((t.name, 'Words exit up'))


def recipes(d):
    k = d.comp('RECIPES', 200, 'mrc')
    k.rect('Background', 0, 0, W, H, BG, f0=0, dur=200)
    PUSH = (0.7, 0.0, 0.2, 1.0)
    a = k.rect('Push A', 0, 0, W, H, BRAND, f0=0, dur=32)
    a.pos([(16, (960, 540), 'Linear'), (31, (-960, 540), PUSH)])
    b = k.rect('Push B', 0, 0, W, H, ACCENT, f0=16, dur=32)
    b.pos([(16, (2880, 540), 'Linear'), (31, (960, 540), PUSH)])
    za = ctext(k, 'Zoom A', 'BEFORE', 958, 480, 115, WHITE, 700, f0=48, dur=20)
    za.scale([(55, 1.0, 'Linear'), (67, 2.4, ACCEL)]); za.op([(55, 1.0, 'Linear'), (60, 1.0, 'Linear'), (67, 0.0, ACCEL)])
    zb = ctext(k, 'Zoom B', 'AFTER', 959, 480, 115, ACCENT, 700, f0=68, dur=26)
    zb.scale([(68, 1.22, 'Linear'), (88, 1.0, EXPO)]); zb.op([(68, 0.0, 'Linear'), (76, 1.0, STD)])
    for name, x, f0, dur, col, rot, hero in (('Card 1', 499.2, 100, 50, css('535765'), -4.0, False), ('Card 2', 768.0, 104, 46, css('6F7280'), 0, False),
                                             ('Card 3 (hero)', 1036.8, 108, 42, ACCENT, 4.0, True)):
        c = k.rect(name, x, 290.4, 384, 499.2, col, r=2.3, f0=f0, dur=dur)
        if rot: c.rotv(rot)
        if hero:
            c.scale([(f0, 0.0, 'Linear'), (f0 + 8, 1.162, SPRING_STAMP), (f0 + 15, 0.98, INOUT), (f0 + 24, 1.0, EXPO)]); c.op([(f0, 0.0, 'Linear'), (f0 + 5, 1.0, 'Linear')])
        else:
            c.scale([(f0, 0.6, 'Linear'), (f0 + 11, 1.018, SPRING_PEAK), (f0 + 20, 1.0, EXPO)]); c.op([(f0, 0.0, 'Linear'), (f0 + 7, 1.0, STD)])
    h = k.rect('Highlight', 672, 482.4, 576, 115.2, ACCENT, f0=156, dur=44)
    h.set('transformOrigin', '0% 50%'); h.scale([(156, [0.0, 1.0], 'Linear'), (174, [1.0, 1.0], EXPO)])
    t = ctext(k, 'Highlighted text', 'Made to move', 958, 497.99, 80, BG, 700, f0=150, dur=50)
    cx, cy = t.base
    t.pos([(150, (cx, cy + 32.4), 'Linear'), (166, (cx, cy), EXPO)]); t.op([(150, 0.0, 'Linear'), (158, 1.0, STD)])
    t.stagger(by='words', each=3)


def template_test(d):
    k = d.comp('Template Test', 300, 'mtt2')
    comps = {c.name: c for c in d.comps}
    k.nest(comps['MP LT Accent bar'], 'Lower third - accent bar', f0=0, dur=102)
    k.nest(comps['MP Logo stamp reveal'], 'Logo - stamp reveal', f0=0, dur=90)


def clip_keys(ks, fr):
    """Rows (frames relative to the object) that start before 0: cut at frame 0 with the value the first segment has reached there."""
    import re
    from curves import bezier
    ks = sorted(ks, key=lambda k: fr(k['at']))
    out, props = [], {}
    def mix(a, b, p):
        if isinstance(a, list): return [mix(x, y, p) for x, y in zip(a, b)]
        if isinstance(a, str) and a.endswith('%'): return '%g%%' % (float(a[:-1]) + (float(b[:-1]) - float(a[:-1])) * p)
        return a + (b - a) * p
    i = 0
    while i + 1 < len(ks) and fr(ks[i + 1]['at']) <= 0: i += 1
    a, b = ks[i], ks[min(i + 1, len(ks) - 1)]
    t = (0 - fr(a['at'])) / max(1, fr(b['at']) - fr(a['at'])) if b is not a else 0
    m = re.match(r'cubic-bezier\(([^)]*)\)', a.get('ease', ''))
    pr = bezier(*[float(x) for x in m.group(1).split(',')])(t) if m else t
    first = {'at': '0f', 'props': {k: mix(v, b['props'].get(k, v), pr) for k, v in a['props'].items()}}
    if a.get('ease'): first['ease'] = a['ease']
    return [first] + [k for k in ks[i + 1:] if fr(k['at']) > 0]


class RawComp(Comp):
    """A comp stored as a design-unit scene document (scene.get output of the original lab comp).
    Three things scene.get writes that scene.apply does not take back as they are are adjusted when it is sent:
    point-text boxes, two key rows on one frame, keys before the object starts (the object then starts earlier, its look
    is unchanged because the earliest key holds the hidden state), nested children (sent flat at their world position and
    parented after the apply, see MPDoc.send) and comp instances (placed with Comp.nest)."""
    def __init__(self, doc, name, scene):
        c = scene['comp']
        super().__init__(doc, name, int(str(c['duration']).rstrip('f')), 'raw', width=int(c['width']), height=int(c['height']), fps=int(c['fps']))
        self._scene = scene
        self.pairs = []          # (parent name, [child names]) to parent after the apply
        self.instances = []      # (instance name, scene node) to key after the apply
        for n in scene['children']:
            if n.get('type') == 'comp':
                src = next(x for x in doc.comps if x.name == n['name'].split('(')[-1].rstrip(')').replace('Dubai base', 'MAP Dubai base') or x.name == n['name'])
                self.nest(src, n['name'], f0=int(str(n.get('start', '0f')).rstrip('f')), dur=int(str(n['duration']).rstrip('f')))
                self.instances.append((n['name'], n))

    def scene(self):
        import copy
        sc = copy.deepcopy(self._scene)
        fr = lambda v: int(str(v).rstrip('f'))
        def flat(n, ox, oy, out):
            st = n.get('style', {})
            kids = n.pop('children', [])
            if ox or oy:
                st['x'] = st.get('x', 0.0) + ox; st['y'] = st.get('y', 0.0) + oy
            out.append(n)
            for ch in kids: flat(ch, st.get('x', 0.0), st.get('y', 0.0), out)
            if kids: self.pairs.append((n['name'], [c['name'] for c in kids]))
        def fix(n):
            n['id'] = 'r_' + str(n['id'])            # the stored ids clash with the ids the app hands out
            st = n.get('style', {})
            if n.get('type') == 'text' and st.get('whiteSpace') != 'normal': st.pop('width', None); st.pop('height', None)
            rows = {}
            for k in n.get('keyframes', []):          # one row per frame: merge rows that share a frame
                r = rows.setdefault(k['at'], {'at': k['at'], 'props': {}})
                r['props'].update(k['props'])
                if k.get('ease') and not r.get('ease'): r['ease'] = k['ease']
            if rows:
                ks = list(rows.values())
                lo = min(fr(k['at']) for k in ks)
                if lo < 0:                            # keys before the object starts: the object shows the value the keys have reached at its first frame
                    n['keyframes'] = ks = clip_keys(ks, fr)
                n['keyframes'] = ks
            end = fr(n.get('start', '0f')) + fr(n['duration'])
            if end > self.length: n['duration'] = '%df' % (self.length - fr(n.get('start', '0f')))
        self.pairs = []
        out = []
        for n in sc['children']:
            if n.get('type') == 'comp': continue
            flat(n, 0.0, 0.0, out)
        for n in out: fix(n)
        sc['children'] = out
        return sc


def stored_demos(d):
    data = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'motion_patterns_scenes.json')))
    for name, sc in data.items():
        c = RawComp(d, name, sc); d.comps.append(c)


def install_presets(client):
    """Copy the pack's presets into the scratch user Library of this host and reload (used to apply them to the benches)."""
    import shutil
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, '..', '..', '..', 'library', 'templates', 'motion-patterns')
    folder = client.run('library.folder').get('readings', [{}])[0].get('path') or client.run('library.folder').get('path')
    dst = os.path.join(folder, 'templates', 'motion-patterns'); os.makedirs(dst, exist_ok=True)
    for f in os.listdir(src):
        if f.endswith(('.carverpreset', '.carverpack')): shutil.copy(os.path.join(src, f), dst)
    client.run('library.reload')


TEMPLATE_COMPS = (two_tone_wipe, iris, logo_stamp_reveal, lt_accent_bar, info_bar_chart)


class MPDoc(Doc):
    """Doc that raises the old templates' face parameters after the apply (see FACE)."""
    def send(self, client, save_path):
        # Object ids repeat from comp to comp (clip_3 ...) and param.raise resolves an id across the document, so the template comps
        # are made and raised first, before any other comp exists; the rest follows.
        everything = self.comps
        first = [c for c in everything if c.name in FACE or c.name == 'Template Test']
        self.comps = first
        Doc.send(self, client, save_path)
        lst = client.tool('carvercat_list')
        comps = {c['name']: c['index'] for c in lst['comps']}
        for cname, items in FACE.items():
            if cname not in comps: continue
            client.run('comp.switch', comp=comps[cname])
            objs = {o['name']: o['id'] for o in client.tool('carvercat_list')['objects']}
            for oname, kind in items:
                oid = objs.get(oname)
                if not oid: continue
                path = ('src.e_src_text_content_%s.content' if kind == 'content' else 'src.e_src_shape_fill_%s.color') % oid
                client.run('param.raise', id=oid, path=path, up=True, check=False)
        for (cname, oname), lists in POST.items():
            client.run('comp.switch', comp=comps[cname])
            oid = {o['name']: o['id'] for o in client.tool('carvercat_list')['objects']}[oname]
            for rows in lists: client.run('anim.set', id=oid, keyframes=rows)
        self.comps = [c for c in everything if c not in first]
        Doc.send(self, client, save_path)
        self.comps = everything
        lst = client.tool('carvercat_list')
        comps = {c['name']: c['index'] for c in lst['comps']}
        for c in self.comps:
            if not isinstance(c, RawComp): continue
            client.run('comp.switch', comp=comps[c.name])
            objs = {o['name']: o['id'] for o in client.tool('carvercat_list')['objects']}
            for parent, kids in reversed(c.pairs):                      # deepest parents first
                client.run('parent.assign', ids=[objs[parent]] + [objs[k] for k in kids], check=False)
            for iname, node in c.instances:
                iid = objs.get(iname)
                if not iid: continue
                st = node.get('style', {})
                if 'transformOrigin' in st: client.run('property.set', id=iid, key='transformOrigin', value=st['transformOrigin'], check=False)
                rows = [dict(at=k['at'], ease=k.get('ease', 'linear'), **k['props']) for k in node.get('keyframes', [])]
                if rows: client.run('anim.set', id=iid, keyframes=rows, check=False)
                for extra in INSTANCE_EXTRA.get(iname, []):
                    client.run('anim.set', id=iid, keyframes=extra, check=False)
        if PRESETS:
            install_presets(client)
            for cname, items in PRESETS.items():
                if cname not in comps: continue
                client.run('comp.switch', comp=comps[cname])
                objs = {o['name']: o['id'] for o in client.tool('carvercat_list')['objects']}
                for oname, pname in items:
                    client.run('select.clip', id=objs[oname], check=False)
                    client.run('preset.apply', name=pname, id=objs[oname])
        client.run('edit.save', path=save_path)
        return save_path


def build(path=None, m=None):
    d = MPDoc()
    for f in TEMPLATE_COMPS: f(d)
    preset_bench(d); text_lab(d); recipes(d); template_test(d); stored_demos(d)
    return d


if __name__ == '__main__':
    print(__doc__)
