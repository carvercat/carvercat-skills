"""Write the Retro lab comps into a .carverproj (direct project-file authoring).

    import retro_lab as L; presets, masks = L.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); edit.save.
Check with carvercat_inspect and carvercat_look; extract templates with
comp_to_template.py (--drop "Lab bg").

"On twos": twos() keys a move on every other frame with easing Hold (the arriving key
jumps), the stepped look of 12-drawings-a-second animation.
Fonts: Rethink Sans must be installed (KI-136).
Docs: ai/patterns/retro.md. Pixel space 1920x1080, y down; comp frames, 30 fps.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cc import Doc, lin, P, BEZ
from curves import named

COL = dict(cream=lin('F4E4C1'), orange=lin('E8772E'), mustard=lin('E3B23C'), brown=lin('5C3A21'), teal=lin('2A9D8F'),
           red=lin('C8553D'), night=lin('1A0B2E'), pink=lin('FF2E88'), yellow=lin('FFD319'), purple=lin('7A2BD8'), cyan=lin('2DE2E6'))
EXPO = BEZ['expo']
PRESETS, MASKS = [], []


def lab_bg(k, n, col=None):
    k.rect("Lab bg", 0, 0, 1920, 1080, col or COL['cream'], f0=0, dur=n)


def twos(f0, f1, frm, to, curve='expo-out'):
    """key specs [(frame, value, ease)] stepping on even frames (Hold) from f0 to f1"""
    out, f = [], f0
    def lerp(a, b, p):
        return [x + (y - x) * p for x, y in zip(a, b)] if isinstance(a, list) else a + (b - a) * p
    while f <= f1:
        p = 1.0 if f + 2 > f1 else named[curve]((f - f0) / (f1 - f0))
        out.append((f, lerp(frm, to, p), 'Linear' if not out else 'Hold')); f += 2
    return out


def sunburst(d):
    n = 90
    k = d.comp("RT Sunburst title", n, "rsb"); lab_bg(k, n)
    rays = k.star("Rays", 960, 540, 2600, 24, 0.12, COL['mustard'], f0=0, dur=n)
    rays.rot([(0, 0.0, 'Linear'), (n, 15.0, 'Linear')])
    rays.op(twos(0, 8, 0.0, 0.55, 'linear'))
    t = k.text("Title", "SINCE 1975", 960, 520, 160, COL['brown'], f0=6, dur=n - 6, style='ExtraBold', align='center')
    fx = t.shadow(x=round(10 / 1920, 5), y=round(-10 / 1920, 5), soft=0.0, op=1.0)
    r, g, b = COL['orange'][:3]; t.set(fx + '.red', r).set(fx + '.green', g).set(fx + '.blue', b)
    PRESETS.append(("RT Sunburst title", "Title", "Pop - on twos"))
    k.text("Subtitle", "FAMILY RECIPES", 960, 650, 44, COL['brown'], f0=14, dur=n - 14, style='SemiBold', align='center', track=1.4)
    PRESETS.append(("RT Sunburst title", "Subtitle", "Rise - on twos"))


def synthwave(d):
    n = 120
    k = d.comp("RT Synthwave", n, "rsw"); lab_bg(k, n, COL['night'])
    hy = 640
    sun = k.ell("Sun", 960, 440, 520, 520, COL['pink'], f0=0, dur=n)
    sun.gradient([(0.0, COL['yellow']), (1.0, COL['pink'])], (960, 180), (960, 700))
    sun.scale(twos(0, 16, 0.0, 1.0, 'expo-out'))
    for i in range(5):                                     # bands cut through the lower half, drifting up one way
        y = 520 + i * 34; h = 6 + i * 4
        bnd = k.rect(f"Band {i + 1}", 960, y, 600, h, COL['night'], f0=0, dur=n, center=True)
        bx, by = bnd.base
        bnd.pos([(0, [bx, by], 'Linear'), (n, [bx, by + 24 / 1080], 'Linear')])
    k.rect("Floor", 0, hy, 1920, 1080 - hy, COL['night'], f0=0, dur=n)
    k.line("Horizon", [(0, hy), (1920, hy)], COL['pink'], px=4, f0=0, dur=n).glow(size=10, amount=0.6)
    for i, xb in enumerate((-600, 0, 480, 960, 1440, 1920, 2520)):
        end = (xb, 1080)
        if xb < 0: end = (0, hy + (1080 - hy) * 960 / (960 - xb))            # stop at the frame edge (lint: cropped at rest)
        if xb > 1920: end = (1920, hy + (1080 - hy) * 960 / (xb - 960))
        gl = k.line(f"Grid V{i + 1}", [(960, hy), end], COL['purple'], px=3, f0=0, dur=n)
        gl.trim([(0, 0.0, 'Linear'), (20, 1.0, EXPO)], which='end')
    for i in range(6):                                     # horizontal grid lines run toward the viewer, accelerating
        f0 = i * 20; f1 = f0 + 40
        if f1 > n: break                                   # every line finishes its run inside the comp
        hl = k.line(f"Grid H{i + 1}", [(0, hy + 4), (1920, hy + 4)], COL['purple'], px=3, f0=f0, dur=min(n, f1) - f0)
        bx, by = hl.base
        hl.pos([(f0, [bx, by], 'Linear'), (f1, [bx, by - (1080 - hy) / 1080], 'Ease in')])
    t = k.text("Title", "NEON NIGHTS", 960, 860, 120, COL['cyan'], f0=20, dur=n - 20, style='ExtraBold', align='center', track=1.2)
    t.set(t.src('text_fill', 'glow'), 4.0)
    PRESETS.append(("RT Synthwave", "Title", "Rise - on twos"))


def stripes(d):
    n = 75
    k = d.comp("RT Rainbow stripes", n, "rrs"); lab_bg(k, n)
    for i, col in enumerate((COL['red'], COL['orange'], COL['mustard'], COL['teal'])):
        y = 600 + i * 30; f = i * 4
        s = k.rect(f"Stripe {i + 1}", 960, y, 1920, 26, col, f0=0, dur=n, center=True)
        s.anchor(-1, 0); s.scale(twos(f, f + 16, [0.0, 1.0], [1.0, 1.0], 'expo-out'))
    k.text("Title", "GROOVE RADIO", 960, 460, 150, COL['brown'], f0=14, dur=n - 14, style='ExtraBold', align='center')
    PRESETS.append(("RT Rainbow stripes", "Title", "Rise - on twos"))


def checker_wipe(d):
    n = 54                                                # the last diagonal (a = 22) is gone by f52
    k = d.comp("RT Checker wipe", n, "rcw"); lab_bg(k, n)
    cols, rows, w, h = 8, 5, 240, 216
    for r in range(rows):
        for c in range(cols):
            sq = k.rect(f"Square {r + 1}-{c + 1}", c * w + w / 2, r * h + h / 2, w + 1, h + 1,
                        COL['brown'] if (r + c) % 2 else COL['orange'], f0=0, dur=n, center=True)
            a = (r + c) * 2                               # the diagonal order
            sq.scale(twos(a, a + 6, 0.0, 1.0, 'expo-out') + twos(a + 24, a + 30, 1.0, 0.0, 'accel')[1:])   # covered f22-30


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    sunburst(d); synthwave(d); stripes(d); checker_wipe(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
