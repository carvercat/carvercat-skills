"""Build every recipe sample headless on both routes and read the result back.

    CARVERCAT_EXE=/path/to/carvercat-host CARVERCAT_RESOURCE_ROOT=<the app resource folder> \
        python3 verify_recipes.py [--only rc_sports ...] [--work /scratch/dir]

For each `rc_*.py` builder (a fresh isolated host, fresh preferences, data and cache folders each time):
  1. run it on the file route (carvercat/2 master written by cc_project, `edit.open`) and on the apply route
     (one `scene.apply` into a fresh project);
  2. check the printed lint is 0 / 0 / 0 and that every shot of the shot list was placed;
  3. open the saved project in a new host, check it is `carvercat/2`, read it back with `scene.get`
     (comp size, length, the background fill, and every placed template at its frame), and check the two routes
     read back the same, and that the sample project the recipe page names (v1 shape, still opens) holds the same shots.
Exit status 0 = every recipe held on both routes.
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from cc_client import Client


def build(script, route, work):
    env = dict(os.environ, RECIPE_ROUTE=route, RECIPE_LAB=work, CARVERCAT_STATE=os.path.join(work, "state"))
    out = subprocess.run([sys.executable, script], env=env, cwd=work, capture_output=True, text=True, timeout=900)
    if out.returncode:
        raise AssertionError("builder failed:\n" + out.stdout[-1500:] + out.stderr[-1500:])
    return out.stdout


def read_back(path, work, v2=True):
    doc = json.load(open(path))
    if v2:
        assert doc.get("format") == "carvercat/2", "saved file is not carvercat/2: %r" % doc.get("format")
    with Client.stdio(os.environ["CARVERCAT_EXE"], os.path.join(work, "reader"), resource_root=os.environ.get("CARVERCAT_RESOURCE_ROOT")) as c:
        c.run("edit.open", path=path, force=True)
        return c.scene()


def shape(scene):
    kids = [(k["name"], k["start"], k["duration"]) for k in scene["children"]]
    return scene["comp"], sorted(kids)


def check(script, root):
    base = os.path.basename(script)[:-3]
    src = open(script).read()
    n = int(re.search(r"^N = (\d+)", src, re.M).group(1))
    vertical = "w=1080" in src
    reads = {}
    for route in ("file", "apply"):
        work = os.path.join(root, base, route)
        os.makedirs(work)
        stdout = build(script, route, work)
        assert "LINT ('0 error(s), 0 warning(s), 0 note(s)', [])" in stdout, "lint not clean:\n" + stdout[-800:]
        placed = re.findall(r"^placed (.+) at (\d+) track (\d+)", stdout, re.M)
        scene = read_back(os.path.join(work, base + ".carverproj"), work)
        comp = scene["comp"]
        assert (comp["width"], comp["height"], comp["fps"]) == ((1080, 1920, 30) if vertical else (1920, 1080, 30)), comp
        assert comp["duration"] == "%df" % n, comp
        names = [k["name"] for k in scene["children"]]
        assert names.count("Background") == 1 and len(names) == len(placed) + 1, names
        bg = next(k for k in scene["children"] if k["name"] == "Background")
        assert bg["start"] == "0f" and bg["duration"] == "%df" % n and (bg["style"]["width"], bg["style"]["height"]) == (comp["width"], comp["height"]), bg
        for t, f, _ in placed:
            assert any(k["name"] == t and k["start"] == "%sf" % f for k in scene["children"]), (t, f)
        reads[route] = shape(scene)
    assert reads["file"] == reads["apply"], "the routes read back differently"
    # the sample project the recipe page names (stored in the older v1 shape, which still opens) holds the same shots
    page = next(p for p in glob.glob(os.path.join(HERE, "..", "..", "..", "recipes", "*.md")) if "recipes/%s.py" % base in open(p).read())
    sample = re.search(r"Sample: `(categories/recipes/[\w-]+)`", open(page).read()).group(1)
    sample_path = os.path.join(HERE, "..", "..", "..", "..", sample, "project.carverproj")
    work = os.path.join(root, base, "sample")
    os.makedirs(work)
    s = read_back(sample_path, work, v2=False)
    want = sorted((k["name"], k["start"]) for k in scene["children"])
    assert sorted((k["name"], k["start"]) for k in s["children"]) == want, "the sample project differs from the builder's result"
    return "%d placed, %s, %d frames" % (len(placed), "1080x1920" if vertical else "1920x1080", n)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--work")
    a = ap.parse_args()
    for var in ("CARVERCAT_EXE",):
        if not os.environ.get(var):
            sys.exit("set CARVERCAT_EXE")
    root = a.work or tempfile.mkdtemp(prefix="recipes-")
    scripts = sorted(glob.glob(os.path.join(HERE, "rc_*.py")))
    if a.only:
        scripts = [s for s in scripts if os.path.basename(s)[:-3] in a.only]
    held = failed = 0
    for s in scripts:
        try:
            print("held    %s  %s" % (os.path.basename(s), check(s, root)), flush=True)
            held += 1
        except Exception as e:
            print("FAILED  %s  %s" % (os.path.basename(s), str(e)[:900]), flush=True)
            failed += 1
    print("\n%d held, %d failed" % (held, failed))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
