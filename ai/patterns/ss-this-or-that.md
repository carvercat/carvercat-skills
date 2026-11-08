# This or that (9:16)

**Template** `ss_this_or_that` (Library name "This or that (9:16)") · Social Short-form pack · **verified 0.1.8.1 (rev 1127)**, comp `SS This or that` in `categories/social-media-reels/ss-lab-3`.

**Measured on 0.1.8.1 (rev 1127, harness `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0, no flashes; against the v1 original the worst silhouette difference is 0.00 % (limit 2 %) and every object is present with the same text (box offset at most 0.0 px); colours are now the exact hex the page states (mean shift 14.1 of 255, intended). The frame numbers in the table above are the keys of the generator (`design units`), unchanged.


For briefs like "this or that", "which one would you pick", "A or B quiz". A question, two choice cards side by side (420 × 520 px stand-ins) with labels, a VS badge, then the pick: a yellow outline and tick on one card while the other dims. 150 f, holds. Unlike the Poll sticker (result bars), this shows a choice being made.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Question "THIS OR THAT?" (ExtraBold 96 px) | 0 | Hook punch (as keys) | **f7** |
| Choice 1 / 2 (from the left / right) | 8, 12 | Whip in (as keys), motion blur 180 | **f15 / f19** |
| Choice labels (ExtraBold 60 px, outline) | 10, 14 | Whip in | **f17 / f21** |
| Pick outline (yellow 10 px, under the badge) | 70 | Hook punch from 1.06 | **f77** |
| VS badge (150 px yellow) and "VS" (ExtraBold 60 px) | 22 | pop 0 → 1 / 0.6 → 1, back curve | **9.7% overshoot**, **f32** |
| Choice 1 and its label | (keys at 70) | opacity 1 → 0.35, 8 f | **f78** |
| Pick badge (96 px) and tick (9 px) | 72, 76 | pop; trimEnd 0% → 100%, 8 f, expo | badge **f82**, tick **f81** |

Lint 0/0/0. `bounds_inside` passed for every object (the cards end at y 1090, above the button column). Placed into a fresh 1080 × 1920 comp: lint 0/0/0. Text-gap audit: closest pair 149.6 px. The cards whip in from outside the frame inside the instance; a full-frame look of the placed comp (f0–149) shows them uncut once they land.

## Steps
1. Replace the card fills with stills or clips (mask them to the cards) and edit the labels.
2. To pick the left card, swap the outline, badge and tick to x 310 and put the dim keys on Choice 2.

## Pitfalls
- The pick outline was first drawn after the VS badge, and its left edge (x 548) ran through the "S". Draw it before the badge so the badge covers it.
- "VS" popped from 0 gave a `text_too_small` warning (a 17.5 px line while scaling); popping text from 0.6 avoids it.

Inspiration: "this or that" choice games on short-form video. No external text or code was used.
