"""Build the Sports preset pack (library/templates/sports/, prefix sp_).

    python build_sports_pack.py OUT_DIR

Same method as build_pattern_pack.py (curves baked to keys with LINEAR joins; values
RELATIVE to the object; positions in frame fractions, Y UP), plus multi-segment tracks:
a property can run several curves one after another (fall, squash, recover), which is
what an impact (overshoot down, then settle) needs. Templates come from sports_lab.py
via comp_to_template.py; docs ai/patterns/sports.md.
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

preset("sp_slash_in", "Slash in", "in", 10, lambda n: [
    track("center", [([-0.22, -0.12], [0, 0], "expo-out", 0.0, 1.0)], n),
    track("blend", [(0.0, 1.0, "linear", 0.0, 0.2)], n)],
    ["in", "slash", "diagonal", "fast", "sports"],
    "Cuts in along a diagonal from the lower left (22% W, 12% H) in 10 f on a hard expo. Add the Motion blur effect for the smear.")
preset("sp_impact_slam", "Impact slam", "in", 12, lambda n: [
    track("size", [(2.2, 0.92, "accel", 0.0, 0.4), (0.92, 1.0, "spring-gentle", 0.4, 1.0)], n),
    track("blend", [(0.0, 1.0, "linear", 0.0, 0.15)], n)],
    ["in", "slam", "impact", "hit", "sports"],
    "Slams down from 220%, accelerating, overshoots to 92% on impact (frame 5) and springs back to rest. Scores, GOAL, big words; put the hit SFX on the impact frame.")
preset("sp_zoom_past", "Zoom past", "out", 8, lambda n: [
    track("size", [(1.0, 3.0, "accel", 0.0, 1.0)], n),
    track("blend", [(1.0, 0.0, "accel", 0.4, 1.0)], n)],
    ["out", "zoom", "fast", "transition", "sports"],
    "Rushes toward camera to 300% and fades in 8 f, accelerating. The exit that sells speed; cut on its last frame.")

def build(out_dir, tol=0.01):
    os.makedirs(out_dir, exist_ok=True)
    for p in P:
        d = {"presetVersion": 2, "id": "cc.sp." + p["pid"][3:], "name": p["name"], "category": "animation",
             "tags": p["tags"] + ["sports pack"],
             "note": p["note"] + " Curves baked as keys (linear joins) - see the skill's ai/patterns/sports.md.",
             "anchor": p["anchor"], "frames": p["frames"], "tracks": p["tracks"](p["frames"])}
        with open(os.path.join(out_dir, p["pid"] + ".carverpreset"), "w") as f:
            json.dump(d, f, indent=1)
    pack = {"packVersion": 1, "id": "cc.sports", "name": "Sports", "origin": "carvercat-skills", "version": 1, "tier": "free",
            "note": "High-energy sports graphics: slash-ins, impact slams, zoom-past exits, a score bug with a number flip, a player card, head-to-head stat bars and a GOAL slam. Source: carvercat-skills/ai/scripts/motion/build_sports_pack.py and categories/sports."}
    with open(os.path.join(out_dir, "pack.carverpack"), "w") as f:
        json.dump(pack, f, indent=1)
    return len(P)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "sports"
    print(build(out), "presets ->", out)
