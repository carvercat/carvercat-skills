---
id: cookbook/weather-icon-loop
title: Loop an animated weather icon
section: cookbook
tags: [weather, icon, sun, cloud, rain, loop, animated icon, forecast]
styles: [explainer, saas-ui, cartoon-bounce, social-short-form]
topics: [loops, shapes, rigging]
related: [cookbook/seamless-loop, cookbook/orbit, cookbook/loading-spinner, techniques/looping]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/icon-usability/]
---

# Loop an animated weather icon

**Goal.** A "sun behind a cloud with rain" icon that loops seamlessly: the sun's rays turn, the cloud drifts
out and back, the drops fall.

## Steps

1. **Sun**: a 200 px disc. **Rays**: eight rounded rectangles 20 × 64 px, 150 px from the sun's centre at 45°
   steps, each rotated to point outwards.
2. A **null** at the sun's centre; select the rays, then the null last, and `parent.assign`. Key the null's
   `rotate` `"0deg"` → **`"45deg"`** over the loop (`linear`). Eight rays repeat every 45°, so the last frame matches the
   first.
3. **Cloud**: three ellipses and a rounded base, all parented to a "Cloud" null; key the null x out 24 px and
   back (S-curve, f0 → f30 → f60).
4. **Drops**: each falls 120 px in 20 f (`linear`) and jumps back with a `hold` key; three drops offset by 7 f.
   The loop length (60) is a whole number of drop cycles.
5. Comp 60 f, last keys on f60 ([seamless loop](seamless-loop.md)).

## Measured in Carvercat 0.1.6

Comp `K Weather` in [cookbook lab 8](../labs/README.md#cookbook-lab-8carverproj); `inspect probe` on Ray 1
(angle measured clockwise from straight up):

| Frame | 0 | 15 | 30 | 45 | 59 |
|---|---|---|---|---|---|
| Ray 1 angle | 0.0° | 11.26° | 22.5° | 33.74° | 44.27° |
| Ray 1 distance from the sun centre | 150.0 | 150.0 | 150.0 | 150.0 | 150.0 |
| Cloud x | 1000.0 | 1012.0 | 1024.0 | 1012.0 | 1000.1 |

- A **positive** `rotate` turns the rays **clockwise** on screen (stored as a negative rotation in 0.1.6); 0.75° a frame, so f60 = 45° = f0.
- Drop 1: y 660 on f0, 6 px a frame, 774 on f19, back to 660 on **f20** (the Hold key), again on f40.
- `inspect qc`: loop seam **0.0**. `inspect lint`: **2 errors**, `never_visible` on the two nulls (they are
  transparent on purpose), and `speed_jump` notes on the drops' jumps.

## Traps

- Parent with `parent.assign`, not by writing a parent id into the file: the command keeps each child where it
  is ([KI-153](../../ai/references/known-issues.md#ki-153) for parenting at a scaled pose).
- Lint calls nulls `never_visible` errors: [FR-041](../../ai/references/known-issues.md#fr-041).
- `qc` compares brightness only ([KI-140](../../ai/references/known-issues.md#ki-140)): the probe table above
  is the real proof that f59 runs into f0.

## In Carvercat

- Curve names on this page (S-curve) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Cloud`, `Drop` and `Ring` shapes, `Sparkle` sticker; `Cycle loop` scene.
- Background: [looping](../techniques/looping.md), [orbit](orbit.md) (the same rotating parent).
