"""Write the sports/sp-showcase sample project in design units: a 10 s match-graphics reel from the Sports lab comps - score bug and
GOAL slam over a pitch stand-in, then the player card and head-to-head.

    import sports_showcase as SH; doc = SH.build(); doc.send(client, PROJECT.carverproj)

The four comps are the lab's (sports_lab.py); the score bug and the GOAL slam lose their lab background so they overlay the pitch.
Each is placed in the master with comp.place (cc2 Comp.nest). After sending: lint, look and qc the master.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sports_lab as L

LENGTH = 300


def build():
    d = L.SDoc()
    L.score_bug(d); L.player_card(d); L.head_to_head(d); L.goal_slam(d)
    comps = {c.name: c for c in d.comps}
    for name in ("SP Score bug", "SP Goal slam"):                       # overlays over the pitch: no lab backgrounds
        comps[name].objs = [o for o in comps[name].objs if o.name != "Lab bg"]
    master = d.comp("Sports showcase", LENGTH, "pshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL['bg'], f0=0, dur=LENGTH)
    pitch = master.rect("Pitch stand-in", 960, 540, 1920, 1080, L.COL['bg'], f0=0, dur=120, center=True)
    pitch.gradient([(0.0, '#1E6B34'), (1.0, '#0E3B1C')], (960, 0), (960, 1080))
    master.nest(comps["SP Score bug"], f0=0, dur=120)
    master.nest(comps["SP Goal slam"], f0=49, dur=60)   # GOAL! lands (f58) as the score rolls over
    master.nest(comps["SP Player card"], f0=120, dur=90)
    master.nest(comps["SP Head to head"], f0=210, dur=90)
    d.comps = [c for c in d.comps if c is not master] + [master]   # the lab comps first, the master last (and open)
    return d


if __name__ == "__main__":
    print(__doc__)
