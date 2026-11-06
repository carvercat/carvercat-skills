---
id: history/swiss-international-style
title: Swiss International Typographic Style
section: history
tags: [swiss style, international typographic style, grid, helvetica, akzidenz, sans serif, objectivity, corporate identity]
styles: [corporate-brand, minimal-luxury, saas-ui, data-viz]
topics: [history, typography, grid]
related: [history/bauhaus-and-constructivism, design/grids-and-layout, design/typography-pairing, history/flat-design-and-ui-motion, design/negative-space]
verified: no (theory only)
source_inspiration: [https://en.wikipedia.org/wiki/International_Typographic_Style, https://en.wikipedia.org/wiki/Josef_M%C3%BCller-Brockmann, https://madegooddesigns.com/grid-systems/]
---

# Swiss International Typographic Style

The post-war design style from the schools of Basel and Zürich that made the **grid**, **sans-serif type**
and **asymmetric, objective layouts** the default of corporate and information design. Most clean
"corporate" and "SaaS" motion today descends from it.

## What defined it

- A mathematical grid decided before anything was placed; every element aligned to it.
- Grotesque sans-serifs (Akzidenz-Grotesk, then Helvetica and Univers), flush-left, ragged-right text.
- Asymmetric layouts with generous white space; hierarchy through size and position, not decoration.
- Objective photography instead of illustration; clarity as an ethical goal.
- Concert posters of the 1950s translated musical structure into rhythm, scale and repetition of simple
  geometric forms: an early model for music-driven layouts.
- Adopted by corporations and institutions from the 1960s as the language of identity systems.

## Why it matters for motion

- Grids give motion a structure: elements travel along columns and rows and land on lines.
- Rhythm and repetition of simple forms map directly onto staggered, beat-driven animation.
- Restraint keeps attention on information; motion becomes punctuation rather than decoration.

## Using the influence well

- Define margins, columns and a spacing unit first; animate within them ([grids and layout](../design/grids-and-layout.md)).
- One sans family, two or three sizes, flush-left alignment.
- Use space and scale for hierarchy; one accent colour.
- Motion that reveals structure: lines draw on the grid, blocks slide along columns, text steps in by rows.

## In Carvercat

No measurements on this page. Packs and techniques in this spirit:

- [Corporate Brand](../../ai/patterns/corporate-brand.md) (`Title card - split rule`, `Three stats`, `Agenda`)
  and [Data Viz](../../ai/patterns/data-viz.md).
- Grid overlay while composing: `carvercat_look {overlay:["grid","safe"]}` (a 6 × 6 grid at 320 × 180 px on
  1920 × 1080, see [grids and layout](../design/grids-and-layout.md)).
- Rows stepping in: [stagger systems](../techniques/stagger-systems.md); drawn rules:
  [line drawing](../techniques/line-drawing.md).
