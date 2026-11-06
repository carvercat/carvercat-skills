"""Write the Futuristic HUD lab comps into a .carverproj (direct project-file authoring).

    import futuristic_hud_lab as L; presets, masks = L.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); edit.save.
Check with carvercat_inspect (curves, lint, qc for flashes) and carvercat_look; extract
templates with comp_to_template.py (--drop "Lab bg").

Measured geometry used here (0.1.6): an ellipse's stroke path starts at 3 o'clock and runs
counter-clockwise; rotation is positive counter-clockwise. Glow amount stays <= 0.8.
Fonts: Rethink Sans must be installed (KI-136).
Docs: ai/patterns/futuristic-hud.md. Pixel space 1920x1080, y down; comp frames, 30 fps.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author"))
from cc import Doc, lin, P, BEZ

COL = dict(bg=lin('05080F'), cyan=lin('35E0FF'), dim=lin('0E6F86'), amber=lin('FFB020'), white=lin('E6FBFF'), grid=lin('0F2A36'))
EXPO = BEZ['expo']
PRESETS, MASKS = [], []


def lab_bg(k, n):
    k.rect("Lab bg", 0, 0, 1920, 1080, COL['bg'], f0=0, dur=n)


def reticle(d):
    n = 90
    k = d.comp("FH Reticle", n, "frt"); lab_bg(k, n)
    cx, cy = 960, 540
    outer = k.ell("Outer ring", cx, cy, 440, 440, None, f0=0, dur=n); outer.stroke(COL['cyan'], 4, line='dashed', dash=28, gap=14)
    outer.glow(size=8, amount=0.5)
    outer.rot([(0, 0.0, 'Linear'), (n, 60.0, 'Linear')])
    PRESETS.append(("FH Reticle", "Outer ring", "Scan open (Y)"))
    inner = k.ell("Inner arcs", cx, cy, 300, 300, None, f0=6, dur=n - 6); inner.stroke(COL['cyan'], 8, cap='butt')
    inner.glow(size=8, amount=0.5)
    tp = inner.trim([(6, 0.1, 'Linear'), (20, 0.45, EXPO)], which='end'); inner.set(tp + '.start', 0.1)
    inner.rot([(6, 0.0, 'Linear'), (n, -90.0, 'Linear')])
    for name, a, b in (("Cross left", (cx - 270, cy), (cx - 90, cy)), ("Cross right", (cx + 270, cy), (cx + 90, cy)),
                       ("Cross top", (cx, cy - 270), (cx, cy - 90)), ("Cross bottom", (cx, cy + 270), (cx, cy + 90))):
        ln = k.line(name, [a, b], COL['white'], px=3, f0=10, dur=n - 10)
        ln.trim([(10, 0.0, 'Linear'), (22, 1.0, EXPO)], which='end')
    k.ell("Centre dot", cx, cy, 14, 14, COL['amber'], f0=20, dur=n - 20)
    PRESETS.append(("FH Reticle", "Centre dot", "Flicker on"))
    k.text("Lock label", "TARGET LOCKED", cx, cy + 320, 34, COL['amber'], f0=30, dur=n - 30, style='SemiBold', align='center', track=1.4)
    PRESETS.append(("FH Reticle", "Lock label", "Flicker on"))


def brackets(d):
    n = 75
    k = d.comp("FH Brackets", n, "fbr"); lab_bg(k, n)
    cx, cy, w, h, arm = 960, 540, 640, 380, 60
    l, r, t, b = cx - w / 2, cx + w / 2, cy - h / 2, cy + h / 2
    corners = [("Corner TL", [(l, t + arm), (l, t), (l + arm, t)], -1, -1), ("Corner TR", [(r - arm, t), (r, t), (r, t + arm)], 1, -1),
               ("Corner BR", [(r, b - arm), (r, b), (r - arm, b)], 1, 1), ("Corner BL", [(l + arm, b), (l, b), (l, b - arm)], -1, 1)]
    for i, (name, pts, sx, sy) in enumerate(corners):
        o = k.line(name, pts, COL['cyan'], px=5, f0=0, dur=n)
        o.glow(size=6, amount=0.45)
        bx, by = o.base; f = i * 2
        o.pos([(f, [bx + sx * 90 / 1920, by - sy * 90 / 1080], 'Linear'), (f + 14, [bx, by], EXPO)])
        o.op([(f, 0, 'Linear'), (f + 4, 1, 'Linear')])
    scan = k.rect("Scan line", cx, t + 10, w - 40, 3, COL['cyan'], f0=16, dur=n - 16, center=True)
    scan.glow(size=10, amount=0.6)
    sxp, syp = scan.base
    scan.pos([(16, [sxp, syp], 'Linear'), (56, [sxp, syp - (h - 20) / 1080], 'S-curve')])
    scan.op([(16, 0, 'Linear'), (20, 1, 'Linear')])
    k.text("Tag", "SCAN 01", l, t - 30, 26, COL['cyan'], f0=12, dur=n - 12, style='SemiBold', track=1.4)
    PRESETS.append(("FH Brackets", "Tag", "Flicker on"))


def readout(d):
    n = 100
    k = d.comp("FH Readout", n, "frd"); lab_bg(k, n)
    rows = [("SYS STATUS", "NOMINAL"), ("CORE TEMP", "41.8 C"), ("LINK", "ENCRYPTED"), ("SIGNAL", "98%")]
    bar = k.rect("Accent bar", 560, 540, 6, 300, COL['cyan'], f0=0, dur=n, center=True)
    bar.scale([(0, [1.0, 0.0], 'Linear'), (14, [1.0, 1.0], EXPO)]); bar.glow(size=6, amount=0.5)
    for i, (lab, val) in enumerate(rows):
        y = 435 + i * 70; f = 8 + i * 10
        k.text(f"Label {i + 1}", lab, 600, y, 34, COL['dim'], f0=f, dur=n - f, style='SemiBold', track=1.3)
        PRESETS.append(("FH Readout", f"Label {i + 1}", "Flicker on"))
        v = k.text(f"Value {i + 1}", val, 1320, y, 34, COL['cyan'], f0=f + 4, dur=n - f - 4, style='SemiBold', align='right', track=1.2)
        rpo = f'src.e_src_text_relative_{v.id}.opacity'
        ents = v.clip['containers'].setdefault('effects', {'entries': [], 'promoted': []})['entries']
        ents.insert(0, {'id': f'e_fx_stagger_{v.id}', 'cap': 'stagger', 'on': True, 'by': 'character', 'order': 'forward',
                        'amount': 2.0, 'amountMode': 'each', 'seed': 1, 'connected': [rpo]})
        v.key(rpo, [(f + 4, 0, 'Linear'), (f + 5, 1, 'Hold')])          # types on, 2 f per character


def radar(d):
    n = 120
    k = d.comp("FH Radar", n, "frr"); lab_bg(k, n)
    cx, cy, R = 960, 540, 300
    for i, dia in enumerate((200, 400, 600)):
        ring = k.ell(f"Ring {i + 1}", cx, cy, dia, dia, None, f0=0, dur=n); ring.stroke(COL['grid'], 2)
    k.line("Axis H", [(cx - R, cy), (cx + R, cy)], COL['grid'], px=2, f0=0, dur=n)
    k.line("Axis V", [(cx, cy - R), (cx, cy + R)], COL['grid'], px=2, f0=0, dur=n)
    period = 60                                                      # one clockwise turn per 2 s
    wedge = k.ell("Sweep wedge", cx, cy, R, R, None, f0=0, dur=n); wedge.stroke(COL['cyan'], R, cap='butt')   # a butt-capped stroke as wide as the radius: a pie slice
    tp = wedge.trim([(0, 0.07, 'Linear')], which='end'); wedge.set(tp + '.start', 0.0)
    wedge.opv(0.28)
    wedge.rot([(0, 0.0, 'Linear'), (n, -360.0 * n / period, 'Linear')])
    beam = k.line("Sweep line", [(cx, cy), (cx + R, cy)], COL['cyan'], px=3, f0=0, dur=n)
    beam.anchor(-1, 0); beam.glow(size=8, amount=0.6)
    beam.rot([(0, 0.0, 'Linear'), (n, -360.0 * n / period, 'Linear')])
    for i, (ang, rad) in enumerate(((300, 0.55), (200, 0.8), (40, 0.35))):    # math angles, counter-clockwise from 3 o'clock
        import math
        x = cx + R * rad * math.cos(math.radians(ang)); y = cy - R * rad * math.sin(math.radians(ang))
        t = round(((360 - ang) % 360) / 360 * period)
        dot = k.ell(f"Blip {i + 1}", x, y, 18, 18, COL['amber'], f0=t, dur=n - t)
        dot.glow(size=6, amount=0.5)
        dot.scale([(t, 0.0, 'Linear'), (t + 6, 1.0, BEZ['back'])])
        dot.op([(t, 1.0, 'Linear'), (t + 50, 0.35, 'Linear')])


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    reticle(d); brackets(d); readout(d); radar(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
