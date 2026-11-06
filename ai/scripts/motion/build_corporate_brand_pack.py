"""Build the Corporate Brand preset pack (library/templates/corporate-brand/, prefix cb_).

    python build_corporate_brand_pack.py OUT_DIR

Same method as build_pattern_pack.py: curves baked to keys with LINEAR joins; values
RELATIVE to the object; positions in frame fractions, Y UP. Templates come from the
lab comps (corporate_brand_lab.py) via comp_to_template.py; docs ai/patterns/corporate-brand.md.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pattern_pack import lane, fade_in, fade_out, lane_keys

P = []
def preset(pid, name, anchor, frames, lanes, tags, note):
    P.append(dict(pid=pid, name=name, anchor=anchor, frames=frames, lanes=lanes, tags=tags, note=note))

preset("cb_soft_rise", "Soft rise", "in", 24,
       [lane("center", [0, -0.015], [0, 0], "standard"), fade_in(0.6, "standard")],
       ["in", "rise", "fade", "calm", "corporate"],
       "A calm 1.5% rise under a long fade (24 f, standard curve). Corporate titles, captions and logos: unhurried and never springy.")
preset("cb_soft_fall_out", "Soft fade out", "out", 16,
       [lane("center", [0, 0], [0, 0.01], "accel"), fade_out(0.0, "accel")],
       ["out", "fade", "calm", "corporate"],
       "Fades out over 16 f while drifting 1% up, accelerating. The calm exit for anything that entered with Soft rise.")
preset("cb_photo_push", "Photo push - 5 s", "in", 150,
       [lane("size", 1.0, 1.06, "linear")],
       ["in", "push", "photo", "ken burns", "hold"],
       "A linear 6% push over 150 f (5 s) so stills, plates and held frames keep moving. Keep the clip no longer than 150 f: once the push stops, a full-frame plate held above 100% is reported by lint as cropped at rest.")
preset("cb_card_settle", "Card settle", "in", 20,
       [lane("center", [0, -0.02], [0, 0], "emphasized-decel"), lane("size", 0.97, 1.0, "emphasized-decel"), fade_in(0.5, "standard")],
       ["in", "card", "panel", "settle", "corporate"],
       "Rises 2% and grows from 97% on a strong decelerate, no overshoot. Cards, panels and stat columns in brand films.")

def build(out_dir, tol=0.01):
    os.makedirs(out_dir, exist_ok=True)
    for p in P:
        d = {"presetVersion": 2, "id": "cc.cb." + p["pid"][3:], "name": p["name"], "category": "animation",
             "tags": p["tags"] + ["corporate brand"],
             "note": p["note"] + " Curve baked as keys (linear joins) - see the skill's ai/patterns/corporate-brand.md.",
             "anchor": p["anchor"], "frames": p["frames"],
             "tracks": [{"property": l["prop"], "keys": lane_keys(l, p["frames"], tol)} for l in p["lanes"]]}
        with open(os.path.join(out_dir, p["pid"] + ".carverpreset"), "w") as f:
            json.dump(d, f, indent=1)
    pack = {"packVersion": 1, "id": "cc.corporate-brand", "name": "Corporate Brand", "origin": "carvercat-skills", "version": 1, "tier": "free",
            "note": "Calm, on-brand motion: soft rises and fades, photo pushes, a split-rule title card, a two-box lower third, a line-built logo resolve and a three-stat row. Source: carvercat-skills/ai/scripts/motion/build_corporate_brand_pack.py and categories/corporate-brand."}
    with open(os.path.join(out_dir, "pack.carverpack"), "w") as f:
        json.dump(pack, f, indent=1)
    return len(P)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "corporate-brand"
    print(build(out), "presets ->", out)
