"""Write the Sports lab comps into a .carverproj (direct project-file authoring).

    import sports_lab as L; presets, masks = L.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); for each MASKS
pair (content, window) run mask.make {ids:[window, content]} - the FIRST id is the mask -
then parent.clear; edit.save. Check with carvercat_inspect and carvercat_look; extract
templates with comp_to_template.py (--drop "Lab bg").

Fonts: Rethink Sans must be installed (KI-136).
Docs: ai/patterns/sports.md. Pixel space 1920x1080, y down; comp frames, 30 fps.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author"))
from cc import Doc, lin, P, BEZ

COL = dict(bg=lin('0B1020'), panel=lin('141B33'), red=lin('E63946'), blue=lin('1D7CF2'), yellow=lin('FFD60A'),
           white=lin('FFFFFF'), grey=lin('8892AA'), ink=lin('0B1020'))
EXPO, BACK = BEZ['expo'], BEZ['back']
PRESETS, MASKS = [], []


def lab_bg(k, n):
    k.rect("Lab bg", 0, 0, 1920, 1080, COL['bg'], f0=0, dur=n)


def grow_x(o, f, d=10):
    o.anchor(-1, 0); o.scale([(f, [0.0, 1.0], 'Linear'), (f + d, [1.0, 1.0], EXPO)])


def score_bug(d):
    n = 120
    k = d.comp("SP Score bug", n, "ssb"); lab_bg(k, n)
    x, y, h = 96, 64, 64
    parts = [("Team A box", 120, COL['red']), ("Score box", 140, COL['panel']), ("Team B box", 120, COL['blue']), ("Clock box", 130, COL['grey'])]
    cx = x
    for i, (name, w, col) in enumerate(parts):
        b = k.rect(name, cx, y, w, h, col, f0=0, dur=n)
        grow_x(b, i * 3)
        parts[i] = (name, w, col, cx)
        cx += w
    def label(name, s, px, x0, w, f, col=COL['white']):
        k.text(name, s, x0 + w / 2, y + h / 2, px, col, f0=f, dur=n - f, style='ExtraBold', align='center')
    label("Team A", "LIV", 34, parts[0][3], 120, 6)
    label("Team B", "MCI", 34, parts[2][3], 120, 12)
    label("Clock", "67:12", 30, parts[3][3], 130, 15, COL['ink'])
    sx, sw = parts[1][3], 140
    old = k.text("Score old", "2 - 1", sx + sw / 2, y + h / 2, 34, COL['white'], f0=9, dur=58 - 9, style='ExtraBold', align='center')
    ox, oy = old.base
    old.pos([(52, [ox, oy], 'Linear'), (58, [ox, oy + 50 / 1080], 'Ease in')])       # leaves upward through the window
    new = k.text("Score new", "3 - 1", sx + sw / 2, y + h / 2, 34, COL['yellow'], f0=58, dur=n - 58, style='ExtraBold', align='center')
    nx, ny = new.base
    new.pos([(58, [nx, ny - 50 / 1080], 'Linear'), (68, [nx, ny], EXPO)])   # enters as the old one has left: never both
    for nm, f0, dur in (("Score window old", 9, 58 - 9), ("Score window new", 58, n - 58)):
        k.rect(nm, sx, y, sw, h, COL['white'], f0=f0, dur=dur)
    MASKS.extend([("SP Score bug", "Score old", "Score window old"), ("SP Score bug", "Score new", "Score window new")])
    ul = k.rect("Goal underline", sx, y + h, sw, 6, COL['yellow'], f0=60, dur=n - 60)
    grow_x(ul, 60, 8)


def player_card(d):
    n = 90
    k = d.comp("SP Player card", n, "spc"); lab_bg(k, n)
    slant = 120
    pts = [(300 + slant, 260), (1620, 260), (1620 - slant, 820), (300, 820)]
    panel = k.path("Panel", pts, f0=0, dur=n, closed=True); panel.fill(COL['panel'])
    PRESETS.append(("SP Player card", "Panel", "Slash in"))
    stripe = k.line("Stripe", [(1380, 260), (1260, 820)], COL['red'], px=40, f0=4, dur=n - 4)
    stripe.set(stripe.src('shape_stroke', 'cap'), 'butt')
    stripe.trim([(4, 0.0, 'Linear'), (14, 1.0, EXPO)], which='end')
    num = k.text("Number", "10", 1380, 540, 360, COL['yellow'], f0=8, dur=n - 8, style='ExtraBold', align='center')
    num.set(num.src('text_fill', 'paint'), 'none')
    num.set(num.src('text_outline', 'paint'), 'solid').set(num.src('text_outline', 'color'), COL['yellow'][:3]).set(num.src('text_outline', 'thickness'), 0.025)
    PRESETS.append(("SP Player card", "Number", "Impact slam"))
    k.text("Name", "ALEX MORGAN", 470, 500, 88, COL['white'], f0=10, dur=n - 10, style='ExtraBold')
    PRESETS.append(("SP Player card", "Name", "Slash in"))
    k.text("Position", "FORWARD  ·  #10", 474, 600, 38, COL['yellow'], f0=16, dur=n - 16, style='SemiBold', track=1.3)
    PRESETS.append(("SP Player card", "Position", "Slash in"))


def head_to_head(d):
    n = 90
    k = d.comp("SP Head to head", n, "shh"); lab_bg(k, n)
    k.text("H2H title", "HEAD TO HEAD", 960, 250, 48, COL['white'], f0=0, dur=n, style='ExtraBold', align='center', track=1.3)
    PRESETS.append(("SP Head to head", "H2H title", "Slash in"))
    rows = [("SHOTS", 14, 9, "14", "9"), ("POSSESSION", 58, 42, "58%", "42%"), ("CORNERS", 7, 3, "7", "3")]
    for i, (lab, a, b, ta, tb) in enumerate(rows):
        y = 420 + i * 150; f = 8 + i * 8
        k.text(f"Row label {i + 1}", lab, 960, y - 48, 30, COL['grey'], f0=f, dur=n - f, style='SemiBold', align='center', track=1.3)
        tot = a + b; wa, wb = 560 * a / tot * 2 * 0.9, 560 * b / tot * 2 * 0.9
        la = k.rect(f"Bar A {i + 1}", 940 - wa / 2, y, wa, 34, COL['red'], f0=f, dur=n - f, center=True)
        la.anchor(1, 0); la.scale([(f, [0.0, 1.0], 'Linear'), (f + 14, [1.0, 1.0], EXPO)])     # grows left from the centre
        lb = k.rect(f"Bar B {i + 1}", 980 + wb / 2, y, wb, 34, COL['blue'], f0=f, dur=n - f, center=True)
        lb.anchor(-1, 0); lb.scale([(f, [0.0, 1.0], 'Linear'), (f + 14, [1.0, 1.0], EXPO)])    # grows right
        k.text(f"Value A {i + 1}", ta, 940 - wa - 24, y, 40, COL['white'], f0=f + 12, dur=n - f - 12, style='ExtraBold', align='right')
        k.text(f"Value B {i + 1}", tb, 980 + wb + 24, y, 40, COL['white'], f0=f + 12, dur=n - f - 12, style='ExtraBold')


def goal_slam(d):
    n = 60
    k = d.comp("SP Goal slam", n, "sgs"); lab_bg(k, n)
    cx, cy = 960, 540
    for i in range(10):
        a = math.radians(i * 36 + 12)
        p0 = (cx + 260 * math.cos(a), cy - 160 * math.sin(a)); p1 = (cx + 900 * math.cos(a), cy - 520 * math.sin(a))
        p1 = (min(max(p1[0], 0), 1920), min(max(p1[1], 0), 1080))
        ln = k.line(f"Speed line {i + 1}", [p0, p1], COL['white'] if i % 2 else COL['yellow'], px=8, f0=0, dur=n)
        tp = ln.trim([(0, 0.0, 'Linear'), (8, 1.0, EXPO)], which='end')
        ln.key(tp + '.start', [(6, 0.0, 'Linear'), (18, 1.0, 'Ease in')])
    band = k.path("Band", [(200, 430), (1800, 380), (1720, 700), (120, 650)], f0=0, dur=n, closed=True); band.fill(COL['red'])
    PRESETS.append(("SP Goal slam", "Band", "Slash in"))
    g = k.text("Goal", "GOAL!", cx, cy, 260, COL['yellow'], f0=4, dur=n - 4, style='ExtraBold', align='center')
    g.set(g.src('text_outline', 'paint'), 'solid').set(g.src('text_outline', 'color'), COL['ink'][:3]).set(g.src('text_outline', 'thickness'), 0.05).set(g.src('text_outline', 'outsideOnly'), True)
    PRESETS.append(("SP Goal slam", "Goal", "Impact slam"))


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    score_bug(d); player_card(d); head_to_head(d); goal_slam(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
