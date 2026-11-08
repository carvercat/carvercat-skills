# Bar chart that grows

**Template:** `Bar chart - grow` (mp_info_bar_chart) · **Verified 0.1.8.1 (rev 1127)** · 120 f · overlay

## Timing

```
Baseline  0 grow X from its left edge (18 f)
Bar 1       6 grow Y from its bottom edge (16 f, expo)
Bar 2          9
Bar 3             12
Bar 4 (hero)         15  <- accent colour, the tallest bar, last
```


**Measured** on `MP INFO Bar chart` (one definition for every number below: the lab comp rendered at 320x180, `starts` = first frame that differs from frame 0 by at least 0.5 (mean channel value, 0-255), `steady` = the frames whose picture matches the settled one within 0.5; harness `ai/scripts/motion/verify_pack.py`): first change f8, the picture is steady from f21 to the end (f119); the hero bar's keys end f37 but move under the threshold from f21. Lint 0/0/0 in 16:9 and 9:16; shape difference against v1 0.00 %.

## Steps


1. Rectangles: width 134.4 px (the stored 0.07 W at 1920), height = value × scale in px.
2. **Set `transformOrigin "50% 100%"`** (the bottom edge; stored anchor `[0,-1]`) on each bar, then seat it on the baseline with `layout.align` / `property.set` on `x`, `y` in px (box `[x, top, 134.4, baseline_y - top]`), and check it with `measure.boxes`.
3. Baseline: `transformOrigin "0% 50%"` (stored `transformOrigin "0% 50%"`), then `Grow across (X)`.
4. Bars: `Grow up (Y)`, each clip starting 3 f after the previous one. Stagger by moving the clip starts, not by shifting keys.
5. Value labels: put a text above each bar and give it `Rise - expo` 4 f after its bar starts.

## Knobs

- Horizontal bars: anchor `[-1,0]` and `Grow across (X)`.
- Counting numbers: there is no text counter in 0.0.72, and `text.content` cannot be keyframed. Cut short text clips back to back (one clip per number), or reveal only the final number with Pop - gentle.
