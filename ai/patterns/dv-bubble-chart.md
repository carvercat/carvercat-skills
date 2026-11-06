# Bubble chart

**Template** `dv_bubble_chart` (Library name "Bubble chart") · Data Viz pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `DV Bubble chart` in `categories/data-viz/dv-lab-3`.

For briefs like "price vs quality", "where do we sit against competitors", "two measures and a size". Ten fictional team-chat apps (sample data): x = price per seat ($0–40), y = satisfaction (60–100), bubble area = paying teams. One bubble ("Cove") is the subject: cyan, ringed and labelled; the rest are slate and step back. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Grid, axis labels, axis titles | 0–8 | opacity in 8 f, 2 f apart | |
| Bubbles (diameter 2·√(teams/31)·55 px, 3 px ground-colour stroke) | 14 + 4 per bubble, in price order | scale 0 → 1, 12 f, expo; opacity in 3 f | **0% overshoot**; first (Iris) settles **f22**, last (Flux) **f58** |
| Context bubbles | 60 | opacity 0.9 → 0.55, 10 f | settle **f69** |
| Hero ring | 60 | scale 0.7 → 1, 14 f, expo | settles **f69** |
| Hero name / note (34 / 28 px) | 64 / 68 | 16 px from above, 12 f | note settles **f76** |

Lint 0 errors, 0 warnings (9 notes: the context bubbles' held opacity). Placed into a fresh comp: lint 0/0/0. Text-gap audit: closest 15.4 px (hero name / note, two lines of one label).

## Steps
1. New data: edit `BUBBLES` (name, x, y, size) and `hero` in `bubble()` in `ai/scripts/motion/data_viz_lab3.py`; the axis ranges are in `X` and `Y`.
2. Keep the label above the hero bubble clear of its neighbours; check with the text-gap audit after moving it.

## Pitfalls
- **Size by area, not diameter**: diameter ∝ √value. Diameter ∝ value makes a 2× value look 4× bigger.
- Big bubbles are drawn first so small ones stay on top and visible.
- `inspect curves` reports a 63.6% "overshoot" on the context bubbles' opacity: that is the step back from 0.9 to 0.55, not a spring.

Inspiration: scatter and bubble charts in market maps. No external text or code was used.
