"""Futuristic HUD round 2: eight more lab comps (ID lower third, segmented loader, hex grid,
signal bars, target lock, alert banner, map ping, scan wipe), written straight into a
.carverproj.

    import futuristic_hud_lab2 as L; presets, masks = L.build(PROJECT.carverproj)

Same palette and rules as futuristic_hud_lab.py: glow amount 0.45-0.6 (never above 0.8),
thin strokes, tracked SemiBold caps, stepped (Hold) changes for digital readouts, and
continuous motion one way only. After writing: edit.open {path, force:true}; apply PRESETS
(preset.apply); edit.save; check with carvercat_inspect (curves, lint, qc) and carvercat_look;
extract templates with comp_to_template.py (--drop "Lab bg"). Docs: ai/patterns/futuristic-hud.md.
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from futuristic_hud_lab import Doc, lin, P, COL, EXPO, lab_bg
from cc import BEZ

PRESETS, MASKS = [], []


def corner_set(k, name, cx, cy, w, h, arm, f, px=4):
    l, r, t, b = cx - w / 2, cx + w / 2, cy - h / 2, cy + h / 2
    out = []
    for i, pts in enumerate([[(l, t + arm), (l, t), (l + arm, t)], [(r - arm, t), (r, t), (r, t + arm)],
                             [(r, b - arm), (r, b), (r - arm, b)], [(l + arm, b), (l, b), (l, b - arm)]]):
        o = k.line(f"{name} {i + 1}", pts, COL['cyan'], px=px, f0=f, dur=None if f == 0 else k.length - f)
        o.glow(size=6, amount=0.45); out.append(o)
    return out


def id_lower_third(d):
    n = 150
    k = d.comp("FH ID lower third", n, "fid"); lab_bg(k, n)
    for o in corner_set(k, "ID corner", 530, 885, 820, 180, 30, 0):   # audit 2026-10-28: 120-940 x 795-975, clear of the text
        o.trim([(0, 0.0, 'Linear'), (12, 1.0, EXPO)])
        PRESETS.append(("FH ID lower third", o.clip['label'], "Power down"))
    k.text("Callsign", "CMDR. ARIA VOSS", 150, 860, 46, COL['white'], f0=8, dur=n - 8, style='SemiBold', track=1.3)
    PRESETS.extend([("FH ID lower third", "Callsign", "Flicker on"), ("FH ID lower third", "Callsign", "Exit fade - fast")])   # Power down squeezes text below lint's 18 px
    k.text("ID line", "ID 0427  //  ORBITAL OPS", 150, 912, 28, COL['dim'], f0=16, dur=n - 16, style='SemiBold', track=1.4)
    PRESETS.extend([("FH ID lower third", "ID line", "Flicker on"), ("FH ID lower third", "ID line", "Exit fade - fast")])
    dot = k.ell("Status dot", 890, 862, 16, 16,   # the callsign ends near x 850 (geometry): the dot sat on it before
                 COL['amber'], f0=22, dur=n - 22); dot.glow(size=6, amount=0.5)
    PRESETS.extend([("FH ID lower third", "Status dot", "Flicker on"), ("FH ID lower third", "Status dot", "Power down")])


def loader(d):
    n = 130
    k = d.comp("FH Loader", n, "fld"); lab_bg(k, n)
    x0, segs, w, gap = 560, 10, 70, 10
    k.text("Loader label", "UPLOADING MODEL", x0, 450, 34, COL['dim'], f0=0, dur=n, style='SemiBold', track=1.3)
    PRESETS.append(("FH Loader", "Loader label", "Flicker on"))
    for i in range(segs):
        x = x0 + i * (w + gap)
        k.rect(f"Slot {i + 1}", x, 510, w, 40, None, f0=0, dur=n).stroke(COL['dim'], 2)
        f = 10 + i * 9
        s = k.rect(f"Segment {i + 1}", x + 4, 514, w - 8, 32, COL['cyan'], f0=f, dur=n - f)
        s.glow(size=6, amount=0.45)
        s.op([(f, 0.0, 'Hold'), (f + 1, 1.0, 'Hold')])                 # a digital fill: each segment snaps on
    for i, (pct, f0, f1) in enumerate([("30%", 28, 55), ("60%", 55, 91), ("100%", 91, n)]):   # each label appears with its segment
        o = k.text(f"Percent {i + 1}", pct, x0 + segs * (w + gap) - gap, 450, 34, COL['cyan'], f0=f0, dur=f1 - f0, style='SemiBold',
                   align='right', track=1.2)
    k.text("Done", "COMPLETE", x0, 600, 34, COL['amber'], f0=91, dur=n - 91, style='SemiBold', track=1.4)
    PRESETS.append(("FH Loader", "Done", "Flicker on"))


def hex_grid(d):
    n = 120
    k = d.comp("FH Hex grid", n, "fhx"); lab_bg(k, n)
    r = 70
    i = 0
    for row in range(-1, 8):
        for col in range(-1, 13):
            x = col * r * 1.75 + (r * 0.875 if row % 2 else 0)
            y = row * r * 1.52
            if not (r < x < 1920 - r and r < y < 1080 - r): continue      # whole hexes only: lint cropped_at_rest
            h = k.ngon(f"Hex {i + 1}", x, y, 2 * r - 10, 6, None, f0=0, dur=n, angle=30.0)
            h.nofill(); h.stroke(COL['dim'], 2)                         # cc.ngon fills even with col=None: clear it
            dist = math.hypot(x - 960, y - 540)
            f = int(dist / 40)                                          # a ring of light spreads from the centre
            h.op([(0, 0.0, 'Hold'), (f, 1.0, 'Hold'), (f + 2, 0.3, 'Hold'), (f + 4, 1.0, 'Hold')])
            i += 1
    core = k.ngon("Core hex", 960, 540, 2 * r - 10, 6, COL['cyan'], f0=0, dur=n, angle=30.0); core.glow(size=10, amount=0.55)
    PRESETS.append(("FH Hex grid", "Core hex", "Flicker on"))


def signal_bars(d):
    n = 120
    k = d.comp("FH Signal bars", n, "fsg"); lab_bg(k, n)
    k.text("Signal label", "SIGNAL ANALYSIS", 600, 330, 30, COL['dim'], f0=0, dur=n, style='SemiBold', track=1.4)
    PRESETS.append(("FH Signal bars", "Signal label", "Flicker on"))
    import random
    rnd = random.Random(7)
    for i in range(16):
        x = 620 + i * 44
        b = k.rect(f"Bar {i + 1}", x, 400, 28, 300, COL['cyan'] if i % 5 else COL['amber'], f0=0, dur=n)   # baseline y 700
        b.anchor(0, -1); b.glow(size=4, amount=0.45)
        keys = [(0, [1.0, 0.0], 'Hold')]
        for j, f in enumerate(range(4 + i, n, 12)):                       # stepped levels, a new reading every 12 f
            keys.append((f, [1.0, round(0.15 + 0.85 * rnd.random(), 3)], 'Hold'))
        b.scale(keys)


def target_lock(d):
    n = 90
    k = d.comp("FH Target lock", n, "ftl"); lab_bg(k, n)
    cx, cy = 1180, 470
    for i, o in enumerate(corner_set(k, "Lock corner", cx, cy, 200, 200, 36, 0, px=5)):
        sx, sy = [(-1, -1), (1, -1), (1, 1), (-1, 1)][i]
        bx, by = o.base
        o.pos([(0, [bx + sx * 320 / 1920, by - sy * 320 / 1080], 'Linear'), (24, [bx, by], EXPO)])
        o.op([(0, 0.0, 'Linear'), (4, 1.0, 'Linear')])
        o.rot([(0, 90.0, 'Linear'), (24, 0.0, EXPO)])
    dot = k.ell("Target", cx, cy, 20, 20, COL['amber'], f0=0, dur=n); dot.glow(size=8, amount=0.55)
    PRESETS.append(("FH Target lock", "Target", "Flicker on"))
    ln = k.line("Lock leader", [(cx + 110, cy - 110), (cx + 220, cy - 200), (cx + 440, cy - 200)], COL['amber'], px=3, f0=26, dur=n - 26)
    ln.trim([(26, 0.0, 'Linear'), (38, 1.0, EXPO)])
    k.text("Lock text", "LOCKED", cx + 240, cy - 236, 40, COL['amber'], f0=34, dur=n - 34, style='SemiBold', track=1.4)
    PRESETS.append(("FH Target lock", "Lock text", "Flicker on"))
    k.text("Lock data", "RANGE 1.2 KM", cx + 240, cy - 166, 26, COL['dim'], f0=40, dur=n - 40, style='SemiBold', track=1.3)
    PRESETS.append(("FH Target lock", "Lock data", "Flicker on"))


def alert_banner(d):
    n = 120
    k = d.comp("FH Alert banner", n, "fal"); lab_bg(k, n)
    band = k.rect("Alert band", 960, 540, 1000, 150, lin('2A1B05'), f0=0, dur=n, center=True); band.sc([1.6, 1.0])
    PRESETS.append(("FH Alert banner", "Alert band", "Scan open (Y)"))
    for i, y in enumerate((465, 615)):
        e = k.rect(f"Alert edge {i + 1}", 960, y, 1000, 6, COL['amber'], f0=0, dur=n, center=True); e.sc([1.6, 1.0]); e.glow(size=8, amount=0.5)
        PRESETS.append(("FH Alert banner", f"Alert edge {i + 1}", "Scan open (Y)"))
    t = k.text("Alert text", "WARNING  //  HULL BREACH", 960, 540, 64, COL['amber'], f0=8, dur=n - 8, style='SemiBold', align='center', track=1.3)
    t.glow(size=8, amount=0.45)
    # two slow pulses (1 a second, well under 3 flashes a second), then steady
    t.op([(8, 0.0, 'Hold'), (10, 1.0, 'Hold'), (40, 0.35, 'Hold'), (48, 1.0, 'Hold'), (70, 0.35, 'Hold'), (78, 1.0, 'Hold')])


def map_ping(d):
    n = 120
    k = d.comp("FH Map ping", n, "fmp"); lab_bg(k, n)
    cx, cy = 820, 560
    for i in range(3):
        f = i * 20
        rg = k.ell(f"Ping ring {i + 1}", cx, cy, 200, 200, None, f0=f, dur=40); rg.stroke(COL['cyan'], 4); rg.glow(size=6, amount=0.45)
        rg.scale([(f, 0.1, 'Linear'), (f + 40, 2.2, BEZ['decel'])])        # rings only grow: one way
        rg.op([(f, 1.0, 'Linear'), (f + 40, 0.0, 'Linear')])
    dot = k.ell("Ping dot", cx, cy, 26, 26, COL['amber'], f0=0, dur=n); dot.glow(size=8, amount=0.55)
    PRESETS.append(("FH Map ping", "Ping dot", "Flicker on"))
    k.line("Ping leader", [(cx + 20, cy - 20), (cx + 120, cy - 120), (cx + 420, cy - 120)], COL['dim'], px=2, f0=10, dur=n - 10).trim(
        [(10, 0.0, 'Linear'), (24, 1.0, EXPO)])
    k.text("Ping coords", "47.3769 N  8.5417 E", cx + 140, cy - 156, 30, COL['cyan'], f0=20, dur=n - 20, style='SemiBold', track=1.2)
    PRESETS.append(("FH Map ping", "Ping coords", "Flicker on"))
    k.text("Ping name", "RELAY STATION 3", cx + 140, cy - 84, 26, COL['dim'], f0=26, dur=n - 26, style='SemiBold', track=1.4)
    PRESETS.append(("FH Map ping", "Ping name", "Flicker on"))


def scan_wipe(d):
    n = 30
    k = d.comp("FH Scan wipe", n, "fsw")
    pan = k.rect("Scan panel", 960, 500, 1000, 1000, COL['grid'], f0=0, dur=n, center=True)   # top edge at y 0; x 1.08 reaches 1080
    pan.anchor(0, 1)                                                     # grows down from the top edge
    pan.scale([(0, [1.92, 0.0], 'Linear'), (12, [1.92, 1.08], BEZ['smooth']), (16, [1.92, 1.08], 'Linear'), (n, [1.92, 0.0], BEZ['accel'])])
    line = k.rect("Scan beam", 960, 540, 1000, 6, COL['cyan'], f0=0, dur=n, center=True); line.sc([1.92, 1.0]); line.glow(size=12, amount=0.6)
    bx, by = line.base
    e = 4 / 1080                                                      # keep the beam 4 px inside the frame while it waits
    line.pos([(0, [bx, 1.0 - e], 'Linear'), (12, [bx, e], BEZ['smooth']), (16, [bx, e], 'Linear'), (n, [bx, 1.0 - e], BEZ['accel'])])


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    id_lower_third(d); loader(d); hex_grid(d); signal_bars(d); target_lock(d); alert_banner(d); map_ping(d); scan_wipe(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
