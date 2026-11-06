# 80s action title

**Template** `rt_action_title` (Library name "80s action title") · Retro pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `RT Action title` in `categories/retro/rt-lab-3`.

For briefs like "80s action movie title", "blockbuster trailer card", "coming this summer". STEEL THUNDER in chrome type (a static text gradient: sky, bright band, dark horizon, hot metal) with a two-step hard extrusion (two shadows, dark red 6 px and brown 12 px), flying in from far away on twos; a glint and a lens streak flare once on the S; a tracked tagline and release line rise on twos over a sunset glow. 150 f, holds. Full-frame dark ground included. The title and dates are invented stand-ins.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Sunset glow (1920 × 360 px, transparent red at the top → orange at the bottom) | 0 | opacity 0 → 1 on twos, 12 f | **f12** |
| Title (ExtraBold 190 px, chrome gradient, two hard shadows) | 4 | scale 0.2 → 1 on an expo curve, stepped every 2 f (10 keys to f22); opaque on twos by f8 | **0%**, settles **f16** |
| Glint (4-point star, 150 px, glow) and Streak (440 × 8 px, glow) | 26 | scale 0 → 1 → 0 on twos (peak f34), the star turns 45° one way; both clips end at f42 | gone **f42** |
| Tagline (Bold 56 px, tracking 1.3) | 30 | Rise - on twos as keys (43 px) | **f40** |
| Release (ExtraBold 44 px, mustard) | 40 | the same | **f50** |

Lint 0 errors, 0 warnings in the lab (2 notes: `speed_jump` on the stepped rises, the on-twos look); placed into a fresh comp 0/0/0. `inspect qc` (240 px): no flashes. Text-gap audit: closest pair 73.9 px (tagline and release). The gradients were checked with looks: the chrome has its sky at the top, and the glow is dark at the top and orange at the bottom ([KI-155](../references/known-issues.md#ki-155)). Full-frame looks of the placed instance at f6 and f34 (the glint and streak at their widest) show nothing cut ([KI-144](../references/known-issues.md#ki-144)).

## Steps
1. Edit the title; keep it under about 1500 px wide at 190 px (the glint sits 50 px in from its left edge, computed with `cc.textw` in `retro_lab3.py`).
2. Over footage, delete `Title ground` and `Sunset glow`; the chrome needs a dark picture behind it.

## Pitfalls
- Two `shadow` effects on one text both render (measured on the look): use them for a stepped extrusion instead of stacked copies of the text, which lint would call `text_overlap`.
- The chrome cannot animate (text gradients are static, KI-009 c): the size move carries it.

Inspiration: 80s action-film title cards and chrome lettering. No external text or code was used.
