# Poll sticker (9:16)

**Template** `ss_poll` (Library name "Poll sticker (9:16)") · Social Short-form pack · **verified 0.1.8.1 (rev 1127)**, comp `SS Poll` in `categories/social-media-reels/ss-lab-2`.

**Measured on 0.1.8.1 (rev 1127, harness `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0, no flashes; against the v1 original the worst silhouette difference is 0.00 % (limit 2 %) and every object is present with the same text (box offset at most 1.9 px); colours are now the exact hex the page states (mean shift 2.4 of 255, intended). The frame numbers in the table above are the keys of the generator (`design units`), unchanged.


An 820 × 560 px white card with a question (ExtraBold 64 px) and two answer bars (700 × 110 px tracks) that fill to their results, 62% pink and 38% purple, with percentages. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Poll card | 0 | Hook punch | |
| Question | 4 | Caption words pop | |
| Track 1–2 | 10 | Hook punch | |
| Bar 1–2 (transformOrigin "0% 50%", the left edge) | 30, 36 | scale X 0 → 1, 18 f, expo | settle **f42 / f48** |
| Option 1–2 (Bold 48 px, white) | bar + 6 | Hook punch | |
| Percent 1–2 (ExtraBold 48 px) | bar + 14 | Hook punch | Percent 2 settles **f57** |

Lint 0 errors, 0 warnings. `bounds_inside` the safe box [61, 268, 955, 1270] passed for every object. Placed into a fresh 1080 × 1920 comp (`comp.format`): applied at 1080 × 1920, lint 0/0/0.

## Steps
1. Place and apply. Edit the question and options; set each Bar's width to result × 700 px (left edge stays at x 190) and the percentages.

## Pitfalls
- The option labels are white on the bar, so they wait for it. In the first build they started at f14 and were invisible on the light track until the bars arrived.

Inspiration: poll stickers in stories. No external text or code was used.
