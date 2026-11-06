---
id: cookbook/typewriter-with-cursor
title: Type text with a blinking cursor
section: cookbook
tags: [typewriter, cursor, caret, type on, terminal, blink, hold keys, search bar]
styles: [saas-ui, glitch, kinetic-typography, explainer]
topics: [text, timing]
related: [cookbook/type-on-text, techniques/stagger-systems, principles/holds-and-stillness, sound-and-timing/reading-time]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Cursor_(user_interface), https://en.wikipedia.org/wiki/Typewriter]
---

# Type text with a blinking cursor

**Goal.** Letters appear one at a time with a cursor that sits right after the last typed letter, stays
solid while typing, and blinks before and after.

## Steps

1. Type the text on as in [type on text](type-on-text.md): `anim.set {from: {opacity: 0}, at: k, duration: "1f", ease: "hold", stagger: {target: "chars", each: "3f"}}`
   (the old way: Stagger Text by character, gap 3 f, with `text.relative.opacity` keyed 0 at *k* and 1 at *k* + 1 on `hold`). Letter *i* appears at
   *k* + 1 + 3 × (*i* − 1).
2. Measure where each prefix ends: `carvercat_authoring geometry` on texts holding the first 1, 2, 3 …
   characters (same font, size and x). The cursor's x after *i* letters = right edge of that prefix + a
   few px. After a **space** the bounds stop at the previous letter (KI-149), so use the left edge of the
   next letter instead (right edge of the next prefix − that letter's width).
3. The cursor: a rectangle (8 × 104 px at 96 px type). Key its position with **`hold`** keys on the frames
   the letters appear, so it jumps, never slides.
4. Blink with `hold` opacity keys: every 8 f before typing, solid from the first letter, then every 16 f
   (about 0.5 s on, 0.5 s off) after the last.

## Measured in Carvercat 0.1.6

Comp `K Typewriter` in [cookbook lab 5](../labs/README.md#cookbook-lab-5carverproj): "Ready when you are."
96 px Bold, *k* = 10, gap 3 (letters at f11 … f65); frames rendered with `carvercat_render`, gap = first
cursor pixel − last text pixel on the line:

| Frame | 14 ("Re") | 23 ("Ready") | 26 ("Ready ") | 29 ("Ready w") | 65 (all) |
|---|---|---|---|---|---|
| Gap to the cursor (px) | 5 | 5 | 13 | 5 | 4 |

- At every letter frame the cursor sat 4–5 px after the ink; after the space it moved to the next letter's
  slot (13 px from the "y").
- Bounds measured "Ready" and "Ready " both 258.6 px wide (the trailing space is dropped).
- Blink, `inspect probe` opacity: on f0–7, off f8–10, on from f11 while typing, off f81–96, on f97–112,
  off from f113.
- `inspect lint`: 0 errors, 0 warnings, 1 note (`speed_jump` on the cursor's jumps).

## Traps

- Geometry bounds drop a trailing space: [KI-149](../../ai/references/known-issues.md#ki-149).
- `text.content` can't be keyed, so a counter or retyped word is separate clips:
  [KI-051](../../ai/references/known-issues.md#ki-051).
- A staggered key replays per character, so the last letter lands gap × (letters − 1) after the first:
  [KI-050](../../ai/references/known-issues.md#ki-050).

## In Carvercat

- Library: `Terminal type-on` ([gl-terminal](../../ai/patterns/gl-terminal.md)); search-box typing in
  [su-search-typing](../../ai/patterns/su-search-typing.md).
- Background: [stagger systems](../techniques/stagger-systems.md), [holds](../principles/holds-and-stillness.md),
  [reading time](../sound-and-timing/reading-time.md).
