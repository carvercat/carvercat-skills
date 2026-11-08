"""Write the Glitch lab comps in design units (cc2.py: px from the top-left, y down, degrees clockwise, CSS colours and easing).

    import glitch_lab as L; doc = L.build(); doc.send(client, PROJECT.carverproj)   # scene.apply per comp, then edit.save

Rounds 2 and 3 (glitch_lab2.py, glitch_lab3.py) import the helpers defined here: `GDoc` (a Doc that also keys the SECOND drop shadow of an
RGB split, which a scene cannot say), `rgb_split()`, `jolt()`, `held()`, `T()`, `line()` and the pack's presets baked as keys
(`glitch_in()`, `glitch_out()`, `stretch_hit()`). Nothing is applied after `send`.

Glitches are stepped: keys with the Hold ease jump on the frame they arrive. Keep stepped opacity changes small and few (qc: no flashes):
photosensitivity matters most here. Rotation is clockwise degrees (the old kit stored counter-clockwise values).
Fonts: Rethink Sans must be installed (KI-136). Docs: ai/patterns/glitch.md. 1920x1080, 30 fps.
"""
import os, sys, random, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author"))
from cc2 import Doc, css, bezier, BEZ, HOLD

W, H = 1920, 1080
COL = dict(bg=css('0A0A0A'), white=css('F2F2F2'), red=css('FF2A55'), cyan=css('00E5FF'), green=css('39FF14'), grey=css('2A2A2A'))
WEIGHT = dict(Medium=500, SemiBold=600, Bold=700, ExtraBold=800)
TRACK = 1920 / 1146.24      # old tracking 1.0 = normal; px of letter spacing = (tracking - 1) x font size x 1.675
EXPO = BEZ['expo']


class GDoc(Doc):
    """A Doc that can also key the second drop shadow of an object. `shadow_keys(obj, [(frame, x px)], ...)` is collected here and sent
    right after the object's comp is applied, with key.set on the effect's own parameter (a scene keys only the first shadow)."""
    def __init__(self):
        Doc.__init__(self, unparent_masks=True); self.raw = []

    def send(self, client, save_path):
        raws, done = self.raw, set()

        class Proxy:
            def __init__(p, c): p.c = c
            def __getattr__(p, n): return getattr(p.c, n)
            def apply_scene(p, scene, **kw):
                r = p.c.apply_scene(scene, **kw)
                ids = (r.get('scene') or {}).get('ids', {})
                for i, (sid, key, rows) in enumerate(raws):
                    if i in done or sid not in ids: continue
                    done.add(i)
                    cid = ids[sid]
                    for f, v, e in rows:
                        p.c.run('key.set', id=cid, key=key.replace('{id}', cid), at=f, value=v, ease=e)
                return r
        return Doc.send(self, Proxy(client), save_path)


_DOC = [None]


def new_doc():
    _DOC[0] = GDoc(); return _DOC[0]


def lab_bg(k, n):
    k.rect("Lab bg", 0, 0, W, H, COL['bg'], f0=0, dur=n)


def held(spec):
    """[(frame, value)] -> key specs with Hold arriving (stepped jumps)"""
    return [(f, v, 'Linear' if i == 0 else HOLD) for i, (f, v) in enumerate(spec)]


def more(o, key, extra):
    have = [(f + o.f0, v, e) for f, v, e in o.tracks.get(key, [])]
    new = {f for f, *_ in extra}
    return o.key(key, sorted([x for x in have if x[0] not in new] + list(extra), key=lambda s: s[0]))


# ---------------------------------------------------------------- text and paths
_FONTS = {}


def textw(s, px, style='SemiBold'):
    """advance width in px of Rethink Sans text (PIL; within about 5 % of the app)"""
    try:
        from PIL import ImageFont
        key = (round(px * 4), style)
        if key not in _FONTS:
            f = ImageFont.truetype(os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author", "RethinkSans.ttf"), max(1, round(px * 4)))
            f.set_variation_by_name(style.encode()); _FONTS[key] = f
        return _FONTS[key].getlength(s) / 4
    except Exception:
        return len(s) * px * 0.62


def T(k, name, s, x, y, px, col, f0=0, dur=None, style='Bold', align='left', track=None):
    """text with its left (align 'left'), centre or right edge at x and its vertical centre at y; a box as wide as the words, 1.34 lines high"""
    tk = 0.0 if track is None else round((track - 1) * px * TRACK, 3)
    w = max(20, round(textw(s, px, style) + (len(s) - 1) * tk + 0.1 * px, 1))
    cx = x - 0.04 * px + w / 2 if align == 'left' else (x + 0.03 * px - w / 2 if align == 'right' else x)
    o = k.text(name, s, cx, y, px, col, f0=f0, dur=dur, weight=WEIGHT[style], align=align, width=w,
               tracking=None if track is None else tk)
    o.box = (cx, y, w, round(px * 1.34, 2)); o.base = (cx, y)
    return o


def line(k, name, pts, col=None, px=2, f0=0, dur=None, closed=False, fill=None, cap='round', center=None):
    """a path through `pts` (px, y down), its box the path's bounding box (so pos keys, the CENTRE of that box, work). `center`: (x, y)
    moves the path so its box is centred there."""
    if center is not None:
        xs, ys = [p[0] for p in pts], [p[1] for p in pts]
        dx, dy = center[0] - (min(xs) + max(xs)) / 2, center[1] - (min(ys) + max(ys)) / 2
        pts = [(p[0] + dx, p[1] + dy) for p in pts]
    o = k.path(name, bezier(pts, closed), col or '#FFFFFF', px, f0=f0, dur=dur, cap=cap, fill=fill)
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    x0, y0, w, h = min(xs), min(ys), max(xs) - min(xs), max(ys) - min(ys)
    if w < 1: x0, w = x0 - (1 - w) / 2, 1.0
    if h < 1: y0, h = y0 - (1 - h) / 2, 1.0
    o.box = (x0 + w / 2, y0 + h / 2, w, h); o.base = (x0 + w / 2, y0 + h / 2)
    return o


def type_on(o, gap=1.0):
    return o.stagger(by='chars', each=gap, keyframes=[(0, {'opacity': 0}, 'Linear'), (1, {'opacity': 1}, HOLD)])


# ---------------------------------------------------------------- baked glitch moves
def rgb_split(t, events, op=0.85, events2=None):
    """two hard drop shadows (red, cyan) on one text; events = [(frame, px)] of Hold jumps (red goes -px, cyan +px), the last one should
    settle. One text, so no second copy for lint text_overlap. The first shadow is keyed in the scene, the second with key.set."""
    a = '%02X' % round(op * 255)
    px0 = events[0][1]; events2 = events2 or events
    t.set('filter', 'drop-shadow(%gpx 0px 0px %s%s) drop-shadow(%gpx 0px 0px %s%s)' % (-px0, COL['red'], a, events2[0][1], COL['cyan'], a))
    t.key('dropShadow', held([(f, '%gpx 0px 0px %s%s' % (-px, COL['red'], a)) for f, px in events]))
    _DOC[0].raw.append((t.id, 'fx.e_fx_shadow_{id}_2.x', [(f - t.f0, round(px / 1920.0, 6), HOLD) for f, px in events2]))   # key.set counts from the clip start
    return t


def jolt(o, events):
    """held horizontal jumps: events = [(frame, dx px)], the last one should be (f, 0)"""
    bx, by = o.base
    return o.pos(held([(f, (bx + dx, by)) for f, dx in events]))


def glitch_in(o, f=None):
    """Glitch in (12 f): held jumps of +3, -2, +1.2, -0.6, +0.3 % of the width, stepped opacity 0 > 100 > 40 > 100 > 70 > 100 %"""
    f = o.f0 if f is None else f
    bx, by = o.base
    dxs = [(0, 57.6), (2, -38.4), (4, 23.04), (6, -11.52), (8, 5.76), (10, 0.0), (12, 0.0)]
    more(o, 'pos', [(f + a, (bx + dx, by), 'Linear' if a <= 2 else HOLD) for a, dx in dxs])          # the first step eases in (as the stored preset)
    more(o, 'opacity', [(f + a, v, 'Linear' if a <= 2 else HOLD) for a, v in ((0, 0.0), (2, 1.0), (4, 0.4), (6, 1.0), (8, 0.7), (10, 1.0), (12, 1.0))])
    return o


def glitch_out(o, end=None):
    """Glitch out (10 f): growing held jumps (-0.8 ... +4 % of the width) and stepped opacity to 0; the last key is the clip's last frame"""
    end = (o.f0 + o.dur) if end is None else end
    f = end - 11
    bx, by = o.base
    dxs = [(0, 0.0), (2, -15.36), (4, 28.8), (6, -48.0), (8, 76.8), (10, 76.8)]
    more(o, 'pos', [(f + a, (bx + dx, by), 'Linear' if a <= 2 else HOLD) for a, dx in dxs])
    more(o, 'opacity', [(f + a, v, 'Linear' if a <= 2 else HOLD) for a, v in ((0, 1.0), (2, 0.6), (4, 1.0), (6, 0.3), (8, 0.0), (10, 0.0))])
    return o


def stretch_hit(o, f=None, sx=1.0, sy=1.0, preset=True):
    """Glitch stretch hit (8 f): scale 160 x 60 % > 85 x 110 % > 112 x 95 % > 100 %, Hold steps, settles f + 6"""
    f = o.f0 if f is None else f
    more(o, 'scale', [(f + a, [x * sx, y * sy], 'Linear' if a <= (2 if preset else 0) else HOLD) for a, (x, y) in
                      ((0, (1.6, 0.6)), (2, (0.85, 1.1)), (4, (1.12, 0.95)), (6, (1.0, 1.0)), (8, (1.0, 1.0)))])
    return o


def rgb_title(d):
    n = 90
    k = d.comp("GL RGB title", n, "grt"); lab_bg(k, n)
    t = T(k, "Title", "SIGNAL LOST", 960, 540, 170, COL['white'], f0=0, dur=n, style='ExtraBold', align='center')
    glitch_in(t)
    rng = random.Random(7)
    base = [(0, 18), (3, 30), (6, 10), (9, 24), (12, 6), (15, 14)]
    red = base + [(f, rng.choice((4, 6, 8))) for f in range(20, n - 4, 14)]          # each shadow draws its own random sizes, as before
    cyan = base + [(f, rng.choice((4, 6, 8))) for f in range(20, n - 4, 14)]
    rgb_split(t, red, events2=cyan)


def slice_shift(d):
    n = 75
    k = d.comp("GL Slice shift", n, "gss"); lab_bg(k, n)
    cx, cy, size, bands = 960, 540, 460, 5
    bh = size / bands
    rng = random.Random(3)
    for i in range(bands):
        mark = k.ngon(f"Mark {i + 1}", cx, cy, size, 6, COL['green'], f0=0, dur=n)
        mark.stroke(COL['white'], 10, cap='butt')
        bx, by = mark.base
        jumps = [(0, 0)] + [(f, rng.choice((-60, -30, 30, 45, 80)) * (1 if i % 2 else -1)) for f in (12, 15, 18, 21)] + [(24, 0)]
        jumps += [(52, rng.choice((-40, 40))), (55, 0)]
        mark.pos(held([(f, (bx + dx, by)) for f, dx in jumps]))
        top = cy - size / 2 + i * bh
        band = k.rect(f"Band {i + 1}", cx - size, top, size * 2, bh + 1, COL['white'], f0=0, dur=n)
        k.mask(mark, band)


def noise_bars(d):
    n = 60
    k = d.comp("GL Noise bars", n, "gnb"); lab_bg(k, n)
    rng = random.Random(11)
    for i in range(6):
        y = rng.randint(120, 960); h = rng.choice((6, 10, 18, 30)); w = rng.randint(500, 1600)
        col = (COL['white'], COL['cyan'], COL['red'])[i % 3]
        bar = k.rect(f"Noise bar {i + 1}", 0, y, w, h, col, f0=0, dur=n)
        on = sorted(rng.sample(range(2, n - 4, 4), 3))           # 4 f apart: each 2 f blip ends before the next starts
        spec = [(0, 0.0)]
        for f in on: spec += [(f, round(rng.uniform(0.15, 0.35), 2)), (f + 2, 0.0)]
        bar.op(held(spec))
        bx, by = bar.base
        bar.pos(held([(0, (bx, by))] + [(f, (bx + rng.randint(-200, 400), by)) for f in on]))
    track = k.rect("Tracking bar", 0, 0, 1920, 46, COL['white'], f0=0, dur=n)
    track.opv(0.06)
    tx, ty = track.base
    track.pos([(0, (tx, ty - 50), 'Linear'), (n, (tx, ty + 1100), 'Linear')])


def glitch_cut(d):
    n = 30
    k = d.comp("GL Glitch cut", n, "ggc")
    k.rect("Scene A", 0, 0, 1920, 1080, COL['grey'], f0=0, dur=15)
    k.rect("Scene B", 0, 0, 1920, 1080, COL['bg'], f0=15, dur=15)
    rng = random.Random(5)
    for i in range(7):
        y = rng.randint(60, 1000); h = rng.choice((20, 40, 70, 110)); w = rng.randint(900, 1920)
        col = (COL['red'], COL['cyan'], COL['white'])[i % 3]
        f0 = 9 + rng.randint(0, 3); dur = rng.choice((4, 6, 8))
        bar = k.rect(f"Cut bar {i + 1}", rng.randint(0, 1920 - w), y, w, h, col, f0=f0, dur=dur)   # inside the frame
        bx, by = bar.base
        room_l, room_r = int(bx - w / 2), int(1920 - bx - w / 2)
        dx = rng.randint(-min(240, room_l), min(240, room_r)) if w < 1920 else 0
        bar.pos(held([(f0, (bx, by)), (f0 + 2, (bx + dx, by))]))
        bar.opv(0.55)


def build(path=None, m=None):
    d = new_doc()
    rgb_title(d); slice_shift(d); noise_bars(d); glitch_cut(d)
    return d


if __name__ == "__main__":
    print(__doc__)
