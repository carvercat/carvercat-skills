"""Explainer round 2: eight more lab comps (speaker lower third, compare columns, flow
diagram, key term card, checklist, Venn diagram, quiz question, cycle loop), written
straight into a .carverproj.

    import explainer_lab2 as L; presets, masks = L.build(PROJECT.carverproj)

Same palette and rules as explainer_lab.py: everything enters in reading order at the speed
of narration, one emphasis at a time, and the last item gets time to be read. Arrows reuse
explainer_lab.arrow (a trimmed line plus a triangle head). After writing: edit.open {path,
force:true}; apply PRESETS (preset.apply); edit.save; check with carvercat_inspect and
carvercat_look; extract templates with comp_to_template.py (--drop "Lab bg").
Docs: ai/patterns/explainer.md.
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explainer_lab import Doc, lin, P, COL, EXPO, BACK, lab_bg, pop, arrow

PRESETS, MASKS = [], []


def light_bg(k, n):
    """full-frame layouts keep their light ground in the template (the 'Lab bg' is dropped on extraction,
    which would leave ink text on whatever is underneath)"""
    k.rect("Light background", 0, 0, 1920, 1080, COL['bg'], f0=0, dur=n)


def end_with_comp(k, n):
    """clips made with dur=None (arrow helper) end with the comp"""
    for o in k.vtracks:
        cl = o[0]
        if cl['duration'] <= 0 or cl['left'] / 4 + cl['duration'] > n: cl['duration'] = n - cl['left'] / 4


def check_mark(k, name, x, y, s, col, f):
    o = k.line(name, [(x - s * 0.45, y), (x - s * 0.1, y + s * 0.35), (x + s * 0.5, y - s * 0.35)], col, px=10, f0=f, dur=None)
    o.trim([(f, 0.0, 'Linear'), (f + 10, 1.0, EXPO)])
    return o


def lower_third(d):
    n = 150
    k = d.comp("EX Lower third", n, "elt"); lab_bg(k, n)
    k.rect("LT card", 120, 830, 640, 130, COL['white'], r=24, f0=0, dur=n).shadow(y=-0.003, soft=0.012, op=0.15)
    PRESETS.extend([("EX Lower third", "LT card", "Step in"), ("EX Lower third", "LT card", "Exit fade - fast")])
    dot = k.ell("LT dot", 180, 895, 36, 36, COL['blue'], f0=4, dur=n - 4); pop(dot, 4, 10)
    PRESETS.append(("EX Lower third", "LT dot", "Exit fade - fast"))
    k.text("LT name", "Dr. Lena Park", 220, 870, 46, COL['ink'], f0=6, dur=n - 6, style='Bold')
    PRESETS.extend([("EX Lower third", "LT name", "Step in"), ("EX Lower third", "LT name", "Exit fade - fast")])
    k.text("LT role", "Climate scientist", 220, 922, 30, COL['muted'], f0=10, dur=n - 10, style='Medium')
    PRESETS.extend([("EX Lower third", "LT role", "Step in"), ("EX Lower third", "LT role", "Exit fade - fast")])


def compare_columns(d):
    n = 150
    k = d.comp("EX Compare columns", n, "ecc"); lab_bg(k, n); light_bg(k, n)
    cols = [("Old way", COL['coral'], 520, ["Manual exports", "Lost versions", "Slow reviews"], False),
            ("New way", COL['green'], 1400, ["One click", "Every version saved", "Comments in place"], True)]
    for c, (title, col, x, items, good) in enumerate(cols):
        f0 = c * 40
        k.rect(f"Col head {c + 1}", x - 300, 250, 600, 90, col, r=20, f0=f0, dur=n - f0)
        PRESETS.append(("EX Compare columns", f"Col head {c + 1}", "Step in"))
        k.text(f"Col title {c + 1}", title, x, 295, 44, COL['white'], f0=f0 + 2, dur=n - f0 - 2, style='Bold', align='center')
        PRESETS.append(("EX Compare columns", f"Col title {c + 1}", "Step in"))
        for i, it in enumerate(items):
            y, f = 430 + i * 110, f0 + 8 + i * 8
            if good:
                check_mark(k, f"Tick {c + 1}.{i + 1}", x - 250, y, 50, col, f)
            else:
                for j, (a, b) in enumerate([((x - 270, y - 20), (x - 230, y + 20)), ((x - 270, y + 20), (x - 230, y - 20))]):
                    ln = k.line(f"Cross {c + 1}.{i + 1}.{j + 1}", [a, b], col, px=10, f0=f + j * 2, dur=None)
                    ln.trim([(f + j * 2, 0.0, 'Linear'), (f + j * 2 + 6, 1.0, EXPO)])
            k.text(f"Item {c + 1}.{i + 1}", it, x - 190, y, 38, COL['ink'], f0=f + 2, dur=n - f - 2, style='Medium')
            PRESETS.append(("EX Compare columns", f"Item {c + 1}.{i + 1}", "Step in"))
    end_with_comp(k, n)


def flow_diagram(d):
    n = 150
    k = d.comp("EX Flow diagram", n, "efd"); lab_bg(k, n); light_bg(k, n)
    boxes = [("Record", 400, COL['blue']), ("Edit", 960, COL['coral']), ("Publish", 1520, COL['green'])]
    for i, (lab, x, col) in enumerate(boxes):
        f = i * 26
        k.rect(f"Node {i + 1}", x - 190, 470, 380, 140, COL['white'], r=26, f0=f, dur=n - f).stroke(col, 6)
        PRESETS.append(("EX Flow diagram", f"Node {i + 1}", "Step in"))
        k.text(f"Node label {i + 1}", lab, x, 540, 48, COL['ink'], f0=f + 4, dur=n - f - 4, style='Bold', align='center')
        PRESETS.append(("EX Flow diagram", f"Node label {i + 1}", "Step in"))
        if i < 2:
            arrow(k, f"Flow arrow {i + 1}", (x + 200, 540), (boxes[i + 1][1] - 215, 540), f + 12, COL['muted'])
    k.text("Flow note", "about 10 minutes end to end", 960, 720, 34, COL['muted'], f0=70, dur=n - 70, style='Medium', align='center')
    PRESETS.append(("EX Flow diagram", "Flow note", "Step in"))
    end_with_comp(k, n)


def key_term(d):
    n = 150
    k = d.comp("EX Key term", n, "ekt"); lab_bg(k, n); light_bg(k, n)
    k.text("Term tag", "KEY TERM", 400, 330, 30, COL['blue'], f0=0, dur=n, style='Bold', track=1.4)
    PRESETS.append(("EX Key term", "Term tag", "Step in"))
    t = k.text("Term", "Keyframe", 400, 440, 120, COL['ink'], f0=6, dur=n - 6, style='ExtraBold')
    PRESETS.append(("EX Key term", "Term", "Step in"))
    ul = k.rect("Term underline", 400, 510, 520, 10, COL['coral'], r=5, f0=16, dur=n - 16)
    ul.anchor(-1, 0); ul.scale([(16, [0.0, 1.0], 'Linear'), (30, [1.0, 1.0], EXPO)])
    k.text("Definition", "A moment where you fix a value;\nthe software fills in the frames between.", 400, 640, 46, COL['ink'], f0=26, dur=n - 26,
           style='Medium', lh=1.3)
    PRESETS.append(("EX Key term", "Definition", "Step in"))


def checklist(d):
    n = 150
    k = d.comp("EX Checklist", n, "ecl"); lab_bg(k, n); light_bg(k, n)
    k.text("List title", "Before you render", 520, 260, 64, COL['ink'], f0=0, dur=n, style='ExtraBold')
    PRESETS.append(("EX Checklist", "List title", "Step in"))
    for i, it in enumerate(["Fonts installed", "Lint is clean", "Audio levels checked", "Safe areas respected"]):
        y, f = 400 + i * 120, 10 + i * 18
        box = k.rect(f"Box {i + 1}", 520, y - 32, 64, 64, None, r=14, f0=f, dur=n - f); box.stroke(COL['grey'], 6)
        PRESETS.append(("EX Checklist", f"Box {i + 1}", "Step in"))
        k.text(f"Check item {i + 1}", it, 620, y, 44, COL['ink'], f0=f + 2, dur=n - f - 2, style='Medium')
        PRESETS.append(("EX Checklist", f"Check item {i + 1}", "Step in"))
        check_mark(k, f"Check {i + 1}", 552, y, 44, COL['green'], f + 10)
    end_with_comp(k, n)


def venn(d):
    n = 120
    k = d.comp("EX Venn", n, "evn"); lab_bg(k, n); light_bg(k, n)
    for i, (lab, col, x, sx) in enumerate([("Design", COL['blue'], 820, -1), ("Code", COL['coral'], 1100, 1)]):
        c = k.ell(f"Set {i + 1}", x, 520, 460, 460, col, f0=0, dur=n); c.opv(0.55)
        bx, by = c.base
        c.pos([(0, [bx + sx * 220 / 1920, by], 'Linear'), (24, [bx, by], EXPO)])
        PRESETS.append(("EX Venn", f"Set {i + 1}", "Step in"))
        k.text(f"Set label {i + 1}", lab, x + sx * 110, 520, 48, COL['ink'], f0=20, dur=n - 20, style='Bold', align='center')
        PRESETS.append(("EX Venn", f"Set label {i + 1}", "Step in"))
    k.text("Overlap label", "Motion", 960, 520, 40, COL['white'], f0=36, dur=n - 36, style='ExtraBold', align='center')
    PRESETS.extend([("EX Venn", "Overlap label", "Step in"), ("EX Venn", "Overlap label", "Emphasis pulse")])
    k.text("Venn caption", "where the two meet", 960, 840, 34, COL['muted'], f0=44, dur=n - 44, style='Medium', align='center')
    PRESETS.append(("EX Venn", "Venn caption", "Step in"))


def quiz(d):
    n = 180
    k = d.comp("EX Quiz", n, "eqz"); lab_bg(k, n); light_bg(k, n)
    k.text("Quiz question", "Which key shapes the move into it?", 960, 280, 56, COL['ink'], f0=0, dur=n, style='Bold', align='center')
    PRESETS.append(("EX Quiz", "Quiz question", "Step in"))
    opts = ["The key before", "The key after", "Neither"]
    reveal = 100                                                          # think time, then the answer
    for i, o in enumerate(opts):
        y, f = 450 + i * 130, 20 + i * 8
        right = i == 1
        card = k.rect(f"Option {i + 1}", 560, y - 50, 800, 100, COL['white'], r=22, f0=f, dur=n - f); card.stroke(COL['grey'], 4)
        PRESETS.append(("EX Quiz", f"Option {i + 1}", "Step in"))
        k.text(f"Option text {i + 1}", f"{'ABC'[i]}.  {o}", 610, y, 42, COL['ink'], f0=f + 2, dur=n - f - 2, style='Medium')
        PRESETS.append(("EX Quiz", f"Option text {i + 1}", "Step in"))
        if right:
            hl = k.rect("Answer frame", 560, y - 50, 800, 100, None, r=22, f0=reveal, dur=n - reveal); hl.stroke(COL['green'], 8)
            PRESETS.append(("EX Quiz", "Answer frame", "Emphasis pulse"))
            check_mark(k, "Answer check", 1290, y, 50, COL['green'], reveal + 4)
    end_with_comp(k, n)


def cycle(d):
    n = 150
    k = d.comp("EX Cycle", n, "ecy"); lab_bg(k, n); light_bg(k, n)
    cx, cy, R = 960, 540, 300
    ring = k.ell("Cycle ring", cx, cy, 2 * R, 2 * R, None, f0=0, dur=n); ring.stroke(COL['grey'], 6, line='dashed', dash=24, gap=16)
    ring.rot([(0, 0.0, 'Linear'), (n, -45.0, 'Linear')])                # turns clockwise, one way
    steps = [("Plan", COL['blue']), ("Make", COL['coral']), ("Test", COL['green']), ("Learn", COL['ink'])]
    for i, (lab, col) in enumerate(steps):
        a = math.radians(90 - i * 90)                                    # clockwise from 12 o'clock
        x, y = cx + R * math.cos(a), cy - R * math.sin(a)
        f = 6 + i * 14
        node = k.ell(f"Cycle node {i + 1}", x, y, 170, 170, col, f0=f, dur=n - f); pop(node, f)
        k.text(f"Cycle label {i + 1}", lab, x, y, 40, COL['white'], f0=f + 4, dur=n - f - 4, style='Bold', align='center')
        PRESETS.append(("EX Cycle", f"Cycle label {i + 1}", "Step in"))
    k.text("Cycle centre", "repeat", cx, cy, 44, COL['muted'], f0=64, dur=n - 64, style='Medium', align='center')
    PRESETS.append(("EX Cycle", "Cycle centre", "Step in"))


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    lower_third(d); compare_columns(d); flow_diagram(d); key_term(d); checklist(d); venn(d); quiz(d); cycle(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
