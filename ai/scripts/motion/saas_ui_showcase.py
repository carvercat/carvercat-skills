"""Write the saas-launch/saas-ui-showcase sample project in design units: the SaaS UI lab comps cut together into one 15.3 s master,
each scene a nested comp (cc2 Comp.nest).

    import saas_ui_showcase as SH; doc = SH.build(); doc.send(client, PROJECT.carverproj)

Hard cuts, every scene plays its full length. The cursor plays over the toggle: its own background is dropped, and it starts 14 f
into its own comp (the in edge is trimmed to master frame 230 after the placing), so its ripple (local f28) lands at 244 = the
knob's start. The long holds (KPI tile, toast) keep a slow 3 % push on their instance.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import saas_ui_lab as L
from dvsu_kit import KDoc

SCENES = [("SU Search typing", 0), ("SU Sidebar drawer", 80), ("SU KPI tile", 140), ("SU Toggle switch", 230), ("SU Counter", 278),
          ("SU Notification toast", 338)]
CURSOR_AT, CURSOR_IN = 230, 14
LENGTH = 458


def build():
    d = KDoc()
    L.cursor_click(d); L.toast(d); L.toggle(d); L.kpi(d); L.sidebar(d); L.counter(d); L.typing(d)
    comps = {c.name: c for c in d.comps}
    cur = comps["SU Cursor click"]
    cur.objs = [o for o in cur.objs if o.name != "Lab bg"]
    master = d.comp("SaaS UI showcase", LENGTH, "show")
    master.rect("Background", 0, 0, 1920, 1080, L.COL['bg'], f0=0, dur=LENGTH)
    for name, f0 in SCENES:
        master.nest(comps[name], f0=f0)
        if name in ("SU KPI tile", "SU Notification toast"):
            master.nest_edit(name, f0, scale=[(f0, 1.0, 'Linear'), (f0 + comps[name].length, 1.03, 'Linear')])
    master.nest(cur, f0=CURSOR_AT - CURSOR_IN)
    master.nest_edit("SU Cursor click", CURSOR_AT - CURSOR_IN, trim_in=CURSOR_AT)
    return d


if __name__ == "__main__":
    print(__doc__)
