# Shapes: rectangle, ellipse, polygon, star, line, path

Read this when building anything from primitives — icons, cards, badges, bars, characters, maps, UI.

`object.new {kind}` with kind `rectangle | ellipse | polygon | star | text | background | adjustment` (`rect`, `circle`, `ngon` are aliases); custom shapes with `object.path`. Verified on 0.0.72 unless marked.

## Units (the #1 source of mistakes)
- `width` and `height` are px (or `%` of the frame). Stored geometry is fractions of the **comp WIDTH** for both axes: on 16:9 a full-height rectangle is stored height 0.5625 (1080 px at 1920 wide), a full-frame one 1 × 0.5625.
- Position is `x`, `y` in px from the frame's top-left, **y down**, the top-left of the object's box (stored `center`: frame fractions, y up). Pivot is `transformOrigin` as in CSS ("0% 50%" left edge, "50% 100%" bottom edge, "50% 0%" top); stored anchors are half-sizes of the object ([−1,0], [0,−1], [0,1]).
- Default size: rectangle/ellipse/star 384 px at 1920 (stored 0.2 W).
- Keep geometry ≤ the frame (larger is cropped to the frame before transform scale) and transform scale ≤ ~2.5 (beyond, edges step).

## Per-shape geometry (`shape.geometry.<kind>.*`)
| Shape | Params | Notes |
|---|---|---|
| rectangle | width, height, **cornerRadius** (stored; design `borderRadius` px or %), angle (not the transform) | pills: `borderRadius "50%"` (stored cornerRadius = height/2). On a gradient-filled rect a 0.04 radius looked smaller than expected — check with a look. Rotate with the TRANSFORM (`rotate`, clockwise), not geometry angle |
| ellipse | width, height, angle | circles: width = height. Ring = fill none + stroke |
| polygon (ngon) | width, height, **sides**, angle | triangle 3, hexagon 6 (badges), sides keyframeable & hookable |
| star | width, height, **sides** (points), **innerRadius** (depth 0–1, default 0.37), angle | burst/sticker: sides 12–24, innerRadius 0.75–0.85; classic star 5 / 0.38–0.45 |
| line | width, height, cornerRadius, angle | thin rectangle semantics |
| path | `object.path {points, handles?, closed, smooth?}` | points in frame fractions, **y DOWN** (stored; design form `object.path {d}` in px); the object is recentred (reply gives geometry_centre); `smooth:true` resamples — read `stored_nodes` |

## Paint
Fill (stored `shape.fill.*`: color, paint none/solid/gradient, softEdge; design `fill`, `softEdge` px), stroke (stored `shape.stroke.*`: paint, width, cap, corners, align, line dashed/dotted; design `strokeWidth` px, `strokeLinecap`, `strokeLinejoin`, `strokeAlign`, `strokeDasharray`; the shape's one `softEdge` px softens fill and stroke together). See ../effects/fill-and-gradients.md, stroke-and-trim.md, soft-edge.md.

## Recipes by shape
- **Badge / sticker:** star sides 16, innerRadius 0.82, accent fill + text on top; entrance `Swing in` or `Pop - spring`; slow continuous rotation (linear, 0.5°/f) during the hold.
- **Hexagon icon tile:** polygon sides 6, angle 30 (pointy-top; stored value), stroke 0.003 (stored fraction of width) + soft glow ≤ 0.6.
- **Progress ring:** ellipse fill none, stroke round cap, `trimEnd` 0 → value (key `trimEnd` by name).
- **Pill button / CTA:** rectangle, `borderRadius "50%"`, label text centred via `layout.align {mode: center}` or `layout.fit`; `Pop - gentle` + shadow lift.
- **Morphing icon:** rope rotation → star innerRadius or polygon sides (../effects/basement-promote-ropes.md).
- **Arrows / connectors:** `authoring.arrow` builds a single editable path whose head and shaft share an endpoint.
- **Burst lines:** 8–12 thin rectangles around a point (rotate each by 360/n with `transformOrigin` "50% 100%" at their inner end; stored anchor [0,−1]), scaleY 0 → 1 → 0 staggered 1 f — a classic impact accent.

## Arranging
- Measure, don't guess: `measure.boxes` gives true bounds in px; `layout.fit`, `layout.align` and `layout.safe` seat objects (place BEFORE animating).
- `layout.align {ids, mode: left|right|top|bottom|centerX|centerY|center, to: frame|safe|selection}` and `layout.distribute {ids, axis}` (older `align.apply {mode, to}`: left/hcenter/right/top/vcenter/bottom/distribute-h/distribute-v/space-h/space-v) on a selection.
- Stack order = track order: higher track draws on top. Plan tracks before building (../../patterns/promo-assembly.md).
- Validate: `measure.overlaps {within: "frame"|"safe"}` and `carvercat_inspect mode:lint|expect`.

## Recreating UI (demo / tutorial shots)
- Pointer: draw the cursor as a 7-point polygon (~2.4 px/unit), white fill, dark outside stroke with round corners. `object.path` recentres the object on its node-extrema midpoint, so the pointer tip (hotspot) is offset from the position — store that offset and key `position = hotspot + offset` (stored value).
- A "switch" UI element (e.g. a timeline's keyframe/curve pill) reads best as a rounded rect whose icon swaps (dash → lane → curve) while the clip below grows from bar → lane → curve height.
