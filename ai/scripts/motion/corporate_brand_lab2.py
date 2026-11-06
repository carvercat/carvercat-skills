"""Corporate Brand round 2: eight more lab comps (chapter title, quote, end card, agenda,
team row, split screen, leader callout, brand panel wipe), written straight into a .carverproj.

    import corporate_brand_lab2 as L; presets, masks = L.build(PROJECT.carverproj)

Same palette, style rules and verification as corporate_brand_lab.py: standard and
decelerate curves only, no springs or overshoot. After writing: edit.open {path,
force:true}; apply PRESETS (preset.apply); edit.save; check with carvercat_inspect and
carvercat_look; extract templates with comp_to_template.py (--drop "Lab bg").
Docs: ai/patterns/corporate-brand.md. Pixel space 1920x1080, y down; comp frames, 30 fps.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corporate_brand_lab import Doc, lin, COL, EXPO, DECEL, lab_bg
from cc import BEZ

ACCEL = BEZ['accel']
PRESETS, MASKS = [], []


def grow_x(o, f, d=14):
    o.anchor(-1, 0); o.scale([(f, [0.0, 1.0], 'Linear'), (f + d, [1.0, 1.0], EXPO)]); return o


def chapter_title(d):
    n = 90
    k = d.comp("CB Chapter title", n, "cch"); lab_bg(k, n)
    k.text("Chapter number", "01", 240, 430, 120, COL['teal'], f0=0, dur=n, style='SemiBold')
    PRESETS.append(("CB Chapter title", "Chapter number", "Soft rise"))
    grow_x(k.rect("Chapter rule", 240, 520, 1100, 3, COL['grey'], f0=6, dur=n - 6), 6, 24)
    k.text("Chapter name", "Our mission", 240, 610, 88, COL['white'], f0=12, dur=n - 12, style='SemiBold')
    PRESETS.append(("CB Chapter title", "Chapter name", "Soft rise"))
    k.text("Chapter note", "Why we build what we build", 240, 690, 34, COL['grey'], f0=20, dur=n - 20, style='Regular')
    PRESETS.append(("CB Chapter title", "Chapter note", "Soft rise"))


def quote(d):
    n = 150
    k = d.comp("CB Quote", n, "cqt"); lab_bg(k, n)
    bar = k.rect("Quote bar", 300, 380, 6, 260, COL['teal'], f0=0, dur=n)
    bar.anchor(0, 1); bar.scale([(0, [1.0, 0.0], 'Linear'), (20, [1.0, 1.0], DECEL)])   # draws down from its top
    k.text("Quote", "Good infrastructure is the kind\nnobody has to think about.", 360, 450, 64, COL['white'], f0=8, dur=n - 8,
           style='SemiBold', lh=1.15)
    PRESETS.append(("CB Quote", "Quote", "Soft rise"))
    k.text("Speaker", "Dana Okafor", 360, 610, 34, COL['teal'], f0=26, dur=n - 26, style='SemiBold')
    PRESETS.append(("CB Quote", "Speaker", "Soft rise"))
    k.text("Speaker role", "Head of Operations, Northwind", 360, 656, 28, COL['grey'], f0=30, dur=n - 30, style='Regular')
    PRESETS.append(("CB Quote", "Speaker role", "Soft rise"))
    for o in ("Quote bar", "Quote", "Speaker", "Speaker role"):
        PRESETS.append(("CB Quote", o, "Soft fade out"))


def end_card(d):
    n = 120
    k = d.comp("CB End card", n, "cec"); lab_bg(k, n); k.rect("Light background", 0, 0, 1920, 1080, COL['light'], f0=0, dur=n)   # kept in the template
    k.rect("Mark outer", 960, 380, 120, 120, COL['navy'], r=24, f0=0, dur=n, center=True)
    PRESETS.append(("CB End card", "Mark outer", "Card settle"))
    k.rect("Mark inner", 960, 380, 48, 48, COL['teal'], r=10, f0=6, dur=n - 6, center=True)
    PRESETS.append(("CB End card", "Mark inner", "Card settle"))
    k.text("Wordmark", "NORTHWIND", 960, 510, 60, COL['ink'], f0=12, dur=n - 12, style='SemiBold', align='center', track=1.25)
    PRESETS.append(("CB End card", "Wordmark", "Soft rise"))
    grow_x(k.rect("End rule", 860, 570, 200, 3, COL['teal'], f0=20, dur=n - 20), 20, 20)
    k.text("URL", "northwind.com", 960, 630, 34, COL['grey'], f0=26, dur=n - 26, style='Medium', align='center')
    PRESETS.append(("CB End card", "URL", "Soft rise"))


def agenda(d):
    n = 150
    k = d.comp("CB Agenda", n, "cag"); lab_bg(k, n)
    k.text("Agenda title", "Agenda", 300, 260, 64, COL['white'], f0=0, dur=n, style='SemiBold')
    PRESETS.append(("CB Agenda", "Agenda title", "Soft rise"))
    items = ["The year in numbers", "Our people", "New markets", "What comes next"]
    ind = k.rect("Active marker", 300, 420, 8, 64, COL['teal'], f0=24, dur=n - 24, center=True)
    ind.op([(24, 0, 'Linear'), (36, 1, 'Ease out')])
    bx, by = ind.base
    ind.pos([(60, [bx, by], 'Linear'), (78, [bx, by - 100 / 1080], DECEL)])     # moves to item 2
    for i, s in enumerate(items):
        y, f = 420 + i * 100, 8 + i * 5
        k.text(f"Number {i + 1}", f"0{i + 1}", 340, y, 40, COL['teal'], f0=f, dur=n - f, style='SemiBold')
        PRESETS.append(("CB Agenda", f"Number {i + 1}", "Soft rise"))
        t = k.text(f"Item {i + 1}", s, 430, y, 40, COL['white'] if i == 1 else COL['grey'], f0=f, dur=n - f, style='Medium')
        PRESETS.append(("CB Agenda", f"Item {i + 1}", "Soft rise"))


def team_row(d):
    n = 120
    k = d.comp("CB Team row", n, "ctm"); lab_bg(k, n); k.rect("Light background", 0, 0, 1920, 1080, COL['light'], f0=0, dur=n)   # kept in the template
    people = [("Dana Okafor", "Operations"), ("Lee Varga", "Engineering"), ("Sam Ruiz", "Finance")]
    for i, (name, role) in enumerate(people):
        x, f = 560 + i * 400, 4 + i * 6
        k.ell(f"Portrait {i + 1}", x, 430, 220, 220, lin('C9D1DC'), f0=f, dur=n - f)
        PRESETS.append(("CB Team row", f"Portrait {i + 1}", "Card settle"))
        k.text(f"Name {i + 1}", name, x, 600, 38, COL['ink'], f0=f + 8, dur=n - f - 8, style='SemiBold', align='center')
        PRESETS.append(("CB Team row", f"Name {i + 1}", "Soft rise"))
        k.text(f"Role {i + 1}", role, x, 648, 28, COL['grey'], f0=f + 12, dur=n - f - 12, style='Regular', align='center')
        PRESETS.append(("CB Team row", f"Role {i + 1}", "Soft rise"))


def split_screen(d):
    n = 150
    k = d.comp("CB Split screen", n, "css"); lab_bg(k, n); k.rect("Light background", 0, 0, 1920, 1080, COL['light'], f0=0, dur=n)   # kept in the template
    ph = k.rect("Photo", 480, 540, 960, 1080, COL['navy2'], f0=0, dur=n, center=True)     # stand-in for a photo or video
    PRESETS.append(("CB Split screen", "Photo", "Photo push - 5 s"))
    st = k.rect("Accent strip", 960, 0, 12, 1080, COL['teal'], f0=4, dur=n - 4)
    st.anchor(0, 1); st.scale([(4, [1.0, 0.0], 'Linear'), (24, [1.0, 1.0], DECEL)])   # draws down from the top
    k.text("Kicker", "CASE STUDY", 1080, 380, 28, COL['teal'], f0=8, dur=n - 8, style='SemiBold', track=1.3)
    PRESETS.append(("CB Split screen", "Kicker", "Soft rise"))
    k.text("Heading", "Cutting energy\nuse by 38%", 1080, 500, 72, COL['ink'], f0=12, dur=n - 12, style='SemiBold', lh=1.1)
    PRESETS.append(("CB Split screen", "Heading", "Soft rise"))
    k.text("Body", "Three plants, one retrofit plan.", 1080, 650, 34, COL['grey'], f0=20, dur=n - 20, style='Regular')
    PRESETS.append(("CB Split screen", "Body", "Soft rise"))


def leader_callout(d):
    n = 120
    k = d.comp("CB Leader callout", n, "clc"); lab_bg(k, n, COL['navy2'])
    px, py = 760, 640                                                         # the point being called out
    ring = k.ell("Point ring", px, py, 44, 44, None, f0=0, dur=n); ring.stroke(COL['white'], 3)
    PRESETS.append(("CB Leader callout", "Point ring", "Card settle"))
    k.ell("Point", px, py, 16, 16, COL['teal'], f0=0, dur=n)
    PRESETS.append(("CB Leader callout", "Point", "Card settle"))
    ld = k.line("Leader", [(px + 22, py - 22), (px + 180, py - 180), (px + 480, py - 180)], COL['white'], px=3, f0=0, dur=n)
    ld.trim([(8, 0.0, 'Linear'), (30, 1.0, DECEL)])
    k.text("Callout title", "Heat recovery unit", px + 200, py - 222, 40, COL['white'], f0=26, dur=n - 26, style='SemiBold')
    PRESETS.append(("CB Leader callout", "Callout title", "Soft rise"))
    k.text("Callout note", "Saves 1.2 GWh a year", px + 200, py - 140, 30, COL['grey'], f0=30, dur=n - 30, style='Regular')
    PRESETS.append(("CB Leader callout", "Callout note", "Soft rise"))
    for o in ("Point ring", "Point", "Leader", "Callout title", "Callout note"):
        PRESETS.append(("CB Leader callout", o, "Soft fade out"))


def panel_wipe(d):
    """Back panel (navy) enters first and leaves last; the front panel (teal) enters 3 f later and
    leaves 3 f earlier, so the navy shows as a leading band on the way in and a trailing band on the way out."""
    k = d.comp("CB Panel wipe", 40, "cpw")
    for name, col, fin, fout in [("Panel navy", COL['navy'], 0, 23), ("Panel teal", COL['teal'], 3, 20)]:
        end = fout + 16
        p = k.rect(name, 960, 540, 1000, 1080, col, f0=fin, dur=end - fin, center=True)   # the clip spans only its motion
        p.sc([1.94, 1.0])                                                     # drawn 1000 px wide, scaled to cover (KI-137)
        bx, by = p.base
        p.pos([(fin, [bx - 1.0, by], 'Linear'), (fin + 16, [bx, by], BEZ['smooth']), (fout, [bx, by], 'Linear'),
               (end, [bx + 1.0, by], BEZ['smooth'])])


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    chapter_title(d); quote(d); end_card(d); agenda(d); team_row(d); split_screen(d); leader_callout(d); panel_wipe(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
