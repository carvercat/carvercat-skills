"""Minimal Luxury round 3 in design units: eight lab comps for briefs the pack could not serve before (material swatches, a hotel or
property feature, a collection index, fragrance notes, an invitation or save-the-date, a boutique address card, a limited-edition
number, an editorial spread).

    import minimal_luxury_lab3 as L; doc = L.build(); doc.send(client, PROJECT.carverproj)

Same palette and style rules as minimal_luxury_lab.py (slow, no overshoot, wide tracking, every hold keeps moving). Every move is plain
keys (corporate_luxury_kit.py: slow_in, drift_up) and the three mask windows are scene masks. Check with carvercat_inspect and
carvercat_look (qc reads this style as black and frozen); templates are extracted with regen_pack.py.
Fonts: Rethink Sans must be installed (KI-136). Docs: ai/patterns/minimal-luxury.md (round 3).
Design units: px from the top-left, y down; comp frames, 30 fps. Names, places and numbers are sample copy.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corporate_luxury_kit import (Doc, css, BEZ, text, line, tracking, slow_in, slow_out, drift_up, rule_open, breathe, lgrad, grow)
from minimal_luxury_lab import COL, DECEL, SMOOTH, EXPO, lab_bg

STD = BEZ['std']


def rise_drift(o, f, n, dy=14, d=40, drift=4.32):
    """Up dy px into place (decelerate), then keep drifting up `drift` px (linear) to the clip end."""
    bx, by = o.base
    o.pos([(f, (bx, by + dy), 'Linear'), (f + d, (bx, by), DECEL), (n, (bx, by - drift), 'Linear')])
    o.op([(f, 0.0, 'Linear'), (f + 36, 1.0, STD)])
    return o


def sheen(o, f0, f1, base, light):
    """a soft lighter band that crosses the shape f0 -> f1 (the shape gradient's endpoints are keyed, as v1 did; they start and end off the shape)
    and a slow brightness swell over the hold, so the swatch keeps moving"""
    from corporate_luxury_kit import lgrad, gradient_keys
    lgrad(o, [(0, base), (0.3, base), (0.5, light), (0.7, base), (1, base)], 90)
    gradient_keys(o, [(f0, (-1.0, 0.5), (0.0, 0.5), SMOOTH), (f1, (1.0, 0.5), (2.0, 0.5), 'Linear')])
    o.key('brightness', [(f0, 1.0, 'Linear'), ((f0 + f1) // 2, 1.07, SMOOTH), (f1, 1.0, SMOOTH)])
    return o

# ---------------------------------------------------------------- 1. material swatches
SWATCHES = [("NAPPA LEATHER", "No. 01  ·  COGNAC", '8A4B2A', 'A8653F'),
            ("BRUSHED GOLD", "No. 02  ·  18K", 'B8975A', 'DCC48E'),
            ("SILK TWILL", "No. 03  ·  IVORY", 'D9D0BC', 'F2ECDF')]


def swatch_card(d):
    n = 180
    k = d.comp("ML Swatch card", n, "msw"); lab_bg(k, n)
    t = text(k, "Heading", "THE MATERIALS", 960, 240, 28, COL['gold'], f0=0, dur=n, style='Regular', align='center', track=1.6)
    slow_in(t, 0); breathe(t, 36, n, 1.6, 1.64)
    for i, (name, code, c, hi) in enumerate(SWATCHES):
        x, f = 480 + i * 480, 16 + i * 14          # 480 px apart: the tracked names are about 350 px wide (KI-138)
        s = k.rect(f"Swatch {i + 1}", x, 500, 320, 400, css(c), r=6, f0=f, dur=n - f, center=True)
        rise_drift(s, f, n, dy=16, d=44)
        sheen(s, 70 + i * 10, 150 + i * 10, css(c), css(hi))           # one slow sheen per swatch over the hold
        g = f + 14
        slow_in(text(k, f"Name {i + 1}", name, x, 762, 28, COL['ivory'], f0=g, dur=n - g, style='Regular', align='center', track=1.25), g, s0=0)
        g += 6
        slow_in(text(k, f"Code {i + 1}", code, x, 812, 26, COL['muted'], f0=g, dur=n - g, style='Regular', align='center', track=1.2), g, s0=0)


# ---------------------------------------------------------------- 2. hotel / property feature
def property_feature(d):
    n = 180
    k = d.comp("ML Property feature", n, "mpy"); lab_bg(k, n)
    cx, cy, w, h = 700, 540, 1000, 640
    ph = k.rect("Photo", cx, cy, w, h, COL['deep'], f0=0, dur=n, center=True)          # stand-in for the photo or video
    lgrad(ph, [(0, css('4A4236')), (0.55, css('2A251E')), (1, css('1A1814'))], 0)
    ph.scale([(0, 1.0, 'Linear'), (n, 1.04, 'Linear')])                                  # a slow 4% push inside the window
    win = k.rect("Photo window", cx, cy, w, h, COL['ivory'], f0=0, dur=n, center=True)
    grow(win, 0, 54, SMOOTH)                                                              # opens from the left edge
    k.mask(ph, win)
    x0 = 1300
    slow_in(text(k, "Kicker", "THE RESIDENCE", x0, 380, 26, COL['gold'], f0=30, dur=n - 30, style='Regular', track=1.5), 30, s0=0)
    nm = text(k, "Name", "Villa Serena", x0, 456, 64, COL['ivory'], f0=40, dur=n - 40, style='Regular')
    rise_drift(nm, 40, n, dy=14, d=40, drift=3.24)
    r = line(k, "Rule", [(x0, 530), (x0 + 240, 530)], COL['gold'], 2, f0=0, dur=n)
    r.trim([(56, 0.0, 'Linear'), (96, 1.0, SMOOTH)], which='end')
    for i, s in enumerate(["4 bedrooms", "380 m²", "Sea view, Positano"]):
        f = 70 + i * 12
        slow_in(text(k, f"Detail {i + 1}", s, x0, 590 + i * 52, 30, COL['muted'], f0=f, dur=n - f, style='Regular'), f, s0=0)


# ---------------------------------------------------------------- 3. collection index
LOOKS = ["The Riviera Coat", "Silk Evening Dress", "Cashmere Wrap", "Pearl Choker", "Velvet Loafer"]
ROMAN = ["I", "II", "III", "IV", "V"]


def collection_index(d):
    n = 210
    k = d.comp("ML Collection index", n, "mci"); lab_bg(k, n)
    t = text(k, "Heading", "INDEX", 960, 230, 28, COL['gold'], f0=0, dur=n, style='Regular', align='center', track=1.8)
    slow_in(t, 0); breathe(t, 36, n, 1.8, 1.84)
    rule_open(line(k, "Rule", [(880, 282), (1040, 282)], COL['gold'], 2, f0=0, dur=n), 12)
    pick, dim = 2, 150
    for i, (r, name) in enumerate(zip(ROMAN, LOOKS)):
        y, f = 370 + i * 90, 24 + i * 12
        num = text(k, f"Numeral {i + 1}", r, 790, y, 28, COL['gold'], f0=f, dur=n - f, style='Regular', align='right')
        nm = text(k, f"Look {i + 1}", name, 850, y, 40, COL['ivory'], f0=f + 4, dur=n - f - 4, style='Regular')
        for o, g in ((num, f), (nm, f + 4)):
            bx, by = o.base
            o.pos([(g, (bx, by + 10), 'Linear'), (g + 40, (bx, by), DECEL)])
            if i == pick:
                o.op([(g, 0.0, 'Linear'), (g + 36, 1.0, STD)])
            else:                                                # the rest step back so one look is chosen
                o.op([(g, 0.0, 'Linear'), (g + 36, 1.0, STD), (dim, 1.0, 'Linear'), (dim + 30, 0.4, SMOOTH)])
        if i == pick:
            nm.colour([(dim, COL['ivory'], 'Linear'), (dim + 30, COL['gold'], SMOOTH)])


# ---------------------------------------------------------------- 4. fragrance notes
NOTES = [("TOP", "Bergamot  ·  Pink pepper", 160), ("HEART", "Iris  ·  Jasmine sambac", 280), ("BASE", "Sandalwood  ·  Amber", 400)]


def fragrance_notes(d):
    n = 180
    k = d.comp("ML Fragrance notes", n, "mfn"); lab_bg(k, n)
    for i, (label, notes, rw) in enumerate(NOTES):
        y, f = 290 + i * 180, 10 + i * 28
        lb = text(k, f"Tier {i + 1}", label, 960, y, 26, COL['gold'], f0=f, dur=n - f, style='Regular', align='center', track=1.6)
        slow_in(lb, f, s0=0); breathe(lb, f + 36, n, 1.6, 1.64)
        g = f + 8
        rise_drift(text(k, f"Notes {i + 1}", notes, 960, y + 56, 40, COL['ivory'], f0=g, dur=n - g, style='Regular', align='center'),
                   g, n, dy=12, d=40, drift=3.24)
        rule_open(line(k, f"Rule {i + 1}", [(960 - rw / 2, y + 116), (960 + rw / 2, y + 116)], COL['gold'], 2, f0=0, dur=n), g + 10, 40)
    f = 100
    slow_in(text(k, "Product", "No. 7  ·  EAU DE PARFUM", 960, 880, 26, COL['muted'], f0=f, dur=n - f, style='Regular', align='center',
                   track=1.4), f, s0=0)


# ---------------------------------------------------------------- 5. invitation / save the date
def invitation(d):
    n = 180
    k = d.comp("ML Invitation", n, "miv"); lab_bg(k, n)
    for i, (w, h, px, f) in enumerate([(960, 680, 2, 0), (920, 640, 1, 10)]):
        fr = k.rect(f"Frame {i + 1}", 960, 540, w, h, None, f0=0, dur=n, center=True); fr.stroke(COL['gold'], px)
        fr.trim([(f, 0.0, 'Linear'), (f + 56, 1.0, SMOOTH)], which='end')
    kk = text(k, "Kicker", "SAVE THE DATE", 960, 320, 26, COL['gold'], f0=24, dur=n - 24, style='Regular', align='center', track=1.6)
    slow_in(kk, 24, s0=0); breathe(kk, 60, n, 1.6, 1.64)
    slow_in(text(k, "Names", "Amelia & James", 960, 430, 80, COL['ivory'], f0=36, dur=n - 36, style='Regular', align='center'), 36)
    rule_open(line(k, "Rule", [(900, 515), (1020, 515)], COL['gold'], 2, f0=0, dur=n), 56)
    dt = text(k, "Date", "12 · 06 · 2027", 960, 590, 40, COL['ivory'], f0=60, dur=n - 60, style='Regular', align='center', track=1.4)
    slow_in(dt, 60, s0=0); breathe(dt, 96, n, 1.4, 1.44)
    slow_in(text(k, "Venue", "VILLA BALBIANO  ·  LAKE COMO", 960, 670, 26, COL['muted'], f0=72, dur=n - 72, style='Regular', align='center',
                   track=1.25), 72, s0=0)                       # 842 px wide at 1.4: too close to the frame
    slow_in(text(k, "Note", "Formal invitation to follow", 960, 750, 26, COL['muted'], f0=84, dur=n - 84, style='Regular', align='center'),
            84, s0=0)


# ---------------------------------------------------------------- 6. boutique address card
def boutique_address(d):
    n = 180
    k = d.comp("ML Boutique address", n, "mba"); lab_bg(k, n)
    ring = k.ell("Pin ring", 960, 250, 44, 44, None, f0=0, dur=n); ring.stroke(COL['gold'], 2)
    ring.rotv(-90.0); ring.trim([(0, 0.0, 'Linear'), (40, 1.0, SMOOTH)])
    slow_in(k.ell("Pin dot", 960, 250, 10, 10, COL['gold'], f0=20, dur=n - 20), 20, s0=0)
    kk = text(k, "Kicker", "NOW OPEN", 960, 330, 26, COL['gold'], f0=24, dur=n - 24, style='Regular', align='center', track=1.6)
    slow_in(kk, 24, s0=0)
    nm = text(k, "Boutique", "MAISON ELAN", 960, 420, 64, COL['ivory'], f0=34, dur=n - 34, style='Regular', align='center', track=1.5)
    slow_in(nm, 34); breathe(nm, 70, n, 1.5, 1.54)
    rule_open(line(k, "Rule", [(900, 490), (1020, 490)], COL['gold'], 2, f0=0, dur=n), 52)
    ad = text(k, "Address", "14 Rue du Faubourg Saint-Honoré\n75008 Paris", 960, 580, 34, COL['ivory'], f0=62, dur=n - 62, style='Regular',
                align='center', lh=1.45)
    rise_drift(ad, 62, n, dy=12, d=40, drift=3.24)
    slow_in(text(k, "Hours", "MON – SAT  ·  10:00 – 19:00", 960, 700, 26, COL['muted'], f0=80, dur=n - 80, style='Regular', align='center',
                   track=1.3), 80, s0=0)


# ---------------------------------------------------------------- 7. limited edition number
def limited_edition(d):
    n = 150
    k = d.comp("ML Limited edition", n, "mle"); lab_bg(k, n)
    kk = text(k, "Kicker", "LIMITED EDITION", 960, 330, 26, COL['gold'], f0=0, dur=n, style='Regular', align='center', track=1.6)
    slow_in(kk, 0, s0=0); breathe(kk, 36, n, 1.6, 1.64)
    win = k.rect("Number window", 960, 540, 900, 280, COL['ivory'], f0=0, dur=n, center=True)
    num = text(k, "Number", "027", 960, 540, 220, COL['ivory'], f0=12, dur=n - 12, style='Regular', align='center', track=1.1)
    bx, by = num.base
    num.pos([(12, (bx, by + 240), 'Linear'), (66, (bx, by), DECEL)])           # rises out of the window's lower edge
    num.op([(12, 0.0, 'Linear'), (40, 1.0, STD)])
    breathe(num, 66, n, 1.1, 1.14)
    k.mask(num, win)
    rule_open(line(k, "Rule", [(880, 700), (1040, 700)], COL['gold'], 2, f0=0, dur=n), 60)
    slow_in(text(k, "Of", "OF 150", 960, 760, 28, COL['muted'], f0=70, dur=n - 70, style='Regular', align='center', track=1.5), 70, s0=0)


# ---------------------------------------------------------------- 8. editorial spread
def editorial_spread(d):
    n = 180
    k = d.comp("ML Editorial spread", n, "mes"); lab_bg(k, n)
    cx, cy, w, h = 520, 540, 760, 840
    ph = k.rect("Photo", cx, cy, w, h, COL['deep'], f0=0, dur=n, center=True)            # stand-in for the photo
    lgrad(ph, [(0, css('4A4236')), (1, css('1F1B16'))], 45)
    ph.scale([(0, 1.0, 'Linear'), (n, 1.03, 'Linear')])
    fe = 100                                                                              # Fill soft edge: the feather
    win = k.rect("Photo window", cx, cy, w + 2 * fe, h + 2 * fe, COL['ivory'], f0=0, dur=n, center=True)   # a feather wider than the photo, so its edges are crisp at rest
    win.set('softEdge', fe)
    bx, by = win.base
    win.pos([(0, (bx, by - (h + 2 * fe + 20)), 'Linear'), (60, (bx, by), SMOOTH)])   # comes down from above
    k.mask(ph, win)
    g = line(k, "Gutter", [(960, 160), (960, 920)], css('3A352C'), 2, f0=0, dur=n)
    g.trim([(10, 0.0, 'Linear'), (60, 1.0, SMOOTH)], which='end')
    x0 = 1060
    slow_in(text(k, "Kicker", "ISSUE 04  ·  AUTUMN", x0, 290, 26, COL['gold'], f0=30, dur=n - 30, style='Regular', track=1.5), 30, s0=0)
    hd = text(k, "Headline", "The Art of\nSlow Living", x0, 420, 80, COL['ivory'], f0=40, dur=n - 40, style='Regular', lh=1.15)
    rise_drift(hd, 40, n, dy=14, d=44, drift=3.24)
    rule_open(line(k, "Rule", [(x0, 552), (x0 + 160, 552)], COL['gold'], 2, f0=0, dur=n), 64)
    slow_in(text(k, "Standfirst", "A season of cashmere, quiet rooms\nand long afternoons by the lake.", x0, 640, 30, COL['muted'], f0=66,
                   dur=n - 66, style='Regular', lh=1.5), 66, s0=0)
    slow_in(text(k, "Folio", "14", 1720, 930, 26, COL['muted'], f0=90, dur=n - 90, style='Regular', align='right'), 90, s0=0)


def build():
    d = Doc()
    swatch_card(d); property_feature(d); collection_index(d); fragrance_notes(d); invitation(d); boutique_address(d)
    limited_edition(d); editorial_spread(d)
    return d


if __name__ == "__main__":
    print(__doc__)
