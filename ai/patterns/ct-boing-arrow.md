# Boing arrow

**Template** `ct_boing_arrow` (Library name "Boing arrow") · Cartoon Bounce pack · **verified 0.1.8.1 (rev 1127; headless, isolated folders, pack added to a scratch user Library)**, comp `CT Boing arrow` in `categories/cartoon-bounce/ct-lab-3`.

For briefs like "tap here", "look at this", "click the button" in a kids' or playful tutorial. A label pops, a curved hand-drawn arrow draws toward a button, boings at it, and the button squashes from the poke. 90 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Arrow label "Tap here!" (ExtraBold 72 px) | 0 | pops from 60% | settles **f15** |
| Arrow shaft (curved path, 14 px, round caps) | 0 | draws f6–22 (trim end, expo) | trim settles **f16** |
| Arrow head (chevron along the end tangent) | 18 | fades in f18–20 | |
| Arrow tail (the pivot: an ink dot at the tail) | 0 | boing: 110 × 92% (f26), 95 × 105%, 103 × 97%, 100% (f41) | settles **f41**; x·y 0.997–1.012 |
| Target (green button) / Target label "GO!" | 0 | pop f0–14; poked: 86 × 114% (f28), 106 × 95%, 98 × 102%, 100% (f40) | scale settles **f39**; x·y 0.98–1.012 |

Lint 0 errors, 0 warnings, 5 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 5 pairs, closest 36 px (Arrow label / Arrow tail). Full-frame looks of the placed comp at f27 and f89: nothing cut.

## Steps
1. Change the label and the button text; move the button with `bxp, byp` and the arrow with `ax, ay, tx, ty` and the end handle `hin` (the head follows the end tangent).
2. Point it at a real UI element by replacing the Target with nothing and keeping the poke on the element.

## Pitfalls
- A scale on a rig is axis-aligned, so the boing stretches x and squashes y; it reads along this mostly horizontal arrow. For a steep arrow, stretch y instead.
- "GO!" popping with the button from 0 read `text_too_small` at f1 (14.8 px); it starts at 60% and fades in from f3, after the button has grown past it.

Inspiration: hand-drawn pointer arrows in tutorials. No external text or code was used.
