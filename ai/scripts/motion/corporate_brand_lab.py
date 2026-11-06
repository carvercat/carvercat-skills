"""Write the Corporate Brand lab comps into a .carverproj (direct project-file authoring).

    import corporate_brand_lab as L; presets, masks = L.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); for each MASKS
pair (content, window) run mask.make {ids:[window, content]} - the FIRST id is the mask -
then parent.clear with the same ids; edit.save. Check with carvercat_inspect and
carvercat_look; extract templates with comp_to_template.py (--drop "Lab bg").

Docs: ai/patterns/corporate-brand.md. Pixel space 1920x1080, y down; comp frames, 30 fps.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author"))
from cc import Doc, lin, P, BEZ

COL = dict(navy=lin('0B1F3A'), white=lin('FFFFFF'), light=lin('F3F5F8'), teal=lin('00A3A1'), grey=lin('8A94A6'),
           ink=lin('0B1F3A'), navy2=lin('163A63'))
EXPO, DECEL = BEZ['expo'], BEZ['decel']
PRESETS, MASKS = [], []


def lab_bg(k, n, col=None):
    k.rect("Lab bg", 0, 0, 1920, 1080, col or COL['navy'], f0=0, dur=n)


def title_card(d):
    n = 90
    k = d.comp("CB Title card", n, "ctc"); lab_bg(k, n)
    cx, cy = 960, 540
    rule = k.rect("Rule", cx, cy, 4, 168, COL['teal'], f0=0, dur=n, center=True)
    rule.scale([(0, [1.0, 0.0], 'Linear'), (14, [1.0, 1.0], EXPO)])
    t = k.text("Title", "Annual Report", cx - 32, cy - 22, 64, COL['white'], f0=0, dur=n, style='SemiBold', align='right')
    tx, ty = t.base
    t.pos([(8, [tx + 480 / 1920, ty], 'Linear'), (30, [tx, ty], EXPO)])   # starts wholly behind the rule (masked), slides out left
    yr = k.text("Year", "2026", cx - 32, cy + 48, 40,   # 8 px lower: the audit (2026-10-28) measured an 11 px gap to the title
                COL['teal'], f0=0, dur=n, style='SemiBold', align='right')
    yx, yy = yr.base
    yr.pos([(12, [yx + 160 / 1920, yy], 'Linear'), (34, [yx, yy], EXPO)])
    # the subtitle starts once the title has nearly landed, so their boxes never overlap (lint is mask-blind)
    s = k.text("Subtitle", "Growth, focus, people", cx + 32, cy, 40, COL['grey'], f0=18, dur=n - 18, style='Regular')
    sx, sy = s.base
    s.pos([(18, [sx - 20 / 1920, sy], 'Linear'), (40, [sx, sy], EXPO)])
    s.op([(18, 0, 'Linear'), (30, 1, 'Ease out')])
    k.rect("Left window", 0, cy - 120, cx - 6, 240, COL['white'], f0=0, dur=n)
    k.rect("Left window 2", 0, cy - 120, cx - 6, 240, COL['white'], f0=0, dur=n)
    k.rect("Right window", cx + 6, cy - 120, 1920 - cx - 6, 240, COL['white'], f0=18, dur=n - 18)
    MASKS.extend([("CB Title card", "Title", "Left window"), ("CB Title card", "Year", "Left window 2"),
                  ("CB Title card", "Subtitle", "Right window")])


def lower_third(d, bg=True):
    n = 150
    k = d.comp("CB Lower third", n, "clt")
    if bg: lab_bg(k, n, COL['navy2'])
    x0, y1, w1, h1 = 120, 836, 560, 76
    y2, w2, h2 = y1 + h1, 420, 52
    b1 = k.rect("Name box", x0 + w1 / 2, y1 + h1 / 2, w1, h1, COL['white'], f0=0, dur=n, center=True)
    b1.anchor(-1, 0); b1.scale([(0, [0.0, 1.0], 'Linear'), (14, [1.0, 1.0], EXPO)])
    b2 = k.rect("Role box", x0 + w2 / 2, y2 + h2 / 2, w2, h2, COL['teal'], f0=6, dur=n - 6, center=True)
    b2.anchor(-1, 0); b2.scale([(6, [0.0, 1.0], 'Linear'), (20, [1.0, 1.0], EXPO)])
    nm = k.text("Name", "Dana Okafor", x0 + 28, y1 + h1 / 2, 40, COL['ink'], f0=0, dur=n, style='SemiBold')
    nx, ny = nm.base
    nm.pos([(4, [nx - 60 / 1920, ny], 'Linear'), (22, [nx, ny], EXPO)])
    rl = k.text("Role", "Head of Operations", x0 + 28, y2 + h2 / 2, 26, COL['white'], f0=6, dur=n - 6, style='Medium')
    rx, ry = rl.base
    rl.pos([(10, [rx - 60 / 1920, ry], 'Linear'), (28, [rx, ry], EXPO)])
    for name, box, y, w, h, f in (("Name window", b1, y1, w1, h1, 0), ("Role window", b2, y2, w2, h2, 6)):
        win = k.rect(name, x0 + w / 2, y + h / 2, w, h, COL['white'], f0=f, dur=n - f, center=True)
        win.anchor(-1, 0); win.scale([(f, [0.0, 1.0], 'Linear'), (f + 14, [1.0, 1.0], EXPO)])   # grows with its box
    MASKS.extend([("CB Lower third", "Name", "Name window"), ("CB Lower third", "Role", "Role window")])
    for o in ("Name box", "Role box", "Name", "Role"):
        PRESETS.append(("CB Lower third", o, "Soft fade out"))


def logo_resolve(d):
    n = 90
    k = d.comp("CB Logo resolve", n, "clr"); lab_bg(k, n)
    cx, cy, s = 960, 470, 240
    l, r, t, b = cx - s / 2, cx + s / 2, cy - s / 2, cy + s / 2
    sides = [("Frame top", [(l, t), (r, t)]), ("Frame right", [(r, t), (r, b)]),
             ("Frame bottom", [(r, b), (l, b)]), ("Frame left", [(l, b), (l, t)])]
    for i, (name, pts) in enumerate(sides):
        o = k.line(name, pts, COL['teal'], px=4, f0=0, dur=n)
        f = i * 4
        o.trim([(f, 0.0, 'Linear'), (f + 14, 1.0, EXPO)], which='end')
    mark = k.ell("Mark", cx, cy, 120, 120, COL['white'], f0=18, dur=n - 18)
    PRESETS.append(("CB Logo resolve", "Mark", "Card settle"))
    k.text("Wordmark", "NORTHWIND", cx, cy + 210, 56, COL['white'], f0=26, dur=n - 26, style='SemiBold', align='center', track=1.25)
    PRESETS.append(("CB Logo resolve", "Wordmark", "Soft rise"))
    k.text("Tagline", "Built to last", cx, cy + 280, 30, COL['grey'], f0=34, dur=n - 34, style='Regular', align='center')
    PRESETS.append(("CB Logo resolve", "Tagline", "Soft rise"))


def three_stats(d):
    n = 90
    k = d.comp("CB Three stats", n, "cts"); lab_bg(k, n, COL['light'])
    stats = [("38%", "lower energy use"), ("12", "new markets"), ("4.9", "customer rating")]
    for i, (num, lab) in enumerate(stats):
        x = 480 + i * 480; f = i * 6
        rule = k.line(f"Rule {i + 1}", [(x - 100, 400), (x + 100, 400)], COL['teal'], px=4, f0=0, dur=n)
        rule.trim([(f, 0.0, 'Linear'), (f + 14, 1.0, EXPO)], which='end')
        k.text(f"Number {i + 1}", num, x, 490, 96, COL['ink'], f0=f + 6, dur=n - f - 6, style='Bold', align='center')
        PRESETS.append(("CB Three stats", f"Number {i + 1}", "Card settle"))
        k.text(f"Label {i + 1}", lab, x, 580, 30, COL['grey'], f0=f + 10, dur=n - f - 10, style='Medium', align='center')
        PRESETS.append(("CB Three stats", f"Label {i + 1}", "Soft rise"))


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    title_card(d); lower_third(d); logo_resolve(d); three_stats(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
