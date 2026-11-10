---
id: techniques/directional-blur-and-speed
title: Directional blur and speed (measured)
section: techniques
tags: [directional blur, speed, whip, streak, smear, impact, push, motion blur, wipe]
styles: [sports, social-short-form, kinetic-typography, cartoon-bounce, glitch]
topics: [speed, effects, transitions]
related: [techniques/motion-blur, techniques/film-grain, cookbook/whip-in-title, techniques/shadow-and-glow-in-motion]
verified: design/1 (Carvercat 0.1.10)
source_inspiration: [https://github.com/carvercat/carvercat-skills]
---

# Directional blur and speed (measured)

An object that crosses the frame in six frames cannot be sharp: the eye expects a streak. A directional blur is that streak,
chosen by you: a length and an angle, keyed so it is long while the object is fast and gone when it lands.

## The idea

- **Fast means long, then zero.** The streak is the length of the move in the fastest frames, and it must be 0 on the frame the
  object comes to rest, so the landing is crisp.
- **Along the move.** Set the angle to the direction of travel: 0 for a horizontal move, 90 for a vertical one, the move's own
  angle for a diagonal. A centred blur has no arrow, so 0 and 180 are the same pixels.
- **Short and fast.** 3 to 8 frames carry the streak. A streak that stays on reads as a soft, slow picture.
- **Streak plus squash.** On a slam or a bounce, pair the blur with a scale overshoot; the blur gives speed, the squash gives weight.

## Measured in Carvercat (design/1)

A white 600 x 400 block over black, rendered at 1920 x 1080 (verified: directional-blur-and-speed,
`wiki/tools/verify_keyed_pages.py`). The 10 to 90 % width of an edge's ramp is read from the rendered pixels (converted to linear
light, interpolated).

| `directionalBlur` | Ramp across the vertical edge | Ramp across the horizontal edge |
|---|---|---|
| `"10px"` | 8.0 px | 1.2 px (a hard edge) |
| `"40px"` (the default length) | 32.0 px | 1.2 px |
| `"100px"` | 80.0 px | 1.2 px |
| `"200px 0deg"` | 159.9 px | 1.2 px |
| `"40px 90deg"` | 1.2 px | 32.0 px |
| `"100px 45deg"` | 56.8 px | 56.8 px |
| `"100px 180deg"` | 80.0 px | 1.2 px (the same as 0deg) |

- A streak of length L softens an edge over **0.8 x L** along its own direction; across the streak the edge stays hard (1.2 px
  is a pixel-hard edge here).
- A 45deg streak gives 0.8 x L x cos 45 = 56.6 px on each edge.
- A key moves the length: `0px` at frame 0 to `100px` at frame 10 reads 50 px at frame 5.
- Resolve: exact (measured on Resolve Studio, mean difference under 0.1 of 255); After Effects: approximate (a tent kernel; mean
  difference 0.2 to 0.7 of 255 up to 100 px).

## Rules of thumb

- Whip in or out: 160 to 300 px at the start, to 0 on landing, `expo` or accelerating ease, 6 to 10 f.
- Slam: a vertical 60 to 120 px streak on the landing frame, gone in 3 to 4 f.
- Push or wipe: the full-frame panel gets 160 to 240 px along its travel.
- Never on text the viewer must read at that frame.
- For a long curved move prefer [motion blur](motion-blur.md) (it follows each frame's real travel); use directional blur when you
  want to direct the streak.

## Checklist

- [ ] Angle matches the move (0 horizontal, 90 vertical, or the move's angle).
- [ ] Length keyed to 0 on the resting frame.
- [ ] No streak on the frames where text must be read.
- [ ] `carve.preflight` read. The effect is exact in Resolve and approximate in After Effects; on 0.1.10 the preflight line wrongly says `unsupported` ([KI-171](../../ai/references/known-issues.md#ki-171)).

## In Carvercat

- Design key `directionalBlur` (`"40px 30deg"`), or `directional-blur(...)` in `filter`; keyable by name;
  `effect.add {cap: "dirblur"}`. Full reference: [directional blur](../../ai/references/effects/directional-blur.md).
- Library: the Cartoon Bounce pack's `Smear whoosh`, the Sports pack's `Goal slam`, the Social pack's `Swipe up`, the Transitions
  pack's `Slide wipe`, the Kinetic Typography pack's `Line reveal`
  ([ct-smear-whoosh](../../ai/patterns/ct-smear-whoosh.md), [sp-goal-slam](../../ai/patterns/sp-goal-slam.md),
  [ss-swipe-up](../../ai/patterns/ss-swipe-up.md), [tx-cover-transitions](../../ai/patterns/tx-cover-transitions.md),
  [kt-line-reveal](../../ai/patterns/kt-line-reveal.md)).
- How-to: [a whip-in title with a streak](../cookbook/whip-in-title.md).
- Background: [motion blur](motion-blur.md), [styles: sports](../styles/sports.md).
