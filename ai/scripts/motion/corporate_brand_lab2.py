"""Corporate Brand round 2 in design units: eight lab comps (chapter title, quote, end card, agenda, team row, split screen,
leader callout, brand panel wipe).

    import corporate_brand_lab2 as L; doc = L.build(); doc.send(client, PROJECT.carverproj)

Same palette, style rules and checks as corporate_brand_lab.py: standard and decelerate curves only, no springs or overshoot.
The pack's moves are plain keys (corporate_luxury_kit.py), so nothing is applied after `send`. Check with carvercat_inspect and
carvercat_look; templates are extracted with regen_pack.py. Docs: ai/patterns/corporate-brand.md.
Design units: px from the top-left, y down; comp frames, 30 fps.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corporate_luxury_kit import EASE_OUT
from corporate_luxury_kit import (Doc, css, BEZ, text, line, grow, soft_rise, card_settle, soft_out, push)
from corporate_brand_lab import COL, EXPO, DECEL, lab_bg, fade_all

ACCEL = BEZ['accel']
PORTRAIT = css('C9D1DC')


def chapter_title(d):
    n = 90
    k = d.comp("CB Chapter title", n, "cch"); lab_bg(k, n)
    soft_rise(text(k, "Chapter number", "01", 240, 430, 120, COL['teal'], f0=0, dur=n, style='SemiBold'), 0)
    grow(k.rect("Chapter rule", 240, 520, 1100, 3, COL['grey'], f0=6, dur=n - 6), 6, 24)
    soft_rise(text(k, "Chapter name", "Our mission", 240, 610, 88, COL['white'], f0=12, dur=n - 12, style='SemiBold'), 12)
    soft_rise(text(k, "Chapter note", "Why we build what we build", 240, 690, 34, COL['grey'], f0=20, dur=n - 20, style='Regular'), 20)


def quote(d):
    n = 150
    k = d.comp("CB Quote", n, "cqt"); lab_bg(k, n)
    bar = k.rect("Quote bar", 300, 380, 6, 260, COL['teal'], f0=0, dur=n)
    grow(bar, 0, 20, DECEL, edge='top')   # draws down from its top
    q = soft_rise(text(k, "Quote", "Good infrastructure is the kind\nnobody has to think about.", 360, 450, 64, COL['white'], f0=8, dur=n - 8,
                       style='SemiBold', lh=1.15), 8)
    sp = soft_rise(text(k, "Speaker", "Dana Okafor", 360, 610, 34, COL['teal'], f0=26, dur=n - 26, style='SemiBold'), 26)
    sr = soft_rise(text(k, "Speaker role", "Head of Operations, Northwind", 360, 656, 28, COL['grey'], f0=30, dur=n - 30, style='Regular'), 30)
    fade_all([bar, q, sp, sr], n)


def end_card(d):
    n = 120
    k = d.comp("CB End card", n, "cec"); lab_bg(k, n); k.rect("Light background", 0, 0, 1920, 1080, COL['light'], f0=0, dur=n)   # kept in the template
    card_settle(k.rect("Mark outer", 960, 380, 120, 120, COL['navy'], r=24, f0=0, dur=n, center=True), 0)
    card_settle(k.rect("Mark inner", 960, 380, 48, 48, COL['teal'], r=10, f0=6, dur=n - 6, center=True), 6)
    soft_rise(text(k, "Wordmark", "NORTHWIND", 960, 510, 60, COL['ink'], f0=12, dur=n - 12, style='SemiBold', align='center', track=1.25), 12)
    grow(k.rect("End rule", 860, 570, 200, 3, COL['teal'], f0=20, dur=n - 20), 20, 20)
    soft_rise(text(k, "URL", "northwind.com", 960, 630, 34, COL['grey'], f0=26, dur=n - 26, style='Medium', align='center'), 26)


def agenda(d):
    n = 150
    k = d.comp("CB Agenda", n, "cag"); lab_bg(k, n)
    soft_rise(text(k, "Agenda title", "Agenda", 300, 260, 64, COL['white'], f0=0, dur=n, style='SemiBold'), 0)
    items = ["The year in numbers", "Our people", "New markets", "What comes next"]
    ind = k.rect("Active marker", 300, 420, 8, 64, COL['teal'], f0=24, dur=n - 24, center=True)
    ind.op([(24, 0, 'Linear'), (36, 1, EASE_OUT)])
    bx, by = ind.base
    ind.pos([(60, (bx, by), 'Linear'), (78, (bx, by + 100), DECEL)])     # moves to item 2
    for i, s in enumerate(items):
        y, f = 420 + i * 100, 8 + i * 5
        soft_rise(text(k, f"Number {i + 1}", f"0{i + 1}", 340, y, 40, COL['teal'], f0=f, dur=n - f, style='SemiBold'), f)
        soft_rise(text(k, f"Item {i + 1}", s, 430, y, 40, COL['white'] if i == 1 else COL['grey'], f0=f, dur=n - f, style='Medium'), f)


def team_row(d):
    n = 120
    k = d.comp("CB Team row", n, "ctm"); lab_bg(k, n); k.rect("Light background", 0, 0, 1920, 1080, COL['light'], f0=0, dur=n)   # kept in the template
    people = [("Dana Okafor", "Operations"), ("Lee Varga", "Engineering"), ("Sam Ruiz", "Finance")]
    for i, (name, role) in enumerate(people):
        x, f = 560 + i * 400, 4 + i * 6
        card_settle(k.ell(f"Portrait {i + 1}", x, 430, 220, 220, PORTRAIT, f0=f, dur=n - f), f)
        soft_rise(text(k, f"Name {i + 1}", name, x, 600, 38, COL['ink'], f0=f + 8, dur=n - f - 8, style='SemiBold', align='center'), f + 8)
        soft_rise(text(k, f"Role {i + 1}", role, x, 648, 28, COL['grey'], f0=f + 12, dur=n - f - 12, style='Regular', align='center'), f + 12)


def split_screen(d):
    n = 150
    k = d.comp("CB Split screen", n, "css"); lab_bg(k, n); k.rect("Light background", 0, 0, 1920, 1080, COL['light'], f0=0, dur=n)   # kept in the template
    ph = k.rect("Photo", 480, 540, 960, 1080, COL['navy2'], f0=0, dur=n, center=True)     # stand-in for a photo or video
    push(ph, 0, 149)                                                                       # Photo push, held to the clip
    st = k.rect("Accent strip", 960, 0, 12, 1080, COL['teal'], f0=4, dur=n - 4)
    grow(st, 4, 20, DECEL, edge='top')   # draws down from the top
    soft_rise(text(k, "Kicker", "CASE STUDY", 1080, 380, 28, COL['teal'], f0=8, dur=n - 8, style='SemiBold', track=1.3), 8)
    soft_rise(text(k, "Heading", "Cutting energy\nuse by 38%", 1080, 500, 72, COL['ink'], f0=12, dur=n - 12, style='SemiBold', lh=1.1), 12)
    soft_rise(text(k, "Body", "Three plants, one retrofit plan.", 1080, 650, 34, COL['grey'], f0=20, dur=n - 20, style='Regular'), 20)


def leader_callout(d):
    n = 120
    k = d.comp("CB Leader callout", n, "clc"); lab_bg(k, n, COL['navy2'])
    px, py = 760, 640                                                         # the point being called out
    ring = k.ell("Point ring", px, py, 44, 44, None, f0=0, dur=n); ring.stroke(COL['white'], 3)
    card_settle(ring, 0)
    pt = card_settle(k.ell("Point", px, py, 16, 16, COL['teal'], f0=0, dur=n), 0)
    ld = line(k, "Leader", [(px + 22, py - 22), (px + 180, py - 180), (px + 480, py - 180)], COL['white'], 3, f0=0, dur=n)
    ld.trim([(8, 0.0, 'Linear'), (30, 1.0, DECEL)])
    ct = soft_rise(text(k, "Callout title", "Heat recovery unit", px + 200, py - 222, 40, COL['white'], f0=26, dur=n - 26, style='SemiBold'), 26)
    cn = soft_rise(text(k, "Callout note", "Saves 1.2 GWh a year", px + 200, py - 140, 30, COL['grey'], f0=30, dur=n - 30, style='Regular'), 30)
    fade_all([ring, pt, ld, ct, cn], n)


def panel_wipe(d):
    """Back panel (navy) enters first and leaves last; the front panel (teal) enters 3 f later and
    leaves 3 f earlier, so the navy shows as a leading band on the way in and a trailing band on the way out."""
    k = d.comp("CB Panel wipe", 40, "cpw")
    for name, col, fin, fout in [("Panel navy", COL['navy'], 0, 23), ("Panel teal", COL['teal'], 3, 20)]:
        end = fout + 16
        p = k.rect(name, 960, 540, 1000, 1080, col, f0=fin, dur=end - fin, center=True)   # the clip spans only its motion
        p.sc([1.94, 1.0])                                                     # drawn 1000 px wide, scaled to cover (KI-137)
        bx, by = p.base
        p.pos([(fin, (bx - 1920, by), 'Linear'), (fin + 16, (bx, by), BEZ['smooth']), (fout, (bx, by), 'Linear'),
               (end, (bx + 1920, by), BEZ['smooth'])])


def build():
    d = Doc()
    chapter_title(d); quote(d); end_card(d); agenda(d); team_row(d); split_screen(d); leader_callout(d); panel_wipe(d)
    return d


if __name__ == "__main__":
    print(__doc__)
