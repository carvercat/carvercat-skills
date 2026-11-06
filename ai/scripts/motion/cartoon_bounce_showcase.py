"""Write the cartoon-bounce/ct-showcase sample project: the Cartoon Bounce lab comps cut
together into one 10.8 s cartoon reel (direct project-file authoring).

    import cartoon_bounce_showcase as SH; presets, masks = SH.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); edit.save;
lint and look the master.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartoon_bounce_lab as L

SCENES = [("CT Bouncing ball", 0, 90), ("CT Smear whoosh", 90, 45), ("CT Blink face", 135, 100), ("CT Boing title", 235, 90)]
LENGTH = 325


def build(path, m=None):
    d = L.Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    L.PRESETS.clear(); L.MASKS.clear()
    L.bouncing_ball(d); L.boing_title(d); L.blink_face(d); L.smear_whoosh(d)
    comps = {c.name: c for c in d.comps}
    master = d.comp("Cartoon bounce showcase", LENGTH, "tshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL['cream'], f0=0, dur=LENGTH)
    for name, f0, dur in SCENES:
        master.nest(name, comps[name], f0=f0, dur=dur)
    d.save()
    return L.PRESETS, L.MASKS
