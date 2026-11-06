# The basement: hidden parameters, promoting, raising, and ropes

Carvercat keeps every parameter an object COULD have; only some show on the Controls (Properties) panel. The rest live in the **basement**. The design keys (`blur`, `glow`, `softEdge`, `strokeWidth`, ...) cover the common controls; the basement is the stored table behind them and reaches what has no design key (secondary glow, motion blur, gradient line, stagger slots, text outline thickness). Stored paths and stored units: [PARAMETERS.md](PARAMETERS.md) ("Design names" says which stored parameter each design key writes). Three ladders:

| Rung | What | Command |
|---|---|---|
| panel | on the Controls panel | none |
| basement (`down`) | exists, editable, not shown | `param.list {id, where: "basement"}` |
| face | handed UP to the comp/group that contains the object, so every INSTANCE shows it and can override it | `param.raise {path, up: true}` |

## Read it
`param.list {id, where: "all"|"panel"|"basement"|"face", match}` returns for each param: `path`, `on` (panel/basement), `rung`, `keyframeable`, **`hookable`** (can take a rope), `wired`, **`available`** and `unavailable_reason` (verified: basement-rope-and-reset). `match` narrows by a substring of the path (`match: "glow"`). **Check `available` first**: for example most gradient sub-controls say "Stored separately, but the native gradient renderer does not read this control": setting them does nothing on screen. Setting a design key adds the effect and its entry (`fx.e_fx_glow_clip_3`), so `param.list` is how you learn the path.

## Promote (basement to panel)
`param.promote {id, path, on: true}` (batchable). **Verified** (glow-secondary-in-the-basement): promoting `fx.<glow>.secondary` then setting it true turned on the secondary glow (the stored value reads `on`). Some basement settings must be promoted before `property.set` accepts them (the app's workflow notes say so for effect sub-settings); paint and stroke style controls (line, cap, corners, align, dashes) are editable without promotion, and now have design keys (`strokeLinecap`, `strokeLinejoin`, `strokeAlign`, `strokeDasharray`). When a set refuses with "not on the panel", promote and retry. `on: false` sends it back. `param.reset {path}` returns it to default (verified).

## Raise to a face (make templates editable)
Inside a comp: `param.raise {path: "src.e_src_shape_fill_<id>.color", up: true}`: every instance of that comp shows "Colour" on its face; changing it on an instance writes an override for that instance only (`param.revert {path}` to follow the comp again). `face.rename {path, name}` and `face.order {path, index}` tidy the face. Gradients need BOTH Colour and Gradient raised. **Use this for templates**: raise the accent colour, headline text and key sizes so a placed template is edited from outside without `comp.switch`. This section was not re-run in this pass (it needs a comp instance; on a plain object in the open comp the call answers "no parameter at ..."); the commands and rule are carried over from the earlier verified builds.

## Ropes (wires)
`link.new {id, from, to, mul, add}` wires one parameter to another **on the same object**: `to = from x mul + add`, live every frame, in the STORED units of both ends (a rotation in the stored degrees, a size in size units, a softEdge as a fraction of the frame width). `link.cut {id, to}` removes it. Only `hookable` params take part (rotation, opacity, softEdge, stroke width, dash length/gap, geometry width/height/sides/innerRadius, effect sizes ...).

**Verified** (basement-rope-and-reset): a star's `tr.e_tr_placement_<id>.rotation` to `src.e_src_shape_geometry_star_<id>.innerRadius` with mul 0.002, add 0.2: the reply says "Rotation now drives Depth"; `link.cut {to}` and `param.reset` undo it; a path on another object is refused. The star's rotation is keyed with `anim.set {keyframes: [{at: 0, rotate: 0}, {at: "2s", rotate: 180}]}`.

### Rope ideas (only the first row's mechanism is verified; the others are suggestions)
| from | to | effect |
|---|---|---|
| rotation | star/polygon innerRadius or sides | spinning icon that morphs |
| opacity | blur size (mul -20, add 20, stored size units) | fades in out of focus with one curve. The reply "Opacity now drives Size" was seen, but `property.get blur` still read the unwired value at three frames: check with a look |
| scaleY / geometry height | softEdge | bars soften as they grow (softEdge is a fraction of W) |
| opacity | glow amount (mul 0.7) | glow fades with the element, never burns |
| stroke width | dashGap | thicker line, wider dashes |

Rule: one driver, many followers: key only the driver; the rest stay in sync when you retime.

## Pitfalls
- Paths change with ids (`..._clip_3`): re-read `param.list` after duplicating or templating.
- Key the DRIVER; whether a wired follower's own keys still apply was not tested.
- Raised controls live on the comp; overrides live on instances: `param.revert` before re-styling the source if instances look stale.
- Cross-object paths refuse ("no parameter at ..."): to drive another object, parent it, group it, or key both.
