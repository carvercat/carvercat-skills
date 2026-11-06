---
id: cookbook/rating-stars-fill
title: Fill rating stars to a score
section: cookbook
tags: [rating, stars, review, score, half star, 4.5 stars, testimonial, product, app store]
styles: [saas-ui, corporate-brand, social-short-form]
topics: [shapes, masking, data]
related: [cookbook/progress-bar, cookbook/chart-bars-to-values, techniques/masking, techniques/nested-comps-and-time]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Star_(classification)]
---

# Fill rating stars to a score

**Goal.** Five grey stars fill with gold from the left and stop at the score, half stars included ("4.5"),
then the number and the review count appear.

## Steps

1. Five **grey stars** (Star, 5 points, `innerRadius` 0.45), 120 px wide, centres 140 px apart (here x 680,
   820, 960, 1100, 1240; y 500).
2. A comp **`Rating gold`** with five **gold stars** in exactly the same places; place one instance of it over
   the grey row.
3. A **window** rectangle from the left edge of star 1 to the right edge of star 5 (here x 620 → 1300, 680 px),
   `transformOrigin` `"0% 50%"` so its left edge stays put. On the instance `property.set {key: "mask", value: "<window>"}`, then
   `parent.clear {ids: ["<window>"]}`.
4. **Where the fill stops**: for score *v*, star *i* = ⌊*v*⌋, edge x = left + *i* × spacing + (*v* − *i*) ×
   star width. For 4.5: 620 + 4 × 140 + 0.5 × 120 = **1240**. Key the window's `scale` from `[0, 1]` to
   `[(edge − left) / width, 1]` = `[620 / 680, 1]` = `[0.912, 1]` (f10 → f40, expo out).
5. Bring in the score text with `Pop - gentle` and the caption with `Soft rise` once the fill lands.

The gaps between stars are why the fill is computed per star: a straight 4.5 / 5 = 0.9 would stop at x 1232,
8 px short of the half-way line of star 5.

## Measured in Carvercat 0.1.6

Comp `K Rating` in [cookbook lab 8](../labs/README.md#cookbook-lab-8carverproj); `inspect probe` on the window,
gold pixels found in rendered frames:

| Frame | 10 | 12 | 14 | 16 | 20 | 25 | 30 | 35 | 40 |
|---|---|---|---|---|---|---|---|---|---|
| Window right edge x | 620.0 | 843.0 | 993.0 | 1086.4 | 1179.8 | 1222.5 | 1236.2 | 1239.6 | 1240.0 |

- The left edge stayed at 620 every frame; `inspect curves` settles the fill on **f29**.
- Rightmost gold pixel: 1221 on f25, **1239 on f45**: exactly the middle of star 5 (1240), with nothing gold
  past it.
- `inspect lint contrast:true`: 0 errors, 2 warnings (`reading_time` for the score and caption: this lab comp
  ends 24 f after they appear) and 2 notes.

## Traps

- One mask, one target: masking the five gold stars separately needs five windows; the nested comp needs one.
- Lint ignores masks ([KI-133](../../ai/references/known-issues.md#ki-133)); here it happened not to warn.
- `preset.apply` takes one `id`: [KI-113](../../ai/references/known-issues.md#ki-113).

## In Carvercat

- Curve names on this page (expo out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Rating` sticker, `Star` sticker and the `Star` shape; `Pop - gentle`, `Soft rise`.
- Background: [masking](../techniques/masking.md), [progress bar](progress-bar.md) (the same left-anchored
  scale), [nested comps](../techniques/nested-comps-and-time.md).
