"""Write the saas-launch/saas-ui-showcase sample project: the SaaS UI lab comps cut
together into one 15.3 s master (direct project-file authoring).

    python saas_ui_showcase.py PROJECT.carverproj MEASURE.json

MEASURE.json holds the text bounds the lab's "SU Measure" comp produced
(see saas_ui_lab.py). After writing: edit.open {path, force:true}, apply
saas_ui_lab.PRESETS and MASKS (preset.apply; mask.make {ids:[window, content]} - the FIRST id is the mask - then parent.clear),
edit.save, then check the master with carvercat_inspect lint and carvercat_look.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import saas_ui_lab as L

# (comp, start frame in the master, length): hard cuts, every scene plays its full length
SCENES = [("SU Search typing", 0, 80), ("SU Sidebar drawer", 80, 60), ("SU KPI tile", 140, 90),
          ("SU Toggle switch", 230, 48), ("SU Counter", 278, 60), ("SU Notification toast", 338, 120)]
CURSOR_AT, CURSOR_IN = 230, 14   # cursor starts 14 f into its own comp, so its ripple (local f28) lands at 244 = the knob's start
LENGTH = 458


def build(path, m):
    d = L.Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    L.PRESETS.clear()
    L.cursor_click(d); L.toast(d); L.toggle(d); L.kpi(d); L.sidebar(d); L.counter(d, m); L.typing(d, m)
    comps = {c.name: c for c in d.comps}
    cur = comps["SU Cursor click"]                       # the cursor plays over the toggle: drop its own background
    cur.vtracks = [t for t in cur.vtracks if t[0].get("label") != "Lab bg"]
    master = d.comp("SaaS UI showcase", LENGTH, "show")
    master.rect("Background", 0, 0, 1920, 1080, L.COL['bg'], f0=0, dur=LENGTH)
    inst = {}
    for name, f0, dur in SCENES:
        inst[name] = master.nest(name, comps[name], f0=f0, dur=dur)
    for name in ("SU KPI tile", "SU Notification toast"):  # long holds keep a slow 3% push so the frame never freezes
        f0, dur = [(a, b) for n, a, b in SCENES if n == name][0]
        inst[name].scale([(f0, 1.0, 'Linear'), (f0 + dur, 1.03, 'Linear')])
    master.nest("SU Cursor click", cur, f0=CURSOR_AT, dur=60 - CURSOR_IN, src_in=CURSOR_IN)
    d.save()
    return L.PRESETS, L.MASKS


if __name__ == "__main__":
    for x in build(sys.argv[1], json.load(open(sys.argv[2]))): print(x)
