"""Futuristic HUD round 2 in design units (cc2.py): eight lab comps (ID lower third, segmented loader, hex grid, signal bars, target lock,
alert banner, map ping, scan wipe).

    import futuristic_hud_lab2 as L; doc = L.build(); doc.send(client, PROJECT.carverproj)

Same palette and rules as futuristic_hud_lab.py, whose helpers it uses (line, T, flick, scan_open, power_down, exit_fade, type_on): glow
amount 0.45-0.6 (never above 0.8), thin strokes, tracked SemiBold caps, stepped (Hold) changes for digital readouts, continuous motion
one way only. The pack's presets are baked as keys, so nothing is applied after `send`. Docs: ai/patterns/futuristic-hud.md.
"""
import os, sys, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from futuristic_hud_lab import (HDoc, Doc, css, BEZ, HOLD, COL, EXPO, lab_bg, line, T, gl, flick, scan_open, power_down, exit_fade, type_on, draw)


def corner_set(k, name, cx, cy, w, h, arm, f, px=4):
    l, r, t, b = cx - w / 2, cx + w / 2, cy - h / 2, cy + h / 2
    out = []
    for i, pts in enumerate([[(l, t + arm), (l, t), (l + arm, t)], [(r - arm, t), (r, t), (r, t + arm)],
                             [(r, b - arm), (r, b), (r - arm, b)], [(l + arm, b), (l, b), (l, b - arm)]]):
        o = line(k, f"{name} {i + 1}", pts, COL['cyan'], px=px, f0=f, dur=k.length - f)
        gl(o, 6, 0.45); out.append(o)
    return out


def id_lower_third(d):
    n = 150
    k = d.comp("FH ID lower third", n, "fid"); lab_bg(k, n)
    for o in corner_set(k, "ID corner", 530, 885, 820, 180, 30, 0):   # audit 2026-10-28: 120-940 x 795-975, clear of the text
        o.trim([(0, 0.0, 'Linear'), (12, 1.0, EXPO)])
        power_down(o)
    cs = T(k, "Callsign", "CMDR. ARIA VOSS", 150, 860, 46, COL['white'], f0=8, dur=n - 8, track=1.3)
    flick(cs); exit_fade(cs)                                          # Power down squeezes text below lint's 18 px
    il = T(k, "ID line", "ID 0427  //  ORBITAL OPS", 150, 912, 28, COL['dim'], f0=16, dur=n - 16, track=1.4)
    flick(il); exit_fade(il)
    dot = k.ell("Status dot", 890, 862, 16, 16, COL['amber'], f0=22, dur=n - 22); gl(dot, 6, 0.5)   # the callsign ends near x 850
    flick(dot); power_down(dot)


def loader(d):
    n = 130
    k = d.comp("FH Loader", n, "fld"); lab_bg(k, n)
    x0, segs, w, gap = 560, 10, 70, 10
    flick(T(k, "Loader label", "UPLOADING MODEL", x0, 450, 34, COL['dim'], f0=0, dur=n, track=1.3))
    for i in range(segs):
        x = x0 + i * (w + gap)
        k.rect(f"Slot {i + 1}", x, 510, w, 40, None, f0=0, dur=n).stroke(COL['dim'], 2)
        f = 10 + i * 9
        s = k.rect(f"Segment {i + 1}", x + 4, 514, w - 8, 32, COL['cyan'], f0=f, dur=n - f)
        gl(s, 6, 0.45)
        s.op([(f, 0.0, HOLD), (f + 1, 1.0, HOLD)])                     # a digital fill: each segment snaps on
    for i, (pct, f0, f1) in enumerate([("30%", 28, 55), ("60%", 55, 91), ("100%", 91, n)]):   # each label appears with its segment
        T(k, f"Percent {i + 1}", pct, x0 + segs * (w + gap) - gap, 450, 34, COL['cyan'], f0=f0, dur=f1 - f0, align='right', track=1.2)
    flick(T(k, "Done", "COMPLETE", x0, 600, 34, COL['amber'], f0=91, dur=n - 91, track=1.4))


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
            h = k.ngon(f"Hex {i + 1}", x, y, 2 * r - 10, 6, COL['dim'], f0=0, dur=n)
            h.nofill(); h.stroke(COL['dim'], 2, cap='butt')
            dist = math.hypot(x - 960, y - 540)
            f = int(dist / 40)                                          # a ring of light spreads from the centre
            h.op([(0, 0.0, HOLD), (f, 1.0, HOLD), (f + 2, 0.3, HOLD), (f + 4, 1.0, HOLD)])
            i += 1
    core = k.ngon("Core hex", 960, 540, 2 * r - 10, 6, COL['cyan'], f0=0, dur=n); gl(core, 10, 0.55)
    flick(core)


def signal_bars(d):
    n = 120
    k = d.comp("FH Signal bars", n, "fsg"); lab_bg(k, n)
    flick(T(k, "Signal label", "SIGNAL ANALYSIS", 600, 330, 30, COL['dim'], f0=0, dur=n, track=1.4))
    rnd = random.Random(7)
    for i in range(16):
        x = 620 + i * 44
        b = k.rect(f"Bar {i + 1}", x, 400, 28, 300, COL['cyan'] if i % 5 else COL['amber'], f0=0, dur=n)   # baseline y 700
        b.set('transformOrigin', '50% 100%'); gl(b, 4, 0.45)
        keys = [(0, [1.0, 0.0], HOLD)]
        for j, f in enumerate(range(4 + i, n, 12)):                       # stepped levels, a new reading every 12 f
            keys.append((f, [1.0, round(0.15 + 0.85 * rnd.random(), 3)], HOLD))
        b.scale(keys)


def target_lock(d):
    n = 90
    k = d.comp("FH Target lock", n, "ftl"); lab_bg(k, n)
    cx, cy = 1180, 470
    for i, o in enumerate(corner_set(k, "Lock corner", cx, cy, 200, 200, 36, 0, px=5)):
        sx, sy = [(-1, -1), (1, -1), (1, 1), (-1, 1)][i]
        bx, by = o.base
        o.pos([(0, (bx + sx * 320, by + sy * 320), 'Linear'), (24, (bx, by), EXPO)])
        o.op([(0, 0.0, 'Linear'), (4, 1.0, 'Linear')])
        o.rot([(0, -90.0, 'Linear'), (24, 0.0, EXPO)])                    # the old kit stored +90 (counter-clockwise)
    dot = k.ell("Target", cx, cy, 20, 20, COL['amber'], f0=0, dur=n); gl(dot, 8, 0.55); flick(dot)
    ln = line(k, "Lock leader", [(cx + 110, cy - 110), (cx + 220, cy - 200), (cx + 440, cy - 200)], COL['amber'], px=3, f0=26, dur=n - 26)
    ln.trim([(26, 0.0, 'Linear'), (38, 1.0, EXPO)])
    flick(T(k, "Lock text", "LOCKED", cx + 240, cy - 236, 40, COL['amber'], f0=34, dur=n - 34, track=1.4))
    flick(T(k, "Lock data", "RANGE 1.2 KM", cx + 240, cy - 166, 26, COL['dim'], f0=40, dur=n - 40, track=1.3))


def alert_banner(d):
    n = 120
    k = d.comp("FH Alert banner", n, "fal"); lab_bg(k, n)
    band = k.rect("Alert band", 960, 540, 1000, 150, css('2A1B05'), f0=0, dur=n, center=True)
    scan_open(band, sx=1.6)
    for i, y in enumerate((465, 615)):
        e = k.rect(f"Alert edge {i + 1}", 960, y, 1000, 6, COL['amber'], f0=0, dur=n, center=True); gl(e, 8, 0.5)
        scan_open(e, sx=1.6)
    t = T(k, "Alert text", "WARNING  //  HULL BREACH", 960, 540, 64, COL['amber'], f0=8, dur=n - 8, align='center', track=1.3)
    gl(t, 8, 0.45)
    # two slow pulses (1 a second, well under 3 flashes a second), then steady
    t.op([(8, 0.0, HOLD), (10, 1.0, HOLD), (40, 0.35, HOLD), (48, 1.0, HOLD), (70, 0.35, HOLD), (78, 1.0, HOLD)])


def map_ping(d):
    n = 120
    k = d.comp("FH Map ping", n, "fmp"); lab_bg(k, n)
    cx, cy = 820, 560
    for i in range(3):
        f = i * 20
        rg = k.ell(f"Ping ring {i + 1}", cx, cy, 200, 200, None, f0=f, dur=40); rg.stroke(COL['cyan'], 4); gl(rg, 6, 0.45)
        rg.scale([(f, 0.1, 'Linear'), (f + 40, 2.2, BEZ['decel'])])        # rings only grow: one way
        rg.op([(f, 1.0, 'Linear'), (f + 40, 0.0, 'Linear')])
    dot = k.ell("Ping dot", cx, cy, 26, 26, COL['amber'], f0=0, dur=n); gl(dot, 8, 0.55); flick(dot)
    line(k, "Ping leader", [(cx + 20, cy - 20), (cx + 120, cy - 120), (cx + 420, cy - 120)], COL['dim'], px=2, f0=10, dur=n - 10).trim(
        [(10, 0.0, 'Linear'), (24, 1.0, EXPO)])
    flick(T(k, "Ping coords", "47.3769 N  8.5417 E", cx + 140, cy - 156, 30, COL['cyan'], f0=20, dur=n - 20, track=1.2))
    flick(T(k, "Ping name", "RELAY STATION 3", cx + 140, cy - 84, 26, COL['dim'], f0=26, dur=n - 26, track=1.4))


def scan_wipe(d):
    n = 30
    k = d.comp("FH Scan wipe", n, "fsw")
    pan = k.rect("Scan panel", 960, 500, 1000, 1000, COL['grid'], f0=0, dur=n, center=True)   # top edge at y 0; scale y 1.08 reaches 1080
    pan.set('transformOrigin', '50% 0%')                                  # grows down from the top edge
    pan.scale([(0, [1.92, 0.0], 'Linear'), (12, [1.92, 1.08], BEZ['smooth']), (16, [1.92, 1.08], 'Linear'), (n, [1.92, 0.0], BEZ['accel'])])
    beam = k.rect("Scan beam", 960, 540, 1000, 6, COL['cyan'], f0=0, dur=n, center=True); beam.sc([1.92, 1.0]); gl(beam, 12, 0.6)
    bx, by = beam.base
    e = 4                                                               # keep the beam 4 px inside the frame while it waits
    beam.pos([(0, (bx, e), 'Linear'), (12, (bx, 1080 - e), BEZ['smooth']), (16, (bx, 1080 - e), 'Linear'), (n, (bx, e), BEZ['accel'])])


def build(path=None, m=None):
    d = HDoc()
    id_lower_third(d); loader(d); hex_grid(d); signal_bars(d); target_lock(d); alert_banner(d); map_ping(d); scan_wipe(d)
    return d


if __name__ == "__main__":
    print(__doc__)
