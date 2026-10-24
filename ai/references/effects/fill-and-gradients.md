# Fill and gradients

**Verified 0.0.72:** linear gradient on a rectangle; a shimmer highlight swept across by **keying `gradientStart` and `gradientEnd`** (moved together from [−1,0.5]/[0,0.5] to [1,0.5]/[2,0.5] over 30 f, S-curve).

## Setting a gradient (shape)
```json
{"command":"property.set","args":{"id":"clip_3","key":"shape.fill.paint","value":"gradient"}},
{"command":"property.set","args":{"id":"clip_3","key":"shape.fill.gradient","value":
  {"mode":"linear","stops":[{"p":0,"color":[0.955,0.518,0.027],"a":1},{"p":0.5,"color":[1,0.9,0.6],"a":1},{"p":1,"color":[0.955,0.518,0.027],"a":1}],
   "start":[0,0.5],"end":[1,0.5]}}}
```
- Colours are **linear light** (see conventions). `p` 0–1, `a` alpha per stop. `start`/`end` are object-local normalised coordinates (0–1 across the object), not comp positions. `mode` linear or radial.
- `paint`: `none | solid | gradient`. The solid `color` is kept as a reference when you switch to gradient — recolouring the solid does NOT recolour a live gradient; edit the stops.
- Text: `text.fill.*` the same way (text gradient endpoints `gradientStart/End` are NOT live on text — static packed gradient only).

## What renders and what doesn't (param.list `available`)
| Live | Not read by the renderer on 0.0.72 (stored only) |
|---|---|
| gradient (stops, mode, start, end), **gradientStart**, **gradientEnd** (keyframeable) | gradientAngle, gradientSize, gradientAspect, gradientMapping, gradientType, gradientRadiusX/Y, gradientInterp, **gradientOffset**, gradientRepeat, gradientQuality |
Keying an unavailable one changes nothing on screen (we keyed gradientOffset first — no movement). Always check `param.list` → `available` before animating a paint control.

## Recipes
- **Shimmer / sheen:** stops base–base–highlight–base–base with the highlight 5–10 % wide; key start/end together by +2 object widths over 20–35 f, S-curve. Repeat with a 2–3 s gap, never constantly.
- **Duotone background:** radial gradient, centre stop 15 % lighter than the edge; slow drift of start/end (±0.05) over the whole scene for life.
- **Gradient stroke:** `shape.stroke.paint` gradient with the same object.

## Pitfalls
- Hex → linear: use the toolkit's converter; never paste sRGB 0–255/255 values as linear.
- Corner radius looked much smaller than requested on a gradient-filled rectangle (0.04 W asked) — verify rounded corners with a look (open question).
