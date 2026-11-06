# Partner logo wall

**Template** `cb_partner_wall` (Library name "Partner logo wall") · Corporate Brand pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `CB Partner wall` in `categories/corporate-brand/cb-lab-3`.

For briefs like "trusted by", "our clients", "partners and sponsors". Twelve white tiles in a 4 × 3 grid sweep in from the top left, each with a stand-in wordmark, under a heading and over an "and 400 more" line. The light background is part of the template. 120 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Title (SemiBold 52 px) | 0 | Soft rise (as keys) | **f21** |
| Tiles 1–12 (340 × 150 px, white, radius 14) | 6 + 4 × (row + column) | Card settle (as keys) | Tile 1 **f21**, Tile 12 **f41** |
| Logos 1–12 (34 px stand-in wordmarks) | tile + 4 | opacity in 12 f | Logo 1 **f21** |
| "and 400 more organisations" (Regular 30 px) | 40 | Soft rise | **f61** |

**0% overshoot.** Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (closest 129.1 px).

## Steps
1. Replace each "Logo" text with the partner's logo image (import it, scale it to fit about 260 × 90 px inside its tile, and give it the same clip start and opacity keys as the text it replaces).
2. Use the logos as supplied (usually one-colour versions on white); ask for permission to show them.
3. For eight partners, delete the third row and move the rows to y = 470 and 660.

## Pitfalls
- The wordmarks are invented stand-ins. Never ship a wall with stand-ins, and do not redraw a real company's logo as text.
- A tracked caps name at 34 px uses most of a 340 px tile; keep stand-ins under about 11 letters.

Inspiration: client and partner walls on corporate sites and in pitch films. No external text or code was used.
