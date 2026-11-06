# Safety notice

**Template** `cb_safety_notice` (Library name "Safety notice") · Corporate Brand pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `CB Safety notice` in `categories/corporate-brand/cb-lab-3`.

For briefs like "site safety rule", "compliance notice", "new policy from 1 March", for screens in offices, plants and training films. A warning triangle with "!", a kicker, a two-line rule, its scope and the policy reference, over a signal-amber band. Amber is the warning-sign convention; it is the only place the pack leaves its single teal accent. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Signal band (1920 × 40 px, amber `#F2A900`) | 0 | grows across from the left, 20 f, decelerate | **f15** |
| Sign (340 px triangle, amber) | 6 | Card settle over 24 f; turned with rotation +90 so a point is up | **f24** |
| Sign mark "!" (navy Bold 110 px) | 14 | Soft rise (as keys) | **f35** |
| Kicker "SAFETY NOTICE" (amber, tracked), heading (SemiBold 76 px, two lines) | 10, 14 | Soft rise | heading **f35** |
| Body (Regular 34 px) | 24 | Soft rise | **f45** |
| Rule (120 × 3 px, amber), policy (Medium 30 px) | 30, 34 | rule grows from the left; Soft rise | rule **f44**, policy **f55** |

**0% overshoot.** Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (closest 31.3 px, kicker / heading).

## Steps
1. Edit the heading, scope and policy. Keep the heading an instruction in plain words, two lines at most.
2. For a mandatory-action notice (blue circle) or a prohibition (red ring), change the sign and accent colour together and keep the layout.
3. Safety copy is the client's legal text: use their exact wording and check it against their policy.

## Pitfalls
- The triangle is a 3-sided polygon. Its first corner points right and its Angle control does not turn it on 0.1.6 ([KI-150](../references/known-issues.md#ki-150)), so it is turned with the transform rotation.
- The polygon is centred on its circumcentre: with the point up, the base is 85 px below the centre and the apex 170 px above. The "!" sits 18 px below the centre to look centred in the triangle.

Inspiration: workplace safety signage conventions (warning triangle, signal yellow) and notice screens. No external text or code was used.
