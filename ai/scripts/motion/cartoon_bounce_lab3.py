"""Cartoon Bounce round 3: eight lab comps for briefs the pack could not serve before (a walk
cycle, a map pin drop, a thought bubble, a squash-and-stretch logo reveal, a swinging price tag,
a boing arrow, a comic POW and a kids' lesson title card), written straight into a .carverproj.

    import cartoon_bounce_lab3 as L; presets, masks = L.build(PROJECT.carverproj)

Same palette as cartoon_bounce_lab.py. Every move is baked as keys here (no presets to apply,
no masks): springs are hand-set visible extremes (a baked spring's sub-pixel tail reads as lint
'jitter', pitfall 6), and every squash keeps its volume (x * y between 0.9 and 1.05; VOLUME
records the extremes per object and build() refuses anything outside). Real arcs use the three
methods in ai/references/craft/principles/arcs.md: parabolas baked to keys every 2 f (logo ball,
walk hips), rotation about a visible pivot (price tag, walk legs and arms), never two straight legs.
Rigs use a VISIBLE pivot with a centred anchor (rig() from cartoon_bounce_lab2.py).
After writing: edit.open {path, force:true}; edit.save; check with carvercat_inspect and
carvercat_look; extract templates with comp_to_template.py (--drop "Lab bg").
Fonts: Rethink Sans must be installed (KI-136). Docs: ai/patterns/cartoon-bounce.md (round 3).
Pixel space 1920x1080, y down; comp frames, 30 fps. Names, prices and places are sample copy.
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cartoon_bounce_lab import Doc, lin, P, COL, EXPO, BACK, lab_bg
from cartoon_bounce_lab2 import rig, outline
from curves import named, bake

PRESETS, MASKS = [], []
VOLUME = {}                       # (comp, object) -> (min x*y, max x*y) over its non-uniform scale keys
W, H = 1920.0, 1080.0
COL = dict(COL, map=lin('CFEBC6'), road=lin('FFFFFF'), river=lin('9CCBFF'), pale=lin('FFE7B8'))


def vol(comp, o, spec):
    """record x*y of every non-uniform scale key (squash and stretch keep volume)"""
    xs = [v[0] * v[1] for f, v, e in spec if isinstance(v, list) and abs(v[0] - v[1]) > 1e-9]
    if xs:
        lo, hi = min(xs), max(xs)
        assert 0.9 <= lo and hi <= 1.05, (comp, o.clip['label'], lo, hi)
        VOLUME[(comp, o.clip['label'])] = (round(lo, 3), round(hi, 3))
    o.scale(spec)


def arc(f0, f1, x0, y0, x1, y1, h, step=2):
    """a real parabola baked to keys every `step` frames (Linear joins): x linear in time,
    y = chord - 4 h t (1 - t) (h px above the chord at the middle). Returns [(f, (x, y))]."""
    out, n = [], max(1, int(round((f1 - f0) / step)))
    for i in range(n + 1):
        t = i / n
        out.append((f0 + (f1 - f0) * t, (x0 + (x1 - x0) * t, y0 + (y1 - y0) * t - 4 * h * t * (1 - t))))
    return out


def pop_keys(f, peak=1.12, low=0.95, over=1.02, gap=(4, 4, 4), frm=0.0):
    """uniform pop from frm with three visible extremes (no spring tail). Text pops from 0.6: lint
    text_too_small reads the line height on the first visible frame of the pop."""
    a, b, c = gap
    return [(f, frm, 'Linear'), (f + a, peak, 'Ease out'), (f + a + b, low, 'S-curve'), (f + a + b + c, over, 'S-curve'),
            (f + a + b + c + 4, 1.0, 'S-curve')]


def ink(o, px=8):
    return o.stroke(COL['ink'], px)


# ---------------------------------------------------------------- 1. walk cycle (rigged)
def walk_cycle(d):
    n = 150
    name = "CT Walk cycle"
    k = d.comp(name, n, "cwk"); lab_bg(k, n)
    ground, L, th = 900, 150, 24.0                  # hip-to-sole 150 px, legs swing +-24 deg
    x0, f_go, step = 420, 10, 12                    # a step every 12 f
    stride = 2 * L * math.sin(math.radians(th))     # 122 px: the planted foot does not slide
    k.rect("Ground", 0, ground, 1920, 6, COL['ink'], f0=0, dur=n)
    # leg angle A(f): half step, 7 full steps, half step (f10-106); leg B = -A
    keysA = [(f_go, 0.0)] + [(f_go + 6 + i * step, th if i % 2 == 0 else -th) for i in range(8)]
    keysA.append((keysA[-1][0] + 6, 0.0))
    f_stop = keysA[-1][0]                          # f106

    def ang(f):
        if f <= keysA[0][0]: return 0.0
        for (fa, a), (fb, b) in zip(keysA, keysA[1:]):
            if fa <= f <= fb: return a + (b - a) * (f - fa) / (fb - fa)
        return 0.0
    v = stride / step                               # hip speed that keeps the stance foot planted
    def hip(f):
        x = x0 + v * min(max(f - f_go, 0), f_stop - f_go)
        return x, ground - L * math.cos(math.radians(ang(f)))   # the hip dips when the legs spread
    hx, hy = hip(0)
    sh = k.ell("Walk shadow", hx, ground + 3, 260, 30, COL['shadow'], f0=0, dur=n); sh.opv(0.22)
    sy = hy - 150                                    # shoulder
    arm_b = k.rect("Arm back", hx, sy + 62, 36, 124, COL['blue'], r=18, f0=0, dur=n, center=True); ink(arm_b, 6)
    leg_b = k.rect("Leg back", hx, hy + L / 2, 44, L, COL['ink'], r=22, f0=0, dur=n, center=True)
    leg_f = k.rect("Leg front", hx, hy + L / 2, 44, L, COL['ink'], r=22, f0=0, dur=n, center=True)
    body = k.rect("Body", hx, hy - 150, 230, 270, COL['blue'], r=105, f0=0, dur=n, center=True); ink(body, 10)
    pivot = k.rect("Shorts", hx, hy, 200, 72, COL['red'], r=26, f0=0, dur=n, center=True); ink(pivot, 8)
    eyes = [k.ell(f"Eye {i + 1}", hx + dx, hy - 210, 30, 48, COL['ink'], f0=0, dur=n) for i, dx in enumerate((34, 84))]
    arm_f = k.rect("Arm front", hx, sy + 62, 36, 124, COL['blue'], r=18, f0=0, dur=n, center=True); ink(arm_f, 6)
    rig([arm_b, leg_b, leg_f, body] + eyes + [arm_f], pivot)
    for o in (arm_b, leg_b, leg_f, arm_f): o.anchor(0, 1)      # limbs turn about their top (hip, shoulder)
    # hips: baked every 2 f (x linear, y from the leg angle: a real bob, not a ping-pong of two keys)
    fs = list(range(0, f_go + 1, f_go)) + list(range(f_go + 2, f_stop, 2)) + [f_stop]
    pivot.pos([(f, P(*hip(f)), 'Linear') for f in fs])
    sh.pos([(f, P(hip(f)[0], ground + 3), 'Linear') for f in (0, f_go, f_stop)])
    # legs: Linear between extremes so the stance foot sweeps back at the hip's speed
    leg_f.rot([(f, a, 'Linear') for f, a in keysA]); leg_b.rot([(f, -a, 'Linear') for f, a in keysA])
    # the swinging leg tucks (shorter, a little wider) mid-swing so its foot clears the ground
    for leg, sgn in ((leg_f, 1), (leg_b, -1)):
        sc = [(0, [1.0, 1.0], 'Linear'), (f_go, [1.0, 1.0], 'Linear')]
        for (fa, a), (fb, b) in zip(keysA, keysA[1:]):
            swing = (b - a) * sgn > 0
            mid = (fa + fb) / 2
            sc += [(mid, [1.08, 0.88] if swing else [1.0, 1.0], 'S-curve'), (fb, [1.0, 1.0], 'S-curve')]
        vol(name, leg, sc)
    # arms swing against the legs, S-curve between extremes
    for arm, sgn in ((arm_f, -1), (arm_b, 1)):
        arm.rot([(f, sgn * a * 0.8, 'S-curve' if i else 'Linear') for i, (f, a) in enumerate(keysA)])
    # stop: settle on the hips (pivot squash about the hip, volume kept), then a blink
    vol(name, pivot, [(f_stop, [1.0, 1.0], 'Linear'), (f_stop + 3, [1.06, 0.94], 'Ease out'), (f_stop + 8, [0.97, 1.03], 'S-curve'),
                      (f_stop + 13, [1.0, 1.0], 'S-curve')])
    for e in eyes:
        e.scale([(126, [1, 1], 'Linear'), (128, [1.1, 0.1], 'Ease in'), (132, [1, 1], 'Ease out')])


# ---------------------------------------------------------------- 2. map pin drop (rigged)
def map_pin(d):
    n = 120
    name = "CT Map pin"
    k = d.comp(name, n, "cmp"); lab_bg(k, n)
    m = k.rect("Map", 960, 560, 1400, 780, COL['map'], r=40, f0=0, dur=n, center=True); ink(m, 8)
    m.op([(0, 0.0, 'Linear'), (8, 1.0, 'Ease out')])
    for i, pts in enumerate([[(270, 420), (1650, 470)], [(760, 175), (820, 945)], [(1200, 175), (1330, 945)]]):
        r = k.line(f"Road {i + 1}", pts, COL['road'], px=22, f0=0, dur=n)
        r.op([(0, 0.0, 'Linear'), (8, 1.0, 'Ease out')])
    rv = k.line("River", [(270, 820), (1650, 700)], COL['river'], px=30, f0=0, dur=n,
                handles=[((0, 0), (380, -160), False), ((-420, 200), (0, 0), False)])
    rv.op([(0, 0.0, 'Linear'), (8, 1.0, 'Ease out')])
    tx, ty, f_hit = 880, 680, 16                                  # the tip lands at (880, 680) on f16
    shd = k.ell("Pin shadow", tx, ty + 4, 110, 26, COL['shadow'], f0=0, dur=n)
    shd.scale([(0, 0.3, 'Linear'), (f_hit, 1.0, 'Ease in')]); shd.op([(0, 0.04, 'Linear'), (f_hit, 0.25, 'Ease in')])
    ring = k.ell("Landing ring", tx, ty + 4, 150, 44, None, f0=f_hit, dur=22); ink(ring, 6)
    ring.scale([(f_hit, 0.6, 'Linear'), (f_hit + 20, 1.9, EXPO)]); ring.op([(f_hit, 0.8, 'Linear'), (f_hit + 20, 0.0, 'Linear')])
    S = 1.4
    head = k.path("Pin head", [(tx, ty), (tx - 62 * S, ty - 112 * S), (tx, ty - 176 * S), (tx + 62 * S, ty - 112 * S)], f0=0, dur=n, closed=True,
                  handles=[((0, 0), (0, 0), True), ((0, 46 * S), (0, -34 * S), False), ((-34 * S, 0), (34 * S, 0), False),
                           ((0, -34 * S), (0, 46 * S), False)])
    head.fill(COL['red']); ink(head, 10)
    dot = k.ell("Pin dot", tx, ty - 114 * S, 64, 64, COL['white'], f0=0, dur=n); ink(dot, 8)
    tip = k.ell("Pin tip", tx, ty, 16, 10, COL['ink'], f0=0, dur=n)            # the visible pivot at the point
    rig([head, dot], tip)
    tip.pos([(0, P(tx, -40), 'Linear'), (f_hit, P(tx, ty), 'Ease in')])         # falls, accelerating
    vol(name, tip, [(0, [0.88, 1.14], 'Linear'), (f_hit - 1, [0.86, 1.16], 'Linear'), (f_hit + 1, [1.22, 0.8], 'Ease out'),
                    (f_hit + 5, [0.92, 1.08], 'S-curve'), (f_hit + 9, [1.04, 0.96], 'S-curve'), (f_hit + 13, [1.0, 1.0], 'S-curve')])
    # the label pops out of the pin's side
    lx, ly = 1250, 420
    card = k.rect("Label card", lx, ly, 440, 150, COL['white'], r=34, f0=26, dur=n - 26, center=True); ink(card, 6)
    card.scale(pop_keys(26)); card.op([(26, 0.0, 'Linear'), (28, 1.0, 'Linear')])
    t1 = k.text("Place", "Pip's Bakery", lx, ly - 22, 54, COL['ink'], f0=30, dur=n - 30, style='ExtraBold', align='center')
    t2 = k.text("Note", "OPEN TILL 6", lx, ly + 40, 34, COL['red'], f0=34, dur=n - 34, style='ExtraBold', align='center', track=1.1)
    for t, f in ((t1, 30), (t2, 34)):
        t.scale(pop_keys(f, frm=0.6)); t.op([(f, 0.0, 'Linear'), (f + 2, 1.0, 'Linear')])


# ---------------------------------------------------------------- 3. thought bubble (rigged cloud)
def thought_bubble(d):
    n = 120
    name = "CT Thought bubble"
    k = d.comp(name, n, "ctb"); lab_bg(k, n)
    hx, hy = 470, 800
    head = k.ell("Head", hx, hy, 300, 300, COL['yellow'], f0=0, dur=n); ink(head, 8)
    vol(name, head, [(0, [0.0, 0.0], 'Linear'), (6, [1.1, 0.92], 'Ease out'), (10, [0.95, 1.05], 'S-curve'),
                     (14, [1.02, 0.98], 'S-curve'), (18, [1.0, 1.0], 'S-curve')])
    eyes = [k.ell(f"Eye {i + 1}", hx + dx, hy - 50, 34, 52, COL['ink'], f0=6, dur=n - 6) for i, dx in enumerate((10, 80))]
    for e in eyes:                                                 # eyes pop, then look up (a blink at f84)
        e.scale(pop_keys(6) + [(84, 1.0, 'Linear'), (86, [1.1, 0.1], 'Ease in'), (90, 1.0, 'Ease out')])
    # trail dots: small to big, along the line from the head to the cloud
    for i, (x, y, s) in enumerate([(650, 610, 40), (740, 530, 58), (850, 450, 80)]):
        o = k.ell(f"Trail {i + 1}", x, y, s, s, COL['white'], f0=12 + 4 * i, dur=n - 12 - 4 * i); ink(o, 6)
        o.scale(pop_keys(12 + 4 * i, 1.25, 0.92, 1.03, (3, 3, 3)))
    cx, cy = 1250, 330
    puffs = [(cx + 255 * math.cos(math.radians(a)), cy + 120 * math.sin(math.radians(a)), s)
             for a, s in [(0, 180), (45, 170), (90, 190), (135, 170), (180, 180), (225, 170), (270, 200), (315, 170)]]
    outl = [k.ell(f"Puff line {i + 1}", x, y, s + 16, s + 16, COL['ink'], f0=24, dur=n - 24) for i, (x, y, s) in enumerate(puffs)]
    core_l = k.ell("Core line", cx, cy, 536, 276, COL['ink'], f0=24, dur=n - 24)
    fill = [k.ell(f"Puff {i + 1}", x, y, s, s, COL['white'], f0=24, dur=n - 24) for i, (x, y, s) in enumerate(puffs)]
    core = k.ell("Cloud", cx, cy, 520, 260, COL['white'], f0=24, dur=n - 24)   # the pivot: centred, visible
    rig(outl + [core_l] + fill, core)
    # jelly in: pop, then squash/stretch extremes that keep the volume; then a slow 12 px float (one way, no loop)
    vol(name, core, [(24, [0.0, 0.0], 'Linear'), (30, [1.1, 0.92], 'Ease out'), (34, [0.94, 1.06], 'S-curve'),
                     (38, [1.03, 0.97], 'S-curve'), (42, [1.0, 1.0], 'S-curve')])
    core.pos([(42, P(cx, cy), 'Linear'), (n, P(cx, cy - 12), 'Linear')])
    t = k.text("Thought", "Snack time?", cx, cy, 80, COL['ink'], f0=36, dur=n - 36, style='ExtraBold', align='center')
    t.scale(pop_keys(36, frm=0.6)); t.op([(36, 0.0, 'Linear'), (38, 1.0, 'Linear')])
    t.pos([(42, P(cx, cy), 'Linear'), (n, P(cx, cy - 12), 'Linear')])


# ---------------------------------------------------------------- 4. squash-and-stretch logo reveal
def logo_reveal(d):
    n = 120
    name = "CT Logo reveal"
    k = d.comp(name, n, "clr"); lab_bg(k, n)
    word, px = "bouncy", 190
    from cc import textw
    ww = textw(word, px, 'ExtraBold')
    r, gap = 70, 36
    total = 2 * r + gap + ww
    bx = 960 - total / 2 + r                             # the ball's rest centre (the logo mark)
    wx = bx + r + gap                                    # the word's left edge
    base = 600                                           # ground / baseline of the mark
    yc = base - r
    hits = [(14, 1500), (30, 1020), (42, bx)]            # contact frame, contact x (third hit = the mark), right to left
    sh = k.ell("Ball shadow", bx, base + 6, 150, 26, COL['shadow'], f0=0, dur=n)
    ball = k.ell("Logo ball", bx, yc, 2 * r, 2 * r, COL['red'], f0=0, dur=n); ink(ball, 8)
    ball.anchor(0, -1)                                   # squash on the ground: pivot at the bottom edge
    pts = arc(0, 14, 2040, yc - 360, hits[0][1], yc, 0)  # entering from the top right, accelerating (a falling half-parabola)
    pts = [(f, (x, (yc - 360) + 360 * ((f - 0) / 14) ** 2)) for f, (x, y) in pts]
    pts += arc(14, 30, hits[0][1], yc, hits[1][1], yc, 230)[1:]
    pts += arc(30, 42, hits[1][1], yc, hits[2][1], yc, 90)[1:]
    ball.pos([(f, P(x, y), 'Linear') for f, (x, y) in pts])
    sh.pos([(f, P(x, base + 6), 'Linear') for f, (x, y) in pts])
    sh.scale([(f, round(0.4 + 0.6 * (1 - min(1, (yc - y) / 360)), 4), 'Linear') for f, (x, y) in pts])
    sh.op([(f, round(0.06 + 0.2 * (1 - min(1, (yc - y) / 360)), 4), 'Linear') for f, (x, y) in pts])
    sc = [(0, [0.9, 1.12], 'Linear')]
    for i, (f, x) in enumerate(hits):
        sq = [1.3, 0.74] if i < 2 else [1.24, 0.8]
        sc += [(f - 2, [0.88, 1.14], 'Linear'), (f, sq, 'Linear')]
        if i < 2: sc += [(f + 3, [0.92, 1.09], 'Ease out')]           # stretches up off the ground
        else: sc += [(f + 4, [0.93, 1.07], 'S-curve'), (f + 8, [1.03, 0.97], 'S-curve'), (f + 12, [1.0, 1.0], 'S-curve')]
    vol(name, ball, sc)
    # the word springs up out of the baseline on the last impact, letter by letter
    f_w = 42
    t = k.text("Wordmark", word, wx, base - 0.36 * px, px, COL['ink'], f0=f_w, dur=n - f_w, style='ExtraBold', align='left')
    t.stagger(f_w, by='character', gap=2, dy=-0.07, d=14, blur=0)
    rp = f'src.e_src_text_relative_{t.id}.position'
    t.key(rp, [(f_w, [0, -0.07], 'Linear'), (f_w + 6, [0, 0.012], 'Ease out'), (f_w + 10, [0, -0.004], 'S-curve'),
               (f_w + 14, [0, 0.0], 'S-curve')])
    tag = k.text("Tagline", "Toys that make you jump", 960, base + 90, 44, COL['ink'], f0=66, dur=n - 66, style='Bold', align='center')
    tag.rise(66, dy=24, d=14)


# ---------------------------------------------------------------- 5. swinging price tag (rigged)
def price_tag(d):
    n = 150
    name = "CT Price tag"
    k = d.comp(name, n, "cpt"); lab_bg(k, n)
    nx, ny = 960, 140
    tag = k.path("Tag", [(nx, 270), (nx + 220, 370), (nx + 220, 830), (nx - 220, 830), (nx - 220, 370)], f0=0, dur=n, closed=True)
    tag.fill(COL['yellow']); ink(tag, 10)
    hole = k.ell("Tag hole", nx, 335, 40, 40, COL['cream'], f0=0, dur=n); ink(hole, 6)
    sale = k.text("Sale", "SALE", nx, 420, 64, COL['red'], f0=0, dur=n, style='ExtraBold', align='center', track=1.1)
    old = k.text("Old price", "was $14", nx, 545, 54, COL['ink'], f0=0, dur=n, style='Bold', align='center')
    strike = k.line("Strike", [(nx - 115, 556), (nx + 115, 534)], COL['red'], px=10, f0=0, dur=n)
    strike.trim([(66, 0.0, 'Linear'), (74, 1.0, EXPO)], which='end')
    new = k.text("New price", "$9", nx, 715, 170, COL['red'], f0=76, dur=n - 76, style='ExtraBold', align='center')
    outline(new, 0.06)
    string = k.line("String", [(nx, ny), (nx, 335)], COL['ink'], px=6, f0=0, dur=n)
    nail = k.ell("Nail", nx, ny, 30, 30, COL['ink'], f0=0, dur=n)              # the visible pivot: everything turns about it
    rig([tag, hole, sale, old, strike, new, string], nail)
    # drops in from above the nail and swings down (true arcs about the nail), losing energy each swing;
    # then the new price stamps in and kicks one small wobble
    nail.rot([(0, 160.0, 'Linear'), (16, -38.0, 'S-curve'), (28, 21.0, 'S-curve'), (38, -10.0, 'S-curve'), (47, 4.0, 'S-curve'),
              (58, 0.0, 'S-curve'), (76, 0.0, 'Linear'), (80, 4.0, 'Ease out'), (90, 0.0, 'S-curve')])
    vol(name, new, [(76, [1.35, 1.35], 'Linear'), (80, [1.12, 0.88], 'Ease in'), (84, [0.95, 1.05], 'S-curve'),
                    (88, [1.02, 0.98], 'S-curve'), (92, [1.0, 1.0], 'S-curve')])
    new.op([(76, 0.0, 'Linear'), (78, 1.0, 'Linear')])
    # the words pop on once the big swing has passed (lint text_overlap compares axis-aligned boxes, and two
    # rotated words' boxes overlap while the tag is steep, although the words do not touch)
    for t, f in ((sale, 16), (old, 22)):
        t.scale(pop_keys(f, frm=0.6))
    sale.op([(16, 0.0, 'Linear'), (18, 1.0, 'Linear')])
    old.op([(22, 0.0, 'Linear'), (24, 1.0, 'Linear'), (66, 1.0, 'Linear'), (80, 0.55, 'S-curve')])


# ---------------------------------------------------------------- 6. boing arrow (rigged)
def boing_arrow(d):
    n = 90
    name = "CT Boing arrow"
    k = d.comp(name, n, "cba"); lab_bg(k, n)
    lab = k.text("Arrow label", "Tap here!", 520, 330, 72, COL['ink'], f0=0, dur=n, style='ExtraBold', align='center')
    lab.scale(pop_keys(0, frm=0.6)); lab.op([(0, 0.0, 'Linear'), (2, 1.0, 'Linear')])
    ax, ay, tx, ty = 560, 420, 1170, 610
    hin = (-260, 30)
    shaft = k.line("Arrow shaft", [(ax, ay), (tx, ty)], COL['ink'], px=14, f0=0, dur=n,
                   handles=[((0, 0), (40, 280), False), (hin, (0, 0), False)])
    shaft.trim([(6, 0.0, 'Linear'), (22, 1.0, EXPO)], which='end')
    ux, uy = -hin[0], -hin[1]; l = math.hypot(ux, uy); ux, uy = ux / l, uy / l
    nxv, nyv = -uy, ux
    head = k.line("Arrow head", [(tx - 54 * ux + 40 * nxv, ty - 54 * uy + 40 * nyv), (tx, ty), (tx - 54 * ux - 40 * nxv, ty - 54 * uy - 40 * nyv)],
                  COL['ink'], px=14, f0=18, dur=n - 18)
    head.op([(18, 0.0, 'Linear'), (20, 1.0, 'Linear')])
    tail = k.ell("Arrow tail", ax, ay, 26, 26, COL['ink'], f0=0, dur=n)      # the visible pivot at the tail
    rig([shaft, head], tail)
    # boing: the arrow stretches toward the target and springs back (x stretch, y squash: volume kept)
    vol(name, tail, [(22, [1.0, 1.0], 'Linear'), (26, [1.1, 0.92], 'Ease out'), (31, [0.95, 1.05], 'S-curve'),
                     (36, [1.03, 0.97], 'S-curve'), (41, [1.0, 1.0], 'S-curve')])
    bxp, byp = 1390, 620
    btn = k.ell("Target", bxp, byp, 220, 220, COL['green'], f0=0, dur=n); ink(btn, 10)
    go = k.text("Target label", "GO!", bxp, byp, 72, COL['white'], f0=0, dur=n, style='ExtraBold', align='center')
    outline(go, 0.07)
    poke = [(0, [0.0, 0.0], 'Linear'), (6, [1.1, 0.92], 'Ease out'), (10, [0.96, 1.04], 'S-curve'), (14, [1.0, 1.0], 'S-curve'),
            (26, [1.0, 1.0], 'Linear'), (28, [0.86, 1.14], 'Ease out'), (32, [1.06, 0.95], 'S-curve'), (36, [0.98, 1.02], 'S-curve'),
            (40, [1.0, 1.0], 'S-curve')]
    vol(name, btn, poke)
    vol(name, go, [(0, [0.6, 0.6], 'Linear')] + poke[1:])           # text pops from 0.6 (text_too_small)
    go.op([(0, 0.0, 'Linear'), (3, 0.0, 'Linear'), (5, 1.0, 'Linear')])  # after the button has grown past it


# ---------------------------------------------------------------- 7. comic POW
def comic_pow(d):
    n = 75
    name = "CT Comic pow"
    k = d.comp(name, n, "cpw"); lab_bg(k, n)
    for i in range(10):
        a = math.radians(i * 36 + 18)
        p0 = (960 + 330 * math.cos(a), 540 + 300 * math.sin(a)); p1 = (960 + 560 * math.cos(a), 540 + 470 * math.sin(a))
        ln = k.line(f"Action line {i + 1}", [p0, p1], COL['ink'], px=10, f0=2, dur=20)
        tp = ln.trim([(2, 0.0, 'Linear'), (8, 1.0, EXPO)], which='end')
        ln.key(tp + '.start', [(8, 0.0, 'Linear'), (20, 1.0, 'Ease in')])
    back = k.star("Burst back", 960, 540, 700, 16, 0.72, COL['red'], f0=2, dur=n - 2); ink(back, 10)
    back.scale(pop_keys(2, 1.16, 0.95, 1.02)); back.rot([(2, -8.0, 'Linear'), (n, -14.0, 'Linear')])
    front = k.star("Burst", 960, 540, 560, 13, 0.66, COL['yellow'], f0=0, dur=n); ink(front, 10)
    front.scale(pop_keys(0, 1.18, 0.94, 1.03)); front.rot([(0, 0.0, 'Linear'), (n, 6.0, 'Linear')])
    t = k.text("Pow", "POW!", 960, 540, 230, COL['red'], f0=3, dur=n - 3, style='ExtraBold', align='center')
    outline(t, 0.07); t.rotv(-8.0)
    # slams in from big, squashes on the 'impact', springs back (volume kept on the squash keys)
    vol(name, t, [(3, [2.4, 2.4], 'Linear'), (8, [1.16, 0.86], 'Ease in'), (12, [0.94, 1.06], 'S-curve'), (16, [1.02, 0.98], 'S-curve'),
                  (20, [1.0, 1.0], 'S-curve')])
    t.op([(3, 0.0, 'Linear'), (5, 1.0, 'Linear')])


# ---------------------------------------------------------------- 8. kids' lesson title card
def lesson_title(d):
    n = 150
    name = "CT Lesson title"
    k = d.comp(name, n, "clt"); lab_bg(k, n)
    cx, cy, cw, ch = 960, 580, 1320, 520
    card = k.rect("Card", cx, cy, cw, ch, COL['blue'], r=60, f0=0, dur=n, center=True); ink(card, 10)
    card.anchor(0, -1)                                    # lands on its bottom edge
    card.pos([(0, P(cx, -300), 'Linear'), (14, P(cx, cy), 'Ease in')])
    vol(name, card, [(0, [0.93, 1.07], 'Linear'), (13, [0.93, 1.07], 'Linear'), (15, [1.12, 0.86], 'Ease out'),
                     (19, [0.96, 1.04], 'S-curve'), (23, [1.02, 0.98], 'S-curve'), (27, [1.0, 1.0], 'S-curve')])
    sh = k.ell("Card shadow", cx, cy + ch / 2 + 16, 1100, 40, COL['shadow'], f0=0, dur=n)
    sh.scale([(0, 0.4, 'Linear'), (14, 1.0, 'Ease in')]); sh.op([(0, 0.0, 'Linear'), (14, 0.18, 'Ease in')])
    bx, by = 520, 330
    badge = k.rect("Badge", bx, by, 330, 92, COL['yellow'], r=46, f0=22, dur=n - 22, center=True); ink(badge, 6); badge.rotv(6.0)
    bt = k.text("Badge text", "LESSON 3", bx, by, 46, COL['ink'], f0=22, dur=n - 22, style='ExtraBold', align='center', track=1.05)
    bt.rotv(6.0)
    jelly = [(22, [0.0, 0.0], 'Linear'), (27, [1.12, 0.9], 'Ease out'), (31, [0.94, 1.06], 'S-curve'), (35, [1.02, 0.98], 'S-curve'),
             (39, [1.0, 1.0], 'S-curve')]
    vol(name, badge, jelly); vol(name, bt, jelly)
    star = k.star("Star", 1500, 340, 130, 5, 0.5, COL['yellow'], f0=36, dur=n - 36); ink(star, 6)
    star.scale(pop_keys(36, 1.25, 0.92, 1.03)); star.rot([(36, -40.0, 'Linear'), (44, 12.0, 'Ease out'), (50, -5.0, 'S-curve'),
                                                         (56, 0.0, 'S-curve')])
    t = k.text("Title", "Why do cats purr?", cx, 560, 116, COL['white'], f0=26, dur=n - 26, style='ExtraBold', align='center')
    outline(t, 0.08)
    t.stagger(26, by='character', gap=2, dy=0.12, d=18, blur=0)
    rp = f'src.e_src_text_relative_{t.id}.position'
    t.key(rp, [(26 + p_t * 18, [0, round(0.12 * (1 - p), 5)], 'Linear') for p_t, p in bake(named['bounce'], 18, 0.01)])
    s = k.text("Subtitle", "Science for curious kids", cx, 700, 48, COL['pale'], f0=62, dur=n - 62, style='Bold', align='center')
    s.rise(62, dy=24, d=14)


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear(); VOLUME.clear()
    walk_cycle(d); map_pin(d); thought_bubble(d); logo_reveal(d); price_tag(d); boing_arrow(d); comic_pow(d); lesson_title(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
