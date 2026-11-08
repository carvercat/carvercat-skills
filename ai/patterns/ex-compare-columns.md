# Compare columns

**Template** `ex_compare_columns` · Explainer pack · **verified 0.1.8.1 (rev 1127; `ai/scripts/motion/verify_pack.py`: placed in a fresh 16:9 and a fresh 9:16 comp, lint 0/0/0, qc no flash; against the v1 original the silhouette differs by at most 0.00 % of pixels over 7 frames; object-level check pass)**, comp `EX Compare columns` in `categories/explainer/ex-lab-2`.

Two columns: "Old way" (coral header, three items with drawn crosses) and "New way" (green header, three items with drawn ticks). The second column starts 40 f after the first, so the narration can finish the first. 150 f, holds. The light ground (`#F7F7FA`) is a "Light background" object kept in the template.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Col head 1, Col title 1 | 0, 2 | Step in | |
| Cross / Item rows 1–3 | 8, 16, 24 | crosses draw (two 6 f strokes, 2 f apart); items Step in 2 f later | |
| Col head 2, Col title 2 | 40, 42 | Step in | head settles **f51** |
| Tick / Item rows 1–3 | 48, 56, 64 | tick draws (trim, 10 f, expo); items Step in | Item 2.3 settles **f77** |

Lab comp lint on 0.1.8.1 (native size): 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0.

Inspiration: "old way vs new way" comparisons in product explainers. No external text or code was used.
