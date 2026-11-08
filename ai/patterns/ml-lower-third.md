# Luxury lower third

**Template** `ml_lower_third` (Library name "Luxury lower third") · Minimal Luxury pack · **Verified 0.1.8.1 (rev 1127)**, comp `ML Lower third` in `categories/minimal-luxury/ml-lab-2`.

A 360 px gold rule at y 860 with a tracked name above (Regular 40 px, tracking 1.5) and a tracked role below (26 px, muted). 180 f (6 s) with its own exit.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Rule (2 px) | 0 | Trim end 0 → 1, f0–40, S curve cubic-bezier(0.333, 0, 0.667, 1), the curve arriving at the key; 1 → 0, f140–170 | drawn by **f40**, gone at **f168** (harness: last visible f167) |
| Name | 10 | Slow fade in + Slow fade out; tracking 1.50 → 1.56 over the clip (linear) | opaque by about f42 |
| Role | 22 | Slow fade in + Slow fade out | |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0. No overshoot (the pack's style rule).

## Steps
1. Place and apply. Edit the name and role (keep caps; the tracking is part of the look).

## Pitfalls
- `curves` reports "overshoot 100" on scaleUniform where Slow fade in (1.03 → 1) and Slow fade out (1 → 1.015) share a clip. It is the stacked entrance and exit, not an overshoot; the look shows none.

Inspiration: understated name supers in fashion and hospitality films. No external text or code was used.
