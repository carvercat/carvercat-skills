---
id: cookbook/ken-burns-slideshow
title: Make a Ken Burns photo slideshow
section: cookbook
tags: [ken burns, slideshow, photo slideshow, pan and zoom, stills, dissolve, memories, montage]
styles: [corporate-brand, minimal-luxury, explainer, social-short-form]
topics: [camera, stills, timing]
related: [cookbook/camera-push-on-a-still, cookbook/cross-dissolve, techniques/camera-moves-2d, principles/slow-in-slow-out, sound-and-timing/reading-time]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Ken_Burns_effect]
---

# Make a Ken Burns photo slideshow

**Goal.** Three stills, each slowly zooming and drifting, joined by short dissolves, so a still looks like it was
filmed. The edges of the picture must never show.

## Steps

1. One clip per photo, each the full 1920 × 1080 frame (here a gradient rectangle stands in for a photo).
   Photo *i* starts at f 75 × *i*, lasts 90 f: 75 f of its own time plus 15 f under the next photo.
2. **Zoom**, `linear` on both keys: photo 1 and 3 scale 1.00 → 1.12 over the clip, photo 2 runs the other way,
   1.12 → 1.00. Linear keeps the speed constant, as a camera would ([camera push](camera-push-on-a-still.md)).
3. **Drift**: key the position along the same span, 100 px sideways and 40 px down at the end of the zoom-in;
   photo 2 drifts back to the centre. Alternate the direction (photos 1 and 3 go right, photo 2 starts left).
4. **Edge rule.** At any frame the offset must not exceed the margin the zoom has made: offset ≤ (scale − 1)
   × 960 px sideways, ≤ (scale − 1) × 540 px vertically. Start a zoom-in with zero offset and let both grow
   together; end a zoom-out with zero offset.
5. **Dissolve**: photos 2 and 3 fade opacity 0 → 1 over their first 15 f (`linear`) while the previous photo keeps
   running underneath ([cross-dissolve](cross-dissolve.md): fade only the incoming clip).

## Measured in Carvercat 0.1.6

Comp `K Ken Burns` (240 f) in [cookbook lab 9](../labs/README.md#cookbook-lab-9carverproj); `inspect probe` of
the three photo clips, every frame:

| Frame | 0 | 37 | 74 | 82 | 89 | 90 |
|---|---|---|---|---|---|---|
| Photo 1 width (px) | 1920.0 | 2014.7 | 2109.4 | 2129.9 | 2147.8 | gone |
| Photo 1 centre x | 960.0 | 1001.1 | 1042.2 | 1051.1 | 1058.9 | |
| Photo 2 opacity | 0 | 0 | 0 | 0.467 | 0.933 | 1.0 |

- Zoom speed **2.56 px/frame** in width (0.12 × 1920 / 90) and drift **1.11 px/frame**, constant.
- Worst edge cover over every frame the photo is visible (a value ≤ 0 on the left and top, ≥ 1920 and ≥ 1080 on
  the right and bottom means covered): photo 1 exactly 0.0 / 1920.0 / 0.0 / 1080.0 (at f0, no margin to spare);
  photo 2 −2.4 / 1920.2 / −1.1 / 1080.3 (the end of its zoom-out); photo 3 −0.2 / 1922.4 / −0.3 / 1081.1. The
  frame is covered on all 240 frames.
- The dissolve is linear: photo 2 is 0.467 at f82 and 0.933 at f89; the centre pixel goes (167, 133, 97) on f75,
  (169, 119, 88) on f82, (171, 100, 75) on f90.
- `inspect lint`: 0 errors, 0 warnings, 0 notes. `inspect qc` reports three **freeze** notes (f0–75, f90–150,
  f165–239) although the picture moves 2.56 px every frame ([KI-164](../../ai/references/known-issues.md#ki-164)).

## Traps

- A zoom that starts at 1.0 has no margin: any drift at the first frame shows the edge. Grow the drift with the
  zoom, as above.
- Ease the zoom (S-curve) and the speed changes visibly at every cut; for a slideshow keep `linear`.
- Slow moves can be read as "frozen" by qc: [KI-164](../../ai/references/known-issues.md#ki-164). Look at the
  frames instead ([lint and QC audit](../workflow/lint-and-qc-audit.md)).
- Real photos: 1.12 of a 1920 px photo is soft on a 4K export; use a photo at least 1.2 × the frame.

## In Carvercat

- Curve names on this page (S-curve) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Photo push - 5 s` (one still, scale 1 → 1.06), `Photo stack` for framed stills.
- Commands: `media.import`, `anim.set` / `key.set` on `scale` and `x`, `y`, opacity keys for the dissolve.
- Background: [camera moves 2D](../techniques/camera-moves-2d.md), [slow in and slow out](../principles/slow-in-slow-out.md).
