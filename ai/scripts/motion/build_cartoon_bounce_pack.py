"""Build the Cartoon Bounce preset pack (library/templates/cartoon-bounce/, prefix ct_).

    python build_cartoon_bounce_pack.py OUT_DIR

Same method as build_pattern_pack.py (curves baked to keys with LINEAR joins; values
RELATIVE to the object; positions in frame fractions, Y UP), plus multi-segment tracks:
a property can run several curves one after another (fall, squash, recover), which is
what squash-and-stretch needs. Templates come from cartoon_bounce_lab.py via
comp_to_template.py; docs ai/patterns/cartoon-bounce.md.
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

# Squash land: falls 8% H accelerating (0-40%), squashes on contact (40-55%), springs back (55-100%)
preset("ct_squash_land", "Squash land", "in", 20, lambda n: [
    track("center", [([0, 0.08], [0, 0], "accel", 0.0, 0.4)], n),
    track("scaleX", [(1.0, 0.85, "accel", 0.0, 0.4), (0.85, 1.3, "expo-out", 0.4, 0.55), (1.3, 1.0, "spring-bouncy", 0.55, 1.0)], n),
    track("scaleY", [(1.0, 1.2, "accel", 0.0, 0.4), (1.2, 0.72, "expo-out", 0.4, 0.55), (0.72, 1.0, "spring-bouncy", 0.55, 1.0)], n),
    track("blend", [(0.0, 1.0, "linear", 0.0, 0.1)], n)],
    ["in", "squash", "stretch", "land", "cartoon"],
    "Drops in stretched (85% wide, 120% tall), squashes flat on landing (130% x 72%) and springs back. Set the anchor to the bottom edge ([0,-1]) so it squashes on the ground.")
# Anticipate jump: crouch (0-35%), then stretch and leave upward (35-100%)
preset("ct_anticipate_jump", "Anticipate jump out", "out", 20, lambda n: [
    track("scaleX", [(1.0, 1.18, "emphasized-decel", 0.0, 0.35), (1.18, 0.82, "expo-out", 0.35, 0.6), (0.82, 0.82, "linear", 0.6, 1.0)], n),
    track("scaleY", [(1.0, 0.78, "emphasized-decel", 0.0, 0.35), (0.78, 1.3, "expo-out", 0.35, 0.6), (1.3, 1.3, "linear", 0.6, 1.0)], n),
    track("center", [([0, 0], [0, 0], "linear", 0.0, 0.35), ([0, 0], [0, 0.6], "accel", 0.35, 1.0)], n)],
    ["out", "anticipation", "jump", "squash", "cartoon"],
    "Crouches (118% wide, 78% tall), then stretches tall and shoots up 60% of the frame, accelerating. Anchor at the bottom edge ([0,-1]).")
preset("ct_jelly_in", "Jelly in", "in", 28, lambda n: [
    track("scaleX", [(0.0, 1.0, "spring-wobbly", 0.0, 1.0)], n),
    track("scaleY", [(0.0, 1.0, "spring-bouncy", 0.0, 0.85), (1.0, 1.0, "linear", 0.85, 1.0)], n),
    track("blend", [(0.0, 1.0, "linear", 0.0, 0.12)], n)],
    ["in", "jelly", "wobble", "squash", "cartoon"],
    "Grows in with width and height on different springs (31% and 16% overshoot), so it wobbles like jelly before it settles.")
preset("ct_pop_wobbly", "Pop - wobbly", "in", 22, lambda n: [
    track("size", [(0.0, 1.0, "spring-wobbly", 0.0, 1.0)], n),
    track("blend", [(0.0, 1.0, "linear", 0.0, 0.15)], n)],
    ["in", "pop", "spring", "wobbly", "cartoon"],
    "Size 0 to 1 on a wobbly spring (about 31% overshoot, 2-3 visible wobbles). Stickers, stars, cartoon props.")

def build(out_dir, tol=0.01):
    os.makedirs(out_dir, exist_ok=True)
    for p in P:
        d = {"presetVersion": 2, "id": "cc.ct." + p["pid"][3:], "name": p["name"], "category": "animation",
             "tags": p["tags"] + ["cartoon bounce"],
             "note": p["note"] + " Curves baked as keys (linear joins) - see the skill's ai/patterns/cartoon-bounce.md.",
             "anchor": p["anchor"], "frames": p["frames"], "tracks": p["tracks"](p["frames"])}
        with open(os.path.join(out_dir, p["pid"] + ".carverpreset"), "w") as f:
            json.dump(d, f, indent=1)
    pack = {"packVersion": 1, "id": "cc.cartoon-bounce", "name": "Cartoon Bounce", "origin": "carvercat-skills", "version": 1, "tier": "free",
            "note": "Squash and stretch, anticipation, jelly and wobbly pops, a bouncing ball, a boing title, a blinking face and a smear whoosh. Source: carvercat-skills/ai/scripts/motion/build_cartoon_bounce_pack.py and categories/cartoon-bounce."}
    with open(os.path.join(out_dir, "pack.carverpack"), "w") as f:
        json.dump(pack, f, indent=1)
    return len(P)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "cartoon-bounce"
    print(build(out), "presets ->", out)
