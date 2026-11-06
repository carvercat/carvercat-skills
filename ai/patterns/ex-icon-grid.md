# Icon grid

**Template** `ex_icon_grid` · Explainer pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `EX Icon grid`.

Six 300 × 260 px white tiles (radius 28, soft shadow) in a 3 × 2 grid. Each has an icon built from native shapes (star, disc, rounded square, triangle, hexagon, ring) and a Bold 34 px caption.

| Part (tile *i*, reading order) | Frames | Motion | Measured |
|---|---|---|---|
| Tile | from 5*i* | **Step in** | settles 11 f after its start |
| Icon | from 5*i* + 4 | scale 0 → 1, Custom back | 9.8% overshoot, settles 10 f after its start |
| Caption | from 5*i* + 8 | **Step in** | |

Lint 0/0. Replace each icon with the product's icon (an SVG-imported path or a library sticker) and keep the 5 f reading-order stagger.
