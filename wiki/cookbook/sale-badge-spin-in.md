---
id: cookbook/sale-badge-spin-in
title: Spin in a sale badge
section: cookbook
tags: [sale, badge, starburst, discount, price, spin, promo, sticker, retail]
styles: [funky, social-short-form, cartoon-bounce, retro]
topics: [shapes, text]
related: [genres/social-ads, principles/exaggeration, cookbook/pop-in, cookbook/logo-sting]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/animation-usability/, https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation]
---

# Spin in a sale badge

**Goal.** A starburst badge spins in, then the discount pops and the word "SALE" stamps on top.

## Steps

1. The badge: a **Star** shape, `points: 16`, `innerRadius: "84%"` (the old `shape.geometry.star.sides` 16 and `innerRadius` 0.84),
   560 px.
2. Apply **`Spin in`** to the star: half a turn (`rotate` `"180deg"` → `"0deg"`, counter-clockwise; the 0.1.6 note said −180° → 0°), scale 30% → 100%
   with a small spring, fade in over the first 4 f. 20 f.
3. The figure ("-30%", 140 px ExtraBold) on a clip starting 10 f after the badge, with **`Pop - spring`**.
4. The word ("SALE", 70 px Bold) 6 f after that, with **`Stamp`**.
5. Keep the text upright: don't parent it to the spinning star.

## Measured in Carvercat 0.1.6

Comp `K Sale badge` in [cookbook lab 5](../labs/README.md#cookbook-lab-5carverproj): star from f6, figure
from f16, word from f22; `inspect curves`:

| Object | Preset | Overshoot | Settles |
|---|---|---|---|
| Badge rotation | `Spin in` | 0 (eases out) | f22 |
| Badge scale | `Spin in` | 4.4% of its travel (1.031) | f24 |
| "-30%" | `Pop - spring` | 16.2% | f36 |
| "SALE" | `Stamp` | 4.6% under (0.959) | f35 |

- The badge was fully opaque from **f10**; half of the turn was done by f8 (−91°).
- At 170 px the figure touched the star's points in `carvercat_look`; 140 px fits inside.
- `inspect lint`: 0 errors, 1 warning (`text_too_small`: the figure is 8.5 px tall on its first pop
  frame), 3 notes.

## Traps

- `preset.apply` takes one `id`; apply presets one object at a time:
  [KI-113](../../ai/references/known-issues.md#ki-113).
- A polygon's old `angle` does not rotate it, nor a rectangle's; turn shapes with `rotate`:
  [KI-150](../../ai/references/known-issues.md#ki-150), [KI-057](../../ai/references/known-issues.md#ki-057).

## In Carvercat

- Library: `Sale badge` ([fk-sale-badge](../../ai/patterns/fk-sale-badge.md)), `Sale` (text), `Seal`,
  `Burst`, `Spin in`, `Spin out`, `Tilt pop`.
- Background: [social ads](../genres/social-ads.md), [exaggeration](../principles/exaggeration.md).
