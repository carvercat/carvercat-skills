# Milestone timeline

**Template** `ex_timeline` · Explainer pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `EX Timeline`.

A 1400 px grey track at y 560 and a blue progress line on top of it. Four milestones carry a dot (30 px, white ring), a year above (ExtraBold 44 px) and an event below (Medium 30 px): 2019 Idea, 2021 First release, 2023 Teams, 2026 Everywhere.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Track | 0–24 | Trim end 0 → 1, expo | |
| Progress | 30–110 | Trim end 0 → 1, S curve cubic-bezier(0.333, 0, 0.667, 1) | settles **f106** |
| Milestone *i* | 30 + 80*i*/3 | dot scale 0 → 1 (back) as the progress reaches it; year and event **Step in** 2 and 5 f later | last dot 9.7% overshoot |

Lint 0/0 (the comp runs to 150 f so the last event is readable). With more milestones, space them evenly and keep the pop frames at 30 + 80*i*/(count − 1) on the S curve's even spacing. The progress is not linear, so for exact sync check the frames with a look.
