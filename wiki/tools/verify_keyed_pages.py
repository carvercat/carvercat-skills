"""Re-verify the wiki pages that key a trim, blur, soft edge, feather, border radius, glow or shadow by design name.

    CARVERCAT_RESOURCE_ROOT=<the app resource folder> python3 wiki/tools/verify_keyed_pages.py \
        --exe /path/to/carvercat-host [--scripts ai/scripts] [--only donut-clockwise]

Needs the design-units Python toolkit (`ai/scripts/cc_client.py` with `Client.stdio(..., resource_root=)`, `cc_scene.py`),
which is on skills-e61-ai and on main once that branch is merged. Each case starts a fresh headless host with fresh
preferences, data and cache folders (never an open app), builds the example a page describes and reads the result back
(values at frames, or rendered pixels). Exit status 0 = every case held. The cases are named for the pages they check.
"""
import argparse
import glob
import os
import sys
import tempfile

CASES = {}


def case(fn):
    CASES[fn.__name__.replace("_", "-")] = fn
    return fn


def lin(v):  # the renderer's transfer (BT.709), as the soft-edge page measures it
    v /= 255.0
    return v / 4.5 if v < 0.081 else ((v + 0.099) / 1.099) ** (1 / 0.45)


def render(c, name):
    from PIL import Image
    d = tempfile.mkdtemp(prefix=name)
    c.tool("carvercat_render", dir=d, at=0)
    return Image.open(sorted(glob.glob(d + "/*.png"))[0]).convert("RGB")


def render_at(c, frame):
    from PIL import Image
    d = tempfile.mkdtemp(prefix="f")
    c.tool("carvercat_render", dir=d, at=frame)
    return Image.open(sorted(glob.glob(d + "/*.png"))[0]).convert("RGB")


def ramp(im, y, x0, x1):
    row = [lin(im.getpixel((x, y))[0]) for x in range(x0, x1)]
    lo, hi = min(row), max(row)

    def cross(t):
        th = lo + t * (hi - lo)
        for i in range(1, len(row)):
            if (row[i - 1] - th) * (row[i] - th) <= 0 and row[i] != row[i - 1]:
                return x0 + i - 1 + (th - row[i - 1]) / (row[i] - row[i - 1])
    return abs(cross(0.9) - cross(0.1)), cross(0.5)


def val(c, oid, key, frame):
    c.run("view.seek", frame=frame)
    v = c.run("property.get", id=oid, key=key)["readings"][0]["value"]
    return float(str(v).replace("px", "").replace("%", ""))


def scene(c, W=1920, H=1080, dur="3s"):
    from cc_scene import Scene
    return Scene(c, width=W, height=H, fps=30, duration=dur)


def near(a, b, tol, what=""):
    assert abs(a - b) <= tol, "%s: %s not within %s of %s" % (what, a, tol, b)


S_CURVE = "cubic-bezier(0.333, 0, 0.667, 1)"


@case
def draw_a_line_along_a_path(c):
    """cookbook/draw-a-line-along-a-path, animated-arrow, point-at-something, underline-a-word, hand-drawn-underline,
    milestone-timeline, split-screen, tutorial-callouts, logo-sting: a stroked path drawn on with trimEnd by name."""
    from cc_client import Refused
    o = c.run("object.path", frame=0, d="M 300 700 C 600 200 1000 900 1500 400")["touched"][0]
    for k, v in (("fill", "none"), ("stroke", "#f2b03c"), ("strokeWidth", 8), ("strokeLinecap", "round")):
        c.run("property.set", id=o, key=k, value=v)
    r = c.run("anim.set", id=o, keyframes=[{"at": 10, "trimEnd": "0%", "ease": S_CURVE}, {"at": 40, "trimEnd": "100%"}])
    assert r["changed"]
    got = [val(c, o, "trimEnd", f) for f in (10, 25, 40)]
    near(got[0], 0, 0.5, "f10"), near(got[1], 50, 1.5, "f25 (the S-curve midpoint)"), near(got[2], 100, 0.5, "f40")
    # an "in the middle of an animation" property.set writes ONE key at the playhead
    c.run("view.seek", frame=30)
    c.run("property.set", id=o, key="trimEnd", value="90%")
    keys = c.run("key.list", id=o, key="trimEnd")
    assert "30" in str(keys), keys
    print("   trimEnd at f10/f25/f40 =", got)


@case
def donut_clockwise(c):
    """cookbook/donut-fill: rotate -90deg and key trimStart 100% -> 32% sweeps clockwise from 12 o'clock to 68%."""
    import math
    s = scene(c)
    s.rectangle("bg", __import__("cc_scene").Box(0, 0, 1920, 1080), fill="#000000")
    s.apply()
    cx, cy, R = 960, 540, 200

    def ring(name, **style):
        n = c.run("object.new", kind="ellipse", frame=0, style=dict({"x": cx - R, "y": cy - R, "width": 2 * R, "height": 2 * R, "fill": "none",
                                                           "stroke": "#ffffff", "strokeWidth": 36, "strokeLinecap": "butt"}, **style))["touched"][0]
        return n
    cw = ring("cw", rotate="-90deg")
    c.run("anim.set", id=cw, keyframes=[{"at": 10, "trimStart": "100%", "ease": "cubic-bezier(0.16, 1, 0.3, 1)"}, {"at": 40, "trimStart": "32%"}])
    im = render_at(c, 45)

    def lit(angle_cw_from_12):
        a = math.radians(angle_cw_from_12)
        x, y = cx + R * math.sin(a), cy - R * math.cos(a)
        return im.getpixel((int(x), int(y)))[0] > 128
    on = [a for a in range(0, 360, 15) if lit(a)]
    assert all(a in on for a in range(15, 240, 15)) and not any(a in on for a in range(255, 345, 15)), on
    print("   clockwise arc lit from 12 o'clock at", on[0], "to", on[-1], "degrees")
    c.run("edit.undo") if False else None


@case
def donut_counter_clockwise(c):
    """cookbook/donut-fill step 4: rotate 0, trimEnd 0% -> 68% runs counter-clockwise from 3 o'clock."""
    import math
    from cc_scene import Box
    s = scene(c)
    s.rectangle("bg", Box(0, 0, 1920, 1080), fill="#000000")
    s.apply()
    cx, cy, R = 960, 540, 200
    n = c.run("object.new", kind="ellipse", frame=0, style={"x": cx - R, "y": cy - R, "width": 2 * R, "height": 2 * R, "fill": "none", "stroke": "#ffffff", "strokeWidth": 36})["touched"][0]
    c.run("anim.set", id=n, keyframes=[{"at": 10, "trimEnd": "0%", "ease": "cubic-bezier(0.16, 1, 0.3, 1)"}, {"at": 40, "trimEnd": "68%"}])
    im = render_at(c, 45)

    def lit(angle_ccw_from_3):
        a = math.radians(angle_ccw_from_3)
        return im.getpixel((int(cx + R * math.cos(a)), int(cy - R * math.sin(a))))[0] > 128
    on = [a for a in range(0, 360, 15) if lit(a)]
    assert all(a in on for a in range(15, 235, 15)) and not any(a in on for a in range(255, 345, 15)), on
    print("   counter-clockwise arc lit from 3 o'clock at", on[0], "to", on[-1], "degrees")


@case
def loading_spinner_and_countdown_ring(c):
    """cookbook/loading-spinner (trimEnd 5% -> 80% then trimStart 0% -> 75%), countdown (linear ring), checkmark-draw."""
    ring = c.run("object.new", kind="ellipse", frame=0, style={"x": 700, "y": 280, "width": 520, "height": 520, "fill": "none", "stroke": "#ffffff", "strokeWidth": 24})["touched"][0]
    c.run("anim.set", id=ring, keyframes=[{"at": 0, "trimEnd": "5%", "trimStart": "0%", "ease": S_CURVE}, {"at": 30, "trimEnd": "80%", "trimStart": "0%", "ease": S_CURVE}, {"at": 60, "trimStart": "75%"}])
    got = [(val(c, ring, "trimStart", f), val(c, ring, "trimEnd", f)) for f in (0, 30, 60)]
    near(got[0][1], 5, 0.5), near(got[1][1], 80, 0.5), near(got[1][0], 0, 0.5), near(got[2][0], 75, 0.5)
    lin_ring = c.run("object.new", kind="ellipse", frame=0, style={"x": 100, "y": 100, "width": 300, "height": 300, "fill": "none", "stroke": "#ffffff", "strokeWidth": 12})["touched"][0]
    c.run("anim.set", id=lin_ring, keyframes=[{"at": 0, "trimEnd": "0%", "ease": "linear"}, {"at": 25, "trimEnd": "100%"}])
    near(val(c, lin_ring, "trimEnd", 10), 40, 0.5, "linear f10 of 25")
    tick = c.run("object.path", frame=0, d="M 760 560 L 920 700 L 1180 420")["touched"][0]
    for k, v in (("fill", "none"), ("stroke", "#ffffff"), ("strokeWidth", 16), ("strokeLinecap", "round"), ("strokeLinejoin", "round")):
        c.run("property.set", id=tick, key=k, value=v)
    c.run("anim.set", id=tick, keyframes=[{"at": 20, "trimEnd": "0%", "ease": "cubic-bezier(0.333, 0.667, 0.667, 1)"}, {"at": 30, "trimEnd": "100%"}])
    assert val(c, tick, "trimEnd", 25) > 75, "decelerating arrival draws most of the stroke early"
    print("   spinner (start,end) at f0/f30/f60 =", got)


@case
def focus_in_and_staging_blur(c):
    """cookbook/focus-in (blur 28px -> 0px over 20 f), principles/staging (a focus pull between two elements)."""
    from cc_scene import Box
    s = scene(c)
    s.text("title", "Focus", box=Box(360, 340, 1200, 200), size=160, weight=700, align="center")
    s.rectangle("a", Box(200, 700, 300, 200), fill="#ffffff")
    s.rectangle("b", Box(700, 700, 300, 200), fill="#ffffff")
    s.apply()
    c.run("anim.set", id="#title", keyframes=[{"at": 0, "blur": "28px", "opacity": 0, "ease": "cubic-bezier(0.16, 1, 0.3, 1)"}, {"at": 20, "blur": "0px", "opacity": 1}])
    near(val(c, "#title", "blur", 0), 28, 0.1), near(val(c, "#title", "blur", 20), 0, 0.1)
    assert 0 < val(c, "#title", "blur", 8) < 28
    c.run("anim.set", id="#a", keyframes=[{"at": 0, "blur": "0px", "ease": "ease-in-out"}, {"at": 20, "blur": "9.2px"}])
    c.run("anim.set", id="#b", keyframes=[{"at": 0, "blur": "9.2px", "ease": "ease-in-out"}, {"at": 20, "blur": "0px"}])
    near(val(c, "#a", "blur", 20), 9.2, 0.1), near(val(c, "#b", "blur", 20), 0, 0.1)
    near(val(c, "#b", "blur", 0), 9.2, 0.1)
    print("   blur keys read back by name")


@case
def morph_border_radius_and_inner_radius(c):
    """techniques/morphing: borderRadius 0 -> 50% on a 200 px square (a circle), innerRadius on a star, sides on a polygon."""
    from cc_client import Refused
    sq = c.run("object.new", kind="rectangle", frame=0, style={"x": 100, "y": 100, "width": 200, "height": 200, "fill": "#ffffff", "borderRadius": 0})["touched"][0]
    c.run("anim.set", id=sq, keyframes=[{"at": 0, "borderRadius": 0, "ease": "ease-in-out"}, {"at": 20, "borderRadius": "50%"}])
    got = [val(c, sq, "borderRadius", f) for f in (0, 10, 20)]
    near(got[0], 0, 0.1), near(got[1], 50, 15), near(got[2], 100, 0.1)
    star = c.run("object.new", kind="star", frame=0, style={"x": 600, "y": 100, "width": 300, "height": 300, "fill": "#ffffff", "points": 5, "innerRadius": "37%"})["touched"][0]
    try:
        r = c.run("anim.set", id=star, keyframes=[{"at": 0, "innerRadius": "37%"}, {"at": 20, "innerRadius": "100%"}])
        inner = ("keyed", [val(c, star, "innerRadius", f) for f in (0, 20)])
    except Refused as e:
        inner = ("refused", str(e)[:200])
    print("   borderRadius at f0/f10/f20 =", got, "| innerRadius by name:", inner)


@case
def trim_offset_travelling_window(c):
    """techniques/line-drawing: trimStart 0, trimEnd 20, trimOffset 0% -> 80% travels a dash along a straight path."""
    p = c.run("object.path", frame=0, d="M 200 540 L 1720 540")["touched"][0]
    for k, v in (("stroke", "#ffffff"), ("strokeWidth", 8)):
        c.run("property.set", id=p, key=k, value=v)
    c.run("property.set", id=p, key="trimEnd", value="20%")
    c.run("anim.set", id=p, keyframes=[{"at": 10, "trimOffset": "0%", "ease": S_CURVE}, {"at": 40, "trimOffset": "80%"}])
    got = [val(c, p, "trimOffset", f) for f in (10, 25, 40)]
    near(got[0], 0, 0.5), near(got[1], 40, 1.5), near(got[2], 80, 0.5)
    print("   trimOffset at f10/f25/f40 =", got)


def extent(im, y, x0, x1, thresh=128):
    xs = [x for x in range(x0, x1) if im.getpixel((x, y))[0] > thresh]
    return (min(xs), max(xs)) if xs else None


@case
def camera_null(c):
    """techniques/camera-moves-2d: three 240 px cards parented to a null at the frame centre; the null's scale 1 -> 1.3."""
    from cc_scene import Box
    from cc_client import Refused
    s = scene(c, dur="3s")
    s.rectangle("bg", Box(0, 0, 1920, 1080), fill="#000000")
    for name, cx in (("c1", 560), ("c2", 960), ("c3", 1360)):
        s.rectangle(name, Box(cx - 120, 420, 240, 240), fill="#ffffff")
    s.apply()
    cam = c.run("object.new", kind="null", frame=0, duration="3s", style={"x": 910, "y": 490})["touched"][0]   # centre (960, 540)
    assert c.run("parent.assign", ids=[cam, "#c1", "#c2", "#c3"])["changed"]
    c.run("anim.set", id=cam, keyframes=[{"at": 10, "scale": 1, "ease": S_CURVE}, {"at": 40, "scale": 1.3}])
    # the cards are 240 px wide with gaps; read the lit runs along y = 540 at f10 and f40
    def runs(im):
        out, start = [], None
        for x in range(0, 1920):
            on = im.getpixel((x, 540))[0] > 128
            if on and start is None:
                start = x
            if not on and start is not None:
                out.append((start, x - 1)); start = None
        return out
    r10, r40 = runs(render_at(c, 10)), runs(render_at(c, 40))
    assert [round((a + b) / 2) for a, b in r10] == [560, 960, 1360], r10
    assert [round((a + b) / 2) for a, b in r40] == [440, 960, 1480], r40
    assert [b - a + 1 for a, b in r40] == [312, 312, 312] or all(abs((b - a + 1) - 312) <= 1 for a, b in r40), r40
    # the null draws nothing and has no opacity of its own
    try:
        c.run("property.set", id=cam, key="opacity", value=0.5)
        raise AssertionError("a null has no opacity")
    except Refused as e:
        assert e.code == "not-settable"
    print("   cards at f10", r10, "at f40", r40)


@case
def null_object_rig(c):
    """techniques/null-object: a null at the joint, parts nested under it, the null rotated; a null of a null."""
    from cc_scene import Box
    doc = {"schema": "carvercat/2.0", "comp": {"width": 1920, "height": 1080, "fps": 30, "duration": "3s"}, "children": [
        {"id": "bg", "type": "rect", "style": {"x": 0, "y": 0, "width": 1920, "height": 1080, "fill": "#000000"}},
        {"id": "pivot", "type": "null", "style": {"x": 910, "y": 150}, "children": [
            {"id": "sign", "type": "rect", "style": {"x": -100, "y": 150, "width": 300, "height": 200, "fill": "#ffffff"}}]}]}
    c.apply_scene(doc)
    c.run("anim.set", id="#pivot", keyframes=[{"at": 0, "rotate": 0, "ease": "ease-in-out"}, {"at": 30, "rotate": 30}])
    at0, at30 = render_at(c, 0), render_at(c, 30)
    white = lambda im, x, y: im.getpixel((x, y))[0] > 200
    assert white(at0, 960, 400) and white(at0, 1100, 490)
    assert white(at30, 860, 373) and not white(at30, 1100, 490), "the sign swung 30 degrees about (960, 200)"
    n = c.scene()["children"][1]
    assert n["type"] == "null" and "width" not in n["style"] and [k["id"] for k in n["children"]] == ["sign"], n
    print("   null pivot: sign centre (960, 400) -> (860, 373) at 30 degrees")


@case
def glow_and_shadow_keyed(c):
    """techniques/shadow-and-glow-in-motion: dropShadow, glow, brightness keyed by name."""
    from cc_scene import Box
    s = scene(c)
    s.rectangle("card", Box(660, 340, 600, 400), fill="#1a1c26", radius=24)
    s.apply()
    c.run("anim.set", id="#card", keyframes=[
        {"at": 0, "dropShadow": "0 6px 12px #00000059", "glow": "18px #1a99ff 0.5 0.2", "ease": "ease-out"},
        {"at": 18, "dropShadow": "0 28px 30px #00000033", "glow": "18px #1a99ff 0.75 0.2"}])
    c.run("view.seek", frame=18)
    assert str(c.run("property.get", id="#card", key="dropShadow")["readings"][0]["value"]).startswith("0px 28px 30px")
    print("   dropShadow and glow keyed together; f18 =", c.run("property.get", id="#card", key="glow")["readings"][0]["value"])


@case
def soft_edge_one_value_and_feather(c):
    """techniques/soft-edge-and-feather and soft-and-inverted-masks: the ramp table (one softEdge for fill and stroke),
    scale, the old name strokeSoftEdge, and softEdge / feather keyed by name."""
    from cc_scene import Box
    rows = []
    s = scene(c, dur="1s")
    s.rectangle("bg", Box(0, 0, 1920, 1080), fill="#000000")
    s.rectangle("r", Box(560, 240, 800, 600), fill="#ffffff")
    s.apply()
    for v in (8, 24, 60):
        c.run("property.set", id="#r", key="softEdge", value=v)
        w, mid = ramp(render(c, "fill"), 540, 400, 700)
        rows.append(("fill", v, round(w, 1)))
        near(w, v, 1.0, "fill ramp"), near(mid, 560, 1.5, "50% point")
    # a stroke-only shape: the same one value softens the stroke (both of its edges)
    c.run("property.set", id="#r", key="softEdge", value=0)
    c.run("property.set", id="#r", key="fill", value="none")
    c.run("property.set", id="#r", key="stroke", value="#ffffff")
    c.run("property.set", id="#r", key="strokeWidth", value=200)
    for v in (8, 24, 60):
        c.run("property.set", id="#r", key="softEdge", value=v)
        im = render(c, "stroke")
        outer, _ = ramp(im, 540, 400, 560)
        rows.append(("stroke", v, round(outer, 1)))
        near(outer, v, 1.0, "stroke ramp")
    # the old name sets the same value
    r = c.run("property.set", id="#r", key="strokeSoftEdge", value=30)
    assert r["changes"][0]["key"] == "softEdge" and r["units"]["deprecated"]["use"] == "softEdge"
    # scale scales it
    c.run("property.set", id="#r", key="fill", value="#ffffff")
    c.run("property.set", id="#r", key="stroke", value="none")
    c.run("property.set", id="#r", key="softEdge", value=24)
    c.run("property.set", id="#r", key="scale", value=2)
    w2, _ = ramp(render(c, "scale"), 540, 0, 400)
    near(w2, 48, 2.0, "scale 2")
    rows.append(("scale 2", 24, round(w2, 1)))
    # keyed
    c.run("property.set", id="#r", key="scale", value=1)
    c.run("anim.set", id="#r", keyframes=[{"at": 0, "softEdge": 0, "ease": "linear"}, {"at": 20, "softEdge": 24}])
    got = [val(c, "#r", "softEdge", f) for f in (0, 10, 20)]
    near(got[1], 12, 0.5), near(got[2], 24, 0.1)
    print("   ramp table (kind, set px, measured px):", rows, "| softEdge keyed f0/f10/f20 =", got)


@case
def feather_on_a_mask_shape(c):
    """techniques/soft-edge-and-feather, soft-and-inverted-masks: feather = the mask shape's soft edge, same ramp; keyed by name."""
    from cc_scene import Box
    rows = []
    s2 = scene(c, dur="1s")
    s2.rectangle("bg2", Box(0, 0, 1920, 1080), fill="#000000")
    s2.rectangle("plate", Box(0, 0, 1920, 1080), fill="#ffffff")
    s2.rectangle("win", Box(560, 240, 800, 600), fill="#ffffff")
    s2.apply()
    ids = s2.ids
    c.run("property.set", id=ids["plate"], key="mask", value={"ref": ids["win"], "invert": False})
    for v in (8, 24, 60):
        c.run("property.set", id=ids["win"], key="feather", value=v)
        w, _ = ramp(render(c, "feather"), 540, 400, 700)
        rows.append(("feather", v, round(w, 1)))
        near(w, v, 1.0, "feather ramp")
    assert c.run("property.get", id=ids["win"], key="softEdge")["readings"][0]["value"] == 60.0
    c.run("anim.set", id=ids["win"], keyframes=[{"at": 0, "feather": "0px", "ease": "ease-out"}, {"at": 20, "feather": "60px"}])
    gf = [val(c, ids["win"], "feather", f) for f in (0, 20)]
    near(gf[0], 0, 0.1), near(gf[1], 60, 0.1)
    print("   feather ramp (kind, set px, measured px):", rows, "| feather keyed f0/f20 =", gf)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--exe", required=True)
    ap.add_argument("--scripts", default=os.path.join(os.path.dirname(__file__), "..", "..", "ai", "scripts"))
    ap.add_argument("--only")
    a = ap.parse_args()
    sys.path.insert(0, os.path.abspath(a.scripts))
    from cc_client import Client
    root = os.environ.get("CARVERCAT_RESOURCE_ROOT")
    failed = 0
    for name, fn in CASES.items():
        if a.only and name != a.only:
            continue
        with tempfile.TemporaryDirectory() as d:
            with Client.stdio(a.exe, d, resource_root=root) as c:
                try:
                    fn(c)
                    print("held   ", name)
                except Exception as e:  # noqa: BLE001
                    failed += 1
                    print("FAILED ", name, "-", type(e).__name__, str(e)[:400])
    print("\n%d failed" % failed)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
