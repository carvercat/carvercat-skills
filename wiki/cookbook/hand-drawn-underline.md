---
id: cookbook/hand-drawn-underline
title: Scribble a hand-drawn underline under a word
section: cookbook
tags: [hand drawn, scribble, underline, marker, emphasis, organic, trim, double stroke, pen]
styles: [funky, explainer, social-short-form, cartoon-bounce]
topics: [text, line drawing]
related: [cookbook/underline-a-word, cookbook/highlight-a-word, techniques/line-drawing, techniques/wiggle-and-jitter]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/animation-usability/]
---

# Scribble a hand-drawn underline under a word

**Goal.** A marker-style double scribble under one word in a sentence: a little uneven, overshooting the
word, drawn quickly like a pen stroke.

## Steps

1. Find the word's span in the centred sentence: right edge = sentence left + width of "This one really"
   (measured left-aligned); left edge = right edge − width of "really" (`carvercat_authoring geometry`).
2. Stroke 1: a 4-point path with gentle handles that wanders ±6 px around a line 18 px below the text, starts
   10 px before the word and ends 14 px past it, rising slightly at the end. 9 px stroke, round caps.
3. Stroke 2: a shorter 3-point path 12–18 px lower, 7 px.
4. Draw each with `trimEnd` `"0%"` → `"100%"`, **decelerate**: stroke 1 over 10 f, stroke 2 over 8 f starting as
   stroke 1 finishes, like a pen going back.

## Measured in Carvercat 0.1.6

Comp `K Hand underline` in [cookbook lab 7](../labs/README.md#cookbook-lab-7carverproj): "This one really
matters", 96 px Bold, centred; `inspect probe` and `inspect composite`:

- "really" spans x **863.4–1087.9** (224.5 px). Stroke 1 spans 853.4–1101.9 (248.5 px wide, 12 px tall):
  10 px before and 14 px past the word, as drawn. Its centre line is at y 592.2, 18 px under the text's
  box (bottom 574.2).
- Stroke 1 first showed at **f13** and was 98% drawn at **f19**; stroke 2 at f21 and f26.
- `inspect lint`: **0 errors, 0 warnings, 0 notes**.

## Traps

- Bounds drop a trailing space, so measure "This one really", not "This one really ":
  [KI-149](../../ai/references/known-issues.md#ki-149).
- Round caps add half the stroke at each end ([underline a word](underline-a-word.md)).
- Keyed dash length and gap don't animate, so a "pen" can't be faked with dashes:
  [KI-147](../../ai/references/known-issues.md#ki-147).

## In Carvercat

- `trimEnd` keys by design name: `anim.set {id, keyframes: [{at, trimEnd: "0%", ease}, {at, trimEnd: "100%"}]}`, `ease` on the key that leaves (checked: `wiki/tools/verify_keyed_pages.py`, case draw-a-line-along-a-path). A static `trimEnd` is one call. The older stored key `trim.end` (0 to 1) still works.
- Curve names on this page (decelerate) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Squiggle underline` ([fk-squiggle-underline](../../ai/patterns/fk-squiggle-underline.md)),
  `Scribble circle`, `Underline`, `Highlight sweep`.
- Background: [underline a word](underline-a-word.md), [line drawing](../techniques/line-drawing.md).
