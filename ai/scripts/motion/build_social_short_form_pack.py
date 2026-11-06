"""Build the Social Short-form preset pack (library/templates/social-short-form/, prefix ss_).

    python build_social_short_form_pack.py OUT_DIR

Same method as build_pattern_pack.py: curves baked to keys with LINEAR joins; values
RELATIVE to the object; positions in frame fractions, Y UP. Templates come from the
lab comps (social_short_form_lab.py) via comp_to_template.py; docs ai/patterns/social-short-form.md.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pattern_pack import lane, fade_in, fade_out, lane_keys

P = []
def preset(pid, name, anchor, frames, lanes, tags, note, stagger=None):
    P.append(dict(pid=pid, name=name, anchor=anchor, frames=frames, lanes=lanes, tags=tags, note=note, stagger=stagger))

preset("ss_hook_punch", "Hook punch", "in", 10,
       [lane("size", 1.25, 1.0, "expo-out"), fade_in(0.2, "linear")],
       ["in", "hook", "punch", "fast", "social"],
       "A 10 f punch-in from 125%: the first-second hook of a short. Big text, a face, a product.", None)
preset("ss_caption_pop", "Caption words pop", "in", 8,
       [lane("size", 0.7, 1.0, "spring-gentle"), fade_in(0.25, "linear")],
       ["in", "stagger", "word", "caption", "social"],
       "Captions word by word, 3 f apart: each word pops from 70% in 8 f with a small spring. Fast enough to follow speech.",
       dict(by="word", order="forward", gap=3))
preset("ss_whip_in_left", "Whip in - left", "in", 10,
       [lane("center", [-0.3, 0], [0, 0], "expo-out")],
       ["in", "whip", "slide", "fast", "social"],
       "Arrives from 30% of the frame width to the left in 10 f on a hard expo. Add the Motion blur effect for the smear.", None)

def build(out_dir, tol=0.01):
    os.makedirs(out_dir, exist_ok=True)
    for p in P:
        d = {"presetVersion": 2, "id": "cc.ss." + p["pid"][3:], "name": p["name"], "category": "animation",
             "tags": (["stagger"] + [t for t in p["tags"] if t != "stagger"] if p["stagger"] else p["tags"]) + ["social short-form"],
             "note": p["note"] + " Curve baked as keys (linear joins) - see the skill's ai/patterns/social-short-form.md.",
             "anchor": p["anchor"], "frames": p["frames"],
             "tracks": [{"property": l["prop"], "keys": lane_keys(l, p["frames"], tol)} for l in p["lanes"]]}
        if p["stagger"]: d["only"] = "text"; d["stagger"] = p["stagger"]
        with open(os.path.join(out_dir, p["pid"] + ".carverpreset"), "w") as f:
            json.dump(d, f, indent=1)
    pack = {"packVersion": 1, "id": "cc.social-short-form", "name": "Social Short-form", "origin": "carvercat-skills", "version": 1, "tier": "free",
            "note": "Vertical 9:16 Reels/Shorts/TikTok: hook punches, fast word captions, whip-ins, a hook title, caption pages, a story progress bar and a follow end card - all inside the social safe area. Source: carvercat-skills/ai/scripts/motion/build_social_short_form_pack.py and categories/social-media-reels."}
    with open(os.path.join(out_dir, "pack.carverpack"), "w") as f:
        json.dump(pack, f, indent=1)
    return len(P)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "social-short-form"
    print(build(out), "presets ->", out)
