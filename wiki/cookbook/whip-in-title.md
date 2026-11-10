---
id: cookbook/whip-in-title
title: Whip a title in with a speed streak
section: cookbook
tags: [whip, directional blur, speed, streak, title, slide in, impact]
styles: [sports, social-short-form, kinetic-typography, cartoon-bounce]
topics: [speed, effects, titles]
related: [techniques/directional-blur-and-speed, techniques/motion-blur, cookbook/film-look-grain-overlay]
verified: design/1 (Carvercat 0.1.10)
source_inspiration: [https://github.com/carvercat/carvercat-skills]
---

# Whip a title in with a speed streak

**Goal.** A title flies in from the left, streaked while it is fast, and lands crisp.

## Steps

1. A text, `x` resting at 360 (a 1200 px wide box on a 1920 frame).
2. One `anim.set` carries the move and the streak:

   ```json
   {"command": "anim.set", "args": {"id": "#title", "keyframes": [
     {"at": 0, "x": -1500, "directionalBlur": "240px 0deg", "ease": "cubic-bezier(.16,1,.3,1)"},
     {"at": 10, "x": 360, "directionalBlur": "0px 0deg"}]}}
   ```

3. The angle is the direction of travel: `0deg` for a left-to-right move, `90deg` for a rise. The ease leaves the first key, so the
   fast part is at the start; the streak is longest there and falls to 0 on landing.
4. Optional weight: a `scale` overshoot (1.06 to 1 over 4 f) on the landing frame.
5. Read it back: at frame 0 `property.get {key: "directionalBlur"}` is `240px 0deg`, at frame 10 `0px 0deg`, at frame 4 a value between.

## Measured in Carvercat (design/1)

Case `whip-in-title-and-film-look` (`wiki/tools/verify_keyed_pages.py`): the three readings above hold; a streak of length L softens
an edge over 0.8 x L along its angle ([directional blur and speed](../techniques/directional-blur-and-speed.md)).

## Traps

- Leave the streak at 0 for every frame the title is read.
- Length is px of a 1920 frame; a 1080-wide vertical comp scales it by 1080/1920.
- On 0.1.10 `carve.preflight` lists the effect as `unsupported` by mistake ([KI-171](../../ai/references/known-issues.md#ki-171));
  it is exact in Resolve and approximate in After Effects.
- For a long curved move use motion blur ([motion blur](../techniques/motion-blur.md)).

## In Carvercat

- Design key `directionalBlur`: [reference](../../ai/references/effects/directional-blur.md).
- Library: Cartoon Bounce `Smear whoosh` ([ct-smear-whoosh](../../ai/patterns/ct-smear-whoosh.md)), Sports `Goal slam`
  ([sp-goal-slam](../../ai/patterns/sp-goal-slam.md)), Social `Swipe up` ([ss-swipe-up](../../ai/patterns/ss-swipe-up.md)),
  Kinetic Typography `Line reveal` ([kt-line-reveal](../../ai/patterns/kt-line-reveal.md)).
