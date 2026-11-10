"""Retro round 3 in design units: eight lab comps (80s action movie title, mixtape tracklist, 90s "under construction" page,
film countdown leader, pixel level-up, 70s TV ident, polaroid memory, retro weather map).

    import retro_lab3 as L; doc = L.build(); doc.send(client, PROJECT.carverproj)

Same palette and "on twos" rule as retro_lab.py (whose helpers this uses). Every move is baked as keys (no presets):
rise2() is "Rise - on twos", pop2() is "Pop - on twos", and group2() moves a set of parts as one rigid object (shared centre,
angle and size), keyed on twos, so a polaroid or an extruded title turns and grows as one piece without parenting. Things that
keep moving after they land (reels, sun rays, hazard stripes, clouds) move one way at constant speed and are not stepped.
Blinks use Hold keys 15 f or more apart. Names, titles, dates, places and numbers are invented stand-ins.
Design units: px from the top-left, y down, degrees CLOCKWISE (group2 takes a counter-clockwise angle a, as the old kit did,
and writes -a). Docs: ai/patterns/retro.md (round 3).
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from retro_lab import (EASE_OUT, PDoc, fit_box, COL, EXPO, W, H, css, twos, hold_keys, anchor, more, glow, hard_shadow, text, line, lab_bg,
                       text_gradient, named)
from cc2 import bezier
from cc import textw

WHITE = css('FBF8F0')
INK = css('2B1A10')


def rise2(o, f, d=16, dy=43.0):
    """Rise - on twos as keys: up from dy px below on expo, stepped every 2 f; opaque on twos over the first 4 f"""
    bx, by = o.base
    o.pos(twos(f, f + d, (bx, by + dy), (bx, by), 'expo-out'))
    o.op(twos(f, f + 4, 0.0, 1.0, 'linear'))
    return o


def pop2(o, f, d=12, curve='spring-gentle', s0=0.0, s1=1.0):
    o.scale(twos(f, f + d, s0, s1, curve)); return o


def grow2(o, f, d=12, ax=-1):
    anchor(o, ax, 0); o.scale(twos(f, f + d, [0.0, 1.0], [1.0, 1.0], 'expo-out')); return o


def spin(o, f0, f1, dpf, sym):
    """constant clockwise turning, dpf degrees a frame, for a shape that looks the same every `sym` degrees. A scene rotate key
    stays within 360 degrees, so the turn is keyed in runs of at most 300: each run ends on a Hold key that jumps by a whole
    number of symmetry steps minus the frame's turn (invisible), and the next run goes on."""
    run = int(300 // dpf); keys, f, v = [(f0, 0.0, 'Linear')], f0, 0.0
    while f < f1:
        g = min(f1, f + run); v += (g - f) * dpf; keys.append((g, round(v, 4), 'Linear')); f = g
        if f < f1:
            v = round(v % sym + dpf, 4); f += 1; keys.append((f, v, 'Hold'))      # same picture as the unwrapped angle
            v_next = v
    return o.rot(keys)


def steps(f0, f1, curve):
    out, f = [], f0
    while f <= f1:
        out.append((f, 1.0 if f + 2 > f1 else named[curve]((f - f0) / (f1 - f0)))); f += 2
    return out


def group2(parts, cx, cy, f0, f1, c0=None, a0=0.0, a1=0.0, s0=1.0, s1=1.0, curve='expo-out', fade=4):
    """move parts as one rigid object, on twos: centre c0 -> (cx, cy) px, angle a0 -> a1 degrees COUNTER-clockwise (as the old
    kit), size s0 -> s1. parts: [(obj, local_angle, local_scale)]; each part's offset from (cx, cy) is its base."""
    c0 = c0 or (cx, cy)
    for o, la, ls in parts:
        ox, oy = o.base[0] - cx, o.base[1] - cy
        ps, rs, ss = [], [], []
        for i, (f, p) in enumerate(steps(f0, f1, curve)):
            e = 'Linear' if i == 0 else 'Hold'
            a, s = a0 + (a1 - a0) * p, s0 + (s1 - s0) * p
            gx, gy = c0[0] + (cx - c0[0]) * p, c0[1] + (cy - c0[1]) * p
            r = math.radians(a)
            x = gx + s * (ox * math.cos(r) + oy * math.sin(r))
            y = gy + s * (-ox * math.sin(r) + oy * math.cos(r))
            ps.append((f, (x, y), e)); rs.append((f, round(-(a + la), 4), e)); ss.append((f, round(s * ls, 5), e))
        for lane, ks in ((o.pos, ps), (o.rot, rs), (o.scale, ss)):
            if any(k[1] != ks[0][1] for k in ks): lane(ks)       # a lane that never changes gets no keys (lint repeated_key_value)
        if la and not any(k[1] != rs[0][1] for k in rs): o.rotv(-(la + a0))
        if fade: o.op(twos(f0, f0 + fade, 0.0, 1.0, 'linear'))


# ---------------------------------------------------------------- 1. 80s action movie title
def action_title(d):
    n = 150
    k = d.comp("RT Action title", n, "rat")
    k.rect("Title ground", 0, 0, W, H, css('120A0C'), f0=0, dur=n)
    glw = k.rect("Sunset glow", 960, 900, W, 360, COL['red'], f0=0, dur=n, center=True)
    glw.gradient([(0.0, css('C8553D', 0.0)), (1.0, css('E8772E', 0.85))], (960, 720), (960, 1080))   # dark at the top, orange at the bottom
    glw.op(twos(0, 12, 0.0, 1.0, 'linear'))
    cx, cy = 960, 470
    t = text(k, "Title", "STEEL THUNDER", cx, cy, 190, COL['cyan'], f0=4, dur=n - 4, style='ExtraBold', track=1.04)
    text_gradient(t, [(0.0, css('9EE7FF')), (0.47, css('F2FBFF')), (0.53, css('5A2A18')), (1.0, css('FFB347'))])   # sky, bright band, dark horizon, hot metal
    sh = lambda col, dx, dy: 'drop-shadow(%gpx %gpx 0px %s)' % (dx, round(dy * H / W, 4), col)
    t.set('filter', sh(css('8A2A1A'), 6, 6) + ' ' + sh(css('3A140C'), 12, 12))   # a two-step extrusion: dark red then brown
    group2([(t, 0.0, 1.0)], cx, cy, 4, 22, s0=0.2, s1=1.0, curve='expo-out')     # flies in from far away, stepped
    gx, gy = cx - textw("STEEL THUNDER", 190, 'ExtraBold') * 1.04 / 2 + 50, cy - 66      # on the S
    st = k.star("Glint", gx, gy, 150, 4, 0.12, css('FFF6E0'), f0=26, dur=16); glow(st, 14, 0.7)
    st.scale(twos(26, 34, 0.0, 1.0, 'expo-out') + twos(34, 42, 1.0, 0.0, 'accel')[1:])
    st.rot([(26, 0.0, 'Linear'), (42, 45.0, 'Linear')])
    sk = k.ell("Streak", gx, gy, 440, 8, css('FFE7C2'), f0=26, dur=16); glow(sk, 10, 0.6)
    sk.scale(twos(26, 34, [0.0, 1.0], [1.0, 1.0], 'expo-out') + twos(34, 42, [1.0, 1.0], [0.0, 1.0], 'accel')[1:])
    rise2(text(k, "Tagline", "ONE SUMMER.  ONE LAST RACE.", cx, 680, 56, COL['cream'], f0=30, dur=n - 30, style='Bold', track=1.3), 30)
    rise2(text(k, "Release", "COMING JULY 1987", cx, 790, 44, COL['mustard'], f0=40, dur=n - 40, style='ExtraBold', track=1.3), 40)


# ---------------------------------------------------------------- 2. mixtape tracklist
TRACKS = [("1", "Night Drive", "3:42"), ("2", "Sunset Strip", "4:05"), ("3", "Cherry Cola", "2:58"),
          ("4", "Roller Rink", "3:31"), ("5", "Last Dance", "5:12")]


def mixtape(d):
    n = 150
    k = d.comp("RT Mixtape", n, "rmx"); lab_bg(k, n)
    cx, cy = 560, 540
    parts = []
    parts.append(k.rect("Cassette", cx, cy, 760, 480, COL['brown'], r=30, f0=0, dur=n, center=True))
    parts.append(k.rect("Label", cx, cy - 70, 660, 230, COL['cream'], r=14, f0=0, dur=n, center=True))
    for i, col in enumerate((COL['orange'], COL['mustard'], COL['teal'])):
        parts.append(k.rect(f"Label stripe {i + 1}", cx, cy - 2 + i * 16, 660, 12, col, f0=0, dur=n, center=True))
    parts.append(text(k, "Mix title", "SUMMER MIX '86", cx, cy - 130, 60, COL['brown'], f0=0, dur=n, style='ExtraBold'))
    parts.append(k.rect("Tape window", cx, cy + 120, 380, 120, INK, r=60, f0=0, dur=n, center=True))
    reels = []
    for i, dx in enumerate((-120, 120)):
        parts.append(k.ell(f"Reel {i + 1}", cx + dx, cy + 120, 100, 100, COL['cream'], f0=0, dur=n))
        h = k.star(f"Reel hub {i + 1}", cx + dx, cy + 120, 56, 6, 0.55, COL['brown'], f0=0, dur=n); parts.append(h); reels.append(h)
    for i, (sx, sy) in enumerate(((-350, -210), (350, -210), (-350, 210), (350, 210))):
        parts.append(k.ell(f"Screw {i + 1}", cx + sx, cy + sy, 22, 22, COL['mustard'], f0=0, dur=n))
    for o in parts:                                     # the cassette slides in from the left on twos, all parts as one piece
        bx, by = o.base
        o.pos(twos(0, 16, (bx - 420, by), (bx, by), 'expo-out'))
        o.op(twos(0, 4, 0.0, 1.0, 'linear'))
    for h in reels:                                     # the reels play: one way, constant speed (6 deg a frame), from the landing on
        spin(h, 16, n, 6.0, 60.0)
    x0, x1 = 1060, 1760
    rise2(text(k, "Side", "SIDE A", x0, 290, 44, COL['orange'], f0=12, dur=n - 12, style='ExtraBold', align='left', track=1.4), 12)
    grow2(k.rect("Side rule", (x0 + x1) / 2, 340, x1 - x0, 6, COL['orange'], r=3, f0=16, dur=n - 16, center=True), 16, 14)
    for i, (no, name, tm) in enumerate(TRACKS):
        f, y = 22 + i * 6, 420 + i * 86
        rise2(text(k, f"Track {i + 1} no", no, x0, y, 48, COL['red'], f0=f, dur=n - f, style='ExtraBold', align='left'), f)
        rise2(text(k, f"Track {i + 1}", name, x0 + 70, y, 48, COL['brown'], f0=f, dur=n - f, style='Bold', align='left'), f)
        rise2(text(k, f"Track {i + 1} time", tm, x1, y, 44, COL['teal'], f0=f, dur=n - f, style='Bold', align='right'), f)


# ---------------------------------------------------------------- 3. 90s "under construction" web page
def hazard_band(k, name, yc, n, way):
    h, period, sw = 120, 120, 60
    k.rect(f"{name}", 960, yc, W, h, COL['yellow'], f0=0, dur=n, center=True)
    travel = way * period * 2                            # two periods per comp: the last frame matches the first
    x = -2 * period - h if way > 0 else -period
    i = 0
    while x < (1920 if way > 0 else 1920 + 2 * period):
        lo, hi = min(x, x + travel), max(x, x + travel) + sw + h
        if hi <= 0 or lo >= 1920: x += period; continue  # off frame for the whole clip: lint never_visible
        i += 1
        pts = [(x, yc + h / 2), (x + sw, yc + h / 2), (x + sw + h, yc - h / 2), (x + h, yc - h / 2)]   # a 45 degree parallelogram
        s = k.path(f"{name} stripe {i}", bezier(pts, closed=True), None, 0, f0=0, dur=n, fill=css('1A1A1A'))
        s.set('stroke', 'none'); fit_box(s, pts)
        bx, by = s.base
        s.pos([(0, (bx, by), 'Linear'), (n, (bx + travel, by), 'Linear')])
        x += period


def under_construction(d):
    n = 150
    k = d.comp("RT Under construction", n, "ruc")
    k.rect("Page ground", 0, 0, W, H, css('C0C0C0'), f0=0, dur=n)
    bar = k.rect("Title bar", 960, 56, W, 112, css('000080'), f0=0, dur=n, center=True)
    bar.gradient([(0.0, css('000080')), (1.0, css('1084D0'))], (0, 56), (1920, 56))      # navy on the left, light blue on the right
    text(k, "Title bar text", "Welcome to my home page!", 110, 76, 34, css('FFFFFF'), f0=0, dur=n, style='Bold', align='left')
    hazard_band(k, "Band top", 236, n, -1)
    hazard_band(k, "Band bottom", 900, n, 1)
    x0 = 200
    t = text(k, "Headline", "UNDER CONSTRUCTION", x0, 410, 104, css('1A1A1A'), f0=4, dur=n - 4, style='ExtraBold', align='left')
    hard_shadow(t, css('FFFFFF'), 5, 5)
    rise2(t, 4, 14)
    rise2(text(k, "Subline", "Come back soon - new pages every week!", x0, 520, 50, css('000080'), f0=14, dur=n - 14, style='Bold', align='left'), 14)
    rise2(text(k, "Counter label", "You are visitor no.", x0, 640, 44, css('1A1A1A'), f0=24, dur=n - 24, style='Bold', align='left'), 24)
    cw = textw("000419", 50, 'Bold') + 60
    lx = x0 + textw("You are visitor no.", 44, 'Bold') + 30
    box = k.rect("Counter box", lx + cw / 2, 640, cw, 76, css('000000'), f0=24, dur=n - 24, center=True)
    box.stroke(css('808080'), 4)
    box.op(twos(24, 28, 0.0, 1.0, 'linear'))
    for i, (s, f0, f1) in enumerate((("000417", 28, 80), ("000418", 80, 120), ("000419", 120, n))):
        c = text(k, f"Counter {i + 1}", s, lx + cw / 2, 640, 50, css('39FF14'), f0=f0, dur=f1 - f0, style='Bold')
        if i == 0: c.op(twos(28, 32, 0.0, 1.0, 'linear'))
    rise2(text(k, "Footer", "Best viewed at 800 x 600", x0, 750, 36, css('404040'), f0=34, dur=n - 34, style='Medium', align='left'), 34)
    bx, by = 1560, 520
    burst = k.star("New burst", bx, by, 290, 14, 0.74, css('E01010'), f0=10, dur=n - 10)
    nw = text(k, "New", "NEW!", bx, by, 64, COL['yellow'], f0=10, dur=n - 10, style='ExtraBold')
    pop2(burst, 10); pop2(nw, 10)
    burst.rot([(22, 0.0, 'Linear'), (n, 60.0, 'Linear')])             # the burst keeps turning one way (old -60 counter-clockwise)
    seq, f, on = [(10, 1.0)], 50, False                                # 40 f on, then 15 off / 30 on: under one flash a second
    while f < n:
        seq.append((f, 1.0 if on else 0.0)); f += 30 if not on else 15; on = not on
    nw.op(hold_keys(seq))


# ---------------------------------------------------------------- 4. film countdown leader
def film_leader(d):
    per, nums = 30, ("5", "4", "3", "2")
    n = per * len(nums)
    k = d.comp("RT Film leader", n, "rfl")
    k.rect("Leader ground", 0, 0, W, H, css('B4B0A8'), f0=0, dur=n).grain(0.2, 2.2, softness=0.4, colour=0.1)   # old print grain on the ground (an adjustment layer would add a lint warning, KI-158)
    cx, cy, R = 960, 540, 330
    for i, (f, num) in enumerate(zip(range(0, n, per), nums)):
        w = k.ell(f"Sweep {i + 1}", cx, cy, R, R, None, f0=f, dur=per)
        w.stroke(css('6E6A63'), R, cap='butt')         # a butt-capped stroke as wide as the radius: a pie slice
        w.trim([(f, 1.0, 'Linear'), (f + per, 0.0, 'Linear')], which='start')   # start 1 -> 0 sweeps clockwise from 12 o'clock
        w.rotv(-90.0)
    line(k, "Cross H", [(0, cy), (W, cy)], css('2A2622'), 4, f0=0, dur=n)
    line(k, "Cross V", [(cx, 0), (cx, H)], css('2A2622'), 4, f0=0, dur=n)
    ro = k.ell("Ring outer", cx, cy, 2 * R + 40, 2 * R + 40, None, f0=0, dur=n); ro.stroke(css('F4F1EA'), 12)
    ri = k.ell("Ring inner", cx, cy, 2 * R - 60, 2 * R - 60, None, f0=0, dur=n); ri.stroke(css('2A2622'), 6)
    for i, (f, num) in enumerate(zip(range(0, n, per), nums)):
        text(k, f"Number {i + 1}", num, cx, cy, 420, css('1A1714'), f0=f, dur=per, style='ExtraBold')


# ---------------------------------------------------------------- 5. pixel level-up
SPRITE = ["....#....", "...#o#...", "..#ooo#..", "##ooooo##", "#ooooooo#", ".#ooooo#.", "..#o#o#..", ".#o#.#o#.", ".##...##."]


def level_up(d):
    n = 120
    k = d.comp("RT Level up", n, "rlu"); lab_bg(k, n, COL['night'])
    px, cx, cy = 26, 960, 270
    for r, row in enumerate(SPRITE):
        for c, ch in enumerate(row):
            if ch == '.': continue
            k.rect(f"Pixel {r + 1}-{c + 1}", cx + (c - 4) * px, cy + (r - 4) * px, px, px,
                   COL['orange'] if ch == '#' else COL['yellow'], f0=r * 2, dur=n - r * 2, center=True)   # row by row, every 2 f
    t = text(k, "Level up", "LEVEL UP!", cx, 520, 150, COL['yellow'], f0=12, dur=n - 12, style='ExtraBold', track=1.06)
    hard_shadow(t, COL['pink'], 10, 10)
    pop2(t, 12)
    for i in range(8):                                   # pixel sparks fly out on twos and are gone by f42
        a = math.radians(i * 45 + 22.5)
        x0, y0 = cx + 330 * math.cos(a), 520 - 150 * math.sin(a)
        x1, y1 = cx + 560 * math.cos(a), 520 - 300 * math.sin(a)
        s = k.rect(f"Spark {i + 1}", x0, y0, 18, 18, COL['cyan'] if i % 2 else COL['pink'], f0=14, dur=28, center=True)
        s.pos(twos(14, 40, (x0, y0), (x1, y1), 'expo-out'))
        s.op(hold_keys([(14, 1.0), (34, 0.5)]))
    bw, bh, by = 900, 56, 720
    fr = k.rect("XP frame", cx, by, bw, bh, None, f0=20, dur=n - 20, center=True); fr.stroke(COL['cream'], 6)
    fr.op(twos(20, 24, 0.0, 1.0, 'linear'))
    text(k, "XP label", "XP", cx - bw / 2 - 30, by, 44, COL['cream'], f0=20, dur=n - 20, style='ExtraBold', align='right').op(twos(20, 24, 0.0, 1.0, 'linear'))
    seg = (bw - 24) / 10
    for i in range(10):                                  # the bar fills one block every 2 f
        f = 26 + i * 2
        k.rect(f"XP block {i + 1}", cx - bw / 2 + 12 + seg * i + seg / 2, by, seg - 8, bh - 20, COL['cyan'], f0=f, dur=n - f, center=True)
    lv = cx + bw / 2 + 30
    text(k, "Level old", "LV 11", lv, by, 48, COL['cream'], f0=20, dur=30, style='ExtraBold', align='left').op(twos(20, 24, 0.0, 1.0, 'linear'))
    nl = text(k, "Level new", "LV 12", lv, by, 48, COL['yellow'], f0=50, dur=n - 50, style='ExtraBold', align='left')
    nl.scale(twos(50, 58, 1.5, 1.0, 'expo-out'))
    rise2(text(k, "XP gain", "+500 XP", cx, 830, 56, COL['pink'], f0=52, dur=n - 52, style='ExtraBold'), 52)


# ---------------------------------------------------------------- 6. 70s TV ident
def tv_ident(d):
    n = 150
    k = d.comp("RT TV ident", n, "rti")
    k.rect("Ident ground", 0, 0, W, H, css('2A1A10'), f0=0, dur=n)
    cx, cy = 960, 450
    for i, (dia, col) in enumerate(zip((620, 520, 420, 320), (COL['red'], COL['orange'], COL['mustard'], COL['teal']))):
        f = i * 4
        r = k.ell(f"Ring {i + 1}", cx, cy, dia, dia, None, f0=f, dur=n - f); r.stroke(col, 34, cap='butt')
        r.trim(twos(f, f + 16, 0.0, 1.0, 'expo-out'), which='end')
        r.rotv(-90.0)                                    # each ring draws from 12 o'clock
    seven = text(k, "Number", "7", cx, cy, 230, COL['cream'], f0=24, dur=n - 24, style='ExtraBold')
    pop2(seven, 24)
    rise2(text(k, "Channel", "CHANNEL SEVEN", cx, 870, 72, COL['cream'], f0=34, dur=n - 34, style='ExtraBold', track=1.4), 34)
    rise2(text(k, "Tagline", "NOW IN COLOUR", cx, 962, 40, COL['mustard'], f0=42, dur=n - 42, style='Bold', track=1.6), 42)
    dot = k.ell("Orbit dot", cx, cy - 350, 26, 26, COL['cream'], f0=30, dur=n - 30)
    dot.op(twos(30, 34, 0.0, 1.0, 'linear'))
    seq = []                                             # the dot circles the rings one way at constant speed, sampled every 2 f, held
    for j, f in enumerate(range(30, n + 1, 2)):
        a = math.radians(90 + (f - 30) * 3.0)
        seq.append((f, (cx + 350 * math.cos(a), cy - 350 * math.sin(a)), 'Linear' if j == 0 else 'Hold'))
    dot.pos(seq)


# ---------------------------------------------------------------- 7. polaroid memory
def polaroid(d):
    n = 150
    k = d.comp("RT Polaroid", n, "rpo"); lab_bg(k, n)
    cx, cy = 700, 540
    fw, fh, ph = 600, 720, 520
    py = cy - fh / 2 + 40 + ph / 2
    frame = k.rect("Polaroid frame", cx, cy, fw, fh, WHITE, r=6, f0=0, dur=n, center=True)
    frame.shadow(8, round(12 * H / W, 3), 16.6, css('000000', 0.3))
    photo = k.rect("Photo", cx, py, ph, ph, COL['teal'], f0=0, dur=n, center=True)
    photo.gradient([(0.0, css('8FC7D1')), (0.55, css('F2C27A')), (1.0, css('C8553D'))], (cx, py - ph / 2), (cx, py + ph / 2))
    lbl = text(k, "Photo label", "photo", cx, py, 40, WHITE, f0=0, dur=n, style='Bold')
    dev = k.rect("Developing", cx, py, ph, ph, css('3B3226'), f0=0, dur=n, center=True)
    cap = text(k, "Caption", "Summer '79", cx, cy + fh / 2 - 80, 58, COL['brown'], f0=0, dur=n, style='Bold')
    tape = k.rect("Tape", cx, cy - fh / 2 + 4, 200, 60, css('E3B23C', 0.75), f0=0, dur=n, center=True)
    parts = [(frame, 0.0, 1.0), (photo, 0.0, 1.0), (lbl, 0.0, 1.0), (dev, 0.0, 1.0), (cap, 0.0, 1.0), (tape, 6.0, 1.0)]
    group2(parts, cx, cy, 0, 16, c0=(cx + 140, cy - 700), a0=14.0, a1=-4.0, curve='expo-out', fade=0)   # drops in, tilting, on twos
    dev.op([(20, 1.0, 'Linear'), (90, 0.0, EASE_OUT)])                 # the picture develops: smooth, not stepped
    lbl.op([(40, 0.0, 'Linear'), (70, 1.0, 'Linear')])
    x0 = 1150
    rise2(text(k, "Heading", "The lake house", x0, 470, 88, COL['brown'], f0=34, dur=n - 34, style='ExtraBold', align='left'), 34)
    rise2(text(k, "Line", "Our first summer, 1979", x0, 570, 48, COL['red'], f0=42, dur=n - 42, style='Medium', align='left'), 42)
    grow2(k.rect("Rule", x0 + 160, 640, 320, 8, COL['orange'], r=4, f0=50, dur=n - 50, center=True), 50, 12)


# ---------------------------------------------------------------- 8. retro weather map
ISLAND = [(560, 300), (820, 250), (1000, 330), (1180, 250), (1440, 330), (1570, 520), (1470, 690), (1540, 860), (1300, 960),
          (1020, 890), (820, 990), (560, 900), (430, 700), (500, 520)]
CITIES = [("Port Ash", 800, 430, "sun", "24°"), ("Kelby", 1300, 470, "cloud", "19°"),
          ("Marrow", 720, 740, "rain", "15°"), ("Tolly Bay", 1200, 770, "sun", "22°")]


def smooth_closed(pts, t=0.22):
    """a closed smooth outline through pts: bezier points with tangent handle offsets (Catmull-Rom style, scaled by t)"""
    out, m = [], len(pts)
    for i in range(m):
        (x0, y0), (x2, y2) = pts[i - 1], pts[(i + 1) % m]
        tx, ty = (x2 - x0) * t, (y2 - y0) * t
        out.append((pts[i][0], pts[i][1], (-tx, -ty), (tx, ty)))
    return out


def cloud(k, name, x, y, col, f0, n, s=1.25):
    parts = [k.ell(f"{name} puff {j + 1}", x + dx * s, y + dy * s, w * s, w * s, col, f0=f0, dur=n - f0)
             for j, (dx, dy, w) in enumerate(((-34, 10, 70), (8, -12, 92), (46, 12, 66)))]
    parts.append(k.rect(f"{name} base", x + 6 * s, y + 30 * s, 150 * s, 34 * s, col, r=17 * s, f0=f0, dur=n - f0, center=True))
    return parts


def weather_map(d):
    n = 150
    k = d.comp("RT Weather map", n, "rwm")
    k.rect("Sea", 0, 0, W, H, css('1F5F7A'), f0=0, dur=n)
    land = k.path("Land", bezier(smooth_closed(ISLAND), closed=True), COL['brown'], 6, f0=0, dur=n, fill=COL['cream'])
    hb = k.rect("Header", 110 + 300, 140, 600, 120, COL['brown'], r=18, f0=0, dur=n, center=True)
    grow2(hb, 0, 12)
    rise2(text(k, "Header title", "WEATHER", 150, 122, 64, COL['cream'], f0=6, dur=n - 6, style='ExtraBold', align='left', track=1.2), 6)
    rise2(text(k, "Header day", "TUESDAY", 150, 178, 34, COL['mustard'], f0=10, dur=n - 10, style='Bold', align='left', track=1.5), 10)
    for i, (name, x, y, kind, temp) in enumerate(CITIES):
        f = 16 + i * 10
        ix = x - 110
        if kind == 'sun':
            rays = k.star(f"{name} rays", ix, y, 160, 12, 0.62, COL['orange'], f0=f, dur=n - f)
            sun = k.ell(f"{name} sun", ix, y, 96, 96, COL['mustard'], f0=f, dur=n - f)
            pop2(rays, f); pop2(sun, f)
            more(rays, 'rotate', [(f + 12, 0.0, 'Linear'), (n, 45.0, 'Linear')])   # rays turn one way after the pop
        else:
            ps = cloud(k, name + " cloud", ix, y - 10, css('9AA8B2') if kind == 'cloud' else css('6F7E89'), f, n)
            if kind == 'rain':
                for j in range(3):
                    dr = line(k, f"{name} drop {j + 1}", [(ix - 50 + j * 50, y + 76), (ix - 62 + j * 50, y + 106)], COL['teal'], 8,
                              f0=f + 8, dur=n - f - 8)
                    dr.op(twos(f + 8, f + 12, 0.0, 1.0, 'linear'))
            group2([(o, 0.0, 1.0) for o in ps], ix, y - 10, f, f + 12, s0=0.0, s1=1.0, curve='spring-gentle', fade=0)
        tile = k.rect(f"{name} tile", x + 40, y, 140, 96, COL['red'], r=12, f0=f + 4, dur=n - f - 4, center=True)
        tt = text(k, f"{name} temp", temp, x + 40, y, 60, COL['cream'], f0=f + 4, dur=n - f - 4, style='ExtraBold')
        pop2(tile, f + 4); pop2(tt, f + 4, s0=0.5)          # from half size: from 0 the first steps are under lint's 18 px
        rise2(text(k, f"{name} name", name, x + 40, y + 84, 36, COL['brown'], f0=f + 8, dur=n - f - 8, style='Bold'), f + 8, d=12, dy=20)


def comps(d):
    action_title(d); mixtape(d); under_construction(d); film_leader(d); level_up(d); tv_ident(d); polaroid(d); weather_map(d)


def build():
    d = PDoc(); comps(d)
    return d


if __name__ == "__main__":
    print(__doc__)
