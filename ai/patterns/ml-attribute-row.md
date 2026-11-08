# Attribute row

**Template** `ml_attribute_row` · Minimal Luxury pack · **Verified 0.1.8.1 (rev 1127)**, comp `ML Attribute row` in `categories/minimal-luxury/ml-lab-2`.

Three tracked attributes ("HANDMADE", "FLORENCE", "18K GOLD", Regular 28 px, tracking 1.6) 520 px apart on one line (centres at x 440, 960, 1480), with 8 px gold dots midway between them. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Attribute 1–3 | 10, 28, 46 | Slow fade in; tracking 1.60 → 1.64 over the clip | Attribute 1 size settles **f38**, Attribute 3 **f74** |
| Separator 1–2 | 22, 40 | Slow fade in | |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0. No overshoot (the pack's style rule).

Measured ink at f140 (`carvercat_authoring geometry`): Attribute 1 x 262–618, dot 696–704, Attribute 2 790–1130, dot 1216–1224, Attribute 3 1311–1649: a 78–92 px gap on each side of each dot.

## Pitfalls
- **Fixed 2026-10-28.** The first release placed the words 400 px apart at 34 px. Each word is about 432 px wide at that size and tracking, so they ran into each other and a dot covered the F of FLORENCE, and lint did not report it ([KI-138](../references/known-issues.md#ki-138)). Measure tracked text before spacing it.

Inspiration: craft and provenance captions in luxury product films. No external text or code was used.
