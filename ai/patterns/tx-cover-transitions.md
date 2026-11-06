# Cover transitions (7 templates)

**Templates** in `library/templates/transitions/` · Transitions pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comps `TX …` in `categories/transitions/tx-lab`. The templates drop the lab's stand-in "Scene A" and "Scene B".

| Template | Pieces | Keys | Measured |
|---|---|---|---|
| **Slide wipe** (36 f) | one frame-size panel | position −1 W → 0 (0–16, ease-in Custom), hold to 20, → +1 W (20–36, expo-out) | covered 16–20; settles **f29** |
| **Diagonal wipe** (36 f) | a 1000 px square, scale 2.6, rotated 30° (stored value) | position −1.5 W → 0 (0–17), hold to 19, → +1.5 W | covered 17–19; settles **f29** |
| **Split doors** (36 f) | two 1920 × 548 px doors (8 px overlap) | each slides 560 px in (0–17, ease-in), holds to 20, slides back out (expo) | covered 17–20 |
| **Bars stagger** (40 f) | six 320 px bars, alternating accent / coral | each drops in from below (expo, 10 f) 2 f apart, leaves upward (accelerate) 2 f apart | covered **20–22**; last bar settles **f40** |
| **Clock wipe** (40 f) | a 380 px ellipse with a 380 px butt stroke, scale 2.95, rotated 90 → 96° (stored value) | Trim start 1 → 0 (0–19, ease-in), then Trim end 1 → 0 (21–40, expo) | covered 19–21; start settles **f19**, end **f33** |
| **Bubble cover** (40 f) | three 1000 px discs (coral, accent, ink), scale up to 2.4 | grow 3 f apart (ease-in); the first two vanish under the ink at 21–22; the ink one shrinks away 24–36 | covered 20–24; settles **f36** |
| **Dip to colour** (30 f) | one frame-size rectangle | opacity 0 → 1 (0–13, `cubic-bezier(0.333, 0, 0.667, 1)`), hold to 17, → 0 (same curve) | covered 13–17; qc: no flash |

All seven: lint 0/0 in the lab and 0/0/0 when placed in a fresh comp.

**Choosing:**
- Slide wipe or doors for corporate and explainer work.
- Diagonal or bars for sports and social.
- Clock wipe for retro or countdowns.
- Bubbles for playful styles.
- Dip to colour for a mood change or a chapter break (keep its colour dark or brand-solid; a white dip is the most likely to trip flash checks).
