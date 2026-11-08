"""Kinetic Typography round 2 in design units: seven more lab comps (lower third, split title, highlight sweep, quote card, stat punch,
numbered list, end card).

    import kinetic_type_lab2 as L; doc = L.build(); doc.send(client, PROJECT.carverproj)

Same palette and kit as kinetic_type_lab.py: the stored presets (Letters zoom in, Words rise, Lines slide in, Words slam, Letters
shimmer in, Stamp, Pop - spring and the exits) are baked as keys or as a text stagger's tween, so no preset is applied afterwards.
Where a text staggers and also exits (the lower third), the exit rides in the stagger tween: a staggered text cannot carry keys
of its own in a scene, so the letters leave in the same order they came, one frame apart. Word positions come from
explainer_lab.textw (Rethink Sans advance widths, within about 1 % of Carvercat). Docs: ai/patterns/kinetic-typography.md.
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kinetic_type_lab import (KDoc, COL, EXPO, ACCEL, BACK, STD, FONT_STYLE, lab_bg, KT, textw, origin, fade, rise, slam, stamp, pop_spring,
                              exit_fade, staggered, tween_letters_zoom, tween_lines_left, tween_words_rise, tween_words_slam, shimmer, W, H)


def lower_third(d):
    n = 150
    k = d.comp("KT Lower third", n, "klt"); lab_bg(k, n)
    bar = k.rect("Accent bar", 120, 800, 14, 166, COL['accent'], f0=0, dur=n)
    origin(bar, 0, 1)                                                       # grows down from its top edge
    bar.scale([(0, [1.0, 0.0], 'Linear'), (12, [1.0, 1.0], EXPO), (n - 10, [1.0, 1.0], 'Linear'), (n, [1.0, 0.0], ACCEL)])
    # name: letters zoom in; the exit down is the whole name's
    name = KT(k, "Name", "MAYA ORTIZ", 166, 840, 76, COL['ink'], 4, n - 4)
    by, each, rows = tween_letters_zoom()
    dur = n - 4
    rows = rows + [(16, dict(dy=0), 'linear')]
    staggered(name, by, each, rows)
    acc = 'cubic-bezier(%s)' % ', '.join('%g' % v for v in ACCEL)
    y0 = round(name.box[1] - name.box[3] / 2, 3)
    # the exit is the whole name's (as v1): 54 px down on an accelerate over the last 12 f, faded over the last 8
    # (own keys beside the stagger, keyed after the apply)
    d.post.append(("KT Lower third", "Name", lambda c, i, dur=dur, acc=acc: c.run('anim.set', id=i, keyframes=[
        dict(at=dur - 13, ease=acc, y=y0), dict(at=dur - 9, ease=acc, opacity=1.0),
        dict(at=dur - 1, y=round(y0 + 54, 3), opacity=0.0)])))
    role = KT(k, "Role", "Creative director, Northwind", 166, 936, 36, COL['muted'], 12, n - 12, 'Medium')
    by, each, rows = tween_lines_left()
    dur = n - 12
    rows = rows + [(dur - 1 - 8, dict(opacity=1.0), ACCEL), (dur - 1, dict(opacity=0.0), 'linear')]
    staggered(role, by, each, rows)


def split_title(d):
    n = 90
    k = d.comp("KT Split title", n, "kst"); lab_bg(k, n)
    for i, (s, y, col, dx, f) in enumerate([("MAKE IT", 450, COL['ink'], -360, 0), ("MOVE", 650, COL['accent'], 360, 4)]):
        o = KT(k, f"Line {i + 1}", s, 960, y, 190, col, f, n - f, align='center')
        bx, by = o.base
        o.pos([(f, (bx + dx, by), 'Linear'), (f + 16, (bx, by), EXPO)])
        o.op([(f, 0, 'Linear'), (f + 4, 1, 'Linear')])
    dot = k.ell("Dot", 960 + textw("MOVE", 190, FONT_STYLE) / 2 + 40, 690, 36, None, COL['sun'], f0=18, dur=n - 18)
    pop_spring(dot, 18)


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
    origin(hl, -1, 0)
    hl.scale([(14, [0.0, 1.0], 'Linear'), (26, [1.0, 1.0], EXPO)])        # wipes in left to right behind the word
    for i, (s, x) in enumerate(zip(HL_PARTS, xs)):
        f = [0, 18, 6][i]
        o = KT(k, f"Part {i + 1}", s, x, y, HL_PX, COL['bg'] if i == 1 else COL['ink'], f, n - f)
        staggered(o, *tween_words_rise())


def quote_card(d):
    n = 150
    k = d.comp("KT Quote", n, "kqt"); lab_bg(k, n)
    q = KT(k, "Quote mark", "“", 360, 330, 320, COL['accent'], 0, n)
    stamp(q, 0)                                                            # a pop from 0 reads as 7 px text: lint text_too_small
    quote = KT(k, "Quote", "We cut our edit time\nin half the first week.", 400, 520, 84, COL['ink'], 8, n - 8, lh=1.1)
    staggered(quote, *tween_words_rise())
    att = KT(k, "Attribution", "Head of video, Northwind", 400, 760, 38, COL['muted'], 46, n - 46, 'Medium')
    staggered(att, *tween_lines_left())


def stat_punch(d):
    n = 90
    k = d.comp("KT Stat punch", n, "ksp"); lab_bg(k, n)
    ring = k.ell("Ring", 960, 470, 520, None, None, f0=0, dur=n)
    ring.stroke(COL['accent'], px=12); ring.rotv(-90.0)                    # the stroke starts at 3 o'clock: turn it to 12
    ring.trim([(4, 0.0, 'Linear'), (34, 1.0, EXPO)])
    num = KT(k, "Number", "3x", 960, 470, 300, COL['ink'], 2, n - 2, align='center')
    staggered(num, *tween_words_slam())
    lab = KT(k, "Label", "faster renders", 960, 800, 64, COL['ink'], 16, n - 16, align='center')
    staggered(lab, *tween_words_rise())


def numbered_list(d):
    n = 120
    k = d.comp("KT Numbered list", n, "knl"); lab_bg(k, n)
    staggered(KT(k, "List title", "THREE RULES", 360, 260, 84, COL['ink'], 0, n), *tween_letters_zoom())
    rule = k.rect("Title rule", 360, 320, 200, 10, COL['accent'], f0=8, dur=n - 8)
    origin(rule, -1, 0); rule.scale([(8, [0.0, 1.0], 'Linear'), (22, [1.0, 1.0], EXPO)])
    for i, s in enumerate(["Keep it short", "Say one thing", "End on the action"]):
        f, y = 16 + i * 12, 450 + i * 130
        staggered(KT(k, f"Number {i + 1}", f"0{i + 1}", 360, y, 64, COL['accent'], f, n - f), *tween_letters_zoom())
        staggered(KT(k, f"Item {i + 1}", s, 500, y, 64, COL['ink'], f + 3, n - f - 3), *tween_words_rise())


def end_card(d):
    n = 120
    k = d.comp("KT End card", n, "kec"); lab_bg(k, n)
    staggered(KT(k, "Call", "FOLLOW FOR MORE", 960, 470, 150, COL['ink'], 0, n, align='center'), *tween_words_slam())
    bar = k.rect("Handle bar", 960, 640, 640, 92, COL['accent'], f0=18, dur=n - 18, center=True)
    bar.scale([(18, [0.0, 1.0], 'Linear'), (30, [1.0, 1.0], EXPO)])     # opens from its centre
    shimmer(KT(k, "Handle", "@northwind.studio", 960, 640, 52, COL['ink'], 24, n - 24, align='center'))


def build(path=None, m=None):
    d = KDoc()
    lower_third(d); split_title(d); highlight_sweep(d); quote_card(d); stat_punch(d); numbered_list(d); end_card(d)
    return d


if __name__ == "__main__":
    print(__doc__)
