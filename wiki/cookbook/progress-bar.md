---
id: cookbook/progress-bar
title: Make a progress bar
section: cookbook
tags: [progress, loading, bar, fill, upload, percent, anchor, scale x]
styles: [saas-ui, data-viz, social-short-form, explainer, futuristic-hud]
topics: [data, ui]
related: [genres/ui-ux-demos, genres/data-stories, cookbook/count-a-number-up, cookbook/seamless-loop]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://m3.material.io/components/progress-indicators/overview, https://www.nngroup.com/articles/progress-indicators/]
---

# Make a progress bar

**Goal.** A bar that fills from its left edge to a value (72%), with a label that matches it.

## Steps

1. **Track**: a rectangle, 800 × 16 px, dark.
2. **Fill**: the same rectangle in the accent colour, on top. Set its `transformOrigin` to the **left edge**,
   `"0% 50%"`, so the scale grows from there.
3. Key `scale` from `[0, 1]` to `[value, 1]`, here `[0.72, 1]`. S-curve reads as a
   steady load; expo out reads as "fast, then nearly done".
4. The percentage can't count with plain text keys: fade in the final value as the bar arrives, or use a
   rolling counter ([count a number up](count-a-number-up.md)).

## Measured in Carvercat 0.1.6

Comp `K Progress bar` in [cookbook lab 1](../labs/README.md#cookbook-lab-1carverproj): fill `scale`
`[0, 1]` → `[0.72, 1]` over f10–f50, S-curve; `carvercat_inspect probe` on the fill.

| Frame | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 |
|---|---|---|---|---|---|---|---|---|---|
| Fill width (px) | 0 | 24.8 | 90.0 | 182.3 | 288.0 | 393.8 | 486.0 | 551.3 | 576.0 |
| Left edge (px) | 560 | 560 | 560 | 560 | 560 | 560 | 560 | 560 | 560 |

- The left edge stays put at every frame; the fill ends at 576 px = 0.72 × 800.
- Half of the final width at f30, the middle of the move.
- `inspect lint`: **0 errors, 0 warnings, 0 notes**.

## Traps

- The old `cornerRadius` capped at a quarter of the short side, so a fully round pill was not possible
  ([KI-121](../../ai/references/known-issues.md#ki-121)). `borderRadius: "50%"` makes a stadium (verified: a 440 × 110 rectangle reads 55 px). Note a scaled
  fill scales its radius too; for a round-ended bar that grows, a 2-point path with a round `strokeLinecap` and `trimEnd` is steadier.
- On nested comp instances the old `anchor` did not compensate the position (not re-measured for `transformOrigin`):
  [KI-109](../../ai/references/known-issues.md#ki-109).
- `text.content` cannot be keyed: [KI-051](../../ai/references/known-issues.md#ki-051).

## In Carvercat

- Curve names on this page (S-curve, expo out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Progress` (Carvercat Essentials), `Story progress bar (9:16)`
  ([ss-progress-bar](../../ai/patterns/ss-progress-bar.md)), `Progress rings`
  ([dv-progress-rings](../../ai/patterns/dv-progress-rings.md)), preset `Grow across (X)`.
- A bar that loops while waiting: [loop seamlessly](seamless-loop.md).
- Background: [UI and UX demos](../genres/ui-ux-demos.md), [data stories](../genres/data-stories.md).
