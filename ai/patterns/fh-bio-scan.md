# Biometric scan

**Template** `fh_bio_scan` (Library name "Biometric scan") · Futuristic HUD pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FH Bio scan` in `categories/futuristic-hud/fh-lab-3`.

For briefs like "health tech", "medical device", "fitness wearable" or a sci-fi medbay. A body outline draws on, a scan beam passes over it once, markers ping on the brain and heart as the beam reaches them, an ECG trace draws with a pen dot, and three vitals type on. 150 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Head outline, Body outline | 0 | Trim end 0 → 1 (expo), f0–18 and f2–22 | |
| Section 1–3 (faint torso lines) | 10 | Trim end, f10–22, 3 f apart | |
| Scan beam (4 px) and Scan glow (60 px, soft edge 26 px, 22%) | 18 | y 230 → 770 at constant speed (9 px a frame, Linear), f18–78; fade out f78–86 | beam position settles **f78**, opacity **f86** |
| Brain marker, Heart marker (+ ping rings) | 24 / 50 | pop 0 → 115 → 100% when the beam reaches them (frame computed from the beam speed); a ring grows 0.3 → 2.4× and fades over 24 f | heart scale settles **f60** (the 15% is the keyed peak) |
| ECG frame | 6 | scan open (scale Y 2% → 100%), f6–16 | |
| ECG trace (3 beats, round corners) | 20 | Trim end 0 → 1, Linear, f20–110 | |
| ECG pen (white dot) | 20 | rides the tip of the trace: position baked every frame from the path's arc length; fades f110–116 | position settles **f110**, opacity **f116** |
| Heart rate / SpO2 / Temp (label 26 px #4FA8BF, value 50 px) | 52 / 60 / 68 | label flickers on, value types on 4 f later (1 f a character) | heart value from **f56** |
| Status "SCAN COMPLETE" (40 px, green #3FD08A) | 86 | Flicker on (Hold steps) | on **f96** |

Lint (with `contrast:true`) 0 errors, 0 warnings, 6 notes (`repeated_key_value` on the scan's holds, `speed_jump` where the beam stops; intended). `inspect qc` (240 px): no flashes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 54 pairs, closest 24.4 px (Oxygen label / value). Full-frame looks of the placed comp at f52 (beam on the heart) and f149: nothing cut; the QRS spike stays inside the ECG frame.

## Steps
1. Replace the body outline with the subject's own silhouette path, or a photo under it; keep the beam span (`y0`, `y1`) on the subject.
2. Change the vitals in `bio_scan()`; marker frames follow the beam (`at(y)`).

## Pitfalls
- A tall ECG spike first touched the frame's top edge (−86 px in a 170 px frame); −66 px clears it. Look at the frame with the spike drawn.
- Three readout columns at 56 px ran into each other (`text_overlap`, then a 35 px gap): wide-tracked caps are wider than they look. Measure with `measure.boxes` and right-align the last column on the frame's edge.

Inspiration: common sci-fi HUD and interface conventions. No external text or code was used.
