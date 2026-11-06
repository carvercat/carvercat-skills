---
id: principles/anticipation
title: Anticipation
section: principles
tags: [anticipation, wind-up, preparation, wind back, telegraph]
styles: [cartoon-bounce, funky, sports, kinetic-typography, social-short-form]
topics: [preparation, attention]
related: [principles/exaggeration, principles/squash-and-stretch, principles/staging, principles/timing-and-spacing, sound-and-timing/beat-sync]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation, https://skills.cat/skills/dylantarre/animation-principles/video-motion-graphics, https://learn.toonboom.com/modules/animation-principles/topic/activity-1-experimenting-with-space-and-time, https://www.schoolofmotion.com/blog/animation-tricks-follow-through-after-effects]
---

# Anticipation

Before a big action, a small opposite one. A jumper crouches, a pitcher winds back, a button dips before
it pops. Anticipation tells the eye where to look a moment before the action, so the action is not missed.

## The idea

- The wind-up moves **against** the main action: back before forward, smaller before bigger, down before up.
- It is short and small compared with the action, and it is followed by the fastest part of the move.
- The bigger and more sudden the action, the more it needs anticipation. Utility moves (a label sliding
  in) need none.
- In graphics, a "stillness before the hit" can be the anticipation: a held frame or a slow push just
  before a beat.

## Rules of thumb

- Size: 10–25% of the action. A 600 px slide winds back 60–90 px; a pop to 112% dips to 90–95%.
- Time: 2–6 f for the wind-up, about 20% of the whole move. Phase split for a character-like move:
  wind-up 20%, action 50%, settle 30%.
- Ease the wind-up out (it slows into its extreme), then release on a strong ease out.
- Anticipation sits **before** the beat; the landing sits **on** it.
- One anticipated move per beat. If everything winds up, nothing does.

## Measured in Carvercat

| Test | Keys | Result (probe) |
|---|---|---|
| Slide | x 500 at f10, x 440 at f16 (quad out), x 1400 at f30 (expo out) | back 60 px by f16; 66% of the forward travel done by f18, 2 f after release; at rest f25 |
| Pop | scale 1.0 at f10, 0.90 at f16 (quad out), 1.12 at f24 (expo), 1.0 at f32 (S-curve) | dip to 0.925 at f13 and 0.90 at f16; 1.08 at f18; peak 1.12 at f24; rest f32 |

The expo release makes the contrast: after six slow frames backwards, the object covers two thirds of the
distance in two frames. That contrast is what reads as "spring".

## Do and don't

- Do anticipate hero entrances, slams, jumps and logo hits.
- Do keep the wind-up on the same axis as the action.
- Don't anticipate exits that should just get out of the way, or captions people are reading.
- Don't make the wind-up so long that it reads as a separate move (over about 8 f).

## Checklist

- [ ] The wind-up is opposite to the action and 10–25% of its size.
- [ ] It lasts 2–6 f and eases into its extreme.
- [ ] The release is the fastest part of the whole move.
- [ ] With music, the release lands on the beat.

## In Carvercat

- Curve names on this page (S-curve, expo out, quad out) are `ease` strings: [names](easing-reference.md#names-used-in-this-wiki).
- Template examples with measured numbers and lint traps for this principle: [craft principle page](../../ai/references/craft/principles/anticipation.md).
- Build it with three keys on one property: rest, wind-up (quad out), target (a strong ease out such as
  expo out, `cubic-bezier(0.16, 1, 0.3, 1)`), then optionally a settle key (S-curve). Each key's `ease` shapes the segment it leaves.
- Presets with anticipation built in: `Anticipate jump out` (7 f crouch + 13 f launch) from
  [Cartoon Bounce](../../ai/patterns/cartoon-bounce.md); `Exit shrink - anticipate` (grows to 1.076 then
  to 0, peak 5 f in) from [Motion Patterns](../../ai/patterns/README.md); `Impact slam` from
  [Sports](../../ai/patterns/sports.md).
- For text, put the wind-up on the clip (the object's own `x`, `y`, `scale`; old: `transform.placement`) rather than on a staggered text channel,
  so the whole line winds up together.
- Check with `carvercat_inspect {mode:"curves"}`: the wind-up shows as the first key's value, and the
  peak speed should sit just after it.
- Lab: comp `W Anticipation` in [the principles lab](../labs/README.md).
