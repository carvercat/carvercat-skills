"""A lower third, end to end, in a private headless Carvercat. Never touches the visible editor.

    CARVERCAT_RESOURCE_ROOT=<the app resource folder, only for a host not run from the app bundle> \
    python3 example_creative.py --exe /path/to/carvercat-host --output /tmp/e

It shows: one validated scene document (dry run first), a GSAP-style stagger, the no-render checks (measure, contrast,
overlaps, lint), carve.preflight before a send, one look, and a saved editable project. Exit status 0 means every step held.
"""
import argparse
from pathlib import Path

from cc_client import Client
from cc_scene import Box, Scene, gradient

p = argparse.ArgumentParser()
p.add_argument("--exe", required=True)
p.add_argument("--output", required=True)
a = p.parse_args()
out = Path(a.output).resolve()
out.mkdir(parents=True, exist_ok=True)

with Client.stdio(Path(a.exe).resolve(), out / "state") as c:
    s = Scene(c, width=1920, height=1080, fps=30, duration="4s")
    s.rectangle("bg", Box(0, 0, 1920, 1080), fill=gradient([(0, "#14141f"), (100, "#2a1f4a")], angle=180))
    s.rectangle("plate", Box(160, 760, 900, 200), fill="#1a1c26", radius=24)
    s.rectangle("accent", Box(160, 760, 16, 200), fill="#b6ee3b")
    s.text("name", "Alex Morgan", box=Box(210, 775, 820, 100), size=88, weight=700)
    s.text("role", "DESIGNER / DIRECTOR", box=Box(210, 880, 820, 60), size=34, color="#b6ee3b")
    s.keys("plate", "x", [(0, -900), (18, 160)], ease="cubic-bezier(.16,1,.3,1)")
    s.keys("accent", "x", [(0, -900), (18, 160)], ease="cubic-bezier(.16,1,.3,1)")
    s.stagger("name", by="words", each="100ms", keyframes=[{"at": 10, "props": {"opacity": 0, "y": 799}},
                                                          {"at": 26, "props": {"opacity": 1, "y": 775}, "ease": "ease-out"}])
    s.entrance(["role"], start=24, frames=12, scale=1)

    dry = s.apply(dry_run=True)
    assert dry["scene"]["validated"] and not dry["scene"]["applied"] and c.tool("carvercat_list")["objects"] == []
    reply, pre = s.apply(preflight="resolve")
    print("applied:", len(reply["changes"]), "changes; preflight resolve:", pre["summary"])

    box = s.measure("name")
    assert abs(box.w - 820) < 0.01 and abs(box.x - 210) < 0.01, box
    print("contrast name on plate: %.2f:1" % s.contrast("#ffffff", "#1a1c26")["ratio"])
    print("outside the safe area:", s.check_zones(["name", "role"], within="safe")["outside"])

    review = s.review(out / "look.png", frames=(0, 12, 30, 80))
    print("lint:", review["lint"]["summary"], "| look files:", review["look"]["files"])
    c.run("edit.save", path=str(out / "lower_third.carverproj"))
    print(out / "lower_third.carverproj")
