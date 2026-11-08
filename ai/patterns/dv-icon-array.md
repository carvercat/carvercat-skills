# Icon array

**Template** `dv_icon_array` (Library name "Icon array") · Data Viz pack · **Verified 0.1.8.4 (rev 1130)**, comp `DV Icon array` in `categories/data-viz/dv-lab-3`.

For briefs like "1 in 4 people", "how many out of 10", survey results about people. 40 person icons (a 30 px head and a 50 × 62 px rounded body) in four rows of ten; the top row turns cyan, so each column of four has one highlighted person; then "1 in 4" and its label. Sample data. 120 f, holds. Different from the waffle chart: people, not percent squares.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Icons (track grey) | 4 + 2·column + row | scale 0.6 → 1, 10 f, expo; opacity in 4 f | first settles **f11**, last **f32** |
| Highlight (top row, head and body) | 36 + 3·column | Colour track → cyan, 6 f, decelerating arrival cubic-bezier(0.333, 0.667, 0.667, 1) | last settles **f69** |
| "1 in 4" (Bold 160 px, cyan) | 70 | 16 px from above, 14 f | settles **f79** |
| Label (Medium 44 px) | 74 | 16 px from above, 12 f | settles **f82** |

Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (closest 19.8 px).

## Steps
1. Another ratio: change the row count, `on` and the stat text in `icon_array()` in `ai/scripts/motion/data_viz_lab3.py` (1 in 5: five rows, top row on).
2. A percentage that is not a simple ratio (37%): use the waffle chart instead.

## Pitfalls
- 80 shapes: rebuild from the script rather than recolouring by hand.
- Keep the highlighted icons in a pattern the eye can count (one row, one column, or the first n); scattered highlights read as noise.

Inspiration: icon arrays in health and survey communication. No external text or code was used.
