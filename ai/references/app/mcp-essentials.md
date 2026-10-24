# Driving Carvercat through MCP - essentials for any agent

Carvercat exposes an MCP server (enable it in the app: **File -> Connect to AI**).
Tool names as the server publishes them: `carvercat_run` (one command),
`carvercat_batch` (many commands as one undoable step), `carvercat_look` (render frames
to an image to SEE the work), `carvercat_render` (PNG frames to disk),
`carvercat_list` (objects, comps, tracks, bins), `carvercat_authoring` (live controls,
geometry, fonts), `carvercat_inspect` (timing, curves, lint), `carvercat_state`.
Your agent may prefix them (e.g. `mcp__carvercat__carvercat_run`). Command names below
are what goes in `carvercat_run {command, args}` or a batch step `{command, args, frame?, as?}`.
Written against Carvercat Dev 0.0.69-0.0.72; newer builds may differ - trust the live app.
**Machine-readable catalogue**: the app's agent schema, read through the `carvercat://` MCP resources (`resources/list`): `commands.json` every
command with arguments, `authoring.json` units/batching/validation, `workflows`,
`errors.json`. Read the relevant entry before using an unfamiliar command.

## Loop: build -> look -> fix
1. `carvercat_list` - know the comps, tracks and ids before touching anything.
2. Build with batches (<= 256 steps; `as` aliases; `$ref` reuse; per-step `frame`).
3. **Look** at entrance, hold and exit frames (`carvercat_look {from, to, count}`).
   Never report a scene done without looking at it.
3b. **Validate** layout natively: `carvercat_authoring {mode:"validate"}` with checks
   `bounds_inside` (an [x,y,w,h] px box - use it for title-safe and 9:16 safe areas),
   `no_overlap` (with explicit `allow` pairs), `font_exact` (no font substitution) and
   `path_nodes_coincident`. Measured from real glyph/shape geometry, read-only.
4. `edit.save` often. Name things (`clip.rename`) so the timeline reads.

## Units
| Thing | Unit |
|---|---|
| Position | normalised `[x/W, y/H]`, **y up** (0.5,0.5 = centre) |
| Rect width AND height, ellipse size, stroke width, corner radius | fraction of comp **width** |
| Text size | fraction of width; px = size x width x 0.597 |
| Path points (`object.path`) | normalised x/W, y/H **y down**; the object is recentred (reply gives `geometry_centre`) |
| Time | comp frames; JSON `left` = frame x `scene.ppf` (4) |
| Blur/glow sizes | effect units (blur default 10, max 100) |

**Short key names** (accepted by `property.set` / `key.set` and presets): `center` = `transform.placement.position`, `size` = uniform scale, `scaleX`/`scaleY`, `angle` = rotation, `blend` = opacity, `anchor`; `text` = the text content; caps like `text.font.size`, `shape.fill.color` resolve when the object has exactly one such entry. For effect parameters use the stored path from `param.list` (`fx.<entry>.<param>`) or a batch `{"$param":[alias,param]}`. Parameter ranges/defaults: [effects/PARAMETERS.md](../effects/PARAMETERS.md) (e.g. softEdge ≤ 0.2, blur size ≤ 100) — a value out of range refuses the whole batch.

## Commands worth knowing
- Create: `object.new {kind: text|rectangle|ellipse|adjustment, track, duration}`,
  `object.path {points, handles, closed, track, duration}`, `media.import {paths}`,
  `library.place {name, frame, track}`, `template.apply`, `preset.apply {name}`.
- Edit: `property.set {id, key, value}`, `key.set {id, key, value, easing}` (+ step
  `frame`), `key.remove`, `clip.move {id, frame, track}`, `clip.rename`, `edit.delete
  {ids}`, `edit.group {ids}`, `object.enter/exit` (not batchable), `track.add`.
- Effects: `effect.addable {id}` then `effect.add {id, cap: blur|glow|shadow|motionblur|trim|fill|stroke}`.
- Text stagger: `stagger.new`, `stagger.connect {param}`, `stagger.set {by: character|word, gap}`.
- Masks/parenting: `mask.make {ids:[target, mask]}` (also parents!), `parent.clear`.
- Layout: `authoring.place_bounds {id, box:[x,y,w,h], horizontal, vertical}` inside a
  batch places text by its measured glyph bounds; `align.apply {mode: left|hcenter|right|
  top|vcenter|bottom|distribute-h|distribute-v|space-h|space-v, to: selection|key|comp}`
  (0.0.72); `view.rulers`, `guide.add {axis, position}`, `guide.snap` (0.0.72).
- Audio: `media.import {paths, frame}`; level `media.audio.gain` (dB, keyframeable).
- Comps/bins: `comp.new`, `comp.switch {index}`, `comp.duplicate {comp}`,
  `comp.format {width,height}`, `comp.delete {index}`, `bin.new {name}`,
  `comp.move_to_bin {comps, bin}`, `bin.list`.
- File: `edit.save`, `edit.open {path, force}`.
- Export: `export.set {settings}` -> `export.run` (asynchronous: returns the durable job path in `why`; poll `export.status {job}`, never re-run; an `interrupted` job continues with `export.resume {job}`); cancel `deliver.cancel`. Settings/verification: [workflows/export-and-delivery.md](../workflows/export-and-delivery.md).
- Easing names: `Linear`, `Ease in`, `Ease out`, `S-curve`, `Hold`. **Any other name
  silently becomes Linear.** `key.set` easing is the curve ARRIVING at that key.
- **Exact curves over MCP (verified 0.0.72):** two `key.set` keys, then `key.handle {path,
  frame, side:"out"|"in", x, y, tied:false}` on each. (x1,y1) goes on the first key's out
  handle and (x2,y2) on the second key's in handle. This is a CSS cubic-bezier exactly; y up
  to 2.5 overshoots. See [../patterns/custom-curves.md](../../patterns/custom-curves.md).
  In the project file the same thing is `customEase`.
- Retiming keys: `key.box {id, start, end, to_start, to_end}` (document frames).

## Pitfalls that cost hours
- **Placement follows the live playhead** unless you say otherwise: give batch steps
  their own `frame` (0.0.71+ places the object there and restores the playhead) and
  `media.import` a `frame`. On older builds seek to 0 first and verify `left` afterwards.
- A `clip.move` to where the clip already is was a batch-aborting refusal up to 0.0.70;
  from 0.0.71 it is a harmless no-op.
- From 0.0.71 `edit.nudge`, `edit.duplicate`, `comp.duration` and `track.remove_empty`
  are batchable.
- **Higher track index draws on top**; `track.add` appends on top.
- **Groups**: keys on children need `object.enter`; `object.new` refuses inside an
  entered group (create at top level, move into the group in JSON). A group's position is
  an offset around 0.5; it scales about its bounds centre.
- **New blur = size 10**; **glow blend > 0 = haze**; rectangle `angle` doesn't rotate
  (use transform rotation); upscaling small paths with transform scale renders soft (rebuild
  at size).
- **Don't copy clips in the project JSON with their ids** (keys go inert). Clips built
  fresh from a template with new ids work (verified 0.0.72): whole films can be generated
  into the JSON, see [json-authoring.md](json-authoring.md).
- **`comp.duplicate` keeps clip ids** -> rename them ([performance.md](performance.md)).
- Moving an object's anchor keeps the picture in place from 0.0.72 (centre compensated).
  **The anchor is in HALF-SIZES of the object, y up**: `[-1,0]` = left edge, `[0,-1]` =
  bottom edge. Set it BEFORE positioning (`authoring.place_bounds`), then grow scaleX or
  scaleY from that edge.
- **`clip.move` is an overwrite edit**: moving onto a clip on the same track trims or
  deletes that clip, silently. Combined with `object.new` without a `track` (it picks "a
  track with room" at the PLAYHEAD), a series of object.new + clip.move calls can destroy
  each other. Create with the batch step's `frame` instead; it picks a free track for that span.
- `authoring.place_bounds` measures at the playhead: give the step a `frame` inside the
  clip, or it refuses ("no measurable geometry"). It also refuses when the object is
  bigger than the box.
- **Not batchable (0.0.72):** `preset.apply`, `comp.new`, `key.box`, `template.apply`
  (plus `object.enter/exit`). Run them with `carvercat_run`, one call each.
- **`preset.apply` takes ONE object** (`id`); an `ids` list is silently reduced to the first id. One call per object — or group the objects and apply to the group.
- **`authoring.place_bounds` refuses an object whose position is animated** ("measured placement refuses animated position"): place first, apply presets after.
- **New text renders red** (default fill on 0.0.72 is not the schema's white): always set `text.fill.color`.
- **Shapes larger than the frame are cropped to the frame before transform scale**, and small shapes scaled ×5+ render stair-stepped: keep geometry ≤ frame size and scale ≤ ~2.5.
- **`edit.save {path}` is SAVE-AS**: the open document becomes that file.
- Track indexes count audio tracks too (A1's index moves when you `track.add`).
- `carvercat_authoring validate` measures a nested-comp instance as its whole (scaled) comp frame, so `bounds_inside`/`no_overlap` give false failures for instances — check those with a look.
- **There is no "remove all keys of a property"**; `key.remove` takes the key at the
  playhead. Apply presets last, and undo (`edit.undo`) if one was wrong.
- **New comps restart clip ids at `clip_1`**, so ids repeat across comps
  ([performance.md](performance.md)).
- A text takes ONE staggered preset per property: a staggered exit on a property that a
  staggered entrance already uses is refused. Use a whole-block exit.
- `text.content` is not keyframeable (no type-on counters); cut text clips back to back.
- If the person clicks around in the app while you work (for example switching comps),
  your next commands act on THEIR comp. Check `carvercat_list` when a reply looks wrong,
  and ask them to keep their hands off during a build.
- `carvercat_look {region}` can draw a full-frame background only partly (seen 0.0.72):
  check backgrounds on a full-frame look, not a region.

## Bulk edits through the project file
For 50+ keys, JSON is faster than MCP: `edit.save` -> edit the `.carverproj` with
`../scripts/motion/carverproj.py` -> `edit.open {path, force:true}` -> `comp.switch`.
A force-reopen discards unsaved work in the app: tell the person not to edit meanwhile.
Property keys look like `tr.e_tr_placement_<id>.position`,
`src.e_src_shape_geometry_rectangle_<id>.width`, `fx.e_fx_blur_<id>.size`,
`src.e_src_text_relative_<id>.opacity`; each is `{keyframes:[{frame,value,easing,
customEase?}], static}`.

## Library: presets and templates
`library/templates/<pack>/` holds `.carverpreset` (a keyframe recipe applied to the
selected object; `frames`, `tracks[{property, keys[{at 0..1, value, easing}]}]`,
optional `stagger`) and `.carvertemplate` (a whole scene), each with a PNG/GIF preview and
a `pack.carverpack` manifest. `library.reload` rescans; the app also watches the folder
(about 2 s). The pack's FIRST tag is its Library shelf (`in`, `out`, `stagger`). Preset
values are RELATIVE: positions and angles add, size, scale and opacity multiply. Preset
easing names only, so curves are baked as keys.

**The Motion Patterns pack** (`../../library/templates/motion-patterns/`, 25 presets and 5
templates, all verified on 0.0.72) installs by copying the folder into the app's
`library/templates/`. The catalogue, timing charts and recipes are in
[../patterns/README.md](../../patterns/README.md). Rebuild it with
`../scripts/motion/build_pattern_pack.py` (presets and cards) and
`../scripts/motion/comp_to_template.py` (a comp of a saved project -> `.carvertemplate`).
