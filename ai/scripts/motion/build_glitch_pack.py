"""Build the Glitch preset pack (library/templates/glitch/, prefix gl_).

    python build_glitch_pack.py OUT_DIR

Same method as build_pattern_pack.py (curves baked to keys with LINEAR joins; values
RELATIVE to the object; positions in frame fractions, Y UP), plus multi-segment tracks:
a property can run several curves one after another (fall, squash, recover), which is
and steps() writes held jumps (easing Hold) at given fractions: the stepped,
broken-signal look. Templates come from glitch_lab.py via comp_to_template.py;
docs ai/patterns/glitch.md.
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

def steps(prop, pts):
    """pts: [(at, value)] -> held jumps (easing Hold arrives at each key)"""
    return {"property": prop, "keys": [dict(at=a, value=v, easing="Linear" if i == 0 else "Hold") for i, (a, v) in enumerate(pts)]}

preset("gl_glitch_in", "Glitch in", "in", 12, lambda n: [
    steps("center", [(0.0, [0.03, 0]), (0.17, [-0.02, 0]), (0.33, [0.012, 0]), (0.5, [-0.006, 0]), (0.67, [0.003, 0]), (0.83, [0, 0]), (1.0, [0, 0])]),
    steps("blend", [(0.0, 0.0), (0.17, 1.0), (0.33, 0.4), (0.5, 1.0), (0.67, 0.7), (0.83, 1.0), (1.0, 1.0)])],
    ["in", "glitch", "jump", "stepped"],
    "Arrives in 12 f as a broken signal: held horizontal jumps of 3%, -2%, 1.2%, -0.6%, 0.3% of the frame width with stepped opacity, then locks in.")
preset("gl_glitch_out", "Glitch out", "out", 10, lambda n: [
    steps("center", [(0.0, [0, 0]), (0.2, [-0.008, 0]), (0.4, [0.015, 0]), (0.6, [-0.025, 0]), (0.8, [0.04, 0]), (1.0, [0.04, 0])]),
    steps("blend", [(0.0, 1.0), (0.2, 0.6), (0.4, 1.0), (0.6, 0.3), (0.8, 0.0), (1.0, 0.0)])],
    ["out", "glitch", "jump", "stepped"],
    "The signal breaks up and drops out in 10 f: growing held jumps with stepped opacity, gone by the last 2 frames.")
preset("gl_stretch_hit", "Glitch stretch hit", "in", 8, lambda n: [
    steps("scaleX", [(0.0, 1.6), (0.25, 0.85), (0.5, 1.12), (0.75, 1.0), (1.0, 1.0)]),
    steps("scaleY", [(0.0, 0.6), (0.25, 1.1), (0.5, 0.95), (0.75, 1.0), (1.0, 1.0)])],
    ["in", "glitch", "stretch", "hit", "stepped"],
    "An 8 f stepped squash: 160% x 60%, 85% x 110%, 112% x 95%, then rest. Logos and words on a beat hit.")

def build(out_dir, tol=0.01):
    os.makedirs(out_dir, exist_ok=True)
    for p in P:
        d = {"presetVersion": 2, "id": "cc.gl." + p["pid"][3:], "name": p["name"], "category": "animation",
             "tags": p["tags"] + ["glitch pack"],
             "note": p["note"] + " Curves baked as keys (linear joins) - see the skill's ai/patterns/glitch.md.",
             "anchor": p["anchor"], "frames": p["frames"], "tracks": p["tracks"](p["frames"])}
        with open(os.path.join(out_dir, p["pid"] + ".carverpreset"), "w") as f:
            json.dump(d, f, indent=1)
    pack = {"packVersion": 1, "id": "cc.glitch", "name": "Glitch", "origin": "carvercat-skills", "version": 1, "tier": "free",
            "note": "Broken-signal motion: stepped glitch in/out, a stretch hit, an RGB-split title, a slice-shift logo, noise bars and a glitch cut. Source: carvercat-skills/ai/scripts/motion/build_glitch_pack.py and categories/glitch."}
    with open(os.path.join(out_dir, "pack.carverpack"), "w") as f:
        json.dump(pack, f, indent=1)
    return len(P)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "glitch"
    print(build(out), "presets ->", out)
