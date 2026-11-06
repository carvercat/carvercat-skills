# Composition and layout, in Carvercat

How to place things in the frame so the viewer reads them in the right order, at the right size, and nothing is cut off. Tool-independent rules, then the Carvercat checks that prove them.

## Rules

- **One focal point per frame.** The hero is the biggest, highest-contrast and first-moving thing. Everything else is smaller, quieter and enters after it (3–6 f later).
- **Reading order is motion order.** Left to right, top to bottom (right to left for RTL). Stagger entrances in that order so the eye is led, not made to search: the Explainer icon grid at 5 f per tile, the Data Viz bars at 4 f per row.
- **Grids.**
  - Pick a margin (96 px at 1920 × 1080, which is also the 5% graphics-safe line) and a column rhythm (6 or 12 columns with 24–32 px gutters), and snap text edges to it.
  - Centred layouts suit titles. Left-aligned layouts suit lists, data and anything read line by line.
- **Hierarchy by size steps.** Each level is about 1.5–2× the next: display 120–220 px, title 64–96 px, body 30–48 px, labels 26–34 px. Lint wants glyphs at least 18 px tall. Measured: 26 px Regular lowercase without ascenders is only 13.5 px tall, so use 36 px or more for such text, and 28 px or more for caps and mixed case at 1080p.
- **Contrast does the pointing.** Value contrast first (light on dark), then hue (one accent), then motion (only the hero moves at the moment of reading).
- **Negative space is a layout element.** Luxury and minimal pieces use 60–70% empty frame. Data and explainers can use 40–50%. Social short-form puts content in the middle 60% of the height.
- **Depth without 3D:** overlap, scale (far things smaller), soft shadows on the near layer only, slower motion for far layers (parallax).
- **Safe areas:**
  - broadcast graphics-safe is 5% in from each edge (96 / 54 px at 1080p);
  - for social 9:16, see [vertical-and-safe-areas.md](vertical-and-safe-areas.md): x 61–1016, y 268–1538, and x < 851 below y 1151.

## In Carvercat

- **Units:** design units: px from the frame's top-left, y down; `x`, `y` are the top-left of the object's box ([../app/design-units.md](../app/design-units.md)). Write layouts in pixels; the app converts inside.
- **Measure, don't guess:**
  - `measure.boxes` gives the real boxes of text in px. The rolling counter, typing caret and word swap are all placed this way.
  - `layout.align`, `layout.fit` and `layout.safe` seat objects inside the frame or the safe area; `text.fit` finds the largest `fontSize` that fits a box.
- **Prove the layout:**
  - `measure.overlaps {within: "safe"}` (safe areas, cards, labels) and `carvercat_inspect mode:lint|expect` (the font really resolved);
  - `carvercat_inspect mode:lint` (`outside_graphics_safe`, `cropped_at_rest`, `text_overlap`, `text_too_small`, `reading_time`);
  - `carvercat_look` with `overlay:["safe","grid"]`.
- **Things lint does not see:** masks ([../known-issues.md#ki-133](../known-issues.md#ki-133)), and thin lines crossing text. Always finish with a look.
- **Anchors for growth direction:** `transformOrigin` "0% 50%" (stored anchor [−1, 0]) grows from the left, "100% 50%" ([1, 0]) from the right, "50% 100%" ([0, −1]) from the bottom. In raw JSON the stored anchor does not move the position (stored value).

## Checklist before a frame is done

1. Can you name the focal point in one word?
2. Does it enter first, and are the rest in reading order?
3. Do all text edges sit on the grid or margin?
4. Is nothing important outside the safe area, at every keyframe and not only at rest?
5. Is every text on screen long enough to read (lint `reading_time`) and big enough (lint `text_too_small`)?
6. Does the hold keep moving a little (drift, push, breathe) without looping back and forth?
