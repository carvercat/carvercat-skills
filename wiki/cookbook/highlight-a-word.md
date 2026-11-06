---
id: cookbook/highlight-a-word
title: Highlight a word in a sentence
section: cookbook
tags: [highlight, marker, emphasis, key word, underline, text, measure text]
styles: [kinetic-typography, explainer, social-short-form, saas-ui, corporate-brand]
topics: [text, emphasis, layout]
related: [techniques/kinetic-type, design/visual-hierarchy, cookbook/type-on-text, cookbook/vertical-captions]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/principles-visual-design/]
---

# Highlight a word in a sentence

**Goal.** A marker that sweeps in behind one word of a sentence, exactly under that word.

## Steps

1. Split the sentence into three texts at the same size and baseline: before, the word, after. (One text
   can't hold a shape behind one word.)
2. **Measure** with `carvercat_authoring mode:geometry detail:"bounds"` on throwaway texts, all
   left-aligned at the same x:
   - "Ship it on Friday" (the sentence up to and **including** the word);
   - "Friday" (the word alone).
   The word's left edge = right edge of the first − width of the second. The "after" text starts at the
   right edge of the first.
3. **Marker**: a rectangle the word's width + 28 px, 104 px tall at 80 px type, behind the word. Set its
   `transformOrigin` on its **left edge**, `"0% 50%"`, and key `scale` `[0, 1]` → `[1, 1]` over 12 f,
   expo out.
4. Time it after the sentence has been read once: the marker says "this one".

## Measured in Carvercat 0.1.6

Comp `K Highlight word` in [cookbook lab 2](../labs/README.md#cookbook-lab-2carverproj), "Ship it on
Friday, not Monday", 80 px Rethink Sans Bold on #F4F1EA:

- Measured widths: "Ship it on " **321.9 px**, "Friday" 214.0 px, "Ship it on Friday" 561.4 px. The
  first stops at the "n": the trailing space is not in the bounds, so placing the word at its right edge
  put "Friday" **25.5 px** too far left, over the "n" (seen in `carvercat_look`).
- Placed as above, "Friday" sits at x 707.4–921.4 and ", not Monday" starts at 921.4: the sentence reads
  as one line in `carvercat_look`.
- Marker x 693.4, width 242; its left edge stayed at 693.4 at every probed frame; scale settles **f22**
  (keys f14 → f26).
- `inspect lint contrast:true`: **0 errors, 0 warnings, 0 notes**. The overlapping first attempt also
  linted clean.

## Traps

- Geometry bounds drop a trailing space: [KI-149](../../ai/references/known-issues.md#ki-149).
- Lint misses small overlaps between neighbouring texts: [KI-138](../../ai/references/known-issues.md#ki-138).
- Word spacing is not rendered, so don't try to open a gap with it: [KI-145](../../ai/references/known-issues.md#ki-145).
- Positive tracking written into JSON garbles text: [KI-117](../../ai/references/known-issues.md#ki-117).

## In Carvercat

- Curve names on this page (expo out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Highlight sweep` ([kinetic-highlight-sweep](../../ai/patterns/kinetic-highlight-sweep.md),
  [kt-highlight-sweep](../../ai/patterns/kt-highlight-sweep.md)), `Highlight` (Carvercat Essentials),
  `Highlight caption (9:16)` ([ss-highlight-caption](../../ai/patterns/ss-highlight-caption.md)),
  `Squiggle underline` ([fk-squiggle-underline](../../ai/patterns/fk-squiggle-underline.md)).
- Measuring text: [JSON authoring](../../ai/references/app/json-authoring.md#measuring-text-for-a-direct-edit).
- Background: [kinetic type](../techniques/kinetic-type.md), [visual hierarchy](../design/visual-hierarchy.md).
