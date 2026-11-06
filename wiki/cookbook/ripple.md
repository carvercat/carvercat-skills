---
id: cookbook/ripple
title: Make a ripple
section: cookbook
tags: [ripple, tap, click, ring, pulse ring, ui feedback, shockwave]
styles: [saas-ui, explainer, futuristic-hud, social-short-form]
topics: [ui, feedback, timing]
related: [principles/secondary-action, genres/ui-ux-demos, cookbook/draw-attention-pulse, cookbook/pop-in]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://m3.material.io/foundations/interaction/states/overview, https://www.nngroup.com/articles/progress-indicators/]
---

# Make a ripple

**Goal.** A ring that spreads from a tap or an impact and fades away, once or as a few echoes.

## Steps

1. Draw a **ring**: an ellipse with fill `none` and a stroke (6 px here), at its **largest** size
   (240 px). Growing to 1.0 keeps the stroke at its drawn width; scale multiplies the stroke too
   ([scale vs size](../techniques/scale-vs-size.md)).
2. Start the ring clip **on the tap frame** and make it about 18 f long.
3. Apply the Library preset **`Tap ripple`** (`preset.apply {name:"Tap ripple", id}`): it keys the ring
   from 25% to full size and fades it out. Or key it yourself: scale 0.4 → 1.6 expo out and opacity 1 → 0
   linear over 24 f.
4. For echoes, copy the ring and start each copy 6 f later.

## Measured in Carvercat 0.1.6

Comp `K Ripple` in [cookbook lab 2](../labs/README.md#cookbook-lab-2carverproj), 240 px rings, 6 px stroke,
`carvercat_inspect` `curves` and `probe`:

| Ring | Keys the preset wrote | Width | Opacity |
|---|---|---|---|
| `Tap ripple` (clip at f10) | `scale` 0.25 → 1.0 (old name `scaleUniform`) over 17 f (baked keys), opacity 0.7 held 3 f then down to 0 | 60 px at f10, 202 at f14, 237 at f20 | 0.70 to f13, 0.25 at f16, 0.03 at f22, 0 at f27 |
| Hand-keyed (clip at f10) | scale 0.4 → 1.6 expo, opacity 1 → 0 linear, 24 f | 96 px at f10, 334 at f16, 384 at f32 | 0.75 at f16, 0.08 at f32 |

- `Tap ripple`: scale settles f21 (11 f after the tap); the ring is gone 17 f after the tap.
- Echo rings at f16 and f22 ran the same curve 6 and 12 f later.
- `inspect lint`: 0 errors, 0 warnings, 3 notes (`repeated_key_value`: the preset's held 0.7 opacity).

## Traps

- `preset.apply` takes one `id`; apply it to each ring: [KI-113](../../ai/references/known-issues.md#ki-113).
- Shapes larger than the comp are cropped before scaling; for a full-screen shockwave draw the ring at
  comp size or less and scale it up: [KI-137](../../ai/references/known-issues.md#ki-137).

## In Carvercat

- Curve names on this page (expo out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Tap ripple` (SaaS UI), `Cursor click` ([su-cursor-click](../../ai/patterns/su-cursor-click.md)),
  `Map ping` ([fh-map-ping](../../ai/patterns/fh-map-ping.md)).
- Background: [secondary action](../principles/secondary-action.md), [UI and UX demos](../genres/ui-ux-demos.md).
