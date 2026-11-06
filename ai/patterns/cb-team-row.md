# Team row

**Template** `cb_team_row` · Corporate Brand pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `CB Team row` in `categories/corporate-brand/cb-lab-2`.

Three 220 px portrait circles (grey stand-ins) with names and roles below, on a light background (kept). 120 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Light background | 0 | none | |
| Portrait 1–3 | 4, 10, 16 | Card settle | Portrait 1 settles **f20** |
| Name 1–3 (SemiBold 38 px) | portrait + 8 | Soft rise | |
| Role 1–3 (Regular 28 px) | portrait + 12 | Soft rise | Role 3 settles **f49** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0. No overshoot anywhere (the pack's style rule).

## Steps
1. Place and apply. Replace each portrait circle with a photo masked by the circle: `property.set {id:<photo>, key:"mask", value:{"ref":"<circle id>"}}`, then `parent.clear {ids:[circle, photo]}` when the circle must move independently.
2. Edit names and roles.

Inspiration: leadership and team introductions in company films. No external text or code was used.
