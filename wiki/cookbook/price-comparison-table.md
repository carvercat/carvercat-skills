---
id: cookbook/price-comparison-table
title: Animate a price comparison table
section: cookbook
tags: [pricing, price table, comparison, plans, tiers, saas, recommended plan, columns]
styles: [saas-ui, corporate-brand, social-ads]
topics: [layout, stagger, nested comps]
related: [cookbook/stat-card-trend-arrow, cookbook/pop-in, techniques/nested-comps-and-time, techniques/stagger-systems, genres/product-launches]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/comparison-tables/]
---

# Animate a price comparison table

**Goal.** Three plan columns rise in one after another, then the recommended middle plan grows a little so it
reads as "the one".

## Steps

1. Build **one comp per column** (each holds its card 440 × 600 px, plan name, price, "per month", three
   features and a button, centred in the frame). Three comps with the same layout and different text and colours.
2. In the table comp place three **nested instances**, at x 480, 960, 1440 (gap 40 px between the cards), y 540.
3. **Stagger**: instance *i* starts at f 6 *i*: position y 600 → 540 (expo out, 18 f) and opacity 0 → 1 over 8 f.
4. **Recommended plan**: scale the Pro instance 1.00 → **1.06** from f50 to f62 with the back out bezier. The
   instance scales about its own centre, which is the card's centre because each column comp is centred.
5. Check the gaps at the biggest scale: the card grows 13.2 px each side, so a 40 px gap shrinks to 26.8 px.

## Measured in Carvercat 0.1.6

Comp `K Pricing` in [cookbook lab 9](../labs/README.md#cookbook-lab-9carverproj); card edges found in rendered
frames along y 300:

| Frame | Basic card | Pro card | Team card |
|---|---|---|---|
| 45 | 260–699 | 739–1180 | 1220–1659 |
| 62 and 99 | 260–699 | 726–1193 | 1220–1659 |

- Cards 440 px wide before the push; Pro **468 px** after (440 × 1.06 = 466.4, within 2 px of the edge reading),
  gap to its neighbours 27 px (expected 26.8).
- Rise: Basic's opacity 0.94 and cy 545.8 on f6, cy 540.0 on f18; Pro starts f6 (cy 545.8 on f12); Team starts f12.
- Pro scale reads 1.063 on f55 and 1.060 from f62; `inspect curves` overshoot 9.8% of the move (back out).
- `inspect probe` on an instance reports the **child comp's** frame (1920 × 1080), not the card, so measure card
  sizes from pixels.
- `inspect lint contrast:true`: 0 errors, **3 warnings**, `cropped_at_rest` on the three instances (75%, 89%,
  75% "on screen") although every card is fully visible ([KI-163](../../ai/references/known-issues.md#ki-163)),
  and 2 `speed_jump` notes.

## Traps

- Do not scale each element of the Pro column separately: they scale about different points. One nested
  instance keeps the whole card together.
- `cropped_at_rest` on nested instances placed off the frame centre is a false alarm:
  [KI-163](../../ai/references/known-issues.md#ki-163).
- Leave at least 24 px between cards at full scale.

## In Carvercat

- Curve names on this page (expo out, back out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Price card`, `Compare columns`, `Sale badge`, `Pop - gentle`.
- Background: [nested comps](../techniques/nested-comps-and-time.md), [stagger systems](../techniques/stagger-systems.md),
  [product launches](../genres/product-launches.md).
