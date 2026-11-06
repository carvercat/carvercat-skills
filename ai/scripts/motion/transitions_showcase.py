"""Write the transitions/tx-showcase sample project: eight stand-in scenes cut together through
the seven cover transitions, each placed so its cover frame lands on the cut.

    import transitions_showcase as SH; presets, masks = SH.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; edit.save; lint, look and qc the master.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import transitions_lab as L

# (comp, the comp frame to put on the cut)
TRANSITIONS = [("TX Slide wipe", 18), ("TX Diagonal wipe", 18), ("TX Split doors", 18), ("TX Bars stagger", 20),
               ("TX Clock wipe", 20), ("TX Bubble cover", 20), ("TX Dip to colour", 15)]
SCENE = 45
COLOURS = ['2B3A67', 'E8D6B3', '496A81', 'D98E73', '1F2333', 'F2C14E', '3B6EF6', 'F7F7FA']


def build(path, m=None):
    d = L.Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    L.PRESETS.clear(); L.MASKS.clear()
    for f in (L.slide_wipe, L.diagonal_wipe, L.split_doors, L.bars_stagger, L.clock_wipe, L.bubble_cover, L.dip_to_colour):
        f(d)
    comps = {c.name: c for c in d.comps}
    for name, _ in TRANSITIONS:                                    # overlays: drop the stand-in scenes
        comps[name].vtracks = [t for t in comps[name].vtracks if t[0].get("label") not in ("Scene A", "Scene B")]
    n = SCENE * len(COLOURS)
    master = d.comp("Transitions showcase", n, "xshow")
    for i, hexcol in enumerate(COLOURS):
        master.rect(f"Scene {i + 1}", 0, 0, 1920, 1080, L.lin(hexcol), f0=i * SCENE, dur=SCENE)
        ink = L.lin('14151C') if i in (1, 5, 7) else L.lin('FFFFFF')
        master.text(f"Scene {i + 1} label", f"SCENE {i + 1}", 960, 540, 120, ink, f0=i * SCENE, dur=SCENE, style='ExtraBold', align='center')
    for i, (name, cut) in enumerate(TRANSITIONS):
        at = (i + 1) * SCENE - cut
        master.nest(name, comps[name], f0=at, dur=comps[name].length)
    d.save()
    return L.PRESETS, L.MASKS
