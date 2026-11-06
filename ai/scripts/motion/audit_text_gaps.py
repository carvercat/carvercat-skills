"""Audit every Library template in the skills repo for small text overlaps that lint misses.
Each template's scene becomes a timeline in one audit project; for every pair of texts (and text vs small
shape, both sides <= 80 px) that are visible and AT REST together, measure the gap with
carvercat_authoring geometry at the middle of their shared rest window."""
import json, glob, shutil, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "recipes"))
from recipe_kit import client, open_project, switch, LAB, S      # CARVERCAT_EXE, CARVERCAT_STATE, RECIPE_LAB (headless only)
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
# usage: python audit_text_gaps.py [name-fragment ... | path/to/x.carvertemplate ...]; writes RECIPE_LAB/work/audit_overlap.json
p = LAB + "/audit_overlap.carverproj"
shutil.copy(LAB + "/base.carverproj", p)
d = json.load(open(p))
tpls = sorted(glob.glob(REPO + "/library/templates/*/*.carvertemplate"))
only = sys.argv[1:]
if only: tpls = [o for o in only if o.endswith(".carvertemplate") and os.path.exists(o)] or [t for t in tpls if any(o in t for o in only)]
tls = []
for i, f in enumerate(tpls):
    t = json.load(open(f)); sc = t["scene"]
    sc.setdefault("audioTracks", [{"id": "atrack_1", "enabled": True, "clips": []}])
    tls.append({"id": f"tl_aud{i}", "name": "AUD " + os.path.basename(f), "scene": sc, "bin": None})
d["timelines"] = tls; d["lastTimelineId"] = tls[-1]["id"]
json.dump(d, open(p, "w"), separators=(",", ":"))

def clusters(keys):
    ks = sorted(set(keys))
    if not ks: return []
    out = [[ks[0]]]
    for k in ks[1:]:
        if k - out[-1][-1] <= 12: out[-1].append(k)
        else: out.append([k])
    return out

def rest_window(o):
    c0, c1 = o["clip"]
    ent = int(o["enters"].split("(")[1].rstrip(")")) if o.get("enters") else None
    ex = int(o["exits"].split("(")[1].rstrip(")")) if o.get("exits") else None
    if ent is None or ex is None: return None
    cl = clusters(o.get("key_frames") or [])
    a, b = ent, ex
    if cl and cl[0][0] <= ent + 2: a = max(a, cl[0][-1])                       # after the entrance keys
    if len(cl) > 1 and len(cl[-1]) >= 2 and cl[-1][-1] >= c1 - 2: b = min(b, cl[-1][0])   # before the exit keys
    return (a, b) if b > a else None

def gap(A, B):
    ax0, ay0, ax1, ay1 = A["x"], A["y"], A["x"] + A["w"], A["y"] + A["h"]
    bx0, by0, bx1, by1 = B["x"], B["y"], B["x"] + B["w"], B["y"] + B["h"]
    gx = max(bx0 - ax1, ax0 - bx1); gy = max(by0 - ay1, ay0 - by1)
    if gx < 0 and gy < 0: return max(gx, gy)          # overlapping: negative = overlap depth (smaller side)
    if gx < 0: return gy
    if gy < 0: return gx
    return (gx * gx + gy * gy) ** 0.5

report = {}
with client() as c:
    open_project(c, p)
    for tl in tls:
        name = tl["name"]; switch(c, name)
        tm = c.tool("carvercat_inspect", mode="timing")["objects"]
        cache = {}
        def bounds(o, fr):
            k = (o["id"], fr)
            if k not in cache:
                cache[k] = c.tool("carvercat_authoring", mode="geometry", id=o["id"], frame=fr, detail="bounds")["bounds"]
            return cache[k]
        objs = [o for o in tm if o["kind"] in ("text", "shape")]
        for o in objs: o["rw"] = rest_window(o)
        texts = [o for o in objs if o["kind"] == "text" and o["rw"]]
        small = []
        for o in objs:
            if o["kind"] == "shape" and o["rw"]:
                fr = (o["rw"][0] + o["rw"][1]) // 2
                b = bounds(o, fr)
                if b["w"] <= 80 and b["h"] <= 80: small.append(o)
        pairs = [(a, b) for i, a in enumerate(texts) for b in texts[i + 1:]] + [(a, s) for a in texts for s in small]
        worst = None; flags = []
        for a, b in pairs:
            lo, hi = max(a["rw"][0], b["rw"][0]), min(a["rw"][1], b["rw"][1])
            if hi <= lo: continue
            fr = (lo + hi) // 2
            g = gap(bounds(a, fr), bounds(b, fr))
            if worst is None or g < worst[0]: worst = (round(g, 1), a["name"], b["name"], fr)
            if g < 12: flags.append((round(g, 1), a["name"], b["name"], fr))
        report[name] = {"pairs": len(pairs), "min": worst, "flags": flags}
        print(name, "pairs", len(pairs), "min", worst, "FLAGS" if flags else "", flags[:6], flush=True)
json.dump(report, open(S + "/work/audit_overlap.json", "w"), indent=1)
