# Kinetic quote

**Template** `kt_quote` (Library name "Kinetic quote"; the bundled essentials already have a "Quote card") · Kinetic Typography pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `KT Quote` in `categories/kinetic-typography/kt-lab-2`.

A large accent quotation mark, a two-line quote (ExtraBold 84 px, line spacing 1.1) and an attribution, left-aligned at x 400. 150 f (5 s), holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Quote mark ("“", ExtraBold 320 px, `#FF4D2E`) | 0 | Stamp | **4.6% overshoot, settles f13** |
| Quote (9 words) | 8 | Words rise - expo (3 f per word) | first word settles **f19**; the last lands about f48 |
| Attribution ("Head of video, Northwind", Medium 38 px, muted) | 46 | Lines slide in - left | settles **f62** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0. The quote is fully readable from about f48, which leaves 100 f (3.3 s) of hold; at the usual 3–4 words a second that suits quotes of up to about 12 words.

## Steps
1. Place and apply. Edit the quote (a line break is a newline in the text) and the attribution.
2. Longer quotes: lengthen every clip; start the attribution once the last word has landed (start + 3 f × words + 16 f).

## Pitfalls
- A pop from 0 on the quote mark failed lint: `text_too_small` ("a line is 7.0 px tall"). Stamp starts large (1.9×) and slams down instead.
- The attribution first started at f34, while the quote was still rising. It now waits for the last word.

Inspiration: testimonial cards in product and brand films. No external text or code was used.
