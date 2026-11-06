"""Sports round 2: eight more lab comps (player lower third, match-up title, standings table,
full-time card, starting lineup, player spotlight, replay stinger, slash wipe), written
straight into a .carverproj.

    import sports_lab2 as L; presets, masks = L.build(PROJECT.carverproj)

Same palette and rules as sports_lab.py: diagonals, fast 8-14 f moves, one hit per beat.
After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); edit.save; check
with carvercat_inspect and carvercat_look; extract templates with comp_to_template.py
(--drop "Lab bg"). Docs: ai/patterns/sports.md.
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sports_lab import Doc, lin, P, COL, EXPO, BACK, lab_bg, grow_x
from cc import BEZ

ACCEL = BEZ['accel']
PRESETS, MASKS = [], []


def slant_panel(k, name, x0, y0, x1, y1, slant, col, f0, dur):
    p = k.path(name, [(x0 + slant, y0), (x1, y0), (x1 - slant, y1), (x0, y1)], f0=f0, dur=dur, closed=True); p.fill(col)
    return p


def lower_third(d):
    n = 150
    k = d.comp("SP Lower third", n, "slt"); lab_bg(k, n)
    slant_panel(k, "LT number panel", 110, 820, 290, 960, 30, COL['red'], 0, n)
    PRESETS.extend([("SP Lower third", "LT number panel", "Slash in"), ("SP Lower third", "LT number panel", "Zoom past")])
    slant_panel(k, "LT name panel", 270, 820, 900, 960, 30, COL['panel'], 3, n - 3)
    PRESETS.extend([("SP Lower third", "LT name panel", "Slash in"), ("SP Lower third", "LT name panel", "Zoom past")])
    k.text("LT number", "9", 200, 890, 96, COL['white'], f0=18, dur=n - 18,   # after the name has slid past it (both Slash in from the lower left)
           style='ExtraBold', align='center')
    PRESETS.extend([("SP Lower third", "LT number", "Slash in"), ("SP Lower third", "LT number", "Exit fade - fast")])   # Impact slam (220%) and Zoom past (300%) on texts overlap the next line: lint text_overlap
    k.text("LT name", "JORDAN REYES", 330, 870, 56, COL['white'], f0=8, dur=n - 8, style='ExtraBold')
    PRESETS.extend([("SP Lower third", "LT name", "Slash in"), ("SP Lower third", "LT name", "Exit fade - fast")])
    k.text("LT stat", "STRIKER  ·  14 GOALS", 330, 932, 30, COL['yellow'], f0=12, dur=n - 12, style='SemiBold', track=1.2)
    PRESETS.extend([("SP Lower third", "LT stat", "Slash in"), ("SP Lower third", "LT stat", "Exit fade - fast")])


def match_up(d):
    n = 90
    k = d.comp("SP Match up", n, "smu"); lab_bg(k, n)
    for i, (name, col, side) in enumerate([("HAWKS", COL['red'], -1), ("WOLVES", COL['blue'], 1)]):
        x0, x1 = (0, 900) if side < 0 else (1020, 1920)
        pnl = slant_panel(k, f"Team panel {i + 1}", x0 - 60 * (side > 0), 380, x1 + 60 * (side < 0), 700, 80, col, 0, n)
        bx, by = pnl.base
        pnl.pos([(0, [bx + side * 1000 / 1920, by], 'Linear'), (10, [bx, by], EXPO)])
        t = k.text(f"Team {i + 1}", name, 450 if side < 0 else 1470, 540, 120, COL['white'], f0=4, dur=n - 4, style='ExtraBold', align='center')
        tx, ty = t.base
        t.pos([(4, [tx + side * 600 / 1920, ty], 'Linear'), (14, [tx, ty], EXPO)])
        t.op([(4, 0.0, 'Linear'), (7, 1.0, 'Linear')])
    disc = k.ell("VS disc", 960, 540, 230, 230, COL['yellow'], f0=12, dur=n - 12); disc.stroke(COL['ink'], 10)
    PRESETS.append(("SP Match up", "VS disc", "Impact slam"))
    k.text("VS", "VS", 960, 540, 110, COL['ink'], f0=14, dur=n - 14, style='ExtraBold', align='center')
    PRESETS.append(("SP Match up", "VS", "Impact slam"))
    k.text("Match info", "SATURDAY  ·  20:00  ·  RIVER STADIUM", 960, 790, 36, COL['grey'], f0=24, dur=n - 24, style='SemiBold', align='center', track=1.2)
    PRESETS.append(("SP Match up", "Match info", "Slash in"))


def standings(d):
    n = 150
    k = d.comp("SP Standings", n, "sst"); lab_bg(k, n)
    k.text("Table title", "LEAGUE TABLE", 480, 250, 56, COL['white'], f0=0, dur=n, style='ExtraBold', track=1.2)
    PRESETS.append(("SP Standings", "Table title", "Slash in"))
    rows = [("1", "HAWKS", "54"), ("2", "WOLVES", "51"), ("3", "BEARS", "47"), ("4", "FALCONS", "44"), ("5", "SHARKS", "40")]
    hl = slant_panel(k, "Row highlight", 460, 534, 1460, 602, 20, COL['red'], 50, n - 50)     # row 3 (y 568)
    grow_x(hl, 50, 10)
    for i, (rk, tm, pts) in enumerate(rows):
        y, f = 400 + i * 84, 8 + i * 4
        if i != 2:                                                       # row 3 (y 568) sits on the red highlight instead
            slant_panel(k, f"Row {i + 1}", 460, y - 34, 1460, y + 34, 20, COL['panel'], f, n - f)
            PRESETS.append(("SP Standings", f"Row {i + 1}", "Slash in"))
        for j, (s, x, al) in enumerate([(rk, 520, 'center'), (tm, 600, 'left'), (pts, 1400, 'right')]):
            k.text(f"Cell {i + 1}.{j + 1}", s, x, y, 40, COL['yellow'] if j == 2 else COL['white'], f0=f + 2, dur=n - f - 2, style='ExtraBold', align=al)
            PRESETS.append(("SP Standings", f"Cell {i + 1}.{j + 1}", "Slash in"))


def full_time(d):
    n = 120
    k = d.comp("SP Full time", n, "sft"); lab_bg(k, n)
    k.text("FT label", "FULL TIME", 960, 300, 56, COL['yellow'], f0=0, dur=n, style='ExtraBold', align='center', track=1.4)
    PRESETS.append(("SP Full time", "FT label", "Slash in"))
    for i, (tm, col, x) in enumerate([("HAWKS", COL['red'], 560), ("WOLVES", COL['blue'], 1360)]):
        slant_panel(k, f"FT team box {i + 1}", x - 260, 470, x + 260, 610, 40, col, 4 + i * 4, n - 4 - i * 4)
        PRESETS.append(("SP Full time", f"FT team box {i + 1}", "Slash in"))
        k.text(f"FT team {i + 1}", tm, x, 540, 72, COL['white'], f0=8 + i * 4, dur=n - 8 - i * 4, style='ExtraBold', align='center')
        PRESETS.append(("SP Full time", f"FT team {i + 1}", "Slash in"))
    k.text("FT score", "2 - 1", 960, 540, 140, COL['white'], f0=18, dur=n - 18, style='ExtraBold', align='center')
    PRESETS.append(("SP Full time", "FT score", "Impact slam"))
    k.text("FT scorers", "REYES 23'  67'   ·   OKAFOR 81'", 960, 720, 34, COL['grey'], f0=30, dur=n - 30, style='SemiBold', align='center', track=1.1)
    PRESETS.append(("SP Full time", "FT scorers", "Slash in"))


def lineup(d):
    n = 150
    k = d.comp("SP Lineup", n, "slu"); lab_bg(k, n)
    k.text("Lineup title", "STARTING FIVE", 300, 220, 64, COL['white'], f0=0, dur=n, style='ExtraBold', track=1.2)
    PRESETS.append(("SP Lineup", "Lineup title", "Slash in"))
    names = [("1", "M. ALVES", "G"), ("7", "J. REYES", "F"), ("10", "A. MORGAN", "F"), ("14", "T. NAKAMURA", "D"), ("23", "K. OKAFOR", "C")]
    for i, (num, nm, pos) in enumerate(names):
        y, f = 360 + i * 120, 8 + i * 6
        box = slant_panel(k, f"Num box {i + 1}", 300, y - 44, 420, y + 44, 18, COL['red'], f, n - f)
        PRESETS.append(("SP Lineup", f"Num box {i + 1}", "Slash in"))
        k.text(f"Num {i + 1}", num, 360, y, 48, COL['white'], f0=f + 2, dur=n - f - 2, style='ExtraBold', align='center')
        PRESETS.append(("SP Lineup", f"Num {i + 1}", "Slash in"))
        k.text(f"Player {i + 1}", nm, 460, y, 52, COL['white'], f0=f + 4, dur=n - f - 4, style='ExtraBold')
        PRESETS.append(("SP Lineup", f"Player {i + 1}", "Slash in"))
        k.text(f"Pos {i + 1}", pos, 1100, y, 40, COL['yellow'], f0=f + 6, dur=n - f - 6, style='ExtraBold', align='right')
        PRESETS.append(("SP Lineup", f"Pos {i + 1}", "Slash in"))


def spotlight(d):
    n = 120
    k = d.comp("SP Spotlight", n, "ssp"); lab_bg(k, n)
    cx, cy = 900, 820                                                    # the player's feet on the pitch
    base = k.ell("Spot base", cx, cy, 300, 90, None, f0=0, dur=n); base.stroke(COL['yellow'], 8)
    base.scale([(0, 0.0, 'Linear'), (10, 1.0, BACK)])
    for i in range(3):
        f = 10 + i * 20
        r = k.ell(f"Spot ring {i + 1}", cx, cy, 300, 90, None, f0=f, dur=30); r.stroke(COL['yellow'], 5)
        r.scale([(f, 1.0, 'Linear'), (f + 30, 1.8, BEZ['decel'])]); r.op([(f, 0.9, 'Linear'), (f + 30, 0.0, 'Linear')])
    arrow = k.ngon("Spot arrow", cx, 380, 70, 3, COL['yellow'], f0=6, dur=n - 6); arrow.rotv(-90.0)   # a 3-gon points right; -90 deg (clockwise) points it down
    ax, ay = arrow.base
    arrow.pos([(6, [ax, ay + 60 / 1080], 'Linear'), (16, [ax, ay], EXPO)])
    arrow.op([(6, 0.0, 'Linear'), (9, 1.0, 'Linear')])
    tag = slant_panel(k, "Spot tag", cx - 200, 230, cx + 200, 320, 20, COL['red'], 10, n - 10)
    PRESETS.append(("SP Spotlight", "Spot tag", "Slash in"))
    k.text("Spot name", "REYES  #9", cx, 275, 48, COL['white'], f0=12, dur=n - 12, style='ExtraBold', align='center')
    PRESETS.append(("SP Spotlight", "Spot name", "Slash in"))


def replay_stinger(d):
    n = 45
    k = d.comp("SP Replay stinger", n, "srs")
    cols = [COL['red'], COL['blue'], COL['yellow']]
    for i in range(3):
        f = i * 3
        s = k.rect(f"Replay stripe {i + 1}", 960, 540, 1000, 500, cols[i], f0=f, dur=30, center=True)
        s.rotv(-20.0); s.sc([2.6, 1.0])
        bx, by = s.base
        off = 1.6
        s.pos([(f, [bx - off, by - 0.15 + i * 0.15], 'Linear'), (f + 12, [bx, by - 0.15 + i * 0.15], EXPO), (f + 18, [bx + 0.03, by - 0.15 + i * 0.15], 'Linear'),   # drifts: an oversized shape held still is cropped_at_rest
               (f + 30, [bx + off, by - 0.15 + i * 0.15], ACCEL)])
    t = k.text("Replay word", "REPLAY", 960, 540, 200, COL['white'], f0=10, dur=32, style='ExtraBold', align='center')
    t.set(t.src('text_outline', 'paint'), 'solid').set(t.src('text_outline', 'color'), COL['ink'][:3]).set(t.src('text_outline', 'thickness'), 0.05).set(t.src('text_outline', 'outsideOnly'), True)
    PRESETS.extend([("SP Replay stinger", "Replay word", "Impact slam"), ("SP Replay stinger", "Replay word", "Zoom past")])


def slash_wipe(d):
    n = 30
    k = d.comp("SP Slash wipe", n, "ssw")
    for i, col in enumerate([COL['blue'], COL['red'], COL['panel']]):
        f = i * 2
        s = k.rect(f"Slash {i + 1}", 960, 540, 1000, 1000, col, f0=f, dur=n - 4, center=True)
        s.rotv(-25.0); s.sc([2.2, 2.4])                                   # 2200 px wide turned 25 deg still spans the frame
        bx, by = s.base
        s.pos([(f, [bx - 1.5, by], 'Linear'), (f + 10, [bx, by], BEZ['whip']), (f + 14, [bx + 0.03, by], 'Linear'),
               (f + n - 4, [bx + 1.5, by], ACCEL)])                  # keeps drifting while it covers (cropped_at_rest)


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    lower_third(d); match_up(d); standings(d); full_time(d); lineup(d); spotlight(d); replay_stinger(d); slash_wipe(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
