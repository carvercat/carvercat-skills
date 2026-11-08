"""Write the retro/rt-showcase sample project in design units: the Retro lab comps cut together into one 9.5 s reel, each scene
placed as a nested comp (comp.place), the checker wipe on a track above the scenes.

    import retro_showcase as SH; doc = SH.build(); doc.send(client, PROJECT.carverproj)

After sending: lint and look the master. Presets of the lab comps (Pop / Rise - on twos) are applied by PDoc.send.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import retro_lab as L

SCENES = [("RT Sunburst title", 0, 90), ("RT Rainbow stripes", 90, 75), ("RT Synthwave", 165, 120)]
LENGTH = 285


def build():
    d = L.PDoc(); L.comps(d)
    comps = {c.name: c for c in d.comps}
    cw = comps["RT Checker wipe"]                          # an overlay: drop its own lab background or it hides the cut
    cw.objs = [o for o in cw.objs if o.name != "Lab bg"]
    master = d.comp("Retro showcase", LENGTH, "rshow")
    master.rect("Background", 0, 0, L.W, L.H, L.COL["cream"], f0=0, dur=LENGTH)
    for name, f0, dur in SCENES:
        master.nest(comps[name], f0=f0)
    # the checkerboard covers the frame from its f22 to f28 (master 161-167): the cut to the synthwave scene (165) happens under it
    master.nest(cw, f0=139, track='top')
    d.comps = [c for c in d.comps if c is not master] + [master]
    return d


if __name__ == "__main__":
    print(__doc__)
