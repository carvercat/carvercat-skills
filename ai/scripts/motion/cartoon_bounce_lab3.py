"""Cartoon Bounce round 3 in design units: eight lab comps (walk cycle, map pin drop, thought bubble, squash-and-stretch logo
reveal, swinging price tag, boing arrow, comic POW, kids' lesson title card).

    import cartoon_bounce_lab3 as L; doc = L.build(); doc.send(client, PROJECT.carverproj)

Same palette and units as cartoon_bounce_lab.py (cc2: px, y down, degrees clockwise, CSS colours and easing). Every move is
baked as keys (no presets): springs are hand-set visible extremes (a baked spring's sub-pixel tail reads as lint 'jitter'), and
every squash keeps its volume (x * y between 0.9 and 1.05; VOLUME records the extremes per object and build() refuses anything
outside). Arcs are parabolas baked every 2 f, or rotation about a visible pivot. Rigs use a VISIBLE pivot (cc2 Obj.child); a
child is drawn above its parent, so the pivot is the lowest object of its rig. In the walk cycle the shorts are the pivot, so
the legs and the back arm now draw over the shorts (the old kit drew the shorts over them). Names, prices and places are sample
copy. Docs: ai/patterns/cartoon-bounce.md (round 3).
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cartoon_bounce_lab import (PDoc, COL as COL1, EXPO, BACK, W, H, lab_bg, txt, outline, bounce_letters, rise, origin, line, shape,
                                textw, css)
from curves import named, bake

PRESETS = []
VOLUME = {}                       # (comp, object) -> (min x*y, max x*y) over its non-uniform scale keys
COL = dict(COL1, map=css('CFEBC6'), road=css('FFFFFF'), river=css('9CCBFF'), pale=css('FFE7B8'))


def vol(comp, o, spec):
    """record x*y of every non-uniform scale key (squash and stretch keep volume)"""
    xs = [v[0] * v[1] for f, v, e in spec if isinstance(v, list) and abs(v[0] - v[1]) > 1e-9]
    if xs:
        lo, hi = min(xs), max(xs)
        assert 0.9 <= lo and hi <= 1.05, (comp, o.name, lo, hi)
        VOLUME[(comp, o.name)] = (round(lo, 3), round(hi, 3))
    o.scale(spec)


def arc(f0, f1, x0, y0, x1, y1, h, step=2):
    """a real parabola baked to keys every `step` frames: x linear in time, y = chord - 4 h t (1 - t) (h px above the chord at
    the middle). Returns [(f, (x, y))]."""
    out, n = [], max(1, int(round((f1 - f0) / step)))
    for i in range(n + 1):
        t = i / n
        out.append((f0 + (f1 - f0) * t, (x0 + (x1 - x0) * t, y0 + (y1 - y0) * t - 4 * h * t * (1 - t))))
    return out


def pop_keys(f, peak=1.12, low=0.95, over=1.02, gap=(4, 4, 4), frm=0.0):
    """uniform pop from frm with three visible extremes (no spring tail). Text pops from 0.6: lint text_too_small reads the
    line height on the first visible frame of the pop."""
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
    k.rect("Ground", 0, ground, W, 6, COL['ink'], f0=0, dur=n)
    # leg angle A(f), counter-clockwise positive as the walk is designed (negated where it is keyed): half step, 7 full steps, half step
    keysA = [(f_go, 0.0)] + [(f_go + 6 + i * step, th if i % 2 == 0 else -th) for i in range(8)]
    keysA.append((keysA[-1][0] + 6, 0.0))
    f_stop = keysA[-1][0]

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
    for o in [arm_b, leg_b, leg_f, body] + eyes + [arm_f]: pivot.child(o)
    for o in (arm_b, leg_b, leg_f, arm_f): origin(o, 0, 1)      # limbs turn about their top (hip, shoulder)
    # hips: baked every 2 f (x linear, y from the leg angle: a real bob, not a ping-pong of two keys)
    fs = [0, f_go] + list(range(f_go + 2, f_stop, 2)) + [f_stop]
    pivot.pos([(f, hip(f), 'Linear') for f in fs])
    sh.pos([(f, (hip(f)[0], ground + 3), 'Linear') for f in (0, f_go, f_stop)])
    # legs: Linear between extremes so the stance foot sweeps back at the hip's speed (design degrees run clockwise)
    leg_f.rot([(f, -a, 'Linear') for f, a in keysA]); leg_b.rot([(f, a, 'Linear') for f, a in keysA])
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
        arm.rot([(f, -sgn * a * 0.8, 'S-curve' if i else 'Linear') for i, (f, a) in enumerate(keysA)])
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
        r = line(k, f"Road {i + 1}", pts, COL['road'], px=22, f0=0, dur=n)
        r.op([(0, 0.0, 'Linear'), (8, 1.0, 'Ease out')])
    rv = line(k, "River", [(270, 820), (1650, 700)], COL['river'], px=30, f0=0, dur=n, handles=[(None, (380, -160)), ((-420, 200), None)])
    rv.op([(0, 0.0, 'Linear'), (8, 1.0, 'Ease out')])
    tx, ty, f_hit = 880, 680, 16                                  # the tip lands at (880, 680) on f16
    shd = k.ell("Pin shadow", tx, ty + 4, 110, 26, COL['shadow'], f0=0, dur=n)
    shd.scale([(0, 0.3, 'Linear'), (f_hit, 1.0, 'Ease in')]); shd.op([(0, 0.04, 'Linear'), (f_hit, 0.25, 'Ease in')])
    ring = k.ell("Landing ring", tx, ty + 4, 150, 44, None, f0=f_hit, dur=22); ink(ring, 6)
    ring.scale([(f_hit, 0.6, 'Linear'), (f_hit + 20, 1.9, EXPO)]); ring.op([(f_hit, 0.8, 'Linear'), (f_hit + 20, 0.0, 'Linear')])
    S = 1.4
    head = shape(k, "Pin head", [(tx, ty), (tx - 62 * S, ty - 112 * S), (tx, ty - 176 * S), (tx + 62 * S, ty - 112 * S)], COL['red'],
                 handles=[(None, None), ((0, 46 * S), (0, -34 * S)), ((-34 * S, 0), (34 * S, 0)), ((0, -34 * S), (0, 46 * S))],
                 f0=0, dur=n)
    ink(head, 10)
    dot = k.ell("Pin dot", tx, ty - 114 * S, 64, 64, COL['white'], f0=0, dur=n); ink(dot, 8)
    tip = k.ell("Pin tip", tx, ty, 16, 10, COL['ink'], f0=0, dur=n)            # the visible pivot at the point
    tip.child(head); tip.child(dot)
    tip.pos([(0, (tx, -40), 'Linear'), (f_hit, (tx, ty), 'Ease in')])           # falls, accelerating
    vol(name, tip, [(0, [0.88, 1.14], 'Linear'), (f_hit - 1, [0.86, 1.16], 'Linear'), (f_hit + 1, [1.22, 0.8], 'Ease out'),
                    (f_hit + 5, [0.92, 1.08], 'S-curve'), (f_hit + 9, [1.04, 0.96], 'S-curve'), (f_hit + 13, [1.0, 1.0], 'S-curve')])
    # the label pops out of the pin's side
    lx, ly = 1250, 420
    card = k.rect("Label card", lx, ly, 440, 150, COL['white'], r=34, f0=26, dur=n - 26, center=True); ink(card, 6)
    card.scale(pop_keys(26)); card.op([(26, 0.0, 'Linear'), (28, 1.0, 'Linear')])
    t1 = txt(k, "Place", "Pip's Bakery", lx, ly - 22, 54, COL['ink'], f0=30, dur=n - 30)
    t2 = txt(k, "Note", "OPEN TILL 6", lx, ly + 40, 34, COL['red'], f0=34, dur=n - 34, track=1.1)
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
        # every key a pair: a scalar key among pair keys is a uniform channel and the x/y channels would hold the blink's
        # first value (0.1 tall) back to the start
        e.scale([(f, [v, v] if not isinstance(v, list) else v, ea) for f, v, ea in
                 pop_keys(6) + [(84, 1.0, 'Linear'), (86, [1.1, 0.1], 'Ease in'), (90, 1.0, 'Ease out')]])
    # trail dots: small to big, along the line from the head to the cloud
    for i, (x, y, s) in enumerate([(650, 610, 40), (740, 530, 58), (850, 450, 80)]):
        o = k.ell(f"Trail {i + 1}", x, y, s, s, COL['white'], f0=12 + 4 * i, dur=n - 12 - 4 * i); ink(o, 6)
        o.scale(pop_keys(12 + 4 * i, 1.25, 0.92, 1.03, (3, 3, 3)))
    cx, cy = 1250, 330
    puffs = [(cx + 255 * math.cos(math.radians(a)), cy + 120 * math.sin(math.radians(a)), s)
             for a, s in [(0, 180), (45, 170), (90, 190), (135, 170), (180, 180), (225, 170), (270, 200), (315, 170)]]
    # the pivot is the ink core outline (the lowest object of the cloud, same ink as the puff outlines under the white fills)
    core_l = k.ell("Core line", cx, cy, 536, 276, COL['ink'], f0=24, dur=n - 24)
    outl = [k.ell(f"Puff line {i + 1}", x, y, s + 16, s + 16, COL['ink'], f0=24, dur=n - 24) for i, (x, y, s) in enumerate(puffs)]
    fill = [k.ell(f"Puff {i + 1}", x, y, s, s, COL['white'], f0=24, dur=n - 24) for i, (x, y, s) in enumerate(puffs)]
    core = k.ell("Cloud", cx, cy, 520, 260, COL['white'], f0=24, dur=n - 24)
    for o in outl + fill + [core]: core_l.child(o)
    # jelly in: pop, then squash/stretch extremes that keep the volume; then a slow 12 px float (one way, no loop)
    vol(name, core_l, [(24, [0.0, 0.0], 'Linear'), (30, [1.1, 0.92], 'Ease out'), (34, [0.94, 1.06], 'S-curve'),
                       (38, [1.03, 0.97], 'S-curve'), (42, [1.0, 1.0], 'S-curve')])
    core_l.pos([(42, (cx, cy), 'Linear'), (n, (cx, cy - 12), 'Linear')])
    t = txt(k, "Thought", "Snack time?", cx, cy, 80, COL['ink'], f0=36, dur=n - 36)
    t.scale(pop_keys(36, frm=0.6)); t.op([(36, 0.0, 'Linear'), (38, 1.0, 'Linear')])
    t.pos([(42, (t.base[0], t.base[1]), 'Linear'), (n, (t.base[0], t.base[1] - 12), 'Linear')])


# ---------------------------------------------------------------- 4. squash-and-stretch logo reveal
def logo_reveal(d):
    n = 120
    name = "CT Logo reveal"
    k = d.comp(name, n, "clr"); lab_bg(k, n)
    word, px = "bouncy", 190
    ww = textw(word, px, 800)
    r, gap = 70, 36
    total = 2 * r + gap + ww
    bx = 960 - total / 2 + r                             # the ball's rest centre (the logo mark)
    wx = bx + r + gap                                    # the word's left edge
    base = 600                                           # ground / baseline of the mark
    yc = base - r
    hits = [(14, 1500), (30, 1020), (42, bx)]            # contact frame, contact x (third hit = the mark), right to left
    sh = k.ell("Ball shadow", bx, base + 6, 150, 26, COL['shadow'], f0=0, dur=n)
    ball = k.ell("Logo ball", bx, yc, 2 * r, 2 * r, COL['red'], f0=0, dur=n); ink(ball, 8)
    origin(ball, 0, -1)                                  # squash on the ground: pivot at the bottom edge
    pts = arc(0, 14, 2040, yc - 360, hits[0][1], yc, 0)  # entering from the top right, accelerating (a falling half-parabola)
    pts = [(f, (x, (yc - 360) + 360 * ((f - 0) / 14) ** 2)) for f, (x, y) in pts]
    pts += arc(14, 30, hits[0][1], yc, hits[1][1], yc, 230)[1:]
    pts += arc(30, 42, hits[1][1], yc, hits[2][1], yc, 90)[1:]
    ball.pos([(f, (x, y), 'Linear') for f, (x, y) in pts])
    sh.pos([(f, (x, base + 6), 'Linear') for f, (x, y) in pts])
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
    t = txt(k, "Wordmark", word, wx, base - 0.36 * px, px, COL['ink'], f0=f_w, dur=n - f_w, align='left')
    # the word springs up: each letter starts 0.07 H low, overshoots 0.012 H high, settles (y is the top of the letter's box)
    top = t.box[1] - t.box[3] / 2
    t.stagger(by='chars', each=2, keyframes=[(0, {'y': top + 0.07 * H, 'opacity': 0.0}, 'Ease out'), (6, {'y': top - 0.012 * H}, 'S-curve'),
                                              (7, {'opacity': 1.0}, 'linear'), (10, {'y': top + 0.004 * H}, 'S-curve'), (14, {'y': top}, 'linear')])
    tag = txt(k, "Tagline", "Toys that make you jump", 960, base + 90, 44, COL['ink'], f0=66, dur=n - 66, weight=700)
    rise(tag, 66, dy=24, d=14)


# ---------------------------------------------------------------- 5. swinging price tag (rigged)
def price_tag(d):
    n = 150
    name = "CT Price tag"
    k = d.comp(name, n, "cpt"); lab_bg(k, n)
    nx, ny = 960, 140
    nail = k.ell("Nail", nx, ny, 30, 30, COL['ink'], f0=0, dur=n)              # the visible pivot: everything turns about it
    tag = shape(k, "Tag", [(nx, 270), (nx + 220, 370), (nx + 220, 830), (nx - 220, 830), (nx - 220, 370)], COL['yellow'], f0=0, dur=n)
    ink(tag, 10)
    hole = k.ell("Tag hole", nx, 335, 40, 40, COL['cream'], f0=0, dur=n); ink(hole, 6)
    sale = txt(k, "Sale", "SALE", nx, 420, 64, COL['red'], f0=0, dur=n, track=1.1)
    old = txt(k, "Old price", "was $14", nx, 545, 54, COL['ink'], f0=0, dur=n, weight=700)
    strike = line(k, "Strike", [(nx - 115, 556), (nx + 115, 534)], COL['red'], px=10, f0=0, dur=n)
    strike.trim([(66, 0.0, 'Linear'), (74, 1.0, EXPO)], which='end')
    new = txt(k, "New price", "$9", nx, 715, 170, COL['red'], f0=76, dur=n - 76)
    outline(new, 0.06)
    string = line(k, "String", [(nx, ny), (nx, 335)], COL['ink'], px=6, f0=0, dur=n)
    for o in (tag, hole, sale, old, strike, new, string): nail.child(o)
    # drops in from above the nail and swings down (true arcs about the nail), losing energy each swing;
    # then the new price stamps in and kicks one small wobble
    nail.rot([(0, -160.0, 'Linear'), (16, 38.0, 'S-curve'), (28, -21.0, 'S-curve'), (38, 10.0, 'S-curve'), (47, -4.0, 'S-curve'),
              (58, 0.0, 'S-curve'), (76, 0.0, 'Linear'), (80, -4.0, 'Ease out'), (90, 0.0, 'S-curve')])
    vol(name, new, [(76, [1.35, 1.35], 'Linear'), (80, [1.12, 0.88], 'Ease in'), (84, [0.95, 1.05], 'S-curve'),
                    (88, [1.02, 0.98], 'S-curve'), (92, [1.0, 1.0], 'S-curve')])
    new.op([(76, 0.0, 'Linear'), (78, 1.0, 'Linear')])
    # the words pop on once the big swing has passed (lint text_overlap compares axis-aligned boxes)
    for t, f in ((sale, 16), (old, 22)):
        t.scale(pop_keys(f, frm=0.6))
    sale.op([(16, 0.0, 'Linear'), (18, 1.0, 'Linear')])
    old.op([(22, 0.0, 'Linear'), (24, 1.0, 'Linear'), (66, 1.0, 'Linear'), (80, 0.55, 'S-curve')])


# ---------------------------------------------------------------- 6. boing arrow (rigged)
def boing_arrow(d):
    n = 90
    name = "CT Boing arrow"
    k = d.comp(name, n, "cba"); lab_bg(k, n)
    lab = txt(k, "Arrow label", "Tap here!", 520, 330, 72, COL['ink'], f0=0, dur=n)
    lab.scale(pop_keys(0, frm=0.6)); lab.op([(0, 0.0, 'Linear'), (2, 1.0, 'Linear')])
    ax, ay, tx, ty = 560, 420, 1170, 610
    hin = (-260, 30)
    tail = k.ell("Arrow tail", ax, ay, 26, 26, COL['ink'], f0=0, dur=n)      # the visible pivot at the tail
    shaft = line(k, "Arrow shaft", [(ax, ay), (tx, ty)], COL['ink'], px=14, f0=0, dur=n, handles=[(None, (40, 280)), (hin, None)])
    shaft.trim([(6, 0.0, 'Linear'), (22, 1.0, EXPO)], which='end')
    ux, uy = -hin[0], -hin[1]; l = math.hypot(ux, uy); ux, uy = ux / l, uy / l
    nxv, nyv = -uy, ux
    head = line(k, "Arrow head", [(tx - 54 * ux + 40 * nxv, ty - 54 * uy + 40 * nyv), (tx, ty), (tx - 54 * ux - 40 * nxv, ty - 54 * uy - 40 * nyv)],
                COL['ink'], px=14, f0=18, dur=n - 18)
    head.op([(18, 0.0, 'Linear'), (20, 1.0, 'Linear')])
    tail.child(shaft); tail.child(head)
    # boing: the arrow stretches toward the target and springs back (x stretch, y squash: volume kept)
    vol(name, tail, [(22, [1.0, 1.0], 'Linear'), (26, [1.1, 0.92], 'Ease out'), (31, [0.95, 1.05], 'S-curve'),
                     (36, [1.03, 0.97], 'S-curve'), (41, [1.0, 1.0], 'S-curve')])
    bxp, byp = 1390, 620
    btn = k.ell("Target", bxp, byp, 220, 220, COL['green'], f0=0, dur=n); ink(btn, 10)
    go = txt(k, "Target label", "GO!", bxp, byp, 72, COL['white'], f0=0, dur=n)
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
        ln = line(k, f"Action line {i + 1}", [p0, p1], COL['ink'], px=10, f0=2, dur=20)
        ln.trim([(2, 0.0, 'Linear'), (8, 1.0, EXPO)], which='end')
        ln.trim([(8, 0.0, 'Linear'), (20, 1.0, 'Ease in')], which='start')
    back = k.star("Burst back", 960, 540, 700, 16, 0.72, COL['red'], f0=2, dur=n - 2); ink(back, 10)
    back.scale(pop_keys(2, 1.16, 0.95, 1.02)); back.rot([(2, 8.0, 'Linear'), (n, 14.0, 'Linear')])
    front = k.star("Burst", 960, 540, 560, 13, 0.66, COL['yellow'], f0=0, dur=n); ink(front, 10)
    front.scale(pop_keys(0, 1.18, 0.94, 1.03)); front.rot([(0, 0.0, 'Linear'), (n, -6.0, 'Linear')])
    t = txt(k, "Pow", "POW!", 960, 540, 230, COL['red'], f0=3, dur=n - 3)
    outline(t, 0.07); t.rotv(8.0)
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
    origin(card, 0, -1)                                   # lands on its bottom edge
    card.pos([(0, (cx, -300), 'Linear'), (14, (cx, cy), 'Ease in')])
    vol(name, card, [(0, [0.93, 1.07], 'Linear'), (13, [0.93, 1.07], 'Linear'), (15, [1.12, 0.86], 'Ease out'),
                     (19, [0.96, 1.04], 'S-curve'), (23, [1.02, 0.98], 'S-curve'), (27, [1.0, 1.0], 'S-curve')])
    sh = k.ell("Card shadow", cx, cy + ch / 2 + 16, 1100, 40, COL['shadow'], f0=0, dur=n)
    sh.scale([(0, 0.4, 'Linear'), (14, 1.0, 'Ease in')]); sh.op([(0, 0.0, 'Linear'), (14, 0.18, 'Ease in')])
    bx, by = 520, 330
    badge = k.rect("Badge", bx, by, 330, 92, COL['yellow'], r=46, f0=22, dur=n - 22, center=True); ink(badge, 6); badge.rotv(-6.0)
    bt = txt(k, "Badge text", "LESSON 3", bx, by, 46, COL['ink'], f0=22, dur=n - 22, track=1.05)
    bt.rotv(-6.0)
    jelly = [(22, [0.0, 0.0], 'Linear'), (27, [1.12, 0.9], 'Ease out'), (31, [0.94, 1.06], 'S-curve'), (35, [1.02, 0.98], 'S-curve'),
             (39, [1.0, 1.0], 'S-curve')]
    vol(name, badge, jelly); vol(name, bt, jelly)
    star = k.star("Star", 1500, 340, 130, 5, 0.5, COL['yellow'], f0=36, dur=n - 36); ink(star, 6)
    star.scale(pop_keys(36, 1.25, 0.92, 1.03)); star.rot([(36, 40.0, 'Linear'), (44, -12.0, 'Ease out'), (50, 5.0, 'S-curve'),
                                                         (56, 0.0, 'S-curve')])
    t = txt(k, "Title", "Why do cats purr?", cx, 560, 116, COL['white'], f0=26, dur=n - 26)
    outline(t, 0.08)
    bounce_letters(t, 26, each=2)
    s = txt(k, "Subtitle", "Science for curious kids", cx, 700, 48, COL['pale'], f0=62, dur=n - 62, weight=700)
    rise(s, 62, dy=24, d=14)


def build():
    d = PDoc(PRESETS)
    PRESETS.clear(); VOLUME.clear()
    walk_cycle(d); map_pin(d); thought_bubble(d); logo_reveal(d); price_tag(d); boing_arrow(d); comic_pow(d); lesson_title(d)
    return d


if __name__ == "__main__":
    print(__doc__)
