# Driving Carvercat through MCP - essentials for any agent

Carvercat exposes an MCP server (enable it in the app: **File -> Connect to AI**).
Tool names as the server publishes them: `carvercat_run` (one command), `carvercat_look` (render frames
to an image to SEE the work), `carvercat_render` (PNG frames to disk), `carvercat_list` (objects, comps, tracks, bins),
`carvercat_describe` (every parameter of the selection), `carvercat_inspect` (timing, curves, lint, expect),
`carvercat_state`, `carvercat_session` (attach to the visible editor), `carvercat_authoring` (fonts, geometry) and
`carvercat_batch` (many commands as one undoable step; a whole scene is better sent as `scene.apply`).
Your agent may prefix them (e.g. `mcp__carvercat__carvercat_run`). Command names below
are what goes in `carvercat_run {command, args}` or a batch step `{command, args, frame?, as?}`.
Rewritten for design units (API 1.0, Carvercat 0.1.8); trust the live app.
**Machine-readable catalogue**: the app repo's `schema/agent/` (`commands.json` every
command with arguments, `authoring.json` units/batching/validation, `workflows`,
`errors.json`). Read the relevant entry before using an unfamiliar command.

## Loop: build -> look -> fix
1. `carvercat_list` - know the comps, tracks and ids before touching anything.
2. Build the whole scene with ONE `scene.apply` (dry run first, then apply); edit by selector.
3. **Look** at entrance, hold and exit frames (`carvercat_look {from, to, count}`).
   Never report a scene done without looking at it.
3b. **Validate** layout with no render: `measure.boxes`, `measure.overlaps {within: "safe"}`, `layout.safe`, `measure.contrast`, `carvercat_inspect {mode:"lint"|"expect"}`. Before any send: `carve.preflight {host}`.
4. `edit.save` often. Name things (`clip.rename`) so the timeline reads.

## Units

Everything is in design units: px from the frame's top-left with y down, degrees clockwise, CSS colours and easing, time as frames, `"1.5s"` or `"500ms"`. The full table, the call patterns and the old names (accepted for one release) are in [design-units.md](design-units.md). The live, generated reference is `carvercat://schema/design`.

## Commands worth knowing
- Create: `scene.apply` (a whole scene), `object.new {kind: text|rectangle|ellipse|adjustment, style, track, duration}`,
  `object.path {d | pointsPx, closed, track, duration}` (px, y down; one subpath), `media.import {paths}`,
  `library.place {name, frame, track}`, `template.apply`, `preset.apply {name}`.
- Edit: `property.set {id, key, value}` (design keys; `id` may be a selector), `anim.set {id, keyframes|to|from|fromTo|stagger|motionPath}`, `key.set {id, key, value, at, ease}`, `key.remove`, `clip.move {id, frame, track}`, `clip.rename`, `edit.delete
  {ids}`, `edit.group {ids}`, `object.enter/exit` (not batchable), `track.add`.
- Effects: `property.set` of `blur`, `dropShadow`, `glow`, `grain`, `directionalBlur`, `filter` ... (see [../effects/README.md](../effects/README.md)); `effect.add {cap: motionblur}` for motion blur.
- Text stagger: `stagger.new`, `stagger.connect {param}`, `stagger.set {by: character|word, gap}`.
- Masks/parenting: `property.set {id: target, key: "mask", value: {"ref": <mask id>}}` (the mask becomes a child of the target), `clipPath`, `parent.assign`, `parent.clear`.
- Layout: `layout.align | distribute | stack | grid | fit | safe` (px, layout boxes), `text.fit`, `text.balance`, `measure.boxes | overlaps | distance | contrast`; `guide.add {axis, position}`.
- Audio: `media.import {paths, frame}`; level `media.audio.gain` (dB, keyframeable).
- Comps/bins: `comp.new`, `comp.switch {index}`, `comp.duplicate {comp}`,
  `comp.format {width,height}`, `comp.delete {index}`, `bin.new {name}`,
  `comp.move_to_bin {comps, bin}`, `bin.list`.
- File: `edit.save`, `edit.open {path, force}`.
- Export: `export.set {settings}` -> `export.run` (asynchronous: returns the durable job path in `why`; poll `export.status {job}`, never re-run; an `interrupted` job continues with `export.resume {job}`); cancel `deliver.cancel`. Settings/verification: [workflows/export-and-delivery.md](../workflows/export-and-delivery.md).
- Easing is CSS: `ease`, `ease-out`, `ease-in-out`, `cubic-bezier(a,b,c,d)` (x 0-1, y -1.5 to 2.5, so it can overshoot), `steps()`, `spring(...)`. A key's `ease` shapes the segment that LEAVES it; an unknown name is refused (it no longer plays as linear). See [design-units.md](design-units.md) and [../../patterns/custom-curves.md](../../patterns/custom-curves.md). In the project file the stored form is `customEase`.
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
- A new blur has no default: write `blur` in px; a `glow` mix above about 0.3 is haze; a rectangle turns with `rotate`; upscaling small paths with transform scale renders soft (rebuild
  at size).
- **Don't copy clips in the project JSON with their ids** (keys go inert). Clips built
  fresh from a template with new ids work (verified 0.0.72): whole films can be generated
  into the JSON, see [json-authoring.md](json-authoring.md).
- **`comp.duplicate` keeps clip ids** -> rename them ([performance.md](performance.md)).
- Moving `transformOrigin` on a rotated or scaled object keeps the picture where it is and moves `x`, `y` to compensate (at rotate 0, scale 1 it moves nothing). It is CSS: `"left top"`, `"50% 100%"`, `"20px 30px"`. Set it BEFORE a rotate or scale animation, then grow `scale`/`width` from that edge.
- **`clip.move` is an overwrite edit**: moving onto a clip on the same track trims or
  deletes that clip, silently. Combined with `object.new` without a `track` (it picks "a
  track with room" at the PLAYHEAD), a series of object.new + clip.move calls can destroy
  each other. Create with the batch step's `frame` instead; it picks a free track for that span.
- `measure.boxes` and the layout helpers work on layout boxes at the object's rest, in px, with no render and no playhead.
- **Not batchable (0.0.72):** `preset.apply`, `comp.new`, `key.box`, `template.apply`
  (plus `object.enter/exit`). Run them with `carvercat_run`, one call each.
- **`preset.apply` takes ONE object** (`id`); an `ids` list is silently reduced to the first id. One call per object — or group the objects and apply to the group.
- **`layout.*` refuses an object whose position is animated**: place first, animate after (`anim.set`).
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
`src.e_src_shape_geometry_rectangle_<id>.width`, `fx.e_fx_blur_<id>.size` (the stored format; write design keys over MCP),
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
templates, all verified on 0.0.72) installs into the user Library folder (Help > Library Folder or `library.folder`; Carvercat 0.1.8+), in its
`templates/` subfolder, then `library.reload`; read `user.issues` for clashes. Steps: [../patterns/README.md](../../patterns/README.md#installing-a-pack). The catalogue, timing charts and recipes are in
[../patterns/README.md](../../patterns/README.md). Rebuild it with
`../scripts/motion/build_pattern_pack.py` (presets and cards) and
`../scripts/motion/comp_to_template.py` (a comp of a saved project -> `.carvertemplate`).
