---
id: cookbook/film-look-grain-overlay
title: Give a title a film look with a grain overlay
section: cookbook
tags: [grain, film look, cinematic, adjustment layer, texture, vhs, retro]
styles: [retro, minimal-luxury, glitch]
topics: [texture, effects]
related: [techniques/film-grain, techniques/blend-modes, cookbook/whip-in-title]
verified: design/1 (Carvercat 0.1.10)
source_inspiration: [https://github.com/carvercat/carvercat-skills]
---

# Give a title a film look with a grain overlay

**Goal.** Take a clean title card and make it feel shot on film (or taped): one grain over the whole picture, faded in with the card.

## Steps

1. Build the card: a dark ground and the title (here a 160 px bold text on `#14141f`).
2. Add an **adjustment layer** above everything (`object.new {kind: "adjustment"}`). It has no picture; its effects apply to
   everything below it.
3. Set the grain on it: `property.set {id, key: "grain", value: "0.08 1.5px softness=0.4 colour=0.1"}` for a quiet film finish.
   For an old print use `"0.2 2.2px softness=0.4 colour=0.1"`; for tape `"0.22 3.5px softness=0.5 colour=0.6"`.
4. Fade it in with the card: `anim.set {id, keyframes: [{at: 0, grain: "0 1.5px", ease: "ease-out"}, {at: 24, grain: "0.08 1.5px"}]}`.
5. Look at 100 % (`carvercat_look` on the full frame), then run `measure.contrast` on the title against the ground.

## Measured in Carvercat (design/1)

`wiki/tools/verify_keyed_pages.py` cases `film-grain` and `whip-in-title-and-film-look`.

- On a flat `#808080` the default `"0.25 1.5px"` reads a standard deviation of 0.050 and amount 1 reads 0.198 (0.2 x amount);
  the mean stays 0.502, so the ground does not get lighter or darker. Full table: [film grain](../techniques/film-grain.md).
- A new frame gives new pixels; with `held` two frames are identical pixels.
- `carve.preflight`: `filter:grain` is `approximate` on Resolve and on After Effects (a Fusion Film Grain and an Add Grain).

## Traps

- Grain on a card with small light text: from about 0.3 the text loses its edge. Lower the amount or use `colour=0`.
- One adjustment layer for the whole picture. Several layers each with grain add up and read as dirt.
- Lint reports an adjustment layer as one `never_visible` warning (it draws nothing itself; [KI-158](../../ai/references/known-issues.md#ki-158)): look at the picture, not the lint line.
- It covers the comp for the layer's length: set its `start` and `duration` to the card's, or it grains the next scene too.
- A freeze frame under animated grain shimmers: add `held`.

## In Carvercat

- Design key `grain`: [reference](../../ai/references/effects/grain.md). Technique and numbers: [film grain](../techniques/film-grain.md).
- Library: Retro pack `Film countdown leader` ([rt-film-leader](../../ai/patterns/rt-film-leader.md), grain on its ground).
- Recipes with a finishing grain layer: [retro night promo](../../ai/recipes/retro-night-promo.md), [luxury product teaser](../../ai/recipes/luxury-product-teaser.md), [glitch music teaser](../../ai/recipes/glitch-music-teaser.md).
