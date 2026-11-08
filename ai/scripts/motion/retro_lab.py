"""Retro lab round 1 in design units (cc2.py: px from the top-left, y down, degrees clockwise, CSS colours and easing).

    import retro_lab as L; doc = L.build(); doc.send(client, PROJECT.carverproj)   # scene.apply per comp, preset.apply, edit.save

Four comps: sunburst title, synthwave sun, rainbow stripes, checker wipe. Retro rounds 2 and 3 (retro_lab2.py, retro_lab3.py)
import the helpers below. Check with carvercat_inspect (curves, lint, qc) and carvercat_look; extract templates with
regen_pack.py (the lab comps' "Lab bg" is dropped by name).

"On twos": twos() keys a move on every other frame with the Hold ease (the arriving key jumps), the stepped look of
12-drawings-a-second animation. Fonts: Rethink Sans must be installed (KI-136). Docs: ai/patterns/retro.md.
Design units: 1920 x 1080 px, comp frames, 30 fps; rotation in degrees CLOCKWISE (the old kit stored counter-clockwise:
every angle below is the old one negated).

Presets: PDoc keeps `presets` [(comp, object, preset)] and applies them with preset.apply right after the scene of that comp
is applied (the stored `.carverpreset` files are the app's own presets, they are not rewritten here).
"""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "json_author")); sys.path.insert(0, HERE)
from cc2 import Doc, css, BEZ, HOLD, bezier
from curves import named

W, H = 1920, 1080
COL = dict(cream=css('F4E4C1'), orange=css('E8772E'), mustard=css('E3B23C'), brown=css('5C3A21'), teal=css('2A9D8F'),
           red=css('C8553D'), night=css('1A0B2E'), pink=css('FF2E88'), yellow=css('FFD319'), purple=css('7A2BD8'), cyan=css('2DE2E6'))
EXPO = BEZ['expo']
# the old model's named curves (cc2 maps these names to CSS ease-in / ease-out / ease-in-out, which are different curves)
EASE_IN, EASE_OUT, SCURVE = (1 / 3, 0, 2 / 3, 1 / 3), (1 / 3, 2 / 3, 2 / 3, 1), (1 / 3, 0, 2 / 3, 1)
WEIGHT = dict(Medium=500, SemiBold=600, Bold=700, ExtraBold=800)
LINE = 1.34                                  # the font's default line height, a multiple of the size
HIDE = 0.0                                   # box centre = the old anchor (measured: caps ink centre; the old box hung 0.155 sizes lower)


# ---------------------------------------------------------------- the document: Doc + presets
class PDoc(Doc):
    """A cc2 Doc that also applies stored motion presets: self.presets = [(comp name, object name, preset name)]."""

    PACK = 'retro'                       # the pack whose .carverpreset files the presets come from

    def __init__(self):
        super().__init__(cap_radius=True); self.presets = []       # the old kit's corner cap (cc2 Doc option)

    def preset(self, comp, obj, name):
        self.presets.append((comp.name if hasattr(comp, 'name') else comp, obj.name if hasattr(obj, 'name') else obj, name))

    def send(self, client, save_path):
        if self.presets: self.install_presets(client)
        return super().send(_Presets(client, self), save_path)

    def install_presets(self, client):
        """a fresh host has an empty user Library: copy the pack's .carverpreset files into it and read it again"""
        import shutil
        src = os.path.join(HERE, '..', '..', '..', 'library', 'templates', self.PACK)
        user = client.run('library.reload')['readings'][0]['user']['path']
        dst = os.path.join(user, 'templates', 'presets'); os.makedirs(dst, exist_ok=True)
        for f in os.listdir(src):
            if f.endswith('.carverpreset'): shutil.copy(os.path.join(src, f), dst)
        client.run('library.reload')


class _Presets:
    """client proxy: after a comp's scene is applied, its presets go on (preset.apply takes one object at a time)"""

    def __init__(self, client, doc): self._c, self._d, self._cur, self._done = client, doc, None, set()

    def __getattr__(self, name): return getattr(self._c, name)

    def run(self, cmd, **kw):
        if cmd == 'comp.new': self._cur = kw.get('name')
        return self._c.run(cmd, **kw)

    def apply_scene(self, scene):
        reply = self._c.apply_scene(scene)
        if self._cur and self._cur not in self._done:
            self._done.add(self._cur)
            ids = dict((reply.get('scene') or {}).get('ids', {}))
            comp = next(c for c in self._d.comps if c.name == self._cur)
            byname = {}
            def walk(o): byname[o.name] = o; [walk(k) for k in o.children]
            for o in comp.objs: walk(o)
            for cname, oname, pname in self._d.presets:
                if cname == self._cur: self._c.run('preset.apply', name=pname, id=ids[byname[oname].id])
            for o in byname.values():
                if getattr(o, 'text_grad', None): self._text_gradient(ids[o.id], o)
                for key, val in getattr(o, 'model', {}).items():
                    self._c.run('property.set', id=ids[o.id], key=key.replace('{id}', ids[o.id]), value=val)
        return reply

    def _text_gradient(self, oid, o):
        """a text fill gradient has no design key: it is set on the model (src.e_src_text_fill.*), with each stop's colour
        read back from a solid fill of that hex so it is the exact colour the page states"""
        start, end, stops = o.text_grad
        model = []
        for p, hx in stops:
            self._c.run('property.set', id=oid, key='fill', value=hx)
            v = self._c.run('property.get', id=oid, key='src.e_src_text_fill_%s.color' % oid)['readings'][0]['value']
            model.append({'p': p, 'color': list(v[:3]), 'a': 1})
        self._c.run('property.set', id=oid, key='fill', value=o.style['fill'])
        self._c.run('property.set', id=oid, key='src.e_src_text_fill_%s.paint' % oid, value='gradient')
        self._c.run('property.set', id=oid, key='src.e_src_text_fill_%s.gradient' % oid,
                    value={'mode': 'linear', 'start': list(start), 'end': list(end), 'stops': model})


# ---------------------------------------------------------------- keys on twos, and small object helpers
def lerp(a, b, p):
    return [x + (y - x) * p for x, y in zip(a, b)] if isinstance(a, (list, tuple)) else a + (b - a) * p


def twos(f0, f1, frm, to, curve='expo-out'):
    """key specs [(frame, value, ease)] stepping on even frames (Hold) from f0 to f1"""
    out, f = [], f0
    while f <= f1:
        p = 1.0 if f + 2 > f1 else named[curve]((f - f0) / (f1 - f0))
        out.append((f, lerp(frm, to, p), 'Linear' if not out else 'Hold')); f += 2
    return out


def hold_keys(seq):
    """[(frame, value)] -> Hold-stepped key spec"""
    return [(f, v, 'Linear' if i == 0 else 'Hold') for i, (f, v) in enumerate(seq)]


def anchor(o, ax, ay):
    """pivot in half-sizes as the old kit said it (-1 left/bottom, +1 right/top) -> CSS transform-origin"""
    return o.set('transformOrigin', '%g%% %g%%' % ((ax + 1) * 50, (1 - ay) * 50))


def more(o, key, spec):
    """add keys to a property that already has some (frames are comp frames)"""
    o.tracks[key] = sorted(o.tracks.get(key, []) + [(f - o.f0, v, e) for f, v, e in spec], key=lambda t: t[0]); return o


def glow(o, size=10, amount=0.55, blend=0.2):
    """the old glow size is 1.15 px per unit"""
    return o.glow(round(size * 1.15, 3), amount, blend)


def hard_shadow(o, col, dx, dy):
    """a hard drop shadow (no blur). The old kit read the y offset in frame heights, so dy px of the old call render
    dy x 1080 / 1920 px down: the offsets here are the ones that were verified."""
    return o.shadow(dx, round(dy * H / W, 4), 0, col)


def text(k, name, s, x, y, px, col, f0=0, dur=None, style='Bold', align='center', track=None, lh=None, width=None):
    """Text placed the way the old kit did: x, y is the anchor point (centre x for centred text, the left / right edge for
    left / right text), at the middle of the (middle-aligned) box. `track` is the old tracking (1 = none)."""
    lines = s.split('\n')
    lhr = LINE if lh is None else round(0.8 * lh / 0.597, 4)
    ls = None if not track else round((track - 1) / 0.597 * px, 3)
    try:
        from cc import textw
        wd = max(textw(l, px, style) for l in lines) + (ls or 0) * max(len(l) for l in lines) + 30
    except Exception:
        wd = max(len(l) for l in lines) * px * 0.75 + 30
    wd = int(width or math.ceil(wd))
    h = len(lines) * lhr * px
    cy = y + HIDE * px
    cx = {'center': x, 'left': x - 0.04 * px + wd / 2, 'right': x + 0.02 * px - wd / 2}[align]
    o = k.text(name, s, cx, cy, px, col, f0=f0, dur=dur, weight=WEIGHT[style], align=align, width=wd, tracking=ls)
    o.box = (cx, cy, wd, h); o.base = (cx, cy)
    o.style['lineHeight'] = lhr                       # explicit: an unset line height is the font's own, not 1.34
    return o


def text_gradient(o, stops, start=(0.5, 0.0), end=(0.5, 1.0)):
    """a static linear gradient on a text, object-local, y down ([0.5, 0] = the top of the box); stops [(0..1, '#hex')]"""
    o.text_grad = (start, end, stops); return o


def model_set(o, key, value):
    """a model property with no design key (text outline ...), set after the scene is applied; '{id}' is the app's clip id"""
    if not hasattr(o, 'model'): o.model = {}
    o.model[key] = value; return o


def fit_box(o, pts):
    """a path's box is the tight box of its points (at least 1 px, as the app measures it), and its x / y keys are that box's
    absolute top-left: tell cc2 the box so a position key given as a centre lands right"""
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    w, h = max(max(xs) - min(xs), 1.0), max(max(ys) - min(ys), 1.0)
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    o.box = (cx, cy, w, h); o.base = (cx, cy); return o


def line(k, name, pts, col, px=2, f0=0, dur=None):
    """an open stroked path through pts [(x, y)]; scale, turn and trim go about the middle of its box"""
    return fit_box(k.path(name, bezier(pts), col, px, f0=f0, dur=dur), pts)


def lab_bg(k, n, col=None):
    k.rect("Lab bg", 0, 0, W, H, col or COL['cream'], f0=0, dur=n)


# ---------------------------------------------------------------- the lab comps
def sunburst(d):
    n = 90
    k = d.comp("RT Sunburst title", n, "rsb"); lab_bg(k, n)
    rays = k.star("Rays", 960, 540, 2600, 24, 0.12, COL['mustard'], f0=0, dur=n)
    rays.rot([(0, 0.0, 'Linear'), (n, -15.0, 'Linear')])
    rays.op(twos(0, 8, 0.0, 0.55, 'linear'))
    t = text(k, "Title", "SINCE 1975", 960, 520, 160, COL['brown'], f0=6, dur=n - 6, style='ExtraBold')
    hard_shadow(t, COL['orange'], 10, 10)
    d.preset(k, t, "Pop - on twos")
    s = text(k, "Subtitle", "FAMILY RECIPES", 960, 650, 44, COL['brown'], f0=14, dur=n - 14, style='SemiBold', track=1.4)
    d.preset(k, s, "Rise - on twos")


def synthwave(d):
    n = 120
    k = d.comp("RT Synthwave", n, "rsw"); lab_bg(k, n, COL['night'])
    hy = 640
    sun = k.ell("Sun", 960, 440, 520, 520, COL['pink'], f0=0, dur=n)
    sun.gradient([(0.0, COL['yellow']), (1.0, COL['pink'])], (960, 180), (960, 700))
    sun.scale(twos(0, 16, 0.0, 1.0, 'expo-out'))
    for i in range(5):                                     # bands cut through the lower half, drifting up one way
        y = 520 + i * 34; h = 6 + i * 4
        bnd = k.rect(f"Band {i + 1}", 960, y, 600, h, COL['night'], f0=0, dur=n, center=True)
        bnd.pos([(0, (960, y), 'Linear'), (n, (960, y - 24), 'Linear')])
    k.rect("Floor", 0, hy, W, H - hy, COL['night'], f0=0, dur=n)
    glow(line(k, "Horizon", [(0, hy), (W, hy)], COL['pink'], 4, f0=0, dur=n), 10, 0.6)
    for i, xb in enumerate((-600, 0, 480, 960, 1440, 1920, 2520)):
        end = (xb, H)
        if xb < 0: end = (0, hy + (H - hy) * 960 / (960 - xb))              # stop at the frame edge (lint: cropped at rest)
        if xb > 1920: end = (1920, hy + (H - hy) * 960 / (xb - 960))
        gl = line(k, f"Grid V{i + 1}", [(960, hy), end], COL['purple'], 3, f0=0, dur=n)
        gl.trim([(0, 0.0, 'Linear'), (20, 1.0, EXPO)], which='end')
    for i in range(6):                                     # horizontal grid lines run toward the viewer, accelerating
        f0 = i * 20; f1 = f0 + 40
        if f1 > n: break                                   # every line finishes its run inside the comp
        hl = line(k, f"Grid H{i + 1}", [(0, hy + 4), (W, hy + 4)], COL['purple'], 3, f0=f0, dur=min(n, f1) - f0)
        bx, by = hl.base
        hl.pos([(f0, (bx, by), 'Linear'), (f1, (bx, by + (H - hy)), EASE_IN)])   # down the screen, toward the viewer
    t = text(k, "Title", "NEON NIGHTS", 960, 860, 120, COL['cyan'], f0=20, dur=n - 20, style='ExtraBold', track=1.2)
    d.preset(k, t, "Rise - on twos")


def stripes(d):
    n = 75
    k = d.comp("RT Rainbow stripes", n, "rrs"); lab_bg(k, n)
    for i, col in enumerate((COL['red'], COL['orange'], COL['mustard'], COL['teal'])):
        y = 600 + i * 30; f = i * 4
        s = k.rect(f"Stripe {i + 1}", 960, y, W, 26, col, f0=0, dur=n, center=True)
        anchor(s, -1, 0); s.scale(twos(f, f + 16, [0.0, 1.0], [1.0, 1.0], 'expo-out'))
    t = text(k, "Title", "GROOVE RADIO", 960, 460, 150, COL['brown'], f0=14, dur=n - 14, style='ExtraBold')
    d.preset(k, t, "Rise - on twos")


def checker_wipe(d):
    n = 54                                                # the last diagonal (a = 22) is gone by f52
    k = d.comp("RT Checker wipe", n, "rcw"); lab_bg(k, n)
    cols, rows, w, h = 8, 5, 240, 216
    for r in range(rows):
        for c in range(cols):
            sq = k.rect(f"Square {r + 1}-{c + 1}", c * w + w / 2, r * h + h / 2, w + 1, h + 1,
                        COL['brown'] if (r + c) % 2 else COL['orange'], f0=0, dur=n, center=True)
            a = (r + c) * 2                               # the diagonal order
            sq.scale(twos(a, a + 6, 0.0, 1.0, 'expo-out') + twos(a + 24, a + 30, 1.0, 0.0, 'accel')[1:])   # covered f22-30


def comps(d):
    sunburst(d); synthwave(d); stripes(d); checker_wipe(d)


def build():
    d = PDoc(); comps(d)
    return d


if __name__ == "__main__":
    print(__doc__)
