# Converting a pack to design units (recipe)

For one pack of `library/templates/<pack>/` (the Transitions pack is the worked example). Everything runs against a headless
host with fresh preferences, data and cache folders; never an open app. Set once:

```
export CARVERCAT_HOST=/path/to/carvercat-host
export CARVERCAT_RESOURCE_ROOT=/path/to/the-app-resource-folder       # fonts and the parameter registry
```

Work on a branch of your own checkout. No publishing, no credentials.

## 1. Convert the lab (and showcase)

`<pack>_lab*.py` and `<pack>_showcase.py` become design-unit scripts built on `json_author/cc2.py` (`Doc` > `Comp` > `Obj`,
sent with `Doc.send(client, path)` = `scene.apply` per comp, then `edit.save`). Each lab module exposes `build() -> Doc`.

Units: px from the top-left, y down; degrees CLOCKWISE; frames; `'#RRGGBB'`; CSS easing; font size in px.
Convert the old kit's numbers, do not copy them:

- **Rotation**: the old kit stored counter-clockwise values; negate them (the first Transitions conversion mirrored a wipe).
- **Colours**: write the hex the page states; the old kit's linear curve is gone.
- **Position keys** are the centre of the object (`pos`), the builder turns them into box x/y.
- Features: `Comp.path` + `bezier(points)`, `Comp.null` + `Obj.child` (parenting), `Comp.nest` (precomp, placed with
  `comp.place`; `track='top'` puts instances on one track above the rest), `Obj.stagger` (text; its tween is `keyframes` here or
  the object's own keys, never both), per-property text keys (`tracking`, `size`, `leading`, `colour`), `Comp.mask`, `mblur`.
- **v1 corrections are `Doc` options, not local patches** (`json_author/cc2.py`): `Doc(v1_look=True)` = `legacy_ease` (the names 'Ease in',
  'Ease out', 'S-curve' mean the app model's curves `OLD_EASE`, or name them outright `'v1-ease-out'`) + `cap_radius` (a corner radius is
  capped at a quarter of the short side, how v1 drew a pill) + `unparent_masks` (the window is let go of the content it cuts: `parent.clear`,
  also for path and text content). Separate: `path_boxes` (a path's box and `base` are its true bounding box, `path_box(d)`, so `pos` keys are
  its centre), `fix_star_names` (0.1.8 app bug), `client_timeout`.
- Helpers: `Obj.hard_shadow(col, dx)` (dy = dx x 9/16, v1's shadow), `Comp.text_at(...)` (x is the left/centre/right edge, y the centre of the
  block, a v1 tracking factor and a line-height multiple), `Obj.tracking_factor(spec)`, `Obj.gradient_keys(spec)` (shape gradient endpoints,
  keyed with `key.set`), `Comp.nest_keys(child, f0, scale=..., trim_in=...)` (keys on a nested instance, found by kind, name and start).
- Two keys of the same frame with different eases are keyed after the apply (`anim.set`), handled in `Doc.send`.
- Preset builders (`.carverpreset`) stay in the stored preset format; they are verified by loading the presets, not rewritten.

## 2. Regenerate

```
python3 regen_pack.py <lab_module> --pack <pack>                       # rewrites library/templates/<pack>/*.carvertemplate
python3 regen_pack.py <lab_module> --pack <pack> --no-templates --keep ../../../categories/<cat>/<name>/project.carverproj
```

`python3 regen_all.py --out DIR` runs every pack (labs 1-3, showcase, showcase-2) one job at a time and writes `<job>.done` marker files;
wait on them with `wait_for.py` (never `pgrep -f`, it matches itself); `run_job.py` starts any long harness command the same way.
`regen_templates` keeps null objects, matches the lab comp by the file stem (else by the template's display name) and warns on stderr, loudly,
when a lab comp looks like a renamed template comp it did not use (`--strict` makes that fatal). A second run must leave `git status` unchanged (the chain is deterministic). Templates are written as `carvercat/2`
(`minApp` 0.1.8); ids, names, tags, notes and fonts are kept. Delete any `project.carverproj.v1.bak` the app leaves next to a
saved project (the old file is in git).

## 3. Verify

```
python3 verify_pack.py <pack> --out /tmp/verify-<pack> [--lab <lab_module> --recipes "Comp A,Comp B"] [--timeout 900] [--ink-templates "Title A"]
```

`verify_pack.py` carries the former `verify_pack_wrap.py` corrections (see its HARNESS CORRECTIONS): objects whose clip has not started are
not measured, the v1 and v2 ink masks share one background colour, `--ink-templates` measures text boxes from the rendered ink (evidence for
one template whose pixels are proven equal, to be named in the report), `--timeout` raises the client timeout. `verify_pack_wrap.py` is a shim.

Writes `verify_<pack>.json` and `.md`. For every template it:

1. places it in a fresh 16:9 and a fresh 9:16 comp, runs lint and qc (expect 0/0/0 and no flashes);
2. compares it with its v1 original from git history (the newest committed version that is not `carvercat/2`; `--v1-ref` picks
   another) at N frames on a magenta underlay: `shape` (silhouette, passes at 2 % or less), `colour` (reported);
3. **object-level check (mandatory)**: opens the placed template's inner comp and, at each compared frame, matches every v1 object
   to a v2 object (type + name, then order) with `measure.boxes`. Text objects must have the same text, ink where v1 has ink (per-box
   pixel diff of the ink area, `inkIoU`) and the same drawn box (ink box) within 16 px; other objects the same box within 16 px.
   A missing, empty, moved or text-different object is a **FAIL whatever the pixel score** (columns: objects, missing, empty,
   box offset max px, worst ink IoU; detail under "Object-level FAILS", exit code 1). Templates with text are pixel-compared at
   960x540 instead of 320x180. The shape metric alone passed a template whose headline was missing (0.75-1.8 %);
4. measures the cover window, cut, settle and gone frames (definitions in the file's docstring: covered = the frame reads the
   same over a magenta and a green underlay), and, with `--lab`, lint and the change window of recipe comps.

A pack is not verified until every template passes the object check **and** you have looked at montages of its frames yourself (the
object check does not see colour, easing feel, clipping by a mask, or an object drawn in the wrong order; eyeball a montage per
template, text templates especially). `--pack-dir` checks a scratch copy and `--repo` another worktree, e.g. to prove a deliberately
broken copy FAILs.

Look at the frames it keeps in `--out` when a compare fails: the usual causes are a rotation sign, an ease that changed, or a
unit (a 1000 px shape scaled, KI-137). Fix the lab, regenerate, run again.

## 4. Restamp the pages

For every page of the pack under `ai/patterns/`: "verified <displayVersion> (rev <packageRevision>, <commit>)" from the report's
`build`, the measured windows from the report (one definition, say which), lint counts. A number the report does not
back is removed or re-measured, not carried over.

## 5. Checks, then commit

```
python3 ai/scripts/verify_examples.py --exe $CARVERCAT_HOST
python3 ai/scripts/motion/recipes/verify_recipes.py                # both routes
python3 ai/scripts/test_cc_toolkit.py                              # CARVERCAT_EXE=$CARVERCAT_HOST for the live tests
python3 wiki/tools/verify_keyed_pages.py --exe $CARVERCAT_HOST
python3 wiki/tools/wiki_index.py
python3 tools/check_links.py        # from the repository root
node tools/build_index.mjs && node tools/build_index.mjs --check
```

Commit in steps (kit changes, regenerated templates and projects, pages), push the branch, do not merge.
