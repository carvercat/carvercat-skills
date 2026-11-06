---
id: cookbook/camera-push-on-a-still
title: Fake a camera push on a still
section: cookbook
tags: [ken burns, push in, zoom, still, photo, slow zoom, nested comp, plate]
styles: [corporate-brand, minimal-luxury, explainer, social-short-form]
topics: [camera, depth]
related: [techniques/camera-moves-2d, techniques/nested-comps-and-time, techniques/parallax, cookbook/seamless-loop]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://videobolt.net/motion-graphics-glossary/ken-burns-effect, https://pypi.org/project/burns/]
---

# Fake a camera push on a still

**Goal.** A photo, plate or held frame that never sits dead: a slow, constant push towards its centre.

## Steps

1. Put the still (an image, or a stand-in built from shapes) in its **own comp** at the frame size, then
   place that comp as one **nested instance** in the scene. One scale on the instance moves everything
   inside it together.
2. Either apply the Library preset **`Photo push - 5 s`** to the instance (`preset.apply {name, id}`), or
   key `scale` yourself: 1.0 → 1.05–1.10, `linear`, over the whole shot. Linear keeps
   the speed constant, so the cut in and out of the shot does not reveal an ease.
3. To push towards a point that is not the centre, also drift the position a few pixels a second in the
   opposite direction, rather than moving `transformOrigin` of a nested instance.
4. Never scale below 1.0 on a full-frame plate: the edges would show.

## Measured in Carvercat 0.1.6

Comps `K Push linear` and `K Push preset` in [cookbook lab 1](../labs/README.md#cookbook-lab-1carverproj):
the 1920 × 1080 comp `K Still` placed as an instance, 150 f, `carvercat_inspect probe` on the instance.

| Version | Keys | Width at f0 → f75 → f149 | Growth per side |
|---|---|---|---|
| Hand-keyed | scale 1.0 → 1.08 `linear`, f0 → f150 | 1920 → 1996.8 → 2072.6 px | 0.51 px a frame |
| `Photo push - 5 s` preset | `scale` 1.0 → 1.06 `linear`, f0 → f149 (what the preset wrote; its old key name is `scaleUniform`) | 1920 → 1978.0 → 2035.2 px | 0.39 px a frame |

- The frame-centre marker stayed at the centre in `carvercat_look` at f0 and f149.
- `inspect lint`: **0 errors, 0 warnings, 0 notes** for both.
- The preset ends at f149: a shot longer than 150 f stops moving, so stretch the keys with the shot.

## Traps

- Nested instances ignore a parent's transform; bake camera moves into the instance's own keys:
  [KI-119](../../ai/references/known-issues.md#ki-119).
- On comp instances the old `anchor` did not compensate the position (not re-measured for `transformOrigin`): [KI-109](../../ai/references/known-issues.md#ki-109).
- Shapes larger than the comp are cropped before their scale: [KI-137](../../ai/references/known-issues.md#ki-137).
- Lint does not see content cut by the frame edge inside a moving nested instance:
  [KI-144](../../ai/references/known-issues.md#ki-144).
- Small paths scaled up render soft: [KI-061](../../ai/references/known-issues.md#ki-061).

## In Carvercat

- Preset `Photo push - 5 s` (Corporate Brand pack); used inside `Split screen`
  ([cb-split-screen](../../ai/patterns/cb-split-screen.md)).
- Zoom moves between shots: preset `Exit zoom through` and the recipe ([tr-zoom-through](../../ai/patterns/tr-zoom-through.md)).
- Background: [camera moves](../techniques/camera-moves-2d.md), [nested comps](../techniques/nested-comps-and-time.md),
  [parallax](../techniques/parallax.md).
