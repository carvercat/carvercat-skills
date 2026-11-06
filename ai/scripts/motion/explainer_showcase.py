"""Write the explainer/ex-showcase sample project: the Explainer lab comps cut
together into one 14.5 s explainer (direct project-file authoring).

    import explainer_showcase as SH; presets, masks = SH.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); edit.save;
lint and look the master.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explainer_lab as L

SCENES = [("EX Process steps", 0, 120), ("EX Icon grid", 120, 90), ("EX Callout", 210, 75), ("EX Timeline", 285, 150)]
LENGTH = 435


def build(path, m=None):
    d = L.Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    L.PRESETS.clear(); L.MASKS.clear()
    L.process_steps(d); L.icon_grid(d); L.callout(d); L.timeline(d)
    comps = {c.name: c for c in d.comps}
    master = d.comp("Explainer showcase", LENGTH, "eshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL["bg"], f0=0, dur=LENGTH)
    for name, f0, dur in SCENES:
        o = master.nest(name, comps[name], f0=f0, dur=dur)
        if name in ("EX Process steps", "EX Icon grid"):     # holds keep a slow 2% push
            o.scale([(f0, 1.0, "Linear"), (f0 + dur, 1.02, "Linear")])
    d.save()
    return L.PRESETS, L.MASKS
