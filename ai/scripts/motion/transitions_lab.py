"""Write the Transitions lab comps in design units (cc2.py: px, y down, degrees, CSS colours and easing).

    import transitions_lab as L; doc = L.build(); doc.send(client, PROJECT.carverproj)   # scene.apply per comp, then edit.save

Two kinds:
- COVER transitions (templates): shapes cover the whole frame around frame CUT; put the
  instance on the top track so its CUT frame lands on your edit point. The lab comps have
  stand-in "Scene A" / "Scene B" rectangles, which the templates drop.
- REVEAL transitions (recipes): scene B is revealed through a mask or moved over scene A;
  they need your two scenes, so they are documented as steps with a verified lab comp.

Masks are scene masks (a `mask` style key on the content that points at the window), so nothing is run after `send`.
Check with carvercat_inspect (curves, lint, qc for flashes) and carvercat_look; extract
templates with comp_to_template.py --drop "Scene A" --drop "Scene B".
Docs: ai/patterns/transitions.md. Design units: px from the top-left, y down; comp frames, 30 fps.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author"))
from cc2 import Doc, css, BEZ, HOLD

COL = dict(a=css('2B3A67'), a2=css('496A81'), b=css('E8D6B3'), b2=css('D98E73'), accent=css('5B5BF6'), ink=css('14151C'),
           coral=css('FF6B5B'), white=css('FFFFFF'))
EXPO, ACCEL, SMOOTH = BEZ['expo'], BEZ['accel'], BEZ['smooth']
IN_EASE = (0.7, 0.0, 0.84, 0.0)       # strong ease-in: cover pieces accelerate INTO the cut
OUT_EASE = (0.16, 1.0, 0.3, 1.0)      # expo-out: they leave fast from the cut and settle
CUT = 18
W, H = 1920, 1080
TL = ((0, 0), (W, H))                 # gradient line, top-left to bottom-right, in px


def scenes(k, n, cut=CUT):
    a = k.rect("Scene A", W / 2, H / 2, W, H, COL['a'], f0=0, dur=cut, center=True)
    a.gradient([(0.0, COL['a']), (1.0, COL['a2'])], *TL)
    b = k.rect("Scene B", W / 2, H / 2, W, H, COL['b'], f0=cut, dur=n - cut, center=True)
    b.gradient([(0.0, COL['b']), (1.0, COL['b2'])], *TL)
    return a, b


def slide_wipe(d):
    n = 36
    k = d.comp("TX Slide wipe", n, "tsw"); scenes(k, n)
    p = k.rect("Panel", W / 2, H / 2, W, H, COL['accent'], f0=0, dur=n, center=True)
    bx, by = p.base
    p.pos([(0, (bx - W, by), 'Linear'), (CUT - 2, (bx, by), IN_EASE), (CUT + 2, (bx, by), 'Linear'), (n, (bx + W, by), OUT_EASE)])


def diagonal_wipe(d):
    n = 36
    k = d.comp("TX Diagonal wipe", n, "tdw"); scenes(k, n)
    # shapes are cropped to a comp-sized box before their scale (KI-137): draw 1000 px, scale 2.6x.
    # A 2600 px square turned 30 deg covers the frame (inscribed radius 1300 > half-diagonal 1101) and is
    # 3552 px wide, so it starts and ends 1.5 W off-centre to be fully off screen.
    p = k.rect("Band", W / 2, H / 2, 1000, 1000, COL['ink'], f0=0, dur=n, center=True)
    p.rotv(-30.0); p.sc(2.6)          # the old kit stored +30 counter-clockwise; design degrees run clockwise
    bx, by = p.base
    off = 1.5 * W
    p.pos([(0, (bx - off, by), 'Linear'), (CUT - 1, (bx, by), IN_EASE), (CUT + 1, (bx, by), 'Linear'), (n, (bx + off, by), OUT_EASE)])


def split_doors(d):
    n = 36
    k = d.comp("TX Split doors", n, "tsd"); scenes(k, n)
    for name, y0, sgn in (("Door top", 270, -1), ("Door bottom", 810, 1)):
        p = k.rect(name, W / 2, y0, W, 548, COL['ink'], f0=0, dur=n, center=True)   # 8 px overlap: no seam at the cut
        bx, by = p.base
        dy = 560
        # the old doors moved sgn*dy in y-up fractions: the top door starts above the frame, the bottom one below
        p.pos([(0, (bx, by + sgn * dy), 'Linear'), (CUT - 1, (bx, by), IN_EASE), (CUT + 2, (bx, by), 'Linear'), (n, (bx, by + sgn * dy), OUT_EASE)])


def bars_stagger(d):
    n = 40
    k = d.comp("TX Bars stagger", n, "tbs"); scenes(k, n, 20)
    cols = 6; w = W / cols
    for i in range(cols):
        p = k.rect(f"Bar {i + 1}", w * i + w / 2, H / 2, w + 2, H, (COL['accent'], COL['coral'])[i % 2], f0=0, dur=n, center=True)
        bx, by = p.base; f = i * 2
        # in from above the frame, out downward
        p.pos([(f, (bx, by - H), 'Linear'), (f + 10, (bx, by), EXPO), (f + 22, (bx, by), 'Linear'), (f + 30, (bx, by + H), ACCEL)])


def clock_wipe(d):
    n = 40
    k = d.comp("TX Clock wipe", n, "tcw"); scenes(k, n, 20)
    # a stroke as wide as the diameter fills the disc; stroke width tops out at 0.2 W (384 px) and shapes are
    # cropped to a comp-sized box before scale (KI-137), so draw 380 px and scale 2.95x (outer radius 1121 px)
    c = k.ell("Clock", W / 2, H / 2, 380, 380, None, f0=0, dur=n); c.stroke(COL['ink'], 380, cap='butt'); c.sc(2.95)
    c.rot([(0, -90.0, 'Linear'), (n, -96.0, 'Linear')])             # starts at 12 o'clock; the slow drift keeps it from ever being 'still' (lint: cropped_at_rest)
    c.trim([(0, 100, 'Linear'), (19, 0, IN_EASE)], which='start')   # sweeps clockwise from 12 o'clock to full
    c.key('trimEnd', [(21, '100%', 'Linear'), (n, '0%', OUT_EASE)])  # then clears in the same direction


def bubble_cover(d):
    n = 40
    k = d.comp("TX Bubble cover", n, "tbc"); scenes(k, n, 20)
    spots = [(420, 300, COL['coral']), (1500, 780, COL['accent']), (960, 540, COL['ink'])]
    for i, (x, y, col) in enumerate(spots):
        b = k.ell(f"Bubble {i + 1}", x, y, 1000, 1000, col, f0=0, dur=n)          # 1000 px, scaled to 2.4x (KI-137)
        f = i * 3
        # never still while oversized: each bubble keeps growing slowly until it leaves (lint: cropped_at_rest)
        b.scale([(f, 0.0, 'Linear'), (f + 14, 2.4, IN_EASE), (24, 2.47, 'Linear'), (36, 0.0, ACCEL)]) if i == 2 else \
            b.scale([(f, 0.0, 'Linear'), (f + 14, 2.4, IN_EASE), (21 + i, 2.47, 'Linear'), (21 + i + 1, 0.0, 'Hold')])


def dip_to_colour(d):
    n = 30
    k = d.comp("TX Dip to colour", n, "tdc"); scenes(k, n, 15)
    p = k.rect("Dip", W / 2, H / 2, W, H, COL['ink'], f0=0, dur=n, center=True)
    p.op([(0, 0.0, 'Linear'), (13, 1.0, 'S-curve'), (17, 1.0, 'Linear'), (n, 0.0, 'S-curve')])


# ---------------------------------------------------------------- reveal recipes (need your scenes)
def shape_reveal(d):
    n = 36
    k = d.comp("TX Shape reveal", n, "tsr")
    a = k.rect("Scene A", W / 2, H / 2, W, H, COL['a'], f0=0, dur=n, center=True)
    a.gradient([(0.0, COL['a']), (1.0, COL['a2'])], *TL)
    b = k.rect("Scene B", W / 2, H / 2, W, H, COL['b'], f0=4, dur=n - 4, center=True)
    b.gradient([(0.0, COL['b']), (1.0, COL['b2'])], *TL)
    s = k.star("Star window", W / 2, H / 2, 1000, 5, 0.5, COL["white"], f0=4, dur=n - 4)   # 1000 px x 5 = inner radius 1250 px > half-diagonal 1101 (KI-137)
    s.scale([(4, 0.0, 'Linear'), (28, 5.0, IN_EASE), (n, 5.3, 'Linear')])   # keeps growing: an oversized window is never 'still'
    s.rot([(4, 40.0, 'Linear'), (28, 0.0, EXPO)])
    k.mask(b, s)


def line_sweep(d):
    n = 36
    k = d.comp("TX Line sweep", n, "tls")
    a = k.rect("Scene A", W / 2, H / 2, W, H, COL['a'], f0=0, dur=n, center=True)
    a.gradient([(0.0, COL['a']), (1.0, COL['a2'])], *TL)
    b = k.rect("Scene B", W / 2, H / 2, W, H, COL['b'], f0=0, dur=n, center=True)
    b.gradient([(0.0, COL['b']), (1.0, COL['b2'])], *TL)
    w = k.rect("Sweep window", W / 2, H / 2, W, H, COL['white'], f0=0, dur=n, center=True)
    wx, wy = w.base
    w.pos([(4, (wx - W, wy), 'Linear'), (28, (wx, wy), SMOOTH)])                # the window's right edge is the line
    k.mask(b, w)
    ln = k.rect("Sweep line", 0, H / 2, 8, H, COL['white'], f0=4, dur=24, center=True)
    ln.glow(size=12, amount=0.6)
    lx, ly = ln.base
    ln.pos([(4, (lx, ly), 'Linear'), (28, (lx + W, ly), SMOOTH)])


def whip_pan(d):
    n = 30
    k = d.comp("TX Whip pan", n, "twp")
    for name, col, f0, f1, ease in (("Scene A", COL['a'], 0, 15, ACCEL), ("Scene B", COL['b'], 15, 30, EXPO)):
        s = k.rect(name, W / 2, H / 2, W, H, col, f0=f0, dur=f1 - f0, center=True)
        s.gradient([(0.0, col), (1.0, COL['a2'] if name == "Scene A" else COL['b2'])], *TL)
        bx, by = s.base
        if name == "Scene A":
            s.pos([(0, (bx, by), 'Linear'), (8, (bx, by), 'Linear'), (15, (bx - W, by), ease)])
            s.scale([(8, [1.0, 1.0], 'Linear'), (15, [1.4, 1.0], ACCEL)])
        else:
            s.pos([(15, (bx + W, by), 'Linear'), (22, (bx, by), ease)])
            s.scale([(15, [1.4, 1.0], 'Linear'), (22, [1.0, 1.0], EXPO)])
        s.mblur(360)


def zoom_blur_punch(d):
    n = 30
    k = d.comp("TX Zoom blur punch", n, "tzb")
    a = k.rect("Scene A", W / 2, H / 2, W, H, COL['a'], f0=0, dur=15, center=True)
    a.gradient([(0.0, COL['a']), (1.0, COL['a2'])], *TL)
    a.scale([(4, 1.0, 'Linear'), (15, 2.6, ACCEL)])
    a.blur([(4, 0.0, 'Linear'), (15, 40.0, ACCEL)])
    b = k.rect("Scene B", W / 2, H / 2, W, H, COL['b'], f0=15, dur=15, center=True)
    b.gradient([(0.0, COL['b']), (1.0, COL['b2'])], *TL)
    b.scale([(15, 1.5, 'Linear'), (27, 1.0, EXPO)])
    b.blur([(15, 40.0, 'Linear'), (25, 0.0, EXPO)])


def build(path=None, m=None):
    d = Doc()
    slide_wipe(d); diagonal_wipe(d); split_doors(d); bars_stagger(d); clock_wipe(d); bubble_cover(d); dip_to_colour(d)
    shape_reveal(d); line_sweep(d); whip_pan(d); zoom_blur_punch(d)
    return d


if __name__ == "__main__":
    print(__doc__)
