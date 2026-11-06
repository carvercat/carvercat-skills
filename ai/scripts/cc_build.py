"""Procedural builders in design units, for jobs that build object by object instead of with one scene document.

New work should prefer cc_scene (one `scene.apply`). These helpers keep the old names of the earlier cc_build and write
design keys through `object.new {style}`, `property.set` and `anim.set`: px from the top-left, y down, CSS colours and
easing, `fontSize` in px. They need a Client:

    from cc_client import Client
    import cc_build
    with Client.stdio(exe, state_dir) as c:
        cc_build.use(c)
        plate = cc_build.card(x=80, y=700, w=820, h=220, fill="#0A0F1F", radius=24)
        name = cc_build.text("Alex Morgan", x=190, y=719, w=620, h=110, size=96, weight=700)
        plate.anim([{"at": 0, "x": -460, "ease": "cubic-bezier(.16,1,.3,1)"}, {"at": 20, "x": 80}])

Renamed or removed: `lin`, `rgba` (no linear colour; pass CSS strings), `grad` (gradient strings from
cc_scene.gradient), `Obj.k/cat/idx/sel` (no capability keys, no selection to restore: every call names its object),
`clear` (never clear a user's document).
"""
from cc_scene import gradient  # noqa: F401  (a CSS gradient string builder)

_client = None


def use(client):
    global _client
    _client = client
    return client


def _c():
    if _client is None:
        raise RuntimeError("call cc_build.use(client) first")
    return _client


class Obj:
    def __init__(self, id):
        self.id = id

    def set(self, key, value):
        return _c().run("property.set", id=self.id, key=key, value=value)

    def key(self, key, at, value, ease=None):
        args = {"id": self.id, "key": key, "value": value, "at": at}
        if ease:
            args["ease"] = ease
        return _c().run("key.set", **args)

    def anim(self, keyframes=None, **tween):
        """anim.set: keyframes=[{at, <props>, ease}] or to/from/fromTo + duration/ease."""
        if keyframes is not None:
            tween["keyframes"] = keyframes
        return _c().run("anim.set", id=self.id, **tween)

    def sel(self):
        return self


def new(kind, x, y, w, h, start=0, duration=90, **style):
    """object.new with its design style in one call. kind: rectangle | ellipse | text."""
    # the keys a box depends on first (whiteSpace, font, size), then width and height, then x and y last
    r = _c().run("object.new", kind=kind, frame=start, duration=duration,
                 style=dict(style, width=w, height=h, x=x, y=y))
    return Obj(r["touched"][0])


def card(x, y, w, h, radius=24, fill="#0A0F1F", opacity=0.72, border=None, border_width=3, start=0, duration=90):
    style = dict(fill=fill, opacity=opacity, borderRadius=radius)
    if border:
        style.update(stroke=border, strokeWidth=border_width)
    return new("rectangle", x, y, w, h, start, duration, **style)


def text(content, x, y, w, h, size=64, family=None, weight=700, color="#FFFFFF", align="center", start=0, duration=90):
    style = dict(fontSize=size, fontWeight=weight, fill=color, textAlign=align, whiteSpace="normal")
    if family:  # omit for the app's bundled default; name an installed family otherwise
        style["fontFamily"] = family
    o = new("text", x, y, w, h, start, duration, **style)
    o.set("text", content)
    return o


def stagger_caption(content, x, y, w, h, size=72, each="80ms", start=0, duration=60):
    """A caption whose words arrive one after another: opacity and a 24 px rise per word."""
    o = text(content, x, y, w, h, size=size, start=start, duration=duration)
    o.anim(**{"from": {"opacity": 0, "y": "+=24px"}, "duration": "0.4s", "ease": "ease-out",
              "stagger": {"target": "words", "each": each}})
    return o
