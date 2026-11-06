# Principles of motion

The twelve principles of animation were written for drawn characters; most of them carry straight over to
motion graphics, and a few more (rhythm, weight, timing and spacing as separate ideas) matter just as much.
Each page explains the idea, gives frame counts, shows what was measured in Carvercat, and ends with how
to do it in Carvercat.

| Page | One line | Key numbers |
|---|---|---|
| [Timing and spacing](timing-and-spacing.md) | Frames per move vs distance per frame | duration ladder 6/9/12/18/24/36 f; exits ≈ 70% |
| [Slow in and slow out](slow-in-slow-out.md) | Easing: arrivals decelerate, exits accelerate | expo out does 83% of the travel in the first quarter |
| [Squash and stretch](squash-and-stretch.md) | Deform on impact, keep volume | 105/95 UI, 115/85 playful, 125/75 cartoon |
| [Anticipation](anticipation.md) | A small opposite move first | 10–25% of the action, 2–6 f |
| [Staging](staging.md) | One focal point per beat | dim support to 30–60%; text keeps contrast |
| [Straight ahead and pose to pose](straight-ahead-and-pose-to-pose.md) | Block poses with `hold`, then spline | `hold` jumps on the key's frame |
| [Follow-through and overlap](follow-through-and-overlap.md) | Parts settle after the body | children lag 2–5 f |
| [Arcs](arcs.md) | Curved paths | position keys are straight; pivot nulls make circles |
| [Secondary action](secondary-action.md) | Smaller reactions to the main move | 2–4 f later, 30–60% the size |
| [Exaggeration and overshoot](exaggeration.md) | Push past realism | back curve y1 1.3/1.56/1.75/2.0 → 3/10/16/25% |
| [Solid drawing in 2D](solid-drawing-2d.md) | One light, one world, consistent form | swap card faces on the zero-width frame |
| [Appeal](appeal.md) | Clarity, personality, polish | three-word personality per film |
| [Weight](weight.md) | Mass from timing and landing | light 8–14 f expo; heavy 24–40 f S-curve |
| [Rhythm](rhythm.md) | The pattern of events in time | stagger 3–6 f; breather every 8–12 s |
| [Easing reference (measured)](easing-reference.md) | 25 curves measured on one move | expo out: 83% at a quarter, settles 13 f into 20 |
| [Springs and damping](springs.md) | Multi-swing overshoot, baked to keys | ζ 0.3 → 35%, 0.5 → 16%, 0.7 → 4.6% |
| [Holds and stillness](holds-and-stillness.md) | Keeping holds alive | qc calls a 6% push over 4 s a freeze: judge holds by eye |

Lab projects: [labs/](../labs/README.md). The companion pages built around the verified Library templates are in
[craft/principles](../../ai/references/craft/principles/README.md); these wiki pages add the lab measurements. The craft summary these pages expand on:
[motion principles](../../ai/references/craft/motion-principles.md).
