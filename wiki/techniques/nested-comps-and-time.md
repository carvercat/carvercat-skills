---
id: techniques/nested-comps-and-time
title: Nested comps and time offsets
section: techniques
tags: [nested comp, precomp, instance, source in, time offset, reuse, scene, scale, parenting]
styles: [all]
topics: [structure, timing]
related: [techniques/match-cuts, techniques/camera-moves-2d, workflow/animatics, techniques/rhythm-editing, principles/arcs]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://helpx.adobe.com/sk/after-effects/how-to/camera-animation.html, https://creativecow.net/?p=39768]
---

# Nested comps and time offsets

A nested comp (a precomp) is a whole comp placed inside another as one object, an **instance**. It is how
scenes are assembled into a film, how a reusable piece (a lower third, a logo sting) is built once and placed
many times, and how one animation is reused at different times or sizes.

## The idea

- **Build once, place many times**: change the inner comp and every instance follows.
- **Offset time**: start the instance later, or skip into the inner animation with a source-in offset.
- **Transform the instance**: position, scale, rotation and opacity apply to the whole inner comp.
- **Scenes as comps**: a film is a master comp of butted scene instances ([animatics](../workflow/animatics.md)).

## Rules of thumb

- One scene or one reusable element per inner comp; name comps after what they contain.
- Make inner comps exactly as long as their content; extend holds inside the inner comp, not by stretching the
  instance.
- Keep camera moves inside each scene comp, or bake them into the instance's own keys.

## Measured in Carvercat

An inner comp (60 f) with a dot moving from x 300 to x 1500 over f0–30, placed five ways in a 90 f master and
rendered every 15 f:

| Instance | f0 | f15 | f30 | f45 | f60 and later |
|---|---|---|---|---|---|
| Plain (starts f0) | 300 | 900 | 1500 | 1500 | **gone** |
| `sourceIn` 15 | 900 | 1500 | 1500 | **gone** | gone |
| Starts at master f20 | not yet | not yet | 700 | 1300 | 1500 (until f80) |
| Instance scale 0.5 | 630 | 930 | 1230 | 1230 | gone |
| Parented to a null that rises 300 px | stayed in place: the instance did **not** follow its parent | | | | |

- Inner time = master frame − instance start + `sourceIn`. A `sourceIn` of 15 skips the first 15 frames.
- **An instance shows nothing after its inner comp ends**, even if the instance clip is longer: it does not
  hold the last frame. Lengthen the inner comp for a longer hold.
- Instance scale works about the master comp's centre here (the inner comp is frame-sized), so positions
  compress towards the centre: 300 → 630, 1500 → 1230 at 0.5.
- Nested instances ignore parenting (still [KI-119](../../ai/references/known-issues.md#ki-119) on 0.1.6): put
  camera moves on the instance's own keys, in source time.

## Do and don't

- Do reuse inner comps for repeated elements; edit once.
- Do set `sourceIn` to start an instance mid-animation.
- Don't stretch an instance past its inner comp's end and expect a hold.
- Don't parent instances to camera nulls; key them directly.

## Checklist

- [ ] Inner comps as long as their content (plus any hold).
- [ ] No instance relies on a parent for motion.
- [ ] `carvercat_look` at the end of each instance shows no unwanted blank frames.

## In Carvercat

- Place an instance: `comp.place {comp, track, ...}` over MCP; in a project file a clip with `nestedTimelineId`,
  `left`, `duration` and `sourceIn` ([JSON authoring](../../ai/references/app/json-authoring.md)); keys on an
  instance are in source time (local frame + `sourceIn`).
- Templates become nested comps when placed: [patterns README](../../ai/patterns/README.md).
- Whole films from continuous subscenes: [JSON authoring](../../ai/references/app/json-authoring.md#continuous-motion-across-sub-comps).
- Lab: comps `N Inner` and `N Master` in [the hierarchy and nesting lab](../labs/README.md).
