---
id: cookbook/wipe-transition
title: Wipe from one scene to the next
section: cookbook
tags: [wipe, transition, panel, cover, cut under, scene change]
styles: [corporate-brand, sports, saas-ui, funky, transitions]
topics: [transitions, timing]
related: [techniques/match-cuts, techniques/rhythm-editing, accessibility/photosensitivity, cookbook/split-screen]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.premiumbeat.com/blog/cut-to-the-beat-tip-for-editing-to-music-in-final-cut-pro-x/, https://blog.frame.io/2018/02/12/animated-masks-after-effects/]
---

# Wipe from one scene to the next

**Goal.** A colour panel that sweeps across, hides the cut from scene A to scene B, and sweeps away.

## Steps

1. Lay scene A and scene B back to back, with the **cut** at the frame the panel fully covers the frame
   (f24 here).
2. A full-frame **panel** on top: key its position from off-screen left (centre x −960) to the centre,
   accelerating, so it covers the frame at f20.
3. Hold it 8 f (f20–f28). The cut happens under it.
4. Send it off to the right, expo out (f28–f40): fast first, then easing away.
5. Run `inspect qc` for flashes: a bright panel over a dark scene changes the luminance of the whole frame.

## Measured in Carvercat 0.1.6

Comp `K Wipe` in [cookbook lab 2](../labs/README.md#cookbook-lab-2carverproj), 60 f, panel #F2B03C
between a #31566A scene and a #F4F1EA scene; `carvercat_inspect probe` on the panel:

| Frame | Panel left edge → right edge (px) |
|---|---|
| f8 | −1920 → 0 (off screen) |
| f14 | −1624 → 296 |
| f18 | −881 → 1040 |
| f20–f28 | 0 → 1920 (**covers the frame**, 9 f) |
| f29 | 827 → 2747 |
| f32 | 1734 → 3654 |
| f40 | 1920 → 3840 (gone) |

- `inspect qc`: **no flash findings** (frame luma 0.32 to 0.94).
- `inspect lint`: 0 errors, 1 warning (`reading_time`: the scene A title was readable for 24 f, wants 25),
  2 notes (`speed_jump` 527.5 px/frame into the hold; `repeated_key_value` for the hold).
- The accelerate arrival hits the hold at 527 px a frame: a hard stop that reads as an impact. Use
  S-curve into the hold for a softer landing.

## Traps

- Shapes larger than the comp are cropped before scaling; move a frame-size panel, don't scale up a
  small one past the comp size: [KI-137](../../ai/references/known-issues.md#ki-137).
- `clip.move` is an overwrite edit; move scene clips in the project file or with care:
  [KI-032](../../ai/references/known-issues.md#ki-032).
- The qc loop-seam line is irrelevant here (`loops_cleanly: false` is expected for a transition).

## In Carvercat

- Curve names on this page (S-curve, expo out, accelerate) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library transitions: `Two-tone wipe` ([tr-two-tone-wipe](../../ai/patterns/tr-two-tone-wipe.md)),
  `Brand panel wipe` ([cb-panel-wipe](../../ai/patterns/cb-panel-wipe.md)), `Slash wipe`
  ([sp-slash-wipe](../../ai/patterns/sp-slash-wipe.md)), `Scan wipe` ([fh-scan-wipe](../../ai/patterns/fh-scan-wipe.md)),
  `Colour iris` ([tr-iris](../../ai/patterns/tr-iris.md)); the cover pack:
  [transitions](../../ai/patterns/transitions.md).
- Background: [match cuts](../techniques/match-cuts.md), [photosensitivity](../accessibility/photosensitivity.md),
  [transitions craft](../../ai/references/craft/transitions.md).
