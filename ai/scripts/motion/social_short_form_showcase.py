"""Write the social-media-reels/ss-showcase sample project in design units: a 9.5 s vertical short cut from the Social Short-form
lab comps (each placed as a nested comp), with a story progress bar running over the whole piece on a track above them.

    import social_short_form_showcase as SH; doc = SH.build(); doc.send(client, PROJECT.carverproj)

After sending: lint, look and validate the master (bounds_inside the safe box).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import social_short_form_lab as L

SCENES = [("SS Hook title", 0, 75), ("SS Caption pages", 75, 120), ("SS Follow CTA", 195, 90)]
LENGTH = 285


def build():
    d = L.SDoc()
    L.hook_title(d); L.caption_pages(d); L.follow_cta(d); L.progress_bar(d, n=LENGTH, bg=False)
    comps = {c.name: c for c in d.comps}
    master = L.comp(d, "Social short showcase", LENGTH, "sshow")
    master.rect("Background", 0, 0, L.W, L.H, L.COL['bg'], f0=0, dur=LENGTH)
    for name, f0, dur in SCENES:
        master.nest(comps[name], f0=f0)
    master.nest(comps["SS Progress bar"], f0=0, track='top')
    d.comps = [c for c in d.comps if c is not master] + [master]
    return d


if __name__ == "__main__":
    print(__doc__)
