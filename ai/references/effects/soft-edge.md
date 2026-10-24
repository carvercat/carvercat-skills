# Soft (smooth) edges on shapes

**Verified 0.0.72:** ellipse 0.35 W, `shape.fill.softEdge` 0.12, opacity 0.35 → a soft ambient light blob; ring stroke with `shape.stroke.softEdge` 0.004 → a slightly feathered line. Soft edges are measured 1:1 against Resolve (4/8/14 px matched with zero error).

| param | range | default | unit |
|---|---|---|---|
| shape.fill.softEdge | 0–0.2 | 0 | fraction of frame width (0.01 ≈ 19 px feather at 1920) |
| shape.stroke.softEdge | 0–0.2 | 0 | same, on the stroke band only |
Both are keyframeable and hookable (can be roped).

## Soft edge vs blur
| Soft edge | Blur |
|---|---|
| feathers only the outline, inside stays solid | smears the whole object |
| cheap, exact, renders 1:1 in Resolve | heavier; size not a pixel radius |
| ideal for light blobs, vignettes, gradient-like glows, soft shadows built from shapes, masks with a feathered edge | focus pulls, depth of field |

## Recipes
- **Ambient light / bokeh blob:** big ellipse (≤ frame size), softEdge 0.08–0.15, opacity 0.1–0.35, accent colour, slow drift over the whole scene. The cheapest way to make a flat background feel lit.
- **Vignette** (not verified): a large dark rectangle/ellipse ring around the frame with softEdge 0.1–0.2 (or a dark frame-sized shape with an inverted soft mask).
- **Shape-built shadow:** dark ellipse under an object, scaleY 0.2, softEdge 0.02–0.04, opacity 0.3 — perfect for bouncing characters (scale it with the bounce height).
- **Feathered mask** (not verified): soft-edged shape used as a mask (`mask.make`) gives a soft wipe edge.
- **Reveal:** animate softEdge 0.2 → 0 with opacity 0 → 1: the shape "condenses" into focus.

## Pitfalls
- The value is width-relative, not object-relative: the same 0.05 is a huge feather on a small icon and a subtle one on a big shape. Scale it with the object.
- softEdge larger than half the shape's smallest dimension eats the shape — for small shapes stay ≤ 25 % of their size.
