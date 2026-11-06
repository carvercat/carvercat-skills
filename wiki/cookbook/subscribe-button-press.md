---
id: cookbook/subscribe-button-press
title: Press a "subscribe" button with a cursor
section: cookbook
tags: [subscribe, button, click, press, cursor, call to action, cta, youtube, state change]
styles: [social-short-form, saas-ui, cartoon-bounce]
topics: [ui, timing]
related: [cookbook/ripple, cookbook/draw-attention-pulse, genres/social-ads, principles/anticipation]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Call_to_action_(marketing), https://www.nngroup.com/articles/animation-purpose-ux/]
---

# Press a "subscribe" button with a cursor

**Goal.** A cursor glides to a red SUBSCRIBE button, clicks, the button dips and springs back, turns grey
and reads SUBSCRIBED, with a ring under the click.

## Steps

1. Button: rectangle 440 × 110 px, `borderRadius` 24, red. Two label clips butted on the click frame: "SUBSCRIBE"
   up to it, "SUBSCRIBED" from it. Parent both labels to the button (at a frame where its scale is 1).
2. Fill colour: key `fill` red on f0 and grey on the click frame with **`hold`**, so it switches
   on that frame instead of fading through brown.
3. Press: button `scale` 1 → 0.92 over 4 f (**ease in**), then back to 1 over 10 f (**back out**). The click
   frame is the bottom of the dip.
4. Cursor: a 7-point closed path (white fill, 3 px ink stroke, round corners), anchored on its **tip**
   (`transformOrigin` `"0% 0%"`, top-left of its bounds). Glide in on an S-curve (20 f), then scale 1 → 0.85 → 1
   around the click.
5. A ring at the tip on its own 18 f clip from the click frame, with **`Tap ripple`**.

## Measured in Carvercat 0.1.6

Comp `K Subscribe` in [cookbook lab 6](../labs/README.md#cookbook-lab-6carverproj): glide f6–f26, press
f28–f42, click on f32; `inspect probe`, `inspect curves` and `carvercat_render`:

- The cursor's tip held **(1010.0, 560.0)** on every sampled frame of the press while its width went
  33.0 → 28.1 (f31) → 33.0 px: it pressed about the tip.
- Button width 440.0 → 404.8 at f32 (0.92) → 443.4 at f38 → 440.0 at f42.
- Rendered pixel inside the button at (770, 510): red (229, 72, 59) at f25 and f31, grey (58, 63, 71) from
  **f32**: the `hold` key switches on its own frame.
- The labels swap on f32 and dip with the button (they are parented): "SUBSCRIBE" 239.7 → 233.6 px wide at f31.
- `inspect lint contrast:true`: 0 errors, 0 warnings, 1 note.

## Traps

- Parenting while the button's scale isn't 1 would bake that scale into the labels:
  [KI-153](../../ai/references/known-issues.md#ki-153).
- `text.content` can't be keyed; the label change is two clips:
  [KI-051](../../ai/references/known-issues.md#ki-051).
- The old rectangle `cornerRadius` stopped at a quarter of the short side ([KI-121](../../ai/references/known-issues.md#ki-121)); a full pill is now `borderRadius: "50%"`.

## In Carvercat

- Curve names on this page (S-curve, back out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Subscribe` (sticker and scene), `Button press` ([ct-button-press](../../ai/patterns/ct-button-press.md)),
  `Cursor click` ([su-cursor-click](../../ai/patterns/su-cursor-click.md)), `Bell`, `Tap ripple`.
- Background: [ripple](ripple.md), [anticipation](../principles/anticipation.md).
