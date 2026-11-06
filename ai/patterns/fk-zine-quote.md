# Zine quote

**Template** `fk_zine_quote` (Library name "Zine quote") · Funky pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FK Zine quote` in `categories/funky/fk-lab-3`.

For briefs like "a quote, but loud", "DIY / zine look", "fan testimonial". Six words, each on its own tilted paper plate in a different colour, weight and size (110–150 px), slap in one after another; a tape strip and the credit follow. 150 f, holds. The quote is invented.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Words 1–6 and their plates | 4, 10, … 34 (6 f apart) | stamp 1.4 → 1 with an 8° turn (alternating sides) into −5°…+4°, 8 f | **9.3%**; **f12** to **f42** |
| Tape (translucent yellow, +20°) | 46 | stamp 1.3 → 1 | **9.3%**, **f54** |
| Credit (Bold 42 px, ink) | 48 | rise 24 px | **f55** |

Lint 0/0/0 in the lab and placed. Text-gap audit: closest pair 90.3 px. Full-frame look of the placed instance at f149: nothing cut.

## Steps
1. Edit `ZINE` (two lines of word, size, weight, text colour, plate colour) in `funky_lab3.py`; each plate is `cc.textw` + 56 px, and each line is centred.
2. Keep each word under about 8 letters: a word is its own clip, and lint wants 25 opaque frames each, which the 150 f hold covers easily.

## Pitfalls
- The tape first sat over the credit's dash; it is now 90 px left of the credit's left edge.
- The credit is ink: keep a light ground.

Inspiration: cut-out lettering in punk zines and collage posters. No external text or code was used.
