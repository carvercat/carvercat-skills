"""The cartoon-bounce/ct-showcase sample project in design units: the Cartoon Bounce lab comps cut together into one 10.8 s
cartoon reel.

    import cartoon_bounce_showcase as SH; doc = SH.build(); doc.send(client, PROJECT.carverproj)

The four lab comps (cartoon_bounce_lab.py) are nested in a master with comp.place (cc2 Comp.nest); library presets are applied
to the lab comps by PDoc. After sending: lint and look the master.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartoon_bounce_lab as L

SCENES = [("CT Bouncing ball", 0, 90), ("CT Smear whoosh", 90, 45), ("CT Blink face", 135, 100), ("CT Boing title", 235, 90)]
LENGTH = 325


def build():
    d = L.PDoc(L.PRESETS)
    L.PRESETS.clear()
    L.bouncing_ball(d); L.boing_title(d); L.blink_face(d); L.smear_whoosh(d)
    comps = {c.name: c for c in d.comps}
    master = d.comp("Cartoon bounce showcase", LENGTH, "tshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL['cream'], f0=0, dur=LENGTH)
    for name, f0, dur in SCENES:
        master.nest(comps[name], f0=f0, dur=dur)
    return d
