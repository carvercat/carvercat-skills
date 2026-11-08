# Careers card

**Template** `cb_careers_card` (Library name "Careers card") · Corporate Brand pack · **Verified 0.1.8.1 (rev 1127)**, comp `CB Careers card` in `categories/corporate-brand/cb-lab-3`.

For briefs like "we're hiring", "join our team", "job opening". A teal bar draws down beside a kicker, the role title, three detail pills (place, contract, team), a two-line pitch and a teal button with the careers URL. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Accent bar (6 × 560 px, teal) | 0 | draws down from its top (anchor top, height 0 → 1), decelerate | **f18** |
| Kicker "WE'RE HIRING", role (SemiBold 84 px) | 4, 8 | Soft rise (as keys) | role **f29** |
| Pills 1–3 (56 px tall, navy, radius 28) and their text (Medium 28 px) | 18, 23, 28 | Card settle; text opacity in 12 f | **f33**, **f38**, **f43** |
| Body (Regular 34 px, two lines) | 32 | Soft rise | **f53** |
| Button (460 × 80 px, teal), button text (navy SemiBold 32 px) | 44, 48 | Card settle; Soft rise | button **f59**, text **f69** |

**0% overshoot.** Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (closest 50.9 px, role / pill text).

## Steps
1. Edit the role, the pitch and the URL. A role of about 22 characters fits at 84 px in one line; longer titles go to 64 px.
2. Edit `PILLS` in `corporate_brand_lab3.py` and rebuild: pill widths are computed from the text length (about 15.5 px per character at 28 px, plus 64 px).
3. For social, recut to 9:16 as its own layout ([vertical recuts](../recipes/vertical-recuts.md)).

## Pitfalls
- The pills are rectangles with the corner radius at its 0.5 cap, which gives rounded ends but not true semicircles ([KI-121](../references/known-issues.md#ki-121)). For true pills, use a 2-point path with a round-capped 56 px stroke.
- Hold the URL at least 2 s: it lands at f69 and the card holds to f150.

Inspiration: job-opening cards in employer-brand social posts. No external text or code was used.
