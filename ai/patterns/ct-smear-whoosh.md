# Smear whoosh

**Template** `ct_smear_whoosh` · Cartoon Bounce pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `CT Smear whoosh`.

A blue rounded blob (260 × 140, radius 60) shoots in from 1200 px to the left and stops at the centre. Three 440 px speed lines draw behind it and wipe away.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Blob position | 0–8 | 1200 px, Custom expo | settles **f5** |
| Blob scale (transformOrigin "100% 50%" at the leading edge, anchor [1, 0]) | 0, 8, 12, 16 | [2.4, 0.8] smear → [0.8, 1.15] squash on the stop → [1.08, 0.94] → [1, 1] | settles **f16** |
| Speed lines | 2–8 draw, 6–16 wipe | Trim end 0 → 1 (expo), then start 0 → 1 (accelerating arrival cubic-bezier(0.333, 0, 0.667, 0.333)) | |

Lint 0/0/0. Use it for any fast arrival; for a departure, reverse it (squash first, then smear out). Add a whoosh SFX starting 2 f before the blob arrives.
