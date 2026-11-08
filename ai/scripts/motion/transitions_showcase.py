"""Write the transitions/tx-showcase sample project in design units: eight stand-in scenes cut together through the seven cover
transitions, each placed as a nested comp so its cover frame lands on the cut.

    import transitions_showcase as SH; doc = SH.build(); doc.send(client, PROJECT.carverproj)

The seven transition comps are the lab's (transitions_lab.py) without their stand-in "Scene A" / "Scene B"; each is placed in
the master with comp.place (cc2 Comp.nest) on a track above the scenes. After sending: lint, look and qc the master.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author"))
import transitions_lab as L
from cc2 import Doc, css

# (comp, the comp frame to put on the cut)
TRANSITIONS = [("TX Slide wipe", 18), ("TX Diagonal wipe", 18), ("TX Split doors", 18), ("TX Bars stagger", 20),
               ("TX Clock wipe", 20), ("TX Bubble cover", 20), ("TX Dip to colour", 15)]
SCENE = 45
COLOURS = ['2B3A67', 'E8D6B3', '496A81', 'D98E73', '1F2333', 'F2C14E', '3B6EF6', 'F7F7FA']
LIGHT = (1, 5, 7)                       # scenes with dark ink


def build():
    d = Doc()
    for f in (L.slide_wipe, L.diagonal_wipe, L.split_doors, L.bars_stagger, L.clock_wipe, L.bubble_cover, L.dip_to_colour):
        f(d)
    comps = {c.name: c for c in d.comps}
    for name, _ in TRANSITIONS:                                    # overlays: drop the stand-in scenes
        c = comps[name]; c.objs = [o for o in c.objs if o.name not in ("Scene A", "Scene B")]
    n = SCENE * len(COLOURS)
    master = d.comp("Transitions showcase", n, "xshow")
    for i, hexcol in enumerate(COLOURS):
        master.rect(f"Scene {i + 1}", 0, 0, 1920, 1080, css(hexcol), f0=i * SCENE, dur=SCENE)
        ink = css('14151C') if i in LIGHT else css('FFFFFF')
        master.text(f"Scene {i + 1} label", f"SCENE {i + 1}", 960, 540, 120, ink, f0=i * SCENE, dur=SCENE, weight=800)
    for i, (name, cut) in enumerate(TRANSITIONS):
        master.nest(comps[name], f0=(i + 1) * SCENE - cut, track='top')
    d.comps = [c for c in d.comps if c is not master] + [master]   # the lab comps first, the master last (and open)
    return d


if __name__ == "__main__":
    print(__doc__)
