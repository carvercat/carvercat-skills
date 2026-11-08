# Swinging price tag

**Template** `ct_price_tag` (Library name "Swinging price tag") · Cartoon Bounce pack · **verified 0.1.8.1 (rev 1127; headless, isolated folders, pack added to a scratch user Library)**, comp `CT Price tag` in `categories/cartoon-bounce/ct-lab-3`.

For briefs like "price drop", "sale on toys", "bake sale prices". A sale tag drops in from above its nail and swings to rest, the old price is struck through and the new price stamps on with a small kick. 150 f.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Nail (the pivot; every part is parented to it) | f0–58 | rotation 160° (above the nail) → −38, 21, −10, 4, 0° at f16, 28, 38, 47, 58 (S curve cubic-bezier(0.333, 0, 0.667, 1)): true arcs, smaller each swing | |
| | f76–90 | kick from the stamp: 0 → 4° → 0 | rotation settles **f86** |
| Tag, Tag hole, String | — | parented | |
| Sale "SALE" (ExtraBold 64 px) / Old price "was $14" (Bold 54 px) | f16 / f22 | pop from 60% once the big swing has passed | |
| Strike (red line) | f66–74 | draws across the old price (trim, expo); the old price dims to 55% | trim settles **f71** |
| New price "$9" (ExtraBold 170 px, ink outline) | f76 | stamps from 135%: 112 × 88% squash, 95 × 105%, 102 × 98%, 100% | scale settles **f91**; x·y 0.986–1.0 |

Lint 0 errors, 0 warnings, 6 notes (held keys and `speed_jump` on the stamp, intended). Placed into a fresh comp: lint 0/0/0; the rig survives placement. Text-gap audit: 9 pairs, closest 41.5 px (Sale / Tag hole). Full-frame looks of the placed comp at f80 and f149: nothing cut at rest (the tag starts above the frame by design).

## Steps
1. Change the prices; "$9" at 170 px fits up to about four characters inside the 440 px tag.
2. Keep every new part parented to the Nail, or it will not swing.

## Pitfalls
- With the words on from f0, lint warned `text_overlap` (15–18%) between SALE and the old price at f5, although the words do not touch: lint compares axis-aligned boxes, and two rotated words' boxes overlap while the tag is steep ([KI-156](../references/known-issues.md#ki-156)). The words now pop on at f16 and f22, after the big swing.
- The stamp first started at 190% and covered the old price's box (lint `text_overlap` 47%); 135% clears it.

Inspiration: swinging shop tags in cartoon sales. No external text or code was used.
