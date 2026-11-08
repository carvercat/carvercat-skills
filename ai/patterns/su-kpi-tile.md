# KPI tile

**Template** `su_kpi_tile` · SaaS UI pack · **Verified 0.1.8.4 (rev 1130)**, comp `SU KPI tile`.

A 440×240 px dashboard card: label, big value, a green delta and a progress bar that draws to 72%.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| KPI card (radius 24, shadow) | 0 | Card lift | settles **f12** |
| KPI label ("Monthly revenue", Medium 24 px, muted) | 3 | Card lift | |
| KPI value ("$48,200", Bold 64 px) | 6 | Card lift | |
| KPI track + KPI fill (10 px round-capped lines) | 10 | Card lift; the fill's trimEnd 0% → 72%, f22–52, Custom expo cubic-bezier(0.16, 1, 0.3, 1) | fill settles **f41** |
| KPI delta ("+12.4%", SemiBold 28 px, `#16A34A`, right-aligned) | 26 | Card lift | settles **f38** |

## Steps
1. Place and apply. Edit the value, delta and the fill's end key inside the comp.
2. For a counting value, replace KPI value with the [rolling counter](su-rolling-counter.md) at 64 px.
3. The tile holds. Give the instance an exit (Modal dismiss) and, for holds over 2 s, a slow 2–3% scale push, as the showcase does.

## Pitfalls
- Lint's minimum text size (18 px measured line height) rules out a delta that pops from 60%. That is why the delta uses Card lift (94%) at 28 px.
