# Pointer callout

**Template** `ex_callout` (Library name **Pointer callout**) · Explainer pack · **verified 0.1.8.1 (rev 1127; `ai/scripts/motion/verify_pack.py`: placed in a fresh 16:9 and a fresh 9:16 comp, lint 0/0/0, qc no flash; against the v1 original the silhouette differs by at most 0.00 % of pixels over 7 frames; object-level check pass)**, comp `EX Callout`.

A coral target dot and ring at (760, 640). An ink leader line goes up 220 px, then across 300 px, to a dark 520 × 84 px label box with white Bold 36 px text.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Dot | 0–10 | scale 0 → 1, back | |
| Ring | from 6 | opacity in 4 f + **Emphasis pulse** (once) | settles **f22** |
| Leader | 10–26 | Trim end 0 → 1, expo | settles **f20** |
| Label box | 24–36 | scale X 0 → 1 from the left edge, expo | settles **f32** |
| Label | from 30 | **Step in** | |

Lab comp lint on 0.1.8.1 (native size): 0 errors, 0 warnings, 0 notes. Move the instance so the dot sits on the thing you point at, and keep the label on the side with the most free space.
