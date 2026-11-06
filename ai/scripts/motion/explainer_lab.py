"""Write the Explainer lab comps into a .carverproj (direct project-file authoring).

    import explainer_lab as L; presets, masks = L.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); edit.save.
Check with carvercat_inspect and carvercat_look; extract templates with
comp_to_template.py (--drop "Lab bg").

Arrows here are a trimmed line plus a separate triangle head that pops when the line
arrives; for a single editable arrow object use the native authoring.arrow batch step.
Fonts: Rethink Sans must be installed (KI-136).
Docs: ai/patterns/explainer.md. Pixel space 1920x1080, y down; comp frames, 30 fps.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author"))
from cc import Doc, lin, P, BEZ

COL = dict(bg=lin('F7F7FA'), ink=lin('1F2333'), blue=lin('3B6EF6'), coral=lin('FF6B5B'), green=lin('2BB673'),
           grey=lin('C9CDD8'), muted=lin('6B7184'), white=lin('FFFFFF'))
EXPO, BACK = BEZ['expo'], BEZ['back']
PRESETS, MASKS = [], []


def lab_bg(k, n):
    k.rect("Lab bg", 0, 0, 1920, 1080, COL['bg'], f0=0, dur=n)


def pop(o, f, d=12):
    o.scale([(f, 0.0, 'Linear'), (f + d, 1.0, BACK)])


def arrow(k, name, a, b, f, col, d=12):
    """a trimmed line from a to b and a triangle head that pops as the line arrives"""
    ln = k.line(name, [a, b], col, px=8, f0=f, dur=None)
    ln.trim([(f, 0.0, 'Linear'), (f + d, 1.0, EXPO)], which='end')
    ang = math.degrees(math.atan2(-(b[1] - a[1]), b[0] - a[0]))      # math angle, y up; rotation is counter-clockwise
    head = k.ngon(name + " head", b[0], b[1], 34, 3, col, f0=f + d - 4, dur=None, angle=0.0)
    head.rotv(round(ang, 2))                                          # measured: a 3-gon at rotation 0 points right
    pop(head, f + d - 4, 8)
    return ln, head


def process_steps(d):
    n = 120
    k = d.comp("EX Process steps", n, "eps"); lab_bg(k, n)
    xs, y = (420, 960, 1500), 480
    labels = [("Plan", "Write the brief"), ("Build", "Make it in Carvercat"), ("Ship", "Render and deliver")]
    for i, (x, (t, s)) in enumerate(zip(xs, labels)):
        f = i * 24
        c = k.ell(f"Step {i + 1}", x, y, 160, 160, (COL['blue'], COL['coral'], COL['green'])[i], f0=f, dur=n - f)
        pop(c, f)
        k.text(f"Step {i + 1} number", str(i + 1), x, y, 72, COL['white'], f0=f + 4, dur=n - f - 4, style='ExtraBold', align='center')
        PRESETS.append(("EX Process steps", f"Step {i + 1} number", "Step in"))
        k.text(f"Step {i + 1} title", t, x, y + 140, 48, COL['ink'], f0=f + 6, dur=n - f - 6, style='Bold', align='center')
        PRESETS.append(("EX Process steps", f"Step {i + 1} title", "Step in"))
        k.text(f"Step {i + 1} text", s, x, y + 200, 30, COL['muted'], f0=f + 10, dur=n - f - 10, style='Medium', align='center')
        PRESETS.append(("EX Process steps", f"Step {i + 1} text", "Step in"))
        if i < 2:
            arrow(k, f"Arrow {i + 1}", (x + 110, y), (xs[i + 1] - 125, y), f + 12, COL['muted'])
    for o in k.vtracks:                                              # arrows were made with dur=None: end with the comp
        cl = o[0]
        if cl['duration'] <= 0 or cl['left'] / 4 + cl['duration'] > n: cl['duration'] = n - cl['left'] / 4


def icon_grid(d):
    n = 90
    k = d.comp("EX Icon grid", n, "eig"); lab_bg(k, n)
    items = [("Fast", "star"), ("Simple", "circle"), ("Secure", "square"), ("Shared", "triangle"), ("Native", "hex"), ("Free", "ring")]
    for i, (word, shape) in enumerate(items):
        r, c = divmod(i, 3); x = 560 + c * 400; y = 380 + r * 320; f = i * 5
        tile = k.rect(f"Tile {i + 1}", x, y, 300, 260, COL['white'], r=28, f0=f, dur=n - f, center=True)
        tile.shadow(y=-0.003, soft=0.012, op=0.15)
        PRESETS.append(("EX Icon grid", f"Tile {i + 1}", "Step in"))
        col = (COL['blue'], COL['coral'], COL['green'])[i % 3]; iy = y - 30
        if shape == "star": ic = k.star(f"Icon {i + 1}", x, iy, 110, 5, 0.45, col, f0=f + 4, dur=n - f - 4)
        elif shape == "circle": ic = k.ell(f"Icon {i + 1}", x, iy, 96, 96, col, f0=f + 4, dur=n - f - 4)
        elif shape == "square": ic = k.rect(f"Icon {i + 1}", x, iy, 90, 90, col, r=18, f0=f + 4, dur=n - f - 4, center=True)
        elif shape == "triangle": ic = k.ngon(f"Icon {i + 1}", x, iy, 110, 3, col, f0=f + 4, dur=n - f - 4)
        elif shape == "hex": ic = k.ngon(f"Icon {i + 1}", x, iy, 104, 6, col, f0=f + 4, dur=n - f - 4)
        else:
            ic = k.ell(f"Icon {i + 1}", x, iy, 96, 96, None, f0=f + 4, dur=n - f - 4); ic.stroke(col, 14)
        pop(ic, f + 4)
        k.text(f"Caption {i + 1}", word, x, y + 80, 34, COL['ink'], f0=f + 8, dur=n - f - 8, style='Bold', align='center')
        PRESETS.append(("EX Icon grid", f"Caption {i + 1}", "Step in"))


def callout(d):
    n = 75
    k = d.comp("EX Callout", n, "eco"); lab_bg(k, n)
    tx, ty = 760, 640
    dot = k.ell("Target", tx, ty, 28, 28, COL['coral'], f0=0, dur=n); pop(dot, 0, 10)
    ring = k.ell("Target ring", tx, ty, 90, 90, None, f0=6, dur=n - 6); ring.stroke(COL['coral'], 5)
    PRESETS.append(("EX Callout", "Target ring", "Emphasis pulse"))
    ring.op([(6, 0.0, 'Linear'), (10, 1.0, 'Linear')])
    lead = k.line("Leader", [(tx + 30, ty - 30), (tx + 220, ty - 220), (tx + 520, ty - 220)], COL['ink'], px=4, f0=10, dur=n - 10)
    lead.trim([(10, 0.0, 'Linear'), (26, 1.0, EXPO)], which='end')
    box = k.rect("Label box", tx + 540, ty - 260, 520, 84, COL['ink'], r=16, f0=24, dur=n - 24)
    box.anchor(-1, 0); box.scale([(24, [0.0, 1.0], 'Linear'), (36, [1.0, 1.0], EXPO)])
    k.text("Label", "The part that matters", tx + 570, ty - 218, 36, COL['white'], f0=30, dur=n - 30, style='Bold')
    PRESETS.append(("EX Callout", "Label", "Step in"))


def timeline(d):
    n = 150                                                           # 40 f after the last milestone: enough to read it
    k = d.comp("EX Timeline", n, "etl"); lab_bg(k, n)
    x0, x1, y = 260, 1660, 560
    base = k.line("Track", [(x0, y), (x1, y)], COL['grey'], px=6, f0=0, dur=n)
    base.trim([(0, 0.0, 'Linear'), (24, 1.0, EXPO)], which='end')
    prog = k.line("Progress", [(x0, y), (x1, y)], COL['blue'], px=6, f0=0, dur=n)
    prog.trim([(30, 0.0, 'Linear'), (110, 1.0, 'S-curve')], which='end')
    ms = [("2019", "Idea"), ("2021", "First release"), ("2023", "Teams"), ("2026", "Everywhere")]
    for i, (yr, txt) in enumerate(ms):
        x = x0 + (x1 - x0) * i / 3
        f = 30 + round(80 * i / 3)                                    # the dot pops as the progress reaches it
        dot = k.ell(f"Milestone {i + 1}", x, y, 30, 30, COL['blue'], f0=f, dur=n - f); dot.stroke(COL['white'], 6); pop(dot, f, 10)
        k.text(f"Year {i + 1}", yr, x, y - 70, 44, COL['ink'], f0=f + 2, dur=n - f - 2, style='ExtraBold', align='center')
        PRESETS.append(("EX Timeline", f"Year {i + 1}", "Step in"))
        k.text(f"Event {i + 1}", txt, x, y + 70, 30, COL['muted'], f0=f + 5, dur=n - f - 5, style='Medium', align='center')
        PRESETS.append(("EX Timeline", f"Event {i + 1}", "Step in"))


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    process_steps(d); icon_grid(d); callout(d); timeline(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
