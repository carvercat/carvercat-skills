# Poster lockup

**Template** `kt_poster_lockup` (Library name "Poster lockup") · Kinetic Typography pack · **verified 0.1.8.1 (rev 1127; `ai/scripts/motion/verify_pack.py`: placed in a fresh 16:9 and a fresh 9:16 comp, lint 0/0/0, qc no flash; against the v1 original the silhouette differs by at most 0.00 % of pixels over 7 frames; object-level check pass)**, comp `KT Poster lockup` in `categories/kinetic-typography/kt-lab-3`.

For briefs like "event announcement", "festival poster", "a title card with a date and a place, no images". Four lines ("NEW TYPE / FESTIVAL / LISBON / MAY 12–14", ExtraBold) are each sized so their ink is exactly 1000 px wide: a justified block, with 34 px between cap boxes. They slide in from alternate sides. 120 f, holds.

Frames are comp frames.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Line 1–4 (off-white, off-white, accent, `#FFD23F`) | 0, 5, 10, 15 | from 240 px left / right / left / right, 18 f (expo), fade 5 f | settle **f12, f17, f22, f27**; 0% overshoot |

Sizes from measured ink (100 px measure texts, scaled): 217, 242, 301 and 200 px. Lab comp lint on 0.1.8.1 (native size): 0 errors, 3 warnings, 0 notes (`text_overlap` between neighbouring text boxes at single frames while the parts move; the v1 lab linted 0 warnings on the same build, not yet traced). Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (34.0 px, the designed gap).

## Steps
1. Edit `LOCKUP` in `ai/scripts/motion/kinetic_type_lab3.py` and rebuild. Pass 1 measures each line at 100 px with `carvercat_authoring mode:geometry`; pass 2 sizes it to `LOCKUP_W` and stacks the cap boxes `LOCKUP_GAP` apart around the frame centre.
2. Pick lines of similar length (6–9 characters). A 4-letter line comes out over 350 px tall and takes the whole frame.
3. Editing a placed instance by hand: change the text, then resize until its width matches the others. Measure the width with geometry; do not judge it by eye.

## Pitfalls
- **Justify on measured bounds, not advance widths.** Carvercat's bounds are 3–5% narrower than `cc.textw` advances, and by a different amount per line (NEW TYPE 0.961, LOOK 0.952, "It isn't luck." 0.970), so lines sized from advances would end 10–20 px apart at the right edge.
- Capitals-only lines centre their cap box on the text's y (measured: within 1.5 px; bounds start exactly at the text's x), so the stack is computed from cap heights alone.

Inspiration: Swiss-style justified type posters. No external text or code was used.
