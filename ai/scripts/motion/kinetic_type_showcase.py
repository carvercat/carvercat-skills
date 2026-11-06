"""Write the kinetic-typography/kt-showcase sample project: the kinetic type lab comps
cut together into one 14.3 s master (direct project-file authoring).

    import kinetic_type_showcase as SH; SH.build(PROJECT.carverproj, measurements)

`measurements` are the "KT Measure" bounds (see kinetic_type_lab.py). After writing:
edit.open {path, force:true}, apply MASKS (mask.make {ids:[window, content]} - the
FIRST id is the mask - then parent.clear), edit.save, then lint and look the master.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kinetic_type_lab as L

# (comp, start in the master, length): hard cuts, each scene plays its full length
SCENES = [("KT Focus pull", 0, 60), ("KT Word swap", 60, 120), ("KT Impact stack", 180, 90),
          ("KT Line reveal", 270, 60), ("KT Beat words", 330, 100)]
LENGTH = 430


def build(path, m):
    d = L.Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    L.MASKS.clear()
    L.word_swap(d, m); L.impact_stack(d); L.line_reveal(d); L.beat_words(d); L.focus_pull(d)
    comps = {c.name: c for c in d.comps}
    master = d.comp("Kinetic type showcase", LENGTH, "kshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL['bg'], f0=0, dur=LENGTH)
    for name, f0, dur in SCENES:
        o = master.nest(name, comps[name], f0=f0, dur=dur)
        if name == "KT Impact stack":                      # its 50 f hold keeps a slow 4% push
            o.scale([(f0, 1.0, 'Linear'), (f0 + dur, 1.04, 'Linear')])
    d.save()
    return [], L.MASKS
