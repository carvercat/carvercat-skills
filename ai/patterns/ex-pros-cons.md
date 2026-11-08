# Pros and cons

**Template** `ex_pros_cons` (Library name "Pros and cons") · Explainer pack · **verified 0.1.8.1 (rev 1127; `ai/scripts/motion/verify_pack.py`: placed in a fresh 16:9 and a fresh 9:16 comp, lint 0/0/0, qc no flash; against the v1 original the silhouette differs by at most 0.00 % of pixels over 7 frames; object-level check pass)**, comp `EX Pros cons` in `categories/explainer/ex-lab-3`.

For briefs like "should you...", "remote work: worth it?", "product trade-offs". Two lists with plus and minus icons, then a seesaw that tips once towards the heavier side and a verdict line. Compare columns (old way / new way) has no verdict; this one decides. Light background included. 165 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Title "Working from home" (60 px ExtraBold) | 0 | Step in | |
| PROS header (green, white 36 px) and CONS header (coral) | 6 / 50 | Step in | |
| Pros items 1–3, Cons items 1–2: icon disc (58 px), sign, text (40 px), rule | 16, 28, 40 / 60, 72 | disc pops 0 → 100% (keyed back), sign and rule draw (6 f, 14 f), text steps in | disc overshoot **9.8%** |
| Seesaw beam, base, fulcrum | 84 | beam and base grow from the centre (scale X, expo 14 f), fulcrum pops | beam settles **f93** |
| Balls (green 128 px, coral 88 px) | 88 | pop; then ride the beam ends (position baked every frame f96–141) | pop settles **f99** |
| Tilt: left end down 8° | 96 | one overshoot to 9.3° (116.5%, f105), then settles | settles **f117** |
| Verdict "Worth it, on balance" (40 px) | 120 | Step in | settles **f129** |

`inspect curves` reads the beam's rotation overshoot as 19% (a baked lane, [KI-152](../references/known-issues.md#ki-152); the formula gives 16.5%). Lab comp lint on 0.1.8.1 (native size): 0 errors, 0 warnings, 15 notes. `inspect qc` (240 px): no flashes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 153 pairs, closest 26.0 px (item text / its icon). Full-frame looks at f104 (peak tilt) and f164: nothing cut; the raised ball clears the cons column by 48 px.

## Steps
1. Edit the two lists in `pros_cons()`; give the heavier list the bigger ball and the left end (or mirror `sign`, `rl`, `rr` and the verdict).
2. `TILT` sets the final angle (8°); the damped curve in `tilt()` gives one overshoot.

## Pitfalls
- A ball that rides a turning beam needs its centre on the beam's normal: end point ± L (cos t, −sin t), then (r + half the beam) along (−sin t, −cos t). Positions are baked every frame; rotating a parent would have needed the rig offset rule.
- Tracked caps were garbled at tracking 0.35 ("SCRP" for PROS): 1.0 is normal spacing and each 1.0 more adds about 1.3 em, so tags use 1.07 ([KI-117](../references/known-issues.md#ki-117)).

Inspiration: common explainer-video conventions (pros and cons, scales). No external text or code was used.
