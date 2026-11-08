"""Retro round 2 in design units: eight more lab comps (70s stripe lower third, VHS overlay, groovy badge, neon sign, chrome
title, TV switch-off, arcade start screen, venetian blinds).

    import retro_lab2 as L; doc = L.build(); doc.send(client, PROJECT.carverproj)

Same palette and "on twos" rule as retro_lab.py (whose helpers this uses): twos() steps every other frame with Hold keys.
Blinks and neon flickers use Hold keys at least 4 f apart (lint same_frame_keys), and never more than 3 flashes a second.
Check with carvercat_inspect (curves, lint, qc) and carvercat_look; extract templates with regen_pack.py.
Design units: 1920 x 1080 px, degrees clockwise. Docs: ai/patterns/retro.md.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from retro_lab import (PDoc, text_gradient, COL, EXPO, W, H, css, twos, hold_keys, anchor, glow, hard_shadow, text, line, lab_bg)


def stripe_lower_third(d):
    n = 150
    k = d.comp("RT Stripe lower third", n, "rlt"); lab_bg(k, n)
    for i, col in enumerate((COL['orange'], COL['mustard'], COL['teal'])):
        s = k.rect(f"LT stripe {i + 1}", 120, 930 + i * 22, 760, 16, col, r=8, f0=0, dur=n)
        f = i * 4
        anchor(s, -1, 0)
        s.scale(twos(f, f + 14, [0.0, 1.0], [1.0, 1.0]) + twos(n - 22 + f // 2, n - 10 + f // 2, [1.0, 1.0], [0.0, 1.0], 'accel')[1:])
    plate = k.rect("LT plate", 120, 800, 620, 116, COL['brown'], r=24, f0=6, dur=n - 6)
    d.preset(k, plate, "Rise - on twos"); d.preset(k, plate, "Exit down - on twos")
    name = text(k, "LT name", "Rosa Delgado", 160, 834, 54, COL['cream'], f0=10, dur=n - 10, style='ExtraBold', align='left')
    d.preset(k, name, "Rise - on twos"); d.preset(k, name, "Exit down - on twos")
    role = text(k, "LT role", "HOST, KITCHEN HOUR", 160, 896, 28,   # audit 2026-10-28: 6.6 px gap to the name before
                COL['mustard'], f0=14, dur=n - 14, style='SemiBold', align='left', track=1.3)
    d.preset(k, role, "Rise - on twos"); d.preset(k, role, "Exit down - on twos")


def vhs_overlay(d):
    n = 120
    k = d.comp("RT VHS overlay", n, "rvh"); lab_bg(k, n, css('2B2B33'))
    white = css('F2F2F2')
    text(k, "VHS play", "PLAY", 140, 140, 64, white, f0=0, dur=n, style='Bold', align='left', track=1.2)
    k.ngon("VHS arrow", 400, 140, 56, 3, white, f0=0, dur=n)               # a 3-gon at 0 deg points right
    dot = k.ell("REC dot", 1640, 140, 40, 40, css('E53935'), f0=0, dur=n)
    dot.op(hold_keys([(0, 1.0)] + [(f, 0.0 if (f // 15) % 2 else 1.0) for f in range(15, n, 15)]))   # blinks once a second
    text(k, "REC label", "REC", 1680, 140, 52, white, f0=0, dur=n, style='Bold', align='left')
    text(k, "VHS time", "SP  0:04:27", 140, 960, 52, white, f0=0, dur=n, style='Bold', align='left', track=1.1)
    text(k, "VHS date", "OCT 27 1989", 1780, 960, 52, white, f0=0, dur=n, style='Bold', align='right', track=1.1)


def groovy_badge(d):
    n = 90
    k = d.comp("RT Groovy badge", n, "rgb"); lab_bg(k, n)
    b = k.star("Badge scallop", 960, 520, 560, 20, 0.86, COL['orange'], f0=0, dur=n)
    d.preset(k, b, "Pop - on twos")
    b.rot([(12, 0.0, 'Linear'), (n, -12.0, 'Linear')])
    ring = k.ell("Badge ring", 960, 520, 420, 420, None, f0=4, dur=n - 4)
    ring.stroke(COL['cream'], 8).set('strokeDasharray', '18 14')
    d.preset(k, ring, "Pop - on twos")
    d.preset(k, text(k, "Badge top", "FAR OUT", 960, 470, 96, COL['cream'], f0=8, dur=n - 8, style='ExtraBold'), "Rise - on twos")
    d.preset(k, text(k, "Badge bottom", "DEALS", 960, 580, 72, COL['brown'], f0=12, dur=n - 12, style='ExtraBold'), "Rise - on twos")


def neon_sign(d):
    n = 120
    k = d.comp("RT Neon sign", n, "rns"); lab_bg(k, n, COL['night'])
    t = text(k, "Neon word", "OPEN LATE", 960, 500, 170, COL['pink'], f0=0, dur=n, style='Bold', track=1.1)
    glow(t, 18, 0.55)
    # warming up: off, short on, off, on, dim, on - Hold keys 4+ f apart, under 3 flashes a second
    t.op(hold_keys([(0, 0.0), (6, 0.8), (10, 0.1), (16, 1.0), (24, 0.4), (30, 1.0)]))
    u = glow(line(k, "Neon underline", [(600, 640), (1320, 640)], COL['cyan'], 8, f0=0, dur=n), 14, 0.55)
    u.op(hold_keys([(0, 0.0), (20, 1.0), (26, 0.3), (32, 1.0)]))
    small = text(k, "Neon small", "diner  &  bar", 960, 730, 64, COL['cyan'], f0=34, dur=n - 34, style='Medium', track=1.3)
    glow(small, 10, 0.45)
    d.preset(k, small, "Rise - on twos")


CHROME = [(0.0, css('9EE7FF')), (0.48, css('F2FBFF')), (0.52, css('3A2A6E')), (1.0, css('E07BFF'))]


def chrome_title(d):
    n = 90
    k = d.comp("RT Chrome title", n, "rch"); lab_bg(k, n, COL['night'])
    hz = glow(line(k, "Chrome horizon", [(160, 640), (1760, 640)], COL['pink'], 4, f0=0, dur=n), 10, 0.55)
    hz.trim(twos(0, 14, 0.0, 1.0))
    t = text(k, "Chrome word", "TURBO", 960, 500, 240, COL['cyan'], f0=4, dur=n - 4, style='ExtraBold', track=1.1)
    # a static chrome gradient on the text: sky, bright band, dark horizon (top of the letters to the bottom of the box)
    text_gradient(t, CHROME)
    d.preset(k, t, "Rise - on twos")
    d.preset(k, text(k, "Chrome sub", "RACING  1986", 960, 720, 56, COL['yellow'], f0=16, dur=n - 16, style='Bold', track=1.4), "Rise - on twos")


def tv_off(d):
    n = 24
    k = d.comp("RT TV off", n, "rtv")
    k.rect("TV black", 0, 0, W, H, css('000000'), f0=0, dur=n)          # cut to this at f0: the set is off behind the glow
    scr = k.rect("TV screen", 960, 540, 1000, 1000, css('F2F2F2'), f0=0, dur=n, center=True)
    # the picture collapses to a bright line, then to a dot, then goes dark - classic CRT switch-off (on twos)
    scr.scale(twos(0, 8, [1.92, 1.08], [1.92, 0.006], 'accel') + twos(8, 16, [1.92, 0.006], [0.01, 0.006], 'accel')[1:])
    scr.op(hold_keys([(0, 1.0), (16, 1.0), (20, 0.0)]))


def arcade_start(d):
    n = 150
    k = d.comp("RT Arcade start", n, "ras"); lab_bg(k, n, COL['night'])
    d.preset(k, text(k, "Arcade score", "HI-SCORE  048200", 960, 260, 56, COL['yellow'], f0=0, dur=n, style='Bold', track=1.2), "Rise - on twos")
    title = text(k, "Arcade title", "STAR RACER", 960, 480, 180, COL['pink'], f0=6, dur=n - 6, style='ExtraBold', track=1.1)
    hard_shadow(title, COL['cyan'], 12, 12)
    d.preset(k, title, "Pop - on twos")
    ps = text(k, "Arcade press", "PRESS START", 960, 760, 64, css('F2F2F2'), f0=30, dur=n - 30, style='Bold', track=1.3)
    # blinks: 30 f on, 15 f off (one flash every 1.5 s); the first on-phase covers lint's reading time
    seq, f, on = [(30, 1.0)], 60, False
    while f < n:
        seq.append((f, 1.0 if on else 0.0)); f += 30 if not on else 15; on = not on
    ps.op(hold_keys(seq))
    text(k, "Arcade credit", "CREDIT 01", 1760, 1000, 36, COL['cyan'], f0=0, dur=n, style='Bold', align='right', track=1.2)


def blinds(d):
    n = 54                                                                # the last slat (f14) leaves f44-52
    k = d.comp("RT Blinds", n, "rbl")
    cols = [COL['orange'], COL['mustard'], COL['teal'], COL['red']]
    for i in range(8):
        y = i * 135 + 67.5
        s = k.rect(f"Blind {i + 1}", 960, y, 1000, 136, cols[i % 4], f0=0, dur=n, center=True)
        anchor(s, 0, 1)                                                   # each slat opens downward from its top edge
        f = i * 2
        s.scale(twos(f, f + 8, [1.92, 0.0], [1.92, 1.0]) + twos(f + 30, f + 38, [1.92, 1.0], [1.92, 0.0], 'accel')[1:])   # all closed f22-30


def comps(d):
    stripe_lower_third(d); vhs_overlay(d); groovy_badge(d); neon_sign(d); chrome_title(d); tv_off(d); arcade_start(d); blinds(d)


def build():
    d = PDoc(); comps(d)
    return d


if __name__ == "__main__":
    print(__doc__)
