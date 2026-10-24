"""Turn one comp of a saved .carverproj into a Carvercat .carvertemplate
(templateVersion 2, the same shape the bundled carvercat-essentials pack uses).

    python comp_to_template.py PROJECT.carverproj "Comp name" OUT.carvertemplate \
        --id cc.mp.tr_two_tone_wipe --name "Two-tone wipe" --tags transition,wipe \
        --note "..." [--drop "Background"] [--prefix tt_]

* Build and LOOK at the pattern in Carvercat first (carvercat_batch / carvercat_look),
  save the project (edit.save {path}), then run this.
* --drop removes clips by label/text (e.g. a stand-in background) so the template is
  an overlay that lands on whatever is underneath.
* Clip ids are rewritten with --prefix so two templates applied to one comp never
  share ids (shared ids are the performance trap in references/app/performance.md).
"""
import argparse, json, re, copy


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project"); ap.add_argument("comp"); ap.add_argument("out")
    ap.add_argument("--id", required=True); ap.add_argument("--name", required=True)
    ap.add_argument("--tags", default=""); ap.add_argument("--note", default="")
    ap.add_argument("--category", default="scene")
    ap.add_argument("--drop", action="append", default=[])
    ap.add_argument("--prefix", default="tpl_")
    ap.add_argument("--fonts", default="")
    a = ap.parse_args()

    proj = json.load(open(a.project, encoding="utf-8"))
    tl = next((t for t in proj["timelines"] if t.get("name") == a.comp or t.get("id") == a.comp), None)
    if tl is None:
        raise SystemExit(f"no comp named {a.comp!r}; have {[t.get('name') for t in proj['timelines']]}")
    scene = copy.deepcopy(tl["scene"])
    for tr in scene["tracks"]:
        tr["clips"] = [c for c in tr["clips"] if (c.get("label") or c.get("text")) not in a.drop]
    scene["tracks"] = [t for t in scene["tracks"] if t["clips"]]
    text = json.dumps(scene)
    text = re.sub(r"\bclip_(\d+)\b", lambda m: a.prefix + m.group(1), text)
    scene = json.loads(text)
    w, h = int(scene.get("width", 1920)), int(scene.get("height", 1080))
    fps = scene.get("sceneFps", 30)
    from math import gcd
    g = gcd(w, h)
    tpl = {
        "templateVersion": 2, "id": a.id, "name": a.name, "category": a.category, "apply": "scene",
        "tags": [t for t in a.tags.split(",") if t] + ["motion patterns"], "note": a.note,
        "frame": {"width": w, "height": h, "fps": fps}, "scene": scene,
        "authoredAspect": [w // g, h // g], "authoredFps": fps, "resolutionPolicy": "on_apply",
        "fit": "contain", "anchor": [0.5, 0.5], "authoredResolution": [w, h],
        "requiredFonts": [f for f in a.fonts.split(",") if f],
    }
    json.dump(tpl, open(a.out, "w", encoding="utf-8"), indent=1)
    n = sum(len(t["clips"]) for t in scene["tracks"])
    print(f"{a.out}: {n} objects, {w}x{h}@{fps}, {scene.get('duration')} frames")


if __name__ == "__main__":
    main()
