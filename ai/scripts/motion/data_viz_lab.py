"""Write the Data Viz lab comps (round 1) in design units (cc2.py through dvsu_kit.py).

    import data_viz_lab as L; doc = L.build(); doc.send(client, PROJECT.carverproj)   # scene.apply per comp, presets, edit.save

Measured on 0.1.8.1: an ellipse's stroke path starts at 3 o'clock and runs counter-clockwise, so Trim Stroke 0 -> 0.25 draws
3 -> 12 o'clock. The donut turns its rings by -90 degrees (a quarter turn counter-clockwise, which is how design units say
the old kit's +90), so the path starts at 12 o'clock, and draws each clockwise share [a, b] as native [1 - b, 1 - a].
The gauge needle sweeps from -180 to -50.4 degrees (clockwise, over the top).

Presets (Bar grow across - spring, Data point pop) are applied after the comps exist (KDoc.send), as before.
Docs: ai/patterns/data-viz.md. Design units: px from the top-left, y down; comp frames, 30 fps.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dvsu_kit import KDoc, css, BEZ, bezier, EASE_OUT

COL = dict(bg=css('0F1420'), ink=css('E8ECF4'), muted=css('7C8599'), grid=css('252C3B'), track=css('2A3244'),
           cyan=css('3FB8F0'), orange=css('F59E0B'), green=css('34D399'), pink=css('F472B6'), bar=css('3A4458'))
EXPO, SMOOTH = BEZ['expo'], BEZ['smooth']
SNAP = (0.34, 1.15, 0.64, 1)


def lab_bg(k, n):
    k.rect("Lab bg", 0, 0, 1920, 1080, COL['bg'], f0=0, dur=n)


def cubic(p0, p1, p2, p3, u):
    v = 1 - u
    return v * v * v * p0 + 3 * v * v * u * p1 + 3 * v * u * u * p2 + u * u * u * p3


def t_for_progress(bez, frac):
    """time fraction at which a cubic-bezier ease reaches `frac` of its value"""
    x1, y1, x2, y2 = bez
    lo, hi = 0.0, 1.0
    for _ in range(60):
        u = (lo + hi) / 2
        if cubic(0, y1, y2, 1, u) < frac: lo = u
        else: hi = u
    return cubic(0, x1, x2, 1, (lo + hi) / 2)


def line_chart(d):
    n = 90
    k = d.comp("DV Line chart", n, "dlc"); lab_bg(k, n)
    x0, x1, yb, yt = 360, 1560, 820, 260
    vals = [32, 45, 41, 58, 66, 84]
    for i, g in enumerate((0, 25, 50, 75, 100)):
        y = yb - g / 100 * (yb - yt)
        gl = k.line(f"Grid {g}", [(x0, y), (x1, y)], COL['grid'], px=2, f0=0, dur=n)
        gl.op([(i * 2, 0, 'Linear'), (i * 2 + 8, 1, 'Ease out')])
        lab = k.text(f"Axis {g}", str(g), x0 - 24, y, 28, COL['muted'], f0=0, dur=n, style='Medium', align='right')
        lab.op([(i * 2, 0, 'Linear'), (i * 2 + 8, 1, 'Ease out')])
    pts = [(x0 + i * (x1 - x0) / (len(vals) - 1), yb - v / 100 * (yb - yt)) for i, v in enumerate(vals)]
    line = k.line("Line", pts, COL['cyan'], px=6, f0=0, dur=n)
    a, b = 10, 55
    line.trim([(a, 0.0, 'Linear'), (b, 1.0, SMOOTH)], which='end')
    seg = [((pts[i + 1][0] - pts[i][0]) ** 2 + (pts[i + 1][1] - pts[i][1]) ** 2) ** 0.5 for i in range(len(pts) - 1)]
    total, run = sum(seg), 0.0
    for i, (x, y) in enumerate(pts):
        frac = run / total
        if i < len(seg): run += seg[i]
        f = a + round(t_for_progress(SMOOTH, frac) * (b - a)) if frac > 0 else a
        dot = k.ell(f"Point {i + 1}", x, y, 20, 20, COL['cyan'], f0=f, dur=n - f)
        dot.stroke(COL['bg'], 4)
        k.preset(f"Point {i + 1}", "Data point pop")
    lx, ly = pts[-1]
    val = k.text("End value", "84%", lx, ly - 52, 40, COL['ink'], f0=b, dur=n - b, style='Bold', align='center')
    bx, by = val.base
    val.pos([(b, (bx, by + 16), 'Linear'), (b + 12, (bx, by), EXPO)])      # rises 16 px into place
    val.op([(b, 0, 'Linear'), (b + 6, 1, 'Ease out')])


def donut(d):
    n = 90
    k = d.comp("DV Donut", n, "ddn"); lab_bg(k, n)
    cx, cy, dia, th = 960, 540, 420, 56
    track = k.ell("Track", cx, cy, dia, dia, None, f0=0, dur=n); track.stroke(COL['track'], th)
    track.op([(0, 0, 'Linear'), (8, 1, 'Ease out')])
    segs = [("Segment 1", 0.0, 0.46, COL['cyan'], 6), ("Segment 2", 0.46, 0.74, COL['orange'], 20), ("Segment 3", 0.74, 0.92, COL['green'], 32)]
    for name, s0, s1, col, f in segs:
        o = k.ell(name, cx, cy, dia, dia, None, f0=0, dur=n); o.stroke(col, th, cap='butt')
        o.rotv(-90)                              # a quarter turn counter-clockwise: the path now starts at 12 o'clock, still running CCW
        # clockwise share [s0, s1] from 12 o'clock = native [1 - s1, 1 - s0]: hold the end, sweep the start
        o.trim([(f, 1 - s0, 'Linear'), (f + 16, 1 - s1, EXPO)], which='start'); o.trim_static('end', 1 - s0)
    big = k.text("Centre value", "92%", cx, cy - 14, 96, COL['ink'], f0=0, dur=n, style='Bold', align='center')
    big.op([(30, 0, 'Linear'), (40, 1, 'Ease out')])
    sub = k.text("Centre label", "of goal", cx, cy + 56, 28, COL['muted'], f0=0, dur=n, style='Medium', align='center')
    sub.op([(34, 0, 'Linear'), (44, 1, 'Ease out')])


def ranked_bars(d):
    n = 90
    k = d.comp("DV Ranked bars", n, "drb"); lab_bg(k, n)
    rows = [("Design", 92), ("Engineering", 78), ("Marketing", 64), ("Sales", 51), ("Support", 37)]
    for i, (name, v) in enumerate(rows):
        y = 300 + i * 120; f = 6 + i * 4
        lab = k.text(f"Label {i + 1}", name, 520, y, 28, COL['ink'] if i == 0 else COL['muted'], f0=0, dur=n, style='Medium', align='right')
        lab.op([(i * 3, 0, 'Linear'), (i * 3 + 8, 1, 'Ease out')])
        w = v / 100 * 1000
        bar = k.rect(f"Bar {i + 1}", 560 + w / 2, y, w, 56, COL['cyan'] if i == 0 else COL['bar'], r=8, f0=f, dur=n - f, center=True)
        bar.anchor(-1, 0)
        k.preset(f"Bar {i + 1}", "Bar grow across - spring")
        g = f + 18                               # after the bar's spring has settled (its 4.4% overshoot reaches 40 px)
        val = k.text(f"Value {i + 1}", str(v), 560 + w + 20, y, 28, COL['ink'], f0=g, dur=n - g, style='SemiBold')
        vx, vy = val.base
        val.pos([(g, (vx - 12, vy), 'Linear'), (g + 10, (vx, vy), EXPO)])
        val.op([(g, 0, 'Linear'), (g + 6, 1, 'Ease out')])


def gauge(d):
    n = 75
    k = d.comp("DV Gauge", n, "dgg"); lab_bg(k, n)
    cx, cy, dia, th, v = 960, 660, 600, 40, 0.72
    track = k.ell("Gauge track", cx, cy, dia, dia, None, f0=0, dur=n); track.stroke(COL['track'], th, cap='butt')
    track.trim([(0, 0.5, 'Linear')], which='end'); track.trim_static('start', 0.0)   # top half: 3 -> 12 -> 9 o'clock
    fill = k.ell("Gauge fill", cx, cy, dia, dia, None, f0=0, dur=n); fill.stroke(COL['cyan'], th, cap='butt')
    fill.trim([(8, 0.5, 'Linear'), (40, 0.5 - 0.5 * v, SNAP)], which='start'); fill.trim_static('end', 0.5)
    L = 250
    needle = k.rect("Needle", cx + L / 2, cy, L, 10, COL['ink'], r=5, f0=0, dur=n, center=True)
    needle.anchor(-1, 0)
    needle.rot([(8, -180.0, 'Linear'), (40, -(180.0 - 180.0 * v), SNAP)])      # clockwise over the top
    k.ell("Hub", cx, cy, 40, 40, COL['ink'], f0=0, dur=n)
    val = k.text("Gauge value", "72", cx, cy + 100, 96, COL['ink'], f0=0, dur=n, style='Bold', align='center')
    val.op([(30, 0, 'Linear'), (40, 1, 'Ease out')])
    k.text("Gauge label", "Health score", cx, cy + 172, 30, COL['muted'], f0=0, dur=n, style='Medium', align='center')


def build(path=None, m=None):
    d = KDoc()
    line_chart(d); donut(d); ranked_bars(d); gauge(d)
    return d


if __name__ == "__main__":
    print(__doc__)
