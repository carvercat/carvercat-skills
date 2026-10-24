# Bar chart that grows

**Template:** `Bar chart - grow` (mp_info_bar_chart) · **verified 0.0.72** · 120 f · overlay

## Timing

```
Baseline  0 grow X from its left edge (18 f)
Bar 1       6 grow Y from its bottom edge (16 f, expo)
Bar 2          9
Bar 3             12
Bar 4 (hero)         15  <- accent colour, the tallest bar, last
```

## Steps

1. Rectangles: width 0.07 W, height = value × scale (geometry height is in frame-WIDTH units).
2. **Set `anchor [0,-1]`** (the bottom edge) on each bar, then seat it on the baseline: `authoring.place_bounds {box:[x, top, 134.4, baseline_y - top], horizontal:"center", vertical:"bottom"}`. The box must be at least as tall as the bar, or it refuses.
3. Baseline: `anchor [-1,0]`, then `Grow across (X)`.
4. Bars: `Grow up (Y)`, each clip starting 3 f after the previous one. Stagger by moving the clip starts, not by shifting keys.
5. Value labels: put a text above each bar and give it `Rise - expo` 4 f after its bar starts.

## Knobs

- Horizontal bars: anchor `[-1,0]` and `Grow across (X)`.
- Counting numbers: there is no text counter in 0.0.72, and `text.content` cannot be keyframed. Cut short text clips back to back (one clip per number), or reveal only the final number with Pop - gentle.
