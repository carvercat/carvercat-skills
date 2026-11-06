---
id: principles/straight-ahead-and-pose-to-pose
title: Straight ahead and pose to pose
section: principles
tags: [pose to pose, straight ahead, blocking, key poses, hold keys, stepped, splining, workflow]
styles: [all]
topics: [workflow, keyframing]
related: [principles/timing-and-spacing, principles/slow-in-slow-out, workflow/animatics, workflow/storyboards, techniques/looping]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation, https://skills.cat/skills/dylantarre/animation-principles/video-motion-graphics, https://learn.toonboom.com/modules/animation-principles/topic/activity-1-experimenting-with-space-and-time]
---

# Straight ahead and pose to pose

Two ways to build a move. **Pose to pose**: set the important poses first, check the timing, then fill
in how the object travels between them. **Straight ahead**: build frame after frame from the start, and
let the motion find itself. Motion graphics is almost always pose to pose; straight ahead lives on in
hand-drawn effects, organic wiggles and procedural noise.

## The idea

- **Key poses** tell the story (start, extreme, landing). **Breakdowns** decide how it gets there (the
  arc, the overshoot). **In-betweens** are the easing.
- **Blocking**: first show only the key poses as jumps, with no interpolation, to judge timing without
  being seduced by smooth curves. Then switch to smooth easing ("splining") and polish.
- Straight ahead suits chaos: sparks, scribbles, flicker, jitter, hand-drawn boil. It is unpredictable,
  which is the point.
- Mix them: block the main object pose to pose, add a straight-ahead flourish on top.

## Rules of thumb

- Block every scene before polishing any of them; fix timing while changes are cheap.
- Key the extremes, not the middle: a move needs a start, an end and maybe one breakdown.
- Keep keys on whole frames and on the project's duration ladder.
- After splining, re-check: smooth curves often make a move feel later and softer than the blocked version.

## Measured in Carvercat: Hold keys as blocking

Two dots keyed at the same three poses (f10, f20, f30). One uses `hold` (the 0.1.6 note: on the arriving keys; today it is the `ease` of the key before each pose), the other
S-curve (probe):

| Frame | 10 | 15 | 19 | 20 | 25 | 29 | 30 |
|---|---|---|---|---|---|---|---|
| `hold` (blocking) | 300 | 300 | 300 | **960** | 960 | 960 | **1620** |
| S-curve (splined) | 300 | 630 | 942 | 960 | 1290 | 1602 | 1620 |

`hold` on a key keeps the previous value through the segment and jumps exactly on the key's frame. That
is a stepped preview of the poses: change the `ease` to quad out / S-curve / a `cubic-bezier` when the timing
works, and nothing else has to move.

## Do and don't

- Do block with `hold`, review the timing, then spline.
- Do keep the number of keys low; every extra key is a place for a bump.
- Don't polish curves before the client has seen the blocked timing.
- Don't use straight-ahead keying for anything that must hit exact marks (beats, text holds).

## Checklist

- [ ] Every scene was reviewed blocked (stepped) before polishing.
- [ ] Each move has only the keys it needs.
- [ ] After splining, `inspect timing` still shows the settle frames you approved.

## In Carvercat

- Curve names on this page (S-curve, quad out) are `ease` strings: [names](easing-reference.md#names-used-in-this-wiki).
- Template examples with measured numbers and lint traps for this principle: [craft principle page](../../ai/references/craft/principles/straight-ahead-and-pose-to-pose.md).
- Blocking: set `ease: "hold"` on each key (the value holds until the next key); spline later by changing only the `ease`.
  Old way, accepted for one release: `"easing": "Hold"` on the arriving keys.
- Stepped on purpose ("on twos"): `Rise - on twos`, `Pop - on twos`, `Exit down - on twos`
  ([Retro](../../ai/patterns/retro.md)); stepped glitches: `Glitch in`, `Glitch out` ([Glitch](../../ai/patterns/glitch.md)).
- Straight-ahead texture: many keys from a script (`ai/scripts/motion/curves.py`) or a noise of small
  `hold` keys on position and rotation, as the Glitch pack does.
- Move a block of keys in time without retyping: `key.box`.
- Lab: comp `W Blocking` in [the principles lab](../labs/README.md).
