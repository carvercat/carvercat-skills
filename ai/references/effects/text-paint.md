# Text paint: fill, outline, hollow type

**Verified 0.0.72:** hollow outline type — `text.fill.color` alpha 0 ([1,1,1,0]) + `text.outline.color` navy + `text.outline.thickness` 0.03 → clean outlined letters.

| control | notes |
|---|---|
| text.fill.color / paint / gradient | as shapes ([fill-and-gradients.md](fill-and-gradients.md)); text gradient endpoints are not live |
| text.outline.color, thickness (0–0.2) | thickness is RELATIVE TO THE TEXT SIZE (not the frame); 0.02–0.04 for display type. The band straddles the glyph edge: an opaque fill hides its inner half |
| text.outline.blur / glow | outline-only softening (declared; not verified) |
| text.relative.* | per-text relative transform used by stagger slots |

## Rules
- **Always set `text.fill.color`** — new text renders red on 0.0.72.
- Hollow type needs size ≥ ~70 px and a bold weight; thin weights + outline look broken.
- Outline + fill in different colours = sticker/arcade look; keep outline ≤ 0.04.
- Legibility over busy imagery: a soft drop shadow (offset 0, softness 0.02) or a pill behind beats a thick outline.
- For outline to reveal with a stagger, connect its own opacity slot (`stroke.opacity`) — fill opacity alone leaves the outline visible.
