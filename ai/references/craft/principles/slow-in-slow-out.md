# Slow in and slow out

**What it does:** real things accelerate and decelerate. Easing is the single biggest difference between "computer" motion and designed motion.

## How in Carvercat
- **A key's `ease` shapes the segment that leaves it**, as in CSS (older projects store it on the arriving key; measured, [saas-ui.md](../../../patterns/saas-ui.md) pitfall 1). Entrances: `ease-out` or a decelerating cubic-bezier on the start key. Exits: `ease-in` on the start key.
- Easings: `linear`, `ease-in`, `ease-out`, `ease-in-out`, `hold`, or `cubic-bezier(x1, y1, x2, y2)` (stored as `customEase [x1, y1, x2, y2]` on the arriving key), e.g. expo out (0.16, 1, 0.3, 1), standard (0.2, 0, 0, 1), accelerate (0.3, 0, 0.8, 0.15).
- Presets bake their curves to keys with linear joins, so they can carry springs and multi-stage moves.

## Measured examples (settle = within 0.5% of the end value)
| Preset / template | Curve | Settles |
|---|---|---|
| Card lift (SaaS) | expo out, 18 f | **f12** |
| Soft rise (Corporate) | standard, 24 f | **f21** |
| Slow fade in (Luxury) | standard + strong decelerate, 36 f | size **f28**, opacity f32 |
| Scan open (Y) (HUD) | expo, 14 f | **f10** |
| Timeline axis ([dv-timeline.md](../../../patterns/dv-timeline.md)) | ease-in-out, f6–60 | f55; dots placed by the inverse of the ease (`t_for_progress`) |
| Modal dismiss (SaaS exit) | accelerate, 9 f | moves in the last 9 f |

## Rules of thumb
- Exits about 50–70% of the entrance length, accelerating.
- Linear only for drifts, pushes and loops (a 6% photo push over 150 f).
- A move that should feel like one stroke across two clips: split one curve exactly (`Curve.window` in `json-authoring.md`).
