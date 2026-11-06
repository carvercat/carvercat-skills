---
id: cookbook/app-store-badge-end-card
title: End an app video with download badges
section: cookbook
tags: [app store, download badges, end card, app icon, call to action, mobile app, get the app]
styles: [saas-ui, social-ads, corporate-brand]
topics: [end card, cta, layout]
related: [cookbook/end-card-with-url, cookbook/pop-in, cookbook/subscribe-button-press, genres/social-ads, genres/product-launches]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://developer.apple.com/app-store/marketing/guidelines/]
---

# End an app video with download badges

**Goal.** The last scene of an app promo: the icon pops in, the name and one line rise under it, and two download
badges slide up one after the other, then the card holds.

## Steps

1. **Icon**: a 260 px rounded square (`borderRadius` 58) with a diagonal gradient (amber to orange) and a white star
   on it, (its centre at (960, 250), so `x` 830, `y` 120). Both scale 0 → 1 over 14 f with the `pop` bezier.
2. **Name** (100 px, white) at y 480 and **tagline** (44 px, grey) at y 590: start f10 and f16, each rising 30 and
   24 px with opacity 0 → 1 (expo out, 16 f).
3. **Badges**: two black rounded rectangles 420 × 120 (`borderRadius` 24, `strokeWidth` 3, grey `stroke`) at x 710 and 1210, y 760, each
   with a small line ("Download for") and a big line ("iPhone", "Android"). Start f26 and f32; each part rises
   40 px, expo out, 16 f, opacity over 8 f.
4. Hold to the end (here 120 f).
5. The real badges are the stores' own artwork under their own rules. Import the supplied image
   (`media.import`) in place of the text badges and keep their clear space; the lab's badges are neutral stand-ins.

## Measured in Carvercat 0.1.6

Comp `K Badge card` in [cookbook lab 9](../labs/README.md#cookbook-lab-9carverproj); `inspect probe`:

| Frame | 0 | 10 | 14 | 26 | 32 | 42 |
|---|---|---|---|---|---|---|
| Icon width | 0 | 286.7 | 260.0 | 260.0 | 260.0 | 260.0 |
| Name cy | | 510.1 | 485.3 | 480.1 | 480.1 | 480.1 |
| Badge 1 cy | | | | 800.0 | 762.9 | 760.0 |

- The icon peaks at **286.7 px (10.3% over)** on f10 (`inspect curves`: 15.8% on the scale) and is 260.0 px from f14.
- Name opacity 0.75 on f14, 1.0 on f20; badges start 40 px low (cy 800) and are within 3 px of rest on f32 (badge 1)
  and f42 (badge 2: 760.4).
- Everything is still (within half a pixel) from about **f42**, then holds for 78 f.
- `inspect lint contrast:true`: **0 errors, 0 warnings, 0 notes**.

## Traps

- The stores publish rules for their badges (artwork, size, clear space); stand-in text badges are for layout only.
- Two badges at 420 px plus a 80 px gap are 920 px wide, well inside the 5% margin; check
  [safe areas](safe-area-guides.md) when you add a third (web) badge.
- Let the end card hold 2 s or more so the viewer can find the store ([end card with URL](end-card-with-url.md)).

## In Carvercat

- Curve names on this page (expo out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `End card`, `CTA end card`, `Brand end card`, `Follow end card`, `Button press`, `Pop - spring`.
- Background: [end card with URL](end-card-with-url.md), [social ads](../genres/social-ads.md),
  [product launches](../genres/product-launches.md).
