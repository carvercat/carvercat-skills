# Award badge

**Template** `cb_award_badge` (Library name "Award badge") · Corporate Brand pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `CB Award badge` in `categories/corporate-brand/cb-lab-3`.

For briefs like "we won an award", "certified", "recognised as". A round badge (drawn teal ring, navy disc, teal star, "WINNER" and the year) above the award name and the awarding body. 120 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Badge ring (380 px, teal 4 px) | 0 | drawn clockwise from 12 o'clock (rotation +90, Trim start 1 → 0 over 30 f) | **f23** |
| Badge disc (336 px, navy) | 8 | Card settle (as keys) | **f23** |
| Star (96 px, 5 points, inner 0.45) | 16 | Card settle; turned with rotation +90 so a point is up | **f31** |
| "WINNER" (SemiBold 36 px, tracked), year (Medium 30 px) | 20, 24 | Soft rise (as keys) | Winner **f41** |
| Award name (SemiBold 60 px), awarding body (Regular 32 px) | 32, 38 | Soft rise | **f53**, **f59** |

**0% overshoot.** Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (closest 32.6 px, Winner / Year).

## Steps
1. Edit the award, the body and the year. For a certification, change "WINNER" to "CERTIFIED" and the star to a short code (a text at 44 px, for example "ISO 27001") in the same place.
2. If the client supplies the real award seal, place it over the disc and delete the star and texts inside it; do not redraw someone else's mark.

## Pitfalls
- A star or polygon starts with a point to the right, and a polygon's Angle control does not rotate it on 0.1.6 ([KI-150](../references/known-issues.md#ki-150)). Turn it with the transform rotation instead.

Inspiration: award and certification badges in company news films. No external text or code was used.
