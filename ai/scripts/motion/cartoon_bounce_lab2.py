"""Cartoon Bounce round 2: eight more lab comps (speech bubble, button press, character hop,
sticker burst, end card, ribbon lower third, hanging sign, bouncy list), written straight
into a .carverproj.

    import cartoon_bounce_lab2 as L; presets, masks = L.build(PROJECT.carverproj)

Same palette and verification as cartoon_bounce_lab.py. Springs are baked from curves.py
(spring-wobbly about 31%, spring-bouncy about 16%) as linear-joined keys. Characters and
the sign are rigged with a PIVOT NULL (ai/references/drawing/rigging.md): the parts are
parented to a tiny invisible ellipse at the joint, and only the null moves, scales or turns.
After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); edit.save; check
with carvercat_inspect and carvercat_look; extract templates with comp_to_template.py
(--drop "Lab bg"). Docs: ai/patterns/cartoon-bounce.md.
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cartoon_bounce_lab import Doc, lin, P, COL, EXPO, BACK, lab_bg
from curves import named, bake

PRESETS, MASKS = [], []


def spring_keys(f0, d, a, b, curve='spring-wobbly', tol=0.006):
    """keys from value a to b over d frames on a baked spring (linear joins)"""
    out = []
    for t, p in bake(named[curve], d, tol):
        v = a + (b - a) * p if not isinstance(a, list) else [ai + (bi - ai) * p for ai, bi in zip(a, b)]
        out.append((f0 + t * d, v, 'Linear'))
    return out


def rig(kids, pivot):
    """Parent kids to pivot. Measured on 0.1.6: in the project file a parented child's position is read as an
    OFFSET from the comp centre, added to the parent's position (not as an absolute comp position). So
    rewrite each child's static position as centre + (child - pivot)."""
    px, py = pivot.base
    for c in kids:
        cx, cy = c.base
        c.base = [round(0.5 + cx - px, 5), round(0.5 + cy - py, 5)]
        c.set(c.tr('position'), c.base)
        c.clip['parentId'] = pivot.id


def outline(t, th=0.08):
    t.set(t.src('text_outline', 'paint'), 'solid').set(t.src('text_outline', 'color'), COL['ink'][:3])
    t.set(t.src('text_outline', 'thickness'), th).set(t.src('text_outline', 'outsideOnly'), True).set(t.src('text_outline', 'corners'), 'round')
    return t


def speech_bubble(d):
    n = 90
    k = d.comp("CT Speech bubble", n, "csb"); lab_bg(k, n)
    tail = k.path("Bubble tail", [(820, 600), (900, 600), (760, 720)], f0=4, dur=n - 4, closed=True)
    tail.fill(COL['white']); tail.stroke(COL['ink'], 8)
    PRESETS.append(("CT Speech bubble", "Bubble tail", "Pop - wobbly"))
    b = k.ell("Bubble", 960, 480, 620, 320, COL['white'], f0=0, dur=n); b.stroke(COL['ink'], 8)
    PRESETS.append(("CT Speech bubble", "Bubble", "Jelly in"))
    k.text("Bubble text", "Hi there!", 960, 480, 96, COL['ink'], f0=8, dur=n - 8, style='ExtraBold', align='center')
    PRESETS.append(("CT Speech bubble", "Bubble text", "Stamp"))


def button_press(d):
    n = 60
    k = d.comp("CT Button press", n, "cbp"); lab_bg(k, n)
    cx, cy, w, h, depth = 960, 520, 480, 150, 18
    k.rect("Button base", cx, cy + depth, w, h, COL['ink'], r=40, f0=0, dur=n, center=True)
    top = k.rect("Button top", cx, cy, w, h, COL['red'], r=40, f0=0, dur=n, center=True); top.stroke(COL['ink'], 6)
    lab = k.text("Button label", "PRESS ME", cx, cy, 64, COL['white'], f0=0, dur=n, style='ExtraBold', align='center')
    for o in (top, lab):
        bx, by = o.base
        down = [bx, by - depth / 1080]
        o.pos([(18, [bx, by], 'Linear'), (21, down, 'Ease in'), (24, down, 'Linear')] +
              spring_keys(24, 14, down, [bx, by], 'spring-bouncy')[1:])          # released: springs back up
    top.anchor(0, -1)
    top.scale([(18, [1.0, 1.0], 'Linear'), (21, [1.05, 0.88], 'Ease in'), (24, [1.05, 0.88], 'Linear')] +
              spring_keys(24, 14, [1.05, 0.88], [1.0, 1.0], 'spring-bouncy')[1:])
    ring = k.ell("Press ring", cx, cy + depth, 520, 200, None, f0=21, dur=16); ring.stroke(COL['ink'], 6)
    ring.scale([(21, 0.9, 'Linear'), (37, 1.35, EXPO)]); ring.op([(21, 0.8, 'Linear'), (37, 0.0, 'Linear')])


def character_hop(d):
    n = 90
    k = d.comp("CT Character hop", n, "cch"); lab_bg(k, n)
    ground = 860
    k.rect("Ground", 0, ground, 1920, 6, COL['ink'], f0=0, dur=n)
    x0, x1 = 520, 1400
    sh = k.ell("Hop shadow", x0, ground + 3, 220, 30, COL['shadow'], f0=0, dur=n); sh.opv(0.25)
    pivot = k.ell("Feet", x0, ground - 4, 150, 22, COL['ink'], f0=0, dur=n)   # the pivot (visible: lint flags an invisible null)
    body = k.rect("Body", x0, ground - 130, 200, 260, COL['green'], r=90, f0=0, dur=n, center=True); body.stroke(COL['ink'], 8)
    eyes = [k.ell(f"Eye {i + 1}", x0 + dx, ground - 175, 30, 46, COL['ink'], f0=0, dur=n) for i, dx in enumerate((-40, 40))]
    rig([body] + eyes, pivot)
    peak = ground - 340
    # anticipation crouch (f10-18), launch (f18-24 stretch), arc (f18-40), land squash (f40-44), settle (spring)
    pivot.pos([(10, P(x0, ground - 4), 'Linear'), (18, P(x0, ground - 4), 'Linear'), (29, P((x0 + x1) / 2, peak), 'Ease out'),
               (40, P(x1, ground - 4), 'Ease in')])
    sc = [(10, [1.0, 1.0], 'Linear'), (18, [1.15, 0.8], 'Ease out'), (22, [0.85, 1.2], 'Ease out'), (29, [0.95, 1.05], 'S-curve'),
          (38, [0.9, 1.12], 'S-curve'), (41, [1.25, 0.75], 'Ease in')]
    # recover in three visible swings; a baked spring's sub-pixel tail reads as lint 'jitter'
    sc += [(46, [0.92, 1.08], 'S-curve'), (51, [1.03, 0.97], 'S-curve'), (56, [1.0, 1.0], 'S-curve')]
    pivot.scale(sc)
    sh.pos([(18, P(x0, ground + 3), 'Linear'), (40, P(x1, ground + 3), 'S-curve')])
    sh.scale([(18, 1.0, 'Linear'), (29, 0.55, 'Ease out'), (40, 1.0, 'Ease in')])
    for e in eyes:                                                      # a blink after landing (keys 4+ f apart)
        e.scale([(64, [1, 1], 'Linear'), (66, [1.1, 0.1], 'Ease in'), (70, [1, 1], 'Ease out')])


def sticker_burst(d):
    n = 75
    k = d.comp("CT Sticker burst", n, "csk"); lab_bg(k, n)
    cols = [COL['red'], COL['yellow'], COL['blue'], COL['green'], COL['red'], COL['yellow']]
    for i in range(6):
        a = math.radians(90 + i * 60)
        r = 330
        if i % 3 == 0: o = k.star(f"Bit {i + 1}", 960, 540, 90, 5, 0.5, cols[i], f0=4, dur=n - 4)
        elif i % 3 == 1: o = k.ell(f"Bit {i + 1}", 960, 540, 70, 70, cols[i], f0=4, dur=n - 4)
        else: o = k.ngon(f"Bit {i + 1}", 960, 540, 90, 3, cols[i], f0=4, dur=n - 4)
        o.stroke(COL['ink'], 6)
        bx, by = o.base
        tgt = [bx + r * math.cos(a) / 1920, by + r * math.sin(a) / 1080]
        o.pos([(4, [bx, by], 'Linear'), (20, tgt, EXPO)])
        o.rot([(4, 0.0, 'Linear'), (20, 180.0 if i % 2 else -180.0, EXPO), (n, 200.0 if i % 2 else -200.0, 'Linear')])
        o.scale(spring_keys(4, 18, 0.0, 1.0, 'spring-wobbly'))
    hero = k.star("Hero star", 960, 540, 300, 5, 0.5, COL['yellow'], f0=0, dur=n); hero.stroke(COL['ink'], 10)
    PRESETS.append(("CT Sticker burst", "Hero star", "Pop - wobbly"))
    hero.rot([(0, 0.0, 'Linear'), (n, 24.0, 'Linear')])


def end_card(d):
    n = 120
    k = d.comp("CT End card", n, "cec"); lab_bg(k, n)
    logo = k.ell("Logo blob", 960, 360, 220, 220, COL['blue'], f0=0, dur=n); logo.stroke(COL['ink'], 10)
    PRESETS.append(("CT End card", "Logo blob", "Jelly in"))
    t = k.text("Sign-off", "SEE YOU SOON!", 960, 600, 120, COL['yellow'], f0=10, dur=n - 10, style='ExtraBold', align='center')
    outline(t)
    t.stagger(10, by='character', gap=2, dy=0.12, d=18, blur=0)
    rp = f'src.e_src_text_relative_{t.id}.position'
    t.key(rp, [(10 + p_t * 18, [0, round(0.12 * (1 - p), 5)], 'Linear') for p_t, p in bake(named['bounce'], 18, 0.01)])
    btn = k.rect("Next button", 960, 800, 420, 110, COL['red'], r=55, f0=44, dur=n - 44, center=True); btn.stroke(COL['ink'], 8)
    PRESETS.append(("CT End card", "Next button", "Pop - wobbly"))
    k.text("Next label", "WATCH NEXT", 960, 800, 48, COL['white'], f0=48, dur=n - 48, style='ExtraBold', align='center')
    PRESETS.append(("CT End card", "Next label", "Stamp"))


def ribbon_lower_third(d):
    n = 150
    k = d.comp("CT Ribbon lower third", n, "crl"); lab_bg(k, n)
    rb = k.rect("Ribbon", 140, 820, 640, 130, COL['yellow'], r=30, f0=0, dur=n); rb.stroke(COL['ink'], 8)
    rb.anchor(0, -1)                                                    # squash on its bottom edge
    PRESETS.append(("CT Ribbon lower third", "Ribbon", "Squash land"))
    PRESETS.append(("CT Ribbon lower third", "Ribbon", "Anticipate jump out"))
    k.text("Ribbon name", "Captain Waffles", 460, 870, 60, COL['ink'], f0=8, dur=n - 8, style='ExtraBold', align='center')
    PRESETS.append(("CT Ribbon lower third", "Ribbon name", "Stamp"))
    PRESETS.append(("CT Ribbon lower third", "Ribbon name", "Anticipate jump out"))
    k.text("Ribbon role", "Chief snack officer", 460, 990, 36, COL['ink'], f0=14, dur=n - 14, style='Bold', align='center')
    PRESETS.append(("CT Ribbon lower third", "Ribbon role", "Stamp"))
    PRESETS.append(("CT Ribbon lower third", "Ribbon role", "Anticipate jump out"))


def hanging_sign(d):
    n = 90
    k = d.comp("CT Hanging sign", n, "chs"); lab_bg(k, n)
    nail_x, nail_y = 960, 220
    pivot = k.ell("Nail", nail_x, nail_y, 24, 24, COL['ink'], f0=0, dur=n)    # the nail is the pivot
    s1 = k.line("String left", [(nail_x, nail_y), (nail_x - 200, 420)], COL['ink'], px=6, f0=0, dur=n)
    s2 = k.line("String right", [(nail_x, nail_y), (nail_x + 200, 420)], COL['ink'], px=6, f0=0, dur=n)
    sign = k.rect("Sign board", nail_x, 520, 560, 220, COL['red'], r=26, f0=0, dur=n, center=True); sign.stroke(COL['ink'], 10)
    txt = k.text("Sign text", "OPEN", nail_x, 520, 120, COL['white'], f0=0, dur=n, style='ExtraBold', align='center')
    outline(txt, 0.06)
    rig([s1, s2, sign, txt], pivot)
    # a swing that loses energy each time: follow-through on a damped spring, then still
    # each swing visibly smaller (28, -16, 8, -3.5, 0), S-curve between extremes: a baked spring's
    # sub-pixel tail reads as lint 'jitter'
    pivot.rot([(0, 28.0, 'Linear'), (12, -16.0, 'S-curve'), (23, 8.0, 'S-curve'), (33, -3.5, 'S-curve'), (42, 0.0, 'S-curve')])


def bouncy_list(d):
    n = 120
    k = d.comp("CT Bouncy list", n, "cbl"); lab_bg(k, n)
    items = [("Snacks", COL['red']), ("Naps", COL['blue']), ("Adventures", COL['green'])]
    for i, (s, col) in enumerate(items):
        y, f = 330 + i * 200, 6 + i * 10
        c = k.rect(f"Item card {i + 1}", 960, y, 760, 150, col, r=40, f0=f, dur=n - f, center=True); c.stroke(COL['ink'], 8)
        c.anchor(0, -1)
        PRESETS.append(("CT Bouncy list", f"Item card {i + 1}", "Squash land"))
        t = k.text(f"Item text {i + 1}", s, 960, y, 72, COL['white'], f0=f + 4, dur=n - f - 4, style='ExtraBold', align='center')
        outline(t, 0.06)
        PRESETS.append(("CT Bouncy list", f"Item text {i + 1}", "Stamp"))


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    speech_bubble(d); button_press(d); character_hop(d); sticker_burst(d); end_card(d); ribbon_lower_third(d)
    hanging_sign(d); bouncy_list(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
