# Light sweep

**Template** `ml_light_sweep` · Minimal Luxury pack · **Verified 0.1.8.1 (rev 1127)**, comp `ML Light sweep` in `categories/minimal-luxury/ml-lab-2`.

A gold wordmark ("ELAN", 220 px, tracking 1.4) with an ivory gleam that crosses it letter by letter. 120 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Gold fill (1000×320 px rectangle, gradient gold / ivory band / gold) | 0 | Slow fade in; gradient start −0.6 → 0.6 and end 0.4 → 1.6 (object-local), f30–110, S curve cubic-bezier(0.333, 0, 0.667, 1), the curve arriving at the key | size settles **f28**; gradient settles **f102** |
| Wordmark (the mask) | 0 | none | |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0. No overshoot (the pack's style rule).

How it is built: the **text is the mask** and the gold rectangle its target (`property.set {id:"rectangle", key:"mask", value:{"ref":"<text id>"}}`, then `parent.clear {ids:[text, rectangle]}`). So the letters show the rectangle's moving gradient. The band is 24% of the fill's width (stops 0.38 / 0.5 / 0.62) and its centre travels from −0.1 to 1.1 of the width.

## Steps
1. Place and apply. Edit the text; keep the Gold fill wider than the word.
2. A second gleam: add two more keys later in the clip (back to −0.6/0.4 on a Hold, then across again). Space gleams 2–3 s apart.

## Pitfalls
- Text gradient endpoints are not live ([KI-009](../references/known-issues.md#ki-009) c), so a text cannot carry the sweep itself. Shape gradient endpoints are live.
- The first build used a second, identical text as the mask of a soft band. Lint flagged `text_overlap` (100%), because it does not see masks ([KI-133](../references/known-issues.md#ki-133)). With one text as the mask there is nothing to overlap.
- The first timing (f36–86, band 12%) crossed the letters in about 10 frames and was hard to see. f30–110 with a 24% band reads letter by letter.

Inspiration: the sheen pass over metal logos in jewellery and watch films. No external text or code was used.
