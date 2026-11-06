---
id: cookbook/card-flip
title: Flip a card
section: cookbook
tags: [flip, card, turn, reveal, question answer, scale x, faux 3d]
styles: [explainer, saas-ui, cartoon-bounce, social-short-form]
topics: [depth, transitions]
related: [techniques/faux-3d, principles/solid-drawing-2d, cookbook/pop-in, cookbook/bullet-list]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://blog.cg-wire.com/camera-work-in-animation/, https://www.nngroup.com/articles/animation-duration/]
---

# Flip a card

**Goal.** A card that turns over to show its other side (question → answer), in 2D.

## Steps

1. Two cards in the same place: **front** (ending at the flip midpoint) and **back** (starting there).
   Each card's label is its own text with the **same keys** as its card.
2. Front: scale `[1, 1]` → `[0, 1]` over 8 f, **accelerate**, ending on the midpoint frame (f18).
3. Back: scale `[0, 1]` → `[1, 1]` over 8 f, **decelerate**, starting on the midpoint frame.
4. Accelerate into the edge-on frame and decelerate out of it, as a real card would turn.
5. Give the front long enough to read before it flips.

## Measured in Carvercat 0.1.6

Comp `K Card flip` in [cookbook lab 3](../labs/README.md#cookbook-lab-3carverproj): 520 × 320 px cards,
front f0–f18, back f18–f60; `inspect probe` widths:

| Frame | 10 | 12 | 14 | 16 | 17 | 18 | 19 | 21 | 23 | 26 |
|---|---|---|---|---|---|---|---|---|---|---|
| Front (px) | 520 | 501.6 | 439.9 | 309.1 | 194.6 | – | – | – | – | – |
| Back (px) | – | – | – | – | – | 0 | 351.4 | 471.7 | 507.4 | 520 |

- f18 is the edge-on frame: neither card shows. The flip reads in 16 f.
- Labels followed their cards: "Question" 254.5 → 95.2 px wide by f17; "Answer" 0 → 208.4 px.
- `inspect lint`: 0 errors, 1 warning: `reading_time` on "Question" (18 frames; 8 characters want 25).
  Hold the front longer in a real film.

## Traps

- Labels don't follow a card's scale unless keyed the same or parented; parenting uses the
  last-selected object as the parent on 0.1.6: [KI-120](../../ai/references/known-issues.md#ki-120).
- Scale on a parent with an off-centre pivot drifted its children (old `anchor`): [KI-108](../../ai/references/known-issues.md#ki-108).
- scaleX/scaleY cannot be driven by Stagger Text, so a row of flips needs its own keys per card:
  [KI-134](../../ai/references/known-issues.md#ki-134).

## In Carvercat

- Curve names on this page (decelerate, accelerate) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Preset: `Flip in (X)` (Carvercat Essentials), the opening half of a flip.
- Background: [faux 3D](../techniques/faux-3d.md) (shading a turn), [solid drawing](../principles/solid-drawing-2d.md).
