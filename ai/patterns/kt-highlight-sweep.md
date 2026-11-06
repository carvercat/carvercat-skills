# Highlight sweep

**Template** `kt_highlight_sweep` · Kinetic Typography pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `KT Highlight sweep` in `categories/kinetic-typography/kt-lab-2`.

A one-line sentence ("Design that actually ships.", ExtraBold 96 px) with a yellow marker that wipes in behind the key word. The sentence is three text objects so the key word can be dark on the marker. 90 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Part 1 "Design that", Part 3 "ships." (off-white) | 0, 6 | Words rise - expo | |
| Highlight (`#FFD23F`, word width + 28 px, 1.1× the font size tall) | 14 | scale X 0 → 1 from its left edge, f14–26, Custom expo | settles **f22** |
| Part 2 "actually" (near-black `#0B0B0F`) | 18 | Words rise - expo | position settles **f29** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place and apply. To change the words, edit `HL_PARTS` in `ai/scripts/motion/kinetic_type_lab2.py` and rebuild: the x positions and the marker width come from `cc.textw` (Rethink Sans advance widths, within about 1% of Carvercat).
2. Editing in place: keep each part's left edge one space width after the previous part's right edge, and resize the Highlight to the new key word.

## Pitfalls
- The key word starts 4 f after the marker, so dark text never shows on the dark background.
- A text object has one fill colour, so per-word colour means separate objects.

Inspiration: the hand-drawn marker emphasis used in explainer and social captions. No external text or code was used.
