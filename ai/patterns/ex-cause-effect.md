# Cause and effect

**Template** `ex_cause_effect` (Library name "Cause and effect") · Explainer pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `EX Cause effect` in `categories/explainer/ex-lab-3`.

For briefs like "why prices rise", "how one event leads to another", "what happens next". Unlike the flow diagram (a straight line of three boxes) this chain **branches**: one cause card, two effect cards and one result, joined by drawn elbow arrows. Light background included. 150 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Column tags CAUSE / EFFECT / RESULT (30 px Bold, tracking 1.07; blue, coral, green) | 0 / 30 / 60 | Step in | |
| Cause card (white, 6 px blue stroke) and "Prices rise" (56 px ExtraBold) | 4 / 8 | Step in | card settles **f13** |
| Cause links 1–2 (6 px, round corners) and heads | 24 | Trim end 0 → 1 (expo, 12 f); each head pops (8 f) as its line arrives | lines done **f36** |
| Effect cards 1–2 and two-line text | 34 / 42 (text +4) | Step in | settle **f43**, **f51** |
| Result links 1–2 | 58 | Trim end, 12 f; one shared head | done **f70** |
| Result card, "Sales fall" (60 px), note (32 px) | 68 / 72 / 80 | Step in | card settles **f77**, text **f81** |
| Emphasis on the outcome | 96 | scale 1 → 1.05 → 1 on card, text and note, once | back to 100% at **f112** |

Heads pop 9.8% (a keyed back ease); every move is baked as keys, there are no presets to apply. Lint (with `contrast:true`) 0 errors, 0 warnings, 0 notes. Nominal text contrast: ink 14.6:1, muted 6.2:1, accents on the ground 5.1–5.7:1. Placed into a fresh comp: lint 0/0/0 (also with `contrast:true`). Text-gap audit: 52 pairs, closest 41.8 px (Result text / note). Text bounds against each card (`carvercat_authoring geometry`): at least 97 px of side margin. Full-frame looks of the placed comp at f62 (links drawing), f100 (pulse) and f149: nothing cut.

## Steps
1. Edit the card texts in `cause_effect()`; keep each line under 360 px at its size (the script raises if it does not fit).
2. For one effect instead of two, delete effect card 2 and its two links; for three, add a third row at y 835 and move the cards 100 px up.

## Pitfalls
- Both cause links need their own head (they end on different cards); the two result links end on the same point, so only the first has a head. A second head on the same tip draws a double arrow.
- Line spacing 1.2 rendered a 1.6 em pitch (the value multiplies the font's own leading): two-line card texts use 0.95.

Inspiration: common explainer-video conventions (cause-and-effect diagrams). No external text or code was used.
