# Strokes, dashes and draw-on (Trim)

**Verified 0.0.72:** an open smooth path with a dashed round-cap stroke drawn on by Trim End 0 → 1 (40 f, S-curve); an ellipse ring with round cap, a soft stroke edge, drawn on to 0.75.

## Stroke parameters (`shape.stroke.*`)
| param | values | notes |
|---|---|---|
| paint | none/solid/gradient | turn the stroke ON (`solid`) — paths default to none |
| width | 0–0.2 (frame-width fractions) | 0.004 ≈ 8 px at 1920 |
| color, opacity | | opacity is absorbed into colour alpha |
| line | solid/dashed/dotted | dashes laid out on the shape's FIRST frame; a growing shape stretches them |
| dashLength / dashGap | 0.001–0.5 (frame-width fractions) | 0.012 / 0.008 = route dashes |
| cap | butt/round/square | **round** for draw-ons and routes |
| corners | sharp/round/bevel | joins |
| align | inside/centered/outside | closed shapes only; open lines always centred |
| softEdge | 0–0.2 | feathered stroke ([soft-edge.md](soft-edge.md)) |
Basement controls (line, cap, corners, align, dash) are editable with `property.set` without promotion; promote only to show them on the panel.

## Trim Stroke (`effect.add {cap:"trim"}`)
| param | range | meaning |
|---|---|---|
| start, end | 0–1 | visible portion (either order) |
| offset | −1–1 | whole turns, wrapping — slides the visible segment around a closed shape |
Measured from **3 o'clock counter-clockwise** on rectangle/ellipse/polygon/star, from the **first point** on a path.

## Recipes
- **Draw-on:** end 0 → 1, 20–45 f, S-curve (long routes) or Ease out (short strokes). Start a dot/arrow head at the end point when end reaches 1.
- **Write-off:** then start 0 → 1 (the tail follows): line travels and disappears.
- **Travelling segment / comet:** start and end both animate with end leading by 0.15; or keep start/end 0/0.2 and animate offset 0 → 1 on a closed shape (loader, orbit).
- **Progress ring:** ellipse, fill none, stroke round cap, end 0 → value.
- **Marching ants:** dashed stroke + offset animation (closed shapes).
- **Underline / strike:** a rectangle is better ([../../patterns/kinetic-highlight-sweep.md](../../patterns/kinetic-highlight-sweep.md)).

## Pitfalls
- Trim is shapes only (not text). For text "write-on" use stagger by character.
- Filled shapes keep their fill while the stroke trims — set `shape.fill.paint` none for a pure line draw.
- `object.path {smooth:true}` resamples your points; read the reply's `stored_nodes`, don't assume one node per input point.
