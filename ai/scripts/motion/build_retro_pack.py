"""Build the Retro preset pack (library/templates/retro/, prefix rt_).

    python build_retro_pack.py OUT_DIR

Same method as build_pattern_pack.py (curves baked to keys with LINEAR joins; values
RELATIVE to the object; positions in frame fractions, Y UP), plus multi-segment tracks:
a property can run several curves one after another (fall, squash, recover), which is
and twos() writes a curve 'on twos': one held value every 2 frames (easing Hold),
the stepped look of hand-drawn animation at 12 drawings a second. Templates come from
retro_lab.py via comp_to_template.py; docs ai/patterns/retro.md.
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

def twos(prop, frm, to, curve, frames, start=0.0, end=1.0):
    """the curve sampled on even frames and held between them (easing Hold): animation on twos"""
    keys, n = [], frames
    f0, f1 = start * n, end * n
    if start > 0: keys.append(dict(at=0, value=frm, easing="Linear"))
    f = f0
    while f <= f1 + 1e-6:
        p = named[curve]((f - f0) / (f1 - f0)) if f1 > f0 else 1.0
        if f + 2 > f1 + 1e-6: p = 1.0
        keys.append(dict(at=round(f / n, 4), value=interp(frm, to, p), easing="Linear" if not keys else "Hold"))
        f += 2
    if keys[-1]["at"] < 1: keys.append(dict(at=1, value=to, easing="Hold"))
    return {"property": prop, "keys": keys}

preset("rt_rise_twos", "Rise - on twos", "in", 16, lambda n: [
    twos("center", [0, -0.04], [0, 0], "expo-out", n), twos("blend", 0.0, 1.0, "linear", n, 0.0, 0.25)],
    ["in", "rise", "on twos", "stepped", "retro"],
    "Rises 4% on an expo curve, but held on every other frame: the hand-drawn, 12-drawings-a-second look.")
preset("rt_pop_twos", "Pop - on twos", "in", 12, lambda n: [
    twos("size", 0.0, 1.0, "spring-gentle", n)],
    ["in", "pop", "on twos", "stepped", "retro"],
    "Pops from zero with a small spring, stepped on twos. Badges, stars, retro stickers.")
preset("rt_exit_down_twos", "Exit down - on twos", "out", 12, lambda n: [
    twos("center", [0, 0], [0, -0.05], "accel", n), twos("blend", 1.0, 0.0, "linear", n, 0.5, 1.0)],
    ["out", "exit", "on twos", "stepped", "retro"],
    "Drops 5% accelerating and fades over the second half, stepped on twos.")

def build(out_dir, tol=0.01):
    os.makedirs(out_dir, exist_ok=True)
    for p in P:
        d = {"presetVersion": 2, "id": "cc.rt." + p["pid"][3:], "name": p["name"], "category": "animation",
             "tags": p["tags"] + ["retro"],
             "note": p["note"] + " Curves baked as keys (linear joins) - see the skill's ai/patterns/retro.md.",
             "anchor": p["anchor"], "frames": p["frames"], "tracks": p["tracks"](p["frames"])}
        with open(os.path.join(out_dir, p["pid"] + ".carverpreset"), "w") as f:
            json.dump(d, f, indent=1)
    pack = {"packVersion": 1, "id": "cc.retro", "name": "Retro", "origin": "carvercat-skills", "version": 1, "tier": "free",
            "note": "70s to 80s looks: motion on twos, a sunburst title, a synthwave sun over a moving grid, rainbow stripes and a checkerboard wipe. Source: carvercat-skills/ai/scripts/motion/build_retro_pack.py and categories/retro."}
    with open(os.path.join(out_dir, "pack.carverpack"), "w") as f:
        json.dump(pack, f, indent=1)
    return len(P)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "retro"
    print(build(out), "presets ->", out)
