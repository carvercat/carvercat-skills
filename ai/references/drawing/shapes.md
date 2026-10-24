# Shapes: rectangle, ellipse, polygon, star, line, path

Read this when building anything from primitives — icons, cards, badges, bars, characters, maps, UI.

`object.new {kind}` with kind `rectangle | ellipse | polygon | star | text | background | adjustment` (`rect`, `circle`, `ngon` are aliases); custom shapes with `object.path`. Verified on 0.0.72 unless marked.

## Units (the #1 source of mistakes)
- Geometry width AND height are fractions of the **comp WIDTH**: on 16:9 a full-height rectangle is height 0.5625, a full-frame one 1 × 0.5625.
- Position (`center`) is frame fractions, **y up**. Anchor is in **half-sizes of the object** ([−1,0] left edge, [0,−1] bottom edge, [0,1] top).
- Default size: rectangle/ellipse/star 0.2 W (384 px at 1920).
- Keep geometry ≤ the frame (larger is cropped to the frame before transform scale) and transform scale ≤ ~2.5 (beyond, edges step).

## Per-shape geometry (`shape.geometry.<kind>.*`)
| Shape | Params | Notes |
|---|---|---|
| rectangle | width, height, **cornerRadius** (0..), angle (not the transform) | pills: cornerRadius = height/2. On a gradient-filled rect a 0.04 radius looked smaller than expected — check with a look. Rotate with the TRANSFORM `angle`, not geometry angle |
| ellipse | width, height, angle | circles: width = height. Ring = fill none + stroke |
| polygon (ngon) | width, height, **sides**, angle | triangle 3, hexagon 6 (badges), sides keyframeable & hookable |
| star | width, height, **sides** (points), **innerRadius** (depth 0–1, default 0.37), angle | burst/sticker: sides 12–24, innerRadius 0.75–0.85; classic star 5 / 0.38–0.45 |
| line | width, height, cornerRadius, angle | thin rectangle semantics |
| path | `object.path {points, handles?, closed, smooth?}` | points in frame fractions, **y DOWN**; the object is recentred (reply gives geometry_centre); `smooth:true` resamples — read `stored_nodes` |

## Paint
Fill (`shape.fill.*`: color, paint none/solid/gradient, softEdge), stroke (`shape.stroke.*`: paint, width, cap, corners, align, line dashed/dotted, softEdge). See ../effects/fill-and-gradients.md, stroke-and-trim.md, soft-edge.md.

## Recipes by shape
- **Badge / sticker:** star sides 16, innerRadius 0.82, accent fill + text on top; entrance `Swing in` or `Pop - spring`; slow continuous rotation (linear, 0.5°/f) during the hold.
- **Hexagon icon tile:** polygon sides 6, angle 30 (pointy-top), stroke 0.003 + soft glow ≤ 0.6.
- **Progress ring:** ellipse fill none, stroke round cap, Trim end 0 → value.
- **Pill button / CTA:** rectangle, cornerRadius = height/2, label text centred via `align.apply hcenter/vcenter` or place_bounds; `Pop - gentle` + shadow lift.
- **Morphing icon:** rope rotation → star innerRadius or polygon sides (../effects/basement-promote-ropes.md).
- **Arrows / connectors:** `authoring.arrow` builds a single editable path whose head and shaft share an endpoint.
- **Burst lines:** 8–12 thin rectangles around a point (rotate each by 360/n with anchor at their inner end [0,−1]), scaleY 0 → 1 → 0 staggered 1 f — a classic impact accent.

## Arranging
- Measure, don't guess: `carvercat_authoring {mode:"geometry", id}` gives true bounds; `authoring.place_bounds` seats an object in a pixel box (place BEFORE animating).
- `align.apply {mode, to}` (left/hcenter/right/top/vcenter/bottom/distribute-h/distribute-v/space-h/space-v; to selection/key/comp) on a selection.
- Stack order = track order: higher track draws on top. Plan tracks before building (../../patterns/promo-assembly.md).
- Validate: `carvercat_authoring {mode:"validate", checks:[bounds_inside, no_overlap]}`.

## Recreating UI (demo / tutorial shots)
- Pointer: draw the cursor as a 7-point polygon (~2.4 px/unit), white fill, dark outside stroke with round corners. `object.path` recentres the object on its node-extrema midpoint, so the pointer tip (hotspot) is offset from the position — store that offset and key `position = hotspot + offset`.
- A "switch" UI element (e.g. a timeline's keyframe/curve pill) reads best as a rounded rect whose icon swaps (dash → lane → curve) while the clip below grows from bar → lane → curve height.
