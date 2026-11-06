"""Build the Data Viz preset pack (library/templates/data-viz/, prefix dv_).

    python build_data_viz_pack.py OUT_DIR

Same method as build_pattern_pack.py: curves from curves.py baked to keys with
LINEAR joins; values RELATIVE to the object; positions in frame fractions, Y UP.
Templates are extracted from the lab comps (data_viz_lab.py) with
comp_to_template.py; docs are ai/patterns/data-viz.md and dv-*.md.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pattern_pack import lane, fade_in, lane_keys

P = []
def preset(pid, name, anchor, frames, lanes, tags, note):
    P.append(dict(pid=pid, name=name, anchor=anchor, frames=frames, lanes=lanes, tags=tags, note=note))

preset("dv_bar_grow_spring", "Bar grow up - spring", "in", 20,
       [lane("scaleY", 0.0, 1.0, "spring-gentle")],
       ["in", "bar", "column", "chart", "spring"],
       "Scale Y from 0 with a 4-5% overshoot. Set the anchor to the bottom edge first ([0,-1]) so the column grows from its baseline. The springy sibling of Grow up (Y).")
preset("dv_bar_grow_across_spring", "Bar grow across - spring", "in", 20,
       [lane("scaleX", 0.0, 1.0, "spring-gentle")],
       ["in", "bar", "horizontal", "chart", "spring"],
       "Scale X from 0 with a 4-5% overshoot. Set the anchor to the left edge first ([-1,0]). Horizontal and ranked bars.")
preset("dv_point_pop", "Data point pop", "in", 12,
       [lane("size", 0.0, 1.0, "spring-bouncy"), fade_in(0.25, "linear")],
       ["in", "point", "dot", "marker", "chart"],
       "A 12 f pop for chart markers: size 0 to 1 with a 16% spring. Start each marker's clip on the frame the line reaches it.")

def build(out_dir, tol=0.01):
    os.makedirs(out_dir, exist_ok=True)
    for p in P:
        d = {"presetVersion": 2, "id": "cc.dv." + p["pid"][3:], "name": p["name"], "category": "animation",
             "tags": p["tags"] + ["data viz"],
             "note": p["note"] + " Curve baked as keys (linear joins) - see the skill's ai/patterns/data-viz.md.",
             "anchor": p["anchor"], "frames": p["frames"],
             "tracks": [{"property": l["prop"], "keys": lane_keys(l, p["frames"], tol)} for l in p["lanes"]]}
        with open(os.path.join(out_dir, p["pid"] + ".carverpreset"), "w") as f:
            json.dump(d, f, indent=1)
    pack = {"packVersion": 1, "id": "cc.data-viz", "name": "Data Viz", "origin": "carvercat-skills", "version": 1, "tier": "free",
            "note": "Charts in motion: spring bars, data-point pops, a self-drawing line chart, a donut that fills, ranked bars and a gauge. Source: carvercat-skills/ai/scripts/motion/build_data_viz_pack.py and the lab comps in categories/data-viz."}
    with open(os.path.join(out_dir, "pack.carverpack"), "w") as f:
        json.dump(pack, f, indent=1)
    return len(P)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "data-viz"
    print(build(out), "presets ->", out)
