"""Build the Explainer preset pack (library/templates/explainer/, prefix ex_).

    python build_explainer_pack.py OUT_DIR

Same method as build_pattern_pack.py (curves baked to keys with LINEAR joins; values
RELATIVE to the object; positions in frame fractions, Y UP), plus multi-segment tracks:
a property can run several curves one after another (fall, squash, recover), which is
what a single emphasis pulse needs. Templates come from explainer_lab.py via
comp_to_template.py; docs ai/patterns/explainer.md.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from curves import named, bake

def interp(a, b, p):
    if isinstance(a, list): return [round(x + (y - x) * p, 5) for x, y in zip(a, b)]
    return round(a + (b - a) * p, 5)

def track(prop, segs, frames, tol=0.01):
    """segs: [(from, to, curve, start, end)] in order, start/end as fractions of the preset span"""
    keys = []
    if segs[0][3] > 0: keys.append(dict(at=0, value=segs[0][0], easing="Linear"))
    for frm, to, curve, a, b in segs:
        for t, p in bake(named[curve], max(2, round((b - a) * frames)), tol):
            at = round(a + t * (b - a), 4)
            k = dict(at=at, value=interp(frm, to, p), easing="Linear")
            if keys and abs(keys[-1]["at"] - at) < 1e-6: keys[-1] = k
            else: keys.append(k)
    if keys[-1]["at"] < 1: keys.append(dict(at=1, value=segs[-1][1], easing="Linear"))
    return {"property": prop, "keys": keys}

P = []
def preset(pid, name, anchor, frames, tracks, tags, note):
    P.append(dict(pid=pid, name=name, anchor=anchor, frames=frames, tracks=tracks, tags=tags, note=note))

preset("ex_step_in", "Step in", "in", 14, lambda n: [
    track("center", [([-0.025, 0], [0, 0], "emphasized-decel", 0.0, 1.0)], n),
    track("blend", [(0.0, 1.0, "standard", 0.0, 0.5)], n)],
    ["in", "step", "explainer", "calm"],
    "A short 2.5% step in from the left on a strong decelerate with a fade: the reading-order entrance for steps, labels and list items.")
preset("ex_emphasis_pulse", "Emphasis pulse", "in", 16, lambda n: [
    track("size", [(1.0, 1.15, "standard", 0.0, 0.4), (1.15, 1.0, "s-curve", 0.4, 1.0)], n)],
    ["in", "emphasis", "pulse", "attention", "explainer"],
    "One 15% swell and back in 16 f (never looped): 'look here'. Split the clip where the narration names the thing, and apply it to the second part.")

def build(out_dir, tol=0.01):
    os.makedirs(out_dir, exist_ok=True)
    for p in P:
        d = {"presetVersion": 2, "id": "cc.ex." + p["pid"][3:], "name": p["name"], "category": "animation",
             "tags": p["tags"] + ["explainer pack"],
             "note": p["note"] + " Curves baked as keys (linear joins) - see the skill's ai/patterns/explainer.md.",
             "anchor": p["anchor"], "frames": p["frames"], "tracks": p["tracks"](p["frames"])}
        with open(os.path.join(out_dir, p["pid"] + ".carverpreset"), "w") as f:
            json.dump(d, f, indent=1)
    pack = {"packVersion": 1, "id": "cc.explainer", "name": "Explainer", "origin": "carvercat-skills", "version": 1, "tier": "free",
            "note": "Clear, narrated-explainer motion: step-ins, a single emphasis pulse, a three-step process with drawn arrows, an icon grid, a callout with a leader line and a milestone timeline. Source: carvercat-skills/ai/scripts/motion/build_explainer_pack.py and categories/explainer."}
    with open(os.path.join(out_dir, "pack.carverpack"), "w") as f:
        json.dump(pack, f, indent=1)
    return len(P)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "explainer"
    print(build(out), "presets ->", out)
