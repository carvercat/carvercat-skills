---
id: cookbook/bullet-list
title: Bring in a bullet list
section: cookbook
tags: [list, bullets, agenda, features, stagger, rise, items]
styles: [explainer, corporate-brand, saas-ui, kinetic-typography]
topics: [text, stagger, hierarchy]
related: [techniques/stagger-systems, design/visual-hierarchy, sound-and-timing/reading-time, cookbook/type-on-text]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/animation-duration/, https://www.ssw.com.au/rules/post-production-do-you-give-enough-time-to-read-texts-in-your-videos]
---

# Bring in a bullet list

**Goal.** A title, then four items arriving in reading order, each with its bullet, readable at once.

## Steps

1. Title first (already on screen, or in at f0).
2. Each item is **two objects**: a bullet dot and a text line. The dot pops (scale 0 → 1, back out, 12 f);
   the text rises 30 px and fades in (expo, 16 f), **2 f after its dot**.
3. Stagger the items **5 f** apart in reading order. One text object per item lets each line keep its
   own timing; Stagger Text by line would force one gap and one curve for all.
4. Hold the full list for its reading time: lint asks for 17 characters a second, at least 25 f.

## Measured in Carvercat 0.1.6

Comp `K Bullets` in [cookbook lab 3](../labs/README.md#cookbook-lab-3carverproj): four 48 px Medium items
at 110 px pitch, dots 18 px, dots from f12 5 f apart; `inspect curves`:

| Item | Text keys | Settles |
|---|---|---|
| 1 | f14 → f30 | f24 |
| 2 | f19 → f35 | f29 |
| 3 | f24 → f40 | f34 |
| 4 | f29 → f45 | f39 |

- Dots: overshoot **9.8%**, the first settles f23.
- The last item has settled by f39 (1.3 s); expo puts the visible landing 10 f into each 16 f move.
- `inspect lint`: 0 errors, 0 warnings, 4 notes (`speed_jump`, each line starting from rest).

## Traps

- Stagger Text has one uniform gap: [KI-041](../../ai/references/known-issues.md#ki-041); staggered exits
  run late: [KI-050](../../ai/references/known-issues.md#ki-050).
- Lint misses small overlaps between neighbouring texts, so check line pitch by eye at the largest
  item: [KI-138](../../ai/references/known-issues.md#ki-138).

## In Carvercat

- Curve names on this page (back out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Agenda` ([cb-agenda](../../ai/patterns/cb-agenda.md)), `Checklist`
  ([ex-checklist](../../ai/patterns/ex-checklist.md)), `Numbered list` ([kt-numbered-list](../../ai/patterns/kt-numbered-list.md)),
  `Bouncy list` ([ct-bouncy-list](../../ai/patterns/ct-bouncy-list.md)), `Listicle (9:16)`
  ([ss-listicle](../../ai/patterns/ss-listicle.md)); presets `Rise - expo`, `Lines reveal - decelerate`.
- Background: [stagger systems](../techniques/stagger-systems.md), [visual hierarchy](../design/visual-hierarchy.md).
