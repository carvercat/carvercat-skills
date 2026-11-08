"""Write the Explainer lab comps in design units (cc2.py: px from the top-left, y down, degrees clockwise, CSS colours and easing).

    import explainer_lab as L; doc = L.build(); doc.send(client, PROJECT.carverproj)   # scene.apply per comp, then edit.save

Rules of the pack: a light ground, everything enters in reading order at the speed of narration, one emphasis at a time, the last
item gets time to be read. The pack's two stored presets (Step in, Emphasis pulse) and the Motion Patterns exit fade are BAKED
here as plain keys (step_in, pulse, exit_fade), so the templates need no preset applied afterwards.

This module is also the small kit of the Explainer labs 2 and 3 and of the showcase: text boxes that place left, centred or
right aligned text by its anchor, lines, arrows, checks, shadows. Arrows are a trimmed line plus a triangle head that pops when
the line arrives. Fonts: Rethink Sans must be installed (KI-136). Docs: ai/patterns/explainer.md. Design units: 1920 x 1080 px,
y down, comp frames, 30 fps.
"""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "json_author"))
from cc2 import Doc, Comp, Obj, css, ease, bezier, BEZ, HOLD

W, H = 1920, 1080
COL = dict(bg='#F7F7FA', ink='#1F2333', blue='#3B6EF6', coral='#FF6B5B', green='#2BB673', grey='#C9CDD8', muted='#6B7184',
           white='#FFFFFF')
# rect corner radius: the old kit capped it at a quarter of the short side (a pill r=h/2 drew at h/4); the labs write the capped value
# the old app model's curves (cc2.ease maps these names to different CSS ones): ease out, S-curve
BEZ['app-out'] = (1 / 3, 2 / 3, 2 / 3, 1)
BEZ['app-s'] = (1 / 3, 0, 2 / 3, 1)
EXPO, BACK = BEZ['expo'], BEZ['back']
WEIGHT = {'Medium': 500, 'Bold': 700, 'ExtraBold': 800}


# ---------------------------------------------------------------- text measure (Rethink Sans advance widths, about 1 % of the app)
_FONTS = {}


def textw(s, px, style='Bold'):
    """advance width in px of Rethink Sans text (matches Carvercat within about 1 %)."""
    from PIL import ImageFont
    k = (round(px * 4), style)
    if k not in _FONTS:
        f = ImageFont.truetype(os.path.join(HERE, 'json_author', 'RethinkSans.ttf'), max(1, round(px * 4)))
        f.set_variation_by_name(style.encode()); _FONTS[k] = f
    return _FONTS[k].getlength(s) / 4


# ---------------------------------------------------------------- keys: merge into the tracks an object already has
def addkeys(o, key, spec):
    """add keys [(comp frame, value, arriving ease)] to a property that may already have some (later keys win on a shared frame)"""
    have = {f: (f, v, e) for f, v, e in o.tracks.get(key, [])}
    for f, v, e in spec: have[f - o.f0] = (f - o.f0, v, e)
    o.tracks[key] = [have[f] for f in sorted(have)]
    return o


def px_ls(track, px):
    """the old kit's tracking (1 = none) as design letterSpacing in px"""
    return round((track - 1) * px * W / 1146.24, 3)


def T(k, name, s, x, y, px, col, f0=0, dur=None, style='Bold', align='left', lh=None, track=None, width=None, maxw=None):
    """a text from frame f0 for dur frames. (x, y): the anchor, as the old kit placed it: x is the left edge, the centre or
    the right edge by `align`, y the vertical middle of the text block. `lh` is the old line-spacing multiple (1 = the font's
    own, 1.34 in design units). `maxw` asserts the widest line fits (lint does not check this)."""
    lines = s.split('\n')
    w = max(textw(l, px, style) for l in lines)
    if maxw is not None and w > maxw: raise ValueError(f"{name}: {w:.0f} px wide, limit {maxw}")
    box_w = width or max(200, int(w * 1.12) + 40)
    cx = x + box_w / 2 if align == 'left' else x - box_w / 2 if align == 'right' else x
    o = k.text(name, s, cx, y, px, col, f0=f0, dur=dur, weight=WEIGHT[style], align=align, width=box_w)
    line_h = round(1.34 * (lh or 1.0), 4)
    o.set('lineHeight', line_h)
    o.box = (cx, y, box_w, math.ceil(len(lines) * px * line_h) + 4)
    o.base = (cx, y)
    if track and track != 1: o.set('letterSpacing', px_ls(track, px))
    if align == 'left': o.set('transformOrigin', '0% 50%')
    elif align == 'right': o.set('transformOrigin', '100% 50%')
    return o


def origin(o, ax, ay):
    """the pivot the old kit set in half-sizes (-1 left / bottom, +1 right / top; y up) as a CSS origin"""
    return o.set('transformOrigin', '%g%% %g%%' % (50 + 50 * ax, 50 - 50 * ay))


def shadow(o, y=-0.003, soft=0.012, op=0.15):
    """the old kit's shadow (y up as a fraction of H, softness as a fraction of W) as a CSS drop shadow in px"""
    return o.shadow(0, round(-y * H, 2), round(soft * 0.433 * W, 2), css('000000', op))


def line(k, name, pts, col, px=2, f0=0, dur=None, closed=False, join='miter'):
    """a stroked open path through points (px). Draw it on with .trim([...])."""
    o = k.path(name, bezier(pts, closed=closed), col=col, width=px, f0=f0, dur=dur)
    if join != 'miter': o.set('strokeLinejoin', join)
    return o


def poly(k, name, pts, f0=0, dur=None, col=None):
    """a filled closed path"""
    o = k.path(name, bezier(pts, closed=True), col='none', width=0, f0=f0, dur=dur, fill=col)
    o.set('stroke', 'none'); o.set('strokeWidth', 0)
    return o


# ---------------------------------------------------------------- the pack's presets, baked
def step_in(o, f, dx=48, ease_op='std'):
    """Step in: 2.5 % of the width in from the left on a strong decelerate (14 f) with a fade (7 f)"""
    bx, by = o.base
    if ease_op == 'std':       # the pack's preset as baked: linear joins between these frames (library/templates/explainer/ex_step_in.carverpreset)
        left = [(0, 1.0), (1, 0.46280), (2, 0.29240), (3, 0.20080), (5, 0.10120), (7, 0.04960), (10, 0.01280), (14, 0.0)]
        addkeys(o, 'pos', [(f + t, (round(bx - dx * q, 3), by), 'Linear') for t, q in left])
        addkeys(o, 'opacity', [(f + t, v, 'Linear') for t, v in [(0, 0.0), (2, 0.66705), (3, 0.82698), (4, 0.91641), (5, 0.96710), (7, 1.0)]])
    else:                      # round 3's variant: expo slide, fade on `ease_op`
        addkeys(o, 'pos', [(f, (bx - dx, by), 'Linear'), (f + 14, (bx, by), EXPO)])
        addkeys(o, 'opacity', [(f, 0.0, 'Linear'), (f + 7, 1.0, ease_op)])
    return o


def pulse(o, f, peak=1.15):
    """Emphasis pulse, once: a swell to `peak` and back in 16 f"""
    return addkeys(o, 'scale', [(f, 1.0, 'Linear'), (f + 6, peak, EXPO), (f + 16, 1.0, BEZ['smooth'])])


def exit_fade(o, n, d=8):
    """Exit fade - fast: opacity to 0 over the last d frames (the last frame of the comp is fully out)"""
    return addkeys(o, 'opacity', [(n - 1 - d, 1.0, 'Linear'), (n - 1, 0.0, BEZ['accel'])])


def pop(o, f, d=12):
    o.scale([(f, 0.0, 'Linear'), (f + d, 1.0, BACK)])


def draw(o, f, d=12, ease_=None):
    return o.trim([(f, 0.0, 'Linear'), (f + d, 1.0, ease_ or EXPO)])


def arrow(k, name, a, b, f, col, d=12, n=None):
    """a trimmed line from a to b and a triangle head that pops as the line arrives"""
    n = n or k.length
    ln = line(k, name, [a, b], col, px=8, f0=f, dur=n - f)
    ln.trim([(f, 0.0, 'Linear'), (f + d, 1.0, EXPO)])
    ang = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))          # clockwise on screen; a triangle at rotate 0 points right
    head = k.ngon(name + " head", b[0], b[1], 34, 3, col, f0=f + d - 4, dur=n - (f + d - 4))
    head.rotv(round(ang, 2))
    pop(head, f + d - 4, 8)
    return ln, head


def lab_bg(k, n):
    k.rect("Lab bg", 0, 0, W, H, COL['bg'], f0=0, dur=n)


def process_steps(d):
    n = 120
    k = d.comp("EX Process steps", n, "eps"); lab_bg(k, n)
    xs, y = (420, 960, 1500), 480
    labels = [("Plan", "Write the brief"), ("Build", "Make it in Carvercat"), ("Ship", "Render and deliver")]
    for i, (x, (t, s)) in enumerate(zip(xs, labels)):
        f = i * 24
        c = k.ell(f"Step {i + 1}", x, y, 160, 160, (COL['blue'], COL['coral'], COL['green'])[i], f0=f, dur=n - f)
        pop(c, f)
        step_in(T(k, f"Step {i + 1} number", str(i + 1), x, y, 72, COL['white'], f + 4, n - f - 4, 'ExtraBold', 'center'), f + 4)
        step_in(T(k, f"Step {i + 1} title", t, x, y + 140, 48, COL['ink'], f + 6, n - f - 6, 'Bold', 'center'), f + 6)
        step_in(T(k, f"Step {i + 1} text", s, x, y + 200, 30, COL['muted'], f + 10, n - f - 10, 'Medium', 'center'), f + 10)
        if i < 2:
            arrow(k, f"Arrow {i + 1}", (x + 110, y), (xs[i + 1] - 125, y), f + 12, COL['muted'], n=n)


def icon_grid(d):
    n = 90
    k = d.comp("EX Icon grid", n, "eig"); lab_bg(k, n)
    items = [("Fast", "star"), ("Simple", "circle"), ("Secure", "square"), ("Shared", "triangle"), ("Native", "hex"), ("Free", "ring")]
    for i, (word, shape) in enumerate(items):
        r, c = divmod(i, 3); x = 560 + c * 400; y = 380 + r * 320; f = i * 5
        tile = k.rect(f"Tile {i + 1}", x, y, 300, 260, COL['white'], r=28, f0=f, dur=n - f, center=True)
        shadow(tile); step_in(tile, f)
        col = (COL['blue'], COL['coral'], COL['green'])[i % 3]; iy = y - 30; g = f + 4
        if shape == "star": ic = k.star(f"Icon {i + 1}", x, iy, 110, 5, 0.45, col, f0=g, dur=n - g)
        elif shape == "circle": ic = k.ell(f"Icon {i + 1}", x, iy, 96, 96, col, f0=g, dur=n - g)
        elif shape == "square": ic = k.rect(f"Icon {i + 1}", x, iy, 90, 90, col, r=18, f0=g, dur=n - g, center=True)
        elif shape == "triangle": ic = k.ngon(f"Icon {i + 1}", x, iy, 110, 3, col, f0=g, dur=n - g)
        elif shape == "hex": ic = k.ngon(f"Icon {i + 1}", x, iy, 104, 6, col, f0=g, dur=n - g)
        else:
            ic = k.ell(f"Icon {i + 1}", x, iy, 96, 96, None, f0=g, dur=n - g); ic.stroke(col, 14)
        pop(ic, g)
        step_in(T(k, f"Caption {i + 1}", word, x, y + 80, 34, COL['ink'], f + 8, n - f - 8, 'Bold', 'center'), f + 8)


def callout(d):
    n = 75
    k = d.comp("EX Callout", n, "eco"); lab_bg(k, n)
    tx, ty = 760, 640
    dot = k.ell("Target", tx, ty, 28, 28, COL['coral'], f0=0, dur=n); pop(dot, 0, 10)
    ring = k.ell("Target ring", tx, ty, 90, 90, None, f0=6, dur=n - 6); ring.stroke(COL['coral'], 5)
    ring.op([(6, 0.0, 'Linear'), (10, 1.0, 'Linear')]); pulse(ring, 6)
    lead = line(k, "Leader", [(tx + 30, ty - 30), (tx + 220, ty - 220), (tx + 520, ty - 220)], COL['ink'], px=4, f0=10, dur=n - 10)
    lead.trim([(10, 0.0, 'Linear'), (26, 1.0, EXPO)])
    box = k.rect("Label box", tx + 540, ty - 260, 520, 84, COL['ink'], r=16, f0=24, dur=n - 24)
    origin(box, -1, 0); box.scale([(24, [0.0, 1.0], 'Linear'), (36, [1.0, 1.0], EXPO)])
    step_in(T(k, "Label", "The part that matters", tx + 570, ty - 218, 36, COL['white'], 30, n - 30, 'Bold'), 30)


def timeline(d):
    n = 150                                                           # 40 f after the last milestone: enough to read it
    k = d.comp("EX Timeline", n, "etl"); lab_bg(k, n)
    x0, x1, y = 260, 1660, 560
    base = line(k, "Track", [(x0, y), (x1, y)], COL['grey'], px=6, f0=0, dur=n)
    base.trim([(0, 0.0, 'Linear'), (24, 1.0, EXPO)])
    prog = line(k, "Progress", [(x0, y), (x1, y)], COL['blue'], px=6, f0=0, dur=n)
    prog.trim([(30, 0.0, 'Linear'), (110, 1.0, 'app-s')])
    ms = [("2019", "Idea"), ("2021", "First release"), ("2023", "Teams"), ("2026", "Everywhere")]
    for i, (yr, txt) in enumerate(ms):
        x = x0 + (x1 - x0) * i / 3
        f = 30 + round(80 * i / 3)                                    # the dot pops as the progress reaches it
        dot = k.ell(f"Milestone {i + 1}", x, y, 30, 30, COL['blue'], f0=f, dur=n - f); dot.stroke(COL['white'], 6); pop(dot, f, 10)
        step_in(T(k, f"Year {i + 1}", yr, x, y - 70, 44, COL['ink'], f + 2, n - f - 2, 'ExtraBold', 'center'), f + 2)
        step_in(T(k, f"Event {i + 1}", txt, x, y + 70, 30, COL['muted'], f + 5, n - f - 5, 'Medium', 'center'), f + 5)


def build(path=None, m=None):
    d = Doc()
    process_steps(d); icon_grid(d); callout(d); timeline(d)
    return d


if __name__ == "__main__":
    print(__doc__)
