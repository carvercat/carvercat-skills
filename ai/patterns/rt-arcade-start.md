# Arcade start screen

**Template** `rt_arcade_start` (Library name "Arcade start screen") · Retro pack · **verified 0.1.8.1 (rev 1127)**, comp `RT Arcade start` in `categories/retro/rt-lab-2`.

**Measured on 0.1.8.1 (rev 1127, harness `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0, no flashes; against the v1 original the worst silhouette difference is 0.02 % (limit 2 %) and every object is present with the same text (box offset at most 0.7 px); colours are now the exact hex the page states (mean shift 21.6 of 255, intended). The frame numbers in the table above are the keys of the generator (`design units`), unchanged.


An arcade title screen: "HI-SCORE 048200" (yellow), "STAR RACER" (pink ExtraBold 180 px with a hard cyan offset shadow), a blinking "PRESS START" and "CREDIT 01". 150 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Arcade score | 0 | Rise - on twos | |
| Arcade title | 6 | Pop - on twos | **3.9%**, settles **f18** |
| Arcade press | 30 | on for 30 f, then Hold blinks: 30 f on, 15 f off | |

Lint 0 errors, 0 warnings; `inspect qc` (240 px) found no flashes. Placed into a fresh comp: lint 0/0/0. The first 30 f on covers lint's reading time; one blink every 1.5 s is far under 3 flashes a second.

Inspiration: 80s arcade attract screens. No external text or code was used.
