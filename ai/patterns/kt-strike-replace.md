# Strike and replace

**Template** `kt_strike_replace` (Library name "Strike and replace") · Kinetic Typography pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `KT Strike and replace` in `categories/kinetic-typography/kt-lab-3`.

For briefs like "myth vs fact", "we changed", "it's not X, it's Y", "rebrand". A claim ("It isn't luck.", ExtraBold 110 px) rises in. A red line strikes through the wrong word and the whole claim steps back to a dim grey. Then the answer lands below it: "It's" slams in, and "practice." rises beside it in accent. 120 f, holds.

Frames are comp frames.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Claim | 0 | rise 24 px, 14 f (expo), fade 5 f | settles **f9** |
| Strike (12 px, accent, through the x-height of "luck") | 34 | Trim Stroke end 0 → 1, 10 f (expo) | settles **f41** |
| Claim dims | f42–52 | Colour `#F4F1EA` → `#6F6B64` | settles **f52** |
| "It's" | 54 | scale 1.3 → 1, 8 f (expo), no fade | settles **f59** |
| "practice." (accent) | 59 | rise 40 px, 12 f (expo), fade 5 f | settles **f67** |

Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (40.2 px).

## Steps
1. Edit `STRIKE` (claim, struck word, size) in `ai/scripts/motion/kinetic_type_lab3.py` and rebuild. The strike is measured from the ink: the right edge of the claim up to the struck word's first letter, minus that letter's width, and the x-height centre of "uc".
2. The claim needs its reading time before the strike: 34 f covers about 19 characters without spaces.

## Pitfalls
- **A slam grows into its neighbour.** The first version slammed both answer words from 1.3. Lint reported `text_overlap` (17%) between them during the entrance. The key word now rises instead.
- The strike first overhung the word by 12 px on the left and touched the "t" before it. It now overhangs 4 px left and 10 px right.
- Colour is keyframeable on `text.fill`, so the claim dims in place; no second text is needed.

Inspiration: correction and myth-busting captions. No external text or code was used.
