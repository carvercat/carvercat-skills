---
id: cookbook/bounce-cycle
title: Loop a squash-and-stretch bounce cycle
section: cookbook
tags: [bounce, cycle, loop, squash, stretch, character, hop, pivot, anchor, mascot]
styles: [cartoon-bounce, funky, social-short-form]
topics: [rigging, looping]
related: [principles/squash-and-stretch, principles/weight, cookbook/seamless-loop, cookbook/map-pin-drop]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Squash_and_stretch, https://en.wikipedia.org/wiki/Walk_cycle]
---

# Loop a squash-and-stretch bounce cycle

**Goal.** A blob character that hops on the spot forever: squashes on the ground, stretches as it leaves,
floats at the top, stretches as it falls and squashes again, with its eyes riding along.

## Steps

1. Body: a 180 px circle standing on the ground line, with its `transformOrigin` on its **bottom** (`"50% 100%"`), so
   squash and stretch keep its feet on the ground.
2. Five poses on a 24 f loop (lift above the ground, scale X × Y):
   f0 contact 0 px, `scale` `[1.25, 0.75]` → f3 30 px, `[0.9, 1.12]` (decelerate) → f12 apex 300 px, `[1, 1]` (decelerate)
   → f21 30 px, `[0.9, 1.12]` (accelerate) → f24 = f0 (accelerate). Lift is `y` going up, so it is a negative change in `y`.
3. Eyes (no parenting): each eye's position = bottom pivot + its offset × the body's scale, keyed on the
   **same frames with the same easing**, plus the same scale. Because both values use the same eased
   fraction, the eyes stay locked to the body between keys.
4. A ground shadow that shrinks with height.
5. Comp length = the cycle (24 f); last key on f24 ([seamless loop](seamless-loop.md)).

## Measured in Carvercat 0.1.6

Comp `K Bounce cycle` in [cookbook lab 7](../labs/README.md#cookbook-lab-7carverproj), ground at y 800;
`inspect probe` on the body (bottom edge, width × height):

| Frame | 0 | 3 | 6 | 12 | 18 | 21 | 23 |
|---|---|---|---|---|---|---|---|
| Bottom (px) | **800.0** | 770.0 | 530.6 | 500.0 | 581.2 | 770.0 | 779.1 |
| Size | 225 × 135 | 162 × 201.6 | 178 × 182.4 | 180 × 180 | 174.6 × 186.5 | 162 × 201.6 | 181 × 181.6 |

- At contact the squashed body's bottom sat exactly on the ground (800.0); its apex is 300 px up at f12.
- The left eye stayed inside the body on every sampled frame: (920, 710) on the squash, (928, 380) at the
  apex.
- `inspect qc`: `loops_cleanly: true`, seam difference 0.006. `inspect lint`: 0 errors, 0 warnings, 3 notes
  (`speed_jump` at the contact, which is the point of a bounce).

## Traps

- Parenting the eyes to a squashing body bakes in the body's pose at the playhead; at the contact frame that
  is the squash: [KI-153](../../ai/references/known-issues.md#ki-153).
- A rotating parent with an off-centre pivot made children drift (old `anchor`): [KI-108](../../ai/references/known-issues.md#ki-108).
- The qc seam check is brightness only: [KI-140](../../ai/references/known-issues.md#ki-140).

## In Carvercat

- Curve names on this page (decelerate, accelerate) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Bouncing ball` ([ct-bouncing-ball](../../ai/patterns/ct-bouncing-ball.md)), `Character hop`
  ([ct-character-hop](../../ai/patterns/ct-character-hop.md)), `Squash land`, `Blinking face`.
- Background: [squash and stretch](../principles/squash-and-stretch.md), [weight](../principles/weight.md).
