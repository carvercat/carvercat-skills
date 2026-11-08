# Anniversary card

**Template** `cb_anniversary` (Library name "Anniversary card") · Corporate Brand pack · **Verified 0.1.8.1 (rev 1127)**, comp `CB Anniversary` in `categories/corporate-brand/cb-lab-3`.

For briefs like "25 years of the company", "milestone anniversary", "celebrating our founding". A teal ring draws round a large number, then the line "years of Northwind", a from–to span with a drawn rule, and a thank-you line. 120 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Kicker "CELEBRATING" (teal SemiBold 30 px, tracked) | 0 | Soft rise (as keys) | |
| Ring (380 px, teal 4 px) | 2 | drawn clockwise from 12 o'clock: rotation +90, Trim start 1 → 0 over 32 f, decelerate | settles **f26** |
| Number "25" (SemiBold 200 px) | 8 | Card settle over 24 f | settles **f26** |
| "years of Northwind" (SemiBold 52 px) | 18 | Soft rise | **f39** |
| 2002 · span rule · 2027 | 26, 30, 40 | Soft rise; rule Trim end 0 → 1 over 18 f | span **f44**, 2027 **f61** |
| Thank-you line (Regular 30 px) | 46 | Soft rise | **f67** |

**0% overshoot.** Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (closest 48.1 px). The ring draws inside the placed instance; a full-frame look of the placed comp shows nothing cut.

## Steps
1. Change the number, the years and the company name. Two digits fit the ring at 200 px; for three digits ("100") drop the number to 160 px.
2. For a product or customer milestone ("1 million orders"), swap the kicker and the line under the ring and remove the year span.

## Pitfalls
- An ellipse's stroke starts at 3 o'clock and runs counter-clockwise; to draw clockwise from 12 o'clock rotate it +90 and trim the start from 1 to 0 ([data-viz geometry facts](data-viz.md#measured-geometry-facts-016)).

Inspiration: anniversary cards in company films and social posts. No external text or code was used.
