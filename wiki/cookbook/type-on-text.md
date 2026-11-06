---
id: cookbook/type-on-text
title: Make text type on letter by letter
section: cookbook
tags: [type on, typewriter, letter by letter, character reveal, stagger, hold, typing]
styles: [saas-ui, kinetic-typography, explainer, glitch, futuristic-hud]
topics: [text, stagger, timing]
related: [techniques/kinetic-type, techniques/stagger-systems, sound-and-timing/reading-time, cookbook/count-a-number-up]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://support.apple.com/en-bw/guide/motion/motn1607df7f/mac, https://motion.dev/tutorials/js-typewriter]
---

# Make text type on letter by letter

**Goal.** One text object whose letters appear one at a time, either hard (a typewriter or terminal) or
soft (each letter fades in), with a timing you can predict to the frame.

## Steps

1. Make **one** text object with the whole line. Don't cut it into one clip per letter: `text.content`
   cannot be keyed and per-letter clips each raise a lint reading-time warning.
2. Stagger the letters with one call, GSAP-style: `anim.set {id, from: {opacity: 0}, at: k, duration, ease, stagger:
   {target: "chars", each: "<gap>f", from: "start"}}` (`each` takes frames, `"40ms"`; `from` is `start`, `end`, `center`,
   `edges` or `random(seed)`). It writes the Stagger Text effect and the plain keys for you.
3. Choose the per-letter move:
   - **Hard type**: `duration: "1f"`, `ease: "hold"` (0 at frame *k*, 1 at *k* + 1).
   - **Soft type**: `duration: "4f"`, `ease` quad out, `cubic-bezier(0.333333, 0.666667, 0.666667, 1)` (0 at *k*, 1 at *k* + 4).
   Verified on a headless Carvercat 0.1.8 build: `from: {opacity: 0}, at: 10, duration: "1f", ease: "hold", stagger: {target:
   "chars", each: "2f"}` on 120 px "ABCDEFGH" showed no ink on f9 and f10 and the first letter on f11 (= *k* + 1).
4. Predict the finish: letter *i* appears at *k* + 1 + gap × (*i* − 1). *N* counts **every** character,
   spaces and punctuation included.
5. For a caret, key a thin rectangle's position on `hold` at the same frames
   ([search typing](../../ai/patterns/su-search-typing.md) gives the measured offsets).

## Measured in Carvercat 0.1.6

Comp `K Type on` in [cookbook lab 1](../labs/README.md#cookbook-lab-1carverproj), 72 px Rethink Sans Bold,
measured frame by frame with `carvercat_inspect mode:composite`.

| Version | Text | Keys | Result |
|---|---|---|---|
| Hard | "Type on, one letter at a time" (29 characters) | gap 2, opacity 0 at f10, 1 at f11 `hold` | first letter f11, last letter **f67** = 11 + 2 × 28 |
| Soft | "Each letter fades in over 4 frames" (34 characters) | gap 1, opacity 0 → 1 over f10–f14 quad out | first ink f11, last letter starts f44 = 10 + 33 + 1 |

- Spaces take a slot: frames 19, 27 and 35 added no ink (the spaces after "Type", "on," and "one").
- `inspect lint`: **0 errors, 0 warnings, 0 notes**.
- Typing 29 characters at 2 f each takes 56 f (1.9 s). Add the reading hold after the last letter, not
  from the first one ([reading time](../sound-and-timing/reading-time.md)).

## Traps

- `text.content` is not keyframeable: [KI-051](../../ai/references/known-issues.md#ki-051).
- The stagger replays the whole key timeline per letter, so exits staggered the same way finish
  gap × (letters − 1) late: [KI-050](../../ai/references/known-issues.md#ki-050).
- One uniform gap only; no per-letter rhythm: [KI-041](../../ai/references/known-issues.md#ki-041).
- An outline reveals early unless it has its own opacity connection:
  [KI-048](../../ai/references/known-issues.md#ki-048).

## In Carvercat

- Curve names on this page (quad out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Call: `anim.set` with `stagger` (above). Old names, accepted for one release: the Stagger Text effect (`cap: "stagger"`,
  `by: "character"`, `order`, `amountMode: "each"`, `amount` in frames) connected to `text.relative.opacity`
  (`src.e_src_text_relative_<id>.opacity`). Full notes: [stagger](../../ai/references/effects/stagger.md).
- Library presets with the same mechanism: `Letters cascade - spring`, `Letters shimmer in`,
  `Letters pop`, `Letters zoom in`.
- Ready-made: `Search typing` recipe ([su-search-typing](../../ai/patterns/su-search-typing.md)),
  `Terminal type-on` ([gl-terminal](../../ai/patterns/gl-terminal.md)).
- Background: [kinetic type](../techniques/kinetic-type.md), [stagger systems](../techniques/stagger-systems.md).
