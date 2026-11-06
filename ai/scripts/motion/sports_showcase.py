"""Write the sports/sp-showcase sample project: a 10 s match-graphics reel from the Sports lab
comps - score bug and GOAL slam over a pitch stand-in, then the player card and head-to-head.

    import sports_showcase as SH; presets, masks = SH.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); for each MASKS
pair (content, window) run mask.make {ids:[window, content]} - the FIRST id is the mask -
then parent.clear; edit.save; lint and look the master.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sports_lab as L

LENGTH = 300


def build(path, m=None):
    d = L.Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    L.PRESETS.clear(); L.MASKS.clear()
    L.score_bug(d); L.player_card(d); L.head_to_head(d); L.goal_slam(d)
    comps = {c.name: c for c in d.comps}
    for name in ("SP Score bug", "SP Goal slam"):                       # overlays over the pitch: no lab backgrounds
        comps[name].vtracks = [t for t in comps[name].vtracks if t[0].get("label") != "Lab bg"]
    master = d.comp("Sports showcase", LENGTH, "pshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL['bg'], f0=0, dur=LENGTH)
    pitch = master.rect("Pitch stand-in", 960, 540, 1920, 1080, L.COL['bg'], f0=0, dur=120, center=True)
    pitch.gradient([(0.0, L.lin('1E6B34')), (1.0, L.lin('0E3B1C'))], (960, 0), (960, 1080))
    master.nest("SP Score bug", comps["SP Score bug"], f0=0, dur=120)
    master.nest("SP Goal slam", comps["SP Goal slam"], f0=49, dur=60)   # GOAL! lands (f58) as the score rolls over
    master.nest("SP Player card", comps["SP Player card"], f0=120, dur=90)
    master.nest("SP Head to head", comps["SP Head to head"], f0=210, dur=90)
    d.save()
    return L.PRESETS, L.MASKS
