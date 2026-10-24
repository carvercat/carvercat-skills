# Drop shadow

**Verified 0.0.72:** "lift" on a white card over a light grey ground — shadow y −0.004 → −0.025, softness 0.006 → 0.03, opacity 0.45 → 0.3 over 18 f, with the card rising 0.015 H and scaling 1 → 1.04. Reads as the card lifting toward the viewer.

| param | range | default | meaning |
|---|---|---|---|
| x, y | −0.5–0.5 | 0.012, −0.012 | offset in FRAME fractions, **y up** (negative y = below) |
| softness | 0–0.2 | 0.01 | blur of the shadow, width-normalised |
| opacity | 0–1 | 0.5 | |
| red/green/blue | 0–1 | 0 | shadow colour (tint toward the background hue, never pure black on colour) |
| output | image/shadow | image | `shadow` renders the shadow alone (useful as a separate soft layer) |
| lightX/lightY/lightDistance | | 0,1,1 | light-direction mode (not verified) |

## Recipes
- **Resting card (UI):** y −0.006, softness 0.012, opacity 0.25–0.35, x 0. Big soft + low opacity beats small hard + dark.
- **Lift / hover:** animate y and softness up together, opacity down slightly (the further away, the softer and fainter), plus scale 1.03–1.05 and a 1–2 % rise. 12–18 f, Ease out.
- **Long shadow (flat design):** offset 0.03/−0.03, softness 0, opacity 0.2, tinted.
- **Text legibility over images:** softness 0.02, opacity 0.5, offset 0 — a soft halo rather than a directional drop.

## Rules
- One light direction for the whole piece (all shadows offset the same way).
- Shadows on dark backgrounds barely read; use a lighter ground or a glow/rim instead.
- Children of a shadowed group: put the shadow on the group/card, not on every child.
