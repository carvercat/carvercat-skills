---
id: cookbook/clock-hand
title: Rotate a clock hand or needle about its end
section: cookbook
tags: [clock, hand, needle, gauge, pivot, anchor, rotate, timer, dial]
styles: [data-viz, explainer, futuristic-hud, retro]
topics: [rigging, data]
related: [principles/arcs, cookbook/orbit, cookbook/donut-fill, cookbook/countdown]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://blog.cg-wire.com/camera-work-in-animation/, https://www.geckoboard.com/blog/to-animate-or-not-to-animate/]
---

# Rotate a clock hand or needle about its end

**Goal.** A hand that turns about the dial's centre, not about its own middle.

## Steps

1. Draw the hand as a thin rectangle (10 × 200 px) **centred half its length away** from the pivot: for
   a dial centred at (960, 540), the hand's centre is (960, 440).
2. Set the anchor to the **bottom edge**: `transformOrigin` `"50% 100%"`. The shape stays
   where it is drawn and turns about that edge.
3. Key `rotate`: positive turns clockwise (`"0deg"` → `"360deg"` for one turn), `linear` for a
   clock, eased for a gauge needle.
4. A hub dot on top hides the joint.

## Measured in Carvercat 0.1.6

Comp `K Clock hand` in [cookbook lab 4](../labs/README.md#cookbook-lab-4carverproj): `rotate` `"0deg"` → `"360deg"`
over f0–f60, `inspect probe` on the hand's centre:

| Frame | 0 | 15 | 30 | 45 | 55 |
|---|---|---|---|---|---|
| Hand centre (x, y) | 960, 440 | 1060, 540 | 960, 640 | 860, 540 | 910, 453 |
| Distance from (960, 540) | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |

- The hand's middle stayed exactly half its length (100 px) from the dial centre at every sampled frame:
  it turns about its bottom end. At f15 it pointed to 3 o'clock: clockwise.
- `inspect lint`: **0 errors, 0 warnings, 0 notes**.

## Traps

- On nested comp instances the old `anchor` did **not** compensate the position and behaved differently (not re-measured for `transformOrigin`):
  [KI-109](../../ai/references/known-issues.md#ki-109).
- A rotating parent with an off-centre pivot made children drift (old `anchor`): [KI-108](../../ai/references/known-issues.md#ki-108).
- Turn it with `rotate`; the old rectangle `angle` is stored but not drawn: [KI-057](../../ai/references/known-issues.md#ki-057).

## In Carvercat

- Library: `Gauge` ([dv-gauge](../../ai/patterns/dv-gauge.md)), `Radar sweep` ([fh-radar](../../ai/patterns/fh-radar.md)).
- Pivots and joints: [rigging](../../ai/references/drawing/rigging.md). Background: [arcs](../principles/arcs.md).
