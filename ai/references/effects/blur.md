# Blur

**Verified 0.0.72:** blur-in title (size 30 → 0 over 16 f, opacity 0 → 1 over 8 f, scale 1.08 → 1) reads as a focus pull; keys on `fx.<entry>.size` animate and render.

## Parameters that matter
| param | range | default | use |
|---|---|---|---|
| size | 0–100 | 10 | strength. Not a pixel radius: ≈1.15 px sigma per unit at 1920 width and scale 1 (app convention); scales with object scale |
| lock / sizeY | — | lock on | unlock for directional (horizontal speed) blur: size 20, sizeY 0 |
| filter | box…fastgaussian | fastgaussian | keep fastgaussian; box is cheaper/harsher |
| blend | 0–1 | 1 | mix with the sharp original (0.5 = dreamy halo over a sharp core) |
| clipping | none/domain/frame | frame | `none` lets blur spread past the object's bounds |

## Recipes
- **Focus pull in (title):** size 25–30 → 0 over 12–18 f, Ease out (arriving), with opacity 0 → 1 over the first half and a tiny scale settle 1.06–1.08 → 1. Exit is the mirror, faster (8–10 f), Ease in.
- **Depth of field:** background layers static size 6–12, mid 0–3, foreground sharp. Never blur text the viewer must read.
- **Whip/speed:** unlock, size 20–40 on X only for 2–4 frames around the fastest frame — or use [motion-blur.md](motion-blur.md), which follows the real motion.
- **Glass card:** a blurred copy of the background inside a mask under the card (see compositing-and-masks.md, not verified here).

## Pitfalls
- New blur starts at size 10 — set it explicitly.
- Big sizes on big objects are expensive; preview with looks, not playback.
- Blur makes edges extend: give room (or `clipping:none`) and check `inspect probe` `effect_spread`.
