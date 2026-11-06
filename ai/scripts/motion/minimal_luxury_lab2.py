"""Minimal Luxury round 2: eight more lab comps (lower third, monogram end card, price card,
collection title, light sweep, attribute row, framed word, slow dip), written straight into a
.carverproj.

    import minimal_luxury_lab2 as L; presets, masks = L.build(PROJECT.carverproj)

Same palette, style rules (slow, no overshoot, wide tracking, every hold keeps moving) and
verification as minimal_luxury_lab.py. After writing: edit.open {path, force:true}; apply
PRESETS (preset.apply); for each MASKS entry run mask.make {ids:[mask, target]} - the FIRST
id is the mask - then parent.clear; edit.save. Check with carvercat_inspect and
carvercat_look; extract templates with comp_to_template.py (--drop "Lab bg").
Docs: ai/patterns/minimal-luxury.md. Pixel space 1920x1080, y down; comp frames, 30 fps.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from minimal_luxury_lab import Doc, lin, COL, DECEL, SMOOTH, EXPO, lab_bg

PRESETS, MASKS = [], []


def rule_open(o, f, d=40):
    """a thin line that opens from its centre"""
    tp = o.trim([(f, 0.5, 'Linear'), (f + d, 0.0, SMOOTH)], which='start')
    o.key(tp + '.end', [(f, 0.5, 'Linear'), (f + d, 1.0, SMOOTH)])


def breathe(o, f, n, a=1.4, b=1.45):
    o.key(o.src('text_font', 'tracking'), [(f, a, 'Linear'), (n, b, 'Linear')])


def lower_third(d):
    n = 180
    k = d.comp("ML Lower third", n, "mlt"); lab_bg(k, n)
    r = k.line("Rule", [(160, 860), (520, 860)], COL['gold'], px=2, f0=0, dur=n)
    tp = r.trim([(0, 0.0, 'Linear'), (40, 1.0, SMOOTH), (n - 40, 1.0, 'Linear'), (n - 10, 0.0, SMOOTH)], which='end')
    nm = k.text("Name", "ISABELLE MOREAU", 160, 810, 40, COL['ivory'], f0=10, dur=n - 10, style='Regular', track=1.5)
    breathe(nm, 10, n, 1.5, 1.56)
    PRESETS.extend([("ML Lower third", "Name", "Slow fade in"), ("ML Lower third", "Name", "Slow fade out")])
    rl = k.text("Role", "CREATIVE DIRECTOR", 160, 910, 26, COL['muted'], f0=22, dur=n - 22, style='Regular', track=1.5)
    PRESETS.extend([("ML Lower third", "Role", "Slow fade in"), ("ML Lower third", "Role", "Slow fade out")])


def monogram_end(d):
    n = 150
    k = d.comp("ML Monogram end card", n, "mme"); lab_bg(k, n)
    ring = k.ell("Monogram ring", 960, 430, 220, 220, None, f0=0, dur=n); ring.stroke(COL['gold'], 2)
    ring.rotv(90.0); ring.trim([(0, 0.0, 'Linear'), (50, 1.0, SMOOTH)])
    k.text("Monogram", "ME", 960, 430, 72, COL['ivory'], f0=24, dur=n - 24, style='Regular', align='center', track=1.2)
    PRESETS.extend([("ML Monogram end card", "Monogram", "Slow fade in"), ("ML Monogram end card", "Monogram", "Drift up - 4 s")])
    wm = k.text("Wordmark", "MAISON ELAN", 960, 640, 48, COL['ivory'], f0=44, dur=n - 44, style='Regular', align='center', track=1.8)
    breathe(wm, 44, n, 1.8, 1.86)
    PRESETS.append(("ML Monogram end card", "Wordmark", "Slow fade in"))
    k.text("Address", "maisonelan.com", 960, 720, 26, COL['muted'], f0=64, dur=n - 64, style='Regular', align='center', track=1.4)
    PRESETS.append(("ML Monogram end card", "Address", "Slow fade in"))


def price_card(d):
    n = 150
    k = d.comp("ML Price card", n, "mpc"); lab_bg(k, n)
    k.text("Product name", "LE SAC No. 3", 900, 440, 56, COL['ivory'], f0=0, dur=n, style='Regular', track=1.5)
    PRESETS.extend([("ML Price card", "Product name", "Slow fade in"), ("ML Price card", "Product name", "Drift up - 4 s")])
    rule_open(k.line("Price rule", [(900, 510), (1220, 510)], COL['gold'], px=2, f0=0, dur=n), 16)
    k.text("Material", "Calfskin, hand-stitched", 900, 570, 30, COL['muted'], f0=30, dur=n - 30, style='Regular', track=1.2)
    PRESETS.append(("ML Price card", "Material", "Slow fade in"))
    k.text("Price", "€ 2 400", 900, 650, 40, COL['gold'], f0=48, dur=n - 48, style='Regular', track=1.3)
    PRESETS.append(("ML Price card", "Price", "Slow fade in"))


def collection_title(d):
    n = 150
    k = d.comp("ML Collection title", n, "mct"); lab_bg(k, n)
    t = k.text("Collection", "AUTUMN  WINTER\n2026", 960, 520, 72, COL['ivory'], f0=0, dur=n, style='Regular', align='center',
               track=1.6, lh=1.35)
    t.stagger(0, by='line', gap=18, dy=0.008, d=40, blur=12)
    breathe(t, 58, n, 1.6, 1.66)
    k.text("Season note", "THE COLLECTION", 960, 760, 26, COL['gold'], f0=60, dur=n - 60, style='Regular', align='center', track=1.6)
    PRESETS.append(("ML Collection title", "Season note", "Slow fade in"))


def light_sweep(d):
    """A gleam across gold letters with ONE text object: the text is the mask of a gold rectangle whose
    gradient (gold - ivory band - gold) has keyed endpoints. Text gradient endpoints are not live (KI-009c),
    shape gradient endpoints are; and a second text copy would trip lint text_overlap (KI-133)."""
    n = 120
    k = d.comp("ML Light sweep", n, "mls"); lab_bg(k, n)
    fill = k.rect("Gold fill", 960, 540, 1000, 320, COL['gold'], f0=0, dur=n, center=True)
    g, iv = COL['gold'], COL['ivory']
    fill.set(fill.src('shape_fill', 'paint'), 'gradient')
    fill.set(fill.src('shape_fill', 'gradient'), {'mode': 'linear', 'start': [0, 0.5], 'end': [1, 0.5], 'stops': [
        {'p': p, 'color': c[:3], 'a': 1} for p, c in [(0, g), (0.38, g), (0.5, iv), (0.62, g), (1, g)]]})
    # band centre = start + 0.5: from -0.1 to 1.1 of the fill's width, slowly (f30-110)
    fill.key(fill.src('shape_fill', 'gradientStart'), [(30, [-0.6, 0.5], 'Linear'), (110, [0.6, 0.5], SMOOTH)])
    fill.key(fill.src('shape_fill', 'gradientEnd'), [(30, [0.4, 0.5], 'Linear'), (110, [1.6, 0.5], SMOOTH)])
    PRESETS.append(("ML Light sweep", "Gold fill", "Slow fade in"))
    k.text("Wordmark", "ELAN", 960, 540, 220, COL['ivory'], f0=0, dur=n, style='Regular', align='center', track=1.4)
    MASKS.append(("ML Light sweep", "Gold fill", "Wordmark"))                # the text is the mask, the gold fill its target


def attribute_row(d):
    n = 150
    k = d.comp("ML Attribute row", n, "mar"); lab_bg(k, n)
    attrs = ["HANDMADE", "FLORENCE", "18K GOLD"]
    for i, a in enumerate(attrs):
        # 520 px apart at 28 px: tracked caps are wide (about 0.14 x size extra per character per +0.1 tracking);
        # the first build (400 px apart, 34 px) ran the words into each other, which lint did not flag
        x, f = 440 + i * 520, 10 + i * 18
        t = k.text(f"Attribute {i + 1}", a, x, 540, 28, COL['ivory'], f0=f, dur=n - f, style='Regular', align='center', track=1.6)
        breathe(t, f, n, 1.6, 1.64)
        PRESETS.append(("ML Attribute row", f"Attribute {i + 1}", "Slow fade in"))
        if i:
            sep = k.ell(f"Separator {i}", x - 260, 540, 8, 8, COL['gold'], f0=f - 6, dur=n - f + 6)
            PRESETS.append(("ML Attribute row", f"Separator {i}", "Slow fade in"))


def framed_word(d):
    n = 150
    k = d.comp("ML Framed word", n, "mfr"); lab_bg(k, n)
    for i, (x, dx) in enumerate([(700, -14), (1220, 14)]):
        ln = k.line(f"Frame line {i + 1}", [(x, 420), (x, 660)], COL['gold'], px=2, f0=0, dur=n)
        rule_open(ln, 0 + i * 6, 44)
        bx, by = ln.base
        ln.pos([(50, [bx, by], 'Linear'), (n, [bx + dx / 1920, by], 'Linear')])   # the frame breathes open over the hold
    k.text("Word", "ATELIER", 960, 540, 80, COL['ivory'], f0=24, dur=n - 24, style='Regular', align='center', track=1.6)
    PRESETS.append(("ML Framed word", "Word", "Slow fade in"))


def slow_dip(d):
    n = 60
    k = d.comp("ML Slow dip", n, "mdp")
    o = k.rect("Dip", 0, 0, 1920, 1080, COL['bg'], f0=0, dur=n)
    o.op([(0, 0.0, 'Linear'), (26, 1.0, SMOOTH), (34, 1.0, 'Linear'), (n, 0.0, SMOOTH)])


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    lower_third(d); monogram_end(d); price_card(d); collection_title(d); light_sweep(d); attribute_row(d); framed_word(d); slow_dip(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
