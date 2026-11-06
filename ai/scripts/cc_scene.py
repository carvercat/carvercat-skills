"""Scene builder in Carvercat design units (API 1.0).

Everything is px from the frame's top-left with y down, degrees clockwise, CSS colours and CSS easing, and time as
frames, "1.5s" or "500ms". The builder collects objects into ONE scene document and sends it with `scene.apply`:
the whole document is checked before anything changes, it is one undo step, and applying it again changes only what
differs (objects keep the scene `id` they were given).

    from cc_client import Client
    from cc_scene import Scene, Box

    with Client.stdio(exe, state_dir) as c:
        s = Scene(c, width=1920, height=1080, fps=30, duration="4s")
        s.rectangle("plate", Box(160, 700, 900, 220), fill="#1a1c26", radius=24)
        s.text("name", "Alex Morgan", box=Box(220, 730, 780, 110), size=88, weight=700)
        s.entrance(["plate", "name"], frames=14, stagger=4)
        s.apply(dry_run=True)            # what would change, in design units; nothing changes
        s.apply(preflight="resolve")     # applies, then says what carves exactly, approximately or not at all

Renamed from the earlier toolkit (see references/app/design-units.md "Old names"): `linear_hex` is gone (colours are
plain CSS strings), `size` is px (a true em), `radius` is px, `rebind` and `manifest` are gone (scene ids are the
identity), `fx_set`/`fx_keys`/`remove_effect` are replaced by effect style keys, `image_card` is gone (use
`media.import`, `layout.fit` and a `clipPath`). `Scene.path(name, d, ...)` is a `type: "path"` scene node (KI-166 is fixed);
`Client.path(d, **style)` still makes one outside a scene with object.path. `Scene.null(name, x, y)` is a null object.
"""
import json
import re
from dataclasses import dataclass

from cc_client import CarvercatError

COLOUR = re.compile(r"^#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")


def finite(*values):
    for v in values:
        if isinstance(v, bool) or not isinstance(v, (int, float)) or v != v or v in (float("inf"), float("-inf")):
            raise ValueError("finite numbers only")
    return values


def css_colour(value):
    """Validate a CSS colour string and return it unchanged. Names, rgb() and hsl() pass through (the app checks them)."""
    if not isinstance(value, str) or not value:
        raise ValueError("a colour is a CSS string such as '#FF7A00', 'rgb(255 122 0)' or 'orange'")
    if value.startswith("#") and not COLOUR.match(value):
        raise ValueError("bad hex colour: " + value)
    return value


def gradient(stops, *, angle=90, radial=False):
    """CSS gradient string from [(percent_0_to_100, colour), ...]. `angle` is CSS degrees (90 = left to right)."""
    if len(stops) < 2:
        raise ValueError("at least two gradient stops are required")
    body = ", ".join("%s %s%%" % (css_colour(c), p) for p, c in sorted(stops))
    return ("radial-gradient(circle, %s)" % body) if radial else ("linear-gradient(%sdeg, %s)" % (angle, body))


@dataclass(frozen=True)
class Box:
    """A box in frame px: x, y are the top-left, y grows downward."""
    x: float
    y: float
    w: float
    h: float

    def __post_init__(self):
        finite(self.x, self.y, self.w, self.h)
        if self.w < 0 or self.h < 0:
            raise ValueError("a box has no negative size")

    @property
    def center(self):
        return self.x + self.w / 2, self.y + self.h / 2

    def inset(self, padding):
        finite(padding)
        if padding * 2 > min(self.w, self.h):
            raise ValueError("inset larger than the box")
        return Box(self.x + padding, self.y + padding, self.w - 2 * padding, self.h - 2 * padding)

    def overlaps(self, o):
        return self.x < o.x + o.w and self.x + self.w > o.x and self.y < o.y + o.h and self.y + self.h > o.y

    def contains(self, o):
        return self.x <= o.x and self.y <= o.y and self.x + self.w >= o.x + o.w and self.y + self.h >= o.y + o.h


def _slug(name):
    s = re.sub(r"[^A-Za-z0-9_-]+", "-", name).strip("-")
    return s or "object"


def _frames(at, fps=30):
    if isinstance(at, (int, float)):
        return float(at)
    m = re.match(r"^([0-9.]+)(f|s|ms)?$", str(at))
    if not m:
        return 0.0
    v = float(m.group(1))
    return v * fps if m.group(2) == "s" else v * fps / 1000 if m.group(2) == "ms" else v


class Scene:
    """Collects objects into one `carvercat/2.0` scene document; `apply()` sends it."""

    def __init__(self, client, *, width=None, height=None, fps=None, duration="4s", prefix=""):
        self.client = client
        comp = {}
        if width or height or fps:
            if not (width and height and fps):
                raise ValueError("give width, height and fps together")
            comp = {"width": width, "height": height, "fps": fps}
        comp["duration"] = duration
        self.comp = comp
        self.width, self.height = width, height
        self.prefix = prefix
        self.nodes = []
        self.by_id = {}
        self.names = {}
        self.ids = {}  # scene id -> object id, filled by apply()

    # -- identity --------------------------------------------------------------------------------------------
    def sid(self, name):
        """The scene id a name gets. Scene ids hold letters, digits, _ and -; the display name is kept as `name`."""
        return self.names.setdefault(name, self.prefix + _slug(name))

    def node(self, name, type, *, parent=None, text=None, d=None, start=None, duration=None, tags=None, **style):
        sid = self.sid(name)
        if sid in self.by_id:
            n = self.by_id[sid]
            if n["type"] != type:
                raise CarvercatError("%s is a %s; it cannot become a %s" % (name, n["type"], type))
            n["style"].update(style)
        else:
            n = {"id": sid, "type": type, "name": name, "style": dict(style)}
            if parent:
                self.by_id[self.sid(parent)].setdefault("children", []).append(n)
            else:
                self.nodes.append(n)
            self.by_id[sid] = n
        for k, v in (("text", text), ("d", d), ("start", start), ("duration", duration), ("tags", tags)):
            if v is not None:
                n[k] = v
        for k, v in n["style"].items():
            if k in ("fill", "stroke") and isinstance(v, str) and v.startswith("#"):
                css_colour(v)
        return n

    def target(self, name):
        """Selector for a scene object: use it wherever a command takes an id."""
        return "#" + self.sid(name)

    # -- objects ---------------------------------------------------------------------------------------------
    def rectangle(self, name, box, *, fill="#151B2A", alpha=1, radius=0, start=None, duration=None, **style):
        return self.node(name, "rect", start=start, duration=duration, x=box.x, y=box.y, width=box.w, height=box.h,
                         fill=fill, opacity=alpha, borderRadius=radius, **style)

    def ellipse(self, name, box, *, fill="#151B2A", alpha=1, start=None, duration=None, **style):
        return self.node(name, "ellipse", start=start, duration=duration, x=box.x, y=box.y, width=box.w, height=box.h,
                         fill=fill, opacity=alpha, **style)

    def text(self, name, content, *, box=None, x=None, y=None, size=64, family=None, weight=400, color="#FFFFFF",
             align="left", start=None, duration=None, **style):
        """Text in px. With `box` it is box text that wraps at spaces; with x and y it is point text (top-left of its
        layout box). `size` is the true em size in px."""
        base = {"fontSize": size, "fontWeight": weight, "fill": color, "textAlign": align}
        if family:  # leave it out for the app's bundled default; name an installed family otherwise
            base["fontFamily"] = family
        if box is not None:
            base.update(x=box.x, y=box.y, width=box.w, height=box.h, whiteSpace="normal")
        else:
            if x is None or y is None:
                raise ValueError("give a box, or x and y")
            base.update(x=x, y=y)
        base.update(style)
        return self.node(name, "text", text=content, start=start, duration=duration, **base)

    def group(self, name, **style):
        return self.node(name, "group", **style)

    def path(self, name, d, *, stroke="#FFFFFF", stroke_width=2, parent=None, start=None, duration=None, **style):
        """A path node: SVG path data `d` in frame px (y down; one subpath), an open stroked line by default. Key `trimEnd`
        0% -> 100% to draw it on. Children of a parent are measured from the parent's top-left."""
        base = {"fill": "none", "stroke": stroke, "strokeWidth": stroke_width}
        base.update(style)
        return self.node(name, "path", parent=parent, d=d, start=start, duration=duration, **base)

    def null(self, name, x, y, *, parent=None, **style):
        """A null object: a transform only, drawn as nothing, the parent of a rig. `x`, `y` are the top-left of its nominal
        100 x 100 px box, so its centre (and the default pivot) is (x + 50, y + 50). Put children under it with
        `parent=name` on their own calls (their x, y then count from the null's top-left) and animate the null with
        `keys(name, "rotate" | "x" | "y" | "scale", ...)`. It takes no width, height or opacity."""
        return self.node(name, "null", parent=parent, x=x, y=y, **style)

    def set(self, name, key, value):
        """Set one design key (the scene stores it as `style`)."""
        self.by_id[self.sid(name)]["style"][key] = value
        return self

    # -- animation -------------------------------------------------------------------------------------------
    def keys(self, name, key, pairs, *, ease="ease-out"):
        """Keyframes of one design key: pairs of (at, value); `at` is frames from the object's start or "0.5s".
        `ease` shapes the segment that LEAVES a key, as in CSS."""
        n = self.by_id[self.sid(name)]
        frames = n.setdefault("keyframes", [])
        for at, value in pairs:
            row = next((f for f in frames if f["at"] == at), None)
            if row is None:
                row = {"at": at, "props": {}}
                frames.append(row)
            row["props"][key] = value
            if ease and "ease" not in row:
                row["ease"] = ease
        frames.sort(key=lambda f: _frames(f["at"]))
        return self

    def entrance(self, names, *, start=0, frames=12, stagger=0, scale=0.94, rise=0, ease="cubic-bezier(.16,1,.3,1)"):
        """Fade (and optionally scale from `scale`, rise `rise` px) each object in; `stagger` frames between objects."""
        for i, name in enumerate(names):
            n = self.by_id[self.sid(name)]
            a = start + i * stagger
            first, last = {"opacity": 0}, {"opacity": 1}
            if scale != 1:
                first["scale"], last["scale"] = scale, 1
            if rise:
                y = n["style"]["y"]
                first["y"], last["y"] = y + rise, y
            n["keyframes"] = [{"at": a, "props": first, "ease": ease}, {"at": a + frames, "props": last}]
        return self

    def envelope(self, name, *, start, hold_end, end, fade=8):
        """Opacity in, hold, out: explicit frames from the object's start."""
        n = self.by_id[self.sid(name)]
        n["keyframes"] = [{"at": start, "props": {"opacity": 0}, "ease": "ease-out"},
                          {"at": start + fade, "props": {"opacity": 1}, "ease": "linear"},
                          {"at": hold_end, "props": {"opacity": 1}, "ease": "ease-in"},
                          {"at": end, "props": {"opacity": 0}}]
        return self

    def stagger(self, name, *, by="words", each="80ms", from_="start", keyframes=None):
        """GSAP-style stagger of a text's parts (target words, chars or lines). `keyframes` is the tween each part plays."""
        n = self.by_id[self.sid(name)]
        st = {"target": by, "each": each, "from": from_}
        if keyframes:
            st["keyframes"] = keyframes
        n["stagger"] = st
        return self

    # -- effects and paint (CSS terms; every reply states the carve status) ----------------------------------
    def blur(self, name, px=8):
        return self.set(name, "blur", px)

    def glow(self, name, *, radius=12, color="#ffcc00", strength=0.6, mix=0.2):
        return self.set(name, "glow", "%spx %s %s %s" % (radius, color, strength, mix))

    def shadow(self, name, *, x=0, y=8, blur=12, color="#00000066"):
        return self.set(name, "dropShadow", "%spx %spx %spx %s" % (x, y, blur, color))

    def soft_edge(self, name, px):
        """The visible 10-90 % ramp of a shape's edge, in px."""
        return self.set(name, "softEdge", px)

    def trim_path(self, name, *, start="0%", end="100%", offset="0%"):
        return self.set(name, "trimStart", start).set(name, "trimEnd", end).set(name, "trimOffset", offset)

    def paint(self, name, *, fill=None, stroke=None, stroke_width=None):
        for k, v in (("fill", fill), ("stroke", stroke), ("strokeWidth", stroke_width)):
            if v is not None:
                self.set(name, k, v)
        return self

    def transform(self, name, *, x=None, y=None, scale=None, rotate=None, opacity=None, origin=None):
        for k, v in (("x", x), ("y", y), ("scale", scale), ("rotate", rotate), ("opacity", opacity), ("transformOrigin", origin)):
            if v is not None:
                self.set(name, k, v)
        return self

    # -- the document ----------------------------------------------------------------------------------------
    def to_dict(self):
        return {"schema": "carvercat/2.0", "comp": dict(self.comp), "children": self.nodes}

    def dumps(self, **kw):
        return json.dumps(self.to_dict(), **kw)

    def apply(self, *, dry_run=False, mode="merge", preflight=None):
        """scene.apply. Returns the reply (or (reply, preflight) with preflight='resolve'|'aftereffects')."""
        out = self.client.apply_scene(self.to_dict(), mode=mode, dry_run=dry_run, preflight=preflight)
        reply = out[0] if isinstance(out, tuple) else out
        if not dry_run:
            self.ids = dict((reply.get("scene") or {}).get("ids", {}))
        return out

    # -- feedback with no render -----------------------------------------------------------------------------
    def measure(self, name):
        rows = self.client.measure([self.target(name)])["objects"]
        b = rows[0]["box"]
        return Box(b["x"], b["y"], b["width"], b["height"])

    def fit(self, name, box, *, minimum=20, maximum=400):
        """text.fit: the largest fontSize in [minimum, maximum] px whose text fits `box` (same shaper as the canvas)."""
        return self.client.run("text.fit", id=self.target(name), box={"width": box.w, "height": box.h},
                               min="%spx" % minimum, max="%spx" % maximum)

    def flow(self, names, *, axis="x", gap=24):
        """layout.stack: one after another along an axis, `gap` px apart, from the first object's place."""
        return self.client.run("layout.stack", ids=[self.target(n) for n in names], axis=axis, gap=gap)

    def align(self, names, mode="centerX", to="frame"):
        return self.client.run("layout.align", ids=[self.target(n) for n in names], mode=mode, to=to)

    def check_zones(self, names, *, within="safe"):
        """measure.overlaps with `within`: what sticks out of the frame or the safe area, and what overlaps."""
        r = self.client.run("measure.overlaps", ids=[self.target(n) for n in names], within=within)["readings"][0]
        if r.get("outside"):
            raise CarvercatError("outside the %s area: %s" % (within, json.dumps(r["outside"])))
        return r

    def contrast(self, fg, bg):
        return self.client.run("measure.contrast", fg=fg, bg=bg)["readings"][0]

    def review(self, path, *, frames=(0, 12, 45, 80)):
        """Lint (no render) then one look. Returns {'lint', 'look'}; read the image, do not just trust the flags."""
        lint = self.client.tool("carvercat_inspect", mode="lint")
        look = self.client.look(path, looks=[{"from": f, "to": f, "count": 1} for f in frames])
        return {"lint": lint, "look": look}

    def component(self, name):
        """A namespace: the scene ids of its children are `<name>-<child>`, so applying again updates the same objects."""
        return Component(self, name)


class Component:
    """Scene objects under one prefix. Repeating it with the same child names updates, never duplicates."""

    def __init__(self, scene, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("a component needs a name")
        self.scene, self.prefix = scene, _slug(name) + "-"

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def _n(self, child):
        return self.prefix + child

    def rectangle(self, child, box, **kw):
        return self.scene.rectangle(self._n(child), box, **kw)

    def text(self, child, content, **kw):
        return self.scene.text(self._n(child), content, **kw)


def title_pair(scene, title, subtitle, *, box, start=None, duration=None, accent="#F0BD35"):
    scene.text("title", title, box=Box(box.x, box.y, box.w, box.h * 0.6), size=76, weight=700, color=accent, start=start, duration=duration)
    scene.text("subtitle", subtitle, box=Box(box.x, box.y + box.h * 0.62, box.w, box.h * 0.38), size=36, start=start, duration=duration)
    return scene


def number_highlight(scene, name, number, label, *, box, start=None, duration=None):
    scene.rectangle(name + " plate", box, start=start, duration=duration)
    scene.text(name + " number", number, box=Box(box.x, box.y, box.w, box.h * 0.6), size=68, weight=700, align="center", start=start, duration=duration)
    scene.text(name + " label", label, box=Box(box.x, box.y + box.h * 0.6, box.w, box.h * 0.4), size=36, align="center", start=start, duration=duration)
    return scene


def caption(scene, name, content, *, box, start=None, duration=None, direction="auto", background=True):
    if background:
        scene.rectangle(name + " plate", box, start=start, duration=duration, alpha=0.7, fill="#0B0B0F")
    fam, wt = ("Almarai", 800) if direction == "rtl" else (None, 400)
    scene.text(name, content, box=box.inset(min(24, box.h / 4)), size=48, family=fam, weight=wt, align="center",
               start=start, duration=duration)
    return scene


def card_group(scene, name, title, label, *, box, start=None, duration=None):
    scene.rectangle(name + " card", box, start=start, duration=duration, radius=24)
    scene.text(name + " title", title, box=Box(box.x, box.y + box.h * 0.12, box.w, box.h * 0.4), size=52, weight=700, align="center", start=start, duration=duration)
    scene.text(name + " label", label, box=Box(box.x, box.y + box.h * 0.58, box.w, box.h * 0.3), size=30, align="center", start=start, duration=duration)
    return scene


def icon_label(scene, icon_name, label_name, label, *, box, start=None, duration=None):
    """A label beside an icon that already exists in the comp (the icon is not touched)."""
    scene.text(label_name, label, box=box, size=36, start=start, duration=duration)
    return scene
