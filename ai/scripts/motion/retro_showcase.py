"""Write the retro/rt-showcase sample project: the Retro lab comps cut
together into one 9.5 s reel (direct project-file authoring).

    import retro_showcase as SH; presets, masks = SH.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); edit.save;
lint and look the master.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import retro_lab as L

SCENES = [("RT Sunburst title", 0, 90), ("RT Rainbow stripes", 90, 75), ("RT Synthwave", 165, 120)]
LENGTH = 285


def build(path, m=None):
    d = L.Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    L.PRESETS.clear(); L.MASKS.clear()
    L.sunburst(d); L.synthwave(d); L.stripes(d); L.checker_wipe(d)
    comps = {c.name: c for c in d.comps}
    cw = comps["RT Checker wipe"]                          # an overlay: drop its own lab background or it hides the cut
    cw.vtracks = [t for t in cw.vtracks if t[0].get("label") != "Lab bg"]
    master = d.comp("Retro showcase", LENGTH, "rshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL["cream"], f0=0, dur=LENGTH)
    for name, f0, dur in SCENES:
        master.nest(name, comps[name], f0=f0, dur=dur)
    # the checkerboard covers the frame from its f22 to f28 (master 161-167): the cut to the synthwave scene (165) happens under it
    master.nest("RT Checker wipe", comps["RT Checker wipe"], f0=139, dur=54)
    d.save()
    return L.PRESETS, L.MASKS
