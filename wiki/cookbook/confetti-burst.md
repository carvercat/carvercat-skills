---
id: cookbook/confetti-burst
title: Burst confetti from a point
section: cookbook
tags: [confetti, burst, celebration, particles, explosion, success, party, scatter]
styles: [funky, cartoon-bounce, social-short-form, saas-ui]
topics: [shapes, timing]
related: [principles/weight, principles/arcs, cookbook/tile-grid-stagger, cookbook/pop-in]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Confetti, https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation]
---

# Burst confetti from a point

**Goal.** A celebration: about thirty small pieces shoot out of one point, slow down, then tumble and
fall while fading.

## Steps

1. Thirty small shapes (14 × 26 px rectangles and 18 px dots) in five or six brand colours, all starting at
   the burst point on the burst frame. Generate them from a fixed random seed so a re-run gives the same
   burst.
2. Two position segments per piece:
   - **out**: to a point 260–520 px away, at an angle in the upper fan (200°–340°, screen y down), over
     12 f with **decelerate**;
   - **fall**: from there 420–620 px down with a sideways drift of ±80 px, over 50 f with **accelerate**.
3. Scale 0.3 → 1 over the first 6 f; `rotate` `"0deg"` → ±360–720deg `linear` for the whole life (random sign; positive is clockwise).
4. Opacity 1 → 0 over the last 14 f, so pieces fade before they leave the frame.

## Measured in Carvercat 0.1.6

Comp `K Confetti` in [cookbook lab 6](../labs/README.md#cookbook-lab-6carverproj): 30 pieces, seed 7, burst at
(960, 640) on f10, out until f22, fall until f72; `inspect probe` on all 30:

- At f16 (6 f in) the furthest piece was already 488.3 px out; at f22 the pieces sat **266.0–513.8 px** from
  the burst point, the highest at y 142.5. Decelerate puts most of the travel in the first frames.
- At f72 they spread from y 650.5 to 985.6 (none below the frame), and the highest opacity was 1.0 at
  f58, 0.5 at f65, 0.07 at f71, **0 from f72**.
- `inspect qc`: no flash findings. `inspect lint`: 0 errors, 0 warnings, 60 notes (`speed_jump` and a
  repeated opacity key on each piece; the out-segment ends at full speed into the fall).

## Traps

- Each piece is its own clip; hundreds of pieces are better written into the project file than sent as
  MCP batches: [KI-118](../../ai/references/known-issues.md#ki-118).
- There is no particle system; a burst is keyed pieces. Keep the count small enough to read (20–40).
- Lint notes scale with the piece count; read them for errors, not volume.

## In Carvercat

- Curve names on this page (decelerate, accelerate) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Sticker burst` ([ct-sticker-burst](../../ai/patterns/ct-sticker-burst.md)), `Burst`, `Sparkle`,
  `Star`.
- Background: [weight](../principles/weight.md), [arcs](../principles/arcs.md).
