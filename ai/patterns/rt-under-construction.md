# Under construction page

**Template** `rt_under_construction` (Library name "Under construction page") · Retro pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `RT Under construction` in `categories/retro/rt-lab-3`.

For briefs like "90s website", "under construction", "coming soon, the old-web way", "throwback homepage". A grey page with a navy-to-blue title bar, two yellow-and-black hazard bands scrolling opposite ways, UNDER CONSTRUCTION with a white offset shadow, a subline, a hit counter that ticks up, a "best viewed at 800 x 600" footer and a red NEW! burst that pops, turns and blinks. 150 f. Full-frame page included.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Band top / Band bottom (120 px, stripes 60 px wide every 120 px, slanted 45°) | 0 | the stripes move 240 px (two periods) left / right over 150 f, linear: the last frame matches the first | 1.6 px a frame |
| Headline (ExtraBold 104 px, white hard shadow 5 px) | 4 | Rise - on twos as keys | **f14** |
| Subline (Bold 50 px, navy) | 14 | the same | **f24** |
| New burst (14-point star, 290 px) and New (ExtraBold 64 px) | 10 | Pop - on twos as keys; the burst then turns −60° to the end | **3.9%**, **f22** |
| New (blink) | 10 | Hold keys: on to f50, then 15 f off / 30 f on | one blink every 1.5 s |
| Counter label, Counter box | 24 | label rises on twos (f34); the box fades in on twos (f28) | |
| Counter 1–3 (000417, 000418, 000419; green Bold 50 px) | 28, 80, 120 | hard cuts | |
| Footer (Medium 36 px) | 34 | Rise - on twos | **f44** |

Lint 0 errors, 0 warnings in the lab (4 notes, `speed_jump` on the stepped rises); placed 0/0/0. `inspect qc`: no flashes. Text-gap audit: closest pair 54.5 px (headline and subline). The title-bar gradient runs navy on the left to light blue on the right (look). Full-frame looks of the placed instance at f0 and f149 show the bands in the same place and nothing cut.

## Steps
1. Change the counter numbers in `retro_lab3.py`; each number needs 25 opaque frames (lint reading time), so keep at least 30 f per tick.
2. The page title is plain text in the bar; replace it with the site name.

## Pitfalls
- A stripe that starts outside the frame and moves further out is `never_visible` (error): `hazard_band()` drops stripes that are off frame for the whole clip.
- The bar text first sat at y 32 with x 40: `outside_graphics_safe` (info). The bar is 112 px tall and the text sits at x 110, y 76.
- NEW! at 56 px popping from size 0 was `text_too_small` (17.1 px on the first step); at 64 px it passes.

Inspiration: 90s personal home pages (hazard bands, hit counters, NEW! bursts). No external text or code was used.
