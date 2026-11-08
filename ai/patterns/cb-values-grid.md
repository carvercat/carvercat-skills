# Values grid

**Template** `cb_values_grid` (Library name "Values grid") · Corporate Brand pack · **Verified 0.1.8.1 (rev 1127)**, comp `CB Values grid` in `categories/corporate-brand/cb-lab-3`.

For briefs like "our company values", "what we stand for", "four principles". Four white cards on the light background in a 2 × 2 grid, each with a short teal rule, a number, the value and one line. The light background is part of the template. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Title (SemiBold 56 px) | 0 | Soft rise (as keys) | |
| Cards 1–4 (680 × 250 px, white, radius 16) | 8, 14, 20, 26 (reading order) | Card settle (as keys) | **f23**, **f29**, **f35**, **f41** |
| Rule (56 × 5 px) and number (teal SemiBold 28 px) | card + 6 | rule grows from the left, decelerate; number Soft rise | Rule 4 **f44**; Number 1 **f35** |
| Value (SemiBold 44 px) | card + 8 | Soft rise | |
| Line (Regular 30 px) | card + 12 | Soft rise | Line 1 **f41**, Line 4 **f59** |

**0% overshoot.** Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (closest 24.0 px, number / rule).

## Steps
1. Edit `VALUES` in `corporate_brand_lab3.py`. Keep each line under about 32 characters at 30 px, so it stays inside the 584 px text width of a card.
2. For three values, use one row of three 520 px cards; for six, three columns of two.

## Pitfalls
- Light layouts need their own background: the template carries "Light background" so navy text never lands on a dark comp.
- Reading time: the last line lands at f59, and a 30-character line needs 53 opaque frames, so do not cut the comp shorter than about 120 f.

Inspiration: values pages in employer-brand and culture films. No external text or code was used.
