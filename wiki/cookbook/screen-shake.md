---
id: cookbook/screen-shake
title: Shake the screen on an impact
section: cookbook
tags: [shake, camera shake, impact, slam, hit, null, parent, decay]
styles: [sports, kinetic-typography, funky, glitch, cartoon-bounce]
topics: [camera, impact, timing]
related: [techniques/wiggle-and-jitter, techniques/camera-moves-2d, accessibility/motion-sensitivity, cookbook/hit-on-the-beat, cookbook/pop-in]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://help.apple.com/motion/mac/5.4/en.lproj/motn13745f4a.html, https://docs.toonboom.com/help/toon-boom-studio/Content/TBS/User_Guide/016_Effects/001g_H2_ShakeEffect.html]
---

# Shake the screen on an impact

**Goal.** When a word or object slams down, the whole frame jolts and settles within a third of a second.

## Steps

1. Land the hit: apply `Impact slam` (or `Stamp`) to the word. Note its **impact frame**: `Impact slam`
   lands 5 f after the clip starts.
2. Add a **camera null** at the comp centre and parent everything that should shake to it
   (`parent.assign`: on 0.1.6 select the children, then the null last).
3. Key the null's position on the impact frame and every 2 f after it, alternating direction and
   shrinking: +24/−14, −18/+12, +12/−8, −7/+5, +3/−2, 0 px (x/y), S-curve. Six swings, 12 f.
4. Put the hit sound on the impact frame ([hit on the beat](hit-on-the-beat.md)).

## Measured in Carvercat 0.1.6

Comp `K Shake` in [cookbook lab 2](../labs/README.md#cookbook-lab-2carverproj): "GOAL" 260 px with
`Impact slam` from f10, null keys f15–f27, seven objects parented; `carvercat_inspect` `curves` and `probe`.

- `Impact slam` wrote `scale` (old name `scaleUniform`) 2.2 → 0.92 at clip frame 5 (comp **f15**), back to 1.0 by f18:
  undershoot 6.7%, settles f18; opacity 0 → 1 over 2 f.
- A parented tile (rest x 300, y 890): f15 300/890 → f17 **324/876** → f19 282/902 → f21 312/882 → f23
  293/895 → f25 303/888 → f27 300/890 (rest). The word moved by the same offsets on top of its own scale.
- `inspect qc`: no findings. `inspect lint`: **1 error** (`never_visible` on the null, an intentional
  invisible parent) and 9 `speed_jump` notes (the shake starting from rest).

## Traps

- Lint reports an invisible parent null as an error: [FR-041](../../ai/references/known-issues.md#fr-041).
- `parent.assign` makes the **last**-selected object the parent on 0.1.6:
  [KI-120](../../ai/references/known-issues.md#ki-120).
- Nested-comp instances ignore their parent: shake them with their own keys:
  [KI-119](../../ai/references/known-issues.md#ki-119).
- Keep shakes short and rare; long or large shakes are a motion-sensitivity risk
  ([motion sensitivity](../accessibility/motion-sensitivity.md)). Shakes of ±1 px every frame read as
  jitter ([wiggle and jitter](../techniques/wiggle-and-jitter.md)).

## In Carvercat

- Curve names on this page (S-curve) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Presets: `Impact slam` (Sports), `Stamp`, `Words slam` (Kinetic Typography); template `GOAL slam`
  ([sp-goal-slam](../../ai/patterns/sp-goal-slam.md)).
- Parenting rules: [rigging](../../ai/references/drawing/rigging.md).
- Background: [camera moves](../techniques/camera-moves-2d.md), [wiggle and jitter](../techniques/wiggle-and-jitter.md).
