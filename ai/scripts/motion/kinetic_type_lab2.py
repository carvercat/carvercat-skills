"""Kinetic Typography round 2: seven more lab comps (lower third, split title, highlight
sweep, quote card, stat punch, numbered list, end card), written straight into a .carverproj.

    import kinetic_type_lab2 as L; presets, masks = L.build(PROJECT.carverproj)

Same palette and verification as kinetic_type_lab.py. After writing: edit.open {path,
force:true}; apply PRESETS (preset.apply; they come from this pack and Motion Patterns);
edit.save; check with carvercat_inspect and carvercat_look; extract templates with
comp_to_template.py (--drop "Lab bg"). Word positions come from cc.textw (Rethink Sans
advance widths, within about 1% of Carvercat). Docs: ai/patterns/kinetic-typography.md.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author"))
from kinetic_type_lab import Doc, lin, COL, EXPO, ACCEL, BACK, FONT_STYLE, lab_bg
from cc import textw

PRESETS, MASKS = [], []


def lower_third(d):
    n = 150
    k = d.comp("KT Lower third", n, "klt"); lab_bg(k, n)
    bar = k.rect("Accent bar", 120, 800, 14, 166, COL['accent'], f0=0, dur=n)
    bar.anchor(0, 1)                                                       # grows down from its top edge
    bar.scale([(0, [1.0, 0.0], 'Linear'), (12, [1.0, 1.0], EXPO), (n - 10, [1.0, 1.0], 'Linear'), (n, [1.0, 0.0], ACCEL)])
    k.text("Name", "MAYA ORTIZ", 166, 840, 76, COL['ink'], f0=4, dur=n - 4, style=FONT_STYLE)
    PRESETS.append(("KT Lower third", "Name", "Letters zoom in"))
    PRESETS.append(("KT Lower third", "Name", "Exit down - accelerate"))   # a second staggered preset is refused (one Stagger per text)
    k.text("Role", "Creative director, Northwind", 166, 936, 36, COL['muted'], f0=12, dur=n - 12, style='Medium')
    PRESETS.append(("KT Lower third", "Role", "Lines slide in - left"))
    PRESETS.append(("KT Lower third", "Role", "Exit fade - fast"))


def split_title(d):
    n = 90
    k = d.comp("KT Split title", n, "kst"); lab_bg(k, n)
    for i, (s, y, col, dx, f) in enumerate([("MAKE IT", 450, COL['ink'], -360, 0), ("MOVE", 650, COL['accent'], 360, 4)]):
        o = k.text(f"Line {i + 1}", s, 960, y, 190, col, f0=f, dur=n - f, style=FONT_STYLE, align='center')
        bx, by = o.base
        o.pos([(f, [bx + dx / 1920, by], 'Linear'), (f + 16, [bx, by], EXPO)])
        o.op([(f, 0, 'Linear'), (f + 4, 1, 'Linear')])
    dot = k.ell("Dot", 960 + textw("MOVE", 190, FONT_STYLE) / 2 + 40, 690, 36, None, COL['sun'], f0=18, dur=n - 18)
    PRESETS.append(("KT Split title", "Dot", "Pop - spring"))


HL_PX = 96
HL_PARTS = ["Design that", "actually", "ships."]


def highlight_sweep(d):
    n = 90
    k = d.comp("KT Highlight sweep", n, "khs"); lab_bg(k, n)
    sp = textw(" ", HL_PX, FONT_STYLE)
    ws = [textw(s, HL_PX, FONT_STYLE) for s in HL_PARTS]
    x0 = 960 - (sum(ws) + 2 * sp) / 2
    xs = [x0, x0 + ws[0] + sp, x0 + ws[0] + ws[1] + 2 * sp]
    y = 540
    hl = k.rect("Highlight", xs[1] - 14, y - HL_PX * 0.6, ws[1] + 28, HL_PX * 1.1, COL['sun'], f0=14, dur=n - 14)
    hl.anchor(-1, 0)
    hl.scale([(14, [0.0, 1.0], 'Linear'), (26, [1.0, 1.0], EXPO)])        # wipes in left to right behind the word
    for i, (s, x) in enumerate(zip(HL_PARTS, xs)):
        f = [0, 18, 6][i]
        col = COL['bg'] if i == 1 else COL['ink']
        k.text(f"Part {i + 1}", s, x, y, HL_PX, col, f0=f, dur=n - f, style=FONT_STYLE)
        PRESETS.append(("KT Highlight sweep", f"Part {i + 1}", "Words rise - expo"))


def quote_card(d):
    n = 150
    k = d.comp("KT Quote", n, "kqt"); lab_bg(k, n)
    k.text("Quote mark", "“", 360, 330, 320, COL['accent'], f0=0, dur=n, style=FONT_STYLE)
    PRESETS.append(("KT Quote", "Quote mark", "Stamp"))   # a pop from 0 reads as 7 px text: lint text_too_small
    k.text("Quote", "We cut our edit time\nin half the first week.", 400, 520, 84, COL['ink'], f0=8, dur=n - 8,
           style=FONT_STYLE, lh=1.1)
    PRESETS.append(("KT Quote", "Quote", "Words rise - expo"))
    k.text("Attribution", "Head of video, Northwind", 400, 760, 38, COL['muted'], f0=46, dur=n - 46, style='Medium')
    PRESETS.append(("KT Quote", "Attribution", "Lines slide in - left"))


def stat_punch(d):
    n = 90
    k = d.comp("KT Stat punch", n, "ksp"); lab_bg(k, n)
    ring = k.ell("Ring", 960, 470, 520, None, None, f0=0, dur=n)
    ring.stroke(COL['accent'], px=12); ring.rotv(90.0)                     # stroke starts at 12 o'clock
    ring.trim([(4, 0.0, 'Linear'), (34, 1.0, EXPO)])
    k.text("Number", "3x", 960, 470, 300, COL['ink'], f0=2, dur=n - 2, style=FONT_STYLE, align='center')
    PRESETS.append(("KT Stat punch", "Number", "Words slam"))
    k.text("Label", "faster renders", 960, 800, 64, COL['ink'], f0=16, dur=n - 16, style=FONT_STYLE, align='center')
    PRESETS.append(("KT Stat punch", "Label", "Words rise - expo"))


def numbered_list(d):
    n = 120
    k = d.comp("KT Numbered list", n, "knl"); lab_bg(k, n)
    k.text("List title", "THREE RULES", 360, 260, 84, COL['ink'], f0=0, dur=n, style=FONT_STYLE)
    PRESETS.append(("KT Numbered list", "List title", "Letters zoom in"))
    rule = k.rect("Title rule", 360, 320, 200, 10, COL['accent'], f0=8, dur=n - 8)
    rule.anchor(-1, 0); rule.scale([(8, [0.0, 1.0], 'Linear'), (22, [1.0, 1.0], EXPO)])
    for i, s in enumerate(["Keep it short", "Say one thing", "End on the action"]):
        f, y = 16 + i * 12, 450 + i * 130
        k.text(f"Number {i + 1}", f"0{i + 1}", 360, y, 64, COL['accent'], f0=f, dur=n - f, style=FONT_STYLE)
        PRESETS.append(("KT Numbered list", f"Number {i + 1}", "Letters zoom in"))
        k.text(f"Item {i + 1}", s, 500, y, 64, COL['ink'], f0=f + 3, dur=n - f - 3, style=FONT_STYLE)
        PRESETS.append(("KT Numbered list", f"Item {i + 1}", "Words rise - expo"))


def end_card(d):
    n = 120
    k = d.comp("KT End card", n, "kec"); lab_bg(k, n)
    k.text("Call", "FOLLOW FOR MORE", 960, 470, 150, COL['ink'], f0=0, dur=n, style=FONT_STYLE, align='center')
    PRESETS.append(("KT End card", "Call", "Words slam"))
    bar = k.rect("Handle bar", 960, 640, 640, 92, COL['accent'], f0=18, dur=n - 18, center=True)
    bar.scale([(18, [0.0, 1.0], 'Linear'), (30, [1.0, 1.0], EXPO)])     # opens from its centre
    k.text("Handle", "@northwind.studio", 960, 640, 52, COL['ink'], f0=24, dur=n - 24, style=FONT_STYLE, align='center')
    PRESETS.append(("KT End card", "Handle", "Letters shimmer in"))


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    lower_third(d); split_title(d); highlight_sweep(d); quote_card(d); stat_punch(d); numbered_list(d); end_card(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
