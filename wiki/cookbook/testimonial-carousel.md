---
id: cookbook/testimonial-carousel
title: Slide through customer testimonials
section: cookbook
tags: [testimonials, carousel, slider, reviews, quotes, social proof, cards, slide]
styles: [saas-ui, corporate-brand, social-short-form]
topics: [layout, timing, text]
related: [cookbook/rounded-image-card, cookbook/lower-third-speaker-swap, cookbook/story-progress-bar, sound-and-timing/reading-time, design/grids-and-layout]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/designing-effective-carousels/]
---

# Slide through customer testimonials

**Goal.** Three quote cards on one strip that slides sideways to the next card, with page dots that follow,
and no card ever touching its neighbour.

## Steps

1. Three cards 1100 × 420 px (`borderRadius` 28), each a rectangle, a two-line quote (56 px) and a name (34 px).
   Card *i* sits at x = 960 + *i* × **1200**, so the gap between cards is 1200 − 1100 = **100 px**.
2. Give card, quote and name of one card the **same position keys**: hold 72 f, slide 18 f to x − 1200
   (ease **smooth**, `cubic-bezier(0.65, 0, 0.35, 1)`), hold 72 f, slide again, hold 72 f. All three
   cards use the same keys shifted by 1200 px, so they move as one strip. Comp length 3 × 72 + 2 × 18 = 252.
3. Three dots at x 920, 960, 1000 (y 880), grey; the active one amber. Use `hold` colour keys on the **middle
   of each slide** (f81 and f171) so the dot changes while the card is crossing.
4. Keep a quote to about 45 characters for a 72 f hold: lint wants 17 characters a second.

## Measured in Carvercat 0.1.6

Comp `K Testimonials` in [cookbook lab 9](../labs/README.md#cookbook-lab-9carverproj); centre x of the cards:

| Frame | 72 | 75 | 81 | 84 | 89 | 90 |
|---|---|---|---|---|---|---|
| Card 1 | 960.0 | 927.2 | 360.0 | −61.1 | −236.9 | −240.0 |
| Card 2 | 2160.0 | 2127.2 | 1560.0 | 1138.9 | 963.1 | 960.0 |

- The distance between neighbouring cards' edges was **100.0 px on every one of the 252 frames**; the slide is
  600 px at f81 (half of 1200) and peaks at 181 px/frame (0.0943 of the width) on f82.
- Between slides the neighbours **peek 310 px** into the frame on both sides (card 1 sits at x −240 while card 2 is
  centred): by design for a carousel, remove it by spacing the cards 1500 px apart.
- Dots: amber on dot 1 through f80, dot 2 from **f81** to f170, dot 3 from **f171** (read from rendered pixels).
- A first build slid the next card in 10 f after the previous one began to leave (expo in, accelerate out);
  the two **overlapped by up to 309.5 px** (f104). Different curves on two cards that share the screen collide;
  one shared curve on a strip cannot.
- `inspect lint contrast:true`: 0 errors, **8 warnings**, all `cropped_at_rest` on the parked cards and their
  quotes ("only 28% on screen while still"), plus 27 `repeated_key_value` notes. The lint cannot tell a carousel
  from a mistake; judge with `carvercat_look`.

## Traps

- Readability: a card is still for 72 f (2.4 s); two long lines at 56 px need more, or a smaller quote
  ([reading time](../sound-and-timing/reading-time.md)).
- If you key each card in and out separately, give them one curve and compute the gap
  ([notification toast](notification-toast.md) shows a one-card version).
- Nothing in lint knows a card is meant to rest off screen.

## In Carvercat

- Curve names on this page (accelerate, smooth) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Quote card`, `Brand quote`, `Slow quote`; `Ring` or `Ellipse` shapes for the pager dots.
- Background: [grids and layout](../design/grids-and-layout.md), [story progress bar](story-progress-bar.md) (another
  pager), [lower-third speaker swap](lower-third-speaker-swap.md).
