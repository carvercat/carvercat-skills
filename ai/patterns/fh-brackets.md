# Corner brackets scan

**Template** `fh_brackets` · Futuristic HUD pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FH Brackets`.

Four 60 px L-shaped corner brackets (5 px cyan, glow) frame a 640 × 380 area centred in the frame. A glowing scan line sweeps through it, and a "SCAN 01" tag sits above the top-left corner.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Corners | 0, 2, 4, 6 (each 14 f) | fly in 90 px diagonally from outside (expo), opacity in 4 f | settle 9 f after each start |
| Scan line (600 × 3 px, glow 0.6) | 16–56 | top → bottom, S curve cubic-bezier(0.333, 0, 0.667, 1); opacity in 4 f | settles **f54** |
| Tag | from 12 | **Flicker on** | |

Lint 0/0. Scale the instance to frame any subject. For a repeating scan, place a second instance, never a back-and-forth key loop.
