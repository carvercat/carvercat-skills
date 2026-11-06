"""Write the Kinetic Typography lab comps into a .carverproj (direct project-file authoring).

Import and call build(path, m) - two passes, as saas_ui_lab.py:
  1. build(path, None) writes only a "KT Measure" comp of throwaway texts; read each
     text's bounds with carvercat_authoring mode:geometry -> m = {label: {x, y, w, h}}.
  2. build(path, m) writes the lab comps. Open the file (edit.open {path, force:true}),
     run mask.make + parent.clear for each MASKS pair, edit.save.
Check with carvercat_inspect (curves, lint) and carvercat_look; extract templates with
comp_to_template.py (--drop "Lab bg").

Docs: ai/patterns/kinetic-typography.md. Pixel space 1920x1080, y down; comp frames, 30 fps.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author"))
from cc import Doc, lin, P, BEZ

COL = dict(bg=lin('0B0B0F'), ink=lin('F4F1EA'), muted=lin('9A968E'), accent=lin('FF4D2E'), sun=lin('FFD23F'))
EXPO, ACCEL, BACK = BEZ['expo'], BEZ['accel'], BEZ['back']
FONT_STYLE = 'ExtraBold'
MASKS = []

SWAP_STATIC, SWAP_WORDS, SWAP_PX = "We build", ["faster", "smarter", "together"], 96


def lab_bg(k, n):
    k.rect("Lab bg", 0, 0, 1920, 1080, COL['bg'], f0=0, dur=n)


def measure(d):
    k = d.comp("KT Measure", 10, "ktm")
    for s in [SWAP_STATIC, SWAP_STATIC + " x"] + SWAP_WORDS + ["x"]:
        k.text(f"M {s}", s, 200, 540, SWAP_PX, COL['ink'], f0=0, dur=10, style=FONT_STYLE)


def word_swap(d, m):
    """A fixed phrase with a slot whose word rolls up to the next one, three times."""
    n, per, f0 = 120, 36, 10
    k = d.comp("KT Word swap", n, "kws"); lab_bg(k, n)
    st = m[f"M {SWAP_STATIC}"]
    # the slot starts where " x" puts its x, minus the x's own ink: static right edge + one space
    x_slot = m[f"M {SWAP_STATIC} x"]["x"] + m[f"M {SWAP_STATIC} x"]["w"] - m["M x"]["w"] - (m["M x"]["x"] - 200)
    widest = max(m[f"M {w}"]["w"] for w in SWAP_WORDS)
    total = (x_slot - 200) + widest
    x0 = 960 - total / 2                              # centre the longest phrase
    shift = x0 - 200
    y, line = 540, SWAP_PX * 1.25
    k.text("Static", SWAP_STATIC, x0, y, SWAP_PX, COL['ink'], f0=0, dur=n, style=FONT_STYLE)
    for i, w in enumerate(SWAP_WORDS):
        a = f0 + i * per
        last = i == len(SWAP_WORDS) - 1
        dur = (n - a) if last else per          # the exit ends as the next word starts: no two words share a frame
        o = k.text(f"Word {i + 1}", w, x_slot + shift, y, SWAP_PX, COL['accent'], f0=a, dur=dur, style=FONT_STYLE)
        bx, by = o.base
        ks = [(a, [bx, by - line / 1080], 'Linear'), (a + 12, [bx, by], EXPO)]
        if not last:
            ks += [(a + per - 8, [bx, by], 'Linear'), (a + per, [bx, by + line / 1080], ACCEL)]
        o.pos(ks)
        top = min(m[f"M {w}"]["y"] for w in SWAP_WORDS) - 6            # measured ink (incl. descenders) + 6 px
        bot = max(m[f"M {w}"]["y"] + m[f"M {w}"]["h"] for w in SWAP_WORDS) + 6
        k.rect(f"Window {i + 1}", x_slot + shift - 12, top, widest + 40, bot - top, COL['ink'], f0=a, dur=dur)
        MASKS.append(("KT Word swap", f"Word {i + 1}", f"Window {i + 1}"))


def impact_stack(d):
    n = 90
    k = d.comp("KT Impact stack", n, "kis"); lab_bg(k, n)
    lines = [("NO", 330, COL['ink']), ("MORE", 540, COL['ink']), ("BORING", 750, COL['accent'])]
    for i, (s, y, col) in enumerate(lines):
        f = i * 8
        o = k.text(f"Line {i + 1}", s, 960, y, 180, col, f0=f, dur=n - f, style=FONT_STYLE, align='center')
        o.scale([(f, 1.7, 'Linear'), (f + 10, 1.0, BACK)])
        o.op([(f, 0, 'Linear'), (f + 3, 1, 'Linear')])
    bar = k.rect("Underline", 960, 862, 520, 16, COL['sun'], f0=26, dur=n - 26, center=True)
    bar.anchor(-1, 0)
    bar.scale([(26, [0.0, 1.0], 'Linear'), (40, [1.0, 1.0], EXPO)])


def line_reveal(d):
    n = 60
    k = d.comp("KT Line reveal", n, "klr"); lab_bg(k, n)
    ly = 610
    rule = k.line("Rule", [(560, ly), (1360, ly)], COL['accent'], px=6, f0=0, dur=n)
    tp = rule.trim([(0, 0.5, 'Linear'), (14, 0.0, EXPO)], which='start')   # draws out from the centre
    rule.key(tp + '.end', [(0, 0.5, 'Linear'), (14, 1.0, EXPO)])
    head = k.text("Headline", "Launch day", 960, 520, 140, COL['ink'], f0=0, dur=n, style=FONT_STYLE, align='center')
    bx, by = head.base
    head.pos([(8, [bx, by - 180 / 1080], 'Linear'), (26, [bx, by], EXPO)])
    k.rect("Above the rule", 0, 300, 1920, ly - 3 - 300, COL['ink'], f0=0, dur=n)
    MASKS.append(("KT Line reveal", "Headline", "Above the rule"))
    sub = k.text("Subline", "October 27  ·  10:00", 960, 680, 40, COL['muted'], f0=18, dur=n - 18, style='Medium', align='center')
    sx, sy = sub.base
    sub.pos([(18, [sx, sy - 24 / 1080], 'Linear'), (32, [sx, sy], EXPO)])
    sub.op([(18, 0, 'Linear'), (26, 1, 'Ease out')])


def beat_words(d):
    n, per = 100, 25
    k = d.comp("KT Beat words", n, "kbw"); lab_bg(k, n)
    words = [("THINK", COL['ink']), ("BUILD", COL['accent']), ("SHIP", COL['ink']), ("REPEAT", COL['sun'])]
    for i, (w, col) in enumerate(words):
        f = i * per
        o = k.text(f"Beat {i + 1}", w, 960, 540, 220, col, f0=f, dur=per, style=FONT_STYLE, align='center')
        o.scale([(f, 1.35, 'Linear'), (f + 8, 1.0, EXPO)])   # a hard cut in, no fade: readable for all 25 f


def focus_pull(d):
    n = 60
    k = d.comp("KT Focus pull", n, "kfp"); lab_bg(k, n)
    t = k.text("Title", "Into focus", 960, 540, 150, COL['ink'], f0=0, dur=n, style=FONT_STYLE, align='center')
    t.stagger(0, by='character', gap=2, dy=0.0, d=18, blur=24)
    tr = t.src('text_font', 'tracking')
    t.key(tr, [(0, 1.6, 'Linear'), (30, 1.0, EXPO), (n, 1.06, 'Linear')])


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    MASKS.clear()
    if m is None:
        measure(d)
    else:
        word_swap(d, m); impact_stack(d); line_reveal(d); beat_words(d); focus_pull(d)
    d.save()
    return [], MASKS


if __name__ == "__main__":
    print(__doc__)
