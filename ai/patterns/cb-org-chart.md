# Org chart

**Template** `cb_org_chart` (Library name "Org chart") · Corporate Brand pack · **Verified 0.1.8.1 (rev 1127)**, comp `CB Org chart` in `categories/corporate-brand/cb-lab-3`.

For briefs like "introduce the new leadership team", "who reports to whom", "our structure after the merger". A top card (teal outline) joined by drawn connectors to three report cards, each with a name and a role. 150 f, holds.

Frames are comp frames.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Title (SemiBold 56 px), subtitle (Regular 30 px) | 0, 4 | Soft rise (as keys) | |
| Top card (440 × 150 px, navy, teal 3 px outline) | 4 | Card settle (as keys) | settles **f19** |
| Top name (SemiBold 38 px), top role (teal Medium 28 px) | 8, 12 | Soft rise | name **f29**, role **f33** |
| Stem, bus left / right, drops (grey 3 px) | 16, 24, 26 / 36 | Trim end 0 → 1, decelerate | stem **f24**, bus **f36**, middle drop **f34**, side drops **f44** |
| Report cards 1–3 | 42, 48, 54 | Card settle | **f57**, **f63**, **f69** |
| Names (SemiBold 36 px), roles (Regular 28 px) | card + 4, card + 8 | Soft rise | last role settles **f83** |

**0% overshoot** on every curve. Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (closest 21.3 px, title / subtitle). The connectors draw inside the placed instance; a full-frame look of the placed comp (f0–149) shows nothing cut.

## Steps
1. Edit `ORG_TOP` and `ORG_REPORTS` in `ai/scripts/motion/corporate_brand_lab3.py` and rebuild, or edit the texts after placing.
2. The cards are 440 px wide: a role of about 26 characters at 28 px fits. Longer titles go on two lines, or shorten them ("CFO").
3. For four reports, move the cards to x = 330, 750, 1170, 1590 at 380 px wide, and move the drops and bus ends with them.

## Pitfalls
- The connectors are under the cards (drawn first). Draw each drop after its card is placed, or the line end shows on an empty frame.
- Keep the names stand-ins until the client confirms spelling and titles; an org chart is checked line by line.

Inspiration: organisation charts in annual reports and onboarding films. No external text or code was used.
