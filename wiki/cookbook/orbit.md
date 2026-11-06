---
id: cookbook/orbit
title: Make something orbit
section: cookbook
tags: [orbit, circle, rotate around, pivot, null, parent, satellite, loop]
styles: [funky, explainer, futuristic-hud, data-viz]
topics: [rigging, loops]
related: [principles/arcs, techniques/camera-moves-2d, cookbook/seamless-loop, cookbook/screen-shake]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://blog.cg-wire.com/camera-work-in-animation/, https://motiondesign.school/blog/loopin-and-loopout/]
---

# Make something orbit

**Goal.** An object that travels round a centre on a perfect circle, at a steady speed, looping.

## Steps

1. A **pivot null** at the centre of the orbit (an invisible tiny ellipse, opacity 0).
2. The object placed at the radius from the pivot (300 px right of it here).
3. Parent the object to the pivot (`parent.assign`; on 0.1.6 select the object, then the pivot last).
4. Key the pivot's `rotate` `"0deg"` → `"360deg"` (clockwise on screen) or `"-360deg"` (counter-clockwise), `linear`, over
   the loop length, with the last key on the frame after the last ([loop seamlessly](seamless-loop.md)).
5. Several satellites: parent them all to one pivot at different angles, or give each its own pivot for
   different speeds.

## Measured in Carvercat 0.1.6

Comp `K Orbit` in [cookbook lab 3](../labs/README.md#cookbook-lab-3carverproj): pivot at (960, 540),
`rotate` `"0deg"` → `"360deg"` over f0–f90, a 60 px planet starting at (1260, 540); `inspect probe`:

| Frame | 0 | 15 | 30 | 45 | 60 | 75 | 89 |
|---|---|---|---|---|---|---|---|
| Planet x, y (px) | 1260, 540 | 1110, 800 | 810, 800 | 660, 540 | 810, 280 | 1110, 280 | 1259, 519 |
| Distance from centre | 300.0 | 300.0 | 300.0 | 300.0 | 300.0 | 300.0 | 300.0 |

- Positive `rotate` went clockwise on screen (down first, y-down coordinates). (The 0.1.6 note, from the old stored rotation: negative went clockwise.)
- The radius held at 300.0 px at every sampled frame.
- `inspect lint`: **1 error** `never_visible` on the pivot null (an intentional invisible parent).

## Traps

- Lint reports an invisible parent as an error: [FR-041](../../ai/references/known-issues.md#fr-041).
- `parent.assign` parents to the last-selected object on 0.1.6: [KI-120](../../ai/references/known-issues.md#ki-120).
- Nested-comp instances ignore their parent; orbit them with their own keys:
  [KI-119](../../ai/references/known-issues.md#ki-119).
- In the project file a child's stored position is an offset from the comp centre
  ([JSON authoring](../../ai/references/app/json-authoring.md#units-and-semantics-verified)).

## In Carvercat

- Library: `Orbit end card` ([fk-orbit-end](../../ai/patterns/fk-orbit-end.md)), `Radar sweep`
  ([fh-radar](../../ai/patterns/fh-radar.md)).
- Rigs and pivots: [rigging](../../ai/references/drawing/rigging.md). Background: [arcs](../principles/arcs.md).
