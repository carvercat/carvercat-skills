# Collection title

**Template** `ml_collection_title` · Minimal Luxury pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `ML Collection title` in `categories/minimal-luxury/ml-lab-2`.

A two-line tracked title ("AUTUMN  WINTER" / "2026", Regular 72 px, tracking 1.6, line spacing 1.35) and a small gold note. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Collection | 0 | Stagger by line, 18 f gap: rise 0.8% H and blur 12 → 0 over 40 f (expo; the blur rides the stagger card's `fill.blur` slot, because a stagger tween does not take blur: [../references/effects/stagger.md](../references/effects/stagger.md) manual build); tracking 1.60 → 1.66 from f58 | line 1 settles **f25**; the second line about 18 f later |
| Season note (26 px, gold, tracking 1.6) | 60 | Slow fade in | settles **f88** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0. No overshoot (the pack's style rule).

## Pitfalls
- At 88 px the tracked first line measured 1850 px wide and lint noted `outside_graphics_safe`. 72 px fits.

Inspiration: season titles in fashion-week films. No external text or code was used.
