# Appeal

**What it does:** the viewer wants to keep watching. Appeal comes from clarity, consistency and charm, not from complexity.

## How in Carvercat
- **Clean silhouettes at every pose:** check entrance, hold and exit frames with `carvercat_look`.
- **One accent per frame,** one easing family per film, one type family ([../colour.md](../colour.md), [../brand-systems.md](../brand-systems.md)).
- **No jitter, no flashes:** lint `jitter` and `inspect qc` flash checks are the floor, not the goal.
- **Every hold breathes:** a drift, a 2–3% push, a tracking breathe or a one-way turn, so nothing freezes.
- **Readable:** text big enough (28 px or more for labels) and long enough (lint `reading_time`).

## Measured examples
| Template | Appeal device |
|---|---|
| Framed word ([ml-framed-word.md](../../../patterns/ml-framed-word.md)) | frame lines drift 14 px apart over the hold |
| Sale badge ([fk-sale-badge.md](../../../patterns/fk-sale-badge.md)) | turns 30° one way after landing |
| Speech bubble ([ct-speech-bubble.md](../../../patterns/ct-speech-bubble.md)) | jelly spring with volume, tail pops behind |
| Every round-2 template | lint 0 errors / 0 warnings, placed lint 0/0/0 |

Run [../review-checklist.md](../review-checklist.md) and the style list in [../review-by-style.md](../review-by-style.md) before showing anything.
