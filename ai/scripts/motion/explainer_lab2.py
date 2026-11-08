"""Explainer round 2 in design units: eight more lab comps (speaker lower third, compare columns, flow diagram, key term card,
checklist, Venn diagram, quiz question, cycle loop).

    import explainer_lab2 as L; doc = L.build(); doc.send(client, PROJECT.carverproj)

Same palette and rules as explainer_lab.py (everything enters in reading order at the speed of narration, one emphasis at a time,
the last item gets time to be read), and the same baked presets (step_in, pulse, exit_fade). Arrows reuse explainer_lab.arrow.
Each full-frame layout carries its own "Light background" (the "Lab bg" is dropped on extraction). Docs: ai/patterns/explainer.md.
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explainer_lab import (Doc, COL, EXPO, BACK, W, H, T, step_in, pulse, exit_fade, pop, draw, arrow, line, lab_bg, shadow,
                           origin, BEZ, css)


def light_bg(k, n):
    k.rect("Light background", 0, 0, W, H, COL['bg'], f0=0, dur=n)


def check_mark(k, name, x, y, s, col, f, n):
    o = line(k, name, [(x - s * 0.45, y), (x - s * 0.1, y + s * 0.35), (x + s * 0.5, y - s * 0.35)], col, px=10, f0=f, dur=n - f)
    o.trim([(f, 0.0, 'Linear'), (f + 10, 1.0, EXPO)])
    return o


def lower_third(d):
    n = 150
    k = d.comp("EX Lower third", n, "elt"); lab_bg(k, n)
    card = k.rect("LT card", 120, 830, 640, 130, COL['white'], r=24, f0=0, dur=n)
    shadow(card); step_in(card, 0); exit_fade(card, n)
    dot = k.ell("LT dot", 180, 895, 36, 36, COL['blue'], f0=4, dur=n - 4); pop(dot, 4, 10); exit_fade(dot, n)
    for nm, s, x, y, px, col, st, f in (("LT name", "Dr. Lena Park", 220, 870, 46, COL['ink'], 'Bold', 6),
                                         ("LT role", "Climate scientist", 220, 922, 30, COL['muted'], 'Medium', 10)):
        o = T(k, nm, s, x, y, px, col, f, n - f, st); step_in(o, f); exit_fade(o, n)


def compare_columns(d):
    n = 150
    k = d.comp("EX Compare columns", n, "ecc"); lab_bg(k, n); light_bg(k, n)
    cols = [("Old way", COL['coral'], 520, ["Manual exports", "Lost versions", "Slow reviews"], False),
            ("New way", COL['green'], 1400, ["One click", "Every version saved", "Comments in place"], True)]
    for c, (title, col, x, items, good) in enumerate(cols):
        f0 = c * 40
        step_in(k.rect(f"Col head {c + 1}", x - 300, 250, 600, 90, col, r=20, f0=f0, dur=n - f0), f0)
        step_in(T(k, f"Col title {c + 1}", title, x, 295, 44, COL['white'], f0 + 2, n - f0 - 2, 'Bold', 'center'), f0 + 2)
        for i, it in enumerate(items):
            y, f = 430 + i * 110, f0 + 8 + i * 8
            if good:
                check_mark(k, f"Tick {c + 1}.{i + 1}", x - 250, y, 50, col, f, n)
            else:
                for j, (a, b) in enumerate([((x - 270, y - 20), (x - 230, y + 20)), ((x - 270, y + 20), (x - 230, y - 20))]):
                    g = f + j * 2
                    ln = line(k, f"Cross {c + 1}.{i + 1}.{j + 1}", [a, b], col, px=10, f0=g, dur=n - g)
                    ln.trim([(g, 0.0, 'Linear'), (g + 6, 1.0, EXPO)])
            step_in(T(k, f"Item {c + 1}.{i + 1}", it, x - 190, y, 38, COL['ink'], f + 2, n - f - 2, 'Medium'), f + 2)


def flow_diagram(d):
    n = 150
    k = d.comp("EX Flow diagram", n, "efd"); lab_bg(k, n); light_bg(k, n)
    boxes = [("Record", 400, COL['blue']), ("Edit", 960, COL['coral']), ("Publish", 1520, COL['green'])]
    for i, (lab, x, col) in enumerate(boxes):
        f = i * 26
        nd = k.rect(f"Node {i + 1}", x - 190, 470, 380, 140, COL['white'], r=26, f0=f, dur=n - f); nd.stroke(col, 6); step_in(nd, f)
        step_in(T(k, f"Node label {i + 1}", lab, x, 540, 48, COL['ink'], f + 4, n - f - 4, 'Bold', 'center'), f + 4)
        if i < 2:
            arrow(k, f"Flow arrow {i + 1}", (x + 200, 540), (boxes[i + 1][1] - 215, 540), f + 12, COL['muted'], n=n)
    step_in(T(k, "Flow note", "about 10 minutes end to end", 960, 720, 34, COL['muted'], 70, n - 70, 'Medium', 'center'), 70)


def key_term(d):
    n = 150
    k = d.comp("EX Key term", n, "ekt"); lab_bg(k, n); light_bg(k, n)
    step_in(T(k, "Term tag", "KEY TERM", 400, 330, 30, COL['blue'], 0, n, 'Bold', track=1.4, width=700), 0)
    step_in(T(k, "Term", "Keyframe", 400, 440, 120, COL['ink'], 6, n - 6, 'ExtraBold'), 6)
    ul = k.rect("Term underline", 400, 510, 520, 10, COL['coral'], r=2.5, f0=16, dur=n - 16)
    origin(ul, -1, 0); ul.scale([(16, [0.0, 1.0], 'Linear'), (30, [1.0, 1.0], EXPO)])
    step_in(T(k, "Definition", "A moment where you fix a value;\nthe software fills in the frames between.", 400, 640, 46, COL['ink'],
              26, n - 26, 'Medium', lh=1.3), 26)


def checklist(d):
    n = 150
    k = d.comp("EX Checklist", n, "ecl"); lab_bg(k, n); light_bg(k, n)
    step_in(T(k, "List title", "Before you render", 520, 260, 64, COL['ink'], 0, n, 'ExtraBold'), 0)
    for i, it in enumerate(["Fonts installed", "Lint is clean", "Audio levels checked", "Safe areas respected"]):
        y, f = 400 + i * 120, 10 + i * 18
        box = k.rect(f"Box {i + 1}", 520, y - 32, 64, 64, None, r=14, f0=f, dur=n - f); box.stroke(COL['grey'], 6); step_in(box, f)
        step_in(T(k, f"Check item {i + 1}", it, 620, y, 44, COL['ink'], f + 2, n - f - 2, 'Medium'), f + 2)
        check_mark(k, f"Check {i + 1}", 552, y, 44, COL['green'], f + 10, n)


def venn(d):
    n = 120
    k = d.comp("EX Venn", n, "evn"); lab_bg(k, n); light_bg(k, n)
    for i, (lab, col, x, sx) in enumerate([("Design", COL['blue'], 820, -1), ("Code", COL['coral'], 1100, 1)]):
        c = k.ell(f"Set {i + 1}", x, 520, 460, 460, css(col, 0.55), f0=0, dur=n)    # translucent fill: the opacity key of step_in would replace a static opacity
        bx, by = c.base
        c.pos([(0, (bx + sx * 220, by), 'Linear'), (24, (bx, by), EXPO)])
        step_in(c, 0)
        step_in(T(k, f"Set label {i + 1}", lab, x + sx * 110, 520, 48, COL['ink'], 20, n - 20, 'Bold', 'center'), 20)
    o = T(k, "Overlap label", "Motion", 960, 520, 40, COL['white'], 36, n - 36, 'ExtraBold', 'center'); step_in(o, 36); pulse(o, 36 + 16)
    step_in(T(k, "Venn caption", "where the two meet", 960, 840, 34, COL['muted'], 44, n - 44, 'Medium', 'center'), 44)


def quiz(d):
    n = 180
    k = d.comp("EX Quiz", n, "eqz"); lab_bg(k, n); light_bg(k, n)
    step_in(T(k, "Quiz question", "Which key shapes the move into it?", 960, 280, 56, COL['ink'], 0, n, 'Bold', 'center'), 0)
    reveal = 100                                                          # think time, then the answer
    for i, o in enumerate(["The key before", "The key after", "Neither"]):
        y, f = 450 + i * 130, 20 + i * 8
        card = k.rect(f"Option {i + 1}", 560, y - 50, 800, 100, COL['white'], r=22, f0=f, dur=n - f); card.stroke(COL['grey'], 4); step_in(card, f)
        step_in(T(k, f"Option text {i + 1}", f"{'ABC'[i]}.  {o}", 610, y, 42, COL['ink'], f + 2, n - f - 2, 'Medium'), f + 2)
        if i == 1:
            hl = k.rect("Answer frame", 560, y - 50, 800, 100, None, r=22, f0=reveal, dur=n - reveal); hl.stroke(COL['green'], 8)
            pulse(hl, reveal)
            check_mark(k, "Answer check", 1290, y, 50, COL['green'], reveal + 4, n)


def cycle(d):
    n = 150
    k = d.comp("EX Cycle", n, "ecy"); lab_bg(k, n); light_bg(k, n)
    cx, cy, R = 960, 540, 300
    ring = k.ell("Cycle ring", cx, cy, 2 * R, 2 * R, None, f0=0, dur=n); ring.stroke(COL['grey'], 6)
    ring.set('strokeDasharray', '24px 16px')
    ring.rot([(0, 0.0, 'Linear'), (n, 45.0, 'Linear')])                 # turns clockwise, one way
    steps = [("Plan", COL['blue']), ("Make", COL['coral']), ("Test", COL['green']), ("Learn", COL['ink'])]
    for i, (lab, col) in enumerate(steps):
        a = math.radians(90 - i * 90)                                    # clockwise from 12 o'clock
        x, y = cx + R * math.cos(a), cy - R * math.sin(a)
        f = 6 + i * 14
        node = k.ell(f"Cycle node {i + 1}", x, y, 170, 170, col, f0=f, dur=n - f); pop(node, f)
        step_in(T(k, f"Cycle label {i + 1}", lab, x, y, 40, COL['white'], f + 4, n - f - 4, 'Bold', 'center'), f + 4)
    step_in(T(k, "Cycle centre", "repeat", cx, cy, 44, COL['muted'], 64, n - 64, 'Medium', 'center'), 64)


def build(path=None, m=None):
    d = Doc()
    lower_third(d); compare_columns(d); flow_diagram(d); key_term(d); checklist(d); venn(d); quiz(d); cycle(d)
    return d


if __name__ == "__main__":
    print(__doc__)
