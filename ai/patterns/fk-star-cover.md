# Star cover

**Template** `fk_star_cover` · Funky pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FK Star cover` in `categories/funky/fk-lab-2`.

A transition: an orange 8-point star spins and grows until it covers the frame, then shrinks away. 36 f.

| Part | Motion | Measured |
|---|---|---|
| Cover star (1000 px drawn, inner radius 0.6) | scale 0 → 4.0, f0–15 (S curve cubic-bezier(0.333, 0, 0.667, 1), the curve arriving at the key); hold to f21; 4.0 → 0, f21–36; rotation −90° → 90° (linear) | frame covered **f10–25** (look) |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place 18 f before your cut, above both scenes; cut at its f18.

## Pitfalls
- Drawn at 1000 px and scaled ([KI-137](../references/known-issues.md#ki-137)). At scale 4 the inner radius is 1200 px, past the 1101 px half-diagonal, so the star's notches never show a corner.

Inspiration: shape-wipe transitions in pop edits. No external text or code was used.
