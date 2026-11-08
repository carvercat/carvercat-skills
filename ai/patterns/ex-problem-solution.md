# Problem and solution

**Template** `ex_problem_solution` (Library name "Problem and solution") · Explainer pack · **verified 0.1.8.1 (rev 1127; `ai/scripts/motion/verify_pack.py`: placed in a fresh 16:9 and a fresh 9:16 comp, lint 0/0/0, qc no flash; against the v1 original the silhouette differs by at most 0.00 % of pixels over 7 frames; object-level check pass)**, comp `EX Problem solution` in `categories/explainer/ex-lab-3`.

For briefs like "the old way hurts, here is the fix", pitch and pain-point films, before/after stories. A pink PROBLEM half with three crossed items is answered by a green SOLUTION half that wipes in from the centre with three ticked items. Compare columns is a quiet side by side; this is a pitch with a turning point. Light background included (the halves are full-height tints over it). 150 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Problem panel (960 × 1080, tint) | 0 | static | |
| PROBLEM pill (coral, white 32 px) and headline "Reports take hours" (84 px ExtraBold) | 4 / 10 | Step in | |
| Crossed items 1–3 (38 px) | 26 / 36 / 46 | cross draws (8 f), text steps in 2 f later | |
| Divider disc (120 px) and arrow | 48 / 52 | disc pops, arrow draws (8 f) and its head pops | disc overshoot **9.8%**, settles **f59** |
| Solution panel (tint) | 56 | scale X 0 → 1 anchored at the centre line (expo, 20 f) | settles **f69** |
| SOLUTION pill (green) and headline "One click, ready in seconds" | 72 / 78 | Step in | headline settles **f87** |
| Ticked items 1–3 | 94 / 104 / 114 | tick draws (10 f), text steps in | last settles **f129** |

Lab comp lint on 0.1.8.1 (native size): 0 errors, 0 warnings, 1 notes. `inspect qc` (240 px): no flashes, a freeze after f129. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 155 pairs, closest 30.0 px (item 3 / its tick). Text bounds: pill tags are 39 and 41 px inside their pills, headlines end at x 589 and x 1709, items at x 650 and x 1533. Full-frame looks of the placed comp at f66 (wipe under way) and f149: nothing cut.

## Steps
1. Edit the two headlines and six items in `problem_solution()`; keep headlines under 740 px at 84 px (the script raises if not).
2. Put the "solved" footage or UI on the green half after f76 by placing it above the template.

## Pitfalls
- White on the pack's old coral (#FF6B5B) measured 2.9:1. A white 28 px tag on #C93A28 still read 3.77:1 at one frame and 32 px gave 4.43:1 (thin antialiased glyphs); the pill is now #B93222 (5.9:1 nominal) with 32 px tags, and the green is #17794A (5.4:1).
- Tracking 1.6 on the tags was wider than their pills (the first and last letters fell on the tint, 1.01:1 in lint); tracking 1.07 fits ([KI-157](../references/known-issues.md#ki-157) is the same gap: lint does not compare text with its plate).
- Line spacing 1.1 on 84 px headlines rendered a 1.46 em pitch; 0.9 gives about 1.2 em.

Inspiration: common explainer-video conventions (problem and solution splits). No external text or code was used.
