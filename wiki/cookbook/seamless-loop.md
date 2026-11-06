---
id: cookbook/seamless-loop
title: Loop seamlessly
section: cookbook
tags: [loop, seamless, gif, cycle, spinner, background, seam]
styles: [all]
topics: [loops, timing]
related: [techniques/looping, workflow/delivery, techniques/wiggle-and-jitter, cookbook/progress-bar]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://motiondesign.school/blog/loopin-and-loopout/, https://aejuice.com/blog/how-to-make-a-seamless-loop-in-after-effects]
---

# Loop seamlessly

**Goal.** A comp that plays end to start with no jump: a spinner, a bob, a pulse, a background for a
GIF or a social loop.

## Steps

1. Pick the loop length *N* (60 f = 2 s here) and make the comp exactly *N* frames.
2. Put the **last key on frame *N***, one frame past the last rendered frame (f59), with the **same value
   as frame 0** (or an equivalent pose: 90° for a square, 72° for a five-point star).
3. Rotation that keeps turning: `linear` from f0 to f*N*, so the step across the seam equals every other
   step.
4. Back-and-forth moves (bob, pulse): three keys, f0 → f*N*/2 → f*N*, S-curve on both halves, so the
   speed is zero at the seam.
5. Check frame *N* − 1 against frame 1: they should mirror each other around frame 0.

## Measured in Carvercat 0.1.6

Comp `K Loop` in [cookbook lab 1](../labs/README.md#cookbook-lab-1carverproj), 60 f, `carvercat_inspect
probe` at frames 0, 1, 58 and 59:

| Object | Keys | f1 | f59 |
|---|---|---|---|
| Square spinner | `rotate` `"0deg"` → `"90deg"` `linear`, f0 → f60 | 1.5° | 88.5° (1.5° short of 90° ≡ 0°) |
| Bob | y 540 → 400 → 540 px, S-curve, f0/f30/f60 | 539.5 px | 539.5 px |
| Pulse | scale 1 → 1.25 → 1, S-curve | 160.1 px wide | 160.1 px wide |

- `inspect qc`: `loops_cleanly: true`, mean luma difference **0.001** across the seam.
- `inspect lint`: **0 errors, 0 warnings, 0 notes**.

## Traps

- The qc seam check only compares brightness, so a shape that jumps position or rotation at the seam can
  still pass: [KI-140](../../ai/references/known-issues.md#ki-140). Compare f1 and f*N* − 1 with `probe`
  as above.
- Staggered parts finish gap × (parts − 1) late and can run past the loop end:
  [KI-050](../../ai/references/known-issues.md#ki-050).

## In Carvercat

- Curve names on this page (S-curve) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Rotation `rotate`, position, scale, all with `linear` or S-curve keys.
- Delivery as GIF or a looping MP4: [delivery](../workflow/delivery.md).
- Library loops: `Segment loader` ([fh-loader](../../ai/patterns/fh-loader.md)), `Radar sweep`
  ([fh-radar](../../ai/patterns/fh-radar.md)), `Pattern drift` ([fk-pattern-drift](../../ai/patterns/fk-pattern-drift.md)).
- Background: [looping](../techniques/looping.md), [wiggle and jitter](../techniques/wiggle-and-jitter.md).
