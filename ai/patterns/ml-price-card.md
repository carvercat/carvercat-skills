# Price card

**Template** `ml_price_card` · Minimal Luxury pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `ML Price card` in `categories/minimal-luxury/ml-lab-2`.

Product name (56 px, tracking 1.5), a 320 px gold rule, the material and a gold price, left-aligned at x 900. The left of the frame is left for the product shot. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Product name | 0 | Slow fade in + Drift up - 4 s | size settles **f28** |
| Price rule | 16 | opens from its centre, f16–56, S curve cubic-bezier(0.333, 0, 0.667, 1), the curve arriving at the key | settles **f52** |
| Material (30 px, muted) | 30 | Slow fade in | |
| Price (40 px, gold) | 48 | Slow fade in | settles **f76** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0. No overshoot (the pack's style rule).

## Steps
1. Place over the product shot and apply; edit name, material and price.

## Pitfalls
- Wide tracking adds a lot of width: "LE SAC No. 3" at 56 px measures 834 px. At x 1240 it ran out of the frame (lint `cropped_at_rest`, 82% on screen); check long names against the graphics-safe area (x ≤ 1824).

Inspiration: product cards in luxury e-commerce films. No external text or code was used.
