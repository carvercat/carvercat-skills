# Stacked bar

**Template** `dv_stacked_bar` · Data Viz pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `DV Stacked bar` in `categories/data-viz/dv-lab-2`.

One 1200×72 px bar split into four shares (cyan 40%, amber 25%, green 20%, pink 15%), a title and a legend. 90 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Title ("Where the time goes", Bold 44 px) | 0 | opacity in 8 f | |
| Segment 1–4 (anchor at the left edge) | 8, 16, 24, 32 | scale X 0 → 1, 12 f, Custom expo | Segment 1 settles **f16**, Segment 4 **f40** |
| Swatch + Legend 1–4 (Medium 30 px) | segment + 6 | opacity in 8 f | |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place and apply. Set each segment's width (share × 1200 px) and its centre (previous right edge + half its width). Edit the legend text.

## Pitfalls
- No spring on the segments: an overshoot would push a segment over the next one for a few frames.

Inspiration: share-of-total bars in reports. No external text or code was used.
