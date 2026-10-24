#!/usr/bin/env python3
"""Explainer overlay for a map built with geo_paths.py -> carvercat_batch steps.

Builds, in comp space of the geo_paths output:
  * hero pin (accent dot + white rim) and a pulse ring
  * catchment rings at real distances (km -> px from the projection transform)
  * hero route(s): smooth open path, round cap, trim draw-on, controlled glow
  * landmark pins + leader line (trim) + card (rounded rect) + name + sub-line
  * a callout text and a hand-built arrow (shaft with trim + chevron head)

Usage:
  python map_overlay.py dubai.json spec.json steps.json
spec.json example:
{
  "hero": "Project", "start": 64, "accent": [0.955,0.518,0.027,1],
  "rings_km": [5,10],
  "routes": [{"to": "Burj Khalifa", "via": [[985,560],[1005,665]], "frames": [98,128]}],
  "landmarks": [
     {"pin": "Burj Khalifa", "sub": "12 min by car", "card_offset": [116,-66], "at": 130},
     {"pin": "Dubai Marina", "sub": "15 min by car", "card_offset": [-170,-67], "at": 138}],
  "callout": {"text": "YOUR NEW HOME", "at": [560,810], "frame": 150,
              "arrow": [[700,780],[880,660]]},
  "end": 240
}
Pins come from geo_paths --pins (pixel coordinates). Keep every overlay INSIDE the map comp so a
camera (instance scale/position) moves them with the map. Then apply presets per object
(preset.apply is one id per call, not batchable): pins "Pop - spring", cards "Pop - gentle",
texts "Rise - expo".
"""
import json, math, sys

W = H = None

def fx(px, py):            # comp px (y down) -> center fraction (y up)
    return [round(px / W, 4), round(1 - py / H, 4)]

def pf(px, py):            # comp px -> object.path point (fraction, y down)
    return [round(px / W, 5), round(py / H, 5)]

def P(alias, key, value):
    return {"command": "property.set", "args": {"id": {"$ref": alias}, "key": key, "value": value}}

def K(alias, key, value, frame, easing="Linear"):
    return {"command": "key.set", "args": {"id": {"$ref": alias}, "key": key, "value": value, "easing": easing}, "frame": frame}

def new(kind, alias, name, frame, end):
    return [{"command": "object.new", "args": {"kind": kind, "duration": end - frame}, "frame": frame, "as": alias},
            {"command": "clip.rename", "args": {"id": {"$ref": alias}, "name": name}}]

def path(alias, name, pts, frame, end, smooth=False):
    return [{"command": "object.path", "args": {"points": [pf(*p) for p in pts], "closed": False, "smooth": smooth,
             "duration": end - frame}, "frame": frame, "as": alias},
            {"command": "clip.rename", "args": {"id": {"$ref": alias}, "name": name}}]

def stroke(alias, color, width, cap="round"):
    return [P(alias, "shape.fill.paint", "none"), P(alias, "shape.stroke.paint", "solid"),
            P(alias, "shape.stroke.color", color), P(alias, "shape.stroke.width", width),
            P(alias, "shape.stroke.cap", cap)]

def trim(alias, a, b, easing="S-curve"):
    fxa = alias + "_tr"
    return [{"command": "effect.add", "args": {"id": {"$ref": alias}, "cap": "trim"}, "as": fxa},
            K(alias, {"$param": [fxa, "end"]}, 0, a), K(alias, {"$param": [fxa, "end"]}, 1, b, easing)]

def text(alias, name, s, size, color, at, frame, end, bold=False, tracking=None):
    size = max(size, 0.01)          # text.font.size min is 0.01 (W fraction)
    out = new("text", alias, name, frame, end) + [P(alias, "text", s), P(alias, "text.font.size", size),
                                                  P(alias, "text.fill.color", color), P(alias, "center", fx(*at))]
    if bold: out.insert(4, P(alias, "text.font.style", "Bold"))
    if tracking: out.append(P(alias, "text.font.tracking", tracking))
    return out

def ellipse(alias, name, d_w, at, frame, end):
    return new("ellipse", alias, name, frame, end) + [P(alias, "shape.geometry.ellipse.width", d_w),
            P(alias, "shape.geometry.ellipse.height", d_w), P(alias, "center", fx(*at))]

def main(geo_file, spec_file, out_file):
    global W, H
    geo = json.load(open(geo_file)); spec = json.load(open(spec_file))
    W, H = geo["comp"]
    pins = {p["name"]: p["px"] for p in geo.get("pins", [])}
    px_per_km = geo["transform"]["scale"] / 6371.0
    if geo.get("projection") == "mercator":
        px_per_km /= math.cos(math.radians(geo.get("lat0", 0)))
    acc = spec.get("accent", [0.955, 0.518, 0.027, 1]); end = spec.get("end", 240)
    white = [1, 1, 1, 1]; s = []
    hx, hy = pins[spec["hero"]]; t0 = spec.get("start", 64)

    for i, km in enumerate(spec.get("rings_km", [])):
        a = f"ring{i}"; d = 2 * km * px_per_km / W; f = t0 + 6 + 8 * i
        s += ellipse(a, f"Radius {km} km", round(d, 4), (hx, hy), f, end) + stroke(a, acc[:3] + [0.6], 0.0012)
        s += [P(a, "shape.stroke.line", "dashed"), P(a, "shape.stroke.dashLength", 0.004),
              P(a, "shape.stroke.dashGap", 0.004), K(a, "size", 0, f), K(a, "size", 1, f + 22, "Ease out")]
        s += text(f"rl{i}", f"Radius label {km} km", f"{km} km", 0.011, acc, (hx, hy - km * px_per_km - 12), f + 12, end)
        s += [K(f"rl{i}", "blend", 0, f + 12), K(f"rl{i}", "blend", 1, f + 22, "Ease out")]

    for i, r in enumerate(spec.get("routes", [])):
        a = f"route{i}"; a0, a1 = r.get("frames", [t0 + 34, t0 + 64])
        pts = [(hx, hy)] + [tuple(p) for p in r.get("via", [])] + [tuple(pins[r["to"]])]
        s += path(a, f"Route to {r['to']}", pts, a0 - 2, end, smooth=True) + stroke(a, acc, 0.003) + trim(a, a0, a1)
        g = a + "_gl"          # glow: amount <= 0.8 never burns; size 12 ~ 30 px halo
        s += [{"command": "effect.add", "args": {"id": {"$ref": a}, "cap": "glow"}, "as": g},
              P(a, {"$param": [g, "size"]}, 12), P(a, {"$param": [g, "amount"]}, 0.6)]

    s += ellipse("hpulse", "Hero pulse", 0.02, (hx, hy), t0 + 2, end) + stroke("hpulse", acc, 0.0015)
    s += [K("hpulse", "size", 0.5, t0 + 4), K("hpulse", "size", 3, t0 + 28, "Ease out"),
          K("hpulse", "blend", 1, t0 + 4), K("hpulse", "blend", 0, t0 + 28, "Ease out")]
    s += ellipse("hpin", "Hero pin", 0.016, (hx, hy), t0, end) + [P("hpin", "shape.fill.color", acc),
          P("hpin", "shape.stroke.paint", "solid"), P("hpin", "shape.stroke.color", white), P("hpin", "shape.stroke.width", 0.002)]

    for i, L in enumerate(spec.get("landmarks", [])):
        px, py = pins[L["pin"]]; f = L.get("at", t0 + 66 + 8 * i)
        dx, dy = L.get("card_offset", [116, -66]); cx, cy = px + dx, py + dy
        s += ellipse(f"lp{i}", f"Pin {L['pin']}", 0.008, (px, py), f, end) + [P(f"lp{i}", "shape.fill.color", white)]
        s += path(f"ll{i}", f"Leader {L['pin']}", [(px, py), (cx, cy)], f + 4, end) + \
             [P(f"ll{i}", "shape.stroke.paint", "solid"), P(f"ll{i}", "shape.stroke.color", [1, 1, 1, 0.7]),
              P(f"ll{i}", "shape.stroke.width", 0.0008)] + trim(f"ll{i}", f + 4, f + 12, "Ease out")
        s += new("rectangle", f"lc{i}", f"Card {L['pin']}", f + 10, end) + [
             P(f"lc{i}", "shape.fill.color", [0.96, 0.96, 0.97, 1]), P(f"lc{i}", "shape.geometry.rectangle.width", 0.1),
             P(f"lc{i}", "shape.geometry.rectangle.height", 0.036), P(f"lc{i}", "shape.geometry.rectangle.cornerRadius", 0.008),
             P(f"lc{i}", "center", fx(cx, cy))]
        s += text(f"ln{i}", f"Card name {L['pin']}", L.get("label", L["pin"]), 0.0115, [0.02, 0.03, 0.06, 1], (cx, cy - 10), f + 12, end, bold=True)
        if L.get("sub"):
            s += text(f"lt{i}", f"Card sub {L['pin']}", L["sub"], 0.01, [0.75, 0.38, 0, 1], (cx, cy + 14), f + 14, end)

    c = spec.get("callout")
    if c:
        s += text("callout", f"Callout {c['text']}", c["text"], 0.016, acc, c["at"], c["frame"], end, bold=True, tracking=1.1)
        if c.get("arrow"):
            (x0, y0), (x1, y1) = c["arrow"]; f = c["frame"] + 2
            s += path("arw", "Arrow shaft", [(x0, y0), (x1, y1)], f, end) + stroke("arw", acc, 0.0021) + trim("arw", f, f + 10, "Ease out")
            ux, uy = x0 - x1, y0 - y1; n = math.hypot(ux, uy); ux, uy = ux / n, uy / n; hl = 22
            wing = lambda a: (x1 + hl * (ux * math.cos(a) - uy * math.sin(a)), y1 + hl * (ux * math.sin(a) + uy * math.cos(a)))
            s += path("ahd", "Arrow head", [wing(0.52), (x1, y1), wing(-0.52)], f + 10, end) + stroke("ahd", acc, 0.0021) + \
                 [P("ahd", "shape.stroke.corners", "round"), K("ahd", "blend", 0, f + 10), K("ahd", "blend", 1, f + 13, "Ease out")]

    json.dump(s, open(out_file, "w"))
    print(f"{len(s)} steps -> {out_file} (px/km {px_per_km:.2f}); batches hold <= 256 steps")

if __name__ == "__main__":
    main(*sys.argv[1:4])
