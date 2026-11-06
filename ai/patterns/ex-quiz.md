# Quiz question

**Template** `ex_quiz` (Library name "Quiz question") · Explainer pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `EX Quiz` in `categories/explainer/ex-lab-2`.

A question (Bold 56 px) and three option cards (800 × 100 px). After a pause, the right answer (B) gets a green frame and a tick. 180 f (6 s). The light ground (`#F7F7FA`) is a "Light background" object kept in the template.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Quiz question | 0 | Step in | |
| Option 1–3, Option text 1–3 | 20, 28, 36 (+2) | Step in | last settles **f49** |
| Answer frame (8 px green stroke) | 100 | Emphasis pulse (once) | settles **f116** |
| Answer check | 104 | trim on, 10 f | |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0. The 50 f between the last option and the reveal is the viewer's think time; stretch it for harder questions.

## Steps
1. Edit the question and options; move the Answer frame and check to the right option's y (450 + option × 130).

Inspiration: quiz moments in educational video. No external text or code was used.
