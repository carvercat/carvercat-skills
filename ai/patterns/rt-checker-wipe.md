# Checker wipe

**Template** `rt_checker_wipe` · Retro pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `RT Checker wipe`.

A transition: an 8 × 5 board of 240 × 216 px squares (orange and brown) covers the frame diagonally, then clears in the same order.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Square (row *r*, column *c*) | in at a = 2(*r* + *c*): a to a + 6; out a + 24 to a + 30 | scale 0 → 1 on twos (expo), then 1 → 0 on twos (accelerating) | covered **f22–28**; clear by **f52** |

## Steps
Put it on the top track so that its f26 lands on your cut (the showcase cuts at master f165 with the wipe starting at f139). Lint 0/0/0. With 40 objects it is the heaviest template in the pack; nest it rather than copying its squares.
