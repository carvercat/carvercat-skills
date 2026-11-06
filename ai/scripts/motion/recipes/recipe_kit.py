"""Build a recipe sample: a master comp with a background, then Library templates placed at frames on tracks
above it (library.place + template.apply, optional slow pushes on long holds), then lint, timing, qc, a look,
and save. Everything is in design units: px from the top-left with y down, CSS colours, frames, CSS easing.

Two routes make the master; the rest is the same:
    RECIPE_ROUTE=file   (default) write a project file in the stored format carvercat/2 (cc_project.py), then
                        edit.open {path, force: true}. The default rule (edit the project file) holds.
    RECIPE_ROUTE=apply  send the background as one scene.apply document into a fresh project: the shorter route
                        for a master this small. edit.save then writes the same carvercat/2 file.

Run headless only, with isolated folders (never --connect):
    CARVERCAT_EXE=/path/to/carvercat-host            a build whose Library (or the installed packs) has the templates
    CARVERCAT_RESOURCE_ROOT=<the app resource folder> the host's resource folder (fonts, parameter registry)
    CARVERCAT_STATE=/path/to/isolated/state          fresh preferences, data and cache folders go in here
    RECIPE_LAB=/path/to/work/dir                     where the project files and looks are written
    python rc_saas.py
The packs the recipes use are in `library/templates/` of the skills repo; `install_packs` copies them into the
user Library folder (`library.folder`) and runs `library.reload`. Docs: ai/recipes/README.md.
"""
import os, sys, json, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from cc_client import Client
from cc_project import Project
from cc_scene import Scene, Box, gradient

EXE, STATE = os.environ.get("CARVERCAT_EXE", ""), os.environ.get("CARVERCAT_STATE", "")
LAB = S = os.environ.get("RECIPE_LAB", os.getcwd())
MASTER = {}          # the last master author() was asked for: the apply route rebuilds it in place of the file
ROUTE = os.environ.get("RECIPE_ROUTE", "file")
PACKS = os.environ.get("RECIPE_PACKS", os.path.join(HERE, "..", "..", "..", "..", "library", "templates"))
os.makedirs(os.path.join(S, "work"), exist_ok=True)


def client():
    os.chdir(LAB)
    return Client.stdio(EXE, STATE, resource_root=os.environ.get("CARVERCAT_RESOURCE_ROOT"))


def install_packs(c, packs=None):
    """Copy every pack folder of the skills repo's library/templates/ into the user Library and rescan."""
    folder = c.run("library.folder")["readings"][0]["path"]
    dest = os.path.join(folder, "templates")
    os.makedirs(dest, exist_ok=True)
    for name in sorted(os.listdir(packs or PACKS)):
        src = os.path.join(packs or PACKS, name)
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(dest, name), dirs_exist_ok=True)
    r = c.run("library.reload")
    return r["readings"][0].get("user", {}).get("issues", [])


def open_project(c, path):
    return c.run("edit.open", path=path, force=True)


def switch(c, name):
    cs = c.tool("carvercat_list")["comps"]
    for i, x in enumerate(cs):
        if x.get("name") == name:
            return c.run("comp.switch", index=x.get("index", i))
    raise RuntimeError(f"no comp {name}")


def lint_summary(res):
    return res.get("summary"), [(f.get("severity"), f.get("check"), (f.get("object") or {}).get("name"), f.get("measured")) for f in res.get("findings", [])]


def author(path, name, n, bg, w=1920, h=1080):
    """File route: write the master as a carvercat/2 project. `bg` is a hex colour ('#0B1F3A') or a pair of hex colours
    for a top-to-bottom gradient. `n` is the length in frames."""
    MASTER.update(bg=bg, w=w, h=h)
    p = Project(name)
    p.comp(name, width=w, height=h, fps=30, frames=n)
    p.rectangle("Background", fill=tuple(bg) if isinstance(bg, (list, tuple)) else bg)
    p.save(path)


def author_apply(c, name, n, bg, w=1920, h=1080):
    """Apply route: one scene.apply document into a fresh project (nothing on disk yet)."""
    c.run("edit.new", force=True)
    s = Scene(c, width=w, height=h, fps=30, duration=f"{n}f")
    fill = gradient([(0, bg[0]), (100, bg[1])], angle=180) if isinstance(bg, (list, tuple)) else bg
    s.rectangle("Background", Box(0, 0, w, h), fill=fill)
    s.apply()
    c.run("comp.rename", name=name, check=False)


def place_all(c, path, name, shots, tag, look_every=None, n=None):
    """Open (or build) the master, place every shot, report lint, timing and qc, write a contact sheet, save.
    A shot is (template, frame, track[, (from, to, amount)][, zoom])."""
    if ROUTE == "apply":
        author_apply(c, name, n, MASTER["bg"], MASTER["w"], MASTER["h"])
    else:
        open_project(c, path)
    issues = install_packs(c)
    other = [i for i in issues if not i.startswith("clash:")]    # a pack item named like a bundled one is skipped; the bundled one wins
    print("library:", len(issues) - len(other), "name clashes skipped", other or "")
    if ROUTE != "apply":
        switch(c, name)
    names = [i["name"] for i in c.tool("carvercat_run", command="library.list", args={})["readings"][0]["items"]]
    for shot in shots:
        t, f, tr = shot[:3]; push = shot[3] if len(shot) > 3 else None
        zoom = shot[4] if len(shot) > 4 else None    # scale the placed instance (e.g. a 16:9 template fitted into 9:16)
        assert names.count(t) == 1, (t, names.count(t))
        r = c.run("library.place", name=t, frame=f, track=tr)
        tid = r.get("touched", [None])[0]
        r2 = c.run("template.apply", id=tid)
        print("placed", t, "at", f, "track", tr, "->", r2.get("why"))
        # `scale` is absolute: template.apply fits a 16:9 template into a 9:16 comp at scale 0.5625 (width 1080 of 1920),
        # so a zoom of 2.4 on content means scale = 0.5625 x 2.4
        fit = float(c.get(tid, "scale")["value"]) if zoom else 1.0
        if zoom and not push:
            r5 = c.run("property.set", id=tid, key="scale", value=fit * float(zoom))
            print("   zoom", zoom, r5.get("why"))
        if push:                                   # (from, to, amount): a slow linear push so long holds never freeze
            a, b, amt = push
            z0 = fit * float(zoom) if zoom else 1.0      # a zoomed instance pushes from its zoom; it is never still, so a frame
            # `atComp` is the comp's own frame; `ease` shapes the segment that LEAVES the key (CSS meaning), and a key with
            # nothing after it keeps no ease. So key the END first, then the start with ease linear: set in the other
            # order, the start's ease is dropped, the push eases out and lint flags the last frames (cropped_at_rest).
            r4 = c.run("key.set", id=tid, key="scale", value=z0 * (1.0 + amt), atComp=b, ease="linear")
            r3 = c.run("key.set", id=tid, key="scale", value=z0, atComp=a, ease="linear")
            print("   push", r3.get("why"), "|", r4.get("why"))
    lint = c.tool("carvercat_inspect", mode="lint")
    print("LINT", lint_summary(lint))
    tm = c.tool("carvercat_inspect", mode="timing")
    for o in tm["objects"]: print("  ", o["name"], o["enters"], o["exits"])
    q = c.tool("carvercat_inspect", mode="qc", width=240)
    print("QC", [x for x in q.get("findings", []) if x.get("check") not in ("black",)])
    if n:
        c.look(S + f"/work/{tag}_sheet.png", **{"from": 0, "to": n - 1, "count": 24, "cols": 6, "max_edge": 1800})
    c.run("edit.save", path=path)
