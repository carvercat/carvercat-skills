# The basement: hidden parameters, promoting, raising, and ropes

Carvercat keeps every parameter an object COULD have; only some show on the Controls (Properties) panel. The rest live in the **basement**. Three ladders:

| Rung | What | Command |
|---|---|---|
| panel | on the Controls panel | — |
| basement (`down`) | exists, editable, not shown | `param.list {id, where:"basement"}` |
| face | handed UP to the comp/group that contains the object, so every INSTANCE shows it and can override it | `param.raise {path, up:true}` |

## Read it
`param.list {id, where:"all"|"panel"|"basement"|"face", match}` → for each param: `path`, `on` (panel/basement), `rung`, `keyframeable`, **`hookable`** (can take a rope), `wired`, **`available`** + `unavailable_reason`. **Check `available` first**: e.g. most gradient sub-controls say "Stored separately, but the native gradient renderer does not read this control" — setting them does nothing on screen.

## Promote (basement → panel)
`param.promote {id, path, on:true}` (batchable). **Verified:** promoting `fx.<glow>.secondary` then setting it true turned on the secondary glow. Some basement settings must be promoted before `property.set` accepts them (the app's workflow notes say so for effect sub-settings); paint/stroke style controls (line, cap, corners, align, dashes) are editable without promotion. When a set refuses with "not on the panel", promote and retry. `on:false` sends it back. `param.reset {path}` returns it to default.

## Raise to a face (make templates editable)
Inside a comp: `param.raise {path:"src.e_src_shape_fill_<id>.color", up:true}` → every instance of that comp shows "Colour" on its face; changing it on an instance writes an override for that instance only (`param.revert {path}` to follow the comp again). `face.rename {path, name}` and `face.order {path, index}` tidy the face. Gradients need BOTH Colour and Gradient raised. **Use this for templates**: raise the accent colour, headline text and key sizes so a placed template is edited from outside without `comp.switch`.

## Ropes (wires)
`link.new {id, from, to, mul, add}` wires one parameter to another **on the same (selected) object**: `to = from × mul + add`, live every frame. `link.cut {id, to}` removes it. Only `hookable` params take part (rotation, opacity, softEdge, stroke width, dash length/gap, geometry width/height/sides/innerRadius, effect sizes …).
**Verified:** a star's `tr.e_tr_placement_<id>.rotation` → `src.e_src_shape_geometry_star_<id>.innerRadius` with mul 0.002, add 0.2: the star's points deepen as it spins (reply: "Rotation now drives Depth").
Cross-object paths refuse ("no parameter at …"): to drive another object, parent it, group it, or key both.

### Rope ideas (only the first row's mechanism is verified; the others are suggestions)
| from | to | effect |
|---|---|---|
| opacity | blur size (mul −20, add 20) | fades in out of focus with one curve |
| rotation | star/polygon innerRadius or sides | spinning icon that morphs |
| scaleY / geometry height | softEdge | bars soften as they grow |
| opacity | glow amount (mul 0.7) | glow fades with the element, never burns |
| stroke width | dashGap | thicker line, wider dashes |
Rule: one driver, many followers — key only the driver; the rest stay in sync when you retime.

## Pitfalls
- Paths change with ids (`…_clip_3`): re-read `param.list` after duplicating/templating.
- Key the DRIVER; whether a wired follower's own keys still apply was not tested.
- Raised controls live on the comp; overrides live on instances — `param.revert` before re-styling the source if instances look stale.
