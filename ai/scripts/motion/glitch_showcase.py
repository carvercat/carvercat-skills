"""Write the glitch/gl-showcase sample project: the Glitch lab comps cut together into one
5.5 s sting with a glitch cut and a noise overlay (direct project-file authoring).

    import glitch_showcase as SH; presets, masks = SH.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); for each MASKS
pair (content, window) run mask.make {ids:[window, content]} - the FIRST id is the mask -
then parent.clear; edit.save; lint, look and qc (flashes) the master.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import glitch_lab as L

LENGTH = 165


def build(path, m=None):
    d = L.Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    L.PRESETS.clear(); L.MASKS.clear()
    L.rgb_title(d); L.slice_shift(d); L.noise_bars(d); L.glitch_cut(d)
    comps = {c.name: c for c in d.comps}
    for name, drop in (("GL Noise bars", ("Lab bg",)), ("GL Glitch cut", ("Scene A", "Scene B"))):   # overlays: no backgrounds
        comps[name].vtracks = [t for t in comps[name].vtracks if t[0].get("label") not in drop]
    master = d.comp("Glitch showcase", LENGTH, "gshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL['bg'], f0=0, dur=LENGTH)
    master.nest("GL RGB title", comps["GL RGB title"], f0=0, dur=90)
    master.nest("GL Slice shift", comps["GL Slice shift"], f0=90, dur=75)
    master.nest("GL Glitch cut", comps["GL Glitch cut"], f0=75, dur=30)        # its f15 lands on the cut at 90
    master.nest("GL Noise bars", comps["GL Noise bars"], f0=105, dur=60)
    d.save()
    return L.PRESETS, L.MASKS
