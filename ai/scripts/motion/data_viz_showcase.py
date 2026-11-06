"""Write the data-viz/dv-showcase sample project: the Data Viz lab comps cut together
into one 11.5 s master (direct project-file authoring).

    import data_viz_showcase as SH; presets, masks = SH.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}, apply PRESETS (preset.apply), edit.save,
then lint and look the master.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data_viz_lab as L

SCENES = [("DV Line chart", 0, 90), ("DV Ranked bars", 90, 90), ("DV Donut", 180, 90), ("DV Gauge", 270, 75)]
LENGTH = 345


def build(path, m=None):
    d = L.Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    L.PRESETS.clear(); L.MASKS.clear()
    L.line_chart(d); L.donut(d); L.ranked_bars(d); L.gauge(d)
    comps = {c.name: c for c in d.comps}
    master = d.comp("Data viz showcase", LENGTH, "dshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL['bg'], f0=0, dur=LENGTH)
    for name, f0, dur in SCENES:
        o = master.nest(name, comps[name], f0=f0, dur=dur)
        if name in ("DV Line chart", "DV Ranked bars"):      # long readable holds keep a slow 3% push
            o.scale([(f0, 1.0, 'Linear'), (f0 + dur, 1.03, 'Linear')])
    d.save()
    return L.PRESETS, L.MASKS
