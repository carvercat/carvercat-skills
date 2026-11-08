# Monogram end card

**Template** `ml_monogram_end` · Minimal Luxury pack · **Verified 0.1.8.1 (rev 1127)**, comp `ML Monogram end card` in `categories/minimal-luxury/ml-lab-2`.

A 220 px gold ring drawn around a monogram ("ME", 72 px), a tracked wordmark (48 px, tracking 1.8) and an address. 150 f (5 s), holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Monogram ring (2 px, rotation 90°) | 0 | Trim end 0 → 1, f0–50, S curve cubic-bezier(0.333, 0, 0.667, 1), the curve arriving at the key | settles **f45** |
| Monogram | 24 | Slow fade in + Drift up - 4 s | size settles **f52** |
| Wordmark | 44 | Slow fade in; tracking 1.80 → 1.86 | |
| Address (26 px, muted) | 64 | Slow fade in | settles **f92** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0. No overshoot (the pack's style rule).

## Steps
1. Place and apply on the last 5 s. Edit the monogram, wordmark and address, or replace the monogram with a logo image (keep the presets).

Inspiration: monogram lockups of maisons and hotels. No external text or code was used.
