# Checker wipe

**Template** `rt_checker_wipe` · Retro pack · **verified 0.1.8.1 (rev 1127)**, comp `RT Checker wipe`.

**Measured on 0.1.8.1 (rev 1127, harness `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0, no flashes; against the v1 original the worst silhouette difference is 0.00 % (limit 2 %) and every object is present with the same text (box offset at most 0.0 px); colours are now the exact hex the page states (mean shift 13.1 of 255, intended); windows over a magenta/green underlay: gone f52. The frame numbers in the table above are the keys of the generator (`design units`), unchanged.


A transition: an 8 × 5 board of 240 × 216 px squares (orange and brown) covers the frame diagonally, then clears in the same order.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Square (row *r*, column *c*) | in at a = 2(*r* + *c*): a to a + 6; out a + 24 to a + 30 | scale 0 → 1 on twos (expo), then 1 → 0 on twos (accelerating) | all squares full size **f22–28** by the keys (the harness reports no covered window: under 99.5 % of the pixels hide the underlay); gone **f52** |

## Steps
Put it on the top track so that its f26 lands on your cut (the showcase cuts at master f165 with the wipe starting at f139). Lint 0/0/0. With 40 objects it is the heaviest template in the pack; nest it rather than copying its squares.
