---
id: cookbook/list-highlight-bar
title: Move a highlight bar down a list
section: cookbook
tags: [list, highlight, selection bar, agenda, steps, current item, kinetic list, menu, chapter list]
styles: [explainer, saas-ui, corporate-brand, kinetic-typography]
topics: [text, layout]
related: [cookbook/bullet-list, cookbook/highlight-a-word, genres/explainers, design/visual-hierarchy]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/animation-purpose-ux/]
---

# Move a highlight bar down a list

**Goal.** A list of steps where a coloured bar slides from item to item and the current item turns
bright while the others stay dim, like an agenda that follows the talk.

## Steps

1. Items as separate texts (56 px Medium, dim grey) 100 px apart, rising in 3 f apart.
2. One bar behind them: rectangle 640 × 84 px, `borderRadius` 14, centred on item 1's **layout line** (the y you
   placed the text at), fading in.
3. Every step (here 20 f), move the bar 100 px down, **expo, 10 f**.
4. Text colour: key `fill` with **`hold`** keys: bright on the frame the bar starts towards an
   item, dim again when it leaves.

## Measured in Carvercat 0.1.6

Comp `K List highlight` in [cookbook lab 6](../labs/README.md#cookbook-lab-6carverproj): five items at y 340–740,
bar moves at f30, f50, f70, f90; `inspect probe` and `carvercat_render`:

- Bar centre: 340.0 to f30, **415.2 at f32**, 437.2 at f35, 440.0 from f40; then 540, 640 and 740. Three
  quarters of each move happen in the first 2 f.
- Item ink centres at rest: 340.1, 440.1, **545.2**, **639.4**, **745.6**. Descenders and capitals move the ink
  box up to 5.6 px off the layout line, so align the bar to the layout y, not to measured ink bounds.
- Brightest text pixel per row at f25: item 1 = 242, others 140; at f45: item 2 = 242, others 140. The
  `hold` colour keys switch on their frames.
- `inspect lint contrast:true`: 0 errors, 0 warnings, 10 notes.

## Traps

- One text per item, so each can have its own colour keys.
- Colour keys without `hold` fade through the in-between colour over the whole gap between keys.
- `text.content` can't be keyed: [KI-051](../../ai/references/known-issues.md#ki-051).

## In Carvercat

- Library: `Agenda` ([cb-agenda](../../ai/patterns/cb-agenda.md)), `Numbered list`
  ([kt-numbered-list](../../ai/patterns/kt-numbered-list.md)), `Checklist`, `Process steps`.
- Background: [bullet list](bullet-list.md), [visual hierarchy](../design/visual-hierarchy.md).
