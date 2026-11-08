"""The funky/fk-showcase sample project in design units: the Funky lab comps cut together into one 10.5 s reel.

    import funky_showcase as SH; doc = SH.build(); doc.send(client, PROJECT.carverproj)

The lab comps (funky_lab.py) are nested in a master with comp.place (cc2 Comp.nest); library presets are applied to them by
PDoc. After sending: lint and look the master.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import funky_lab as L

SCENES = [("FK Memphis shapes", 0, 90), ("FK Offset title", 90, 90), ("FK Sticker stack", 180, 75)]
LENGTH = 315


def build():
    d = L.PDoc(L.PRESETS)
    L.PRESETS.clear()
    L.memphis(d); L.offset_title(d); L.zigzag_ribbon(d); L.sticker_stack(d)
    comps = {c.name: c for c in d.comps}
    master = d.comp("Funky showcase", LENGTH, "fshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL["peach"], f0=0, dur=LENGTH)
    for name, f0, dur in SCENES:
        master.nest(comps[name], f0=f0, dur=dur)
    master.nest(comps["FK Zigzag ribbon"], f0=255, dur=60)   # the snake closes the reel
    return d
