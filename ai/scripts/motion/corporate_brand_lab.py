"""The Corporate Brand lab comps in design units (cc2.py: px, y down, degrees clockwise, CSS colours and easing).

    import corporate_brand_lab as L; doc = L.build(); doc.send(client, PROJECT.carverproj)   # scene.apply per comp, then edit.save

Four comps: title card, lower third, logo resolve, three stats. The pack's moves (Soft rise, Card settle, Soft fade out, Photo push)
are written as plain keys by corporate_luxury_kit.py, and the masks are scene masks (a `mask` style key on the content that points
at its window), so nothing is applied after `send`. Check with carvercat_inspect and carvercat_look; templates are extracted with
regen_pack.py. Docs: ai/patterns/corporate-brand.md. Design units: px from the top-left, y down; comp frames, 30 fps.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corporate_luxury_kit import EASE_OUT
from corporate_luxury_kit import (Doc, css, BEZ, text, line, grow, soft_rise, card_settle, soft_out, push)

COL = dict(navy=css('0B1F3A'), white=css('FFFFFF'), light=css('F3F5F8'), teal=css('00A3A1'), grey=css('8A94A6'),
           ink=css('0B1F3A'), navy2=css('163A63'))
EXPO, DECEL = BEZ['expo'], BEZ['decel']


def lab_bg(k, n, col=None):
    k.rect("Lab bg", 0, 0, 1920, 1080, col or COL['navy'], f0=0, dur=n)


def fade_all(objs, n):
    for o in objs: soft_out(o, n)


def title_card(d):
    n = 90
    k = d.comp("CB Title card", n, "ctc"); lab_bg(k, n)
    cx, cy = 960, 540
    rule = k.rect("Rule", cx, cy, 4, 168, COL['teal'], f0=0, dur=n, center=True)
    rule.scale([(0, [1.0, 0.0], 'Linear'), (14, [1.0, 1.0], EXPO)])
    t = text(k, "Title", "Annual Report", cx - 32, cy - 22, 64, COL['white'], f0=0, dur=n, style='SemiBold', align='right')
    tx, ty = t.base
    t.pos([(8, (tx + 480, ty), 'Linear'), (30, (tx, ty), EXPO)])   # starts wholly behind the rule (masked), slides out left
    yr = text(k, "Year", "2026", cx - 32, cy + 48, 40, COL['teal'], f0=0, dur=n, style='SemiBold', align='right')   # 8 px lower: the audit (2026-10-28) measured an 11 px gap to the title
    yx, yy = yr.base
    yr.pos([(12, (yx + 160, yy), 'Linear'), (34, (yx, yy), EXPO)])
    # the subtitle starts once the title has nearly landed, so their boxes never overlap (lint is mask-blind)
    s = text(k, "Subtitle", "Growth, focus, people", cx + 32, cy, 40, COL['grey'], f0=18, dur=n - 18, style='Regular')
    sx, sy = s.base
    s.pos([(18, (sx - 20, sy), 'Linear'), (40, (sx, sy), EXPO)])
    s.op([(18, 0, 'Linear'), (30, 1, EASE_OUT)])
    lw = k.rect("Left window", 0, cy - 120, cx - 6, 240, COL['white'], f0=0, dur=n)
    lw2 = k.rect("Left window 2", 0, cy - 120, cx - 6, 240, COL['white'], f0=0, dur=n)
    rw = k.rect("Right window", cx + 6, cy - 120, 1920 - cx - 6, 240, COL['white'], f0=18, dur=n - 18)
    k.mask(t, lw); k.mask(yr, lw2); k.mask(s, rw)


def lower_third(d, bg=True):
    n = 150
    k = d.comp("CB Lower third", n, "clt")
    if bg: lab_bg(k, n, COL['navy2'])
    x0, y1, w1, h1 = 120, 836, 560, 76
    y2, w2, h2 = y1 + h1, 420, 52
    b1 = k.rect("Name box", x0 + w1 / 2, y1 + h1 / 2, w1, h1, COL['white'], f0=0, dur=n, center=True)
    grow(b1, 0, 14)
    b2 = k.rect("Role box", x0 + w2 / 2, y2 + h2 / 2, w2, h2, COL['teal'], f0=6, dur=n - 6, center=True)
    grow(b2, 6, 14)
    nm = text(k, "Name", "Dana Okafor", x0 + 28, y1 + h1 / 2, 40, COL['ink'], f0=0, dur=n, style='SemiBold')
    nx, ny = nm.base
    nm.pos([(4, (nx - 60, ny), 'Linear'), (22, (nx, ny), EXPO)])
    rl = text(k, "Role", "Head of Operations", x0 + 28, y2 + h2 / 2, 26, COL['white'], f0=6, dur=n - 6, style='Medium')
    rx, ry = rl.base
    rl.pos([(10, (rx - 60, ry), 'Linear'), (28, (rx, ry), EXPO)])
    wins = []
    for name, y, w, h, f in (("Name window", y1, w1, h1, 0), ("Role window", y2, w2, h2, 6)):
        win = k.rect(name, x0 + w / 2, y + h / 2, w, h, COL['white'], f0=f, dur=n - f, center=True)
        grow(win, f, 14)   # grows with its box
        wins.append(win)
    k.mask(nm, wins[0]); k.mask(rl, wins[1])
    fade_all([b1, b2, nm, rl], n)


def logo_resolve(d):
    n = 90
    k = d.comp("CB Logo resolve", n, "clr"); lab_bg(k, n)
    cx, cy, s = 960, 470, 240
    l, r, t, b = cx - s / 2, cx + s / 2, cy - s / 2, cy + s / 2
    sides = [("Frame top", [(l, t), (r, t)]), ("Frame right", [(r, t), (r, b)]),
             ("Frame bottom", [(r, b), (l, b)]), ("Frame left", [(l, b), (l, t)])]
    for i, (name, pts) in enumerate(sides):
        o = line(k, name, pts, COL['teal'], 4, f0=0, dur=n)
        f = i * 4
        o.trim([(f, 0.0, 'Linear'), (f + 14, 1.0, EXPO)], which='end')
    card_settle(k.ell("Mark", cx, cy, 120, 120, COL['white'], f0=18, dur=n - 18), 18)
    soft_rise(text(k, "Wordmark", "NORTHWIND", cx, cy + 210, 56, COL['white'], f0=26, dur=n - 26, style='SemiBold', align='center', track=1.25), 26)
    soft_rise(text(k, "Tagline", "Built to last", cx, cy + 280, 30, COL['grey'], f0=34, dur=n - 34, style='Regular', align='center'), 34)


def three_stats(d):
    n = 90
    k = d.comp("CB Three stats", n, "cts"); lab_bg(k, n, COL['light'])
    stats = [("38%", "lower energy use"), ("12", "new markets"), ("4.9", "customer rating")]
    for i, (num, lab) in enumerate(stats):
        x = 480 + i * 480; f = i * 6
        rule = line(k, f"Rule {i + 1}", [(x - 100, 400), (x + 100, 400)], COL['teal'], 4, f0=0, dur=n)
        rule.trim([(f, 0.0, 'Linear'), (f + 14, 1.0, EXPO)], which='end')
        card_settle(text(k, f"Number {i + 1}", num, x, 490, 96, COL['ink'], f0=f + 6, dur=n - f - 6, style='Bold', align='center'), f + 6)
        soft_rise(text(k, f"Label {i + 1}", lab, x, 580, 30, COL['grey'], f0=f + 10, dur=n - f - 10, style='Medium', align='center'), f + 10)


def build():
    d = Doc()
    title_card(d); lower_third(d); logo_resolve(d); three_stats(d)
    return d


if __name__ == "__main__":
    print(__doc__)
