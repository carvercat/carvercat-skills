"""Funky round 2: eight more lab comps (tilted lower third, sale badge, swing headline, pattern
drift background, squiggle underline, orbit end card, photo stack, star cover transition),
written straight into a .carverproj.

    import funky_lab2 as L; presets, masks = L.build(PROJECT.carverproj)

Same palette and rules as funky_lab.py: rotation is part of every entrance, and anything
that keeps moving moves ONE way (lint reads ping-pong as jitter). The orbit end card is
rigged: the orbiting shapes are parented to a visible centre disc, and in the project file a
parented child's position is an offset from the comp centre (see cartoon_bounce_lab2.rig).
After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); edit.save; check
with carvercat_inspect and carvercat_look; extract templates with comp_to_template.py
(--drop "Lab bg"). Docs: ai/patterns/funky.md.
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from funky_lab import Doc, lin, P, COL, EXPO, BACK, lab_bg, zigzag
from cartoon_bounce_lab2 import rig
from cc import BEZ

PRESETS, MASKS = [], []


def hard_shadow(t, col, dx=12, dy=12, f=None):
    fx = t.shadow(x=round(dx / 1920, 5), y=round(-dy / 1920, 5), soft=0.0, op=1.0)
    r, g, b = col[:3]
    t.set(fx + '.red', r).set(fx + '.green', g).set(fx + '.blue', b)
    return fx


def lower_third(d):
    n = 150
    k = d.comp("FK Lower third", n, "flt"); lab_bg(k, n)
    blk = k.rect("Name block", 470, 860, 660, 120, COL['purple'], r=20, f0=0, dur=n, center=True); blk.rotv(-4.0)
    blk.stroke(COL['ink'], 8)
    PRESETS.extend([("FK Lower third", "Name block", "Slide in - wiggle"), ("FK Lower third", "Name block", "Spin out")])
    nm = k.text("Name", "DJ PAPAYA", 470, 855, 72, COL['yellow'], f0=4, dur=n - 4, style='ExtraBold', align='center'); nm.rotv(-4.0)
    PRESETS.extend([("FK Lower third", "Name", "Tilt pop"), ("FK Lower third", "Name", "Spin out")])
    tag = k.rect("Tag", 760, 950, 300, 64, COL['teal'], r=32, f0=10, dur=n - 10, center=True); tag.rotv(3.0); tag.stroke(COL['ink'], 6)
    PRESETS.extend([("FK Lower third", "Tag", "Tilt pop"), ("FK Lower third", "Tag", "Spin out")])
    tg = k.text("Tag text", "LIVE TONIGHT", 760, 950, 32, COL['ink'], f0=12, dur=n - 12, style='ExtraBold', align='center'); tg.rotv(3.0)
    PRESETS.extend([("FK Lower third", "Tag text", "Spin in"), ("FK Lower third", "Tag text", "Spin out")])


def sale_badge(d):
    n = 90
    k = d.comp("FK Sale badge", n, "fsb"); lab_bg(k, n)
    st = k.star("Badge", 960, 520, 520, 16, 0.82, COL['pink'], f0=0, dur=n); st.stroke(COL['ink'], 10)
    PRESETS.append(("FK Sale badge", "Badge", "Spin in"))
    st.addkeys(st.tr('rotation'), [(20, 0.0, 'Linear'), (n, 30.0, 'Linear')])     # keeps turning one way
    t1 = k.text("Badge big", "50%", 960, 490, 150, COL['white'], f0=6, dur=n - 6, style='ExtraBold', align='center')
    hard_shadow(t1, COL['ink'], 8, 8)
    PRESETS.append(("FK Sale badge", "Badge big", "Tilt pop"))
    bs = k.text("Badge small", "OFF TODAY", 960, 610, 48, COL['ink'], f0=12, dur=n - 12, style='ExtraBold', align='center')
    bs.rot([(12, -12.0, 'Linear'), (24, 0.0, BACK)])                  # rotation in every entrance (Stamp has none)
    PRESETS.append(("FK Sale badge", "Badge small", "Stamp"))      # Tilt pop starts at 0: small text fails lint text_too_small


def swing_headline(d):
    n = 90
    k = d.comp("FK Swing headline", n, "fsw"); lab_bg(k, n)
    t = k.text("Headline", "Get your groove on", 960, 500, 130, COL['purple'], f0=0, dur=n, style='ExtraBold', align='center')
    hard_shadow(t, COL['orange'], 10, 10)
    PRESETS.append(("FK Swing headline", "Headline", "Words swing in"))
    w = k.line("Wave", zigzag(560, 1360, 640, 16, 12), COL['teal'], px=12, f0=24, dur=n - 24)
    w.trim([(24, 0.0, 'Linear'), (42, 1.0, EXPO)])


def pattern_drift(d):
    n = 150
    k = d.comp("FK Pattern drift", n, "fpd")
    k.rect("Pattern ground", 0, 0, 1920, 1080, COL['yellow'], f0=0, dur=n)
    cols = [COL['pink'], COL['teal'], COL['purple'], COL['orange']]
    step, drift = 240, 240                       # a slow one-way diagonal drift (not a seamless loop)
    i = 0
    for r in range(-1, 6):
        for c in range(-1, 9):
            x, y = c * step + (step / 2 if r % 2 else 0), r * 216
            # keep only cells that are on screen at some point of the drift (+240 px right, 216 px down): a cell that is
            # off frame for its whole clip is a lint ERROR (never_visible)
            if not any(-20 < x + drift * t < 1940 and -20 < y + 216 * t < 1100 for t in [j / 20 for j in range(21)]):
                continue
            shape = i % 3
            if shape == 0: o = k.ell(f"Dot {i + 1}", x, y, 56, 56, cols[i % 4], f0=0, dur=n)
            elif shape == 1: o = k.ngon(f"Tri {i + 1}", x, y, 64, 3, cols[i % 4], f0=0, dur=n)
            else: o = k.rect(f"Bar {i + 1}", x, y, 70, 18, cols[i % 4], r=9, f0=0, dur=n, center=True)
            bx, by = o.base
            o.pos([(0, [bx, by], 'Linear'), (n, [bx + drift / 1920, by - drift * 0.9 / 1080], 'Linear')])
            i += 1


def squiggle_underline(d):
    n = 90
    k = d.comp("FK Squiggle underline", n, "fsq"); lab_bg(k, n)
    k.text("Phrase", "Totally fresh", 960, 480, 150, COL['ink'], f0=0, dur=n, style='ExtraBold', align='center')
    PRESETS.append(("FK Squiggle underline", "Phrase", "Tilt pop"))
    sq = k.line("Squiggle", zigzag(560, 1360, 600, 22, 14), COL['pink'], px=16, f0=12, dur=n - 12)
    sq.trim([(12, 0.0, 'Linear'), (30, 1.0, EXPO)])
    for i, (x, y, col) in enumerate([(500, 360, COL['teal']), (1430, 380, COL['orange']), (1400, 640, COL['purple'])]):
        s = k.star(f"Spark {i + 1}", x, y, 70, 4, 0.4, col, f0=20 + i * 4, dur=n - 20 - i * 4)
        PRESETS.append(("FK Squiggle underline", f"Spark {i + 1}", "Spin in"))


def orbit_end_card(d):
    n = 150
    k = d.comp("FK Orbit end card", n, "foe"); lab_bg(k, n)
    hub = k.ell("Orbit hub", 960, 500, 300, 300, COL['purple'], f0=0, dur=n); hub.stroke(COL['ink'], 10)
    PRESETS.append(("FK Orbit end card", "Orbit hub", "Tilt pop"))
    sats = []
    for i, col in enumerate([COL['orange'], COL['teal'], COL['pink'], COL['yellow']]):
        a = math.radians(i * 90)
        x, y = 960 + 260 * math.cos(a), 500 + 260 * math.sin(a)
        s = k.ell(f"Satellite {i + 1}", x, y, 60, 60, col, f0=0, dur=n); s.stroke(COL['ink'], 6)
        sats.append(s)
    rig(sats, hub)
    hub.addkeys(hub.tr('rotation'), [(18, 0.0, 'Linear'), (n, 120.0, 'Linear')])   # the satellites orbit with it, one way
    ht = k.text("Hub text", "BYE!", 960, 500, 110, COL['yellow'], f0=8, dur=n - 8, style='ExtraBold', align='center')
    ht.rot([(8, -14.0, 'Linear'), (22, 0.0, BACK)])
    PRESETS.append(("FK Orbit end card", "Hub text", "Stamp"))      # Tilt pop from 0 failed lint text_too_small at 110 px
    k.text("Follow", "@papaya.beats", 960, 850, 56, COL['ink'], f0=24, dur=n - 24, style='ExtraBold', align='center')
    PRESETS.append(("FK Orbit end card", "Follow", "Slide in - wiggle"))


def photo_stack(d):
    n = 120
    k = d.comp("FK Photo stack", n, "fps"); lab_bg(k, n)
    for i, (x, y, ang, col) in enumerate([(760, 520, -9, COL['teal']), (1000, 500, 5, COL['orange']), (1180, 560, -3, COL['pink'])]):
        f = i * 10
        frame = k.rect(f"Photo {i + 1}", x, y, 420, 500, COL['white'], r=10, f0=f, dur=n - f, center=True)
        frame.stroke(COL['ink'], 6); frame.shadow(y=-0.006, soft=0.004, op=0.35); frame.rotv(float(ang))
        PRESETS.append(("FK Photo stack", f"Photo {i + 1}", "Slide in - wiggle"))
        pic = k.rect(f"Picture {i + 1}", x, y - 40, 360, 360, col, f0=f, dur=n - f, center=True); pic.rotv(float(ang))
        PRESETS.append(("FK Photo stack", f"Picture {i + 1}", "Slide in - wiggle"))


def star_cover(d):
    n = 36
    k = d.comp("FK Star cover", n, "fsc")
    s = k.star("Cover star", 960, 540, 1000, 8, 0.6, COL['orange'], f0=0, dur=n)
    # drawn 1000 px (KI-137); inner radius 300 px x 4.0 = 1200 > the 1101 px half-diagonal, so it covers at 4.0
    s.scale([(0, 0.0, 'Linear'), (15, 4.0, BEZ['smooth']), (21, 4.0, 'Linear'), (n, 0.0, BEZ['smooth'])])
    s.rot([(0, -90.0, 'Linear'), (n, 90.0, 'Linear')])


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    lower_third(d); sale_badge(d); swing_headline(d); pattern_drift(d); squiggle_underline(d); orbit_end_card(d)
    photo_stack(d); star_cover(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
