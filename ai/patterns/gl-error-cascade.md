# Error cascade

**Template** `gl_error_cascade` · Glitch pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `GL Error cascade` in `categories/glitch/gl-lab-2`.

Four 720 × 300 px grey error windows with blue title bars, each 50 px down-right of the last, popping in 8 f apart. The top window has "FATAL ERROR", the message and an OK button. 120 f, holds.

| Part | Clip start |
|---|---|
| Error window 1–4, Error bar 1–4 | 8, 16, 24, 32 (cut on, no easing) |
| Top window's title, body, button, OK (SemiBold/Medium 30–32 px) | 32 |

Lint 0 errors, 0 warnings; `inspect qc` (240 px) found no flashes. Placed into a fresh comp: lint 0/0/0.

## Pitfalls
- Lint does not see occlusion: texts on every window counted as overlapping (`text_overlap`), and texts cut off after 8 f when the next window landed failed `reading_time`. Only the top window carries text.

Inspiration: cascading OS error dialogs in glitch art. No external text or code was used.
