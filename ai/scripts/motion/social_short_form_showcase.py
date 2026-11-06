"""Write the social-media-reels/ss-showcase sample project: a 9.5 s vertical short cut from the
Social Short-form lab comps, with a story progress bar running over the whole piece.

    import social_short_form_showcase as SH; presets, masks = SH.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); edit.save; lint,
look and validate the master (bounds_inside the safe box).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import social_short_form_lab as L

SCENES = [("SS Hook title", 0, 75), ("SS Caption pages", 75, 120), ("SS Follow CTA", 195, 90)]
LENGTH = 285


def build(path, m=None):
    d = L.Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    L.PRESETS.clear(); L.MASKS.clear()
    L.hook_title(d); L.caption_pages(d); L.follow_cta(d); L.progress_bar(d, n=LENGTH, bg=False)
    comps = {c.name: c for c in d.comps}
    master = L.comp(d, "Social short showcase", LENGTH, "sshow")
    master.rect("Background", 0, 0, 1080, 1920, L.COL['bg'], f0=0, dur=LENGTH)
    for name, f0, dur in SCENES:
        master.nest(name, comps[name], f0=f0, dur=dur, x=540, y=960)
    master.nest("SS Progress bar", comps["SS Progress bar"], f0=0, dur=LENGTH, x=540, y=960)
    d.save()
    return L.PRESETS, L.MASKS
