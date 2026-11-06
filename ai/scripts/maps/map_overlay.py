#!/usr/bin/env python3
"""Explainer overlay for a map built with geo_paths.py, in design units (px, y down, CSS colours and easing).

Builds, in comp space of the geo_paths output:
  * hero pin (accent dot + white rim) and a pulse ring
  * catchment rings at real distances (km -> px from the projection transform)
  * hero route(s): smooth open path, round cap, trim draw-on, controlled glow
  * landmark pins + leader line (trim) + card (rounded rect) + name + sub-line
  * a callout text and a hand-built arrow (shaft with trim + chevron head)

Usage (a private headless Carvercat; never the visible editor):
  CARVERCAT_RESOURCE_ROOT=<the app resource folder> python map_overlay.py geo.json spec.json --exe /path/to/carvercat-host --out job.carverproj
  or from Python: map_overlay.build_map(client, geo); map_overlay.build_overlay(client, geo, spec)
spec.json example:
{
  "hero": "Project", "start": 64, "accent": "#F3840A",
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
import json, math, os, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cc_client import Client, Refused  # noqa: E402

WHITE = "#ffffff"


def build_map(c, geo):
    """One closed or open path per ring (object.path pointsPx), named after its feature. Returns the object ids."""
    ids = []
    for step in geo["steps"]:
        oid = c.run(step["command"], **step["args"])["touched"][0]
        c.run("clip.rename", id=oid, name=step["name"])
        ids.append(oid)
    return ids


def _style(c, oid, **style):
    for k, v in style.items():
        c.run("property.set", id=oid, key=k, value=v)


def _new(c, kind, name, at, end, **style):
    r = c.run("object.new", kind=kind, frame=at, duration=end - at)
    oid = r["touched"][0]
    c.run("clip.rename", id=oid, name=name)
    return oid


def _box(c, kind, name, cx, cy, w, h, at, end, **style):
    """A shape whose CENTRE is (cx, cy) px: x, y are the top-left."""
    oid = _new(c, kind, name, at, end)
    _style(c, oid, width=w, height=h, x=round(cx - w / 2, 2), y=round(cy - h / 2, 2), **style)
    return oid


def _text(c, name, s, size, color, cx, cy, at, end, w=360, weight=400, spacing=None):
    oid = _new(c, "text", name, at, end)
    c.run("property.set", id=oid, key="text", value=s)
    _style(c, oid, fontSize=size, fill=color, fontWeight=weight, textAlign="center", whiteSpace="normal", width=w, height=round(size * 1.4, 1))
    if spacing:
        c.run("property.set", id=oid, key="letterSpacing", value=spacing)
    box = c.run("property.get", id=oid, key="width")["units"]["values"]
    _style(c, oid, x=round(cx - w / 2, 2), y=round(cy - box["height"] / 2, 2))
    return oid


def _fade(c, oid, a, b, ease="ease-out"):
    c.run("anim.set", id=oid, keyframes=[{"atComp": a, "opacity": 0, "ease": ease}, {"atComp": b, "opacity": 1}])


def _draw_on(c, oid, a, b, ease="ease-in-out"):
    """Draw a stroke on with trimEnd 0% -> 100%; fade it in if the build refuses the trim key."""
    try:
        c.run("anim.set", id=oid, keyframes=[{"atComp": a, "trimEnd": "0%", "ease": ease}, {"atComp": b, "trimEnd": "100%"}])
        return "trim"
    except Refused:
        _fade(c, oid, a, b)
        return "fade"


def build_overlay(c, geo, spec):
    W, H = geo["comp"]
    pins = {p["name"]: p["px"] for p in geo.get("pins", [])}
    px_per_km = geo["transform"]["scale"] / 6371.0
    if geo.get("projection") == "mercator":
        px_per_km /= math.cos(math.radians(geo.get("lat0", 0)))
    acc = spec.get("accent", "#F3840A")
    end = spec.get("end", 240)
    t0 = spec.get("start", 64)
    hx, hy = pins[spec["hero"]]
    report = []

    for i, km in enumerate(spec.get("rings_km", [])):
        f = t0 + 6 + 8 * i
        d = 2 * km * px_per_km
        ring = _box(c, "ellipse", f"Radius {km} km", hx, hy, d, d, f, end, fill="none", stroke=acc + "99", strokeWidth=2.3,
                    strokeDasharray="7.7 7.7")
        c.run("anim.set", id=ring, keyframes=[{"atComp": f, "scale": 0, "ease": "ease-out"}, {"atComp": f + 22, "scale": 1}])
        lab = _text(c, f"Radius label {km} km", f"{km} km", 21, acc, hx, hy - km * px_per_km - 12, f + 12, end, w=140)
        _fade(c, lab, f + 12, f + 22)

    for i, r in enumerate(spec.get("routes", [])):
        a0, a1 = r.get("frames", [t0 + 34, t0 + 64])
        pts = [(hx, hy)] + [tuple(p) for p in r.get("via", [])] + [tuple(pins[r["to"]])]
        d = "M " + " L ".join("%s %s" % p for p in pts)
        oid = c.path(d, duration=end, fill="none", stroke=acc, strokeWidth=5.8, strokeLinecap="round", strokeLinejoin="round")
        c.run("clip.rename", id=oid, name=f"Route to {r['to']}")
        c.run("property.set", id=oid, key="glow", value=f"12px {acc} 0.6 0.2")
        report.append(("route %d" % i, _draw_on(c, oid, a0, a1)))

    pulse = _box(c, "ellipse", "Hero pulse", hx, hy, 38.4, 38.4, t0 + 2, end, fill="none", stroke=acc, strokeWidth=2.9)
    c.run("anim.set", id=pulse, keyframes=[{"atComp": t0 + 4, "scale": 0.5, "opacity": 1, "ease": "ease-out"}, {"atComp": t0 + 28, "scale": 3, "opacity": 0}])
    _box(c, "ellipse", "Hero pin", hx, hy, 30.7, 30.7, t0, end, fill=acc, stroke=WHITE, strokeWidth=3.8)

    for i, L in enumerate(spec.get("landmarks", [])):
        px, py = pins[L["pin"]]
        f = L.get("at", t0 + 66 + 8 * i)
        dx, dy = L.get("card_offset", [116, -66])
        cx, cy = px + dx, py + dy
        _box(c, "ellipse", f"Pin {L['pin']}", px, py, 15.4, 15.4, f, end, fill=WHITE)
        lead = c.path(f"M {px} {py} L {cx} {cy}", frame=f, duration=end - f, fill="none", stroke="#ffffffb3", strokeWidth=1.5)
        c.run("clip.rename", id=lead, name=f"Leader {L['pin']}")
        report.append(("leader %d" % i, _draw_on(c, lead, f + 4, f + 12, "ease-out")))
        card = _box(c, "rectangle", f"Card {L['pin']}", cx, cy, 192, 69, f + 10, end, fill="#f5f5f7", borderRadius=15.4)
        _fade(c, card, f + 10, f + 18)
        name = _text(c, f"Card name {L['pin']}", L.get("label", L["pin"]), 22, "#050810", cx, cy - 10, f + 12, end, w=180, weight=700)
        _fade(c, name, f + 12, f + 20)
        if L.get("sub"):
            sub = _text(c, f"Card sub {L['pin']}", L["sub"], 19, "#bf6100", cx, cy + 14, f + 14, end, w=180)
            _fade(c, sub, f + 14, f + 22)

    cal = spec.get("callout")
    if cal:
        t = _text(c, f"Callout {cal['text']}", cal["text"], 31, acc, cal["at"][0], cal["at"][1], cal["frame"], end, w=520, weight=700, spacing=1.1)
        _fade(c, t, cal["frame"], cal["frame"] + 10)
        if cal.get("arrow"):
            (x0, y0), (x1, y1) = cal["arrow"]
            f = cal["frame"] + 2
            shaft = c.path(f"M {x0} {y0} L {x1} {y1}", frame=f, duration=end - f, fill="none", stroke=acc, strokeWidth=4, strokeLinecap="round")
            c.run("clip.rename", id=shaft, name="Arrow shaft")
            report.append(("arrow shaft", _draw_on(c, shaft, f, f + 10, "ease-out")))
            ux, uy = x0 - x1, y0 - y1
            n = math.hypot(ux, uy)
            ux, uy = ux / n, uy / n
            hl = 22
            wing = lambda a: (round(x1 + hl * (ux * math.cos(a) - uy * math.sin(a)), 2), round(y1 + hl * (ux * math.sin(a) + uy * math.cos(a)), 2))
            w1, w2 = wing(0.52), wing(-0.52)
            head = c.path(f"M {w1[0]} {w1[1]} L {x1} {y1} L {w2[0]} {w2[1]}", frame=f, duration=end - f, fill="none", stroke=acc, strokeWidth=4,
                          strokeLinecap="round", strokeLinejoin="round")
            c.run("clip.rename", id=head, name="Arrow head")
            _fade(c, head, f + 10, f + 13)
    return report


def main(geo_file, spec_file, exe, out):
    geo = json.load(open(geo_file))
    spec = json.load(open(spec_file))
    with tempfile.TemporaryDirectory() as d:
        with Client.stdio(exe, d) as c:
            W, H = geo["comp"]
            c.run("comp.format", width=W, height=H, fps=30)
            build_map(c, geo)
            report = build_overlay(c, geo, spec)
            c.run("edit.save", path=str(Path(out).resolve()))
    print("saved", out, report)


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("geo")
    ap.add_argument("spec")
    ap.add_argument("--exe", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    main(a.geo, a.spec, a.exe, a.out)
