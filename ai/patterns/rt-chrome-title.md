# Chrome title

**Template** `rt_chrome_title` · Retro pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `RT Chrome title` in `categories/retro/rt-lab-2`.

"TURBO" (ExtraBold 240 px) with an 80s chrome fill: a static vertical gradient from pale sky to a bright band, a hard step to dark purple at the middle, and magenta at the bottom. A glowing pink horizon line and a yellow subline. 90 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Chrome horizon | 0 | Trim end 0 → 1 on twos, 14 f | settles **f10** |
| Chrome word | 4 | Rise - on twos | position settles **f14** |
| Chrome sub | 16 | Rise - on twos | |

Lint 0 errors, 0 warnings; `inspect qc` (240 px) found no flashes. Placed into a fresh comp: lint 0/0/0.

## How the chrome is made
`text_fill.paint = gradient` and a `gradient` object with stops 0 / 0.48 / 0.52 / 1 and start [0.5, 0] → end [0.5, 1] (object-local, y down: stop 0, the sky, is at the top of the word). The two stops 0.04 apart make the hard horizon step. Measured on 0.1.6: a **static** text gradient renders; its endpoints cannot be animated ([KI-009](../references/known-issues.md#ki-009) c).

**Fixed 2026-10-28 ([KI-155](../references/known-issues.md#ki-155)).** The chrome rendered upside down: magenta at the top and the sky at the bottom. The endpoints had been written y up (`[0.5, 1]` → `[0.5, 0]`); text gradients, like shape gradients, are object-local with y down. Measured on 0.1.6 (rev 1105) at f60 down the letters: sky `(172, 233, 255)` near the top, bright `(231, 248, 255)` just above the middle, dark purple `(95, 48, 135)` under the step, magenta `(186, 92, 220)` at the bottom. Placed into a fresh comp: lint 0/0/0. `categories/retro/rt-lab-2`, `rt-showcase-2` and the recipe `retro-night-promo` carry the same fix ([audit](../references/audits/gradient-direction-audit-2026-10-28.md)).

Inspiration: 80s chrome logotypes. No external text or code was used.
