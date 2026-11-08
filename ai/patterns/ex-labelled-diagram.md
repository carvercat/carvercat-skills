# Labelled diagram

**Template** `ex_labelled_diagram` (Library name "Labelled diagram") · Explainer pack · **verified 0.1.8.1 (rev 1127; `ai/scripts/motion/verify_pack.py`: placed in a fresh 16:9 and a fresh 9:16 comp, lint 0/0/0, qc no flash; against the v1 original the silhouette differs by at most 0.00 % of pixels over 7 frames; object-level check pass)**, comp `EX Labelled diagram` in `categories/explainer/ex-lab-3`.

For briefs like "anatomy of", "what's inside", "the parts of a product". An object in the centre with four labels, one after another: a dot pops on the part, a leader line draws out to the side, the label and a note step in. The pointer callout points at one thing; this one annotates a whole object. Light background included. 165 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Title "Inside the phone" (56 px ExtraBold) | 0 | Step in | |
| Phone body (300 × 720, vertical gradient #1F2333 → #48517A, soft shadow) | 2 | scale 0.92 → 1 (expo), fade 8 f | settles **f12** |
| Screen (vertical gradient #E6ECFD → white), camera dot, button | 8 / 10 / 12 | fade, pop, pop | |
| Battery outline (dashed blue) | 14 | Trim end 0 → 1, 14 f | done **f28** |
| Label 1 Camera (left), 2 Power button (right), 3 Screen (left), 4 Battery (right) | 34 / 56 / 78 / 100 | dot pops (8 f, 9.3%), leader draws (f+2, 12 f), label (f+10) and note (f+14, 30 px muted) step in | label 4 settles **f119** |

Lab comp lint on 0.1.8.1 (native size): 0 errors, 0 warnings, 1 notes. `inspect qc` (240 px): no flashes, a freeze after the last label (the hold). Placed into a fresh comp: lint 0/0/0. Text-gap audit: 126 pairs, closest 20.0 px (a label to its own leader line; the label and its note were 10.1 px apart in the first build and moved to 56 px spacing). Both gradients were checked in a full-frame look (dark at the top of the body, light at the top of the screen, as written). Full-frame looks of the placed comp at f62 and f164: nothing cut.

## Steps
1. Put the product's own image (a PNG on a track below) in place of the phone shapes, move the four `parts` points onto its features and edit the texts; labels on the left end at x 715, on the right start at x 1225.
2. For more than four labels, keep them in reading order, alternate sides and keep 100 px or more between labels on one side.

## Pitfalls
- Gradients on the body and screen are written in comp pixels (y down) through \`Obj.gradient()\`, which takes rect and ellipse endpoints in comp pixels; the look at f164 confirmed the direction (a wrong one would show a light top on the body).
- Label and note at 46 px apart were 10 px (text-gap audit); 56 px keeps 20 px or more.

Inspiration: common explainer and product-diagram conventions. No external text or code was used.
