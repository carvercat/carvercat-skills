"""Funky round 3 in design units: eight lab comps for briefs the pack could not serve before (gig poster, menu special, new drop
reveal, marquee bands, blob photo frame, party invite, countdown, zine quote).

    import funky_lab3 as L; doc = L.build(); doc.send(client, PROJECT.carverproj)

Same palette, units and rules as funky_lab.py (cc2: px, y down, degrees CLOCKWISE; the angles below are written as the old kit
stored them, counter-clockwise, and every rotation is negated where it is keyed): rotation is part of every entrance, and
anything that keeps moving moves ONE way (lint reads ping-pong as jitter). Every move is baked as keys (no presets): stamp(),
pop(), slide_in() and spin_in() write the pack's sticker slam, the badge pop, Slide in - wiggle and Spin in as keys. The blob
frame uses a scene mask (Comp.mask: the window cuts the photo). Names, dates, prices and photos are stand-ins (invented).
Plates behind text are sized with textw (needs Pillow). Fonts: Rethink Sans must be installed (KI-136). Docs: ai/patterns/funky.md
(round 3).
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from funky_lab import (PDoc, COL, EXPO, BACK, POP, W, H, lab_bg, zigzag, txt, textw, hard_shadow, SY, origin, line, shape, css)

MUTED = css('8A7FA8')            # stand-in labels on photo panels
PRESETS = []
WEIGHT = {'ExtraBold': 800, 'Bold': 700}


# ---------------------------------------------------------------- baked moves (angles counter-clockwise as designed)
def stamp(o, f, ang=0.0, s0=1.45, d=8, turn=10.0):
    """sticker slam: size s0 -> 1 on the back curve, opaque in 2 f, and a turn of `turn` degrees into the final angle `ang`"""
    o.scale([(f, s0, 'Linear'), (f + d, 1.0, BACK)])
    o.op([(f, 0.0, 'Linear'), (f + 2, 1.0, 'Linear')])
    if turn: o.rot([(f, -(ang + turn), 'Linear'), (f + d, -ang, BACK)])
    else: o.rotv(-ang)
    return o


def pop(o, f, d=12, s0=0.0, ang=None, turn=-14.0):
    """badge pop for shapes (Tilt pop as keys): size s0 -> 1 on the pop curve, opaque in 3 f, angle ang+turn -> ang"""
    o.scale([(f, s0, 'Linear'), (f + d, 1.0, POP)])
    o.op([(f, 0.0, 'Linear'), (f + 3, 1.0, 'Linear')])
    if ang is not None: o.rot([(f, -(ang + turn), 'Linear'), (f + d, -ang, POP)])
    return o


def slide_in(o, f, d=14, dx=500.0, ang=0.0, turn=12.0):
    """Slide in - wiggle as keys: from dx px to the right on expo, angle ang+turn -> ang on the pop curve"""
    bx, by = o.base
    o.pos([(f, (bx + dx, by), 'Linear'), (f + d, (bx, by), EXPO)])
    o.rot([(f, -(ang + turn), 'Linear'), (f + d + 4, -ang, POP)])
    return o


def spin_in(o, f, d=16, s0=0.3, turn=-180.0):
    """Spin in as keys: angle turn -> 0 (expo), size s0 -> 1 (back), opaque in 4 f"""
    o.rot([(f, -turn, 'Linear'), (f + d, 0.0, EXPO)])
    o.scale([(f, s0, 'Linear'), (f + d, 1.0, BACK)])
    o.op([(f, 0.0, 'Linear'), (f + 4, 1.0, 'Linear')])
    return o


def drift_spin(o, f, n, a0, a1):
    """after landing, keep turning one way (linear), on the same rotation lane; no second key on the landing frame (two keys on
    one frame are a lint error, same_frame_keys)"""
    cur = [(kf + o.f0, v, e) for kf, v, e in o.tracks.get('rotate', [])]
    have = {r[0] for r in cur}
    add = ([] if f in have else [(f, -a0, 'Linear')]) + [(n, -a1, 'Linear')]
    return o.rot(sorted(cur + add, key=lambda r: r[0]))


def fade(o, f, d=6):
    return o.op([(f, 0.0, 'Linear'), (f + d, 1.0, 'Ease out')])


def rise(o, f, d=10, dy=24):
    bx, by = o.base
    o.pos([(f, (bx, by + dy), 'Linear'), (f + d, (bx, by), EXPO)])
    return fade(o, f, 5)


def draw(o, f, d=14):
    o.trim([(f, 0.0, 'Linear'), (f + d, 1.0, EXPO)]); return o


def grow_x(o, f, d=10, ax=-1):
    origin(o, ax, 0); o.scale([(f, [0.0, 1.0], 'Linear'), (f + d, [1.0, 1.0], EXPO)]); return o


def plate_text(k, name, s, x, y, px, fg, bg, f0, n, style='ExtraBold', padx=36, h=None, r=None, stroke=6):
    """a text on its own rounded plate; returns (plate, text, plate width)"""
    w = textw(s, px, WEIGHT[style]) + 2 * padx; h = h or round(px * 1.25)
    pl = k.rect(name + " plate", x, y, w, h, bg, r=r if r is not None else h / 2, f0=f0, dur=n - f0, center=True)
    if stroke: pl.stroke(COL['ink'], stroke)
    t = txt(k, name, s, x, y, px, fg, f0=f0, dur=n - f0, weight=WEIGHT[style])
    return pl, t, w


BLOB = [1.0, 0.84, 1.1, 0.9, 1.04, 0.8, 1.08]


def blob_pts(cx, cy, r, wob, phase=0.0, m=7):
    """a closed smooth blob: m nodes on a circle of radius r scaled by BLOB (wob 0..1 sets how lumpy), tangent handles
    [(in, out)] in px"""
    pts, hs = [], []
    k = 4.0 / 3.0 * math.tan(math.pi / (2 * m))
    for i in range(m):
        a = phase + 2 * math.pi * i / m
        rr = r * (1 + (BLOB[i % len(BLOB)] - 1) * wob)
        x, y = cx + rr * math.cos(a), cy + rr * math.sin(a)
        tx, ty = -math.sin(a) * rr * k, math.cos(a) * rr * k
        pts.append((x, y)); hs.append(((-tx, -ty), (tx, ty)))
    return pts, hs


# ---------------------------------------------------------------- 1. gig poster (music event)
def gig_poster(d):
    n = 150
    k = d.comp("FK Gig poster", n, "fgp"); lab_bg(k, n)
    # the record: grooves and a scalloped label that keeps spinning one way
    rx, ry = 1440, 500
    rec = [k.ell("Record", rx, ry, 500, 500, COL['ink'], f0=0, dur=n)]
    for i, dia in enumerate((420, 340)):
        g = k.ell(f"Groove {i + 1}", rx, ry, dia, dia, None, f0=0, dur=n); g.stroke(css('3A2C66'), 4); rec.append(g)
    lab = k.star("Record label", rx, ry, 190, 10, 0.8, COL['orange'], f0=0, dur=n); rec.append(lab)
    hole = k.ell("Record hole", rx, ry, 26, 26, COL['peach'], f0=0, dur=n); rec.append(hole)
    for o in rec:
        bx, by = o.base
        o.pos([(0, (bx + 700, by), 'Linear'), (16, (bx, by), EXPO)])
    lab.rot([(0, -120.0, 'Linear'), (16, 0.0, EXPO), (n, 200.0, 'Linear')])      # rolls in, then keeps turning one way
    x0 = 190
    kick = txt(k, "Kicker", "LIVE MUSIC", x0, 226, 48, COL['teal'], f0=0, dur=n, align='left', track=1.2)
    stamp(kick, 0, 0.0, 1.3, turn=0)
    # stacked big lines slam from 1.15, not the sticker's 1.45: from 1.45 the growing box covered the kicker (lint
    # text_overlap); wide lines turn only 4 deg over 12 f, or their far ends sweep into the next line and jump speed
    l1 = txt(k, "Headliner 1", "SUNNY &", x0, 410, 160, COL['orange'], f0=4, dur=n - 4, align='left')
    hard_shadow(l1, COL['purple'], 10); stamp(l1, 4, 2.0, 1.15, d=12, turn=4.0)
    l2 = txt(k, "Headliner 2", "THE SPROCKETS", x0, 590, 116, COL['pink'], f0=16, dur=n - 16, align='left')
    hard_shadow(l2, COL['purple'], 8); stamp(l2, 16, 2.0, 1.15, d=12, turn=4.0)
    dw = textw("FRI 14 NOV", 64, 800) + 80
    dt = k.rect("Date plate", x0 + dw / 2, 742, dw, 100, COL['yellow'], r=50, f0=22, dur=n - 22, center=True)
    dt.stroke(COL['ink'], 8); stamp(dt, 22, -4.0)
    stamp(txt(k, "Date", "FRI 14 NOV", x0 + dw / 2, 742, 64, COL['ink'], f0=22, dur=n - 22), 22, -4.0)
    rise(txt(k, "Venue", "The Velvet Room  ·  doors 8 pm", x0, 864, 48, COL['ink'], f0=34, dur=n - 34, weight=700, align='left'), 34)
    draw(line(k, "Wave", zigzag(x0 + dw + 40, x0 + dw + 360, 742, 16, 10), COL['teal'], px=12, f0=28, dur=n - 28), 28, 16)


# ---------------------------------------------------------------- 2. menu / food special
def menu_special(d):
    n = 150
    k = d.comp("FK Menu special", n, "fmn"); lab_bg(k, n)
    x0 = 190
    rw = textw("TODAY'S SPECIAL", 52, 800) + 90
    rib = k.rect("Ribbon", x0 + rw / 2, 250, rw, 96, COL['pink'], f0=0, dur=n, center=True); rib.rotv(-3.0)
    grow_x(rib, 0, 10)
    fade(txt(k, "Ribbon text", "TODAY'S SPECIAL", x0 + rw / 2, 250, 52, COL['white'], f0=4, dur=n - 4), 4, 4).rotv(-3.0)
    d1 = txt(k, "Dish 1", "SPICY MANGO", x0, 410, 120, COL['orange'], f0=8, dur=n - 8, align='left')
    hard_shadow(d1, COL['ink'], 8); stamp(d1, 8, 0.0, 1.15, d=12, turn=4.0)
    d2 = txt(k, "Dish 2", "TACOS", x0, 574, 170, COL['purple'], f0=16, dur=n - 16, align='left')
    hard_shadow(d2, COL['ink'], 10); stamp(d2, 16, 0.0, 1.15)
    rise(txt(k, "Description", "slow-cooked, lime slaw, chilli crunch", x0, 714, 44, COL['ink'], f0=28, dur=n - 26, weight=700,
             align='left'), 28)
    sw = textw("Served 12 – 3 pm", 46, 800) + 80
    pl = k.rect("Served plate", x0 + sw / 2, 836, sw, 90, COL['teal'], r=45, f0=36, dur=n - 36, center=True)
    pl.stroke(COL['ink'], 6); stamp(pl, 36, -3.0)
    stamp(txt(k, "Served", "Served 12 – 3 pm", x0 + sw / 2, 836, 46, COL['white'], f0=36, dur=n - 36), 36, -3.0)
    px, py = 1390, 560
    plate = k.ell("Dish plate", px, py, 560, 560, COL['white'], f0=4, dur=n - 4); plate.stroke(COL['ink'], 10)
    photo = k.ell("Dish photo", px, py, 440, 440, COL['teal'], f0=4, dur=n - 4)
    for o in (plate, photo): spin_in(o, 4, 18)
    fade(txt(k, "Photo label", "dish photo", px, py, 34, COL['white'], f0=14, dur=n - 14, weight=700), 14, 8)
    st = k.star("Price badge", 1640, 320, 250, 14, 0.8, COL['yellow'], f0=24, dur=n - 24); st.stroke(COL['ink'], 8)
    pop(st, 24, 12, 0.0, 0.0, -20.0); drift_spin(st, 36, n, 0.0, -30.0)
    stamp(txt(k, "Price", "$9", 1640, 320, 110, COL['ink'], f0=26, dur=n - 26), 26, 8.0)


# ---------------------------------------------------------------- 3. new drop (streetwear reveal)
def new_drop(d):
    n = 120
    k = d.comp("FK New drop", n, "fnd"); lab_bg(k, n)
    x0 = 190
    fade(txt(k, "Collection", "COLLECTION 03", x0, 206, 40, COL['purple'], f0=0, dur=n, align='left', track=1.4), 0, 6)
    w1 = txt(k, "New", "NEW", x0, 404, 220, COL['yellow'], f0=2, dur=n - 2, align='left')
    hard_shadow(w1, COL['ink'], 12); stamp(w1, 2, 4.0, 1.15, d=9, turn=12.0)
    w2 = txt(k, "Drop", "DROP", x0, 624, 220, COL['pink'], f0=12, dur=n - 12, align='left')
    hard_shadow(w2, COL['ink'], 12); stamp(w2, 12, 4.0, 1.15, d=9, turn=-12.0)
    tw = textw("DROPS FRI 6 PM", 50, 800) + 100
    tape = k.rect("Tape", x0 + tw / 2, 830, tw, 92, COL['ink'], f0=22, dur=n - 22, center=True); tape.rotv(2.0)
    grow_x(tape, 22, 10)
    fade(txt(k, "Tape text", "DROPS FRI 6 PM", x0 + tw / 2, 830, 50, COL['yellow'], f0=26, dur=n - 26), 26, 4).rotv(2.0)
    px, py = 1350, 540
    pan = k.rect("Product panel", px, py, 560, 660, COL['teal'], r=24, f0=10, dur=n - 10, center=True)
    pan.stroke(COL['ink'], 8)
    pan.key('dropShadow', [(24, '0px 0px 0px %s' % COL['purple'], 'Linear'), (34, '22px %gpx 0px %s' % (round(22 * SY, 3), COL['purple']), EXPO)])  # the slab steps out after it lands
    slide_in(pan, 10, 14, 620.0, -3.0, 12.0)
    lbl = txt(k, "Product label", "product shot", px, py, 36, COL['white'], f0=10, dur=n - 10, weight=700)
    slide_in(lbl, 10, 14, 620.0, -3.0, 12.0)
    for i, (x, y, col) in enumerate([(1660, 250, COL['yellow']), (1050, 860, COL['pink']), (1700, 820, COL['orange'])]):
        f = 32 + i * 4
        s = k.star(f"Spark {i + 1}", x, y, 90, 4, 0.4, col, f0=f, dur=n - f); s.stroke(COL['ink'], 4)
        spin_in(s, f, 14); drift_spin(s, f + 14, n, 0.0, 40.0 if i % 2 else -40.0)


# ---------------------------------------------------------------- 4. marquee bands
MQ = [(["FRESH", "FUNKY", "LOUD"], COL['pink'], COL['white'], 415.0, -100.0, -1),
      (["NEW SOUNDS", "NEW FACES"], COL['yellow'], COL['ink'], 770.0, 100.0, 1)]


def marquee(d):
    n = 150
    k = d.comp("FK Marquee bands", n, "fmq"); lab_bg(k, n)
    hh, px = 85, 84                                     # half band height, text size
    sp = textw(" ", px, 800)
    for b, (words, bg, fg, yc, rise_, way) in enumerate(MQ):
        # band centre line: y = yc + rise_ * (x / 1920 - 0.5); a parallelogram that ends exactly at the frame edges
        y0, y1 = yc - rise_ / 2, yc + rise_ / 2
        band = shape(k, f"Band {b + 1}", [(0, y0 - hh), (W, y1 - hh), (W, y1 + hh), (0, y0 + hh)], bg, f0=0, dur=n)
        band.stroke(COL['ink'], 8)
        origin(band, -1 if way < 0 else 1, 0)
        band.scale([(b * 6, [0.0, 1.0], 'Linear'), (b * 6 + 12, [1.0, 1.0], EXPO)])
        ang = math.degrees(math.atan2(-rise_, W))         # the band's slope, counter-clockwise as the old kit measured it
        ux, uy = math.cos(math.radians(ang)), -math.sin(math.radians(ang))   # unit vector along the band (screen px)
        # one text per word ("WORD •"), each a step of its own width + one space; the whole cycle of words is the period U, and
        # every word travels exactly U in the clip, so the last frame matches the first (seamless loop)
        ws = [textw(w + " •", px, 800) + sp for w in words]
        U = sum(ws)
        pos, x = [], -2 * U
        while x < 2 * U:
            for w, wd in zip(words, ws):
                pos.append((w, x + wd / 2, wd)); x += wd
        i = 0
        for w, off, wd in pos:
            cx, cy = 960 + off * ux, yc + off * uy
            ex, ey = cx + way * U * ux, cy + way * U * uy
            t0 = (8 + b * 6 + 6) / n                       # opaque from here: a word on screen only while transparent is never_visible
            if not any(-wd / 2 < cx + (ex - cx) * t < 1920 + wd / 2 for t in [t0 + (1 - t0) * j / 20 for j in range(21)]):
                continue                                   # off frame (or transparent) for the whole clip: lint never_visible
            i += 1
            t = txt(k, f"Band {b + 1} word {i}", w + " •", cx, cy, px, fg, f0=0, dur=n)
            t.rotv(round(-ang, 3))
            oy = t.base[1] - cy
            t.pos([(0, (cx, cy + oy), 'Linear'), (n, (ex, ey + oy), 'Linear')])
            fade(t, 8 + b * 6, 6)


# ---------------------------------------------------------------- 5. blob photo frame
def blob_frame(d):
    n = 120
    k = d.comp("FK Blob frame", n, "fbf"); lab_bg(k, n)
    cx, cy = 720, 540
    pts, hs = blob_pts(cx, cy, 310, 1.0)
    back = shape(k, "Blob back", [(x + 30, y + 30) for x, y in pts], COL['purple'], handles=hs, f0=2, dur=n - 2)
    pop(back, 2, 14); drift_spin(back, 16, n, 0.0, 30.0)
    ph = k.rect("Photo", cx, cy, 760, 760, COL['orange'], f0=0, dur=n, center=True)
    ph.gradient([(0, COL['orange']), (1, COL['pink'])], start=(cx, cy - 380), end=(cx, cy + 380))
    ph.scale([(0, 1.0, 'Linear'), (n, 1.06, 'Linear')])                         # a slow push inside the window
    fade(txt(k, "Photo label", "photo", cx, cy, 40, COL['white'], f0=10, dur=n - 10, weight=700), 10, 8)
    win = shape(k, "Blob window", pts, COL['white'], handles=hs, f0=0, dur=n)
    pop(win, 0, 14); drift_spin(win, 14, n, 0.0, 30.0)
    k.mask(ph, win)
    rp, rh = blob_pts(cx, cy, 360, 0.8, phase=0.5)
    ring = shape(k, "Blob ring", rp, None, handles=rh, f0=6, dur=n - 6).set('fill', 'none')
    ring.stroke(COL['ink'], 8); pop(ring, 6, 14); drift_spin(ring, 20, n, 0.0, -30.0)
    sx = 1390
    pl, t, w = plate_text(k, "Name", "MEET MIRA", sx, 430, 84, COL['ink'], COL['yellow'], 18, n)
    stamp(pl, 18, -4.0); stamp(t, 18, -4.0)
    rise(txt(k, "Role", "head of snacks", sx, 560, 52, COL['purple'], f0=30, dur=n - 30), 30)
    for i, (x, y, col) in enumerate([(1130, 250, COL['teal']), (1060, 820, COL['pink'])]):
        f = 26 + i * 5
        s = k.star(f"Spark {i + 1}", x, y, 80, 4, 0.4, col, f0=f, dur=n - f)
        spin_in(s, f, 14); drift_spin(s, f + 14, n, 0.0, 40.0 if i else -40.0)


# ---------------------------------------------------------------- 6. party invite
DETAILS = [("SAT 22 NOV", COL['teal']), ("8 PM", COL['orange']), ("ROOFTOP AT LUNA", COL['yellow'])]


def party_invite(d):
    n = 150
    k = d.comp("FK Party invite", n, "fpi"); lab_bg(k, n)
    import random
    rnd = random.Random(7)
    cols = [COL['pink'], COL['teal'], COL['purple'], COL['orange'], COL['yellow']]
    for i in range(14):                                 # confetti falls one way, only in the side lanes (no pattern under words)
        x = rnd.uniform(70, 270) if i % 2 == 0 else rnd.uniform(1660, 1850)   # the detail row spans x 335-1585
        f = 6 + (i * 7) % 40
        y0 = rnd.uniform(-180, -40); y1 = y0 + rnd.uniform(1150, 1350)
        if i % 3 == 0: c = k.ell(f"Confetti {i + 1}", x, y0, 26, 26, cols[i % 5], f0=f, dur=n - f)
        else: c = k.rect(f"Confetti {i + 1}", x, y0, 20, 44, cols[i % 5], r=4, f0=f, dur=n - f, center=True)
        bx, by = c.base
        c.pos([(f, (bx, by), 'Linear'), (n, (bx + rnd.uniform(-30, 30), by + (y1 - y0)), 'Linear')])
        c.rot([(f, 0.0, 'Linear'), (n, -rnd.choice([-1, 1]) * min(360.0, rnd.uniform(200, 420)), 'Linear')])   # a rotate key stops at 360 deg (the old kit's 420 is capped)
    kick = txt(k, "Kicker", "YOU'RE INVITED", 960, 240, 50, COL['purple'], f0=0, dur=n, track=1.3)
    stamp(kick, 0, 0.0, 1.3, turn=0)
    h = txt(k, "Headline", "Mia turns 30!", 960, 410, 170, COL['pink'], f0=5, dur=n - 5)
    hard_shadow(h, COL['ink'], 12); stamp(h, 5, 2.0)
    px, gap = 56, 44
    ws = [textw(s, px, 800) + 76 for s, _ in DETAILS]
    x = 960 - (sum(ws) + gap * (len(ws) - 1)) / 2
    for i, ((s, col), w) in enumerate(zip(DETAILS, ws)):
        f, ang = 22 + i * 6, (-4.0, 3.0, -2.0)[i]
        pl = k.rect(f"Detail {i + 1} plate", x + w / 2, 630, w, 96, col, r=48, f0=f, dur=n - f, center=True)
        pl.stroke(COL['ink'], 6); stamp(pl, f, ang)
        stamp(txt(k, f"Detail {i + 1}", s, x + w / 2, 630, px, COL['ink'], f0=f, dur=n - f), f, ang)
        x += w + gap
    rise(txt(k, "RSVP", "RSVP by 15 Nov", 960, 790, 46, COL['ink'], f0=44, dur=n - 44, weight=700), 44)


# ---------------------------------------------------------------- 7. countdown 3-2-1-GO
BEATS = [("3", COL['pink']), ("2", COL['teal']), ("1", COL['orange']), ("GO!", COL['purple'])]


def countdown(d):
    per = 30
    n = per * len(BEATS)
    k = d.comp("FK Countdown", n, "fcd"); lab_bg(k, n)
    for i, (s, col) in enumerate(BEATS):
        f = i * per
        b = k.star(f"Burst {i + 1}", 960, 540, 700, 16, 0.72, col, f0=f, dur=per); b.stroke(COL['ink'], 8)
        b.scale([(f, 0.4, 'Linear'), (f + 10, 1.0, POP)])
        b.rot([(f, 0.0, 'Linear'), (f + per, 40.0 if i % 2 else -40.0, 'Linear')])      # each burst turns one way
        disc = k.ell(f"Disc {i + 1}", 960, 540, 400, 400, COL['ink'], f0=f, dur=per)
        disc.scale([(f, 0.6, 'Linear'), (f + 8, 1.0, POP)])
        t = txt(k, f"Count {i + 1}", s, 960, 540, 260 if len(s) == 1 else 160, COL['yellow'], f0=f, dur=per)
        hard_shadow(t, col, 10); stamp(t, f, 0.0, 1.6, d=8, turn=-14.0)


# ---------------------------------------------------------------- 8. zine quote (cut-out words)
ZINE = [[("MAKE", 130, 'ExtraBold', 'white', 'ink'), ("IT", 110, 'Bold', 'ink', 'yellow'), ("LOUD,", 150, 'ExtraBold', 'white', 'pink')],
        [("MAKE", 120, 'Bold', 'ink', 'teal'), ("IT", 130, 'ExtraBold', 'yellow', 'purple'), ("YOURS.", 150, 'ExtraBold', 'ink', 'orange')]]
ZANG = [-5.0, 3.0, -2.0, 4.0, -4.0, 2.0]


def zine_quote(d):
    n = 150
    k = d.comp("FK Zine quote", n, "fzq"); lab_bg(k, n)
    gap, i = 36, 0
    for li, (line_, y) in enumerate(zip(ZINE, (380, 610))):
        ws = [textw(s, px, WEIGHT[st]) + 56 for s, px, st, _, _ in line_]
        x = 960 - (sum(ws) + gap * (len(ws) - 1)) / 2
        for (s, px, st, fg, bg), w in zip(line_, ws):
            f, ang = 4 + i * 6, ZANG[i]
            h = round(px * 1.05)
            pl = k.rect(f"Word {i + 1} plate", x + w / 2, y, w, h, COL[bg], r=8, f0=f, dur=n - f, center=True)
            pl.stroke(COL['ink'], 5); stamp(pl, f, ang, 1.4, turn=8.0 if i % 2 else -8.0)
            stamp(txt(k, f"Word {i + 1}", s, x + w / 2, y, px, COL[fg], f0=f, dur=n - f, weight=WEIGHT[st]),
                  f, ang, 1.4, turn=8.0 if i % 2 else -8.0)
            x += w + gap; i += 1
    aw = textw("— Rosa, 9, on her first drum kit", 42, 700)
    tape = k.rect("Tape", 960 - aw / 2 - 90, 800, 120, 44, css('FFD000', 0.75), f0=46, dur=n - 46, center=True)
    stamp(tape, 46, 20.0, 1.3, turn=0)
    rise(txt(k, "Credit", "— Rosa, 9, on her first drum kit", 960, 800, 42, COL['ink'], f0=48, dur=n - 48, weight=700), 48)


def build():
    d = PDoc(PRESETS)
    PRESETS.clear()
    gig_poster(d); menu_special(d); new_drop(d); marquee(d); blob_frame(d); party_invite(d); countdown(d); zine_quote(d)
    return d


if __name__ == "__main__":
    print(__doc__)
