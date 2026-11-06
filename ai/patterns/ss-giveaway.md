# Giveaway rules (9:16)

**Template** `ss_giveaway` (Library name "Giveaway rules (9:16)") · Social Short-form pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SS Giveaway` in `categories/social-media-reels/ss-lab-3`.

For briefs like "announce a giveaway", "how to enter", "contest rules". GIVEAWAY, the prize, three numbered entry steps that get ticked, the closing date and a not-sponsored line. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Title GIVEAWAY (ExtraBold 130 px, yellow) | 0 | Hook punch (as keys) | **f7** |
| Prize (Bold 56 px) | 6 | Hook punch | **f13** |
| Rule badges 1–3 (84 px, pink) | 16, 26, 36 | pop, back curve | **9.7% overshoot**, **f26 / f36 / f46** |
| Rule numbers | badge + 2 | fade 3 f | last **f41** |
| Rules (Bold 52 px, x 245) | badge + 3 | 20 px rise, expo, fade 3 f | **f26 / f36 / f46** |
| Rule ticks (yellow 10 px, x 830) | 54, 60, 66 | trimEnd 0% → 100%, 8 f, expo | **f59**, …, **f71** |
| Closing line (Medium 42 px, y 1060), disclaimer (Medium 36 px, muted, y 1122) | 60, 66 | Hook punch; fade 6 f | **f67**, **f72** |

Lint 0/0/0. `bounds_inside` passed for every object; everything ends above y 1151, so the button column is never reached. Placed into a fresh 1080 × 1920 comp: lint 0/0/0. Text-gap audit: closest pair 25.5 px (closing line / disclaimer).

## Steps
1. Edit `RULES` (or the texts after placing). A rule up to about 18 characters at 52 px ends before the ticks at x 800.
2. Keep a closing date and a line saying the platform does not sponsor the giveaway; check the platform's current promotion rules for the exact wording.

## Pitfalls
- The first build whipped the rules in from the left; while moving they ran over the number badges. A short rise keeps each rule beside its badge.
- The two small lines at the bottom are 42 and 36 px: lint passes them, but they are the smallest text in the pack; do not go lower on a phone.

Inspiration: giveaway announcement posts on social. No external text or code was used.
