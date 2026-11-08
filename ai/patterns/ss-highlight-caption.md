# Highlight caption (9:16)

**Template** `ss_highlight_caption` · Social Short-form pack · **verified 0.1.8.1 (rev 1127)**, comp `SS Highlight caption` in `categories/social-media-reels/ss-lab-2`.

**Measured on 0.1.8.1 (rev 1127, harness `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0, no flashes; against the v1 original the worst silhouette difference is 0.10 % (limit 2 %) and every object is present with the same text (box offset at most 3.3 px); colours are now the exact hex the page states (mean shift 58.6 of 255, intended). The frame numbers in the table above are the keys of the generator (`design units`), unchanged.


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
