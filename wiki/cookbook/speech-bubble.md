---
id: cookbook/speech-bubble
title: Pop a speech bubble out of a character
section: cookbook
tags: [speech bubble, speech balloon, dialogue, comic, tail, pop, rig, scale from a point]
styles: [cartoon-bounce, explainer, funky, social-short-form]
topics: [rigging, shapes, text]
related: [principles/springs, principles/appeal, cookbook/chat-message, cookbook/pop-in]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Speech_balloon, https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation]
---

# Pop a speech bubble out of a character

**Goal.** A bubble grows out of the tip of its tail, next to the speaker's mouth, then the words pop in.

## Steps

1. Body: a rounded rectangle (560 × 200 px, `borderRadius` 64) with a 6 px ink stroke.
2. Tail in two objects so no line crosses the body: a filled triangle with no stroke (its top edge slightly
   inside the body), and an open 3-point path with the stroke for the two sides only. The tip is the
   point nearest the speaker.
3. A **null on the tail tip**. Parent body, tail fill and tail outline to it **at a frame where its scale is
   1** (select the parts, `select.add` the null last, `parent.assign`).
4. Key the null's scale 0 → 1, **back out**, 14 f. Everything grows from the tip.
5. The text on its own clip 10 f after the bubble starts, with **`Pop - spring`**.

## Measured in Carvercat 0.1.6

Comp `K Speech bubble` in [cookbook lab 5](../labs/README.md#cookbook-lab-5carverproj): tip at (860, 600),
null scale f8–f22; `inspect probe` on the tail outline and body:

| Frame | 9 | 10 | 12 | 16 | 22 → |
|---|---|---|---|---|---|
| Tail tip (left, bottom of its bounds) | 860.0, 600.1 | 859.9, 600.0 | 860.0, 600.0 | 859.9, 600.0 | 860.0, 600.0 |
| Body width (px) | 167.8 | 304.9 | 494.8 | 614.8 | 560.0 |
| Body centre | 925.9, 540.1 | 979.8, 491.1 | 1054.4, 423.3 | 1101.5, 380.4 | 1080.0, 400.0 |

- The tip did not move on any frame; the body's centre travelled along the line from the tip, overshot
  **9.8%** (614.8 px wide at f16) and settled at **f21**.
- `Pop - spring` on "Hi there!" from f18: 16.2% over, settles **f38**.
- `inspect lint`: 1 error (`never_visible` on the null), 1 warning (`text_too_small`: the popping text is
  5.2 px tall on its first frame), 1 note.

## Traps

- Parenting while the null's scale is **0** wrote child scale 1,000,000 and positions around 10⁵; every
  frame of the comp rendered as solid ink: [KI-153](../../ai/references/known-issues.md#ki-153).
- A tail drawn as one closed, stroked triangle draws its top edge across the bubble; split fill and outline.
- The null is reported as `never_visible`: [FR-041](../../ai/references/known-issues.md#fr-041).

## In Carvercat

- Curve names on this page (back out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Speech bubble` ([ct-speech-bubble](../../ai/patterns/ct-speech-bubble.md)), `Speech` and
  `Thought` stickers, `Pop - spring`.
- Background: [springs](../principles/springs.md), [appeal](../principles/appeal.md).
