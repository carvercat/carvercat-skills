# Fill and gradients

`fill` and `stroke` are CSS colours or CSS gradients, as you see them (`"#FF7A00"`, `"rgb(255 122 0)"`, `"orange"`, `"linear-gradient(90deg, #ff7a00 0%, #1b1b1b 100%)"`); never a linear-light array. On a shape, `fill: "none"` (in a scene node's `style`) leaves it unpainted.

**Verified:** a linear gradient fill and a gradient stroke on a rounded rectangle, and a shimmer highlight swept across by **keying the gradient line** (the stored `gradientStart` and `gradientEnd`, moved together over 30 f); verified: gradient-fill-and-sheen. Rounded corners hold on a gradient-filled shape (the 48 px radius in that case's look): the old open question is closed.

## Setting a gradient (shape)
```json
{"command": "property.set", "args": {"id": "#plate", "key": "fill", "value": "linear-gradient(90deg, #b8860b 0%, #b8860b 40%, #fff3c4 50%, #b8860b 60%, #b8860b 100%)"}}
{"command": "property.set", "args": {"id": "#plate", "key": "stroke", "value": "linear-gradient(90deg, #00e5c3 0%, #7a5cff 100%)"}}
{"command": "property.set", "args": {"id": "#plate", "key": "strokeWidth", "value": 6}}
```
Also in a scene node's `style` (`"fill": "radial-gradient(circle 900px at 50% 50%, #2b2b3a 0%, #0d0d14 100%)"`).

- The linear form follows the CSS gradient line (through the box centre, ends on the box edges); stops are in `%` (a `px` stop is refused); the radial form is `circle|ellipse [R] at X Y` with R in px or `%`. The model's radial is box-proportional, so a circle on a non-square box is drawn as an ellipse and the reply says so. After Effects keeps the first and last stop only (reported by `carve.preflight`).
- Reading it back: `fill` is the CSS string when the gradient line passes through the centre exactly; otherwise the stored object is reachable at `src.e_src_shape_fill_<id>.gradient`.
- A solid colour is kept as a reference when you switch to a gradient; recolouring the solid does NOT recolour a live gradient: set `fill` to a new gradient.
- A solid `fill` or `stroke` colour animates by name: `anim.set {keyframes: [{at: 0, fill: "#ff0000"}, {at: 30, fill: "#00ff00"}]}`. A gradient value in `anim.set` is refused (`bad-colour`): animate the gradient line (below).
- **Text:** `fill` on a text takes a colour (alpha allowed), not a gradient (refused, `bad-colour`). A text gradient is the stored paint at `src.e_src_text_fill_<id>.gradient` with stops in linear light (verified: text-gradient-on-the-stored-path):

  ```json
  {"command": "property.set", "args": {"id": "#t", "key": "src.e_src_text_fill_clip_3.gradient", "value":
    {"mode": "linear", "stops": [{"p": 0, "color": [1, 0.1, 0], "a": 1}, {"p": 1, "color": [0, 0.2, 1], "a": 1}], "start": [0, 0.5], "end": [1, 0.5]}}}
  ```

  `p` is 0 to 1, `a` alpha per stop; `start`/`end` are object-local normalised coordinates. Text gradient endpoints are NOT live on text (a static packed gradient only), measured on 0.0.72.

## What renders and what does not (`param.list` `available`)
| Live | Not read by the renderer on 0.0.72 (stored only) |
|---|---|
| gradient (stops, mode, start, end), **gradientStart**, **gradientEnd** (keyframeable) | gradientAngle, gradientSize, gradientAspect, gradientMapping, gradientType, gradientRadiusX/Y, gradientInterp, **gradientOffset**, gradientRepeat, gradientQuality |

Keying an unavailable one changes nothing on screen (keying gradientOffset first moved nothing). Always check `param.list` `available` before animating a paint control (measured on the stored parameters, 0.0.72; the sheen below was re-run on this build).

## Recipes
- **Shimmer / sheen:** stops base, base, highlight, base, base with the highlight 10 to 20 % wide; key the gradient line start and end together over 20 to 35 f, `ease-in-out`. Repeat with a 2 to 3 s gap, never constantly. Verified (gradient-fill-and-sheen):

  ```json
  {"command": "key.set", "args": {"id": "#plate", "key": "src.e_src_shape_fill_clip_2.gradientStart", "value": [-1, 0.5], "at": 0, "ease": "ease-in-out"}}
  {"command": "key.set", "args": {"id": "#plate", "key": "src.e_src_shape_fill_clip_2.gradientStart", "value": [1, 0.5], "at": 30}}
  {"command": "key.set", "args": {"id": "#plate", "key": "src.e_src_shape_fill_clip_2.gradientEnd", "value": [0, 0.5], "at": 0, "ease": "ease-in-out"}}
  {"command": "key.set", "args": {"id": "#plate", "key": "src.e_src_shape_fill_clip_2.gradientEnd", "value": [2, 0.5], "at": 30}}
  ```

  Measured on this build, with the 5-stop plate above (1200 px wide): the highlight is off the plate at frame 0, centred at about 22 %, 52 %, 78 % and 100 % of the plate's width at frames 6, 9, 12 and 15, and gone by frame 18. It crosses faster than the arithmetic of the two key values suggests, so look at three frames and move the second key to time the sweep.
- **Duotone background:** a radial gradient, centre stop 15 % lighter than the edge; a slow drift of the line (about 0.05) over the whole scene for life.
- **Gleam inside text:** make the text the mask of a rectangle with a gold, ivory, gold gradient and key the rectangle's gradient line (verified: gleam-inside-text; the verified keys are [-1, 0.5] to [1, 0.5] and [0, 0.5] to [2, 0.5] over 60 f). The earlier recipe (verified 2026-10-27 on 0.1.6) used [-0.6, 0.5] to [0.6, 0.5] and [0.4, 0.5] to [1.6, 0.5] over 80 f. See [../../patterns/ml-light-sweep.md](../../patterns/ml-light-sweep.md).

  ```json
  {"command": "property.set", "args": {"id": "#gold", "key": "mask", "value": {"ref": "<text id>", "invert": false}}}
  ```

  The text becomes the mask over the rectangle (the mask's own box is then relative to the rectangle). Write `invert` explicitly ([compositing-and-masks.md](compositing-and-masks.md)).
- **Gradient stroke:** `stroke: "linear-gradient(...)"` as above.

## Pitfalls
- Write CSS colours as you see them; never paste an RGB triple as if it were linear light. The only places linear-light arrays remain are the stored paths (the text gradient above).
- A gradient is not keyable through `anim.set`; the gradient line is, on the stored path.
