# Checklist

**Template** `ex_checklist` · Explainer pack · **verified 0.1.8.1 (rev 1127; `ai/scripts/motion/verify_pack.py`: placed in a fresh 16:9 and a fresh 9:16 comp, lint 0/0/0, qc no flash; against the v1 original the silhouette differs by at most 0.00 % of pixels over 7 frames; object-level check pass)**, comp `EX Checklist` in `categories/explainer/ex-lab-2`.

"Before you render" and four rows: an outlined box, the item (Medium 44 px) and a green tick that draws into the box. 150 f, holds. The light ground (`#F7F7FA`) is a "Light background" object kept in the template.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| List title | 0 | Step in | |
| Box i, Check item i | 10 + 18i, +2 | Step in | Check item 4 settles **f77** |
| Check i | box + 10 | trim 0 → 1, 10 f, expo | Check 4 settles **f81** |

Lab comp lint on 0.1.8.1 (native size): 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Edit the items; to tick them one per narration beat, move each Check clip to its word.

Inspiration: pre-flight checklists. No external text or code was used.
