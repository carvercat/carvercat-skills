"""Build the Minimal Luxury preset pack (library/templates/minimal-luxury/, prefix ml_).

    python build_minimal_luxury_pack.py OUT_DIR

Same method as build_pattern_pack.py: curves baked to keys with LINEAR joins; values
RELATIVE to the object; positions in frame fractions, Y UP. Templates come from the
lab comps (minimal_luxury_lab.py) via comp_to_template.py; docs ai/patterns/minimal-luxury.md.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pattern_pack import lane, fade_in, fade_out, lane_keys

P = []
def preset(pid, name, anchor, frames, lanes, tags, note):
    P.append(dict(pid=pid, name=name, anchor=anchor, frames=frames, lanes=lanes, tags=tags, note=note))

preset("ml_slow_fade", "Slow fade in", "in", 36,
       [lane("size", 1.03, 1.0, "emphasized-decel"), fade_in(1.0, "standard")],
       ["in", "fade", "slow", "luxury", "minimal"],
       "A 36 f fade while the object eases down from 103%. Luxury and minimal titles, products and logos: nothing jumps.")
preset("ml_drift_up", "Drift up - 4 s", "in", 120,
       [lane("center", [0, -0.006], [0, 0], "linear")],
       ["in", "drift", "hold", "luxury", "minimal"],
       "A linear 0.6% rise over 120 f (4 s) under a hold, so a still frame keeps breathing. Apply after the entrance, on clips of 120 f or less.")
preset("ml_slow_fade_out", "Slow fade out", "out", 30,
       [lane("size", 1.0, 1.015, "linear"), fade_out(0.0, "standard")],
       ["out", "fade", "slow", "luxury", "minimal"],
       "A 30 f fade on a soft curve while the object grows 1.5%. The exit for anything that entered with Slow fade in.")

def build(out_dir, tol=0.01):
    os.makedirs(out_dir, exist_ok=True)
    for p in P:
        d = {"presetVersion": 2, "id": "cc.ml." + p["pid"][3:], "name": p["name"], "category": "animation",
             "tags": p["tags"] + ["minimal luxury"],
             "note": p["note"] + " Curve baked as keys (linear joins) - see the skill's ai/patterns/minimal-luxury.md.",
             "anchor": p["anchor"], "frames": p["frames"],
             "tracks": [{"property": l["prop"], "keys": lane_keys(l, p["frames"], tol)} for l in p["lanes"]]}
        with open(os.path.join(out_dir, p["pid"] + ".carverpreset"), "w") as f:
            json.dump(d, f, indent=1)
    pack = {"packVersion": 1, "id": "cc.minimal-luxury", "name": "Minimal Luxury", "origin": "carvercat-skills", "version": 1, "tier": "free",
            "note": "Slow, quiet, expensive: long fades, drifts, a tracked title, a feathered wipe reveal, a drawn product frame and a slow quote. Source: carvercat-skills/ai/scripts/motion/build_minimal_luxury_pack.py and categories/minimal-luxury."}
    with open(os.path.join(out_dir, "pack.carverpack"), "w") as f:
        json.dump(pack, f, indent=1)
    return len(P)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "minimal-luxury"
    print(build(out), "presets ->", out)
