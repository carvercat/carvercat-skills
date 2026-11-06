# Stat punch

**Template** `kt_stat_punch` · Kinetic Typography pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `KT Stat punch` in `categories/kinetic-typography/kt-lab-2`.

One big number inside a drawn ring, with a label below. 90 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Ring (520 px ellipse, 12 px accent stroke, rotation 90°) | 0 | Trim Stroke end 0 → 1, f4–34, Custom expo | settles **f23** |
| Number ("3x", ExtraBold 300 px) | 2 | Words slam | **4.6% overshoot, settles f15** |
| Label ("faster renders", ExtraBold 64 px, y 800) | 16 | Words rise - expo | position settles **f27** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place and apply. Edit the number and the label. "3x" fills about 60% of the ring's width; check a longer number with `carvercat_look`.
2. A counting number: replace Number with the [rolling counter](su-rolling-counter.md) recipe.

## Pitfalls
- An ellipse's stroke starts at 3 o'clock and runs counter-clockwise. The 90° rotation (positive is counter-clockwise) moves the start to 12 o'clock.

Inspiration: the "big number" stat beats of explainer and keynote videos. No external text or code was used.
