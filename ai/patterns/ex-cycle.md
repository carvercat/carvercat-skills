# Cycle loop

**Template** `ex_cycle` (Library name "Cycle loop") · Explainer pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `EX Cycle` in `categories/explainer/ex-lab-2`.

A dashed 600 px ring with four 170 px nodes (Plan, Make, Test, Learn) placed clockwise from 12 o'clock, and "repeat" in the centre. 150 f, holds. The light ground (`#F7F7FA`) is a "Light background" object kept in the template.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Cycle ring (6 px dashed) | 0 | rotation 0 → −45° over the clip (clockwise, one way) | |
| Cycle node 1–4 | 6, 20, 34, 48 | pop (back ease, 12 f) | **9.8%**; node 4 settles **f59** |
| Cycle label 1–4 | node + 4 | Step in | |
| Cycle centre | 64 | Step in | settles **f75** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0. The ring keeps turning one way, so the hold never freezes.

Inspiration: cycle diagrams (plan–do–check–act style). No external text or code was used.
