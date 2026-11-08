# POV hook (9:16)

**Template** `ss_pov_hook` (Library name "POV hook (9:16)") · Social Short-form pack · **verified 0.1.8.1 (rev 1127)**, comp `SS POV hook` in `categories/social-media-reels/ss-lab-3`.

**Measured on 0.1.8.1 (rev 1127, harness `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0, no flashes; against the v1 original the worst silhouette difference is 0.00 % (limit 2 %) and every object is present with the same text (box offset at most 0.3 px); colours are now the exact hex the page states (mean shift 1.4 of 255, intended). The frame numbers in the table above are the keys of the generator (`design units`), unchanged.


For briefs like "open with a POV line", "a relatable text hook", "native-looking on-screen text". A pink "POV:" plate, then two lines in black on white plates sized to each line, in the upper third like the platforms' own text tool. 90 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| POV plate and "POV:" (ExtraBold 72 px, white on pink) | 0 | pop 0.4 → 1, back curve, 8 f | **9.3% overshoot**, settles **f8** |
| Line plate 1 + line 1 (Bold 64 px, black on white, r 20) | 6 | Hook punch from 1.15 (as keys) | **f13** |
| Line plate 2 + line 2 | 10 | Hook punch from 1.15 | **f17** |

Plates are sized with `cc.textw` (advance width + 60 px). Lint 0/0/0. `bounds_inside` passed for every object. Placed into a fresh 1080 × 1920 comp: lint 0/0/0. Text-gap audit: closest pair 47.1 px (line 1 / line 2).

## Steps
1. Change `POV_LINES` in `ai/scripts/motion/social_short_form_lab3.py` and rebuild so the plates follow the text; or edit the text after placing and set each plate's width to the line's width + 60 px.
2. Keep each line under about 800 px (19 characters at 64 px); split longer hooks into a third line 106 px lower.
3. Reading time: 35 characters need 62 f opaque; the 90 f template gives 73.

## Pitfalls
- A plate and its text share the same keys and centre, so they scale together; if you move one, move the other.
- The plates are 96 px tall on a 106 px pitch, so only 10 px separate them at rest. The punch starts at 1.15 rather than the preset's 1.25 to keep the overlap small while line 2 scales in over line 1.

Inspiration: the native text-plate style of short-form apps and the "POV:" hook format. No external text or code was used.
