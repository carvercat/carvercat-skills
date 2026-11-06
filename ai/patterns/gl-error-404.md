# Error 404 page

**Template** `gl_error_404` (Library name "Error 404 page") · Glitch pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `GL Error 404` in `categories/glitch/gl-lab-3`.

For briefs like "404 page animation", "broken link", "page not found for a site demo". A white 404 at 380 px that jolts in with a red/cyan split and background-coloured tears through the digits, PAGE NOT FOUND (cyan, tracked), a line of copy, a GO HOME pill button, and a cursor that glides to it and clicks. 120 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Code "404" | 0 | jumps +40, −24, +12, 0 px; split 36 → 20 → 30 → 12 → 0 px; re-glitch f64–68 | split **f12**; steady **f68** |
| Tear 1–5 (near-black bars, 10–24 px) | f2–8, f64–66 | 2–3 f clips across the digits | |
| Headline / Body | 10 / 16 | opacity Hold steps | **f15 / f21** |
| Button (cyan 4 px pill) | 24 | switches on like a tube | **f30** (4.1%) |
| Cursor (path) | 40 | glides in from 420 px right / 200 px below on expo over 24 f; presses (size 85% f74–78) | lands **f55** (curves) |
| Button press / label colour | 74 / 75 | the pill fills cyan; the label turns near-black (Hold key on text fill) | **f75** |

Lint 0 errors, 0 warnings; `inspect qc` (240 px): **no flashes**. Placed into a fresh comp: lint 0/0/0, qc no flashes. Text-gap audit: closest pair label / cursor, 37.5 px (the cursor tip rests on the right end of the button, clear of the label). Full-frame look of the placed instance at f44 (cursor moving in): nothing cut.

Inspiration: playful website error pages. No external text or code was used.
