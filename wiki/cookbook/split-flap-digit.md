---
id: cookbook/split-flap-digit
title: Flip a split-flap digit
section: cookbook
tags: [split flap, flip clock, departure board, digit flip, counter, mask, scale y, retro]
styles: [retro, sports, data-viz, minimal-luxury]
topics: [masking, text]
related: [cookbook/card-flip, cookbook/count-a-number-up, techniques/masking, techniques/faux-3d]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Split-flap_display]
---

# Flip a split-flap digit

**Goal.** A departure-board digit changes from 3 to 4: the top half of the 3 folds down onto the hinge,
then the bottom half of the 4 falls open below it.

## Steps

1. Card: two half rectangles (220 × 150 px each, top a shade lighter), a 4 px hinge line on top of
   everything.
2. Four copies of the digit text (230 px Bold, centred on the hinge), each masked by its own **half-card
   window** (`property.set {key: "mask", value: "<window>"}` on the digit, then `parent.clear`; one window masks one track):
   - **New top** "4" (top window) and **Old bottom** "3" (bottom window): static, underneath;
   - **Old top** "3" (top window) over a top flap rectangle with `transformOrigin` on its **bottom edge** (`"50% 100%"`);
     both `scale` `[1, 1]` → `[1, 0]`, **accelerate**, 6 f;
   - **New bottom** "4" (bottom window) over a bottom flap rectangle with `transformOrigin` on its **top edge** (`"50% 0%"`);
     both `scale` `[1, 0]` → `[1, 1]`, **decelerate**, 6 f, starting as the top flap reaches 0.
3. A text centred on the hinge scales about its own centre, which is the hinge, so it folds into the hinge.
4. Make each mask at a frame where its text is at scale 1.

## Measured in Carvercat 0.1.6

Comp `K Split flap` in [cookbook lab 6](../labs/README.md#cookbook-lab-6carverproj): flip f20–f32; `inspect probe`:

| Frame | 20 | 22 | 24 | 26 | 27 | 28 | 30 | 32 |
|---|---|---|---|---|---|---|---|---|
| Top flap height (px) | 150.0 | 140.4 | 104.9 | 0.0 | – | – | – | – |
| Top flap centre y | 465.0 | 469.8 | 487.6 | 540.0 | – | – | – | – |
| Bottom flap height (px) | – | – | – | 0.0 | 111.5 | 133.0 | 147.3 | 150.0 |
| Old "3" scale Y | 1.0 | 0.94 | 0.70 | 0.0 | – | – | – | – |
| New "4" scale Y | – | – | – | 0.0 | 0.74 | 0.89 | 0.98 | 1.0 |

- The top flap's bottom edge stayed on the hinge (465 + 150/2 = 540; 487.6 + 104.9/2 = 540.1); the flip is
  edge-on at **f26** and complete at **f32**: 12 f for a digit.
- Rendered at f23, f26 and f29, the rows just above (y 380) and below (y 700) the card are pure background:
  no part of either digit leaks out of its half.
- `inspect lint`: 0 errors, 5 warnings (`text_overlap` between the four stacked copies, which lint sees
  without their masks), 1 note.

## Traps

- Lint ignores masks: [KI-133](../../ai/references/known-issues.md#ki-133).
- Setting `mask` (old `mask.make`) links the window and target like parenting; the lab made each mask at a frame where its text
  is at scale 1 (f5, and f40 for the new bottom half), as for [KI-153](../../ai/references/known-issues.md#ki-153).
- Scale Y can't be staggered per character, so each digit is its own text:
  [KI-134](../../ai/references/known-issues.md#ki-134).

## In Carvercat

- Curve names on this page (decelerate, accelerate) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Score bug` ([sp-score-bug](../../ai/patterns/sp-score-bug.md)), `Big number`, `Flip in (X)`;
  rolling digits in [su-rolling-counter](../../ai/patterns/su-rolling-counter.md).
- Background: [card flip](card-flip.md), [faux 3D](../techniques/faux-3d.md).
