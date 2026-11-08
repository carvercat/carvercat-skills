# Save the date

**Template** `ml_invitation` (Library name "Save the date") · Minimal Luxury pack · **Verified 0.1.8.1 (rev 1127)**, comp `ML Invitation` in `categories/minimal-luxury/ml-lab-3`.

For briefs like "wedding save-the-date", "gala invitation", "you are invited". A double gold frame draws itself, then SAVE THE DATE, the names, a short rule, the date, the venue and a line about the invitation fade in. 180 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Frame 1 (960 × 680 px, gold 2 px) | 0 | draws, trim end 0 → 1, f0–56, S curve cubic-bezier(0.333, 0, 0.667, 1), the curve arriving at the key | settles **f51** |
| Frame 2 (920 × 640 px, gold 1 px) | 0 | the same, f10–66 | settles **f61** |
| Kicker "SAVE THE DATE" (gold Regular 26 px, tracking 1.6, y 320) | 24 | opacity in 36 f; tracking 1.60 → 1.64 from f60 | |
| Names "Amelia & James" (ivory Regular 80 px, y 430) | 36 | Slow fade in (baked: opacity and scale 1.03 → 1) | opacity **f67**, size **f63**, **0% overshoot** |
| Rule (120 px, y 515) | 0 | opens from its centre, f56–96 | |
| Date "12 · 06 · 2027" (ivory Regular 40 px, tracking 1.4, y 590) | 60 | opacity in 36 f; tracking 1.40 → 1.44 | opaque **f91** |
| Venue (muted Regular 26 px, tracking 1.25, y 670) and note (muted 26 px, y 750) | 72, 84 | opacity in 36 f | note opaque **f115** |

Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 10 pairs, closest 56.2 px (Date / Venue).

## Steps
1. Change the names, date, venue and note. Keep the names on one line: at 80 px "Amelia & James" measures 578 px of ink, and the inner frame is 920 px wide.
2. For a gala or launch, change the kicker (YOU ARE INVITED) and use the note line for the RSVP date.

## Pitfalls
- **Tracked caps run wide inside a frame.** At 26 px and tracking 1.4, "VILLA BALBIANO · LAKE COMO" measured 842 px, 39 px from the inner frame on each side; at tracking 1.25 it is 666 px. Longer venues need two lines or less tracking.
- The frames are drawn by a trim on the rectangle's stroke; in the looks both start at the top-right corner and run clockwise, the inner one 10 f behind.

Inspiration: engraved wedding and gala stationery. No external text or code was used.
