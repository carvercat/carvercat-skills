"""Minimal Luxury round 2 in design units: eight lab comps (lower third, monogram end card, price card, collection title, light sweep,
attribute row, framed word, slow dip).

    import minimal_luxury_lab2 as L; doc = L.build(); doc.send(client, PROJECT.carverproj)

Same palette and style rules (slow, no overshoot, wide tracking, every hold keeps moving) as minimal_luxury_lab.py. The pack's moves
are plain keys (corporate_luxury_kit.py) and the one mask is a scene mask, so nothing is applied after `send`. Check with
carvercat_inspect and carvercat_look; templates are extracted with regen_pack.py. Docs: ai/patterns/minimal-luxury.md.
Design units: px from the top-left, y down; comp frames, 30 fps.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corporate_luxury_kit import EASE_OUT
from corporate_luxury_kit import (Doc, css, BEZ, text, line, tracking, slow_in, slow_out, drift_up, rule_open, breathe, gradient_keys)
from minimal_luxury_lab import COL, DECEL, SMOOTH, EXPO, lab_bg


def lower_third(d):
    n = 180
    k = d.comp("ML Lower third", n, "mlt"); lab_bg(k, n)
    r = line(k, "Rule", [(160, 860), (520, 860)], COL['gold'], 2, f0=0, dur=n)
    r.trim([(0, 0.0, 'Linear'), (40, 1.0, SMOOTH), (n - 40, 1.0, 'Linear'), (n - 10, 0.0, SMOOTH)], which='end')
    nm = text(k, "Name", "ISABELLE MOREAU", 160, 810, 40, COL['ivory'], f0=10, dur=n - 10, style='Regular', track=1.5)
    breathe(nm, 10, n, 1.5, 1.56); slow_in(nm, 10); slow_out(nm, n)
    rl = text(k, "Role", "CREATIVE DIRECTOR", 160, 910, 26, COL['muted'], f0=22, dur=n - 22, style='Regular', track=1.5)
    slow_in(rl, 22); slow_out(rl, n)


def monogram_end(d):
    n = 150
    k = d.comp("ML Monogram end", n, "mme"); lab_bg(k, n)
    ring = k.ell("Monogram ring", 960, 430, 220, 220, None, f0=0, dur=n); ring.stroke(COL['gold'], 2)
    ring.rotv(-90.0); ring.trim([(0, 0.0, 'Linear'), (50, 1.0, SMOOTH)])      # an ellipse path starts at 3 o'clock: turn it to 12
    mg = text(k, "Monogram", "ME", 960, 430, 72, COL['ivory'], f0=24, dur=n - 24, style='Regular', align='center', track=1.2)
    slow_in(mg, 24); drift_up(mg, 24, 119)
    wm = text(k, "Wordmark", "MAISON ELAN", 960, 640, 48, COL['ivory'], f0=44, dur=n - 44, style='Regular', align='center', track=1.8)
    breathe(wm, 44, n, 1.8, 1.86); slow_in(wm, 44)
    slow_in(text(k, "Address", "maisonelan.com", 960, 720, 26, COL['muted'], f0=64, dur=n - 64, style='Regular', align='center', track=1.4), 64)


def price_card(d):
    n = 150
    k = d.comp("ML Price card", n, "mpc"); lab_bg(k, n)
    pn = text(k, "Product name", "LE SAC No. 3", 900, 440, 56, COL['ivory'], f0=0, dur=n, style='Regular', track=1.5)
    slow_in(pn, 0); drift_up(pn, 0, 120)
    rule_open(line(k, "Price rule", [(900, 510), (1220, 510)], COL['gold'], 2, f0=0, dur=n), 16)
    slow_in(text(k, "Material", "Calfskin, hand-stitched", 900, 570, 30, COL['muted'], f0=30, dur=n - 30, style='Regular', track=1.2), 30)
    slow_in(text(k, "Price", "€ 2 400", 900, 650, 40, COL['gold'], f0=48, dur=n - 48, style='Regular', track=1.3), 48)


def collection_title(d):
    n = 150
    k = d.comp("ML Collection title", n, "mct"); lab_bg(k, n)
    t = text(k, "Collection", "AUTUMN  WINTER\n2026", 960, 520, 72, COL['ivory'], f0=0, dur=n, style='Regular', align='center',
             track=1.6, lh=1.35)
    # each line rises 0.8 % and clears a 13.8 px blur, 18 f after the one before (own keys: a stagger takes all of them as its tween)
    bx, by = t.base
    t.pos([(0, (bx, by + 8.64), 'expo'), (40, (bx, by), 'Linear')])
    t.blur([(0, 13.8, 'expo'), (40, 0, 'Linear')])
    t.op([(0, 0, 'Linear'), (20, 1, EASE_OUT)])
    tracking(t, [(58, 1.6, 'Linear'), (150, 1.66, 'Linear')])     # the v1 template drifts the tracking 1.6 -> 1.66 over the hold
    t.stagger(by='lines', each=18)
    slow_in(text(k, "Season note", "THE COLLECTION", 960, 760, 26, COL['gold'], f0=60, dur=n - 60, style='Regular', align='center', track=1.6), 60)


def light_sweep(d):
    """A gleam across gold letters with ONE text object: the text is the mask of a gold rectangle (1000 x 320, still, as v1 drew it)
    whose gradient (gold, ivory band, gold) is static in its colours and whose endpoints are keyed (f30-110, shape gradient endpoints
    are live; the rectangle never moves). A second text copy would trip lint text_overlap (KI-133)."""
    n = 120
    k = d.comp("ML Light sweep", n, "mls"); lab_bg(k, n)
    fill = k.rect("Gold fill", 960, 540, 1000, 320, COL["gold"], f0=0, dur=n, center=True)
    g, iv = COL['gold'], COL['ivory']
    fill.set('fill', 'linear-gradient(90deg, %s 0%%, %s 38%%, %s 50%%, %s 62%%, %s 100%%)' % (g, g, iv, g, g))
    gradient_keys(fill, [(30, (-0.6, 0.5), (0.4, 0.5), SMOOTH), (110, (0.6, 0.5), (1.6, 0.5), 'Linear')])
    slow_in(fill, 0)
    wm = text(k, "Wordmark", "ELAN", 960, 540, 220, COL['ivory'], f0=0, dur=n, style='Regular', align='center', track=1.4)
    k.mask(fill, wm)                # the text is the mask, the gold fill its target


def attribute_row(d):
    n = 150
    k = d.comp("ML Attribute row", n, "mar"); lab_bg(k, n)
    attrs = ["HANDMADE", "FLORENCE", "18K GOLD"]
    for i, a in enumerate(attrs):
        # 520 px apart at 28 px: tracked caps are wide (about 0.14 x size extra per character per +0.1 tracking);
        # the first build (400 px apart, 34 px) ran the words into each other, which lint did not flag
        x, f = 440 + i * 520, 10 + i * 18
        t = text(k, f"Attribute {i + 1}", a, x, 540, 28, COL['ivory'], f0=f, dur=n - f, style='Regular', align='center', track=1.6)
        breathe(t, f, n, 1.6, 1.64); slow_in(t, f)
        if i:
            slow_in(k.ell(f"Separator {i}", x - 260, 540, 8, 8, COL['gold'], f0=f - 6, dur=n - f + 6), f - 6)


def framed_word(d):
    n = 150
    k = d.comp("ML Framed word", n, "mfr"); lab_bg(k, n)
    for i, (x, dx) in enumerate([(700, -14), (1220, 14)]):
        ln = line(k, f"Frame line {i + 1}", [(x, 420), (x, 660)], COL['gold'], 2, f0=0, dur=n)
        rule_open(ln, 0 + i * 6, 44)
        bx, by = ln.base
        ln.pos([(50, (bx, by), 'Linear'), (n, (bx + dx, by), 'Linear')])   # the frame breathes open over the hold
    slow_in(text(k, "Word", "ATELIER", 960, 540, 80, COL['ivory'], f0=24, dur=n - 24, style='Regular', align='center', track=1.6), 24)


def slow_dip(d):
    n = 60
    k = d.comp("ML Slow dip", n, "mdp")
    o = k.rect("Dip", 0, 0, 1920, 1080, COL['bg'], f0=0, dur=n)
    o.op([(0, 0.0, 'Linear'), (26, 1.0, SMOOTH), (34, 1.0, 'Linear'), (n, 0.0, SMOOTH)])


def build():
    d = Doc()
    lower_third(d); monogram_end(d); price_card(d); collection_title(d); light_sweep(d); attribute_row(d); framed_word(d); slow_dip(d)
    return d


if __name__ == "__main__":
    print(__doc__)
