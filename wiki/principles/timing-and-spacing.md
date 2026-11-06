---
id: principles/timing-and-spacing
title: Timing and spacing
section: principles
tags: [timing, spacing, duration, frames, speed, duration scale]
styles: [all]
topics: [timing, easing]
related: [principles/slow-in-slow-out, principles/weight, principles/rhythm, sound-and-timing/frame-rates, sound-and-timing/beat-sync]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.lollypop.design/blog/2019/march/the-forgotten-art-of-spacing/, https://www.pluralsight.com/resources/blog/software-development/character-animation-fundamentals-timing-spacing, https://www.nngroup.com/articles/animation-duration/, https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md, https://carbondesignsystem.com/elements/motion/overview/, https://learn.toonboom.com/modules/animation-principles/topic/activity-1-experimenting-with-space-and-time]
---

# Timing and spacing

**Timing** is how many frames a move takes. **Spacing** is how far the object travels from one frame to
the next. Two moves with the same timing can feel completely different because of their spacing, and
spacing is what an easing curve controls.

## The idea

- Timing sets speed, and speed tells the viewer about size, weight and importance.
- Spacing sets character: even spacing is mechanical; tight spacing at the ends and wide in the middle is
  natural; wide at the start and tight at the end is a confident arrival.
- Plan both on a timing chart: list the key poses with frame numbers, then mark how the in-betweens
  bunch toward each pose. A Carvercat curve readout is the timing chart after the fact.

## Rules of thumb (30 fps)

| Band | Frames | Milliseconds | Use |
|---|---|---|---|
| Micro | 3–6 | 100–200 | tick, colour flash, button press, cursor click |
| Small | 6–12 | 200–400 | nudges, per-letter units, toggles |
| Medium | 12–20 | 400–670 | text lines, cards, lower thirds: most entrances |
| Large | 20–30 | 670–1000 | full-frame wipes, big scale changes |
| Dramatic | 30–60 | 1–2 s | logo resolve, hero reveal, once per film |

- Pick one ladder per project (for example 6, 9, 12, 18, 24, 36 f) and reuse it.
- Doubling the distance should add roughly 30–50% more time, not 100%.
- Exits take about 70% of the entrance (18 f in, 12–13 f out).
- UI design systems quote durations for interfaces seen hundreds of times a day (about 100–400 ms). A
  video graphic is seen once, so it can afford the upper half of those ranges and more for hero moments.
- After a move lands, leave the object alone for at least 15–20 f before the next thing happens to it.

## Measured in Carvercat: same timing, different spacing

All moves below are 20 f long and 1200 px wide. Frame-by-frame gaps from `carvercat_inspect mode:probe`:

| `ease` on the leaving key | First frame's step | Last frame's step | Largest step |
|---|---|---|---|
| `linear` | 60 px | 60 px | 60 px |
| quad out, `cubic-bezier(0.333333, 0.666667, 0.666667, 1)` | 117 px | 3 px | 117 px |
| S-curve, `cubic-bezier(0.333333, 0, 0.666667, 1)` | 8.7 px | 8.7 px | 89.7 px (middle) |
| expo out, `cubic-bezier(0.16, 1, 0.3, 1)` | 337 px | 0 px | 337 px |
| accelerate, `cubic-bezier(0.3, 0, 0.8, 0.15)` | 1.7 px | 216 px | 216 px |

The expo arrival covers 28% of the distance in its first frame and then spends 10 frames on the last
3%. That long tail is the "settle" that makes it feel finished. Full table: [slow in and slow out](slow-in-slow-out.md).

## Do and don't

- Do time to the slowest thing the eye must follow: big objects and long travel get more frames.
- Do give identical elements identical timing; give different roles different timing.
- Don't pick durations at random; don't give everything the same duration either.
- Don't judge timing from a contact sheet. Read the numbers (`inspect timing` or `curves`) and watch it
  at speed.

## Checklist

- [ ] Every duration is from the project's ladder.
- [ ] Exits are shorter than entrances.
- [ ] Each arrival holds still at least 15 f before its next change.
- [ ] Settle frames match the plan in `carvercat_inspect mode:timing`.

## In Carvercat

- Template examples with measured numbers and lint traps for this principle: [craft principle page](../../ai/references/craft/principles/timing.md).
- Time is frames, `"1.5s"` or `"500ms"` (`at: "14f"`), from the start of the object; `atComp` is the comp's clock.
  In the project file, clip `left` and `duration`/`width` are in pixels of the timeline at 4 px a frame; keys are
  clip-local frames ([JSON authoring](../../ai/references/app/json-authoring.md)).
- Spacing comes from the `ease` on the key the move leaves: `linear`, `ease-in`, `ease-out`, `ease-in-out`,
  `cubic-bezier(...)`, `steps(...)`, `spring(...)`, `hold` ([easing reference](easing-reference.md#names-used-in-this-wiki)).
  Old words (`Ease in`, `Ease out`, `S-curve`, `Custom`) sit on the arriving key and are accepted for one release.
- `carvercat_inspect {mode:"timing"}` lists, per object, the frame it enters, starts moving, settles and
  exits: the quickest way to read a whole scene's timing.
- `carvercat_inspect {mode:"probe", detail:"detailed"}` gives the per-frame centre, so you can read the
  spacing directly.
- Style-specific frame counts, measured on the packs: [timing by style](../../ai/references/craft/timing-by-style.md).
- Lab: comp `W Spacing` in [the principles lab](../labs/README.md).
