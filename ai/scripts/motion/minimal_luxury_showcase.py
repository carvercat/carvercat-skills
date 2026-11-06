"""Write the minimal-luxury/ml-showcase sample project: the Minimal Luxury lab comps cut
together into one 15.5 s film (direct project-file authoring).

    import minimal_luxury_showcase as SH; presets, masks = SH.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); for each MASKS
pair (content, window) run mask.make {ids:[window, content]} - the FIRST id is the mask -
then parent.clear; edit.save; lint and look the master.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import minimal_luxury_lab as L

SCENES = [("ML Tracked title", 0, 120), ("ML Feather wipe", 120, 75), ("ML Product frame", 195, 120), ("ML Slow quote", 315, 150)]
LENGTH = 465


def build(path, m=None):
    d = L.Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    L.PRESETS.clear(); L.MASKS.clear()
    L.tracked_title(d); L.feather_wipe(d); L.product_frame(d); L.slow_quote(d)
    comps = {c.name: c for c in d.comps}
    master = d.comp("Minimal luxury showcase", LENGTH, "lshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL["bg"], f0=0, dur=LENGTH)
    for name, f0, dur in SCENES:
        o = master.nest(name, comps[name], f0=f0, dur=dur)
        if name == "ML Feather wipe":                     # its 30 f hold drifts
            o.scale([(f0, 1.0, "Linear"), (f0 + dur, 1.02, "Linear")])
    d.save()
    return L.PRESETS, L.MASKS
