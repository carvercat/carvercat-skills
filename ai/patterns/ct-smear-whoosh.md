# Smear whoosh

**Template** `ct_smear_whoosh` · Cartoon Bounce pack · **verified 0.1.8.1 (rev 1127; headless, isolated folders, pack added to a scratch user Library)**, comp `CT Smear whoosh`.

**Re-checked with the new effects on Carvercat 0.1.10, 2026-11-10 (headless, isolated folders, `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0; silhouette against the v1 original passes, objects pass; visible f1-44.

A blue rounded blob (260 × 140, radius 60) shoots in from 1200 px to the left and stops at the centre. Three 440 px speed lines draw behind it and wipe away.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Blob position | 0–8 | 1200 px, Custom expo | settles **f5** |
| Blob scale (transformOrigin "100% 50%" at the leading edge, anchor [1, 0]) | 0, 8, 12, 16 | [2.4, 0.8] smear → [0.8, 1.15] squash on the stop → [1.08, 0.94] → [1, 1] | settles **f16** |
| Blob streak | 0–12 | `directionalBlur` 160 px → 40 px (f8) → 0 px (f12) at 0deg, linear ([directional blur](../references/effects/directional-blur.md)): a streak along the run, crisp when it stops | |
| Speed lines | 2–8 draw, 6–16 wipe | Trim end 0 → 1 (expo), then start 0 → 1 (accelerating arrival cubic-bezier(0.333, 0, 0.667, 0.333)) | |

Lint 0/0/0. Use it for any fast arrival; for a departure, reverse it (squash first, then smear out). Add a whoosh SFX starting 2 f before the blob arrives.
