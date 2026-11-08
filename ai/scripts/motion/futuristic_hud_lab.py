"""Write the Futuristic HUD lab comps in design units (cc2.py: px from the top-left, y down, degrees clockwise, CSS colours and easing).

    import futuristic_hud_lab as L; doc = L.build(); doc.send(client, PROJECT.carverproj)   # scene.apply per comp, then edit.save

Round 1: reticle, brackets, readout, radar. Rounds 2 and 3 (futuristic_hud_lab2.py, futuristic_hud_lab3.py) import the helpers
defined here: `line()` (a stroked path whose box is its true bounding box, so position keys work), `T()` (text placed by its left,
centre or right edge), the baked presets `flick()`, `scan_open()`, `power_down()`, `exit_fade()`, `type_on()` and `draw()`.

Every move is baked as keys (the pack's presets, applied in the old kit after the project was written, are keys here), so nothing is
run after `send`. Geometry: an ellipse's stroke path starts at 3 o'clock; rotation is clockwise degrees (the old kit stored
counter-clockwise values, which are negated here). Glow amount stays <= 0.8.
Fonts: Rethink Sans must be installed (KI-136). Docs: ai/patterns/futuristic-hud.md. 1920x1080, 30 fps.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author"))
from cc2 import Doc, css, bezier, BEZ, HOLD

W, H = 1920, 1080
COL = dict(bg=css('05080F'), cyan=css('35E0FF'), dim=css('0E6F86'), amber=css('FFB020'), white=css('E6FBFF'), grid=css('0F2A36'))
EXPO = BEZ['expo']
# the old app's named curves (cc2 maps the names to CSS curves that differ): Ease out, S-curve
EASE_OUT = (1 / 3, 2 / 3, 2 / 3, 1)
S_CURVE = (1 / 3, 0, 2 / 3, 1)
WEIGHT = dict(Medium=500, SemiBold=600, Bold=700, ExtraBold=800)
TRACK = 1920 / 1146.24      # old tracking 1.0 = normal; px of letter spacing = (tracking - 1) x font size x 1.675 (read back from the v1 templates)


ORIGINS = []     # [(scene id, transformOrigin)] set with property.set after the scene is applied (a scene cannot give a path its own pivot)


class HDoc(Doc):
    """A Doc whose mask pass lets go of the parenting it creates (cc2 unparent_masks), and which sets the pivots in ORIGINS that a scene
    cannot give a path"""
    def __init__(self):
        super().__init__(unparent_masks=True)

    def send(self, client, save_path):
        class Proxy:
            def __init__(p, c): p.c = c
            def __getattr__(p, n): return getattr(p.c, n)
            def apply_scene(p, scene, **kw):
                r = p.c.apply_scene(scene, **kw)
                ids = (r.get('scene') or {}).get('ids', {})
                for sid, origin in ORIGINS:
                    if sid in ids: p.c.run('property.set', id=ids[sid], key='transformOrigin', value=origin)
                return r
        return Doc.send(self, Proxy(client), save_path)


def bez_val(b, t):
    """value of a CSS cubic-bezier(x1, y1, x2, y2) easing at time fraction t"""
    x1, y1, x2, y2 = b
    lo, hi = 0.0, 1.0
    for _ in range(50):
        u = (lo + hi) / 2
        x = 3 * (1 - u) ** 2 * u * x1 + 3 * (1 - u) * u * u * x2 + u ** 3
        if x < t: lo = u
        else: hi = u
    u = (lo + hi) / 2
    return 3 * (1 - u) ** 2 * u * y1 + 3 * (1 - u) * u * u * y2 + u ** 3


def lane_val(spec, f, ease_map):
    """value of an animated number lane [(frame, value, arriving ease name)] at frame f (an ease is a cubic-bezier tuple)"""
    if f <= spec[0][0]: return spec[0][1]
    for (f0, v0, _), (f1, v1, e) in zip(spec, spec[1:]):
        if f <= f1:
            b = e if isinstance(e, tuple) else ease_map.get(e, (0, 0, 1, 1)); t = (f - f0) / (f1 - f0)
            return v0 + (v1 - v0) * bez_val(b, t)
    return spec[-1][1]


def lab_bg(k, n):
    k.rect("Lab bg", 0, 0, W, H, COL['bg'], f0=0, dur=n)


# ---------------------------------------------------------------- shapes and text
def _bbox(pts, handles):
    """bounding box of a stroked path's centre line: (x, y, w, h); a zero extent counts as 1 px, as the app reads it"""
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    for i in range(len(pts) - 1):
        hout = handles[i][1] if handles else (0, 0)
        hin = handles[i + 1][0] if handles else (0, 0)
        if not (hout[0] or hout[1] or hin[0] or hin[1]): continue
        a, b = pts[i], pts[i + 1]
        c1 = (a[0] + hout[0], a[1] + hout[1]); c2 = (b[0] + hin[0], b[1] + hin[1])
        for ax in (0, 1):
            p0, p1, p2, p3 = a[ax], c1[ax], c2[ax], b[ax]
            qa, qb, qc = -p0 + 3 * p1 - 3 * p2 + p3, 2 * (p0 - 2 * p1 + p2), p1 - p0
            roots = []
            if abs(qa) < 1e-9:
                if abs(qb) > 1e-9: roots = [-qc / qb]
            else:
                disc = qb * qb - 4 * qa * qc
                if disc >= 0: roots = [(-qb + s * math.sqrt(disc)) / (2 * qa) for s in (1, -1)]
            for t in roots:
                if 0 < t < 1:
                    v = (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t * t * p2 + t ** 3 * p3
                    (xs if ax == 0 else ys).append(v)
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    w, h = x1 - x0, y1 - y0
    if w < 1: x0, w = x0 - (1 - w) / 2, 1.0
    if h < 1: y0, h = y0 - (1 - h) / 2, 1.0
    return x0, y0, w, h


def line(k, name, pts, col, px=2, f0=0, dur=None, closed=False, handles=None, cap='round'):
    """a stroked path through `pts` (px, y down). handles: [((inDx, inDy), (outDx, outDy), corner)] as the old kit kept them.
    The object's box is the path's bounding box, so `pos` keys (the CENTRE of that box) move it as they should."""
    pp = []
    for i, p in enumerate(pts):
        if handles is None or handles[i][2] or handles[i] == ((0, 0), (0, 0), True): pp.append((p[0], p[1]))
        else: pp.append((p[0], p[1], handles[i][0], handles[i][1]))
    o = k.path(name, bezier(pp, closed), col, px, f0=f0, dur=dur, cap=cap)
    x, y, w, h = _bbox(pts, handles)
    o.box = (x + w / 2, y + h / 2, w, h); o.base = (x + w / 2, y + h / 2)
    return o


_FONTS = {}


def textw(s, px, style='SemiBold'):
    """advance width in px of Rethink Sans text (PIL; within about 1 % of the app), used to give a text box the width of its words"""
    try:
        from PIL import ImageFont
        key = (round(px * 4), style)
        if key not in _FONTS:
            f = ImageFont.truetype(os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author", "RethinkSans.ttf"), max(1, round(px * 4)))
            f.set_variation_by_name(style.encode()); _FONTS[key] = f
        return _FONTS[key].getlength(s) / 4
    except Exception:
        return len(s) * px * 0.62


def T(k, name, s, x, y, px, col, f0=0, dur=None, style='SemiBold', align='left', track=None, width=None):
    """text with its left (align 'left'), centre or right edge at x and its vertical centre at y. The box is as wide as the words and
    1.34 lines high, centred on y: the ink then sits where the old kit put it (the old box was 0.155 em lower; the pivot at 50% is the old y)."""
    tk = 0.0 if track is None else round((track - 1) * px * TRACK, 3)
    w = width or max(20, round(textw(s, px, style) + (len(s) - 1) * tk + 0.1 * px, 1))
    cx = x - 0.04 * px + w / 2 if align == 'left' else (x + 0.03 * px - w / 2 if align == 'right' else x)
    o = k.text(name, s, cx, y, px, col, f0=f0, dur=dur, weight=WEIGHT[style], align=align, width=w,
               tracking=None if track is None else tk)
    o.box = (cx, y, w, round(px * 1.34, 2)); o.base = (cx, y)
    return o


def gl(o, size=10, amount=0.55, blend=0.2):
    """the pack's glow in the object's own colour (cc2's glow() writes a white one)"""
    return o.set('glow', '%gpx %g %g' % (round(size * 1.15, 2), amount, blend))      # the old size runs 0..100, px 0..115


def more(o, key, extra):
    """add keys [(comp frame, value, ease)] to the object's lane `key` (a lane keeps one key per frame)"""
    have = [(f + o.f0, v, e) for f, v, e in o.tracks.get(key, [])]
    new = {f for f, *_ in extra}
    return o.key(key, sorted([x for x in have if x[0] not in new] + list(extra), key=lambda s: s[0]))


def scale_keys(o, sx=None, sy=None, base=(1.0, 1.0)):
    """merge separate x and y scale lanes [(comp frame, value, ease)] into one [sx, sy] key list (a lane holds its last value)"""
    frames = sorted(set([f for f, *_ in (sx or [])] + [f for f, *_ in (sy or [])]))
    def at(lane, f, dflt):
        if not lane: return dflt
        v = lane[0][1]
        for ff, vv, *_ in lane:
            if ff <= f: v = vv
        return v
    return more(o, 'scale', [(f, [round(at(sx, f, base[0]), 5), round(at(sy, f, base[1]), 5)], 'Linear') for f in frames])


# ---------------------------------------------------------------- the pack's presets, baked as keys at the object's own clip
SCAN_OPEN = [(0, 0.02), (1, 0.39314), (2, 0.63534), (3, 0.78037), (4, 0.86694), (5, 0.91961), (7, 0.97234), (10, 0.99642), (14, 1.0)]


def flick(o, f=None):
    """Flicker on: opacity 0 -> 80 -> 15 -> 90 -> 50 -> 100 %, Hold keys 2 f apart (fully on at f + 10)"""
    f = o.f0 if f is None else f
    return more(o, 'opacity', [(f, 0.0, 'Linear'), (f + 2, 0.8, 'Linear'), (f + 4, 0.15, HOLD), (f + 6, 0.9, HOLD), (f + 8, 0.5, HOLD),
                               (f + 10, 1.0, HOLD), (f + 12, 1.0, HOLD)])


def scan_open(o, f=None, d=None, sx=1.0, sy=1.0):
    """Scan open (Y): scale Y 2 % -> 100 % on an expo landing (the preset's 14 f), fade in over the first 3 f. `d` makes a shorter one
    (the round-3 labs used 8-12 f)."""
    f = o.f0 if f is None else f
    if d is None:
        o.scale([(f + a, [sx, round(v * sy, 5)], 'Linear') for a, v in SCAN_OPEN])
        o.op([(f, 0.0, 'Linear'), (f + 3, 1.0, 'Linear')])
    else:
        o.scale([(f, [sx, 0.02 * sy], 'Linear'), (f + d, [sx, sy], EXPO)])
        o.op([(f, 0.0, 'Linear'), (f + max(2, d // 5), 1.0, 'Linear')])
    return o


def power_down(o, end=None, sx=1.0, sy=1.0):
    """Power down (out, 12 f): scale Y to 2 % in 6 f (accelerating), then scale X to 0 in 6 f; the last key is the clip's last frame"""
    end = (o.f0 + o.dur) if end is None else end
    f = end - 13
    sy_l = [(f + a, v * sy) for a, v in ((0, 1.0), (1, 0.91258), (2, 0.78168), (3, 0.62159), (5, 0.23894), (6, 0.02), (12, 0.02))]
    sx_l = [(f + a, v * sx) for a, v in ((0, 1.0), (6, 1.0), (7, 0.9108), (8, 0.77722), (9, 0.61387), (11, 0.22341), (12, 0.0))]
    return scale_keys(o, sx_l, sy_l)


def exit_fade(o, end=None):
    """Exit fade - fast (out, 9 f): opacity 1 -> 0 on an accelerating curve; the last key is the clip's last frame"""
    end = (o.f0 + o.dur) if end is None else end
    f = end - 9
    ks = [(0, 1.0), (2, 0.96466), (3, 0.91763), (4, 0.846), (5, 0.74257), (6, 0.59441), (7, 0.3743), (8, 0.0)]
    return more(o, 'opacity', [(f + a, v, 'Linear') for a, v in ks])


def type_on(o, gap=1.0):
    """types the text on: each character snaps on `gap` frames after the previous one (a stagger over opacity)"""
    return o.stagger(by='chars', each=gap, keyframes=[(0, {'opacity': 0}, 'Linear'), (1, {'opacity': 1}, HOLD)])


def spin(o, f0, f1, deg):
    """rotation at a constant speed from f0 to f1 totalling `deg` clockwise degrees. A key holds -360..360, so a longer spin is keyed one
    turn at a time: at the frame a turn completes the value is +-360, and a Hold key on the next frame carries on from the same
    picture (one frame of travel), so every whole frame reads the exact angle."""
    step = deg / (f1 - f0); per = round(360.0 / abs(step)); sgn = 1 if deg > 0 else -1
    keys, t = [(f0, 0.0, 'Linear')], 0
    while abs(deg) - 360 * t > 360 + 1e-6:
        t += 1
        keys.append((f0 + t * per, 360.0 * sgn, 'Linear'))
        keys.append((f0 + t * per + 1, round(step, 5), HOLD))
    keys.append((f1, round(deg - 360.0 * sgn * t, 5), 'Linear'))
    return o.rot(keys)


def draw(o, f, d=14, ease=EXPO):
    o.trim([(f, 0.0, 'Linear'), (f + d, 1.0, ease)], which='end'); return o


def reticle(d):
    n = 90
    k = d.comp("FH Reticle", n, "frt"); lab_bg(k, n)
    cx, cy = 960, 540
    outer = k.ell("Outer ring", cx, cy, 440, 440, None, f0=0, dur=n); outer.stroke(COL['cyan'], 4)
    outer.set('strokeDasharray', '28 14'); gl(outer, 8, 0.5)
    outer.rot([(0, 0.0, 'Linear'), (n, -60.0, 'Linear')])
    scan_open(outer)                                                     # preset Scan open (Y)
    inner = k.ell("Inner arcs", cx, cy, 300, 300, None, f0=6, dur=n - 6); inner.stroke(COL['cyan'], 8, cap='butt')
    gl(inner, 8, 0.5)
    inner.trim([(6, 0.1, 'Linear'), (20, 0.45, EXPO)], which='end'); inner.set('trimStart', '10%')
    inner.rot([(6, 0.0, 'Linear'), (n, 90.0, 'Linear')])
    for name, a, b in (("Cross left", (cx - 270, cy), (cx - 90, cy)), ("Cross right", (cx + 270, cy), (cx + 90, cy)),
                       ("Cross top", (cx, cy - 270), (cx, cy - 90)), ("Cross bottom", (cx, cy + 270), (cx, cy + 90))):
        ln = line(k, name, [a, b], COL['white'], px=3, f0=10, dur=n - 10)
        ln.trim([(10, 0.0, 'Linear'), (22, 1.0, EXPO)], which='end')
    dot = k.ell("Centre dot", cx, cy, 14, 14, COL['amber'], f0=20, dur=n - 20); flick(dot)
    flick(T(k, "Lock label", "TARGET LOCKED", cx, cy + 320, 34, COL['amber'], f0=30, dur=n - 30, align='center', track=1.4))


def brackets(d):
    n = 75
    k = d.comp("FH Brackets", n, "fbr"); lab_bg(k, n)
    cx, cy, w, h, arm = 960, 540, 640, 380, 60
    l, r, t, b = cx - w / 2, cx + w / 2, cy - h / 2, cy + h / 2
    corners = [("Corner TL", [(l, t + arm), (l, t), (l + arm, t)], -1, -1), ("Corner TR", [(r - arm, t), (r, t), (r, t + arm)], 1, -1),
               ("Corner BR", [(r, b - arm), (r, b), (r - arm, b)], 1, 1), ("Corner BL", [(l + arm, b), (l, b), (l, b - arm)], -1, 1)]
    for i, (name, pts, sx, sy) in enumerate(corners):
        o = line(k, name, pts, COL['cyan'], px=5, f0=0, dur=n)
        gl(o, 6, 0.45)
        bx, by = o.base; f = i * 2
        o.pos([(f, (bx + sx * 90, by + sy * 90), 'Linear'), (f + 14, (bx, by), EXPO)])
        o.op([(f, 0, 'Linear'), (f + 4, 1, 'Linear')])
    scan = k.rect("Scan line", cx, t + 10, w - 40, 3, COL['cyan'], f0=16, dur=n - 16, center=True)
    gl(scan, 10, 0.6)
    sxp, syp = scan.base
    scan.pos([(16, (sxp, syp), 'Linear'), (56, (sxp, syp + (h - 20)), S_CURVE)])
    scan.op([(16, 0, 'Linear'), (20, 1, 'Linear')])
    flick(T(k, "Tag", "SCAN 01", l, t - 30, 26, COL['cyan'], f0=12, dur=n - 12, track=1.4))


def readout(d):
    n = 100
    k = d.comp("FH Readout", n, "frd"); lab_bg(k, n)
    rows = [("SYS STATUS", "NOMINAL"), ("CORE TEMP", "41.8 C"), ("LINK", "ENCRYPTED"), ("SIGNAL", "98%")]
    bar = k.rect("Accent bar", 560, 540, 6, 300, COL['cyan'], f0=0, dur=n, center=True)
    bar.scale([(0, [1.0, 0.0], 'Linear'), (14, [1.0, 1.0], EXPO)]); gl(bar, 6, 0.5)
    for i, (lab, val) in enumerate(rows):
        y = 435 + i * 70; f = 8 + i * 10
        flick(T(k, f"Label {i + 1}", lab, 600, y, 34, COL['dim'], f0=f, dur=n - f, track=1.3))
        v = T(k, f"Value {i + 1}", val, 1320, y, 34, COL['cyan'], f0=f + 4, dur=n - f - 4, align='right', track=1.2)
        type_on(v, 2.0)                                                  # types on, 2 f per character


def radar(d):
    n = 120
    k = d.comp("FH Radar", n, "frr"); lab_bg(k, n)
    cx, cy, R = 960, 540, 300
    for i, dia in enumerate((200, 400, 600)):
        ring = k.ell(f"Ring {i + 1}", cx, cy, dia, dia, None, f0=0, dur=n); ring.stroke(COL['grid'], 2)
    line(k, "Axis H", [(cx - R, cy), (cx + R, cy)], COL['grid'], px=2, f0=0, dur=n)
    line(k, "Axis V", [(cx, cy - R), (cx, cy + R)], COL['grid'], px=2, f0=0, dur=n)
    period = 60                                                          # one clockwise turn per 2 s
    wedge = k.ell("Sweep wedge", cx, cy, R, R, None, f0=0, dur=n); wedge.stroke(COL['cyan'], R, cap='butt')   # a butt-capped stroke as wide as the diameter: a pie slice
    wedge.set('trimEnd', '7%'); wedge.set('trimStart', '0%')
    wedge.opv(0.28)
    spin(wedge, 0, n, 360.0 * n / period)
    # the beam turns about its centre end: the line runs from the centre to the rim and its pivot (transformOrigin 0% 50%) is set after the
    # scene is applied (a scene cannot give a path its own pivot)
    beam = line(k, "Sweep line", [(cx, cy), (cx + R, cy)], COL['cyan'], px=3, f0=0, dur=n)
    gl(beam, 8, 0.6)
    ORIGINS.append((beam.id, '0% 50%'))
    spin(beam, 0, n, 360.0 * n / period)
    for i, (ang, rad) in enumerate(((300, 0.55), (200, 0.8), (40, 0.35))):    # math angles, counter-clockwise from 3 o'clock
        x = cx + R * rad * math.cos(math.radians(ang)); y = cy - R * rad * math.sin(math.radians(ang))
        t = round(((360 - ang) % 360) / 360 * period)
        dot = k.ell(f"Blip {i + 1}", x, y, 18, 18, COL['amber'], f0=t, dur=n - t)
        gl(dot, 6, 0.5)
        dot.scale([(t, 0.0, 'Linear'), (t + 6, 1.0, BEZ['back'])])
        dot.op([(t, 1.0, 'Linear'), (t + 50, 0.35, 'Linear')])


def build(path=None, m=None):
    del ORIGINS[:]
    d = HDoc()
    reticle(d); brackets(d); readout(d); radar(d)
    return d


if __name__ == "__main__":
    print(__doc__)
