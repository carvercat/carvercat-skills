# Timing

**What it does:** the number of frames a move takes gives it weight, mood and importance. Fast reads as light or urgent, slow as heavy or premium.

## How in Carvercat
- Work in frames at the comp's fps (30 here). Reuse a duration scale per film instead of new numbers per object.
- Measure, don't guess: `carvercat_inspect mode:curves` gives the settle frame of every property; `mode:timing` gives when each object enters and exits.
- Text has a floor: lint asks for 17 characters a second (spaces not counted) and at least 25 fully opaque frames: `frames = max(25, ceil(chars × 30 / 17))` ([../typography.md](../typography.md)).

## Measured ranges
The per-style table is in [../timing-by-style.md](../timing-by-style.md). In short:
| Feel | Entrance | Examples |
|---|---|---|
| Snappy | 8–12 f | Hook punch (settles f7), Glitch stretch hit (f6), Impact slam (f8) |
| Standard | 14–20 f | Card lift (f12), Bar grow - spring (f18) |
| Calm | 20–24 f | Soft rise (f21) |
| Premium | 36 f and up | Slow fade in (f28–32), Drift up - 4 s (120 f) |

## Traps
- A clip whose keys run past its end is a lint **error** (`key_outside_clip`); staggered exits often do ([rt-blinds.md](../../../patterns/rt-blinds.md)).
- The last part of a stagger lands `gap × (parts − 1)` frames late.
