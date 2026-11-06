# Touchdown burst

**Template** `sp_touchdown_burst` (Library name "Touchdown burst") · Sports pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SP Touchdown burst` in `categories/sports/sp-lab-3`.

For briefs like "touchdown", "try", "home run", "big score celebration". Two sunbursts turn behind a TOUCHDOWN! slam, a shock ring runs out and 28 confetti pieces are thrown and fall; a score strip slashes in underneath. 90 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Sunburst 1 (red, 90%) and 2 (blue, 55%) | 0 | scale 0 → 230% / 150% (overshooting ease, 12 f); rotate 30° and −25° over the clip (stored values) (one way, constant) | scale settles **f13**, **9.8% overshoot** |
| Shock ring (white, 14 px stroke) | 6 | scale 0.3 → 3.4 (decelerating), fade 1 → 0, f6–32 | |
| TOUCHDOWN! (190 px yellow, dark outline 6%) | 6 | Impact slam: 220% → 92% → 100% | opacity **f8**, scale settles **f13**, **6.7%** past the impact |
| Confetti 1–28 (16 × 28 px, yellow, white, blue, red) | 11 | thrown from the centre at 26–42 px/f with 6% air drag per frame and gravity 0.55 px/f², spinning one way; position and rotation baked every 2 f; fade out the last 14 f | gone **f76** |
| Score strip (slanted, dark, 100 px) + line (56 px white) | 22 / 25 | Slash in | strip settles **f29** |

Lint (with `contrast:true`) 0 errors, 0 warnings, 28 notes (`repeated_key_value`, the confetti's opacity hold; intended). `inspect qc` (240 px): no flashes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 1 pair, 190.7 px (TOUCHDOWN! / score line). Full-frame looks of the placed comp at f12 (ring at its widest, the slam still above 100%), f40 and f89: the slam crops at the frame edge only while it is above 100%; at rest the word is 1270 px wide.

## Steps
1. Change the word and score in `touchdown()`; for a longer word keep 190 px × letters under about 1700 px.
2. Confetti: `range(28)`, speed, drag and gravity are in the loop; the same seed gives the same burst. Change the colour list to the teams'.

## Pitfalls
- The sunbursts turn the whole time, so their cropped rays never sit still at rest (a cropped shape at rest reads as a mistake).
- The confetti are rectangles on baked Linear keys every 2 f; `inspect curves` overshoot on baked lanes is meaningless ([KI-152](../references/known-issues.md#ki-152)). The slam's 6.7% is the keyed peak.
- Outline the big word: yellow on red and blue rays is unreadable without the dark outline (`text.outline` Paint solid, thickness 0.06, outside only).

Inspiration: common broadcast sports graphics conventions. No external text or code was used. Teams, players and leagues are invented.
