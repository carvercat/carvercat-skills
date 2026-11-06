# Highlight caption (9:16)

**Template** `ss_highlight_caption` · Social Short-form pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SS Highlight caption` in `categories/social-media-reels/ss-lab-2`.

A one-line caption (ExtraBold 72 px, white with the pack's black outline) centred at x 490, y 1250, with a pink box behind the key word. Three text objects, positioned with `cc.textw`. 90 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Caption part 1 "this is", part 3 "free" | 0, 6 | Caption words pop | |
| Caption highlight (radius 14, 1.2× the font size tall) | 10 | scale X 0 → 1 from its left edge, f10–18, expo | settles **f15** |
| Caption part 2 "actually" | 12 | Caption words pop | **4.4% overshoot**, settles **f20** |

Lint 0 errors, 0 warnings. `bounds_inside` the safe box [61, 268, 955, 1270] passed for every object. Placed into a fresh 1080 × 1920 comp (`comp.format`): applied at 1080 × 1920, lint 0/0/0.

## Steps
1. To change the words, edit `parts` in `highlight_caption()` of `ai/scripts/motion/social_short_form_lab2.py` and rebuild; widths come from `cc.textw` (needs Pillow).

Inspiration: emphasis captions in short-form video. No external text or code was used.
