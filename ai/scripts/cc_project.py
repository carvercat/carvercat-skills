"""Write a Carvercat project file in the stored format `carvercat/2` (design units), with the standard library only.

    from cc_project import Project
    p = Project("Sports score update")
    p.comp("Sports 14s", width=1920, height=1080, fps=30, frames=420)
    p.rectangle("Background", fill=("#2E7D32", "#1B5E20"))        # a vertical gradient; one colour string = solid
    p.save("work/rc_sports.carverproj")                           # then: edit.open {path, force: true}

The file is the one the app itself writes for a rectangle (checked: it opens, `scene.get` reads it back in px, and
`edit.save` writes it again with the same values). Values are the design units of the format: px from the comp's
top-left with y down, degrees clockwise, frames, colours as `color(srgb r g b / a)`, gradient `from`/`to` and stop
`at` in percent. The shapes written here are rectangles and ellipses; for anything richer send a `scene.apply`
document instead (`cc_scene.py`) and `edit.save`: the short route, the file it writes is the same format.
Spec: the `carvercat://schema/scene` resource of the app (the `carvercat/2` format).
"""
import json
import re

FORMAT = "carvercat/2"
MIN_APP = "0.1.8"
_HEX = re.compile(r"^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")


def srgb(colour, alpha=1.0):
    """'#RRGGBB' or '#RGB' -> 'color(srgb r g b / a)', the colour string the stored format uses."""
    if not isinstance(colour, str) or not _HEX.match(colour):
        raise ValueError("a colour here is a hex string such as '#2E7D32': %r" % (colour,))
    h = colour[1:]
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    return "color(srgb %r %r %r / %r)" % (r, g, b, float(alpha))


def _p(value):
    return {"value": value}


class Project:
    """A project of one or more comps, each a stack of shapes on video track 1 (more tracks: pass `track=`)."""

    def __init__(self, name="Untitled", project_id=None):
        self.name = name
        self.id = project_id or re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "project"
        self.comps = []
        self._clip = 0

    def comp(self, name, *, width=1920, height=1080, fps=30, frames=120):
        """Start a comp; the shapes added next go into it. Sizes are px, `frames` is the comp length."""
        for label, v in (("width", width), ("height", height), ("fps", fps), ("frames", frames)):
            if not isinstance(v, (int, float)) or isinstance(v, bool) or not v > 0:
                raise ValueError("%s must be a positive number" % label)
        self.comps.append({"id": "tl%d" % (len(self.comps) + 1), "name": name, "width": float(width), "height": float(height),
                           "fps": float(fps), "frames": float(frames), "tracks": {}, "clips": 0})
        return self

    def _shape(self, kind, name, box, fill, start, duration, radius, track):
        if not self.comps:
            raise ValueError("call comp() first")
        c = self.comps[-1]
        c["clips"] += 1
        oid = "clip_%d" % c["clips"]
        x, y, w, h = box if box is not None else (0, 0, c["width"], c["height"])
        start = 0 if start is None else start
        duration = c["frames"] - start if duration is None else duration
        if isinstance(fill, (tuple, list)):
            a, b = fill
            fill_params = {"paint": _p("gradient"), "fill": _p(srgb(a)), "opacity": _p(1.0),
                           "gradient": _p({"type": "linear", "from": [50.0, 0.0], "to": [50.0, 100.0],
                                            "stops": [{"at": 0.0, "color": srgb(a)}, {"at": 100.0, "color": srgb(b)}]})}
        else:
            fill_params = {"paint": _p("solid"), "fill": _p(srgb(fill)), "opacity": _p(1.0)}
        if kind == "rect":
            geometry = ("shape.geometry.rectangle", "rectangle",
                        {"width": _p(float(w)), "height": _p(float(h)), "borderRadius": _p(float(radius)), "rotate": _p(0.0)})
        else:
            geometry = ("shape.geometry.ellipse", "ellipse", {"width": _p(float(w)), "height": _p(float(h)), "rotate": _p(0.0)})
        cap, leaf, params = geometry
        obj = {
            "id": oid, "type": kind, "name": name, "caption": "Rectangle" if kind == "rect" else "Ellipse",
            "start": float(start), "duration": float(duration), "sourceIn": 0.0,
            "stack": {
                "source": [
                    {"id": "e_src_%s_%s" % (cap.replace(".", "_"), oid), "cap": cap, "on": True, "params": params},
                    {"id": "e_src_shape_fill_" + oid, "cap": "shape.fill", "on": True, "params": fill_params},
                    {"id": "e_src_shape_stroke_" + oid, "cap": "shape.stroke", "on": True,
                     "params": {"paint": _p("none"), "opacity": _p(1.0), "strokeWidth": _p(0.0)}}],
                "effects": [],
                "transform": [
                    {"id": "e_tr_placement_" + oid, "cap": "transform.placement", "on": True,
                     "params": {"center": _p([x + w / 2.0, y + h / 2.0]), "scale": _p([1.0, 1.0]), "scaleUniform": _p(1.0),
                                "rotate": _p(0.0), "transformOrigin": _p([50.0, 50.0]), "opacity": _p(1.0)}},
                    {"id": "e_tr_compositing_" + oid, "cap": "transform.compositing", "on": True,
                     "params": {"mixBlendMode": _p("Normal"), "combine": _p("Over")}}]},
            "controls": {"promoted": {"source": [], "effects": [], "transform": []}},
        }
        c["tracks"].setdefault(track, []).append(obj)
        return oid

    def rectangle(self, name, box=None, *, fill="#000000", start=None, duration=None, radius=0, track=0):
        """A rectangle. `box` is (x, y, w, h) in px from the top-left (default: the whole frame). `fill` is a hex
        colour, or a pair of hex colours for a top-to-bottom gradient. `radius` is the border radius in % of the
        short side. `start`/`duration` are frames (default: the whole comp). `track` 0 is video track 1."""
        return self._shape("rect", name, box, fill, start, duration, radius, track)

    def ellipse(self, name, box, *, fill="#000000", start=None, duration=None, track=0):
        return self._shape("ellipse", name, box, fill, start, duration, 0, track)

    def to_dict(self):
        comps = []
        for c in self.comps:
            layers = []
            for t in range(max(c["tracks"]) + 1 if c["tracks"] else 1):
                layers.append({"id": "track_v%d" % (t + 1), "enabled": True, "objects": c["tracks"].get(t, [])})
            comps.append({"id": c["id"], "name": c["name"], "scene": {
                "fps": c["fps"], "width": c["width"], "height": c["height"], "layers": layers,
                "audioLayers": [{"id": "atrack_1", "enabled": True, "objects": []}],
                "x-legacy": {"fields": {"ppf": 4, "duration": c["frames"], "width": c["width"], "height": c["height"],
                                        "clipCounter": c["clips"]}}}})
        return {"format": FORMAT, "minApp": MIN_APP, "id": self.id, "name": self.name,
                "lastCompId": comps[0]["id"] if comps else None, "comps": comps}

    def save(self, path):
        doc = self.to_dict()
        check(doc)
        with open(path, "w", encoding="utf8") as f:
            json.dump(doc, f, indent=1)
        return path


def check(doc):
    """The part of schema/carvercat-2.schema.json this writer depends on, with the standard library only.
    Raises ValueError with the path of the first problem."""
    def need(cond, where):
        if not cond:
            raise ValueError("not a carvercat/2 document: " + where)
    need(isinstance(doc, dict) and doc.get("format") == FORMAT, "format")
    need(isinstance(doc.get("comps", []), list) and doc.get("comps"), "comps")
    for ci, c in enumerate(doc["comps"]):
        s = c.get("scene")
        need(isinstance(s, dict), "comps[%d].scene" % ci)
        for k in ("fps", "width", "height"):
            need(isinstance(s.get(k), (int, float)) and s[k] > 0, "comps[%d].scene.%s" % (ci, k))
        need(isinstance(s.get("layers"), list), "comps[%d].scene.layers" % ci)
        for li, layer in enumerate(s["layers"]):
            for oi, o in enumerate(layer.get("objects", [])):
                where = "comps[%d].scene.layers[%d].objects[%d]" % (ci, li, oi)
                need(isinstance(o.get("id"), str) and isinstance(o.get("type"), str), where)
                need(isinstance(o.get("start"), (int, float)) and isinstance(o.get("duration"), (int, float)), where + " start/duration")
                for group in ("transform", "source", "effects"):
                    for e in o.get("stack", {}).get(group, []):
                        need(isinstance(e.get("params"), dict) and "cap" in e and "id" in e, where + ".stack." + group)
    return True
