"""Glitch round 2: eight more lab comps (glitch lower third, block-artifact title, error
cascade, terminal type-on, stutter words, RGB split mark, tracking band, pixel dissolve),
written straight into a .carverproj.

    import glitch_lab2 as L; presets, masks = L.build(PROJECT.carverproj)

Same palette and rules as glitch_lab.py: every change is stepped (Hold keys), random event
frames are at least 4 f apart (lint same_frame_keys), opacity blips stay small and few, and
everything that jumps stays inside the frame. After writing: edit.open {path, force:true};
apply PRESETS (preset.apply); edit.save; check with carvercat_inspect (curves, lint, qc for
flashes) and carvercat_look; extract templates with comp_to_template.py (--drop "Lab bg").
Docs: ai/patterns/glitch.md.
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from glitch_lab import Doc, lin, P, COL, lab_bg, held
from cc import BEZ

PRESETS, MASKS = [], []


def rgb_shadows(t, amp, frames, rng, settle_at, op=0.85):
    """two hard drop shadows (red, cyan) whose X offsets jump on Hold keys, then settle to 0"""
    for col, sign in ((COL['red'], -1), (COL['cyan'], 1)):
        fx = t.shadow(x=0.0, y=0.0, soft=0.0, op=op)
        r, g, b = col[:3]; t.set(fx + '.red', r).set(fx + '.green', g).set(fx + '.blue', b)
        xs = [(f, sign * rng.choice(amp)) for f in frames] + [(settle_at, 0)]
        t.key(fx + '.x', held([(f, round(px / 1920, 5)) for f, px in xs]))


def lower_third(d):
    n = 150
    k = d.comp("GL Lower third", n, "glt"); lab_bg(k, n)
    rng = random.Random(21)
    bar = k.rect("LT bar", 120, 820, 12, 150, COL['red'], f0=0, dur=n)
    bar.op(held([(0, 0.0), (2, 1.0), (6, 0.3), (10, 1.0)]))
    PRESETS.append(("GL Lower third", "LT bar", "Glitch out"))
    nm = k.text("LT name", "NOVA_K", 160, 860, 72, COL['white'], f0=2, dur=n - 2, style='ExtraBold')
    rgb_shadows(nm, (8, 14, 22), [2, 6, 10, 14], rng, 18)
    PRESETS.extend([("GL Lower third", "LT name", "Glitch in"), ("GL Lower third", "LT name", "Glitch out")])
    rl = k.text("LT role", "SYSTEMS ARTIST", 160, 930, 32, COL['green'], f0=10, dur=n - 10, style='SemiBold', track=1.3)
    PRESETS.extend([("GL Lower third", "LT role", "Glitch in"), ("GL Lower third", "LT role", "Glitch out")])


def block_title(d):
    n = 90
    k = d.comp("GL Block title", n, "gbt"); lab_bg(k, n)
    t = k.text("Block word", "CORRUPTED", 960, 540, 190, COL['white'], f0=0, dur=n, style='ExtraBold', align='center')
    PRESETS.append(("GL Block title", "Block word", "Glitch stretch hit"))
    rng = random.Random(4)
    for i in range(9):                                                   # block artefacts over the word for the first 20 f
        w, h = rng.choice((80, 120, 200)), rng.choice((40, 60, 90))
        x, y = rng.randint(500, 1420 - w), rng.randint(440, 640 - h)
        f0 = rng.choice((0, 4, 8, 12)); dur = rng.choice((2, 4))
        b = k.rect(f"Block {i + 1}", x, y, w, h, (COL['red'], COL['cyan'], COL['green'], COL['white'])[i % 4], f0=f0, dur=dur)
        b.opv(0.75)
    k.line("Block rule", [(560, 680), (1360, 680)], COL['red'], px=6, f0=20, dur=n - 20).trim(held([(20, 0.0), (22, 0.4), (24, 0.7), (26, 1.0)]))


def error_cascade(d):
    n = 120
    k = d.comp("GL Error cascade", n, "gec"); lab_bg(k, n)
    for i in range(4):
        f = 8 + i * 8
        x, y = 520 + i * 50, 300 + i * 50
        win = k.rect(f"Error window {i + 1}", x, y, 720, 300, lin('C8C8C8'), f0=f, dur=n - f); win.stroke(COL['bg'], 4)
        k.rect(f"Error bar {i + 1}", x, y, 720, 52, lin('2B2BCC'), f0=f, dur=n - f)
        # only the top window carries text: lint does not see occlusion (stacked texts = text_overlap), and
        # texts that end when the next window lands (8 f) fail reading_time
        if i < 3: continue
        td = n - f
        k.text(f"Error title {i + 1}", "FATAL ERROR", x + 24, y + 26, 30, COL['white'], f0=f, dur=td, style='Bold', track=1.2)
        k.text(f"Error body {i + 1}", "Reality.exe has stopped responding", x + 40, y + 140, 32, COL['bg'], f0=f, dur=td, style='Medium')
        k.rect(f"Error button {i + 1}", x + 540, y + 220, 140, 52, lin('E8E8E8'), f0=f, dur=n - f).stroke(COL['bg'], 3)
        k.text(f"Error ok {i + 1}", "OK", x + 610, y + 246, 30, COL['bg'], f0=f, dur=td, style='Bold', align='center')


def terminal(d):
    n = 150
    k = d.comp("GL Terminal", n, "gtm"); lab_bg(k, n)
    lines = ["> connecting to node 7...", "> handshake ok", "> decrypting payload", "> ACCESS GRANTED"]
    for i, s in enumerate(lines):
        f = 6 + i * 26
        col = COL['green'] if i < 3 else COL['white']
        t = k.text(f"Term line {i + 1}", s, 300, 360 + i * 80, 44, col, f0=f, dur=n - f, style='SemiBold')
        rpo = f'src.e_src_text_relative_{t.id}.opacity'
        ents = t.clip['containers'].setdefault('effects', {'entries': [], 'promoted': []})['entries']
        ents.insert(0, {'id': f'e_fx_stagger_{t.id}', 'cap': 'stagger', 'on': True, 'by': 'character', 'order': 'forward',
                        'amount': 1.0, 'amountMode': 'each', 'seed': 1, 'connected': [rpo]})
        t.key(rpo, [(f, 0, 'Linear'), (f + 1, 1, 'Hold')])              # types on, 1 f per character
    from cc import textw
    cur = k.rect("Term cursor", 300 + textw(lines[-1], 44, 'SemiBold') + 10, 600 - 22, 26, 44, COL['white'], f0=104, dur=n - 104)
    spec, f, on = [(104, 1.0)], 118, False                              # after the last line has typed (f84 + 16 characters)
    while f < n:
        spec.append((f, 1.0 if on else 0.0)); f += 14; on = not on
    cur.op(held(spec))


def stutter_words(d):
    n = 100
    k = d.comp("GL Stutter words", n, "gsw"); lab_bg(k, n)
    for i, (w, col) in enumerate([("NO", COL['white']), ("SIGNAL", COL['red']), ("FOUND", COL['white'])]):
        f = i * 30
        dur = 30 if i < 2 else n - f
        t = k.text(f"Stutter {i + 1}", w, 960, 540, 260, col, f0=f, dur=dur, style='ExtraBold', align='center')
        PRESETS.append(("GL Stutter words", f"Stutter {i + 1}", "Glitch stretch hit"))
        bx, by = t.base
        t.pos(held([(f, [bx, by]), (f + 2, [bx + 24 / 1920, by]), (f + 6, [bx - 12 / 1920, by]), (f + 10, [bx, by])]))


def rgb_mark(d):
    n = 90
    k = d.comp("GL RGB mark", n, "grm"); lab_bg(k, n)
    rng = random.Random(9)
    jumps = [0, 3, 6, 9, 12, 40, 43, 46]
    for name, col, sign in (("Mark red", COL['red'], -1), ("Mark cyan", COL['cyan'], 1)):
        m = k.ngon(name, 960, 540, 420, 3, col, f0=0, dur=n, angle=90.0); m.opv(0.8)
        bx, by = m.base
        m.pos(held([(f, [bx + sign * rng.choice((10, 18, 30)) / 1920, by]) for f in jumps] + [(52, [bx + sign * 4 / 1920, by])]))
    core = k.ngon("Mark core", 960, 540, 420, 3, COL['white'], f0=0, dur=n, angle=90.0)
    PRESETS.append(("GL RGB mark", "Mark core", "Glitch in"))
    k.text("Mark word", "PRISM", 960, 860, 90, COL['white'], f0=14, dur=n - 14, style='ExtraBold', align='center', track=1.3)
    PRESETS.append(("GL RGB mark", "Mark word", "Glitch in"))


def tracking_band(d):
    n = 90
    k = d.comp("GL Tracking band", n, "gtb")
    band = k.rect("Track band", 960, 540, 1000, 140, COL['white'], f0=0, dur=n, center=True); band.sc([1.92, 1.0]); band.soft(40); band.opv(0.12)
    bx, by = band.base
    band.pos([(0, [bx, 1.0 + 0.0], 'Linear'), (n, [bx, 0.0], 'Linear')])  # rolls down the frame, one way
    rng = random.Random(13)
    for i in range(5):
        dy = rng.randint(-50, 50)
        w = rng.randint(300, 900)
        ln = k.rect(f"Track line {i + 1}", 960, 540, w, 4, COL['white'], f0=0, dur=n, center=True); ln.opv(0.35)
        lx, ly = ln.base
        xo = rng.randint(-400, 400) / 1920
        ln.pos([(0, [lx + xo, 1.0 + dy / 1080], 'Linear'), (n, [lx + xo, 0.0 + dy / 1080], 'Linear')])


def pixel_dissolve(d):
    n = 40
    k = d.comp("GL Pixel dissolve", n, "gpd")
    cols, rows, w, h = 12, 7, 160, 1080 / 7
    order = list(range(cols * rows)); random.Random(17).shuffle(order)
    for idx, cell in enumerate(order):
        r, c = divmod(cell, cols)
        on = 2 + idx * 14 // (cols * rows)                               # all on within f2-16
        off = 22 + idx * 14 // (cols * rows)                             # all off within f22-36
        ow, oh = (1 if c < cols - 1 else 0), (1 if r < rows - 1 else 0)  # 1 px overlap inside, no overhang past the frame
        k.rect(f"Pixel {cell + 1}", c * w, r * h, w + ow, h + oh, (COL['grey'], COL['bg'])[(r + c) % 2], f0=on, dur=off - on)


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    lower_third(d); block_title(d); error_cascade(d); terminal(d); stutter_words(d); rgb_mark(d); tracking_band(d); pixel_dissolve(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
