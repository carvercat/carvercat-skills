"""Write the corporate-brand/cb-showcase sample project: the Corporate Brand lab comps cut
together into one 14 s brand film (direct project-file authoring).

    import corporate_brand_showcase as SH; presets, masks = SH.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); for each MASKS
pair (content, window) run mask.make {ids:[window, content]} - the FIRST id is the mask -
then parent.clear; edit.save; lint and look the master.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import corporate_brand_lab as L

SCENES = [("CB Logo resolve", 0, 90), ("CB Title card", 90, 90), ("CB Three stats", 180, 90), ("CB Lower third", 270, 150)]
LENGTH = 420


def build(path, m=None):
    d = L.Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    L.PRESETS.clear(); L.MASKS.clear()
    L.title_card(d); L.lower_third(d, bg=False); L.logo_resolve(d); L.three_stats(d)
    comps = {c.name: c for c in d.comps}
    master = d.comp("Corporate brand showcase", LENGTH, "cshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL['navy'], f0=0, dur=LENGTH)
    # stand-in footage under the lower third: a gradient plate that keeps moving with the Photo push - 5 s preset
    plate = master.rect("Footage stand-in", 960, 540, 1920, 1080, L.COL['navy2'], f0=270, dur=150, center=True)
    plate.gradient([(0.0, L.COL['navy2']), (1.0, L.COL['teal'])], (0, 0), (1920, 1080))
    L.PRESETS.append(("Corporate brand showcase", "Footage stand-in", "Photo push - 5 s"))
    for name, f0, dur in SCENES:
        o = master.nest(name, comps[name], f0=f0, dur=dur)
        if name in ("CB Title card", "CB Three stats"):       # long holds keep a slow 3% push
            o.scale([(f0, 1.0, 'Linear'), (f0 + dur, 1.03, 'Linear')])
    d.save()
    return L.PRESETS, L.MASKS
