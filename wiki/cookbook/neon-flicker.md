---
id: cookbook/neon-flicker
title: Make a neon sign flicker on
section: cookbook
tags: [neon, flicker, glow, sign, retro, hold keys, power on]
styles: [retro, futuristic-hud, glitch, funky]
topics: [light, timing, accessibility]
related: [techniques/shadow-and-glow-in-motion, accessibility/photosensitivity, cookbook/glint-sweep]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://help.apple.com/motion/mac/5.4/en.lproj/motn13745f4a.html, https://www.w3.org/WAI/WCAG21/Understanding/three-flashes-or-below-threshold.html]
---

# Make a neon sign flicker on

**Goal.** A glowing word that stutters on like a neon tube warming up, then stays lit.

## Steps

1. The word in a saturated colour on a near-black ground, with a **glow** (`glow: "21px #c9577f 0.6 0.2"`: radius, colour, strength 0.6, mix 0.2; the old size 18 is a 20.7 px radius). Keep amount ≤ 0.8 so it does not burn to white.
2. Key `opacity` on **`hold`**: off, on, off, on, dim, on, 2–6 f apart, then steady.
   Hold keys switch instantly, the way a tube does.
3. Keep the flicker small in the frame and short (under a second). Run `inspect qc` for flashes.

## Measured in Carvercat 0.1.6

Comp `K Neon` in [cookbook lab 3](../labs/README.md#cookbook-lab-3carverproj): "OPEN" 220 px Bold
#C9577F with glow, opacity keys 0 (f0), 1 (f4), 0 (f6), 1 (f8), 0.3 (f14), 1 (f16), all `hold`.

- `inspect probe` opacity per frame: 0 at f0–f3, **1 at f4–f5**, 0 at f6–f7, 1 at f8–f13, 0.3 at f14–f15,
  1 from f16: each Hold key switches on its own frame.
- `inspect qc`: **no flash findings** (frame luma 0.041–0.054: the word is a small part of the frame).
- `inspect lint`: **0 errors, 0 warnings, 0 notes**.
- A full-frame flicker at the same rhythm is a flash risk; see the measured limits in
  [photosensitivity](../accessibility/photosensitivity.md).

## Traps

- Glow `mix` (old `blend`) above 0 hazes the layer even at amount 0, so a "glow off" frame still glows:
  [KI-056](../../ai/references/known-issues.md#ki-056).
- A new blur added with `effect.add` starts at the old size 10 (11.5 px), not 0: [KI-055](../../ai/references/known-issues.md#ki-055).

## In Carvercat

- Library: `Neon sign` ([rt-neon-sign](../../ai/patterns/rt-neon-sign.md)), `Neon` (Carvercat Essentials).
- Glow limits: [glow](../../ai/references/effects/glow.md). Background:
  [shadow and glow in motion](../techniques/shadow-and-glow-in-motion.md).
