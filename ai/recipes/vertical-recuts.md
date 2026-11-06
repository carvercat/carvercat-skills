# Vertical (9:16) re-cuts: what carries over and what doesn't

Measured while making the 9:16 versions of three recipes. **Verified 0.1.6 (rev 1105), 2026-10-28; builder and measures re-run on Carvercat 0.1.8, 2026-11-04**

## `comp.format` on a finished 16:9 film: don't
`comp.format {width:1080, height:1920}` on the SaaS launch master (900 f, eleven placed templates) replied "1080 x 1920 at 30 fps" and changed only the comp frame:
- **Objects keep their pixel size and are re-centred.** The 1920 × 1080 background became a 1080-wide box at y 656–1264 (it measured 1080 × 608: objects keep their size relative to the comp width, so a full-frame 16:9 object becomes a 16:9 band across the middle). Each placed template kept its 1920 × 1080 extent and now overhangs the frame by 420 px on each side (re-measured on master, 4 Nov 2026: same result, 11 warnings at 56%).
- **Nothing is re-laid out.** Text, cards and charts stay where they were relative to the centre, so anything wider than 1080 px is cut at the sides (the feature headline lost its first and last letters).
- **Lint saw it:** 11 `cropped_at_rest` warnings, one per placed template ("only 56% on screen").
- **The template comps inside stay 16:9.** Only the master changed.
So `comp.format` changes the canvas, not the design. Use it on an **empty** comp before placing anything (the social pack's placement tests do this), not to convert a finished film.

## Placing 16:9 templates into a 9:16 comp
`library.place` + `template.apply` into a 1080 × 1920 comp reports "template applied at 1920 x 1080" and **fits** the template inside the width: the instance measured 1080 × 608 (letterboxed in the middle), lint 0 / 0 / 0. Every element is at 56% of its designed size (1080 / 1920), so text gets small: a 30 px label lands at 17 px.

**To make it work, zoom each instance on its content** (`property.set {id, key:"scale", value}`). `scale` is absolute and `template.apply` has already fitted the instance at 0.5625, so the value is 0.5625 × the zoom in the table (2.4 sets `scale` 1.35); the builders do that multiplication:
| Template | Zoom used | Why that number |
|---|---|---|
| Chart card, CTA end card | 2.4, 2.2 | the card is 640 px wide in 16:9: 640 × 0.5625 × 2.4 = 864 px |
| KPI tile | 3.4 | a 440 px tile |
| Stat punch | 2.8 | the 520 px ring |
| Comparison bars | 1.5 | the delta badge sits 600 px right of centre: (600 × 0.5625 × z) must stay under about 520 px |
| Progress rings, waffle | 1.45 | three rings / grid + value span about 1100 px |
| Donut, gauge | 2.2, 2.4 | centred, about 600 px wide |
| Focus pull, word swap, kinetic quote, beat words | 2.2, 1.9, 1.55, 2.0 | each line's width |

Rule: `zoom ≈ 1000 / (content width in 16:9 px × 0.5625)`, then check the widest element with a look.

## Two traps measured
1. **A zoomed instance held still is larger than the frame** (its 1920-wide box), so lint flags `cropped_at_rest` (the first attempt had five: 27–77% on screen). Give every zoomed instance a slow push (3% over its clip, from its zoom; key the end frame first, then the start with `ease: "linear"`, or the start's ease is dropped and lint flags the last frames); then it is never still and lint is 0 / 0 / 0.
2. **Lint does not see content cut inside a moving instance** ([KI-144](../references/known-issues.md#ki-144)). At zoom 2.0 the comparison bars' delta badge and at 1.6 a progress ring were cut by the frame edge, with lint 0 / 0 / 0. Only the look showed it. Check the widest element of every zoomed scene with a full-frame look.

## What needs a manual re-cut
- **Wide horizontal layouts** (column chart with 6 columns, data table, ranked bars, the SaaS dropdown and modal with app canvas, compare columns, team row, split screen): zooming makes them too wide; rebuild them for 9:16 or leave them out. The re-cuts drop them.
- **Hooks and end cards:** use the 9:16 templates (Hook title, Follow end card, Highlight caption, Swipe up) instead of zooming the 16:9 ones; they are built for the safe area.
- **Safe area:** zoomed 16:9 content is centred, so it sits in the safe band naturally; captions and buttons from the social pack keep to their verified `bounds_inside` positions (checked today with `measure.overlaps {within: "safe"}`).
- **Small labels:** after fit and zoom, check that labels are still 28 px or more (labels at 30 px designed and zoom 1.45 land at about 24 px).

## The three re-cuts
| Recipe | 9:16 version |
|---|---|
| [saas-feature-launch-30s](saas-feature-launch-30s.md) | [saas-launch-9x16](saas-launch-9x16.md) |
| [quarterly-results](quarterly-results.md) | [quarterly-results-9x16](quarterly-results-9x16.md) |
| [kinetic-quote-reel](kinetic-quote-reel.md) | [kinetic-quote-reel-9x16](kinetic-quote-reel-9x16.md) |
