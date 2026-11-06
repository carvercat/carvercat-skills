"""Data Viz round 3: seven lab comps for briefs the pack could not serve before (conversion funnel,
bubble chart, bar chart race, stacked area chart, tile-grid map, icon array, calendar heatmap),
written straight into a .carverproj.

    import data_viz_lab3 as L; presets, masks = L.build(PROJECT.carverproj)

Same palette, font and geometry rules as data_viz_lab.py. Every move is baked as keys (no presets
to apply). The stacked area chart is revealed by three mask windows: after edit.open {path,
force:true} run mask.make {ids:[window, layer]} (the window FIRST) + parent.clear for each MASKS
entry, then edit.save. Check with carvercat_inspect and carvercat_look; extract templates with
comp_to_template.py (--drop "Lab bg"). All numbers are sample data and every comp says so on screen.
Fonts: Rethink Sans must be installed (KI-136). Docs: ai/patterns/data-viz.md (round 3).
Pixel space 1920x1080, y down; comp frames, 30 fps.
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_viz_lab import Doc, lin, COL, EXPO, SMOOTH, lab_bg
from data_viz_lab2 import fade, rise
from json_author.cc import P

ACCEL = (0.3, 0.0, 0.8, 0.15)
PRESETS, MASKS = [], []
SLATE = lin('56607A')                      # a second context grey, lighter than COL['bar']
# sequential scale for the map and the heatmap: dark slate-blue to the pack's cyan
SEQ = [lin('243247'), lin('1F4D6E'), lin('236E98'), lin('2F92C4'), lin('3FB8F0')]


def header(k, n, title, sub, x0=360, x1=1560, f=0):
    """Title and subtitle top-left, 'Sample data' top-right on the subtitle row."""
    fade(k.text("Title", title, x0, 150, 48, COL['ink'], f0=0, dur=n, style='Bold'), f)
    fade(k.text("Subtitle", sub, x0, 208, 30, COL['muted'], f0=0, dur=n, style='Medium'), f + 3)
    fade(k.text("Source", "Sample data", x1, 208, 28, COL['muted'], f0=0, dur=n, style='Medium', align='right'), f + 6)


def fillkey(o, spec):
    return o.key(o.src('shape_fill', 'color'), spec)


def textkey(o, spec):
    return o.key(o.src('text_fill', 'color'), spec)


# ---------------------------------------------------------------- 1. conversion funnel
FUNNEL = [("Visited store", 48200), ("Viewed product", 21700), ("Added to cart", 8460), ("Started checkout", 4120), ("Purchased", 2890)]


def funnel(d):
    n = 150
    k = d.comp("DV Funnel", n, "dfn"); lab_bg(k, n)
    header(k, n, "Checkout funnel, March", "Shoppers at each step")
    cx, wmax, bh = 1080, 880, 80
    ys = [300 + i * 136 for i in range(len(FUNNEL))]
    ws = [v / FUNNEL[0][1] * wmax for _, v in FUNNEL]
    rates = [FUNNEL[i + 1][1] / FUNNEL[i][1] for i in range(len(FUNNEL) - 1)]
    worst = min(range(len(rates)), key=lambda i: rates[i])
    starts = [6 + i * 8 for i in range(len(FUNNEL))]
    # connectors first: they sit under the bars
    for i, r in enumerate(rates):
        f = starts[i + 1] + 10
        y0, y1 = ys[i] + bh / 2, ys[i + 1] - bh / 2
        c = k.path(f"Connector {i + 1}", [(cx - ws[i] / 2, y0), (cx + ws[i] / 2, y0), (cx + ws[i + 1] / 2, y1), (cx - ws[i + 1] / 2, y1)],
                   f0=f, dur=n - f, closed=True)
        c.fill(COL['orange'] if i == worst else COL['grid'])
        c.op([(f, 0.0, 'Linear'), (f + 8, 0.55 if i == worst else 1.0, 'Ease out')])
        rise(k.text(f"Rate {i + 1}", f"{round(r * 100)}% continue", 1600, (ys[i] + ys[i + 1]) / 2, 28,
                    COL['orange'] if i == worst else COL['muted'], f0=f, dur=n - f, style='SemiBold' if i == worst else 'Medium'), f)
    for i, ((name, v), y, w, f) in enumerate(zip(FUNNEL, ys, ws, starts)):
        fade(k.text(f"Step {i + 1}", name, 600, y, 32, COL['ink'], f0=0, dur=n, style='Medium', align='right'), max(0, f - 4))
        b = k.rect(f"Bar {i + 1}", cx, y, w, bh, COL['cyan'], r=10, f0=f, dur=n - f, center=True)
        b.scale([(f, [0.0, 1.0], 'Linear'), (f + 14, [1.0, 1.0], EXPO)])          # from the centre line out, no overshoot
        g = f + 10
        rise(k.text(f"Value {i + 1}", f"{v:,}", 1600, y, 36, COL['ink'], f0=g, dur=n - g, style='Bold'), g)
    a = 66
    rise(k.text("Annotation", "Biggest drop: product page to cart", 360, 950, 30, COL['orange'], f0=a, dur=n - a, style='SemiBold'), a)


# ---------------------------------------------------------------- 2. bubble chart
BUBBLES = [("Apex", 32, 88, 14), ("Bolt", 12, 71, 22), ("Cove", 9, 86, 9), ("Drift", 24, 79, 31), ("Ember", 18, 66, 12),
           ("Flux", 36, 92, 6), ("Glow", 27, 74, 18), ("Halo", 15, 81, 26), ("Iris", 6, 68, 7), ("Jolt", 21, 84, 16)]


def bubble(d):
    n = 150
    k = d.comp("DV Bubble chart", n, "dbc"); lab_bg(k, n)
    header(k, n, "Price vs satisfaction", "Ten team-chat apps; bubble size = paying teams")
    x0, x1, yb, yt = 360, 1560, 860, 340
    X = lambda v: x0 + v / 40 * (x1 - x0)
    Y = lambda s: yb - (s - 60) / 40 * (yb - yt)
    for i, s in enumerate((60, 70, 80, 90, 100)):
        fade(k.line(f"Grid {s}", [(x0, Y(s)), (x1, Y(s))], COL['muted'] if s == 60 else COL['grid'], px=2, f0=0, dur=n), i * 2)
        fade(k.text(f"Y label {s}", str(s), x0 - 24, Y(s), 28, COL['muted'], f0=0, dur=n, style='Medium', align='right'), i * 2)
    for i, p in enumerate((0, 10, 20, 30, 40)):
        fade(k.text(f"X label {p}", f"${p}", X(p), yb + 40, 28, COL['muted'], f0=0, dur=n, style='Medium', align='center'), 2 + i * 2)
    fade(k.text("X title", "Price per seat, per month", (x0 + x1) / 2, yb + 92, 28, COL['muted'], f0=0, dur=n, style='Medium',
                align='center'), 8)
    fade(k.text("Y title", "Satisfaction score", x0, yt - 44, 28, COL['muted'], f0=0, dur=n, style='Medium'), 8)
    order = sorted(range(len(BUBBLES)), key=lambda i: BUBBLES[i][1])     # they land in price order, left to right
    hero = 2
    for j, i in enumerate(sorted(order, key=lambda i: -BUBBLES[i][3])):  # big ones drawn first, so small ones stay visible
        name, p, s, t = BUBBLES[i]
        dia = 2 * math.sqrt(t / 31) * 55
        f = 14 + order.index(i) * 4
        b = k.ell(f"Bubble {name}", X(p), Y(s), dia, dia, COL['cyan'] if i == hero else SLATE, f0=f, dur=n - f)
        b.stroke(COL['bg'], 3)
        b.scale([(f, 0.0, 'Linear'), (f + 12, 1.0, EXPO)])
        if i == hero:
            b.op([(f, 0.0, 'Linear'), (f + 3, 1.0, 'Linear')])
        else:
            b.op([(f, 0.0, 'Linear'), (f + 3, 0.9, 'Linear'), (60, 0.9, 'Linear'), (70, 0.55, 'Ease out')])   # context steps back
    name, p, s, t = BUBBLES[hero]
    dia = 2 * math.sqrt(t / 31) * 55
    ring = k.ell("Hero ring", X(p), Y(s), dia + 24, dia + 24, None, f0=60, dur=n - 60); ring.stroke(COL['cyan'], 3)
    ring.scale([(60, 0.7, 'Linear'), (74, 1.0, EXPO)]); fade(ring, 60, 6)
    rise(k.text("Hero name", "Cove", X(p), Y(s) - dia / 2 - 100, 34, COL['cyan'], f0=64, dur=n - 64, style='Bold', align='center'), 64)
    rise(k.text("Hero note", "$9 a seat, score 86", X(p), Y(s) - dia / 2 - 60, 28, COL['ink'], f0=68, dur=n - 68, style='Medium',
                align='center'), 68)


# ---------------------------------------------------------------- 3. bar chart race
RACE_YEARS = ["2022", "2023", "2024", "2025"]
RACE = [("Harbor", [410, 455, 470, 488]), ("Midtown", [520, 540, 505, 498]), ("Riverside", [300, 380, 478, 540]),
        ("Old Town", [350, 360, 395, 410]), ("Airport", [180, 260, 340, 452])]


def race(d):
    n = 220
    k = d.comp("DV Bar race", n, "drc"); lab_bg(k, n)
    header(k, n, "Bike-share rides by station", "Rides per year, thousands")
    x0, scale, bh = 520, 1000 / 600, 72
    rowy = lambda r: 330 + r * 110
    T = [(60, 80), (112, 132), (164, 184)]                 # transitions (start, end): 20 f, smooth; 32 f holds between
    ranks = []
    for y in range(len(RACE_YEARS)):
        order = sorted(range(len(RACE)), key=lambda i: -RACE[i][1][y])
        ranks.append({i: order.index(i) for i in range(len(RACE))})
    # names that swap places in a transition dim while they cross (lint checks text_overlap while texts move)
    crossing = [{i for i in range(len(RACE)) for j in range(len(RACE))
                 if (ranks[y - 1][i] - ranks[y - 1][j]) * (ranks[y][i] - ranks[y][j]) < 0} for y in range(1, len(RACE_YEARS))]
    hero = 2
    for i, (name, vals) in enumerate(RACE):
        ws = [v * scale for v in vals]; wm = max(ws)
        ys = [rowy(ranks[y][i]) for y in range(len(vals))]
        f = 4 + ranks[0][i] * 3
        col = COL['cyan'] if i == hero else COL['bar']
        xc = x0 + wm / 2
        b = k.rect(f"Bar {name}", xc, ys[0], wm, bh, col, r=8, f0=f, dur=n - f, center=True)
        b.anchor(-1, 0)                                    # grows from the left edge; width = value on a fixed scale
        sk = [(f, [0.0, 1.0], 'Linear'), (f + 16, [ws[0] / wm, 1.0], EXPO)]
        pk = []
        for y, (a, e) in enumerate(T, start=1):
            sk += [(a, [ws[y - 1] / wm, 1.0], 'Linear'), (e, [ws[y] / wm, 1.0], SMOOTH)]
            pk += [(a, P(xc, ys[y - 1]), 'Linear'), (e, P(xc, ys[y]), SMOOTH)]
        b.scale(sk); b.pos(pk); fade(b, f, 4)
        lab = k.text(f"Name {name}", name, x0 - 24, ys[0], 32, COL['ink'] if i == hero else COL['muted'], f0=0, dur=n,
                     style='SemiBold' if i == hero else 'Medium', align='right')
        lab.pos([kk for y, (a, e) in enumerate(T, start=1)
                 for kk in ((a, P(x0 - 24, ys[y - 1]), 'Linear'), (e, P(x0 - 24, ys[y]), SMOOTH))])
        ok = [(max(0, f - 2), 0.0, 'Linear'), (f + 6, 1.0, 'Ease out')]
        for y, (a, e) in enumerate(T, start=1):
            if i in crossing[y - 1]:
                ok += [(a, 1.0, 'Linear'), (a + 4, 0.0, ACCEL), (e - 4, 0.0, 'Linear'), (e + 2, 1.0, 'Ease out')]
        lab.op(ok)
        # one value text per year, shown on the holds; its clip ends as it fades out
        for y, v in enumerate(vals):
            g = f + 12 if y == 0 else T[y - 1][1] - 2
            end = T[y][0] + 4 if y < len(T) else n
            t = k.text(f"Value {name} {RACE_YEARS[y]}", str(v), x0 + ws[y] + 16, ys[y], 30, COL['ink'], f0=g, dur=end - g,
                       style='Bold' if i == hero else 'SemiBold')
            if y < len(T):
                t.op([(g, 0.0, 'Linear'), (g + 6, 1.0, 'Ease out'), (T[y][0], 1.0, 'Linear'), (end, 0.0, ACCEL)])
            else:
                fade(t, g, 6)
    # the year: one text per year, cut in sequence (never two on screen at once)
    for y, yr in enumerate(RACE_YEARS):
        a = 4 if y == 0 else T[y - 1][0] + 6
        e = T[y][0] + 6 if y < len(T) else n
        t = k.text(f"Year {yr}", yr, 1560, 900, 120, COL['muted'], f0=a, dur=e - a, style='Bold', align='right')
        if y < len(T):
            t.op([(a, 0.0, 'Linear'), (a + 6, 1.0, 'Ease out'), (T[y][0], 1.0, 'Linear'), (e, 0.0, ACCEL)])
        else:
            fade(t, a, 6)


# ---------------------------------------------------------------- 4. stacked area chart
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
LAYERS = [("Android", [10.2, 10.4, 10.5, 10.9, 11.0, 11.3, 11.5, 11.6, 11.9, 12.1, 12.2, 12.5], COL['bar']),
          ("iOS", [8.0, 8.3, 8.6, 8.8, 9.1, 9.3, 9.6, 9.8, 10.1, 10.3, 10.6, 10.9], SLATE),
          ("Web", [3.1, 3.6, 4.2, 4.9, 5.8, 6.6, 7.7, 8.9, 10.2, 11.8, 13.5, 15.4], COL['cyan'])]


def stacked_area(d):
    n = 150
    k = d.comp("DV Stacked area", n, "dsa"); lab_bg(k, n)
    header(k, n, "Monthly active users by platform", "Millions of users, stacked", x1=1480)
    x0, x1, yb, h, a, b = 360, 1480, 860, 520, 8, 56
    X = lambda i: x0 + i * (x1 - x0) / (len(MONTHS) - 1)
    Y = lambda v: yb - v / 40 * h
    for i, g in enumerate((0, 10, 20, 30, 40)):
        fade(k.line(f"Grid {g}", [(x0, Y(g)), (x1, Y(g))], COL['muted'] if g == 0 else COL['grid'], px=2, f0=0, dur=n), i * 2)
        fade(k.text(f"Axis {g}", f"{g}M" if g else "0", x0 - 24, Y(g), 28, COL['muted'], f0=0, dur=n, style='Medium', align='right'), i * 2)
    for i in range(0, 12, 2):
        fade(k.text(f"Month {MONTHS[i]}", MONTHS[i], X(i), yb + 40, 28, COL['muted'], f0=0, dur=n, style='Medium', align='center'), 2 + i)
    base = [0.0] * len(MONTHS)
    tops = []
    for j, (name, vals, col) in enumerate(LAYERS):
        top = [base[i] + vals[i] for i in range(len(MONTHS))]
        win = k.rect(f"Window {j + 1}", x0 + (x1 - x0 + 20) / 2 - 10, yb - h / 2 - 10, x1 - x0 + 20, h + 40, COL['ink'], f0=0, dur=n,
                     center=True)
        win.anchor(-1, 0)
        win.scale([(a, [0.0, 1.0], 'Linear'), (b, [1.0, 1.0], SMOOTH)])        # one window per layer, all on one timing
        pts = [(X(i), Y(top[i])) for i in range(len(MONTHS))] + [(X(i), Y(base[i])) for i in reversed(range(len(MONTHS)))]
        ar = k.path(f"Layer {name}", pts, f0=0, dur=n, closed=True)
        ar.fill(col)
        MASKS.append(("DV Stacked area", f"Layer {name}", f"Window {j + 1}"))
        tops.append(top); base = top
    # the highlight layer's top edge draws with the reveal
    ln = k.line("Web edge", [(X(i), Y(tops[2][i])) for i in range(len(MONTHS))], lin('9ADCF8'), px=4, f0=0, dur=n)
    ln.trim([(a, 0.0, 'Linear'), (b, 1.0, SMOOTH)])
    prev = [0.0] * len(MONTHS)
    for j, (name, vals, col) in enumerate(LAYERS):
        mid = prev[-1] + vals[-1] / 2
        f = b + 2 + j * 4
        rise(k.text(f"Label {name}", f"{name} {vals[-1]}M", x1 + 24, Y(mid), 30, COL['cyan'] if name == "Web" else COL['ink'], f0=f,
                    dur=n - f, style='Bold' if name == "Web" else 'Medium'), f)
        prev = [prev[i] + vals[i] for i in range(len(MONTHS))]
    # annotate the month the highlight layer passes iOS
    i = 8
    px_, py_ = X(i), Y(tops[2][i])
    f = 70
    dot = k.ell("Callout dot", px_, py_, 22, 22, COL['ink'], f0=f, dur=n - f); dot.stroke(COL['bg'], 4)
    dot.scale([(f, 0.0, 'Linear'), (f + 10, 1.0, EXPO)]); fade(dot, f, 3)
    st = k.line("Callout stem", [(px_, py_ - 18), (px_, py_ - 70)], COL['ink'], px=3, f0=f + 4, dur=n - f - 4)
    st.trim([(f + 4, 0.0, 'Linear'), (f + 12, 1.0, EXPO)])
    rise(k.text("Callout", "Sep: Web passes iOS", px_, py_ - 100, 30, COL['ink'], f0=f + 10, dur=n - f - 10, style='SemiBold',
                align='center'), f + 10)


# ---------------------------------------------------------------- 5. tile-grid map (choropleth)
TILES = {0: [("AK", 0), ("ME", 10)], 1: [("WI", 5), ("VT", 9), ("NH", 10)],
         2: [("WA", 0), ("ID", 1), ("MT", 2), ("ND", 3), ("MN", 4), ("IL", 5), ("MI", 6), ("NY", 8), ("MA", 9)],
         3: [("OR", 0), ("NV", 1), ("WY", 2), ("SD", 3), ("IA", 4), ("IN", 5), ("OH", 6), ("PA", 7), ("NJ", 8), ("CT", 9), ("RI", 10)],
         4: [("CA", 0), ("UT", 1), ("CO", 2), ("NE", 3), ("MO", 4), ("KY", 5), ("WV", 6), ("VA", 7), ("MD", 8), ("DE", 9)],
         5: [("AZ", 1), ("NM", 2), ("KS", 3), ("AR", 4), ("TN", 5), ("NC", 6), ("SC", 7), ("DC", 8)],
         6: [("OK", 3), ("LA", 4), ("MS", 5), ("AL", 6), ("GA", 7)],
         7: [("HI", 0), ("TX", 3), ("FL", 8)]}
SOLAR = dict(AK=1, ME=4, WI=3, VT=7, NH=5, WA=4, ID=5, MT=3, ND=1, MN=3, IL=4, MI=3, NY=7, MA=10, OR=6, NV=15, WY=2, SD=1, IA=3,
             IN=2, OH=3, PA=4, NJ=11, CT=8, RI=7, CA=19, UT=13, CO=10, NE=2, MO=3, KY=2, WV=1, VA=5, MD=8, DE=6, AZ=17, NM=12, KS=3,
             AR=3, TN=3, NC=7, SC=5, DC=9, OK=3, LA=5, MS=2, AL=2, GA=5, HI=21, TX=11, FL=13)
BINS = [(4, "Under 4%"), (8, "4 to 7%"), (12, "8 to 11%"), (16, "12 to 15%"), (101, "16% and over")]


def tile_map(d):
    n = 150
    k = d.comp("DV Tile map", n, "dcm"); lab_bg(k, n)
    header(k, n, "Homes with rooftop solar", "Share of homes, by state", x0=300, x1=1700)
    gx, gy, pitch, ts = 300, 268, 84, 76
    for r, row in TILES.items():
        for st, c in row:
            v = SOLAR[st]
            b = next(i for i, (hi, _) in enumerate(BINS) if v < hi)
            x, y = gx + c * pitch + ts / 2, gy + r * pitch + ts / 2
            f = 4 + c + r                                       # a diagonal sweep from the north-west corner
            t = k.rect(f"Tile {st}", x, y, ts, ts, COL['track'], r=10, f0=f, dur=n - f, center=True)
            t.scale([(f, 0.6, 'Linear'), (f + 10, 1.0, EXPO)]); fade(t, f, 4)
            g = 34 + c * 2 + r                                  # then the values fill in, west to east
            fillkey(t, [(g, COL['track'], 'Linear'), (g + 8, SEQ[b], 'Ease out')])
            lab = k.text(f"State {st}", st, x, y, 28, COL['ink'], f0=f, dur=n - f, style='SemiBold', align='center')
            fade(lab, f + 2, 4)
            if b >= 3:                                          # dark ink on the two brightest bins
                textkey(lab, [(g, COL['ink'], 'Linear'), (g + 8, COL['bg'], 'Ease out')])
    lx, ly = 1340, 420
    fade(k.text("Legend title", "Share of homes", lx, ly - 64, 30, COL['ink'], f0=0, dur=n, style='SemiBold'), 60)
    for i, (_, name) in enumerate(BINS):
        f = 62 + i * 3
        fade(k.rect(f"Legend swatch {i + 1}", lx + 20, ly + i * 56, 40, 40, SEQ[i], r=8, f0=f, dur=n - f, center=True), f)
        fade(k.text(f"Legend {i + 1}", name, lx + 60, ly + i * 56, 28, COL['muted'], f0=f, dur=n - f, style='Medium'), f)
    # highlight the top value: a ring on its tile and a note under the legend
    hx, hy = gx + 0 * pitch + ts / 2, gy + 7 * pitch + ts / 2
    f = 84
    ring = k.rect("Top ring", hx, hy, ts + 16, ts + 16, None, r=14, f0=f, dur=n - f, center=True); ring.stroke(COL['ink'], 4)
    ring.scale([(f, 1.3, 'Linear'), (f + 12, 1.0, EXPO)]); fade(ring, f, 6)
    rise(k.text("Top note", "Highest: Hawaii, 21%", lx, ly + 5 * 56 + 40, 30, COL['ink'], f0=f + 4, dur=n - f - 4, style='SemiBold'), f + 4)


# ---------------------------------------------------------------- 6. icon array
def icon_array(d):
    n = 120
    k = d.comp("DV Icon array", n, "dia"); lab_bg(k, n)
    header(k, n, "Who works fully remote?", "Survey of 2,000 office workers", x1=1640)
    gx, gy, px_, py_ = 300, 330, 72, 132
    for r in range(4):
        for c in range(10):
            x, y = gx + c * px_ + 25, gy + r * py_
            on = r == 0                                         # one in every column of four
            f = 4 + c * 2 + r
            head = k.ell(f"Head {r + 1}.{c + 1}", x, y, 30, 30, COL['track'], f0=f, dur=n - f)
            body = k.rect(f"Body {r + 1}.{c + 1}", x, y + 54, 50, 62, COL['track'], r=20, f0=f, dur=n - f, center=True)
            for o in (head, body):
                o.scale([(f, 0.6, 'Linear'), (f + 10, 1.0, EXPO)]); fade(o, f, 4)
                if on:
                    g = 36 + c * 3
                    fillkey(o, [(g, COL['track'], 'Linear'), (g + 6, COL['cyan'], 'Ease out')])
    fv = 70
    rise(k.text("Stat", "1 in 4", 1100, 460, 160, COL['cyan'], f0=fv, dur=n - fv, style='Bold'), fv, d=14)
    rise(k.text("Stat label", "work fully remote", 1104, 580, 44, COL['ink'], f0=fv + 4, dur=n - fv - 4, style='Medium'), fv + 4)


# ---------------------------------------------------------------- 7. calendar heatmap
def heat_minutes(weeks=20, seed=7):
    """deterministic sample activity in minutes: weekends longer, a week off (week 7), a training block (weeks 12-15)"""
    import random
    rnd = random.Random(seed); out = []
    for w in range(weeks):
        for dw in range(7):
            m = 0 if rnd.random() < 0.3 else rnd.randint(10, 55)
            if dw >= 5 and m: m += rnd.randint(10, 30)
            if w == 6: m = 0
            if 12 <= w <= 15 and rnd.random() < 0.85: m = max(m, rnd.randint(35, 80))
            out.append(m)
    return out


def heat_level(m):
    return 0 if m == 0 else 1 if m <= 20 else 2 if m <= 40 else 3 if m <= 60 else 4


def heatmap(d):
    n = 150
    k = d.comp("DV Heatmap", n, "dhm"); lab_bg(k, n)
    header(k, n, "Days with exercise, January to May", "Active minutes per day; one square per day", x0=440, x1=1472)
    gx, gy, pitch, cs, weeks = 440, 384, 52, 44, 20
    for i, (r, name) in enumerate(((0, "Mon"), (2, "Wed"), (4, "Fri"), (6, "Sun"))):
        fade(k.text(f"Day {name}", name, gx - 20, gy + r * pitch + cs / 2, 28, COL['muted'], f0=0, dur=n, style='Medium', align='right'), i * 2)
    for i, (wk, name) in enumerate(((0, "Jan"), (4, "Feb"), (8, "Mar"), (13, "Apr"), (17, "May"))):
        fade(k.text(f"Month {name}", name, gx + wk * pitch, gy - 34, 28, COL['muted'], f0=0, dur=n, style='Medium'), 2 + i * 2)
    mins = heat_minutes(weeks)
    for w in range(weeks):
        for dw in range(7):
            lvl = heat_level(mins[w * 7 + dw])
            x, y = gx + w * pitch + cs / 2, gy + dw * pitch + cs / 2
            f = 6 + w + dw // 3                                  # week columns sweep left to right
            c = k.rect(f"Day {w + 1}.{dw + 1}", x, y, cs, cs, SEQ[lvl], r=8, f0=f, dur=n - f, center=True)
            c.scale([(f, 0.5, 'Linear'), (f + 8, 1.0, EXPO)]); fade(c, f, 4)
    ly = gy + 7 * pitch + 40
    fade(k.text("Legend less", "Less", gx, ly, 28, COL['muted'], f0=0, dur=n, style='Medium'), 40)
    for i in range(5):
        fade(k.rect(f"Legend {i + 1}", gx + 96 + i * 40, ly, 32, 32, SEQ[i], r=6, f0=40, dur=n - 40, center=True), 40 + i)
    fade(k.text("Legend more", "More", gx + 96 + 4 * 40 + 36, ly, 28, COL['muted'], f0=0, dur=n, style='Medium'), 45)
    # the best week: an outline drawn round its column, then the note under it
    bw = max(range(weeks), key=lambda w: sum(mins[w * 7:w * 7 + 7])); tot = sum(mins[bw * 7:bw * 7 + 7]); f = 52
    ox, oy = gx + bw * pitch + cs / 2, gy + 3 * pitch + cs / 2
    o = k.rect("Best week", ox, oy, cs + 16, 7 * pitch - 8 + 16, None, r=12, f0=f, dur=n - f, center=True)
    o.stroke(COL['ink'], 4)
    o.trim([(f, 0.0, 'Linear'), (f + 16, 1.0, SMOOTH)])
    rise(k.text("Best week note", f"Best week: {tot // 60} h {tot % 60} min", ox + cs / 2 + 8, ly, 30, COL['ink'], f0=f + 14, dur=n - f - 14,
                style='SemiBold', align='right'), f + 14)


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    funnel(d); bubble(d); race(d); stacked_area(d); tile_map(d); icon_array(d); heatmap(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
