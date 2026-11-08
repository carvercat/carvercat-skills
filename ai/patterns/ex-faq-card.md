# FAQ card

**Template** `ex_faq_card` (Library name "FAQ card") · Explainer pack · **verified 0.1.8.1 (rev 1127; `ai/scripts/motion/verify_pack.py`: placed in a fresh 16:9 and a fresh 9:16 comp, lint 0/0/0, qc no flash; against the v1 original the silhouette differs by at most 0.00 % of pixels over 7 frames; object-level check pass)**, comp `EX FAQ card` in `categories/explainer/ex-lab-3`.

For briefs like "common questions", support and help videos, product Q and A. Three question rows; one opens like an accordion and shows its answer while the rows below make room. The quiz asks and reveals one answer; this lists several questions. Light background included. 165 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Title "Questions people ask" (64 px ExtraBold) | 0 | Step in | |
| Rows 1–3 (1200 × 120, white; row 1 has a blue stroke), Q badge (84 px), question (42 px Bold), chevron | 6 / 14 / 22 | Step in (row, then badge, question and chevron 4 f later) | row 2 opaque **f21** |
| Answer panel (tinted, under row 1) | 40 | scale Y 0 → 1 anchored at its top (expo), grows 210 px | settles **f52** |
| Row 1 chevron | 44 | rotation 0 → 180° (S curve cubic-bezier(0.333, 0, 0.667, 1), 14 f) | settles **f58** |
| Rows 2–3 with their badge, question, chevron | 44 | slide down 210 px (expo, 14 f) | settle **f53** |
| Answer text (36 px, two lines) | 52 | Step in | settles **f61** |

Lab comp lint on 0.1.8.1 (native size): 0 errors, 0 warnings, 20 notes. `inspect qc` (240 px): no flashes, a freeze after f61 (the answer is read). Placed into a fresh comp: lint 0/0/0. Text-gap audit: 52 pairs, closest 60.1 px (Q letter / question). Text bounds: questions end at x 912 of the 1200 px row (right edge 1560), the answer sits inside its panel. Full-frame looks of the placed comp at f50 (panel half open) and f164: nothing cut.

## Steps
1. Edit the questions and the answer in `faq()`; the answer panel is 210 px tall (two lines of 36 px).
2. To open a different row, move `shift` to the rows below it and the panel under it.

## Pitfalls
- Position keys that start before a clip's first frame are a lint error (`key_outside_clip`, "position key at clip frame -2"): the Q letter and chevron start 2 f after their row, so their keys start there.
- A 60 px badge with the letter inside was reported by the text-gap audit as a text/shape overlap (−40.7 px); at 84 px (over the audit's 80 px limit for "small shapes") it is not, and the Q reads better.
- The panel grows with scale Y, so its corner radius squashes for about 8 f while it opens; it sits behind row 1, which hides its top corners.

Inspiration: common explainer-video conventions (FAQ accordions). No external text or code was used.
