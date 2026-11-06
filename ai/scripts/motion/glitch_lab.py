"""Write the Glitch lab comps into a .carverproj (direct project-file authoring).

    import glitch_lab as L; presets, masks = L.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); for each MASKS
pair (content, window) run mask.make {ids:[window, content]} - the FIRST id is the mask -
then parent.clear; edit.save. Check with carvercat_inspect (curves, lint, qc for flashes)
and carvercat_look; extract templates with comp_to_template.py (--drop "Lab bg").

Glitches are stepped: keys with easing Hold jump on the frame they arrive. Keep stepped
opacity changes small and few (qc: no flashes) - photosensitivity matters most here.
Fonts: Rethink Sans must be installed (KI-136).
Docs: ai/patterns/glitch.md. Pixel space 1920x1080, y down; comp frames, 30 fps.
"""
import os, sys, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author"))
from cc import Doc, lin, P, BEZ

COL = dict(bg=lin('0A0A0A'), white=lin('F2F2F2'), red=lin('FF2A55'), cyan=lin('00E5FF'), green=lin('39FF14'), grey=lin('2A2A2A'))
PRESETS, MASKS = [], []


def lab_bg(k, n):
    k.rect("Lab bg", 0, 0, 1920, 1080, COL['bg'], f0=0, dur=n)


def held(spec):
    """[(frame, value)] -> key specs with Hold arriving (stepped jumps)"""
    return [(f, v, 'Linear' if i == 0 else 'Hold') for i, (f, v) in enumerate(spec)]


def rgb_title(d):
    n = 90
    k = d.comp("GL RGB title", n, "grt"); lab_bg(k, n)
    t = k.text("Title", "SIGNAL LOST", 960, 540, 170, COL['white'], f0=0, dur=n, style='ExtraBold', align='center')
    PRESETS.append(("GL RGB title", "Title", "Glitch in"))
    rng = random.Random(7)
    for name, col, sign in (("red", COL['red'], -1), ("cyan", COL['cyan'], 1)):
        fx = t.shadow(x=0.0, y=0.0, soft=0.0, op=0.85)          # two hard drop shadows = the split channels
        r, g, b = col[:3]; t.set(fx + '.red', r).set(fx + '.green', g).set(fx + '.blue', b)
        xs = [(0, sign * 18), (3, sign * 30), (6, sign * 10), (9, sign * 24), (12, sign * 6), (15, sign * 14)]
        xs += [(f, sign * rng.choice((4, 6, 8))) for f in range(20, n - 4, 14)]
        t.key(fx + '.x', held([(f, round(px / 1920, 5)) for f, px in xs]))


def slice_shift(d):
    n = 75
    k = d.comp("GL Slice shift", n, "gss"); lab_bg(k, n)
    cx, cy, size, bands = 960, 540, 460, 5
    bh = size / bands
    rng = random.Random(3)
    for i in range(bands):
        mark = k.ngon(f"Mark {i + 1}", cx, cy, size, 6, COL['green'], f0=0, dur=n, angle=30.0)
        mark.stroke(COL['white'], 10)
        bx, by = mark.base
        jumps = [(0, 0)] + [(f, rng.choice((-60, -30, 30, 45, 80)) * (1 if i % 2 else -1)) for f in (12, 15, 18, 21)] + [(24, 0)]
        jumps += [(52, rng.choice((-40, 40))), (55, 0)]
        mark.pos(held([(f, [bx + dx / 1920, by]) for f, dx in jumps]))
        top = cy - size / 2 + i * bh
        k.rect(f"Band {i + 1}", cx - size, top, size * 2, bh + 1, COL['white'], f0=0, dur=n)
        MASKS.append(("GL Slice shift", f"Mark {i + 1}", f"Band {i + 1}"))


def noise_bars(d):
    n = 60
    k = d.comp("GL Noise bars", n, "gnb"); lab_bg(k, n)
    rng = random.Random(11)
    for i in range(6):
        y = rng.randint(120, 960); h = rng.choice((6, 10, 18, 30)); w = rng.randint(500, 1600)
        col = (COL['white'], COL['cyan'], COL['red'])[i % 3]
        bar = k.rect(f"Noise bar {i + 1}", 0, y, w, h, col, f0=0, dur=n)
        on = sorted(rng.sample(range(2, n - 4, 4), 3))           # 4 f apart: each 2 f blip ends before the next starts
        spec = [(0, 0.0)]
        for f in on: spec += [(f, round(rng.uniform(0.15, 0.35), 2)), (f + 2, 0.0)]
        bar.op(held(spec))
        bx, by = bar.base
        bar.pos(held([(0, [bx, by])] + [(f, [bx + rng.randint(-200, 400) / 1920, by]) for f in on]))
    track = k.rect("Tracking bar", 0, 0, 1920, 46, COL['white'], f0=0, dur=n)
    track.opv(0.06)
    tx, ty = track.base
    track.pos([(0, [tx, ty + 50 / 1080], 'Linear'), (n, [tx, ty - 1100 / 1080], 'Linear')])


def glitch_cut(d):
    n = 30
    k = d.comp("GL Glitch cut", n, "ggc")
    k.rect("Scene A", 0, 0, 1920, 1080, COL['grey'], f0=0, dur=15)
    k.rect("Scene B", 0, 0, 1920, 1080, COL['bg'], f0=15, dur=15)
    rng = random.Random(5)
    for i in range(7):
        y = rng.randint(60, 1000); h = rng.choice((20, 40, 70, 110)); w = rng.randint(900, 1920)
        col = (COL['red'], COL['cyan'], COL['white'])[i % 3]
        f0 = 9 + rng.randint(0, 3); dur = rng.choice((4, 6, 8))
        bar = k.rect(f"Cut bar {i + 1}", rng.randint(0, 1920 - w), y, w, h, col, f0=f0, dur=dur)   # inside the frame
        bx, by = bar.base
        room_l, room_r = int(bx * 1920 - w / 2), int(1920 - bx * 1920 - w / 2)
        dx = rng.randint(-min(240, room_l), min(240, room_r)) if w < 1920 else 0
        bar.pos(held([(f0, [bx, by]), (f0 + 2, [bx + dx / 1920, by])]))
        bar.opv(0.55)


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    rgb_title(d); slice_shift(d); noise_bars(d); glitch_cut(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
