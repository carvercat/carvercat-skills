"""Write the futuristic-hud/fh-showcase sample project: the Futuristic HUD lab comps cut
together into one 13 s reel (direct project-file authoring).

    import futuristic_hud_showcase as SH; presets, masks = SH.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); edit.save;
lint and look the master.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import futuristic_hud_lab as L

SCENES = [("FH Brackets", 0, 75), ("FH Readout", 75, 100), ("FH Radar", 175, 120), ("FH Reticle", 295, 90)]
LENGTH = 385


def build(path, m=None):
    d = L.Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    L.PRESETS.clear(); L.MASKS.clear()
    L.reticle(d); L.brackets(d); L.readout(d); L.radar(d)
    comps = {c.name: c for c in d.comps}
    master = d.comp("Futuristic HUD showcase", LENGTH, "hshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL["bg"], f0=0, dur=LENGTH)
    for name, f0, dur in SCENES:
        master.nest(name, comps[name], f0=f0, dur=dur)
    d.save()
    return L.PRESETS, L.MASKS
