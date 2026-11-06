"""Data Viz round 2: eight more lab comps (column chart, stacked bar, progress rings,
before/after, timeline, waffle chart, area chart, data table), written straight into a
.carverproj.

    import data_viz_lab2 as L; presets, masks = L.build(PROJECT.carverproj)

Same palette, geometry rules and verification as data_viz_lab.py. After writing:
edit.open {path, force:true}; apply PRESETS (preset.apply); run mask.make + parent.clear
for each MASKS entry (the window FIRST); edit.save; check with carvercat_inspect and
carvercat_look; extract templates with comp_to_template.py (--drop "Lab bg").
Docs: ai/patterns/data-viz.md. Pixel space 1920x1080, y down; comp frames, 30 fps.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_viz_lab import Doc, lin, COL, EXPO, SMOOTH, SNAP, lab_bg, t_for_progress

PRESETS, MASKS = [], []


def fade(o, f, d=8):
    o.op([(f, 0, 'Linear'), (f + d, 1, 'Ease out')]); return o


def rise(o, f, dy=16, d=12):
    bx, by = o.base
    o.pos([(f, [bx, by + dy / 1080], 'Linear'), (f + d, [bx, by], EXPO)])   # y up: + starts it above and it settles down
    return fade(o, f, max(4, d // 2))


def column_chart(d):
    n = 90
    k = d.comp("DV Column chart", n, "dcc"); lab_bg(k, n)
    x0, x1, yb, h = 460, 1460, 800, 480
    for i, g in enumerate((0, 50, 100)):
        y = yb - g / 100 * h
        fade(k.line(f"Grid {g}", [(x0, y), (x1, y)], COL['grid'] if g else COL['muted'], px=2, f0=0, dur=n), i * 2)
        fade(k.text(f"Axis {g}", str(g), x0 - 24, y, 28, COL['muted'], f0=0, dur=n, style='Medium', align='right'), i * 2)
    vals = [("Jan", 42), ("Feb", 55), ("Mar", 49), ("Apr", 68), ("May", 74), ("Jun", 91)]
    pitch = (x1 - x0) / len(vals)
    for i, (m, v) in enumerate(vals):
        cx, bh, f = x0 + pitch * (i + 0.5), v / 100 * h, 8 + i * 4
        last = i == len(vals) - 1
        b = k.rect(f"Column {i + 1}", cx, yb - bh / 2, 96, bh, COL['cyan'] if last else COL['bar'], r=8, f0=f, dur=n - f, center=True)
        b.anchor(0, -1)
        PRESETS.append(("DV Column chart", f"Column {i + 1}", "Bar grow up - spring"))
        fade(k.text(f"Month {i + 1}", m, cx, yb + 40, 28, COL['muted'], f0=0, dur=n, style='Medium', align='center'), 4 + i * 2)
    g = 8 + 5 * 4 + 18                                                   # after the last column's spring
    cx = x0 + pitch * (len(vals) - 0.5)
    rise(k.text("Peak value", "91", cx, yb - 0.91 * h - 44, 40, COL['ink'], f0=g, dur=n - g, style='Bold', align='center'), g)


def stacked_bar(d):
    n = 90
    k = d.comp("DV Stacked bar", n, "dsb"); lab_bg(k, n)
    x0, wtot, y = 360, 1200, 500
    fade(k.text("Title", "Where the time goes", x0, 380, 44, COL['ink'], f0=0, dur=n, style='Bold'), 0)
    segs = [("Editing", 40, COL['cyan']), ("Review", 25, COL['orange']), ("Export", 20, COL['green']), ("Admin", 15, COL['pink'])]
    x = x0
    for i, (name, v, col) in enumerate(segs):
        w, f = v / 100 * wtot, 8 + i * 8
        s = k.rect(f"Segment {i + 1}", x + w / 2, y, w, 72, col, f0=f, dur=n - f, center=True)
        s.anchor(-1, 0)
        s.scale([(f, [0.0, 1.0], 'Linear'), (f + 12, [1.0, 1.0], EXPO)])   # no spring: an overshoot would cover the next segment
        lx, ly = x0 + i * 300, 640
        fade(k.rect(f"Swatch {i + 1}", lx, ly - 12, 24, 24, col, r=6, f0=f + 6, dur=n - f - 6), f + 6)
        fade(k.text(f"Legend {i + 1}", f"{name}  {v}%", lx + 40, ly, 30, COL['ink'], f0=f + 6, dur=n - f - 6, style='Medium'), f + 6)
        x += w


def progress_rings(d):
    n = 90
    k = d.comp("DV Progress rings", n, "dpr"); lab_bg(k, n)
    rings = [("Uptime", 0.82, COL['cyan']), ("Coverage", 0.64, COL['green']), ("Adoption", 0.45, COL['orange'])]
    dia, th = 300, 26
    for i, (name, v, col) in enumerate(rings):
        cx, cy, f = 560 + i * 400, 500, 6 + i * 6
        tr = k.ell(f"Track {i + 1}", cx, cy, dia, dia, None, f0=0, dur=n); tr.stroke(COL['track'], th)
        fade(tr, i * 3)
        o = k.ell(f"Ring {i + 1}", cx, cy, dia, dia, None, f0=0, dur=n); o.stroke(col, th, cap='round')
        o.rotv(90)                                                      # path starts at 12 o'clock (see data_viz_lab.py)
        tp = o.trim([(f, 1.0, 'Linear'), (f + 30, 1 - v, EXPO)], which='start'); o.set(tp + '.end', 1.0)
        o.op([(f, 0, 'Hold'), (f + 1, 1, 'Hold')])                      # round cap: hide the zero-length dot before the sweep
        fade(k.text(f"Value {i + 1}", f"{round(v * 100)}%", cx, cy, 64, COL['ink'], f0=0, dur=n, style='Bold', align='center'), f + 16)
        fade(k.text(f"Label {i + 1}", name, cx, cy + dia / 2 + 60, 30, COL['muted'], f0=0, dur=n, style='Medium', align='center'), i * 3 + 4)


def before_after(d):
    n = 90
    k = d.comp("DV Before after", n, "dba"); lab_bg(k, n)
    yb, h = 820, 520
    fade(k.line("Baseline", [(620, yb), (1300, yb)], COL['muted'], px=2, f0=0, dur=n), 0)
    for i, (name, v, col) in enumerate([("Before", 30, COL['bar']), ("After", 85, COL['cyan'])]):
        cx, bh, f = 800 + i * 320, v / 100 * h, 6 + i * 10
        b = k.rect(f"Bar {name}", cx, yb - bh / 2, 200, bh, col, r=12, f0=f, dur=n - f, center=True)
        b.anchor(0, -1)
        PRESETS.append(("DV Before after", f"Bar {name}", "Bar grow up - spring"))
        fade(k.text(f"Label {name}", name, cx, yb + 44, 32, COL['muted'], f0=0, dur=n, style='Medium', align='center'), 2 + i * 4)
        g = f + 18
        rise(k.text(f"Value {name}", f"{v} min" if i == 0 else f"{v} min", cx, yb - bh - 44, 40, COL['ink'], f0=g, dur=n - g, style='Bold', align='center'), g)
    badge = k.rect("Delta badge", 1460, 400, 200, 76, COL['green'], r=38, f0=40, dur=n - 40, center=True)
    PRESETS.append(("DV Before after", "Delta badge", "Pop - gentle"))
    k.text("Delta", "2.8x", 1460, 400, 40, COL['bg'], f0=42, dur=n - 42, style='Bold', align='center')
    PRESETS.append(("DV Before after", "Delta", "Zoom settle"))


def timeline(d):
    n = 120
    k = d.comp("DV Timeline", n, "dtl"); lab_bg(k, n)
    x0, x1, y, a, b = 260, 1660, 560, 6, 60
    ln = k.line("Axis", [(x0, y), (x1, y)], COL['muted'], px=4, f0=0, dur=n)
    ln.trim([(a, 0.0, 'Linear'), (b, 1.0, SMOOTH)])
    ms = [("2019", "Founded"), ("2020", "First 100 users"), ("2022", "Series A"), ("2024", "1M users"), ("2026", "Global launch")]
    for i, (yr, cap) in enumerate(ms):
        frac = i / (len(ms) - 1)
        x = x0 + frac * (x1 - x0)
        f = a + round(t_for_progress(SMOOTH, frac) * (b - a)) if frac > 0 else a
        col = COL['cyan'] if i == len(ms) - 1 else COL['ink']
        dot = k.ell(f"Milestone {i + 1}", x, y, 28, 28, col, f0=f, dur=n - f); dot.stroke(COL['bg'], 6)
        PRESETS.append(("DV Timeline", f"Milestone {i + 1}", "Data point pop"))
        rise(k.text(f"Year {i + 1}", yr, x, y - 70, 40, col, f0=f + 2, dur=n - f - 2, style='Bold', align='center'), f + 2)
        rise(k.text(f"Caption {i + 1}", cap, x, y + 70, 28, COL['muted'], f0=f + 5, dur=n - f - 5, style='Medium', align='center'), f + 5, dy=-16)


def waffle(d):
    n = 90
    k = d.comp("DV Waffle chart", n, "dwf"); lab_bg(k, n)
    v, cell, gap = 64, 44, 10
    gx, gy = 360, 540 - (10 * (cell + gap) - gap) / 2
    for i in range(100):
        r, c = divmod(i, 10)
        x, y = gx + c * (cell + gap) + cell / 2, gy + r * (cell + gap) + cell / 2
        on = i < v
        f = 4 + i // 2 if on else 2 + r                                 # filled cells in reading order, 2 a frame
        o = k.rect(f"Cell {i + 1}", x, y, cell, cell, COL['cyan'] if on else COL['track'], r=8, f0=f, dur=n - f, center=True)
        if on:
            o.scale([(f, 0.4, 'Linear'), (f + 8, 1.0, EXPO)])
        o.op([(f, 0, 'Linear'), (f + 4, 1, 'Linear')])
    fv = 4 + (v - 1) // 2 + 8
    big = k.text("Waffle value", f"{v}%", 1000, 470, 160, COL['ink'], f0=fv, dur=n - fv, style='Bold')
    rise(big, fv, d=14)
    rise(k.text("Waffle label", "of teams ship weekly", 1000, 600, 40, COL['muted'], f0=fv + 4, dur=n - fv - 4, style='Medium'), fv + 4)


def area_chart(d):
    n = 90
    k = d.comp("DV Area chart", n, "dac"); lab_bg(k, n)
    x0, x1, yb, h, a, b = 360, 1560, 820, 520, 8, 50
    vals = [20, 34, 30, 48, 55, 52, 70, 86]
    pts = [(x0 + i * (x1 - x0) / (len(vals) - 1), yb - v / 100 * h) for i, v in enumerate(vals)]
    fade(k.line("Baseline", [(x0, yb), (x1, yb)], COL['muted'], px=2, f0=0, dur=n), 0)
    win = k.rect("Window", x0 + (x1 - x0 + 20) / 2 - 10, yb - h / 2 - 10, x1 - x0 + 20, h + 40, COL['ink'], f0=0, dur=n, center=True)
    win.anchor(-1, 0)
    win.scale([(a, [0.0, 1.0], 'Linear'), (b, [1.0, 1.0], SMOOTH)])        # same timing as the line: the fill follows the pen
    area = k.path("Area", pts + [(x1, yb), (x0, yb)], f0=0, dur=n, closed=True)
    area.fill(COL['cyan']); area.opv(0.28)
    MASKS.append(("DV Area chart", "Area", "Window"))
    ln = k.line("Line", pts, COL['cyan'], px=6, f0=0, dur=n)
    ln.trim([(a, 0.0, 'Linear'), (b, 1.0, SMOOTH)])
    lx, ly = pts[-1]
    rise(k.text("End value", "86", lx, ly - 52, 40, COL['ink'], f0=b, dur=n - b, style='Bold', align='center'), b)


def data_table(d):
    n = 120
    k = d.comp("DV Data table", n, "ddt"); lab_bg(k, n)
    cols = [(420, 'left'), (1040, 'right'), (1260, 'right'), (1500, 'right')]
    head = ["Team", "Q1", "Q2", "Change"]
    rows = [("Design", "41", "52", "+27%"), ("Engineering", "88", "97", "+10%"), ("Marketing", "35", "31", "-11%"), ("Support", "60", "72", "+20%")]
    fade(k.line("Header rule", [(400, 330), (1520, 330)], COL['muted'], px=2, f0=0, dur=n), 0)
    for j, (x, al) in enumerate(cols):
        fade(k.text(f"Head {j + 1}", head[j], x, 290, 28, COL['muted'], f0=0, dur=n, style='SemiBold', align=al), j * 2)
    hl = k.rect("Row highlight", 960, 400 + 3 * 90, 1140, 76, lin('1B2B3F'), r=12, f0=56, dur=n - 56, center=True)
    hl.anchor(-1, 0); hl.scale([(56, [0.0, 1.0], 'Linear'), (70, [1.0, 1.0], EXPO)])
    for i, row in enumerate(rows):
        y, f = 400 + i * 90, 8 + i * 6
        for j, (x, al) in enumerate(cols):
            col = COL['ink']
            if j == 3: col = COL['green'] if row[3].startswith('+') else COL['pink']
            rise(k.text(f"Cell {i + 1}.{j + 1}", row[j], x, y, 34, col, f0=f, dur=n - f, style='Bold' if j in (0, 3) else 'Medium', align=al), f)


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    column_chart(d); stacked_bar(d); progress_rings(d); before_after(d); timeline(d); waffle(d); area_chart(d); data_table(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
