"""Write the funky/fk-showcase sample project: the Funky lab comps cut
together into one 10.5 s reel (direct project-file authoring).

    import funky_showcase as SH; presets, masks = SH.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); edit.save;
lint and look the master.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import funky_lab as L

SCENES = [("FK Memphis shapes", 0, 90), ("FK Offset title", 90, 90), ("FK Sticker stack", 180, 75)]
LENGTH = 315


def build(path, m=None):
    d = L.Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    L.PRESETS.clear(); L.MASKS.clear()
    L.memphis(d); L.offset_title(d); L.zigzag_ribbon(d); L.sticker_stack(d)
    comps = {c.name: c for c in d.comps}
    master = d.comp("Funky showcase", LENGTH, "fshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL["peach"], f0=0, dur=LENGTH)
    for name, f0, dur in SCENES:
        master.nest(name, comps[name], f0=f0, dur=dur)
    master.nest("FK Zigzag ribbon", comps["FK Zigzag ribbon"], f0=255, dur=60)   # the snake closes the reel
    d.save()
    return L.PRESETS, L.MASKS
