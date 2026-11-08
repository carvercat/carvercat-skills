# Split title

**Template** `kt_split_title` · Kinetic Typography pack · **verified 0.1.8.1 (rev 1127; `ai/scripts/motion/verify_pack.py`: placed in a fresh 16:9 and a fresh 9:16 comp, lint 0/0/0, qc no flash; against the v1 original the silhouette differs by at most 0.00 % of pixels over 7 frames; object-level check pass)**, comp `KT Split title` in `categories/kinetic-typography/kt-lab-2`.

Two centred lines that arrive from opposite sides: "MAKE IT" (off-white) from the left and "MOVE" (accent) from the right, ExtraBold 190 px, then a yellow full stop. 90 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Line 1 (y 450) | 0 | position −360 px → 0, 16 f, Custom expo; opacity 0 → 1 in 4 f | settles **f10** |
| Line 2 (y 650) | 4 | position +360 px → 0, 16 f, expo; opacity in 4 f | settles **f14** |
| Dot (36 px ellipse, `#FFD23F`, after line 2) | 18 | Pop - spring | **16.2% overshoot, settles f38** |

Lab comp lint on 0.1.8.1 (native size): 0 errors, 1 warnings, 0 notes (`text_overlap` between neighbouring text boxes at single frames while the parts move; the v1 lab linted 0 warnings on the same build, not yet traced). Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place and apply. Edit both lines. The dot's x is set from the measured width of "MOVE" (`cc.textw`); move it if you change line 2, or delete it.
2. Exit: Exit zoom through or a transition from the transitions pack.

## Pitfalls
- The 4 f offset matters: both lines landing on the same frame reads as one block, not two hits.

Inspiration: opposing-direction title builds common in promo edits. No external text or code was used.
