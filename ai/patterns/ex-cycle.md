# Cycle loop

**Template** `ex_cycle` (Library name "Cycle loop") · Explainer pack · **verified 0.1.8.1 (rev 1127; `ai/scripts/motion/verify_pack.py`: placed in a fresh 16:9 and a fresh 9:16 comp, lint 0/0/0, qc no flash; against the v1 original the silhouette differs by at most 0.00 % of pixels over 7 frames; object-level check pass (with `verify_pack.py --ink-templates`: the plain harness reads the faint ring dashes behind the labels as missing ink before the labels appear, the rendered pixels are identical))**, comp `EX Cycle` in `categories/explainer/ex-lab-2`.

A dashed 600 px ring with four 170 px nodes (Plan, Make, Test, Learn) placed clockwise from 12 o'clock, and "repeat" in the centre. 150 f, holds. The light ground (`#F7F7FA`) is a "Light background" object kept in the template.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Cycle ring (6 px dashed) | 0 | rotation 0 → −45° over the clip (clockwise, one way) | |
| Cycle node 1–4 | 6, 20, 34, 48 | pop (back ease, 12 f) | **9.8%**; node 4 settles **f59** |
| Cycle label 1–4 | node + 4 | Step in | |
| Cycle centre | 64 | Step in | settles **f75** |

Lab comp lint on 0.1.8.1 (native size): 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. The ring keeps turning one way, so the hold never freezes.

Inspiration: cycle diagrams (plan–do–check–act style). No external text or code was used.
