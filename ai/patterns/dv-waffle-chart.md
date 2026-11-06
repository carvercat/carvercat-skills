# Waffle chart

**Template** `dv_waffle_chart` · Data Viz pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `DV Waffle chart` in `categories/data-viz/dv-lab-2`.

A 10×10 grid of 44 px rounded cells (10 px gaps): 64 filled cyan, 36 empty, then a big "64%" and a label to the right. 90 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Empty cells (36) | 2 + row | opacity in 4 f | |
| Filled cells (64) | 4 + i / 2 (two a frame, reading order) | scale 0.4 → 1, 8 f, expo; opacity in 4 f | Cell 1 settles **f9**, Cell 64 **f40** |
| Waffle value ("64%", Bold 160 px) | 44 | 16 px from above, 14 f, expo | settles **f52** |
| Waffle label (Medium 40 px) | 48 | 16 px from above, 12 f | |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0. The template has 102 objects.

## Steps
1. A different share: rebuild with `waffle()` in `ai/scripts/motion/data_viz_lab2.py` (change `v`). Editing 100 cells by hand is not practical.

## Pitfalls
- The empty cells are only the unfilled ones, so the top rows look empty (not grey) until they fill. For a grey grid behind every cell, add 64 more track cells under the filled ones.

Inspiration: unit / waffle charts in data journalism. No external text or code was used.
