---
id: techniques/soft-edge-and-feather
title: Soft edge and mask feather
section: techniques
tags: [soft edge, softEdge, one soft edge, feather, mask, blur, fade edge, vignette, wipe, px]
styles: [minimal-luxury, corporate-brand, kinetic-typography, retro, futuristic-hud]
topics: [compositing, reveal, edges]
related: [techniques/soft-and-inverted-masks, techniques/masking, techniques/shadow-and-glow-in-motion, techniques/motion-blur, cookbook/vignette, cookbook/iris-wipe]
verified: design/1 (Carvercat 0.1.8)
source_inspiration: []
---

# Soft edge and mask feather

Two names for one idea: the edge of a shape fades out over a width you choose, in **px**. A shape has **one** `softEdge`,
and it softens the shape as a whole, fill and stroke together; `feather` is the same number on a shape that is used as a
**mask**. One unit everywhere: the width of the visible fade, so the number you type is the number you see. On the canvas the fade looks
the same at every zoom (on screen it used to fade as the canvas zoomed out). That is a canvas fix: it was not driven
headless here, and the renders measured below are at the frame size.

## The idea

- A hard edge reads as graphic and precise; a soft edge reads as light, mist, depth or focus.
- A soft edge is the cheapest blur: it blurs the shape's own paint and costs one number, with no effect to add.
- A feathered mask makes a wipe or a reveal glide in instead of cutting.

## What the number means

`softEdge: 24` (or `"24px"`) gives an edge that rises from 10% to 90% over **24 px**, centred on the shape's edge. It is
the visible ramp, not a blur radius: the Gaussian under it has a sigma of px ÷ 2.563 (24 px is a sigma of about 9.4 px).
It does not depend on how big the shape's box is (the app's own render check, found the same ramp on 500, 800 and 1200 px boxes).

| Key | Where | Unit | Range | Default |
|---|---|---|---|---|
| `softEdge` | a shape: its fill and its stroke together | px (also `%` of the frame width, `pt`) | 0 to 0.2 × frame width (384 px at 1920) | 0 |
| `feather` | a shape that is a mask | px (the same ramp) | same | 0 |

`strokeSoftEdge` is an **old name** for `softEdge`, still accepted for one release: it sets `softEdge`, and the reply says
so (`deprecated: {use: "softEdge"}`). There is no separate stroke value any more, so a stroke-only shape (a vignette ring)
and a filled shape take the same key. A project saved with different fill and stroke values opens with the larger one.

A value above the range is refused with the range (`out-of-range`, `valid.range: ["0px", "384px"]` at 1920 wide). `"5%"`
is 5% of the frame width (96 px at 1920) and `"18pt"` is 24 px.

## Measured in Carvercat (design/1, Carvercat 0.1.8 build)

Each row is a white rectangle (800 × 500) on black, rendered at 1920 × 1080 with `carvercat_render`, the red channel read
along a row through the middle, converted to linear light, and the 10% and 90% points found by interpolation.

| Key set | Rendered 10-90% ramp | 50% point from the shape's edge |
|---|---|---|
| `softEdge` 8 | 8.2 px | within 0.5 px |
| `softEdge` 24 | 24.0 px | within 0.5 px |
| `softEdge` 60 | 60.6 px | within 0.5 px |
| `softEdge` 8 / 24 / 60 on a stroke-only shape (200 px stroke, no fill), outer edge | 8.2 / 24.0 / 60.0 px | within 0.5 px |
| `feather` 8 / 24 / 60 on the mask rectangle, white plate behind | 8.2 / 24.0 / 60.6 px | within 0.5 px |

- The fade is centred on the geometric edge: half of it sits inside the shape, half outside. A soft rectangle is therefore
  smaller at full strength than its box by half the ramp on each side.
- One value softens the whole shape: a white rectangle with a 40 px white stroke and `softEdge` 24 measured a 23.2 px ramp at the outer edge of the stroke.
- **Scale scales the fade.** The same rectangles at `scale` 2 measured 16.3, 48.0 and 120.4 px (softEdge 8, 24, 60). Size the
  edge for the final size of the object, and key `scale` and `softEdge` together if the edge must stay constant.

## Feather: a soft edge on a mask

A mask in Carvercat is another object (`mask` on the object to cut). Its softness is the **mask shape's own soft edge**:

1. Make the mask shape (a rectangle, ellipse or path; a rectangle was measured here), or let `clipPath` make it: `clipPath: "inset(100px round 40px)"`
   creates the rectangle and masks the object with it, and reports the mask it made.
2. Cut with it: on the object to cut, `property.set {key: "mask", value: "<mask id>"}` (the mask must be on another track).
3. Feather the mask shape: `property.set {id: "<mask id>", key: "feather", value: 40}`. It reads back as `softEdge` too: the
   same number under two names (`feather` refuses on a shape that is not a mask and points you at `softEdge`).

```json
{"command": "property.set", "args": {"id": "clip_3", "key": "feather", "value": 40}}
```

- Only a **shape** can be feathered. A picture or text used as a mask has no soft edge (the refusal says so, with code
  `not-settable`, and suggests `clipPath`).
- The window moves the same distance as its edge: to finish a wipe soft, let it travel its feather width past the content
  ([soft and inverted masks](soft-and-inverted-masks.md)).
- Inverted masks: `mask: {ref: "<mask id>", invert: true}`, set while the object has no mask yet.

## In the app: the Properties panel

(From the icon sheet's note for icon 555 and the design-units spec; the panel was not driven headless.)

A shape's **Soft edge** row sits in its own row of the Properties panel (no longer inside the colour block) with the
soft-edge icon, number 555 on the icon sheet: a sharp block whose edge falls off in three bars. The value is in px. The same row, with the same icon, is where a mask shape's **feather** lives: a mask
needs no mark of its own. There is one row for the whole shape; the second, stroke-only row of the first build is gone.

## Keying

A static `softEdge` or `feather` is one call. Both key by design name (checked: `wiki/tools/verify_keyed_pages.py`, cases
soft-edge-one-value-and-feather and feather-on-a-mask-shape: `softEdge` 0 → 24 read 0, 12 and 24 px at f0, f10 and f20
with a linear ease; `feather` 0 → 60 read 0 and 60 at f0 and f20):

```json
{"command": "anim.set", "args": {"id": "clip_3", "keyframes": [
  {"at": 0, "feather": "0px", "ease": "ease-out"},
  {"at": "20f", "feather": "60px"}]}}
```

`key.set {id, key: "softEdge", value, at, ease}` writes one key, `key.remove {id, key: "softEdge", at}` takes it off, and
`scene.get` shows the keys. A scene node takes the same keys in its `keyframes`. The older route, the stored parameter (for
example `src.e_src_shape_fill_clip_3.softEdge`, a fraction of the frame width: 24 px at 1920 is `0.0125`), still works.

## Carve status (what leaves for each host)

| Host | softEdge | feather |
|---|---|---|
| DaVinci Resolve | **exact**: a Fast Gaussian Blur of the shape's paint, keyed values baked per frame | **exact**: the mask shape's blur before the matte |
| After Effects | **approximate**: a Gaussian Blur on the shape layer, blurriness 3.55 per px of sigma | **approximate**: a Gaussian Blur on the matte layer |

Why approximate in After Effects: it has no soft edge on a shape fill, so the layer is blurred. A scaled layer scales its
blur (Carvercat does the same: the render measured above at `scale` 2); the layer blur softens fill and stroke together, as the one
`softEdge` does; the blur does
not stay inside the layer's bounds the way a native Mask Feather does. Ask before sending:
`carve.preflight {host: "aftereffects"}` lists `softEdge` as `approximate: layer Gaussian Blur`, and every `property.set` of
`softEdge` or `feather` carries the same status in its reply (`carve`).

## Do and don't

- Do read the number as the width of the fade you will see: 24 means 24 px from 10% to 90%.
- Do use `feather` 2 to 5% of the frame width (40 to 100 px at 1920) for luxury wipes and 0 for graphic styles.
- Do use `softEdge` instead of a blur effect on a flat shape: it is one number, exact in Resolve and cheaper.
- Don't feather a mask wider than its window can hold: the fade is centred on the edge, so a window narrower than the
  feather never reaches full strength.
- Don't use a soft edge on a shape that will be sent to After Effects at a different scale and expect it to match.

## Checklist

- [ ] The fade is stated in px and chosen from the style, at the size the object will have.
- [ ] A mask is a shape, with `feather` set on it, not on the object it cuts.
- [ ] `carve.preflight` was read for the host the project will be sent to.

## In Carvercat

- Keys: `softEdge`, `feather` (both px, keyable by name), `mask`, `clipPath`.
  Reference: `carvercat://schema/design`.
- Old names, accepted for one release: `strokeSoftEdge` (now the same value as `softEdge`), `shape.fill.softEdge` (and the removed `shape.stroke.softEdge`) as a **fraction of the frame width**
  (0.0125 for 24 px at 1920), `mask.make {ids: [mask, content]}`, and the `mask.invert` parameter, which did not render.
- Ready-made feathered reveal: `Feather wipe reveal` ([ml-feather-wipe](../../ai/patterns/ml-feather-wipe.md)); background:
  [soft edge](../../ai/references/effects/soft-edge.md), [masking](masking.md), [soft and inverted masks](soft-and-inverted-masks.md).
- Lab: comp `T Soft masks` in [measurement lab 3](../labs/README.md): its `Soft window` rectangle stores 0.03125, which is 60 px at 1920.
