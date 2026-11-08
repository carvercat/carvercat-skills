# Speech bubble

**Template** `ct_speech_bubble` · Cartoon Bounce pack · **verified 0.1.8.1 (rev 1127; headless, isolated folders, pack added to a scratch user Library)**, comp `CT Speech bubble` in `categories/cartoon-bounce/ct-lab-2`.

A 620 × 320 px white ellipse with an 8 px ink outline, a triangular tail (closed path) and a line of dialogue (ExtraBold 96 px). 90 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Bubble | 0 | Jelly in | width **30.7%**, height **16.2%** overshoot; settles **f21** |
| Bubble tail (drawn first, so it sits behind) | 4 | Pop - wobbly | **30.8%**, settles **f21** |
| Bubble text | 8 | Stamp | **4.6%**, settles **f21** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place and apply; edit the text. Move the tail's three points to aim it at the speaker.

## Pitfalls
- Text in a cartoon pop must not start from 0 (lint `text_too_small`); Stamp starts at 190%.

Inspiration: comic speech balloons. No external text or code was used.
