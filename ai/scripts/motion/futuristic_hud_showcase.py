"""Write the futuristic-hud/fh-showcase sample project in design units: the Futuristic HUD round-1 lab comps cut together into one 13 s reel,
each placed as a nested comp.

    import futuristic_hud_showcase as SH; doc = SH.build(); doc.send(client, PROJECT.carverproj)

The four comps are the lab's (futuristic_hud_lab.py); the master places them one after another over a background with comp.place
(cc2 Comp.nest). After sending: lint, look and qc the master.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import futuristic_hud_lab as L
from futuristic_hud_lab import HDoc

SCENES = [("FH Brackets", 0, 75), ("FH Readout", 75, 100), ("FH Radar", 175, 120), ("FH Reticle", 295, 90)]
LENGTH = 385


def build(path=None, m=None):
    del L.ORIGINS[:]
    d = HDoc()
    L.reticle(d); L.brackets(d); L.readout(d); L.radar(d)
    comps = {c.name: c for c in d.comps}
    master = d.comp("Futuristic HUD showcase", LENGTH, "hshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL["bg"], f0=0, dur=LENGTH)
    for name, f0, dur in SCENES:
        master.nest(comps[name], f0=f0, dur=dur)
    d.comps = [c for c in d.comps if c is not master] + [master]      # the lab comps first, the master last (and open)
    return d


if __name__ == "__main__":
    print(__doc__)
