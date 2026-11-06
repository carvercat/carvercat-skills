# Process steps

**Template** `ex_process_steps` · Explainer pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `EX Process steps` in `categories/explainer/ex-lab`.

Three 160 px circles (blue, coral, green) at x 420, 960 and 1500, numbered 1–3 (ExtraBold 72 px), each with a title (Bold 48 px) and a line of text (Medium 30 px, muted). 8 px arrows with triangle heads join them.

| Part (step *i*) | Frames | Motion | Measured |
|---|---|---|---|
| Circle | from 24*i* | scale 0 → 1, Custom back | **9.8% overshoot**, settles 11 f after its start |
| Number / title / text | 24*i* + 4 / + 6 / + 10 | **Step in** | text settles 11 f after its start |
| Arrow *i* (between steps) | 24*i* + 12 to + 24 | line Trim end 0 → 1 (expo); head pops at + 20 (back) | line settles **f20** (arrow 1), head **9.3%** overshoot |

Lint 0/0. Change the three titles and lines inside the comp. For more steps, duplicate a step group 540 px to the right and shrink the instance.
