"""Build the Funky preset pack (library/templates/funky/, prefix fk_).

    python build_funky_pack.py OUT_DIR

Same method as build_pattern_pack.py (curves baked to keys with LINEAR joins; values
RELATIVE to the object; positions in frame fractions, Y UP), plus multi-segment tracks:
a property can run several curves one after another (fall, squash, recover), which is
what wiggles need. Templates come from funky_lab.py via comp_to_template.py;
docs ai/patterns/funky.md.
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

preset("fk_tilt_pop", "Tilt pop", "in", 18, lambda n: [
    track("size", [(0.0, 1.0, "spring-bouncy", 0.0, 1.0)], n),
    track("angle", [(-14.0, 0.0, "spring-wobbly", 0.0, 1.0)], n),
    track("blend", [(0.0, 1.0, "linear", 0.0, 0.15)], n)],
    ["in", "pop", "tilt", "spring", "funky"],
    "Pops from zero (16% spring) while untilting from -14 deg on a wobbly spring. Shapes, stickers, badges.")
preset("fk_slide_wiggle", "Slide in - wiggle", "in", 24, lambda n: [
    track("center", [([0.4, 0], [0, 0], "expo-out", 0.0, 0.6)], n),
    track("angle", [(12.0, 0.0, "spring-wobbly", 0.0, 1.0)], n)],
    ["in", "slide", "wiggle", "funky"],
    "Slides in from 40% of the frame width to the right and wiggles its angle from 12 deg to rest on a wobbly spring.")
preset("fk_spin_in", "Spin in", "in", 20, lambda n: [
    track("angle", [(-180.0, 0.0, "expo-out", 0.0, 1.0)], n),
    track("size", [(0.3, 1.0, "spring-gentle", 0.0, 1.0)], n),
    track("blend", [(0.0, 1.0, "linear", 0.0, 0.2)], n)],
    ["in", "spin", "rotate", "funky"],
    "Half a turn in on an expo landing while growing from 30% with a small spring.")
preset("fk_spin_out", "Spin out", "out", 14, lambda n: [
    track("angle", [(0.0, 90.0, "accel", 0.0, 1.0)], n),
    track("size", [(1.0, 0.0, "accel", 0.0, 1.0)], n)],
    ["out", "spin", "shrink", "funky"],
    "A quarter turn while shrinking to nothing, accelerating. The exit for Spin in and Tilt pop.")

def build(out_dir, tol=0.01):
    os.makedirs(out_dir, exist_ok=True)
    for p in P:
        d = {"presetVersion": 2, "id": "cc.fk." + p["pid"][3:], "name": p["name"], "category": "animation",
             "tags": p["tags"] + ["funky"],
             "note": p["note"] + " Curves baked as keys (linear joins) - see the skill's ai/patterns/funky.md.",
             "anchor": p["anchor"], "frames": p["frames"], "tracks": p["tracks"](p["frames"])}
        with open(os.path.join(out_dir, p["pid"] + ".carverpreset"), "w") as f:
            json.dump(d, f, indent=1)
    pack = {"packVersion": 1, "id": "cc.funky", "name": "Funky", "origin": "carvercat-skills", "version": 1, "tier": "free",
            "note": "Bold, playful graphic motion: tilt pops, wiggles, spins, Memphis shapes, an offset-shadow title, a zigzag ribbon and slapped-down stickers. Source: carvercat-skills/ai/scripts/motion/build_funky_pack.py and categories/funky."}
    with open(os.path.join(out_dir, "pack.carverpack"), "w") as f:
        json.dump(pack, f, indent=1)
    return len(P)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "funky"
    print(build(out), "presets ->", out)
