"""Sports round 3: eight lab comps for briefs the pack could not serve before (a live score bug with a
running clock and added time, a substitution card, a signing announcement, a touchdown celebration
burst, a tournament bracket, a league table movement, a fixture list and a match-day poster), written
straight into a .carverproj.

    import sports_lab3 as L; presets, masks = L.build(PROJECT.carverproj)

Same palette and rules as sports_lab.py (dark navy, team red and blue, highlight yellow, slanted
panels, fast 8-14 f moves, one hit per beat). Every move is baked as keys here (no presets to apply):
slash() writes the pack's Slash in, slam() its Impact slam, grow_x() a bar growing from its left edge.
Text that must read on the ground uses colours converted with the renderer's BT.709 curve (KI-141):
labels #B4BCD0, OFF #FF6B5E, ON #3FD08A. White text on the red and blue team panels is 36 px or larger
(the large-text 3:1 rule; white on #E63946 is about 4:1). Yellow is never text on red (2.9:1).
A text cannot change its content over time (text.content is not keyframeable), so the running clock,
changed points and scores are separate clips that hand over on one frame, each on screen 25 f or more.
After writing: edit.open {path, force:true}; edit.save; check with carvercat_inspect (curves, lint
contrast:true, qc), carvercat_authoring geometry and carvercat_look; extract templates with
comp_to_template.py (--drop "Lab bg").
Fonts: Rethink Sans must be installed (KI-136). Docs: ai/patterns/sports.md (round 3).
Pixel space 1920x1080, y down; comp frames, 30 fps. Teams, players, leagues, venues and scores are
invented sample copy.
"""
import os, sys, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sports_lab import Doc, lin, P, COL, EXPO, BACK, lab_bg
from sports_lab2 import slant_panel
from cc import BEZ, textw

ACCEL = BEZ['accel']
PRESETS, MASKS = [], []
W, H = 1920.0, 1080.0


def lin709(h):
    """hex -> linear light with the renderer's BT.709 curve (KI-141: cc.lin renders mid-tones ~10% dark)"""
    h = h.lstrip('#'); v = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return [round(c / 4.5 if c < 0.081 else ((c + 0.099) / 1.099) ** (1 / 0.45), 5) for c in v] + [1.0]


C3 = dict(label=lin709('B4BCD0'), off=lin709('FF6B5E'), on=lin709('3FD08A'), green=lin('1FA35C'),
          line=lin('3A4466'), panel2=lin('1E2848'), dred=lin('7A1B26'), dblue=lin('0F3F7E'))


# ---------------------------------------------------------------- the pack's moves as keys
def slash(o, f, d=10):
    """Slash in: from (-22% W, 12% H lower) diagonally to rest on a hard expo, opaque in 2 f (settles about f+7)"""
    bx, by = o.base
    o.pos([(f, [bx - 0.22, by - 0.12], 'Linear'), (f + d, [bx, by], EXPO)])
    o.op([(f, 0.0, 'Linear'), (f + 2, 1.0, 'Linear')])
    return o


def slam(o, f, s0=2.2):
    """Impact slam: size s0 (220%) -> 92% accelerating (impact at f+5), springs back to 100% by f+8"""
    o.scale([(f, s0, 'Linear'), (f + 5, 0.92, ACCEL), (f + 8, 1.0, 'Ease out')])
    o.op([(f, 0.0, 'Linear'), (f + 2, 1.0, 'Linear')])
    return o


def from_right(o, f, d=10):
    """a short slide in from the right (5% of the width, 96 px) on a hard expo, opaque in 2 f: for a text that must not cross its left neighbour"""
    bx, by = o.base
    o.pos([(f, [bx + 0.05, by], 'Linear'), (f + d, [bx, by], EXPO)])
    o.op([(f, 0.0, 'Linear'), (f + 2, 1.0, 'Linear')])
    return o


def fade(o, f, d=3):
    return o.op([(f, 0.0, 'Linear'), (f + d, 1.0, 'Ease out')])


def grow_x(o, f, d=10, ax=-1):
    o.anchor(ax, 0); o.scale([(f, [0.0, 1.0], 'Linear'), (f + d, [1.0, 1.0], EXPO)]); return o


def draw(o, f, d=14, ease=EXPO):
    o.trim([(f, 0.0, 'Linear'), (f + d, 1.0, ease)], which='end'); return o


def T(k, name, s, x, y, px, col, f, n, align='left', style='ExtraBold', track=None, end=None):
    return k.text(name, s, x, y, px, col, f0=f, dur=(end or n) - f, style=style, align=align, track=track)


def arrow(k, name, x, y, size, col, up, f, n):
    """a solid triangle pointing up or down (a 3-gon points right; +90 turns it up, -90 down, KI-150)"""
    a = k.ngon(name, x, y, size, 3, col, f0=f, dur=n - f); a.rotv(90.0 if up else -90.0); return a


# ---------------------------------------------------------------- 1. live score bug with a running clock
def live_clock(d):
    n = 210
    k = d.comp("SP Live clock", n, "slc"); lab_bg(k, n)
    x, y, h = 96, 64, 64
    parts = [("League box", 96, COL['yellow']), ("Team A box", 128, COL['red']), ("Score box", 150, COL['panel']),
             ("Team B box", 128, COL['blue']), ("Clock box", 140, COL['white'])]
    xs, cx = [], x
    for _, w, _ in parts: xs.append(cx); cx += w
    cl_x, cl_w = xs[4], parts[4][1]
    # the added-time board sits under the clock box (drawn first) and slides down out of it at 45:00
    tab = k.rect("Added time tab", cl_x, y, cl_w, 48, COL['yellow'], f0=140, dur=n - 140)
    tx, ty = tab.base
    tab.pos([(140, [tx, ty], 'Linear'), (150, [tx, ty - 48 / H], EXPO)])
    for i, (name, w, col) in enumerate(parts):
        b = k.rect(name, xs[i], y, w, h, col, f0=0, dur=n)
        grow_x(b, i * 3)
    T(k, "League", "NCL", xs[0] + 48, y + h / 2, 30, COL['ink'], 6, n, align='center', track=1.1)
    fade(T(k, "Team A", "HAW", xs[1] + 64, y + h / 2, 36, COL['white'], 9, n, align='center'), 9)
    fade(T(k, "Score", "1 - 0", xs[2] + 75, y + h / 2, 36, COL['white'], 12, n, align='center'), 12)
    fade(T(k, "Team B", "WOL", xs[3] + 64, y + h / 2, 36, COL['white'], 15, n, align='center'), 15)
    # the clock: one clip per second, handing over on the frame (each 30 f on screen; reading time 25 f)
    ticks = [("44:56", 20, 50), ("44:57", 50, 80), ("44:58", 80, 110), ("44:59", 110, 140), ("45:00", 140, 170), ("45:01", 170, n)]
    for i, (s, f0, f1) in enumerate(ticks):
        t = T(k, f"Clock {i + 1}", s, cl_x + cl_w / 2, y + h / 2, 34, COL['ink'], f0, n, align='center', end=f1)
        if i == 0: fade(t, f0)
    fade(T(k, "Added time", "+3", cl_x + cl_w / 2, y + h + 24, 30, COL['ink'], 150, n, align='center'), 150)


# ---------------------------------------------------------------- 2. substitution card
def substitution(d):
    n = 150
    k = d.comp("SP Substitution", n, "ssu"); lab_bg(k, n)
    x0, x1, sl = 110, 780, 20
    objs = []
    hd = slant_panel(k, "Header", x0, 744, x1, 800, sl, COL['yellow'], 0, n); slash(hd, 0); objs.append(hd)
    objs.append(slash(T(k, "Header text", "SUBSTITUTION", x0 + 40, 772, 30, COL['ink'], 3, n, track=1.3), 3))
    objs.append(slash(T(k, "Minute", "67'", x1 - 40, 772, 30, COL['ink'], 5, n, align='right'), 5))
    rows = [("Off", 850, "9", "J. REYES", "OFF", C3['off'], COL['red'], False, 8),
            ("On", 950, "17", "D. OKORO", "ON", C3['on'], C3['green'], True, 22)]
    for tag, yc, num, name, word, tcol, acol, up, f in rows:
        pn = slant_panel(k, f"{tag} row", x0, yc - 48, x1, yc + 48, sl, COL['panel'], f, n - f); slash(pn, f); objs.append(pn)
        a = arrow(k, f"{tag} arrow", x0 + 64, yc, 46, acol, up, f + 6, n)
        ax, ay = a.base
        dy = 40 / H if up else -40 / H                                  # ON rises from below, OFF drops from above (y up in P)
        a.pos([(f + 6, [ax, ay - dy], 'Linear'), (f + 16, [ax, ay], EXPO)]); fade(a, f + 6, 2); objs.append(a)
        objs.append(slash(T(k, f"{tag} number", num, x0 + 150, yc, 44, COL['yellow'], f + 3, n, align='center'), f + 3))
        objs.append(from_right(T(k, f"{tag} name", name, x0 + 260, yc, 46, COL['white'], f + 5, n), f + 5))
        objs.append(fade(T(k, f"{tag} tag", word, x1 - 50, yc, 28, tcol, f + 12, n, align='right', style='SemiBold', track=1.3), f + 12))
    for o in objs:                                                      # exit: all fade out together in the last 10 f
        o.addkeys(o.tr('opacity'), [(n - 10, 1.0, 'Linear'), (n - 2, 0.0, ACCEL)])


# ---------------------------------------------------------------- 3. signing announcement
def signing(d):
    n = 150
    k = d.comp("SP Signing", n, "ssg"); lab_bg(k, n)
    ph = slant_panel(k, "Photo panel", 120, 150, 800, 930, 90, COL['red'], 0, n); slash(ph, 0)
    # a player stand-in (replace with a cut-out photo): head and shoulders in a darker red
    head = k.ell("Player head", 470, 420, 210, 250, C3['dred'], f0=6, dur=n - 6); fade(head, 6, 6)
    body = k.path("Player shoulders", [(260, 930), (290, 660), (380, 590), (560, 590), (650, 660), (690, 930)], f0=6, dur=n - 6,
                  closed=True, handles=[((0, 0), (0, 0), True), ((0, 0), (20, -50), False), ((-60, 10), (0, 0), False),
                                        ((0, 0), (60, 10), False), ((-20, -50), (0, 0), False), ((0, 0), (0, 0), True)])
    body.fill(C3['dred']); fade(body, 6, 6)
    xr = 880
    slash(T(k, "Kicker", "NEW SIGNING", xr, 270, 40, COL['yellow'], 8, n, track=1.4), 8)
    slash(T(k, "Player name", "MATEO VANCE", xr, 375, 104, COL['white'], 12, n), 12)
    slash(T(k, "Position", "MIDFIELDER  ·  AGE 24", xr, 470, 36, C3['label'], 16, n, style='SemiBold', track=1.2), 16)
    rule = k.line("Divider", [(xr, 540), (1780, 540)], C3['line'], px=4, f0=20, dur=n - 20); draw(rule, 20, 14)
    fade(T(k, "From label", "FROM", xr, 600, 26, C3['label'], 26, n, style='SemiBold', track=1.4), 26)
    slash(T(k, "From club", "RIVERSIDE FC", xr, 650, 44, COL['white'], 28, n), 28)
    fw = textw("RIVERSIDE FC", 44, 'ExtraBold')
    ax0 = xr + fw + 50
    ar = k.line("Transfer arrow", [(ax0, 650), (ax0 + 110, 650)], COL['yellow'], px=8, f0=34, dur=n - 34); draw(ar, 34, 10)
    hd = k.line("Arrow head", [(ax0 + 86, 626), (ax0 + 112, 650), (ax0 + 86, 674)], COL['yellow'], px=8, f0=40, dur=n - 40)
    fade(hd, 40, 3)
    xt = ax0 + 170
    fade(T(k, "To label", "TO", xt, 600, 26, C3['label'], 40, n, style='SemiBold', track=1.4), 40)
    slash(T(k, "To club", "HAWKS", xt, 650, 44, COL['white'], 42, n), 42)
    cw = 642                                                            # the text measures 562 px (tracking 1.2) + 40 px each side
    cp = slant_panel(k, "Contract panel", xr, 730, xr + cw, 800, 16, COL['yellow'], 48, n - 48); grow_x(cp, 48, 10)
    fade(T(k, "Contract", "CONTRACT UNTIL 2030", xr + 40, 765, 34, COL['ink'], 54, n, track=1.2), 54)
    # the stamp lands over the stand-in's chest, turned -8 deg (one hit; nothing else moves then)
    st = k.rect("Stamp frame", 450, 790, 540, 140, COL['ink'], f0=64, dur=n - 64, center=True); st.stroke(COL['yellow'], 9); st.rotv(8.0)
    slam(st, 64, 1.5)
    sw = k.text("Stamp", "SIGNED", 450, 790, 92, COL['yellow'], f0=64, dur=n - 64, style='ExtraBold', align='center', track=1.2)
    sw.rotv(8.0); slam(sw, 64, 1.5)


# ---------------------------------------------------------------- 4. touchdown celebration burst
def touchdown(d):
    n = 90
    k = d.comp("SP Touchdown burst", n, "stb"); lab_bg(k, n)
    cx, cy = 960, 470
    # a sunburst that turns one way the whole time (moving shapes never sit cropped at rest)
    for i, (col, op_, sc, r0, r1) in enumerate(((COL['red'], 0.9, 2.3, 0.0, 30.0), (COL['blue'], 0.55, 1.5, 15.0, -10.0))):
        sb = k.star(f"Sunburst {i + 1}", cx, cy, 1000, 12, 0.12, col, f0=0, dur=n)
        sb.scale([(2 + 2 * i, 0.0, 'Linear'), (14 + 2 * i, sc, BACK)])
        sb.rot([(0, r0, 'Linear'), (n, r1, 'Linear')])
        sb.op([(2 + 2 * i, 0.0, 'Linear'), (6 + 2 * i, op_, 'Linear')])
    ring = k.ell("Shock ring", cx, cy, 300, 300, None, f0=6, dur=26); ring.stroke(COL['white'], 14)
    ring.scale([(6, 0.3, 'Linear'), (32, 3.4, BEZ['decel'])]); ring.op([(6, 1.0, 'Linear'), (32, 0.0, 'Linear')])
    # confetti: 28 pieces thrown out from the centre at the impact, falling under gravity, spinning one way (baked every 2 f)
    rnd = random.Random(7)
    cols = [COL['yellow'], COL['white'], COL['yellow'], COL['blue'], COL['white'], COL['red']]
    f0, f1 = 11, 76
    for i in range(28):
        ang = 2 * math.pi * (i + rnd.uniform(-0.3, 0.3)) / 28
        sp = rnd.uniform(26, 42)                                        # px per frame
        vx, vy = sp * math.cos(ang), sp * math.sin(ang) * 0.75 - 10
        spin = rnd.choice((-1, 1)) * rnd.uniform(9, 16)
        c = k.rect(f"Confetti {i + 1}", cx, cy, 16, 28, cols[i % len(cols)], f0=f0, dur=f1 - f0, center=True)
        ps, rs = [], []
        for f in range(f0, f1 + 1, 2):
            t = f - f0; drag = (1 - 0.94 ** t) / 0.06                   # air drag: speed falls 6% a frame
            x = cx + vx * drag; yy = cy + vy * drag + 0.55 * t * t
            ps.append((f, P(x, yy), 'Linear')); rs.append((f, round(spin * t, 2), 'Linear'))
        c.pos(ps); c.rot(rs)
        c.op([(f0, 1.0, 'Linear'), (f1 - 14, 1.0, 'Linear'), (f1, 0.0, 'Linear')])
    td = k.text("Touchdown", "TOUCHDOWN!", cx, cy, 190, COL['yellow'], f0=6, dur=n - 6, style='ExtraBold', align='center')
    td.set(td.src('text_outline', 'paint'), 'solid').set(td.src('text_outline', 'color'), COL['ink'][:3])
    td.set(td.src('text_outline', 'thickness'), 0.06).set(td.src('text_outline', 'outsideOnly'), True)
    slam(td, 6)
    sw = textw("HAWKS  21 - 14  WOLVES", 56, 'ExtraBold') + 160
    strip = slant_panel(k, "Score strip", cx - sw / 2, 700, cx + sw / 2, 800, 30, COL['ink'], 22, n - 22); slash(strip, 22)
    slash(T(k, "Score line", "HAWKS  21 - 14  WOLVES", cx, 750, 56, COL['white'], 25, n, align='center'), 25)


# ---------------------------------------------------------------- 5. tournament bracket
def bracket(d):
    n = 180
    k = d.comp("SP Bracket", n, "sbr"); lab_bg(k, n)
    cols = [(120, 440), (560, 880), (1000, 1320)]
    hdrs = ["QUARTER-FINALS", "SEMI-FINALS", "FINAL"]
    for i, (a, b) in enumerate(cols):
        fade(T(k, f"Round {i + 1}", hdrs[i], a, 120, 26, C3['label'], [0, 56, 100][i], n, style='SemiBold', track=1.3), [0, 56, 100][i])
    fade(T(k, "Round 4", "CHAMPION", 1460, 120, 26, C3['label'], 140, n, style='SemiBold', track=1.3), 140)
    qf_y = [200, 270, 380, 450, 560, 630, 740, 810]
    sf_y = [(qf_y[2 * i] + qf_y[2 * i + 1]) / 2 for i in range(4)]
    fi_y = [(sf_y[0] + sf_y[1]) / 2, (sf_y[2] + sf_y[3]) / 2]
    ch_y = (fi_y[0] + fi_y[1]) / 2
    qf = [("HAWKS", "3"), ("RAVENS", "1"), ("BEARS", "0"), ("TIGERS", "2"), ("WOLVES", "2"), ("SHARKS", "1"), ("FALCONS", "2"), ("LIONS", "4")]
    sf = [("HAWKS", "2"), ("TIGERS", "1"), ("WOLVES", "0"), ("LIONS", "1")]
    fi = [("HAWKS", "3"), ("LIONS", "2")]

    def slot(tag, col, y, team, score, f_in, f_score, win):
        a, b = cols[col]
        p = slant_panel(k, f"{tag} slot", a, y - 28, b, y + 28, 12, COL['panel'], f_in, n - f_in); slash(p, f_in)
        slash(T(k, f"{tag} team", team, a + 26, y, 30, COL['white'], f_in + 2, n), f_in + 2)
        fade(T(k, f"{tag} score", score, b - 26, y, 30, COL['yellow'], f_score, n, align='right'), f_score)
        if win:                                                          # the winner's edge lights up yellow with the result
            bar = k.rect(f"{tag} win", a + 4, y - 22, 8, 44, COL['yellow'], f0=f_score, dur=n - f_score)
            bar.anchor(0, -1); bar.scale([(f_score, [1.0, 0.0], 'Linear'), (f_score + 8, [1.0, 1.0], EXPO)])

    def joins(tag, col, ys, f):
        a, b = cols[col]; xm = b + 60
        for j in range(0, len(ys), 2):
            ya, yb = ys[j], ys[j + 1]; ym = (ya + yb) / 2
            br = k.line(f"{tag} join {j // 2 + 1}", [(b, ya), (xm, ya), (xm, yb), (b, yb)], C3['line'], px=4, f0=f, dur=n - f); draw(br, f, 12)
            ln = k.line(f"{tag} feed {j // 2 + 1}", [(xm, ym), (xm + 60, ym)], COL['yellow'], px=4, f0=f + 8, dur=n - f - 8); draw(ln, f + 8, 6)

    for i, ((tm, sc), y) in enumerate(zip(qf, qf_y)):
        other = qf[i ^ 1][1]
        slot(f"QF {i + 1}", 0, y, tm, sc, 4 + 3 * i, 30 + 2 * (i // 2), int(sc) > int(other))
    joins("QF", 0, qf_y, 42)
    for i, ((tm, sc), y) in enumerate(zip(sf, sf_y)):
        other = sf[i ^ 1][1]
        slot(f"SF {i + 1}", 1, y, tm, sc, 58 + 3 * i, 78 + 2 * (i // 2), int(sc) > int(other))
    joins("SF", 1, sf_y, 88)
    for i, ((tm, sc), y) in enumerate(zip(fi, fi_y)):
        other = fi[i ^ 1][1]
        slot(f"Final {i + 1}", 2, y, tm, sc, 102 + 3 * i, 120, int(sc) > int(other))
    joins("Final", 2, fi_y, 128)
    chp = slant_panel(k, "Champion panel", 1460, ch_y - 50, 1800, ch_y + 50, 20, COL['yellow'], 140, n - 140); slam(chp, 140)
    slam(T(k, "Champion", "HAWKS", 1630, ch_y, 56, COL['ink'], 140, n, align='center'), 140)
    fade(T(k, "Season", "CUP 2026", 1630, ch_y + 92, 30, C3['label'], 152, n, align='center', style='SemiBold', track=1.3), 152)


# ---------------------------------------------------------------- 6. league table movement
def table_move(d):
    n = 150
    k = d.comp("SP Table move", n, "stm"); lab_bg(k, n)
    slash(T(k, "Table title", "LEAGUE TABLE", 460, 200, 56, COL['white'], 0, n, track=1.2), 0)
    fade(T(k, "Table week", "MATCHWEEK 30", 1460, 200, 28, C3['label'], 6, n, align='right', style='SemiBold', track=1.3), 6)
    fade(T(k, "Pts head", "PTS", 1400, 270, 26, C3['label'], 6, n, align='right', style='SemiBold', track=1.3), 6)
    y0, step = 330, 84
    rows = [("HAWKS", "54"), ("WOLVES", "46"), ("BEARS", "45"), ("SHARKS", "45"), ("FALCONS", "44"), ("TIGERS", "40")]
    ry = lambda i: y0 + i * step
    # the rank column stays; the team rows move
    for i in range(6):
        f = 6 + 3 * i
        rb = slant_panel(k, f"Rank box {i + 1}", 460, ry(i) - 34, 550, ry(i) + 34, 14, COL['panel'], f, n - f); slash(rb, f)
        slash(T(k, f"Rank {i + 1}", str(i + 1), 505, ry(i), 40, COL['white'], f + 2, n, align='center'), f + 2)
    fa, fb, fc, fd = 56, 66, 86, 96                                      # out to the right / climb / back in
    movers = []
    for i, (tm, pts) in enumerate(rows):
        f = 6 + 3 * i; up = i == 4
        pn = slant_panel(k, f"Row {i + 1}", 566, ry(i) - 34, 1460, ry(i) + 34, 14, COL['red'] if up else COL['panel'], f, n - f)
        slash(pn, f)
        nm = slash(T(k, f"Team {i + 1}", tm, 600, ry(i), 40, COL['white'], f + 2, n), f + 2)
        if up:                                                           # the win first: 44 -> 47, then the climb
            pt = slash(T(k, f"Pts {i + 1}", pts, 1400, ry(i), 40, COL['white'], f + 2, n, align='right', end=48), f + 2)
            pt2 = slam(T(k, f"Pts {i + 1} new", "47", 1400, ry(i), 40, COL['white'], 48, n, align='right'), 48)
            movers.append((i, [pn, nm, pt2]))
        else:
            pt = slash(T(k, f"Pts {i + 1}", pts, 1400, ry(i), 40, COL['yellow'], f + 2, n, align='right'), f + 2)
            if 1 <= i <= 3: movers.append((i, [pn, nm, pt]))
    for i, objs in movers:
        for o in objs:
            bx, by = o.base
            if i == 4:   # out 240 px to the right, up three rows, back in: never passes another row's text
                o.addkeys(o.tr('position'), [(fa, [bx, by], 'Linear'), (fb, [bx + 240 / W, by], EXPO),
                                             (fc, [bx + 240 / W, by + 3 * step / H], BEZ['smooth']), (fd, [bx, by + 3 * step / H], EXPO)])
            else:        # rows 2-4 drop one place together while the mover is out to the side
                o.addkeys(o.tr('position'), [(fb, [bx, by], 'Linear'), (fc, [bx, by - step / H], BEZ['smooth'])])
    # the climb badge: a green up arrow and +3 beside the row's new place
    a = arrow(k, "Climb arrow", 1510, ry(1), 34, C3['green'], True, fd + 2, n); slam(a, fd + 2)
    fade(T(k, "Climb", "+3", 1540, ry(1), 34, C3['on'], fd + 4, n), fd + 4)


# ---------------------------------------------------------------- 7. fixture list
def fixtures(d):
    n = 150
    k = d.comp("SP Fixtures", n, "sfx"); lab_bg(k, n)
    slash(T(k, "Fix title", "FIXTURES", 260, 190, 64, COL['white'], 0, n, track=1.2), 0)
    fade(T(k, "Fix round", "MATCHWEEK 31", 1660, 196, 28, C3['label'], 6, n, align='right', style='SemiBold', track=1.3), 6)
    rows = [("SAT 15:00", "HAWKS", "WOLVES", True), ("SAT 17:30", "BEARS", "FALCONS", False), ("SUN 13:00", "SHARKS", "TIGERS", False),
            ("SUN 15:30", "LIONS", "RAVENS", True), ("MON 20:00", "STAGS", "COMETS", False)]
    team_col = dict(HAWKS=COL['red'], WOLVES=COL['blue'])
    for i, (when, home, away, tv) in enumerate(rows):
        y = 320 + i * 120; f = 8 + 5 * i
        p = slant_panel(k, f"Fixture {i + 1}", 260, y - 44, 1660, y + 44, 20, COL['panel'], f, n - f); slash(p, f)
        slash(T(k, f"When {i + 1}", when, 310, y, 32, COL['yellow'], f + 2, n, track=1.1), f + 2)
        slash(T(k, f"Home {i + 1}", home, 870, y, 44, COL['white'], f + 3, n, align='right'), f + 3)
        vs = k.ell(f"VS chip {i + 1}", 960, y, 72, 72, C3['panel2'], f0=f + 4, dur=n - f - 4); slam(vs, f + 4)
        slam(T(k, f"VS {i + 1}", "VS", 960, y, 28, C3['label'], f + 4, n, align='center'), f + 4)
        slash(T(k, f"Away {i + 1}", away, 1050, y, 44, COL['white'], f + 5, n), f + 5)
        for side, tm, x in (("home", home, 870 - textw(home, 44, 'ExtraBold') - 30), ("away", away, 1050 + textw(away, 44, 'ExtraBold') + 30)):
            if tm in team_col:
                ch = k.rect(f"Colour {side} {i + 1}", x, y, 12, 44, team_col[tm], f0=f + 6, dur=n - f - 6, center=True); fade(ch, f + 6)
        if tv:                                                           # the live-on-TV fixtures get a tag, one after the other
            ft = 64 + 10 * (i // 3)
            b = k.rect(f"Live tag {i + 1}", 1550, y, 120, 46, COL['white'], f0=ft, dur=n - ft, center=True); slam(b, ft)
            slam(T(k, f"Live {i + 1}", "LIVE", 1550, y, 28, COL['ink'], ft, n, align='center', track=1.2), ft)


# ---------------------------------------------------------------- 8. match-day poster
def shield(k, name, x, y, w, h, col, f, n):
    """a crest stand-in: flat top, straight sides, a point at the bottom"""
    s = k.path(name, [(x - w / 2, y - h / 2), (x + w / 2, y - h / 2), (x + w / 2, y + h * 0.1), (x, y + h / 2), (x - w / 2, y + h * 0.1)],
               f0=f, dur=n - f, closed=True,
               handles=[((0, 0), (0, 0), True), ((0, 0), (0, 0), True), ((0, 0), (0, h * 0.25), False), ((w * 0.3, -h * 0.1), (-w * 0.3, -h * 0.1), False),
                        ((0, h * 0.25), (0, 0), False)])
    s.fill(col); return s


def match_day(d):
    n = 120
    k = d.comp("SP Match day", n, "smd"); lab_bg(k, n)
    # two slanted bands in the team colours, inside the frame, slashing in from opposite corners
    rb = k.path("Band red", [(0, 760), (760, 1080), (380, 1080), (0, 920)], f0=0, dur=n, closed=True); rb.fill(COL['red'])
    bb = k.path("Band blue", [(1160, 0), (1920, 0), (1920, 320), (1540, 160)], f0=0, dur=n, closed=True); bb.fill(COL['blue'])
    for o, sx, sy in ((rb, -1, 1), (bb, 1, -1)):
        bx, by = o.base
        o.pos([(0, [bx + sx * 0.4, by - sy * 0.3], 'Linear'), (12, [bx, by], EXPO)])
    t = T(k, "Match day", "MATCH DAY", 960, 250, 170, COL['white'], 6, n, align='center', track=1.05); slam(t, 6)
    ul = k.rect("Underline", 960, 352, 560, 12, COL['yellow'], f0=14, dur=n - 14, center=True)
    ul.scale([(14, [0.0, 1.0], 'Linear'), (24, [1.0, 1.0], EXPO)])
    for i, (tm, ini, col, x, f) in enumerate((("HAWKS", "H", COL['red'], 560, 20), ("WOLVES", "W", COL['blue'], 1360, 26))):
        sh = shield(k, f"Crest {i + 1}", x, 560, 190, 230, col, f, n); sh.stroke(COL['white'], 6)
        sh.scale([(f, 0.0, 'Linear'), (f + 12, 1.0, BACK)])
        T(k, f"Crest letter {i + 1}", ini, x, 535, 110, COL['white'], f + 6, n, align='center').scale([(f + 6, 0.0, 'Linear'), (f + 14, 1.0, BACK)])
        slash(T(k, f"Team {i + 1}", tm, x, 730, 60, COL['white'], f + 8, n, align='center', track=1.1), f + 8)
    slam(T(k, "VS", "VS", 960, 560, 90, COL['yellow'], 36, n, align='center'), 36)
    info = "SUN 12 NOV  ·  16:30  ·  RIVER STADIUM"
    iw = 1160                                                           # the tracked line measures 1000 px (textw ignores tracking) + 80 px each side
    ip = slant_panel(k, "Info bar", 960 - iw / 2, 830, 960 + iw / 2, 906, 24, COL['yellow'], 46, n - 46); slash(ip, 46)
    slash(T(k, "Info", info, 960, 868, 38, COL['ink'], 50, n, align='center', track=1.15), 50)


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    live_clock(d); substitution(d); signing(d); touchdown(d); bracket(d); table_move(d); fixtures(d); match_day(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
