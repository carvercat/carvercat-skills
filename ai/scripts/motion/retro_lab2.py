"""Retro round 2: eight more lab comps (70s stripe lower third, VHS overlay, groovy badge,
neon sign, chrome title, TV switch-off, arcade start screen, venetian blinds), written
straight into a .carverproj.

    import retro_lab2 as L; presets, masks = L.build(PROJECT.carverproj)

Same palette and "on twos" rule as retro_lab.py: twos() steps every other frame with Hold
keys. Blinks and neon flickers use Hold keys at least 4 f apart (lint same_frame_keys), and
never more than 3 flashes a second. After writing: edit.open {path, force:true}; apply
PRESETS (preset.apply); edit.save; check with carvercat_inspect (curves, lint, qc) and
carvercat_look; extract templates with comp_to_template.py (--drop "Lab bg").
Docs: ai/patterns/retro.md.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from retro_lab import Doc, lin, P, COL, EXPO, lab_bg, twos
from cc import BEZ

PRESETS, MASKS = [], []


def hold_keys(seq):
    """[(frame, value)] -> Hold-stepped key spec"""
    return [(f, v, 'Linear' if i == 0 else 'Hold') for i, (f, v) in enumerate(seq)]


def stripe_lower_third(d):
    n = 150
    k = d.comp("RT Stripe lower third", n, "rlt"); lab_bg(k, n)
    for i, col in enumerate((COL['orange'], COL['mustard'], COL['teal'])):
        s = k.rect(f"LT stripe {i + 1}", 120, 930 + i * 22, 760, 16, col, r=8, f0=0, dur=n)
        f = i * 4
        s.anchor(-1, 0)
        s.scale(twos(f, f + 14, [0.0, 1.0], [1.0, 1.0]) + twos(n - 22 + f // 2, n - 10 + f // 2, [1.0, 1.0], [0.0, 1.0], 'accel')[1:])
    plate = k.rect("LT plate", 120, 800, 620, 116, COL['brown'], r=24, f0=6, dur=n - 6)
    PRESETS.extend([("RT Stripe lower third", "LT plate", "Rise - on twos"), ("RT Stripe lower third", "LT plate", "Exit down - on twos")])
    k.text("LT name", "Rosa Delgado", 160, 834, 54, COL['cream'], f0=10, dur=n - 10, style='ExtraBold')
    PRESETS.extend([("RT Stripe lower third", "LT name", "Rise - on twos"), ("RT Stripe lower third", "LT name", "Exit down - on twos")])
    k.text("LT role", "HOST, KITCHEN HOUR", 160, 896, 28,   # audit 2026-10-28: 6.6 px gap to the name before
           COL['mustard'], f0=14, dur=n - 14, style='SemiBold', track=1.3)
    PRESETS.extend([("RT Stripe lower third", "LT role", "Rise - on twos"), ("RT Stripe lower third", "LT role", "Exit down - on twos")])


def vhs_overlay(d):
    n = 120
    k = d.comp("RT VHS overlay", n, "rvh"); lab_bg(k, n, lin('2B2B33'))
    white = lin('F2F2F2')
    play = k.text("VHS play", "PLAY", 140, 140, 64, white, f0=0, dur=n, style='Bold', track=1.2)
    tri = k.ngon("VHS arrow", 400, 140, 56, 3, white, f0=0, dur=n)          # a 3-gon at 0 deg points right
    dot = k.ell("REC dot", 1640, 140, 40, 40, lin('E53935'), f0=0, dur=n)
    dot.op(hold_keys([(0, 1.0)] + [(f, 0.0 if (f // 15) % 2 else 1.0) for f in range(15, n, 15)]))   # blinks once a second
    k.text("REC label", "REC", 1680, 140, 52, white, f0=0, dur=n, style='Bold')
    k.text("VHS time", "SP  0:04:27", 140, 960, 52, white, f0=0, dur=n, style='Bold', track=1.1)
    k.text("VHS date", "OCT 27 1989", 1780, 960, 52, white, f0=0, dur=n, style='Bold', align='right', track=1.1)


def groovy_badge(d):
    n = 90
    k = d.comp("RT Groovy badge", n, "rgb"); lab_bg(k, n)
    b = k.star("Badge scallop", 960, 520, 560, 20, 0.86, COL['orange'], f0=0, dur=n)
    PRESETS.append(("RT Groovy badge", "Badge scallop", "Pop - on twos"))
    b.rot([(12, 0.0, 'Linear'), (n, 12.0, 'Linear')])
    inner = k.ell("Badge ring", 960, 520, 420, 420, None, f0=4, dur=n - 4); inner.stroke(COL['cream'], 8, line='dashed', dash=18, gap=14)
    PRESETS.append(("RT Groovy badge", "Badge ring", "Pop - on twos"))
    t = k.text("Badge top", "FAR OUT", 960, 470, 96, COL['cream'], f0=8, dur=n - 8, style='ExtraBold', align='center')
    PRESETS.append(("RT Groovy badge", "Badge top", "Rise - on twos"))
    k.text("Badge bottom", "DEALS", 960, 580, 72, COL['brown'], f0=12, dur=n - 12, style='ExtraBold', align='center')
    PRESETS.append(("RT Groovy badge", "Badge bottom", "Rise - on twos"))


def neon_sign(d):
    n = 120
    k = d.comp("RT Neon sign", n, "rns"); lab_bg(k, n, COL['night'])
    t = k.text("Neon word", "OPEN LATE", 960, 500, 170, COL['pink'], f0=0, dur=n, style='Bold', align='center', track=1.1)
    t.set(t.src('text_fill', 'glow'), 4.0); t.glow(size=18, amount=0.55)
    # warming up: off, short on, off, on, dim, on - Hold keys 4+ f apart, under 3 flashes a second
    t.op(hold_keys([(0, 0.0), (6, 0.8), (10, 0.1), (16, 1.0), (24, 0.4), (30, 1.0)]))
    u = k.line("Neon underline", [(600, 640), (1320, 640)], COL['cyan'], px=8, f0=0, dur=n); u.glow(size=14, amount=0.55)
    u.op(hold_keys([(0, 0.0), (20, 1.0), (26, 0.3), (32, 1.0)]))
    k.text("Neon small", "diner  &  bar", 960, 730, 64, COL['cyan'], f0=34, dur=n - 34, style='Medium', align='center', track=1.3).glow(size=10, amount=0.45)
    PRESETS.append(("RT Neon sign", "Neon small", "Rise - on twos"))


def chrome_title(d):
    n = 90
    k = d.comp("RT Chrome title", n, "rch"); lab_bg(k, n, COL['night'])
    hz = k.line("Chrome horizon", [(160, 640), (1760, 640)], COL['pink'], px=4, f0=0, dur=n); hz.glow(size=10, amount=0.55)
    hz.trim(twos(0, 14, 0.0, 1.0))
    t = k.text("Chrome word", "TURBO", 960, 500, 240, COL['cyan'], f0=4, dur=n - 4, style='ExtraBold', align='center', track=1.1)
    # a static chrome gradient on the text (text gradients are static on 0.1.6, KI-009 c): sky, bright band, dark horizon.
    # Endpoints are object-local, y down: [0.5, 0] is the top of the word (KI-155; was [0.5, 1] -> [0.5, 0], upside down)
    t.set(t.src('text_fill', 'paint'), 'gradient')
    t.set(t.src('text_fill', 'gradient'), {'mode': 'linear', 'start': [0.5, 0.0], 'end': [0.5, 1.0], 'stops': [
        {'p': p, 'color': c[:3], 'a': 1} for p, c in [(0.0, lin('9EE7FF')), (0.48, lin('F2FBFF')), (0.52, lin('3A2A6E')), (1.0, lin('E07BFF'))]]})
    PRESETS.append(("RT Chrome title", "Chrome word", "Rise - on twos"))
    k.text("Chrome sub", "RACING  1986", 960, 720, 56, COL['yellow'], f0=16, dur=n - 16, style='Bold', align='center', track=1.4)
    PRESETS.append(("RT Chrome title", "Chrome sub", "Rise - on twos"))


def tv_off(d):
    n = 24
    k = d.comp("RT TV off", n, "rtv")
    k.rect("TV black", 0, 0, 1920, 1080, lin('000000'), f0=0, dur=n)          # cut to this at f0: the set is off behind the glow
    scr = k.rect("TV screen", 960, 540, 1000, 1000, lin('F2F2F2'), f0=0, dur=n, center=True)
    # the picture collapses to a bright line, then to a dot, then goes dark - classic CRT switch-off (on twos)
    scr.scale(twos(0, 8, [1.92, 1.08], [1.92, 0.006], 'accel') + twos(8, 16, [1.92, 0.006], [0.01, 0.006], 'accel')[1:])
    scr.op(hold_keys([(0, 1.0), (16, 1.0), (20, 0.0)]))


def arcade_start(d):
    n = 150
    k = d.comp("RT Arcade start", n, "ras"); lab_bg(k, n, COL['night'])
    k.text("Arcade score", "HI-SCORE  048200", 960, 260, 56, COL['yellow'], f0=0, dur=n, style='Bold', align='center', track=1.2)
    PRESETS.append(("RT Arcade start", "Arcade score", "Rise - on twos"))
    title = k.text("Arcade title", "STAR RACER", 960, 480, 180, COL['pink'], f0=6, dur=n - 6, style='ExtraBold', align='center', track=1.1)
    fx = title.shadow(x=round(12 / 1920, 5), y=round(-12 / 1920, 5), soft=0.0, op=1.0)
    r, g, b = COL['cyan'][:3]; title.set(fx + '.red', r).set(fx + '.green', g).set(fx + '.blue', b)
    PRESETS.append(("RT Arcade start", "Arcade title", "Pop - on twos"))
    ps = k.text("Arcade press", "PRESS START", 960, 760, 64, lin('F2F2F2'), f0=30, dur=n - 30, style='Bold', align='center', track=1.3)
    # blinks: 30 f on, 15 f off (one flash every 1.5 s); the first on-phase covers lint's reading time
    seq, f, on = [(30, 1.0)], 60, False
    while f < n:
        seq.append((f, 1.0 if on else 0.0)); f += 30 if not on else 15; on = not on
    ps.op(hold_keys(seq))
    k.text("Arcade credit", "CREDIT 01", 1760, 1000, 36, COL['cyan'], f0=0, dur=n, style='Bold', align='right', track=1.2)


def blinds(d):
    n = 54                                                                # the last slat (f14) leaves f44-52
    k = d.comp("RT Blinds", n, "rbl")
    cols = [COL['orange'], COL['mustard'], COL['teal'], COL['red']]
    for i in range(8):
        y = i * 135 + 67.5
        s = k.rect(f"Blind {i + 1}", 960, y, 1000, 136, cols[i % 4], f0=0, dur=n, center=True)
        s.sc([1.92, 1.0]); s.anchor(0, 1)                                 # each slat opens downward from its top edge
        f = i * 2
        s.scale(twos(f, f + 8, [1.92, 0.0], [1.92, 1.0]) + twos(f + 30, f + 38, [1.92, 1.0], [1.92, 0.0], 'accel')[1:])   # all closed f22-30


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    stripe_lower_third(d); vhs_overlay(d); groovy_badge(d); neon_sign(d); chrome_title(d); tv_off(d); arcade_start(d); blinds(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
