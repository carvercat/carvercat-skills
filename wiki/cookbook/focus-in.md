---
id: cookbook/focus-in
title: Bring a title into focus
section: cookbook
tags: [focus, blur, rack focus, defocus, title, reveal, soft]
styles: [minimal-luxury, kinetic-typography, corporate-brand]
topics: [text, blur, depth]
related: [techniques/motion-blur, techniques/shadow-and-glow-in-motion, cookbook/headline-word-by-word, cookbook/camera-push-on-a-still]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://blog.cg-wire.com/camera-work-in-animation/, https://www.schoolofmotion.com/blog/color-theory-after-effects]
---

# Bring a title into focus

**Goal.** A title that starts soft and slightly large and sharpens into place, like a lens finding focus.

## Steps

1. The title text, then `blur` on it (the first write adds the Blur effect). Key `blur` `"28px"` → `"0px"` over 20 f, expo out (the old Blur `size` 24 is 27.6 px at 1920; `anim.set` with `blur` keys it by name).
2. Opacity 0 → 1 over the first 8 f, so the blurriest frames are also the faintest.
3. Scale 1.06 → 1.0 over the same 20 f, expo out: the settle sells the focus pull.
4. Blur only the hero; blurring everything at once looks like a mistake.

## Measured in Carvercat 0.1.6

Comp `K Focus in` in [cookbook lab 4](../labs/README.md#cookbook-lab-4carverproj): "Into focus" 140 px
Bold, keys f6 → f26.

- `inspect curves`: blur and scale both settle **f19**; opacity reaches 1 at f14.
- `carvercat_inspect composite` (pixels the title changes): **7586** at f7, 4382 at f10, 2478 at f14,
  1721 at f18, **1711** from f22. The blurred title spreads over 4.4 times its sharp area at the start.
- `inspect lint`: **0 errors, 0 warnings, 0 notes**.

## Traps

- A blur added with `effect.add` starts at the old size 10 (11.5 px), not 0: set `blur` before keying:
  [KI-055](../../ai/references/known-issues.md#ki-055).
- `blur` is a Gaussian sigma in px: the visible edge ramp is 2.563 × the number, and the spread is about 3 × (the old size 60 = 69 px spread
  207 px in [background drift](background-drift.md)).

## In Carvercat

- Curve names on this page (expo out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Focus pull` ([kt-focus-pull](../../ai/patterns/kt-focus-pull.md)).
- Effect detail: [blur](../../ai/references/effects/blur.md). Background: [motion blur](../techniques/motion-blur.md).
