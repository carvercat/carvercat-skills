---
id: cookbook/blob-morph
title: Morph one shape into another (blob morph)
section: cookbook
tags: [morph, blob, shape morph, path animation, organic, liquid, path keyframes, path.geometry]
styles: [funky, saas-ui, explainer, cartoon-bounce]
topics: [shapes, transformation, loops]
related: [techniques/morphing, techniques/looping, cookbook/seamless-loop, cookbook/background-drift, principles/slow-in-slow-out]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.blobmaker.app/]
---

# Morph one shape into another (blob morph)

**Goal.** An organic blob that slowly turns into a different blob and back, as a looping background shape,
built with the agent tools and nothing else.

## Steps

1. **Draw shape A** with `object.path {d, duration: 60}`: `d` is SVG path data in px, y down, closed with `Z`; here 8
   nodes round the centre at 45° steps, radii 300, 250, 320, 240, 290, 260, 310, 230 px, each node smooth with handles
   along the tangent, length 0.265 × radius (4/3 × tan(π/16), the circle value for 8 nodes). (`points` and `handles` as
   fractions of the frame still work: the old way.)
2. `object.path` gives the path a **38.4 px blue stroke** (`strokeWidth` 38.4). Turn it off with `stroke: "none"` and set the
   fill with `fill: "#4c7bd9"` (`property.set`).
3. **Key the geometry.** `view.seek {frame:0}` then
   `key.set {key:"path.geometry", value:A, ease:"linear"}`; `view.seek 30`, `key.set` with shape B
   (`ease:` the S-curve string); `view.seek 60`, `key.set` with A again for the loop. A value is the whole contour:
   `{"closed":true, "points":[{"x","y","inX","inY","outX","outY","corner"}, …]}` in object-local frame
   fractions, y down, 0.5 = the object's position, exactly as `key.list {key:"path.geometry"}` prints it. The shape of a
   path has no design key yet, so this one stays in the stored fractions; the ease is the key's `ease` (`key.set {…, ease: "linear"}`).
4. **Give every key the same number of nodes, in the same order.** Node *i* travels to node *i*.
5. Comp length 60, last key on f60, so f0 follows f59 without a repeated frame ([seamless loop](seamless-loop.md)).

The editor route works too: once `path.geometry` has one key, moving a point with `point.move` at another
frame adds a key there. In a test run, `key.set` at f0 followed by four `point.move` calls at f20 left
`path.geometry keyed at 0, 20`.

## Measured in Carvercat 0.1.6

Comp `K Blob morph` in [cookbook lab 8](../labs/README.md#cookbook-lab-8carverproj), made by the commands above
only. Distance from the centre to the edge along each node's direction (rendered frames, px):

| Frame | node 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| 0 (A: 300 250 320 240 290 260 310 230) | 299 | 249 | 319 | 239 | 290 | 260 | 310 | 229 |
| 5 | 293 | 255 | 312 | 246 | 284 | 265 | 306 | 235 |
| 15 (halfway; mean of A and B 260 290 275 290 250 290 280 265) | 259 | 289 | 274 | 290 | 250 | 290 | 280 | 265 |
| 30 (B: 220 330 230 340 210 320 250 300) | 219 | 328 | 229 | 340 | 210 | 320 | 250 | 300 |
| 45 | 259 | 289 | 274 | 290 | 250 | 290 | 280 | 265 |
| 59 | 299 | 249 | 319 | 239 | 290 | 260 | 310 | 229 |

- Every node moves straight from its A position to its B position: at the S-curve midpoint (f15) each radius is
  the mean of the two keys to within 1 px; at f5 a node has gone 7.5% of the way (S-curve start).
- `inspect qc`: loop seam **0.0**; `inspect lint`: 0 errors, 0 warnings, 0 notes. `key.list` reports three keys,
  8 nodes each.
- **Different node counts do not morph.** Comp `K Blob mismatch`: the same A, but a 6-node circle on f30. The
  shape held A from f0 **through f30** (ink 670–1258 px on the centre row), jumped to the hexagon-ish circle on
  **f31** (700–1218 px), held it to f59 and jumped back on f60. `key.set` accepted the 6-node key without a
  word and lint reported only a `speed_jump` note.

## Traps

- Node count mismatch is silent: [KI-161](../../ai/references/known-issues.md#ki-161). Read the keys back with
  `key.list` and count the points.
- `object.path` recentres the nodes on their extrema midpoint (it reports this as `source_to_stored`, here
  −5.0 px in x and y), so a `key.set` with no `value` keys the recentred shape, not your numbers. For a loop,
  give every key an explicit value, or copy the f0 value from `key.list` into the last key.
- The default stroke (`strokeWidth` 38.4) makes the blob 19 px bigger all round; it is easy to mistake for a morph error.
- Keep handles roughly the length the node spacing needs (here 0.265 × radius); very long handles on one key
  and short on the other make the edge wobble mid-morph.

## In Carvercat

- Curve names on this page (S-curve) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Commands: `object.path {d}`, `property.set` (`fill`, `stroke`), `view.seek`, `key.set` (`path.geometry`), `key.list`, `point.move`. Old names, accepted for one release: `src.e_src_shape_stroke_<id>.paint`, `src.e_src_shape_fill_<id>.color`, `easing:"Linear"` / `"S-curve"` on the arriving key.
- Library: the `Blob` shape is a ready organic outline to start from; `Pattern drift` for a moving background.
- Background: [shape morphing](../techniques/morphing.md), [looping](../techniques/looping.md),
  [FR-045](../../ai/references/known-issues.md#fr-045) (closed by this page).
