---
id: cookbook/word-swap
title: Swap one word for another
section: cookbook
tags: [word swap, replace word, rotating word, slot, mask, kinetic type, headline]
styles: [kinetic-typography, saas-ui, social-short-form, corporate-brand]
topics: [text, masking]
related: [techniques/kinetic-type, techniques/masking, cookbook/highlight-a-word, cookbook/count-a-number-up]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://wearefevr.com/the-history-of-kinetic-typography, https://tutvid.com/after-effects/swipe-reveal-text-effect-effects-animated-mask-reveal/]
---

# Swap one word for another

**Goal.** "We build **tools**" becomes "We build **teams**": the last word rolls out upwards and the new one
rolls in from below, inside a slot.

## Steps

1. The fixed part ("We build") as one text. Measure where the swapped word starts: right edge of
   "We build tools" − width of "tools" (`carvercat_authoring geometry`; see
   [highlight a word](highlight-a-word.md) for why not "We build ").
2. Word A and word B as two texts at that x, word B's clip starting a few frames before word A's ends.
3. Two identical **window** rectangles over the slot (wide enough for the longer word, 140 px tall at
   110 px type). Mask each word with its own window: on each word `property.set {key: "mask", value: "<window>"}`, then `parent.clear` on the windows.
4. Word A: up 130 px, **accelerate**, 12 f. Word B: from 130 px below, **expo out**, 14 f, starting 4 f
   after word A leaves.

## Measured in Carvercat 0.1.6

Comp `K Word swap` in [cookbook lab 4](../labs/README.md#cookbook-lab-4carverproj): 110 px Bold, word A
f30–f42, word B f34–f48; `inspect probe` and `carvercat_render`:

- Word A y: 540 at f30, 501 at f38, 410 at f42 (out of the slot). Word B y: 675 at f34, 562 at f38, 547
  at f42, settled **f43** (`inspect curves`).
- Rendered at f38 and f41, rows just above (y 455) and below (y 625) the slot are pure background:
  nothing leaks outside the window while both words move.
- `inspect lint`: 0 errors, 1 warning (`text_overlap` word A / word B: their boxes overlap behind the
  masks), 1 note (`speed_jump` as word A stops at its last frame).

## Traps

- Lint ignores masks: [KI-133](../../ai/references/known-issues.md#ki-133).
- One window masks one track, so two words need two windows (the old `mask.make` reported "masking 1 track").
- `text.content` can't be keyed; a swap is two clips: [KI-051](../../ai/references/known-issues.md#ki-051).
- Geometry bounds drop a trailing space: [KI-149](../../ai/references/known-issues.md#ki-149).

## In Carvercat

- Curve names on this page (expo out, accelerate) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Word swap` ([kt-word-swap](../../ai/patterns/kt-word-swap.md)).
- Background: [kinetic type](../techniques/kinetic-type.md), [masking](../techniques/masking.md).
