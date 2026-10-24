"""GeoJSON -> Carvercat paths (dependency-free). Polygons -> closed paths; (Multi)LineStrings
(roads, rivers, rail) -> open paths. --fit-from reuses another output's projection so
overlays (roads on an emirate map) line up exactly.

    python geo_paths.py SRC.geojson OUT.json --where adm0_a3=ARE [--where ...]
        [--name-field name] [--proj equal_earth|mercator|local]
        [--box 160,120,1600,840] [--comp 1920x1080] [--tol 1.5]
        [--min-area 40] [--pins "Burj Khalifa:55.2744,25.1972;DXB:55.3657,25.2532"]
        [--rename "Dubay:Dubai;Fujayrah:Fujairah"]

Writes OUT.json:
  {comp, box, projection, transform, features:[{name, rings:[[[x,y]...]...], label:[x,y], bbox}],
   pins:[{name, lonlat, px}], steps:[ carvercat_batch steps: one closed object.path per ring ]}

* rings / label / px are comp PIXELS, top-left origin, y down.
* steps use object.path with frame-fraction points (y DOWN); paste into carvercat_batch
  (<= 256 steps per call). Largest ring first per feature so the mainland draws first.
* Projections: equal_earth (world/region, honest areas), mercator (matches web maps,
  satellite plates), local (equirectangular scaled by cos(lat0); city/community scale).
* Douglas-Peucker in PIXELS (--tol), ring-safe. Rings under --min-area px^2 are dropped.
* Label anchor = pole of inaccessibility (grid search), not the centroid.

Data: Natural Earth (public domain, no attribution needed), e.g.
  https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_0_countries.geojson
  .../ne_10m_admin_1_states_provinces.geojson  (the only NE file with UAE emirates;
  names "Dubay"/"Fujayrah" - rename). OSM-derived data needs "(c) OpenStreetMap
  contributors" on screen - see references/maps/maps.md.
"""
import argparse, json, math

A1, A2, A3, A4 = 1.340264, -0.081106, 0.000893, 0.003796

def equal_earth(lon, lat, lat0=0):
    l, p = math.radians(lon), math.radians(lat)
    t = math.asin(math.sqrt(3) / 2 * math.sin(p)); t2 = t * t; t6 = t2 ** 3
    x = 2 * math.sqrt(3) * l * math.cos(t) / (3 * (A1 + 3 * A2 * t2 + t6 * (7 * A3 + 9 * A4 * t2)))
    return x, t * (A1 + A2 * t2 + t6 * (A3 + A4 * t2))

def mercator(lon, lat, lat0=0):
    lat = max(-85.05112878, min(85.05112878, lat))
    return math.radians(lon), math.log(math.tan(math.pi / 4 + math.radians(lat) / 2))

def local(lon, lat, lat0=0):
    return math.radians(lon) * math.cos(math.radians(lat0)), math.radians(lat)

PROJ = {"equal_earth": equal_earth, "mercator": mercator, "local": local}

def haversine_km(a, b):
    (lo1, la1), (lo2, la2) = [(math.radians(x), math.radians(y)) for x, y in (a, b)]
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * 6371.0088 * math.asin(math.sqrt(h))

def _seg(p, a, b):
    (x, y), (x1, y1), (x2, y2) = p, a, b
    dx, dy = x2 - x1, y2 - y1
    if dx == dy == 0: return math.hypot(x - x1, y - y1)
    t = max(0, min(1, ((x - x1) * dx + (y - y1) * dy) / (dx * dx + dy * dy)))
    return math.hypot(x - x1 - t * dx, y - y1 - t * dy)

def dp(pts, tol):
    if len(pts) < 3: return pts
    keep = {0, len(pts) - 1}; stack = [(0, len(pts) - 1)]
    while stack:
        a, b = stack.pop(); worst, wi = 0, None
        for i in range(a + 1, b):
            d = _seg(pts[i], pts[a], pts[b])
            if d > worst: worst, wi = d, i
        if wi is not None and worst > tol:
            keep.add(wi); stack += [(a, wi), (wi, b)]
    return [pts[i] for i in sorted(keep)]

def dp_ring(ring, tol):
    if ring[0] == ring[-1]: ring = ring[:-1]
    if len(ring) < 4: return ring
    h = len(ring) // 2
    return dp(ring[:h + 1], tol)[:-1] + dp(ring[h:] + [ring[0]], tol)[:-1]

def area(r):
    return abs(sum(r[i][0] * r[(i + 1) % len(r)][1] - r[(i + 1) % len(r)][0] * r[i][1] for i in range(len(r)))) / 2

def inside(pt, r):
    x, y = pt; c = False
    for i in range(len(r)):
        (x1, y1), (x2, y2) = r[i], r[(i + 1) % len(r)]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1 + 1e-12) + x1: c = not c
    return c

def pole(rings, n=46):
    r = max(rings, key=area); xs = [p[0] for p in r]; ys = [p[1] for p in r]
    best, bp = -1, (sum(xs) / len(xs), sum(ys) / len(ys))
    for i in range(n):
        for j in range(n):
            p = (min(xs) + (max(xs) - min(xs)) * (i + .5) / n, min(ys) + (max(ys) - min(ys)) * (j + .5) / n)
            if not inside(p, r): continue
            d = min(_seg(p, r[k], r[(k + 1) % len(r)]) for k in range(len(r)))
            if d > best: best, bp = d, p
    return [round(bp[0], 1), round(bp[1], 1)]

def polys(g):
    """Outer rings of polygons, or each line of (Multi)LineString as an open 'ring'."""
    t = g["type"]
    if t == "Polygon": return [g["coordinates"]]
    if t == "MultiPolygon": return g["coordinates"]
    if t == "LineString": return [[g["coordinates"]]]
    if t == "MultiLineString": return [[l] for l in g["coordinates"]]
    return []

def is_line(g):
    return g["type"] in ("LineString", "MultiLineString")

def prop(f, k):
    p = f["properties"]
    return p.get(k, p.get(k.upper(), p.get(k.lower())))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("out")
    ap.add_argument("--where", action="append", default=[])
    ap.add_argument("--name-field", default="name")
    ap.add_argument("--proj", default="equal_earth", choices=PROJ)
    ap.add_argument("--box", default="160,120,1600,840")
    ap.add_argument("--comp", default="1920x1080")
    ap.add_argument("--tol", type=float, default=1.5)
    ap.add_argument("--min-area", type=float, default=40)
    ap.add_argument("--pins", default="")
    ap.add_argument("--rename", default="")
    ap.add_argument("--bbox", default="", help="lon0,lat0,lon1,lat1: keep features touching it, clip lines to it")
    ap.add_argument("--fit-bbox", default="", help="lon0,lat0,lon1,lat1: frame THIS area in --box (shapes may run off-frame)")
    ap.add_argument("--fit-from", default="", help="reuse projection+transform from an earlier OUT.json (overlays: roads on a map)")
    a = ap.parse_args()
    W, H = map(int, a.comp.split("x")); bx, by, bw, bh = map(float, a.box.split(","))
    data = json.load(open(a.src, encoding="utf-8"))
    conds = [w.split("=", 1) for w in a.where]
    feats = [f for f in data["features"] if f.get("geometry") and all(str(prop(f, k)) == v for k, v in conds)]
    bb = list(map(float, a.bbox.split(","))) if a.bbox else None
    inbb = lambda pt: bb is None or (bb[0] <= pt[0] <= bb[2] and bb[1] <= pt[1] <= bb[3])
    if bb:
        feats = [f for f in feats if any(inbb(pt) for poly in polys(f["geometry"]) for ring in poly for pt in ring)]
    if not feats: raise SystemExit("no features match " + str(a.where))
    def rings_of(f):
        out = []
        for poly in polys(f["geometry"]):
            r = poly[0]
            if is_line(f["geometry"]) and bb:      # clip a line to the bbox (keep runs inside)
                run = []
                for pt in r:
                    if inbb(pt): run.append(pt)
                    elif run: out.append(run); run = []
                if run: out.append(run)
            else: out.append(r)
        return out
    if a.fit_from:
        ff = json.load(open(a.fit_from, encoding="utf-8"))
        a.proj, lat0 = ff["projection"], ff["lat0"]; s, ox, oy = ff["transform"]["scale"], ff["transform"]["ox"], ff["transform"]["oy"]
        pr = lambda lon, lat: PROJ[a.proj](lon, lat, lat0)
        proj = [[[pr(*pt) for pt in r] for r in rings_of(f)] for f in feats]
    else:
        fb = list(map(float, a.fit_bbox.split(","))) if a.fit_bbox else None
        lats = [fb[1], fb[3]] if fb else [pt[1] for f in feats for r in rings_of(f) for pt in r]
        lat0 = (min(lats) + max(lats)) / 2
        pr = lambda lon, lat: PROJ[a.proj](lon, lat, lat0)
        proj = [[[pr(*pt) for pt in r] for r in rings_of(f)] for f in feats]
        if fb:
            c = [pr(fb[0], fb[1]), pr(fb[2], fb[3])]; xs = [c[0][0], c[1][0]]; ys = [c[0][1], c[1][1]]
        else:
            xs = [p[0] for f in proj for r in f for p in r]; ys = [p[1] for f in proj for r in f for p in r]
        s = min(bw / (max(xs) - min(xs)), bh / (max(ys) - min(ys)))
        ox = bx + (bw - s * (max(xs) - min(xs))) / 2 - s * min(xs)
        oy = by + (bh - s * (max(ys) - min(ys))) / 2 + s * max(ys)
    to_px = lambda p: (ox + s * p[0], oy - s * p[1])
    ren = dict(x.split(":", 1) for x in a.rename.split(";") if ":" in x)
    out = {"comp": [W, H], "box": [bx, by, bw, bh], "projection": a.proj, "lat0": lat0,
           "transform": {"scale": s, "ox": ox, "oy": oy}, "features": [], "pins": [], "steps": []}
    for f, fp in zip(feats, proj):
        rings = []; line = is_line(f["geometry"])
        for r in fp:
            if line:
                o = dp([to_px(p) for p in r], a.tol)
                if len(o) >= 2 and math.dist(o[0], o[-1]) + sum(math.dist(o[i], o[i+1]) for i in range(len(o)-1)) > 4:
                    rings.append([[round(x, 1), round(y, 1)] for x, y in o])
            else:
                o = dp_ring([to_px(p) for p in r], a.tol)
                if len(o) >= 3 and area(o) >= a.min_area: rings.append([[round(x, 1), round(y, 1)] for x, y in o])
        if not rings: continue
        if not line: rings.sort(key=area, reverse=True)
        name = str(prop(f, a.name_field) or "feature"); name = ren.get(name, name)
        xs2 = [p[0] for r in rings for p in r]; ys2 = [p[1] for r in rings for p in r]
        out["features"].append({"name": name, "line": line, "rings": rings, "label": (rings[0][len(rings[0]) // 2] if line else pole(rings)),
                                "bbox": [min(xs2), min(ys2), max(xs2) - min(xs2), max(ys2) - min(ys2)]})
    for item in [x for x in a.pins.split(";") if x.strip()]:
        nm, ll = item.rsplit(":", 1); lon, lat = map(float, ll.split(","))
        x, y = to_px(pr(lon, lat)); out["pins"].append({"name": nm, "lonlat": [lon, lat], "px": [round(x, 1), round(y, 1)]})
    for fi, f in enumerate(out["features"]):
        for ri, r in enumerate(f["rings"]):
            al = f"f{fi}r{ri}"
            out["steps"] += [{"command": "object.path", "args": {"points": [[round(x / W, 5), round(y / H, 5)] for x, y in r], "closed": not f["line"]}, "as": al},
                             {"command": "clip.rename", "args": {"id": {"$ref": al}, "name": f["name"] + ("" if ri == 0 else f" island {ri}")}}]
    json.dump(out, open(a.out, "w", encoding="utf-8"), indent=1)
    print(f"{len(out['features'])} features, {sum(len(f['rings']) for f in out['features'])} rings, "
          f"{sum(len(r) for f in out['features'] for r in f['rings'])} points, {len(out['steps'])} steps; scale {s:.1f}")
    for f in out["features"]: print(" ", f["name"], "label", f["label"], "rings", len(f["rings"]))
    for p in out["pins"]: print("pin", p["name"], p["px"])
    if len(out["pins"]) >= 2:
        print("pins 1-2 straight-line km:", round(haversine_km(out["pins"][0]["lonlat"], out["pins"][1]["lonlat"]), 1))

if __name__ == "__main__":
    main()
