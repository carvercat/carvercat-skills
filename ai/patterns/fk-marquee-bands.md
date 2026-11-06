# Marquee bands

**Template** `fk_marquee_bands` (Library name "Marquee bands") · Funky pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FK Marquee bands` in `categories/funky/fk-lab-3`.

For briefs like "scrolling ticker", "crossing tape bands", "marquee of words over the footage". Two slanted bands (pink rising 100 px across the frame, yellow falling 100 px; 170 px tall, ink edge) grow across from opposite sides, and their words scroll in opposite directions at a constant speed. 150 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Band 1 (pink parallelogram, corners exactly on the frame edges) | 0 | grows from the left edge, expo, 12 f | **f8** |
| Band 2 (yellow) | 6 | grows from the right edge | **f14** |
| Words "FRESH •", "FUNKY •", "LOUD •" (ExtraBold 84 px, white, at the band's rotate 2.98° (stored angle −2.98°)) | 0 | linear, one cycle of the copy (the three words' widths) to the left over 150 f; fade in f8–14 | 0%, constant to f149 |
| Words "NEW SOUNDS •", "NEW FACES •" (ink) | 0 | the same, to the right; fade in f14–20 | 0%, constant |

Each word is its own text clip, spaced by its own width plus one space, and each travels exactly one cycle of the copy, so frame 150 lines up with frame 0: drop the fades (or start the loop after f20) and it loops seamlessly. Lint 0/0/0 in the lab and placed. Text-gap audit: closest pair 28.3 px (neighbouring words). Full-frame looks of the placed instance at f20 and f149 show the bands corner to corner and the words cut only by the frame edge, as intended ([KI-144](../references/known-issues.md#ki-144)).

## Steps
1. Change the words in `MQ` in `funky_lab3.py` and rebuild: the spacing and the loop distance are measured from the text (`cc.textw`).
2. Over footage, keep the bands; their ink edge separates them from the picture.

## Pitfalls
- One long text per band ("FRESH • FUNKY • LOUD •" four times) needs 150 f of reading time for 85 characters, and a unit that only crosses part of the frame was reported `reading_time` (32 of 34 frames). Short per-word clips each need only 25 f.
- A word that is on screen only while it is still transparent (before the fade) is a lint **error** `never_visible`. The lab script keeps only words that are on screen at some point after the fade.
- A band as a rotated rectangle would run past the frame at rest; the parallelogram path ends exactly on the frame edges.

Inspiration: scrolling marquee tape and caution-tape graphics. No external text or code was used.
