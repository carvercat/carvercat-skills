# Player spotlight

**Template** `sp_spotlight` (Library name "Player spotlight") · Sports pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SP Spotlight` in `categories/sports/sp-lab-2`.

An overlay that marks a player in footage: a flat yellow ring on the ground at the feet (300 × 90 px), three rings rippling out from it, a yellow arrow above the head and a red name tag. 120 f.

| Part | Clip | Motion | Measured |
|---|---|---|---|
| Spot base | f0– | scale 0 → 1, 10 f, back ease | **9.7%**, settles **f10** |
| Spot ring 1–3 | f10, 30, 50, 30 f each | scale 1 → 1.8 (decelerate), fade to 0 | |
| Spot arrow (3-gon turned 90° clockwise (stored −90), points down) | f6– | drops 60 px, 10 f, expo | settles **f13** |
| Spot tag, Spot name | f10, f12 | Slash in | |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place over the shot, move the instance so the base sits at the player's feet; for a moving player key the instance's position (or use a tracked null).

## Pitfalls
- A 3-gon points right at rotation 0. The `angle` geometry parameter of `cc.ngon` did not point it down; a transform rotation of 90° clockwise (stored −90) does.

Inspiration: player-tracking highlights in match analysis. No external text or code was used.
