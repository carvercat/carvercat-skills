# SaaS lower third

**Template** `su_lower_third` (Library name "SaaS lower third") · SaaS UI pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SU Lower third` in `categories/saas-launch/saas-ui-lab-2`.

A 680×104 px white pill at bottom left (left edge x 120, y 860) with a 72 px accent logo chip, a name and a role. 150 f (5 s) with its own exit.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Pill (radius 52, shadow) | 0 | scale X 0 → 1 from its left edge (transformOrigin "0% 50%", anchor −1, 0), f0–14, Custom expo cubic-bezier(0.16, 1, 0.3, 1) | settles **f9** |
| Logo chip (72 px ellipse, `#5B5BF6`) | 4 | Pop - gentle | |
| Name ("Priya Shah", Bold 34 px) | 8 | Card lift | position settles **f20** |
| Role ("Product lead, Acme", Medium 26 px, muted) | 11 | Card lift | |
| All four | last 9 f | Modal dismiss | gone at f149 |

Lint 0 errors, 0 warnings (13 notes: held opacity keys). Placed into a fresh comp: lint 0/0/0, enters f0, exits f149.

## Steps
1. Place and apply at the start of the shot the person speaks in. Edit the name and role inside the comp.
2. Long names: widen the Pill (and keep x at 120, its left edge).
3. Longer hold: lengthen every clip in the comp by the same amount; the exit preset is anchored to the clip end, so it moves with it.

## Pitfalls
- Pill scale is X only (scaleX), from the left edge. Do not stagger it: scaleX/scaleY cannot be staggered ([KI-134](../references/known-issues.md#ki-134)).
- The text starts 8 f after the pill so it never shows outside a pill that is still growing.
- **Fixed 2026-10-28 (overlap audit).** The role sat 11.6 px under the name (geometry at rest). The name moved up 3 px and the role down 4 px: an 18.6 px gap ([KI-138](../references/known-issues.md#ki-138)).

Inspiration: the broadcast lower-third convention (name over role, accent mark) restyled for product UI. No external text or code was used.
