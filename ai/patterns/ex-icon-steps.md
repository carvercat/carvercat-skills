# Icon steps

**Template** `ex_icon_steps` (Library name "Icon steps") · Explainer pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `EX Icon steps` in `categories/explainer/ex-lab-3`.

For briefs like "how it works in three steps", onboarding, "upload, customise, share". Three cards, each with an icon that draws itself. Process steps uses numbered circles and no icons; icon grid shows six items at once with no order. Light background included. 150 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Step cards 1–3 (440 × 580, white, soft shadow) | 0 / 34 / 68 | Step in | settle **f13**, **f43**, **f77** |
| Icon tiles (176 px, tinted) | card + 4 | pop 0 → 100% (keyed back) | overshoot **9.8%**, tile 2 settles **f49** |
| Icons: upload (shaft, head, tray), sliders (3 lines, 3 knobs), share (2 lines, 3 nodes) | card + 12 | lines trim 0 → 1 (8–10 f, 3 f apart), knobs and nodes pop | upload head done **f23** |
| STEP tag, title (52 px ExtraBold), two-line text (32 px) | card + 14 / 18 / 22 | Step in | title 3 settles **f95** |
| Arrows between cards | 24 / 58 | Trim end (10 f) and a head | |

Lint (with `contrast:true`) 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 162 pairs, closest 35.0 px (STEP tag / title). Text bounds against the cards: at least 95 px side margin. Full-frame looks of the placed comp at f56 and f149: nothing cut.

## Steps
1. Edit titles and texts in `icon_steps()`; swap an icon by replacing its few `mark()` lines (each icon is 3–5 lines and dots in a 176 px tile).
2. Keep step texts to two lines of about 20 characters (32 px, inside 380 px).

## Pitfalls
- The tile tints and icon strokes use the accent colours; the tags use the same accents as text and pass 4.5:1 on white (blue 6.0, coral 5.9, green 5.4). The pack's old coral and green did not (2.9–4.3).
- Arrows are drawn with their head centred on the line end; end the line 36 px short of the next card.

Inspiration: common explainer-video conventions (three-step icon cards). No external text or code was used.
