"""Write the Funky lab comps into a .carverproj (direct project-file authoring).

    import funky_lab as L; presets, masks = L.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); edit.save.
Check with carvercat_inspect and carvercat_look; extract templates with
comp_to_template.py (--drop "Lab bg").

Continuous motion after an entrance is one-directional (linear rotation or drift), never a
back-and-forth loop: lint reads a ping-pong as jitter.
Fonts: Rethink Sans must be installed (KI-136).
Docs: ai/patterns/funky.md. Pixel space 1920x1080, y down; comp frames, 30 fps.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author"))
from cc import Doc, lin, P, BEZ

COL = dict(peach=lin('FFE8D6'), purple=lin('7B2FF7'), orange=lin('FF7A00'), pink=lin('FF4FA3'), teal=lin('00C2A8'),
           ink=lin('1B1035'), yellow=lin('FFD000'), white=lin('FFFFFF'))
EXPO, BACK = BEZ['expo'], BEZ['back']
PRESETS, MASKS = [], []


def lab_bg(k, n):
    k.rect("Lab bg", 0, 0, 1920, 1080, COL['peach'], f0=0, dur=n)


def zigzag(x0, x1, y, amp, steps):
    return [(x0 + (x1 - x0) * i / steps, y + (amp if i % 2 else -amp)) for i in range(steps + 1)]


def memphis(d):
    n = 90
    k = d.comp("FK Memphis shapes", n, "fms"); lab_bg(k, n)
    items = [("Triangle", lambda f: k.ngon("Triangle", 420, 300, 220, 3, COL['purple'], f0=f, dur=n - f)),
             ("Circle", lambda f: k.ell("Circle", 1500, 260, 200, 200, COL['orange'], f0=f, dur=n - f)),
             ("Squiggle", lambda f: k.line("Squiggle", zigzag(1180, 1620, 780, 40, 8), COL['teal'], px=18, f0=f, dur=n - f)),
             ("Dot", lambda f: k.ell("Dot", 520, 800, 220, 220, COL['pink'], f0=f, dur=n - f)),
             ("Ring", lambda f: k.ell("Ring", 960, 540, 300, 300, None, f0=f, dur=n - f)),
             ("Star", lambda f: k.star("Star", 1280, 470, 180, 5, 0.45, COL['yellow'], f0=f, dur=n - f))]
    for i, (name, make) in enumerate(items):
        f = i * 3
        o = make(f)
        if name == "Ring": o.stroke(COL['ink'], 14)
        PRESETS.append(("FK Memphis shapes", name, "Tilt pop"))
        spin = 25 if i % 2 else -25                       # one-way drift spin after the pop
        o.rot([(f + 18, 0.0, 'Linear'), (n, spin, 'Linear')])


def offset_title(d):
    n = 90
    k = d.comp("FK Offset title", n, "fot"); lab_bg(k, n)
    t = k.text("Title", "GROOVY", 960, 520, 240, COL['orange'], f0=0, dur=n, style='ExtraBold', align='center')
    PRESETS.append(("FK Offset title", "Title", "Tilt pop"))
    # the offset shadow is the native Drop shadow on the same text (hard: softness 0), so no second text overlaps it
    fx = t.shadow(x=0.0, y=0.0, soft=0.0, op=1.0)
    r, g, b = COL['purple'][:3]
    t.set(fx + '.red', r).set(fx + '.green', g).set(fx + '.blue', b)
    t.key(fx + '.x', [(14, 0.0, 'Linear'), (24, round(14 / 1920, 5), EXPO)])     # steps out 14 px right and 14 px down
    t.key(fx + '.y', [(14, 0.0, 'Linear'), (24, round(-14 / 1920, 5), EXPO)])
    wave = k.line("Wave", zigzag(640, 1280, 700, 18, 10), COL['teal'], px=14, f0=18, dur=n - 18)
    wave.trim([(18, 0.0, 'Linear'), (36, 1.0, EXPO)], which='end')


def zigzag_ribbon(d):
    n = 60
    k = d.comp("FK Zigzag ribbon", n, "fzr"); lab_bg(k, n)
    rib = k.line("Ribbon", zigzag(120, 1800, 540, 120, 9), COL['pink'], px=44, f0=0, dur=n)
    tp = rib.trim([(0, 0.0, 'Linear'), (24, 1.0, BEZ['smooth'])], which='end')
    rib.key(tp + '.start', [(18, 0.0, 'Linear'), (44, 1.0, BEZ['smooth'])])           # the tail chases the head: a snake


def sticker_stack(d):
    n = 75
    k = d.comp("FK Sticker stack", n, "fss"); lab_bg(k, n)
    stickers = [("NEW", COL['yellow'], COL['ink'], 760, 460, -8), ("HOT", COL['pink'], COL['white'], 1120, 520, 6),
                ("WOW", COL['teal'], COL['ink'], 940, 640, -3)]
    for i, (word, bg, fg, x, y, ang) in enumerate(stickers):
        f = i * 8
        card = k.rect(f"Sticker {i + 1}", x, y, 300, 170, bg, r=28, f0=f, dur=n - f, center=True)
        card.stroke(COL['ink'], 8); card.shadow(y=-0.006, soft=0.004, op=0.35)
        label = k.text(f"Sticker label {i + 1}", word, x, y, 84, fg, f0=f, dur=n - f, style='ExtraBold', align='center')
        for o in (card, label):
            o.rotv(float(ang))
            o.scale([(f, 1.45, 'Linear'), (f + 8, 1.0, BACK)])
            o.op([(f, 0, 'Linear'), (f + 2, 1, 'Linear')])


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    memphis(d); offset_title(d); zigzag_ribbon(d); sticker_stack(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
