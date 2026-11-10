# Cover transitions (7 templates)

**Templates** in `library/templates/transitions/` · Transitions pack · **verified 0.1.8.1 (rev 1127, master build; headless, isolated folders, `ai/scripts/motion/verify_pack.py`)**; every window below was re-measured with one definition (the underlay is hidden: the frame reads the same over magenta and over green), comps `TX …` in `categories/transitions/tx-lab`. The templates drop the lab's stand-in "Scene A" and "Scene B".

| Template | Pieces | Keys | Measured |
|---|---|---|---|
| **Slide wipe** (36 f) | one frame-size panel | position −1 W → 0 (0–16, ease-in Custom), hold to 20, → +1 W (20–36, expo-out); `directionalBlur` 160 px at 0deg on the way in and out, 0 from f16 to f20 while it covers ([directional blur](../references/effects/directional-blur.md)) | covered 16–20; settles **f29** |
| **Diagonal wipe** (36 f) | a 1000 px square, scale 2.6, rotated 30° (stored value) | position −1.5 W → 0 (0–17), hold to 19, → +1.5 W | covered 17–19; settles **f29** |
| **Split doors** (36 f) | two 1920 × 548 px doors (8 px overlap) | each slides 560 px in (0–17, ease-in), holds to 20, slides back out (expo) | covered 17–20 |
| **Bars stagger** (40 f) | six 320 px bars, alternating accent / coral | each drops in from above (expo, 10 f) 2 f apart, leaves downward (accelerate) 2 f apart | covered **16–23**; last bar settles **f39** |
| **Clock wipe** (40 f) | a 380 px ellipse with a 380 px butt stroke, scale 2.95, rotated 90 → 96° (stored value) | Trim start 1 → 0 (0–19, ease-in), then Trim end 1 → 0 (21–40, expo) | covered 19–21; start settles **f19**, end **f33** |
| **Bubble cover** (40 f) | three 1000 px discs (coral, accent, ink), scale up to 2.4 | grow 3 f apart (ease-in); the first two vanish under the ink at 21–22; the ink one shrinks away 24–36 | covered 17–29; settles **f36** |
| **Dip to colour** (30 f) | one frame-size rectangle | opacity 0 → 1 (0–13, `cubic-bezier(0.333, 0, 0.667, 1)`), hold to 17, → 0 (same curve) | covered 13–17; qc: no flash |

**Slide wipe, re-checked with the streak on Carvercat 0.1.10, 2026-11-10 (`verify_pack.py`):** lint 0/0/0 in 16:9 and 9:16, objects pass, covered f16-20, settles f30. The v1 comparison reads DIFF with a worst silhouette difference of 2.50 % (limit 2 %): the soft streak on the panel's edge is the intended difference; the cover window is unchanged.

All seven (measured before the streak): lint 0/0 in the lab and 0/0/0 when placed in a fresh 16:9 and a fresh 9:16 comp; qc finds no flash; against the v1 originals the silhouette matches at 7 frames each (0.00-0.02 % of pixels differ), and the colour reads exactly as stated (the v1 kit's linear curve made it about 10-13/255 off, which is gone).

**Choosing:**
- Slide wipe or doors for corporate and explainer work.
- Diagonal or bars for sports and social.
- Clock wipe for retro or countdowns.
- Bubbles for playful styles.
- Dip to colour for a mood change or a chapter break (keep its colour dark or brand-solid; a white dip is the most likely to trip flash checks).
