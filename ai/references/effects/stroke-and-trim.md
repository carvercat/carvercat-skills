# Strokes, dashes and draw-on (trim)

**Verified** (strokes-dashes-and-draw-on): an ellipse ring with round caps and a dashed stroke trimmed to 75 %; a rounded square with a 20 px inside stroke and round joins; an open smooth path with a round-cap stroke drawn on by Trim End 0 to 1 over 40 f. On 0.0.72 the same draw-on (dashed round-cap path, Trim End 0 to 1 over 40 f) and a ring drawn to 0.75 were verified on the stored parameters.

## Stroke keys
All are style keys of a shape (a scene node's `style`, `object.new {style}`, `property.set`).

| key | values | notes |
|---|---|---|
| `stroke` | a CSS colour or gradient, `none` | turn the stroke ON by giving a colour; paths default to none. Animates by name (`anim.set` with `stroke`) |
| `strokeWidth` | px, 0 to 0.2 x W (384 px at 1920) | the old 0.004 was 8 px at 1920. `stroke_pass` draws exactly `px` on the frame-width scale (the app counts a 20 px band for 20) |
| `strokeDasharray` | `"dash gap"` in px, `dotted`, `none` | `"24 12"`; the model lays out a whole count of dashes once, on the outline length at the shape's FIRST frame, so a growing shape stretches them. The reply carries `dashEffective {d, g, count, outlinePx, exact, nearestExact}`; `strokeDashoffset`, `pathLength` and patterns of more than two numbers are refused with the reason |
| `strokeLinecap` | `butt` / `round` / `square` | **round** for draw-ons and routes |
| `strokeLinejoin` | `miter` / `round` / `bevel` | joins |
| `strokeAlign` | `inside` / `center` / `outside` | closed shapes only; open lines are always centred |
| `softEdge` | px | one soft edge for the fill and the stroke together ([soft-edge.md](soft-edge.md)); `strokeSoftEdge` is its old name |

```json
{"command": "property.set", "args": {"id": "#ring", "key": "strokeDasharray", "value": "24 12"}}
{"command": "property.set", "args": {"id": "#ring", "key": "strokeLinecap", "value": "round"}}
{"command": "property.set", "args": {"id": "#card", "key": "strokeAlign", "value": "inside"}}
```

A route's dashes of 0.012 W and 0.008 W were 23 and 15 px at 1920. In the stored table these are `shape.stroke.width`, `dashLength`, `dashGap` (fractions of the frame width), `line`, `cap`, `corners`, `align`; the basement controls (line, cap, corners, align, dash) are editable without promotion; promote only to show them on the panel. See [PARAMETERS.md](PARAMETERS.md) "Design names".

## Trim: `trimStart`, `trimEnd`, `trimOffset` in %
`trimStart` and `trimEnd` (0 to 100, the visible portion, either order) and `trimOffset` (-100 to 100, whole turns, wrapping: slides the visible segment around a closed shape). A bare number is a percent; a unit-less string is refused. The first write adds the trim effect, and the reply and `describe` carry `trimOrigin`: rectangles and ellipses start where the ray to the right of the centre meets the outline and run counterclockwise on screen (3 o'clock counterclockwise, measured on 0.0.72 for polygon and star too); a path starts at its first point. The start does not move while start and end change.

```json
{"command": "property.set", "args": {"id": "#ring", "key": "trimEnd", "value": "75%"}}
{"command": "property.set", "args": {"id": "#ring", "key": "trimOffset", "value": "25%"}}
```

## Recipes
- **Draw-on:** `trimEnd` 0 to 100 % over 20 to 45 f, `ease-in-out` (long routes) or `ease-out` (short strokes). Start a dot or arrow head at the end point when the end reaches 100 %.

  By design name (verified: keyed-trim-draw-on, strokes-dashes-and-draw-on):

  ```json
  {"command": "object.path", "args": {"d": "M 1260 700 C 1360 300 1560 300 1700 700"}}
  {"command": "anim.set", "args": {"id": "<path id>", "keyframes": [{"at": 0, "trimEnd": "0%", "ease": "ease-in-out"}, {"at": 40, "trimEnd": "100%"}]}}
  ```

  A path can also be a `type: "path"` node with `d` in a `scene.apply` scene, with its trim keys in `keyframes` (verified: path-node-in-a-scene, scene-keyframes-take-the-effect-keys). At frame 20 `property.get {key: "trimEnd"}` reads back between 20 % and 80 %. `object.path {d}` converts px (y down; one subpath per call; `M L H V C S Q T A Z`). The stored key route (`fx.e_fx_trim_<id>.end`, 0 to 1, from `param.list {id, match: "trim"}`) still works.

- **Write-off:** then `trimStart` 0 to 100 % (the tail follows): the line travels and disappears. Key `trimStart` the same way (verified: keyed-trim-write-on-and-off); the stored route is the entry's `start`.
- **Travelling segment / comet:** `trimStart` and `trimEnd` both animate with the end leading by 15 %; or keep 0 and 20 % and animate `trimOffset` 0 to 100 % on a closed shape (loader, orbit). `trimStart`, `trimEnd` and `trimOffset` are all keyable by name (verified: keyed-trim-write-on-and-off); stored: the `start`, `end`, `offset` keys of the entry.
- **Progress ring:** an ellipse, `fill: "none"`, round-cap stroke, `trimEnd` 0 to the value.
- **Marching ants:** a dashed stroke plus a `trimOffset` animation (closed shapes).
- **Underline / strike:** a rectangle is better ([../../patterns/kinetic-highlight-sweep.md](../../patterns/kinetic-highlight-sweep.md)).
- **Animating the stroke width or the corner radius:** `strokeWidth` (px) and `borderRadius` (px or `%`; rectangles only) are keyable by name in `anim.set` and `key.set` (verified: keyed-stroke-width-and-border-radius). The stored paths are `src.e_src_shape_stroke_<id>.width` (fraction of W) and `src.e_src_shape_geometry_rectangle_<id>.cornerRadius` (2r / min(w, h)).

## Pitfalls
- Trim is shapes only (not text; `effect.addable` on a text does not offer Trim Stroke). For text "write-on" use stagger by character ([stagger.md](stagger.md)).
- Filled shapes keep their fill while the stroke trims: set `fill: "none"` for a pure line draw.
- `object.path` keeps your nodes for `{d}`; a path built with `smooth: true` resamples your points (carried over from 0.0.72, not re-run here): read the reply's `stored_nodes` instead of assuming one node per input point.
- A `type: "path"` node with `d` works in a scene document; `scene.get` hands `d` back (verified: path-node-in-a-scene). `object.path {d}` makes one outside a scene. `object.path` starts at the playhead unless `frame` is given.
