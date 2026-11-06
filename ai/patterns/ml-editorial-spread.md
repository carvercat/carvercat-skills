# Editorial spread

**Template** `ml_editorial_spread` (Library name "Editorial spread") · Minimal Luxury pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `ML Editorial spread` in `categories/minimal-luxury/ml-lab-3`.

For briefs like "magazine feature", "lookbook page", "the story behind the collection". A two-page layout: a photo on the left page, revealed by a feathered window that comes down from above while the photo pushes 3%, a gutter line, and on the right page a kicker, a two-line headline, a rule, a standfirst and the page number. 180 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Photo (stand-in, 760 × 840 px at x 520, y 540, diagonal warm gradient) | 0 | scale 1.00 → 1.03, linear (the push) | linear to **f179** |
| Photo window (the mask, 960 × 1040 px: the photo plus a 100 px feather each side; Fill soft edge 100 px) | 0 | down from above, f0–60, S curve cubic-bezier(0.333, 0, 0.667, 1), the curve arriving at the key | **0% overshoot**, settles **f54** |
| Gutter (dim line, x 960, y 160–920) | 0 | draws, f10–60 | |
| Kicker "ISSUE 04 · AUTUMN" (gold Regular 26 px, tracking 1.5, x 1060, y 290) | 30 | opacity in 36 f | |
| Headline "The Art of / Slow Living" (ivory Regular 80 px, line spacing 1.15, y 420) | 40 | up 14 px over 44 f (decelerate), then a 0.3% H drift | opaque **f71** |
| Rule (160 px, y 552) | 0 | opens from its centre, f64–104 | |
| Standfirst (muted Regular 30 px, two lines, line spacing 1.5, y 640) | 66 | opacity in 36 f | opaque **f97** |
| Folio "14" (muted Regular 26 px, right edge x 1720, y 930) | 90 | opacity in 36 f | |

Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 6 pairs, closest 29.8 px (Kicker / Headline). Full-frame looks of the placed instance at f30 (the feathered edge crossing the photo) and f179: nothing is cut.

## Steps
1. Replace the stand-in: import the photo, cover 760 × 840 px at x 520, y 540, run `property.set {id:"your photo", key:"mask", value:{"ref":"<Photo window id>"}}` + `parent.clear {ids:[Photo window, your photo]}`, delete the Photo rectangle.
2. Change the kicker, headline, standfirst and folio. Keep the headline to two lines of about 12 characters at 80 px ("Slow Living" sets the width: 391 px); the right page runs 764 px from x 1060 to the graphics-safe edge at x 1824.

## Pitfalls
- **A feathered window the same size as the photo keeps feathering it at rest.** In the first build the photo's edges stayed soft for the whole hold. Make the window the photo plus the feather on every side.
- **That larger window must still fit the frame.** At 1160 px tall it ran off the top and bottom and lint warned `cropped_at_rest` on the window, although a mask is never drawn ([KI-151](../references/known-issues.md#ki-151)). The photo is 840 px tall so that photo + 2 × 100 px fits.
- The standfirst first came in at f76 and lint warned `reading_time` (55 characters want 98 f, it had 96). It starts at f66 now; longer copy needs an earlier start or a longer clip.

Inspiration: magazine and lookbook spreads. No external text or code was used.
