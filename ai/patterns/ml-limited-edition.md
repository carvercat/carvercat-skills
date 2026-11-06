# Limited edition number

**Template** `ml_limited_edition` (Library name "Limited edition number") · Minimal Luxury pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `ML Limited edition` in `categories/minimal-luxury/ml-lab-3`.

For briefs like "limited edition", "one of 150", "numbered pieces". The edition number rises out of an invisible window's lower edge (a mask), so it appears from a line rather than from nowhere; a rule opens and OF 150 follows. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Kicker "LIMITED EDITION" (gold Regular 26 px, tracking 1.6, y 330) | 0 | opacity in 36 f; tracking 1.60 → 1.64 | opacity settles **f31** |
| Number window (the mask, 900 × 280 px at the centre, still) | 0 | none | |
| Number "027" (ivory Regular 220 px, tracking 1.1) | 12 | up 240 px from below the window, f12–66 (decelerate); opacity f12–40; tracking 1.10 → 1.14 over the hold | **0% overshoot**; position settles **f53**, opacity **f36** |
| Rule (160 px, y 700) | 0 | opens from its centre, f60–100 | settles **f96** |
| "OF 150" (muted Regular 28 px, tracking 1.5, y 760) | 70 | opacity in 36 f | opaque **f101** |

Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 3 pairs, closest 120 px (Kicker / Number). Full-frame looks of the placed instance at f16 (the digits cut by the window's lower edge, as intended), f24 and f100: at rest nothing is cut.

How it is built: the window is the mask and the number its content (`property.set {id:"Number", key:"mask", value:{"ref":"<Number window id>"}}`, then `parent.clear {ids:[Number window, Number]}`).

## Steps
1. Change the number and the edition size. Up to four digits fit the 900 px window at 220 px: "027" measures 475 px at the end of its breathe, so four digits are about 630 px.
2. Keep the number as one text; separate digit texts would each need the mask.

## Pitfalls
- The rise is fast at first (strong decelerate): the digits clear the window's edge in about 12 frames and then settle slowly. A slower first move shows the cut edge longer, which reads as a wipe, not a rise.
- Lint does not see the mask ([KI-133](../references/known-issues.md#ki-133)); here it raised nothing, because the number is inside the window at rest. Judge the entrance with a look.

Inspiration: numbered editions on watch and jewellery cards. No external text or code was used.
