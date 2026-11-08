"""Write the glitch/gl-showcase sample project in design units: the Glitch round-1 lab comps cut together into one 5.5 s sting with a glitch cut
and a noise overlay, each placed as a nested comp.

    import glitch_showcase as SH; doc = SH.build(); doc.send(client, PROJECT.carverproj)

The two overlays (noise bars, glitch cut) drop their stand-in backgrounds; the cut's f15 lands on the cut at 90. After sending: lint, look
and qc (flashes) the master.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import glitch_lab as L

LENGTH = 165


def build(path=None, m=None):
    d = L.new_doc()
    L.rgb_title(d); L.slice_shift(d); L.noise_bars(d); L.glitch_cut(d)
    comps = {c.name: c for c in d.comps}
    for name, drop in (("GL Noise bars", ("Lab bg",)), ("GL Glitch cut", ("Scene A", "Scene B"))):   # overlays: no backgrounds
        comps[name].objs = [o for o in comps[name].objs if o.name not in drop]
    master = d.comp("Glitch showcase", LENGTH, "gshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL['bg'], f0=0, dur=LENGTH)
    master.nest(comps["GL RGB title"], f0=0, dur=90)
    master.nest(comps["GL Slice shift"], f0=90, dur=75)
    master.nest(comps["GL Glitch cut"], f0=75, dur=30)        # its f15 lands on the cut at 90
    master.nest(comps["GL Noise bars"], f0=105, dur=60)
    d.comps = [c for c in d.comps if c is not master] + [master]
    return d


if __name__ == "__main__":
    print(__doc__)
