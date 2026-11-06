---
id: cookbook/end-card-with-url
title: Make an end card with a web address
section: cookbook
tags: [end card, outro, url, web address, call to action, cta, button, hold, closing frame]
styles: [saas-ui, corporate-brand, social-short-form]
topics: [text, layout, timing]
related: [cookbook/end-cleanly, sound-and-timing/reading-time, genres/product-launches, accessibility/readability]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Call_to_action_(marketing)]
---

# Make an end card with a web address

**Goal.** The last 5 seconds of a promo: logo, headline, the web address people should type, and a button,
built in quickly and then held still long enough to read and remember.

## Steps

1. Logo mark pops first (`Pop - spring`), headline (96 px Bold) rises at f8, the address (56 px Medium, accent
   colour) at f14, the button (380 × 96 px with a 44 px label) pops at f22 (`Pop - gentle`).
2. Everything settles in the first **~1.3 s**; the rest is a **hold**. The address is the one thing people must
   copy, so give it its own line, an accent colour and no motion during the hold.
3. Keep the address short (domain + one path word) and in a size people can read from across the room.
4. Hold at least 3 s after the last element settles; end with [end cleanly](end-cleanly.md).

## Measured in Carvercat 0.1.6

Comp `K End card` in [cookbook lab 6](../labs/README.md#cookbook-lab-6carverproj), 150 f; `inspect curves`,
`inspect probe` and `inspect lint contrast:true`:

| Element | Starts | Settles |
|---|---|---|
| Logo mark (`Pop - spring`, 16.2% over) | f0 | f20 |
| Headline | f8 | f18 |
| Address | f14 | f24 |
| Button (`Pop - gentle`, 4.4% over) | f22 | f40 |

- Last element still at **f40**, so the card holds still for **110 f (3.7 s)** of its 150.
- At rest the address "northwind.app/start" measured 497.5 × 55.5 px, the headline 777.6 × 90.8 px.
- `inspect lint contrast:true`: **0 errors, 0 warnings**, 5 notes.

## Traps

- There is no QR-code object, and a QR built by hand from squares can't be checked in Carvercat:
  [FR-044](../../ai/references/known-issues.md#fr-044). Use a short address instead.
- Lint ignores text inside nested instances when you lint the master, so lint the end-card comp itself:
  [FR-042](../../ai/references/known-issues.md#fr-042).

## In Carvercat

- Library: `CTA end card` ([su-cta-end-card](../../ai/patterns/su-cta-end-card.md)), `End card`, `Brand end card`
  ([cb-end-card](../../ai/patterns/cb-end-card.md)), `Follow end card`, `Link`.
- Background: [end cleanly](end-cleanly.md), [reading time](../sound-and-timing/reading-time.md).
