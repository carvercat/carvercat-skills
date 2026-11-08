"""Sports round 2 in design units: eight lab comps (player lower third, match-up title, standings table, full-time card,
starting lineup, player spotlight, replay stinger, slash wipe).

    import sports_lab2 as L; doc = L.build(); doc.send(client, PROJECT.carverproj)

Same palette and rules as sports_lab.py: diagonals, fast 8-14 f moves, one hit per beat. The pack's presets are baked as keys by
sports_lab's slash(), slam(), zoom_past() and exit_fade(). Rotations are degrees clockwise (the old kit stored counter-clockwise
values, so each is negated). Docs: ai/patterns/sports.md.
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sports_lab import (SDoc, W, COL, EXPO, BACK, ACCEL, BEZ, T, poly, outline, lab_bg, grow_x, slash, slam, zoom_past, exit_fade)


def slant_panel(k, name, x0, y0, x1, y1, slant, col, f0, dur):
    return poly(k, name, [(x0 + slant, y0), (x1, y0), (x1 - slant, y1), (x0, y1)], col, f0, dur)


def lower_third(d):
    n = 150
    k = d.comp("SP Lower third", n, "slt"); lab_bg(k, n)
    p1 = slant_panel(k, "LT number panel", 110, 820, 290, 960, 30, COL['red'], 0, n); slash(p1); zoom_past(p1)
    p2 = slant_panel(k, "LT name panel", 270, 820, 900, 960, 30, COL['panel'], 3, n - 3); slash(p2); zoom_past(p2)
    # after the name has slid past it (both Slash in from the lower left); big hits on text overlap the next line (lint text_overlap)
    exit_fade(slash(T(k, "LT number", "9", 200, 890, 96, COL['white'], 18, n - 18, align='center')))
    exit_fade(slash(T(k, "LT name", "JORDAN REYES", 330, 870, 56, COL['white'], 8, n - 8)))
    exit_fade(slash(T(k, "LT stat", "STRIKER  ·  14 GOALS", 330, 932, 30, COL['yellow'], 12, n - 12, style='SemiBold', track=1.2)))


def match_up(d):
    n = 90
    k = d.comp("SP Match up", n, "smu"); lab_bg(k, n)
    for i, (name, col, side) in enumerate([("HAWKS", COL['red'], -1), ("WOLVES", COL['blue'], 1)]):
        x0, x1 = (0, 900) if side < 0 else (1020, 1920)
        pnl = slant_panel(k, f"Team panel {i + 1}", x0 - 60 * (side > 0), 380, x1 + 60 * (side < 0), 700, 80, col, 0, n)
        bx, by = pnl.base
        pnl.pos([(0, (bx + side * 1000, by), 'linear'), (10, (bx, by), EXPO)])
        t = T(k, f"Team {i + 1}", name, 450 if side < 0 else 1470, 540, 120, COL['white'], 4, n - 4, align='center')
        tx, ty = t.base
        t.pos([(4, (tx + side * 600, ty), 'linear'), (14, (tx, ty), EXPO)])
        t.op([(4, 0.0, 'linear'), (7, 1.0, 'linear')])
    disc = k.ell("VS disc", 960, 540, 230, 230, COL['yellow'], f0=12, dur=n - 12); disc.stroke(COL['ink'], 10)
    slam(disc)
    slam(T(k, "VS", "VS", 960, 540, 110, COL['ink'], 14, n - 14, align='center'))
    slash(T(k, "Match info", "SATURDAY  ·  20:00  ·  RIVER STADIUM", 960, 790, 36, COL['grey'], 24, n - 24, style='SemiBold', align='center', track=1.2))


def standings(d):
    n = 150
    k = d.comp("SP Standings", n, "sst"); lab_bg(k, n)
    slash(T(k, "Table title", "LEAGUE TABLE", 480, 250, 56, COL['white'], 0, n, track=1.2))
    rows = [("1", "HAWKS", "54"), ("2", "WOLVES", "51"), ("3", "BEARS", "47"), ("4", "FALCONS", "44"), ("5", "SHARKS", "40")]
    hl = slant_panel(k, "Row highlight", 460, 534, 1460, 602, 20, COL['red'], 50, n - 50)     # row 3 (y 568)
    grow_x(hl, 50, 10)
    for i, (rk, tm, pts) in enumerate(rows):
        y, f = 400 + i * 84, 8 + i * 4
        if i != 2:                                                       # row 3 sits on the red highlight instead
            slash(slant_panel(k, f"Row {i + 1}", 460, y - 34, 1460, y + 34, 20, COL['panel'], f, n - f))
        for j, (s, x, al) in enumerate([(rk, 520, 'center'), (tm, 600, 'left'), (pts, 1400, 'right')]):
            slash(T(k, f"Cell {i + 1}.{j + 1}", s, x, y, 40, COL['yellow'] if j == 2 else COL['white'], f + 2, n - f - 2, align=al))


def full_time(d):
    n = 120
    k = d.comp("SP Full time", n, "sft"); lab_bg(k, n)
    slash(T(k, "FT label", "FULL TIME", 960, 300, 56, COL['yellow'], 0, n, align='center', track=1.4))
    for i, (tm, col, x) in enumerate([("HAWKS", COL['red'], 560), ("WOLVES", COL['blue'], 1360)]):
        slash(slant_panel(k, f"FT team box {i + 1}", x - 260, 470, x + 260, 610, 40, col, 4 + i * 4, n - 4 - i * 4))
        slash(T(k, f"FT team {i + 1}", tm, x, 540, 72, COL['white'], 8 + i * 4, n - 8 - i * 4, align='center'))
    slam(T(k, "FT score", "2 - 1", 960, 540, 140, COL['white'], 18, n - 18, align='center'))
    slash(T(k, "FT scorers", "REYES 23'  67'   ·   OKAFOR 81'", 960, 720, 34, COL['grey'], 30, n - 30, style='SemiBold', align='center', track=1.1))


def lineup(d):
    n = 150
    k = d.comp("SP Lineup", n, "slu"); lab_bg(k, n)
    slash(T(k, "Lineup title", "STARTING FIVE", 300, 220, 64, COL['white'], 0, n, track=1.2))
    names = [("1", "M. ALVES", "G"), ("7", "J. REYES", "F"), ("10", "A. MORGAN", "F"), ("14", "T. NAKAMURA", "D"), ("23", "K. OKAFOR", "C")]
    for i, (num, nm, pos) in enumerate(names):
        y, f = 360 + i * 120, 8 + i * 6
        slash(slant_panel(k, f"Num box {i + 1}", 300, y - 44, 420, y + 44, 18, COL['red'], f, n - f))
        slash(T(k, f"Num {i + 1}", num, 360, y, 48, COL['white'], f + 2, n - f - 2, align='center'))
        slash(T(k, f"Player {i + 1}", nm, 460, y, 52, COL['white'], f + 4, n - f - 4))
        slash(T(k, f"Pos {i + 1}", pos, 1100, y, 40, COL['yellow'], f + 6, n - f - 6, align='right'))


def spotlight(d):
    n = 120
    k = d.comp("SP Spotlight", n, "ssp"); lab_bg(k, n)
    cx, cy = 900, 820                                                    # the player's feet on the pitch
    base = k.ell("Spot base", cx, cy, 300, 90, None, f0=0, dur=n); base.stroke(COL['yellow'], 8)
    base.scale([(0, 0.0, 'linear'), (10, 1.0, BACK)])
    for i in range(3):
        f = 10 + i * 20
        r = k.ell(f"Spot ring {i + 1}", cx, cy, 300, 90, None, f0=f, dur=30); r.stroke(COL['yellow'], 5)
        r.scale([(f, 1.0, 'linear'), (f + 30, 1.8, BEZ['decel'])]); r.op([(f, 0.9, 'linear'), (f + 30, 0.0, 'linear')])
    arrow = k.ngon("Spot arrow", cx, 380, 70, 3, COL['yellow'], f0=6, dur=n - 6); arrow.rotv(90.0)   # a 3-gon points right; 90 deg clockwise points it down
    ax, ay = arrow.base
    arrow.pos([(6, (ax, ay - 60), 'linear'), (16, (ax, ay), EXPO)])
    arrow.op([(6, 0.0, 'linear'), (9, 1.0, 'linear')])
    slash(slant_panel(k, "Spot tag", cx - 200, 230, cx + 200, 320, 20, COL['red'], 10, n - 10))
    slash(T(k, "Spot name", "REYES  #9", cx, 275, 48, COL['white'], 12, n - 12, align='center'))


def replay_stinger(d):
    n = 45
    k = d.comp("SP Replay stinger", n, "srs")
    cols = [COL['red'], COL['blue'], COL['yellow']]
    for i in range(3):
        f = i * 3
        s = k.rect(f"Replay stripe {i + 1}", 960, 540, 1000, 500, cols[i], f0=f, dur=30, center=True)
        s.rotv(20.0); s.sc([2.6, 1.0])                                    # the old kit stored -20 (counter-clockwise)
        bx, by = s.base
        y = by + 162 - 162 * i
        off = 1.6 * W
        s.pos([(f, (bx - off, y), 'linear'), (f + 12, (bx, y), EXPO), (f + 18, (bx + 57.6, y), 'linear'),   # drifts: an oversized shape held still is cropped_at_rest
               (f + 30, (bx + off, y), ACCEL)])
    t = T(k, "Replay word", "REPLAY", 960, 540, 200, COL['white'], 10, 32, align='center')
    outline(t, COL['ink'], 0.05, True); slam(t); zoom_past(t)


def slash_wipe(d):
    n = 30
    k = d.comp("SP Slash wipe", n, "ssw")
    for i, col in enumerate([COL['blue'], COL['red'], COL['panel']]):
        f = i * 2
        s = k.rect(f"Slash {i + 1}", 960, 540, 1000, 1000, col, f0=f, dur=n - 4, center=True)
        s.rotv(25.0); s.sc([2.2, 2.4])                                    # 2200 px wide turned 25 deg still spans the frame
        bx, by = s.base
        s.pos([(f, (bx - 1.5 * W, by), 'linear'), (f + 10, (bx, by), BEZ['whip']), (f + 14, (bx + 57.6, by), 'linear'),
               (f + n - 4, (bx + 1.5 * W, by), ACCEL)])                   # keeps drifting while it covers (cropped_at_rest)


def build():
    d = SDoc()
    lower_third(d); match_up(d); standings(d); full_time(d); lineup(d); spotlight(d); replay_stinger(d); slash_wipe(d)
    return d


if __name__ == "__main__":
    print(__doc__)
