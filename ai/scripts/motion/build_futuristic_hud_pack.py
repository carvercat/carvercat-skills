"""Build the Futuristic HUD preset pack (library/templates/futuristic-hud/, prefix fh_).

    python build_futuristic_hud_pack.py OUT_DIR

Same method as build_pattern_pack.py (curves baked to keys with LINEAR joins; values
RELATIVE to the object; positions in frame fractions, Y UP), plus multi-segment tracks:
a property can run several curves one after another (fall, squash, recover), which is
what a CRT power-down needs; hold() writes stepped keys (easing Hold) for flickers.
Templates come from futuristic_hud_lab.py via comp_to_template.py; docs
ai/patterns/futuristic-hud.md.
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

def hold(prop, steps):
    """steps: [(at, value)] -> keys that jump at each 'at' (easing Hold arrives at the key)"""
    return {"property": prop, "keys": [dict(at=a, value=v, easing="Linear" if i == 0 else "Hold") for i, (a, v) in enumerate(steps)]}

preset("fh_flicker_on", "Flicker on", "in", 12, lambda n: [
    hold("blend", [(0.0, 0.0), (0.17, 0.8), (0.33, 0.15), (0.5, 0.9), (0.67, 0.5), (0.83, 1.0), (1.0, 1.0)])],
    ["in", "flicker", "hud", "tech", "futuristic"],
    "Switches on in 12 f with stepped opacity (0 > 80 > 15 > 90 > 50 > 100%), like a display warming up. Two steps per 4 f stay well under flash limits.")
preset("fh_scan_open", "Scan open (Y)", "in", 14, lambda n: [
    track("scaleY", [(0.02, 1.0, "expo-out", 0.0, 1.0)], n),
    track("blend", [(0.0, 1.0, "linear", 0.0, 0.2)], n)],
    ["in", "scan", "open", "hud", "futuristic"],
    "Opens vertically from a 2% scanline to full height on an expo landing. Panels, readouts, video windows.")
preset("fh_power_down", "Power down", "out", 12, lambda n: [
    track("scaleY", [(1.0, 0.02, "accel", 0.0, 0.5), (0.02, 0.02, "linear", 0.5, 1.0)], n),
    track("scaleX", [(1.0, 1.0, "linear", 0.0, 0.5), (1.0, 0.0, "accel", 0.5, 1.0)], n)],
    ["out", "crt", "power", "hud", "futuristic"],
    "The CRT switch-off: collapses to a 2% line (6 f), then the line shrinks to a point (6 f).")

def build(out_dir, tol=0.01):
    os.makedirs(out_dir, exist_ok=True)
    for p in P:
        d = {"presetVersion": 2, "id": "cc.fh." + p["pid"][3:], "name": p["name"], "category": "animation",
             "tags": p["tags"] + ["futuristic hud"],
             "note": p["note"] + " Curves baked as keys (linear joins) - see the skill's ai/patterns/futuristic-hud.md.",
             "anchor": p["anchor"], "frames": p["frames"], "tracks": p["tracks"](p["frames"])}
        with open(os.path.join(out_dir, p["pid"] + ".carverpreset"), "w") as f:
            json.dump(d, f, indent=1)
    pack = {"packVersion": 1, "id": "cc.futuristic-hud", "name": "Futuristic HUD", "origin": "carvercat-skills", "version": 1, "tier": "free",
            "note": "Sci-fi interface motion: flicker-on, scan open, CRT power-down, a targeting reticle, corner brackets with a scan line, a typed data readout and a radar sweep. Source: carvercat-skills/ai/scripts/motion/build_futuristic_hud_pack.py and categories/futuristic-hud."}
    with open(os.path.join(out_dir, "pack.carverpack"), "w") as f:
        json.dump(pack, f, indent=1)
    return len(P)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "futuristic-hud"
    print(build(out), "presets ->", out)
