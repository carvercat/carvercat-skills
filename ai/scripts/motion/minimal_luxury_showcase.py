"""The minimal-luxury/ml-showcase sample project in design units: the Minimal Luxury lab comps cut together into one 15.5 s film
(tracked title, feather wipe, product frame, slow quote), each placed as a nested comp.

    import minimal_luxury_showcase as SH; doc = SH.build(); doc.send(client, PROJECT.carverproj)

After sending: lint, look and qc the master.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corporate_luxury_kit import Doc, place_scaled
import minimal_luxury_lab as L

SCENES = [("ML Tracked title", 0, 120), ("ML Feather wipe", 120, 75), ("ML Product frame", 195, 120), ("ML Slow quote", 315, 150)]
LENGTH = 465


def build():
    d = Doc()
    L.tracked_title(d); L.feather_wipe(d); L.product_frame(d); L.slow_quote(d)
    comps = {c.name: c for c in d.comps}
    master = d.comp("Minimal luxury showcase", LENGTH, "lshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL["bg"], f0=0, dur=LENGTH)
    for name, f0, dur in SCENES:
        if name == "ML Feather wipe":                     # its 30 f hold drifts
            place_scaled(master, comps[name], f0, [(f0, 1.0, 'Linear'), (f0 + dur - 1, 1.02, 'Linear')])
        else:
            master.nest(comps[name], f0=f0)
    return d


if __name__ == "__main__":
    print(__doc__)
