"""Glitch round 3: eight lab comps for briefs the pack could not serve before (corrupted video title,
scan-line news ticker, hacker alert, cyber sale, signal-lost end card, error 404, game over,
chromatic logo sting), written straight into a .carverproj.

    import glitch_lab3 as L; presets, masks = L.build(PROJECT.carverproj)

Same palette and rules as glitch_lab.py: every glitch change is stepped (Hold keys), event frames on
one lane are at least 2 f apart and never two keys on one frame (lint same_frame_keys), opacity blips
stay small and few, saturated red never flickers, and everything that jumps stays inside the frame.
Every move is baked as keys (no presets to apply, no masks). After edit.open {path, force:true} and edit.save,
check with carvercat_inspect (curves, lint, qc for
flashes) and carvercat_look; extract templates with comp_to_template.py (--drop "Lab bg"). Names, scores, codes and handles are invented
stand-ins; replace them. Fonts: Rethink Sans must be installed (KI-136). Docs: ai/patterns/glitch.md
(round 3). Pixel space 1920x1080, y down; comp frames, 30 fps.
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from glitch_lab import Doc, lin, P, COL, lab_bg, held
from cc import BEZ, textw

EXPO = BEZ['expo']
GREY = lin('8A8A8A')                    # secondary copy on the near-black ground
PANEL = lin('141414')
PRESETS, MASKS = [], []


# ---------------------------------------------------------------- baked glitch moves
def rgb_split(t, events, op=0.85):
    """two hard drop shadows (red, cyan) on one text; events = [(frame, px)] of Hold jumps (red goes -px, cyan +px).
    End the list with (f, 0) to settle. One text, so no second copy for lint text_overlap."""
    for col, sign in ((COL['red'], -1), (COL['cyan'], 1)):
        fx = t.shadow(x=0.0, y=0.0, soft=0.0, op=op)
        r, g, b = col[:3]; t.set(fx + '.red', r).set(fx + '.green', g).set(fx + '.blue', b)
        t.key(fx + '.x', held([(f, round(sign * px / 1920, 5)) for f, px in events]))
    return t


def jolt(o, events):
    """held horizontal jumps: events = [(frame, dx px)], last one should be (f, 0)"""
    bx, by = o.base
    o.pos(held([(f, [bx + dx / 1920, by]) for f, dx in events]))
    return o


def stretch_hit(o, f):
    """the pack's Glitch stretch hit as Hold keys: 160 x 60% -> 85 x 110% -> 112 x 95% -> 100%, settles f+6"""
    o.scale(held([(f, [1.6, 0.6]), (f + 2, [0.85, 1.1]), (f + 4, [1.12, 0.95]), (f + 6, [1.0, 1.0])]))
    return o


def blink_in(o, f, steps=((0, 0.0), (1, 1.0), (3, 0.4), (5, 1.0))):
    """stepped arrival: opacity Hold steps from the clip start (small text only)"""
    o.op(held([(f + df, v) for df, v in steps]))
    return o


def crt_on(o, f, sx=1.0):
    """a panel switching on like a tube: height 2% -> 40% -> 104% -> 100% on Hold steps, settles f+6"""
    o.scale(held([(f, [sx, 0.02]), (f + 2, [sx, 0.4]), (f + 4, [sx, 1.04]), (f + 6, [sx, 1.0])]))
    return o


def steps_x(o, f, vals, gap=2, ax=-1):
    """a bar that fills in Hold steps from its left edge: scale X through vals"""
    o.anchor(ax, 0)
    o.scale(held([(f + i * gap, [v, 1.0]) for i, v in enumerate(vals)]))
    return o


def blocks(k, prefix, rng, n, x0, x1, y0, y1, frames, op=0.75):
    """block artefacts: each one its own 2-4 f clip (nothing to collide with same_frame_keys), inside the box"""
    cols = (COL['red'], COL['cyan'], COL['green'], COL['white'])
    for i in range(n):
        w, h = rng.choice((60, 100, 160)), rng.choice((24, 40, 64))
        x, y = rng.randint(x0, x1 - w), rng.randint(y0, y1 - h)
        b = k.rect(f"{prefix} {i + 1}", x, y, w, h, cols[i % 4], f0=rng.choice(frames), dur=rng.choice((2, 4)))
        b.opv(op)


# ---------------------------------------------------------------- 1. corrupted video title
def video_title(d):
    n = 120
    k = d.comp("GL Video title", n, "gvt"); lab_bg(k, n)
    x0 = 160
    blink_in(k.text("Kicker", "EP. 07  //  NEW VIDEO", x0, 300, 40, COL['green'], f0=0, dur=n, style='SemiBold', track=1.3), 0)
    for i, (s, y, f) in enumerate((("I LET AN AI", 450, 4), ("RUN MY WEEK", 610, 10))):
        t = k.text(f"Title {i + 1}", s, x0, y, 150, COL['white'], f0=f, dur=n - f, style='ExtraBold')
        ev = [(f, 28), (f + 3, 16), (f + 6, 24), (f + 9, 8), (f + 12, 0)]
        ev += [(70 + i * 4, 10), (72 + i * 4, 4), (74 + i * 4, 0)]          # one small re-glitch in the hold
        rgb_split(t, ev)
        jolt(t, [(f, 44), (f + 3, -26), (f + 6, 14), (f + 9, 0), (70 + i * 4, -18), (72 + i * 4, 0)])
    blocks(k, "Block", random.Random(31), 8, x0, 1300, 380, 680, (4, 6, 10, 12, 14))
    w2 = textw("RUN MY WEEK", 150, 'ExtraBold')
    steps_x(k.rect("Underline", x0, 700, w2, 12, COL['red'], f0=20, dur=n - 20), 20, (0.15, 0.45, 0.7, 1.0))
    blink_in(k.text("Meta", "nullbyte  ·  12:48", x0, 770, 40, GREY, f0=26, dur=n - 26, style='Medium'), 26)


# ---------------------------------------------------------------- 2. scan-line news ticker
HEADLINES = ["SERVERS BACK ONLINE AFTER SIX-HOUR OUTAGE", "PATCH 2.4 ROLLS OUT TONIGHT",
             "FINALS MOVE TO SATURDAY", "NEW MAP LEAKS AHEAD OF LAUNCH"]


def news_ticker(d):
    n = 150
    k = d.comp("GL News ticker", n, "gnt"); lab_bg(k, n)
    yb, hb = 960, 100                                   # ticker band centre and height
    band = k.rect("Ticker band", 960, yb, 1920, hb, PANEL, f0=0, dur=n, center=True)
    crt_on(band, 0)
    for i in range(3):                                  # static scan lines on the band (thin, faint, never flicker)
        k.rect(f"Scan line {i + 1}", 960, yb - 30 + i * 30, 1920, 2, COL['white'], f0=6, dur=n - 6, center=True).opv(0.05)
    yt = yb - hb / 2 - 34                               # the tag row sits on top of the band, left
    tw = textw("BREAKING", 40, 'ExtraBold') + 60
    tag = k.rect("Tag plate", 40 + tw / 2, yt, tw, 68, COL['red'], f0=2, dur=n - 2, center=True)
    crt_on(tag, 2)
    t = k.text("Tag", "BREAKING", 40 + tw / 2, yt, 40, COL['white'], f0=6, dur=n - 6, style='ExtraBold', align='center')
    rgb_split(t, [(6, 12), (9, 6), (12, 0), (70, 8), (72, 0), (120, 8), (122, 0)])
    lw = textw("LIVE", 32, 'SemiBold') * 1.5 + 80               # tracking 1.3 is not in textw
    lx = 40 + tw + 16
    chip = k.rect("Live chip", lx + lw / 2, yt, lw, 68, PANEL, f0=8, dur=n - 8, center=True)
    crt_on(chip, 8)
    dot = k.ell("Live dot", lx + 28, yt, 16, 16, COL['green'], f0=8, dur=n - 8)
    dot.op(held([(8, 1.0)] + [(f, 0.3 if j % 2 == 0 else 1.0) for j, f in enumerate(range(40, n, 15))]))   # 1 s period, tiny area
    blink_in(k.text("Live", "LIVE", lx + 48, yt, 32, COL['white'], f0=8, dur=n - 8, style='SemiBold', track=1.3), 8)
    # headlines scroll left at a constant speed and leave through the frame edge; one clip per headline (reading time)
    v = 7.0                                             # px per frame
    x = 240.0                                           # headline 1 is whole until about f34
    sep = textw("  ///  ", 44, 'SemiBold')
    for i, s in enumerate(HEADLINES):
        if n - (x - 1920) / v < 50: break               # a headline needs 50 f on screen to be read (lint reading_time)
        w = textw(s, 44, 'SemiBold')
        h = k.text(f"Headline {i + 1}", s, x, yb, 44, COL['white'], f0=0, dur=n, style='SemiBold')
        bx, by = h.base
        h.pos([(0, [bx, by], 'Linear'), (n, [bx - v * n / 1920, by], 'Linear')])
        blink_in(h, 10)
        x += w + sep


# ---------------------------------------------------------------- 3. hacker alert
def hack_alert(d):
    n = 150
    k = d.comp("GL Hack alert", n, "gha"); lab_bg(k, n)
    pan = k.rect("Alert panel", 960, 520, 1200, 540, PANEL, f0=0, dur=n, center=True); pan.stroke(COL['red'], 6)
    crt_on(pan, 0)
    tri = k.path("Warning sign", [(960, 290), (1022, 396), (898, 396)], f0=6, dur=n - 6, closed=True)
    tri.stroke(COL['red'], 10); blink_in(tri, 6)
    blink_in(k.text("Warning mark", "!", 960, 366, 64, COL['red'], f0=6, dur=n - 6, style='ExtraBold', align='center'), 6)
    t = k.text("Alert title", "INTRUSION DETECTED", 960, 480, 96, COL['white'], f0=8, dur=n - 8, style='ExtraBold', align='center')
    rgb_split(t, [(8, 24), (11, 12), (14, 20), (17, 6), (20, 0), (90, 10), (92, 0)])
    jolt(t, [(8, 30), (11, -18), (14, 8), (17, 0)])
    blink_in(k.text("Alert detail", "unauthorised access  ·  node 7  ·  03:14:07", 960, 568, 40, COL['green'], f0=16, dur=n - 16,
                    style='SemiBold', align='center'), 16)
    blink_in(k.text("Trace label", "TRACING SOURCE", 560, 650, 32, COL['green'], f0=24, dur=n - 24, style='SemiBold', track=1.3), 24)
    k.rect("Trace track", 960, 700, 800, 28, None, f0=24, dur=n - 24, center=True).stroke(GREY, 3)
    steps_x(k.rect("Trace fill", 560, 686, 800, 28, COL['red'], f0=24, dur=n - 24),
            24, (0.06, 0.21, 0.35, 0.52, 0.66, 0.81, 0.93, 1.0), gap=14)
    blocks(k, "Noise block", random.Random(41), 6, 380, 1540, 260, 780, (8, 12, 16, 60, 64), op=0.5)
    for i, y0 in enumerate((260, 520)):                         # two faint scan lines that roll down the panel, one way
        ln = k.rect(f"Scan line {i + 1}", 960, y0, 1180, 4, COL['white'], f0=10, dur=n - 10, center=True); ln.opv(0.05)
        bx, by = ln.base
        ln.pos([(10, [bx, by], 'Linear'), (n, [bx, by - 250 / 1080], 'Linear')])


# ---------------------------------------------------------------- 4. cyber sale
def cyber_sale(d):
    n = 150
    k = d.comp("GL Cyber sale", n, "gcs"); lab_bg(k, n)
    blink_in(k.text("Kicker", "CYBER MONDAY", 960, 230, 64, COL['cyan'], f0=0, dur=n, style='ExtraBold', align='center', track=1.4), 0)
    big = k.text("Discount", "-50%", 960, 450, 330, COL['white'], f0=6, dur=n - 6, style='ExtraBold', align='center')
    stretch_hit(big, 6)
    rgb_split(big, [(6, 40), (9, 24), (12, 34), (15, 10), (18, 0), (60, 16), (62, 6), (64, 0), (105, 16), (107, 6), (109, 0)])
    blocks(k, "Block", random.Random(53), 8, 560, 1360, 320, 600, (6, 8, 10, 12))   # entrance only: over the resting price the audit reads them as overlaps
    blink_in(k.text("Offer", "EVERYTHING  ·  24 HOURS ONLY", 960, 660, 48, COL['white'], f0=20, dur=n - 20, style='SemiBold',
                    align='center', track=1.2), 20)
    cw = textw("CODE  GLITCH50", 56, 'ExtraBold') + 80
    pl = k.rect("Code plate", 960, 790, cw, 100, PANEL, f0=30, dur=n - 30, center=True); pl.stroke(COL['green'], 4)
    crt_on(pl, 30)
    blink_in(k.text("Code", "CODE  GLITCH50", 960, 790, 56, COL['green'], f0=34, dur=n - 34, style='ExtraBold', align='center'), 34)
    blink_in(k.text("Footer", "ends midnight  ·  shop.example", 960, 920, 36, GREY, f0=40, dur=n - 40, style='Medium',
                    align='center'), 40)


# ---------------------------------------------------------------- 5. signal-lost end card
def end_card(d):
    n = 150
    k = d.comp("GL End card", n, "gse"); lab_bg(k, n)
    blink_in(k.text("Kicker", "//  SIGNAL LOST  —  STAY TUNED", 160, 170, 40, COL['green'], f0=0, dur=n, style='SemiBold', track=1.3), 0)
    for i, (cx, lab, f) in enumerate(((560, "WATCH NEXT", 4), (1360, "BEST OF THE CHANNEL", 10))):
        sl = k.rect(f"Slot {i + 1}", cx, 500, 760, 428, lin('1A1A1A'), f0=f, dur=n - f, center=True); sl.stroke(GREY, 4)
        crt_on(sl, f)
        bx, by = sl.base
        sl.pos(held([(f, [bx, by]), (60 + i * 40, [bx + (-1) ** i * 14 / 1920, by]), (62 + i * 40, [bx, by])]))
        blink_in(k.text(f"Slot label {i + 1}", lab, cx - 380, 760, 36, COL['white'], f0=f + 8, dur=n - f - 8, style='SemiBold',
                        track=1.2), f + 8)
    h = k.text("Handle", "@nullbyte", 160, 905, 72, COL['white'], f0=24, dur=n - 24, style='ExtraBold')
    rgb_split(h, [(24, 18), (27, 10), (30, 14), (33, 0), (110, 8), (112, 0)])
    jolt(h, [(24, 24), (27, -12), (30, 0)])
    sw = textw("SUBSCRIBE", 44, 'ExtraBold') + 90
    sub = k.rect("Subscribe plate", 1740 - sw / 2, 905, sw, 92, COL['red'], r=8, f0=30, dur=n - 30, center=True)
    crt_on(sub, 30)
    blink_in(k.text("Subscribe", "SUBSCRIBE", 1740 - sw / 2, 905, 44, COL['white'], f0=34, dur=n - 34, style='ExtraBold',
                    align='center'), 34)
    band = k.rect("Tracking band", 960, 540, 1920, 120, COL['white'], f0=0, dur=n, center=True); band.soft(40); band.opv(0.02)
    bx, by = band.base
    band.pos([(0, [bx, by + 600 / 1080], 'Linear'), (n, [bx, by - 600 / 1080], 'Linear')])     # rolls down once, one way


# ---------------------------------------------------------------- 6. error 404
def error_404(d):
    n = 120
    k = d.comp("GL Error 404", n, "gnf"); lab_bg(k, n)
    big = k.text("Code", "404", 960, 380, 380, COL['white'], f0=0, dur=n, style='ExtraBold', align='center')
    rgb_split(big, [(0, 36), (3, 20), (6, 30), (9, 12), (12, 0), (64, 18), (66, 8), (68, 0)])
    jolt(big, [(0, 40), (3, -24), (6, 12), (9, 0), (64, -20), (66, 0)])
    rng = random.Random(61)
    for i, (f, dur) in enumerate(((2, 2), (5, 3), (8, 2), (64, 2), (66, 2))):    # background-coloured tears cut the digits
        y = rng.randint(260, 500)
        k.rect(f"Tear {i + 1}", 600, y, 720, rng.choice((10, 16, 24)), COL['bg'], f0=f, dur=dur)
    blink_in(k.text("Headline", "PAGE NOT FOUND", 960, 640, 72, COL['cyan'], f0=10, dur=n - 10, style='ExtraBold', align='center',
                    track=1.2), 10)
    blink_in(k.text("Body", "this page drifted out of signal", 960, 725, 40, GREY, f0=16, dur=n - 16, style='Medium',
                    align='center'), 16)
    bt = k.rect("Button", 960, 860, 360, 96, None, r=48, f0=24, dur=n - 24, center=True); bt.stroke(COL['cyan'], 4)
    crt_on(bt, 24)
    fill = k.rect("Button press", 960, 860, 360, 96, COL['cyan'], r=48, f0=74, dur=n - 74, center=True)
    blink_in(fill, 74, ((0, 0.0), (1, 1.0)))
    lb = k.text("Button label", "GO HOME", 960, 860, 44, COL['cyan'], f0=28, dur=n - 28, style='ExtraBold', align='center')
    blink_in(lb, 28)
    lb.key(lb.src('text_fill', 'color'), held([(28, COL['cyan']), (75, COL['bg'])]))
    cur = k.path("Cursor", [(0, 0), (0, 54), (14, 41), (24, 64), (34, 60), (24, 37), (42, 37)], f0=40, dur=n - 40, closed=True)
    cur.fill(COL['white']); cur.stroke(COL['bg'], 3)
    bx, by = cur.base
    tx, ty = 1095 + 21, 880 + 32                                 # the tip lands on the button's right end, clear of the label
    cur.at(tx, ty); bx, by = cur.base
    cur.pos([(40, [bx + 420 / 1920, by - 200 / 1080], 'Linear'), (64, [bx, by], EXPO)])
    blink_in(cur, 40, ((0, 0.0), (2, 1.0)))
    cur.scale(held([(72, [1.0, 1.0]), (74, [0.85, 0.85]), (78, [1.0, 1.0])]))


# ---------------------------------------------------------------- 7. game over
def game_over(d):
    n = 150
    k = d.comp("GL Game over", n, "ggo"); lab_bg(k, n)
    t = k.text("Game over", "GAME OVER", 960, 380, 200, COL['red'], f0=0, dur=n, style='ExtraBold', align='center')
    stretch_hit(t, 0)
    fx = t.shadow(x=0.0, y=0.0, soft=0.0, op=0.9)
    r, g, b = COL['cyan'][:3]; t.set(fx + '.red', r).set(fx + '.green', g).set(fx + '.blue', b)
    t.key(fx + '.x', held([(0, 0.016), (3, -0.01), (6, 0.006), (9, 0.004)]))      # settles on a 8 px cyan offset
    jolt(t, [(0, -36), (3, 22), (6, -8), (9, 0)])
    blink_in(k.text("Score", "SCORE  004210", 960, 560, 48, COL['white'], f0=14, dur=n - 14, style='SemiBold', align='center',
                    track=1.3), 14)
    blink_in(k.text("Hi score", "HI  128000", 960, 630, 48, COL['green'], f0=18, dur=n - 18, style='SemiBold', align='center',
                    track=1.3), 18)
    blink_in(k.text("Continue", "CONTINUE?", 900, 780, 72, COL['white'], f0=36, dur=n - 36, style='ExtraBold', align='center'), 36)
    for i, s in enumerate("321"):
        f = 42 + i * 32
        dg = k.text(f"Count {i + 1}", s, 1180, 780, 96, COL['cyan'], f0=f, dur=32, style='ExtraBold', align='center')
        jolt(dg, [(f, 18), (f + 2, -8), (f + 4, 0)])
    blink_in(k.text("Coin", "insert coin to continue", 960, 920, 36, GREY, f0=40, dur=n - 40, style='Medium', align='center'), 40)


# ---------------------------------------------------------------- 8. chromatic logo sting
BOLT = [(1010, 230), (840, 470), (950, 470), (900, 630), (1080, 380), (970, 380)]


def chroma_sting(d):
    n = 90
    k = d.comp("GL Chroma sting", n, "gcl"); lab_bg(k, n)
    # three channel copies of the mark in pure red, green and blue, blended with Screen: where they line up they add to white
    for name, col, ev in (("Mark red", [1, 0, 0, 1], [(0, (-70, 0)), (4, (-36, 10)), (8, (-14, -4)), (12, (0, 0)),
                                                      (50, (-22, 0)), (52, (-8, 0)), (54, (0, 0))]),
                          ("Mark green", [0, 1, 0, 1], [(0, (0, 40)), (4, (10, -22)), (8, (-4, 8)), (12, (0, 0)),
                                                        (50, (0, 6)), (52, (0, 0))]),
                          ("Mark blue", [0, 0, 1, 1], [(0, (70, 0)), (4, (36, -10)), (8, (14, 4)), (12, (0, 0)),
                                                       (50, (22, 0)), (52, (8, 0)), (54, (0, 0))])):
        m = k.path(name, BOLT, f0=0, dur=n, closed=True); m.fill(col); m.mode('Screen')
        bx, by = m.base
        m.pos(held([(f, [bx + dx / 1920, by - dy / 1080]) for f, (dx, dy) in ev]))
        m.scale(held([(0, 1.18), (4, 1.08), (8, 1.03), (12, 1.0)]))
    w = k.text("Wordmark", "NULLBYTE", 960, 790, 110, COL['white'], f0=16, dur=n - 16, style='ExtraBold', align='center', track=1.3)
    rgb_split(w, [(16, 22), (19, 12), (22, 16), (25, 4), (28, 0), (50, 10), (52, 4), (54, 0)])
    blink_in(k.text("Tagline", "signal over noise", 960, 900, 40, COL['green'], f0=30, dur=n - 30, style='SemiBold', align='center',
                    track=1.3), 30)


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    video_title(d); news_ticker(d); hack_alert(d); cyber_sale(d); end_card(d); error_404(d); game_over(d); chroma_sting(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
