# Boutique address

**Template** `ml_boutique_address` (Library name "Boutique address") · Minimal Luxury pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `ML Boutique address` in `categories/minimal-luxury/ml-lab-3`.

For briefs like "our new store", "now open in Paris", "visit us", or the last card of a store-opening film. A small gold pin ring draws itself, then NOW OPEN, the boutique name, a rule, a two-line address and the opening hours. 180 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Pin ring (44 px, gold 2 px stroke, y 250) and dot (10 px) | 0, 20 | the ring draws (trim, f0–40, S curve cubic-bezier(0.333, 0, 0.667, 1), the curve arriving at the key); the dot fades in 36 f | ring settles **f36** |
| Kicker "NOW OPEN" (gold Regular 26 px, tracking 1.6, y 330) | 24 | opacity in 36 f | |
| Boutique "MAISON ELAN" (ivory Regular 64 px, tracking 1.5, y 420) | 34 | Slow fade in (baked); tracking 1.50 → 1.54 from f70 | opacity **f65**, size **f61** |
| Rule (120 px, y 490) | 0 | opens from its centre, f52–92 | |
| Address (ivory Regular 34 px, two lines, line spacing 1.45, y 580) | 62 | up 12 px over 40 f (decelerate), then a 0.3% H drift | **0% overshoot**; opaque **f93** |
| Hours (muted Regular 26 px, tracking 1.3, y 700) | 80 | opacity in 36 f | opaque **f111** |

Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 14 pairs, closest 48.5 px (Kicker / Pin ring).

## Steps
1. Change the name, address and hours. The address is one text with a line break; keep it to two lines.
2. Several boutiques: place the template once per city, 150–180 f each, with Slow dip between them.

## Pitfalls
- The name is wide tracked caps: "MAISON ELAN" at 64 px and tracking 1.5 measures 978 px at the end of its breathe; a longer name needs less tracking or a smaller size.
- The pin is a ring and a dot, not a map. For a map with a route, see [maps](../references/maps/maps.md).

Inspiration: store-opening cards in fashion house films. No external text or code was used.
