# Lesson title card

**Template** `ct_lesson_title` (Library name "Lesson title card") · Cartoon Bounce pack · **verified 0.1.8.1 (rev 1127; headless, isolated folders, pack added to a scratch user Library)**, comp `CT Lesson title` in `categories/cartoon-bounce/ct-lab-3`.

For briefs like "kids' lesson 3", "episode title", "today we learn...". A blue card drops and lands on its bottom edge, a LESSON badge jellies in, the title's letters drop and bounce, a star pops and the subtitle rises. 150 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Card (1320 × 520, anchor at the bottom edge) | 0 | falls from above (accelerating arrival cubic-bezier(0.333, 0, 0.667, 0.333)), stretched 93 × 107%; lands **f14**; 112 × 86% at f15, 96 × 104%, 102 × 98%, 100% | scale settles **f27**; x·y 0.963–1.0 |
| Card shadow | 0 | grows and darkens with the fall | |
| Badge + Badge text "LESSON 3" (tilted 6°) | 22 | jelly 0 → 112 × 90% → 94 × 106% → 102 × 98% → 100% | settles **f38**; x·y 0.996–1.008 |
| Title "Why do cats purr?" (ExtraBold 116 px, white, ink outline) | 26 | Stagger Text by character, 2 f apart: each letter drops 12% H (129.6 px) and bounces (baked) | last letter lands **f74** (looks at f66, 70, 74) |
| Star | 36 | pop 0 → 125 → 92 → 103 → 100%, rotation −40 → 12 → −5 → 0° | settles **f55** |
| Subtitle (Bold 48 px) | 62 | rises 24 px, fades in | settles **f75** |

Lint 0 errors, 0 warnings, 2 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 3 pairs, closest 56 px (Title / Subtitle). Full-frame looks of the placed comp at f15 (the widest squash) and f149: nothing cut.

## Steps
1. Change the lesson number and the title; up to about 20 characters fit at 116 px inside the card.
2. A longer title delays the last letter by 2 f per character; keep at least 25 f of hold after it (reading time).

## Pitfalls
- The letters cannot squash one by one ([KI-134](../references/known-issues.md#ki-134)); the card does the squashing and the letters bounce.
- The card squashes from its bottom edge; with a centred anchor it would lift off its shadow.

Inspiration: kids' TV lesson and episode cards. No external text or code was used.
