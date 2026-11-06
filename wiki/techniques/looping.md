---
id: techniques/looping
title: Seamless loops
section: techniques
tags: [loop, cycle, seamless, gif, background, ambient, seam, ping-pong]
styles: [social-short-form, futuristic-hud, funky, saas-ui, retro]
topics: [loops, delivery]
related: [principles/timing-and-spacing, techniques/parallax, principles/straight-ahead-and-pose-to-pose, workflow/delivery]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://motiondesign.school/blog/loopin-and-loopout/, https://community.adobe.com/t5/after-effects-discussions/how-to-make-a-seamless-loop-on-gif/m-p/15049808, https://aejuice.com/blog/how-to-make-a-seamless-loop-in-after-effects]
---

# Seamless loops

A loop plays end to start with no visible jump: background textures, spinners, idle animations, social
GIFs, screens at events. A loop is right when the last frame flows into the first exactly as any frame
flows into the next.

## The idea

- **The seam is between the last frame and the first.** Frame N must be the frame that would come *after*
  the last one, not a copy of the first; otherwise the first pose shows twice and the loop hitches.
- **Cycles must close**: every animated value returns to its start value (or to a visually identical one:
  a square rotated 90° looks like the square at 0°).
- **Constant motion loops with `linear`**; ease-out or ease-in at the seam makes a visible stop.
- **Ping-pong** (there and back) loops with S-curve on both halves: speed is zero at both ends, so the
  turnaround is smooth.
- Long loops hide repetition: 4–8 s for ambient backgrounds, 1–2 s for spinners and icons.

## Rules of thumb

- Make the comp exactly one cycle long; key the closing value on the frame **after** the last frame
  (frame = comp length).
- Rotations: one full turn (360°) or a turn equal to the shape's symmetry (90° for a square, 72° for a
  5-point star).
- Several looping elements: give them cycle lengths that divide the comp length (60 f comp: 60, 30, 20,
  15 f cycles).

## Measured in Carvercat

A 60 f comp: a square rotating `rotate` `"0deg"` → `"90deg"` (the 0.1.6 note: 0 → −90°) with keys at f0 and f60 (`linear`), and a dot bobbing down and
back with keys at f0, f30, f60 (S-curve). With the comp ending at frame 59, frame 60 is the unseen
"next" frame, so the loop closes perfectly. `carvercat_inspect {mode:"qc"}` reported
`loops_cleanly: true`, mean luma difference 0.001.

A deliberately broken copy (rotation stopping at 80deg with quad out, the dot ending 20 px low at f59)
**also** reported `loops_cleanly: true` (difference 0.003). The qc seam check compares overall brightness at
a small size, so it cannot see a shape that jumps position or angle at the seam. Check geometry yourself:

- `carvercat_inspect {mode:"probe", objects:[...], from:0, to:59}`: the values at frame 59 plus one frame
  of motion should equal frame 0.
- `carvercat_inspect {mode:"expect", checks:["\"Bob\" at 1260,540 within 2 at 0"]}` and the same position
  for the predicted next frame.

(Logged as [KI-140](../../ai/references/known-issues.md#ki-140).)

## Do and don't

- Do key the closing value on frame = comp length, not on the last visible frame.
- Do use `linear` for one-way cycles and S-curve for ping-pong.
- Don't trust a brightness-only seam check for moving shapes.
- Don't loop text that must be read; it competes with itself on every pass.

## Checklist

- [ ] Every animated value closes its cycle on frame = comp length.
- [ ] No easing that stops at the seam on a one-way cycle.
- [ ] Probe frame 0 and the predicted frame after the last: they match.
- [ ] `qc` shows no flashes and no freezes.

## In Carvercat

- Curve names on this page (S-curve, quad out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Comp length: `comp.duration {frames}`; in a project file `scene.duration`.
- Rotation loop: `rotate` keys at 0 and at the comp length, `linear`.
- Gradient and dash loops: `shape.fill.gradientOffset` (−1 to 1, with `Repeat` once/repeat/pingpong) and
  the trim effect's `Offset` (`trimOffset`, %) are keyframeable and can drive one-way cycles; the travelling dash in
  [line drawing](line-drawing.md) was measured, the gradient loop was not.
- Ready-made one-way loops: `Radar sweep` ([fh-radar](../../ai/patterns/fh-radar.md)), the synthwave grid
  ([rt-synthwave](../../ai/patterns/rt-synthwave.md)), `Noise bars overlay` ([gl-noise-bars](../../ai/patterns/gl-noise-bars.md)).
- Lab: comps `T Loop good` and `T Loop bad` in [the techniques lab](../labs/README.md).
