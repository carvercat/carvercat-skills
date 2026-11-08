# Brand end card

**Template** `cb_end_card` (Library name "Brand end card") · Corporate Brand pack · **Verified 0.1.8.1 (rev 1127)**, comp `CB End card` in `categories/corporate-brand/cb-lab-2`.

On a light background (kept in the template): a navy rounded-square mark with a teal centre, a tracked wordmark ("NORTHWIND", SemiBold 60 px, tracking 1.25), a teal rule and the URL. 120 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Light background (`#F3F5F8`) | 0 | none | |
| Mark outer (120 px, radius 24), Mark inner (48 px) | 0, 6 | Card settle | outer settles **f16** |
| Wordmark | 12 | Soft rise | settles **f33** |
| End rule (200×3 px) | 20 | scale X 0 → 1, 20 f, expo | |
| URL (Medium 34 px) | 26 | Soft rise | settles **f47** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0. No overshoot anywhere (the pack's style rule).

## Steps
1. Place and apply on the last 4 s. Replace the two mark rectangles with your logo (an image clip with Card settle) and edit the wordmark and URL.

## Pitfalls
- The lab comp's "Lab bg" is dropped on extraction, so the light ground is a separate "Light background" object. Without it the navy text would land on whatever is underneath.

Inspiration: closing logo cards of corporate films. No external text or code was used.
