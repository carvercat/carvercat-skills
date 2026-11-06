# Pattern drift

**Template** `fk_pattern_drift` · Funky pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FK Pattern drift` in `categories/funky/fk-lab-2`.

A background: a yellow ground with a staggered grid (240 × 216 px) of dots, triangles and bars in pink, teal, purple and orange, all drifting 240 px right and 216 px down over 150 f, linearly. 64 shapes plus the ground.

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place on the lowest track and put titles above it. Stretch the clip and the last keys together for a longer drift (keep it slow: about 1.6 px a frame here).

## Pitfalls
- Cells that never enter the frame during the drift are a lint **error** (`never_visible`, "off frame for its whole clip"). The lab keeps only cells whose path enters the frame (sampled along the move).
- The drift is not a seamless loop: odd rows are offset by half a cell, so the last frame does not match the first.

Inspiration: Memphis-pattern backgrounds. No external text or code was used.
