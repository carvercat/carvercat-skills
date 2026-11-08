"""Write the data-viz/dv-showcase sample project in design units: the Data Viz lab comps cut together into one 11.5 s master, each
scene placed as a nested comp (cc2 Comp.nest).

    import data_viz_showcase as SH; doc = SH.build(); doc.send(client, PROJECT.carverproj)

The long readable holds (line chart, ranked bars) keep a slow 3 % push, keyed on their instance after the placing (KDoc.send).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data_viz_lab as L
from dvsu_kit import KDoc

SCENES = [("DV Line chart", 0), ("DV Ranked bars", 90), ("DV Donut", 180), ("DV Gauge", 270)]
LENGTH = 345


def build():
    d = KDoc()
    L.line_chart(d); L.donut(d); L.ranked_bars(d); L.gauge(d)
    comps = {c.name: c for c in d.comps}
    master = d.comp("Data viz showcase", LENGTH, "dshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL['bg'], f0=0, dur=LENGTH)
    for name, f0 in SCENES:
        master.nest(comps[name], f0=f0)
        if name in ("DV Line chart", "DV Ranked bars"):
            master.nest_edit(name, f0, scale=[(f0, 1.0, 'Linear'), (f0 + comps[name].length, 1.03, 'Linear')])
    return d


if __name__ == "__main__":
    print(__doc__)
