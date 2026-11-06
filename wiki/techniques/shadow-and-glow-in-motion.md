---
id: techniques/shadow-and-glow-in-motion
title: Shadow and glow in motion
section: techniques
tags: [shadow, drop shadow, lift, glow, halo, neon, pulse, depth, light]
styles: [saas-ui, futuristic-hud, retro, corporate-brand, minimal-luxury]
topics: [depth, light, effects]
related: [principles/solid-drawing-2d, techniques/faux-3d, principles/secondary-action, accessibility/photosensitivity]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://fluent2.microsoft.design/motion, https://atlassian.design/foundations/motion]
---

# Shadow and glow in motion

Shadows say "this is above that"; glows say "this emits light". Animated, they become the cheapest way to
show lift (a card rising towards the viewer), power (a button switching on) and energy (a neon pulse).

## The idea

- **Lift**: as an object comes closer, its shadow moves further away, grows softer and gets fainter, while the
  object scales up a little.
- **Settle**: the reverse; the shadow tightens as the object lands.
- **Glow on**: a light source powers up; the halo grows, then settles slightly lower.
- **Pulse**: a slow glow breathe for "live", "recording", "active" states.

## Rules of thumb

- Lift over 12–18 f: shadow offset ×3–4, blur ×3–5, opacity down by a third; object `scale` 1.03–1.05.
- Glow pulse: 20–40 f period, S-curve, between a calm and a bright value; never into clipping.
- One light direction for every shadow in the scene ([solid drawing](../principles/solid-drawing-2d.md)).
- Shadows need a lighter ground; on near-black use a glow or rim instead.

## Measured in Carvercat

The 0.1.6 measurements, in the units you set today. The shadow is `dropShadow` (`"x y blur color"`, x right and y **down**, in px; the
blur is a Gaussian sigma, as in CSS). The glow is `glow` (`"radius color strength mix"`). The stored values the lab projects hold
(offsets as fractions of the frame, softness, glow size) convert with `x = offset × 1920`, `y = −offset × 1080` (the stored y is up),
`blur = softness × 0.433 × 1920`, `radius = size × 1.15 × 1920 / 1920`. `scene.get` on the lab comps reads them back as below.

**Shadow** (opacity 1, on a 200 px white square over mid grey), measured on a rendered frame:

| `dropShadow` (the 0.1.6 offsets and softness) | Shadow reaches past the right edge | past the bottom edge |
|---|---|---|
| `"19.2px 10.8px 0px #000"` (0.01, −0.01, softness 0) | 20 px | 12 px |
| `"19.2px 10.8px 8.3px #000"` (0.01, −0.01, softness 0.01) | 34 px | 26 px |
| `"38.4px 21.6px 16.6px #000"` (0.02, −0.02, softness 0.02) | 68 px | 51 px |

- An x offset is in px along the width and a y offset in px down the height: 0.01 of the width is 19.2 px, 0.01 of the height is 10.8 px.
- The blur adds roughly 14 px of spread per 8.3 px of blur on each side.

**Blur to ramp.** A 160 px white square on linear 0.5 grey with a black shadow (opacity 1) pushed 288 px to the side so its right edge stood
alone. The edge profile, converted back to linear light, rendered at 1920 × 1080:

| `dropShadow` blur | 90% → 10% edge ramp | Equivalent Gaussian σ (ramp ÷ 2.563) | σ ÷ blur |
|---|---|---|---|
| `0px` | 2 px (anti-aliasing only) | 0.8 px | none |
| `4.2px` (softness 0.005) | 10 px | 3.9 px | 0.94 |
| `8.3px` (0.01) | 22 px | 8.6 px | 1.03 |
| `16.6px` (0.02) | 42 px | 16.4 px | 0.99 |
| `33.3px` (0.04) | 88 px | 34.3 px | 1.03 |

- The blur is a sigma: the visible soft edge (10–90%) is about **2.563 × the blur** in px (8.3 px of blur: 21 px of edge). The old
  rule of thumb, σ ≈ 0.44 × softness × comp width, is the same thing (0.433).
- The edge stays centred on the shadow's geometric edge (the 50% point did not move), so the blur spreads the
  shadow equally inwards and outwards; at 33 px of blur a 160 px shadow no longer reached full density in its centre (97%).
- The σ column assumes a Gaussian-shaped edge; only the 10–90% widths were measured.

**Glow** (on a 200 px blue square, linear `[0.2, 0.6, 1.0]`, over black):

| `glow` | Halo reach past the edge | Core colour (was 111, 197, 255) |
|---|---|---|
| `"11.5px 0.4 0.2"` (old amount 0.4, size 10, blend 0.2) | 22 px | 118, 210, 255 |
| `"11.5px 0.8 0.2"` (0.8, size 10, 0.2) | 27 px | 152, 255, 255 (green clipped) |
| `"34.5px 0.8 0.2"` (0.8, size 30, 0.2) | 80 px | 151, 255, 255 |
| `"11.5px 0.8 0"` (0.8, size 10, blend 0) | none | unchanged |

- **The radius sets the reach** (11.5 px → about 25 px, 34.5 px → 80 px); **the strength sets intensity** and brightens the core.
- With a `mix` of 0 the glow shows nothing at all; keep it around 0.2.
- Bright colours clip early: at strength 0.8 this blue's green channel hit 255.

## Do and don't

- Do animate shadow offset, blur and colour alpha together for lift.
- Do raise the glow radius for a bigger halo instead of raising the strength.
- Don't pulse glow faster than about 3 times a second or over large areas (flash risk).
- Don't put shadows on every child of a card; shadow the card.

## Checklist

- [ ] All shadows share direction and blur logic.
- [ ] Glow strengths stay below clipping on the brightest colour (check a render).
- [ ] Pulses are slow and `qc` shows no flashes.

## In Carvercat

- Curve names on this page (S-curve) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Shadow: `dropShadow: "0 8px 6px #0000004d"` (x y blur color, y down, blur a sigma in px; also `{x, y, blur, color}`), or
  `filter: "drop-shadow(0 8px 6px #0000004d)"`. Glow: `glow: "12px #ffcc00 0.6 0.2"` (radius, color, strength 0–1, mix 0–1).
  Ranges: |x| up to half the width, |y| up to half the height, shadow blur up to 166 px and glow radius up to 115 px at 1920 wide.
  `none` takes the effect off. All can be keyed by name in `anim.set` (checked: `dropShadow` and `glow` keyed together, f18 reads `0px 28px 30px`). Carve status: Resolve exact; After Effects approximate.
- Old names, accepted for one release: the `shadow` effect (`Offset X`, `Offset Y` as fractions with y up, `Softness`, `Opacity`, colour
  `Red`/`Green`/`Blue`; [shadow](../../ai/references/effects/shadow.md)) and the `glow` effect (`Glow`, `Size`, `Blend`;
  [glow](../../ai/references/effects/glow.md)).
- Ready-made lift: `Card lift` ([SaaS UI](../../ai/patterns/saas-ui.md)); glow looks in
  [Futuristic HUD](../../ai/patterns/futuristic-hud.md) and [Retro](../../ai/patterns/retro.md).
- Labs: comp `F Shadow glow` in [the measurement lab 3](../labs/README.md); comp `F Shadow softness` in [the audio and shadow lab](../labs/README.md).
