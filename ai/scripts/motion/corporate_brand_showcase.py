"""The corporate-brand/cb-showcase sample project in design units: the Corporate Brand lab comps cut together into one 14 s brand
film (logo, title card, three stats, lower third), each placed as a nested comp.

    import corporate_brand_showcase as SH; doc = SH.build(); doc.send(client, PROJECT.carverproj)

The lab comps (corporate_brand_lab.py) are nested into a master with comp.place; the lower third drops its background so it sits on
a gradient plate that keeps moving with the Photo push. After sending: lint, look and qc the master.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corporate_luxury_kit import Doc, push, place_scaled, lgrad
import corporate_brand_lab as L

SCENES = [("CB Logo resolve", 0, 90), ("CB Title card", 90, 90), ("CB Three stats", 180, 90), ("CB Lower third", 270, 150)]
LENGTH = 420


def build():
    d = Doc()
    L.title_card(d); L.lower_third(d, bg=False); L.logo_resolve(d); L.three_stats(d)
    comps = {c.name: c for c in d.comps}
    master = d.comp("Corporate brand showcase", LENGTH, "cshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL['navy'], f0=0, dur=LENGTH)
    # stand-in footage under the lower third: a gradient plate that keeps moving with the Photo push (5 s)
    plate = master.rect("Footage stand-in", 960, 540, 1920, 1080, L.COL['navy2'], f0=270, dur=150, center=True)
    plate.gradient([(0.0, L.COL['navy2']), (1.0, L.COL['teal'])], (0, 0), (1920, 1080))
    push(plate, 270, 149)
    for name, f0, dur in SCENES:
        if name in ("CB Title card", "CB Three stats"):       # long holds keep a slow 3% push
            place_scaled(master, comps[name], f0, [(f0, 1.0, 'Linear'), (f0 + dur - 1, 1.03, 'Linear')])
        else:
            master.nest(comps[name], f0=f0)
    return d


if __name__ == "__main__":
    print(__doc__)
