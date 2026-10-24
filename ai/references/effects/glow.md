# Glow — controlled, never burnt

**Calibrated on 0.0.72** (comp `FX Glow calibration`: a 115×12 px bar, linear colour [0.1, 0.6, 1], rendered and measured per pixel; and `FX Glow grid` for blend). Glow ADDS light onto the element, so it brightens the core as well as making a halo. Past a limit the core clips to white — "burns".

## Measured
| amount | core (8-bit RGB, original ≈ 66,178,231) | verdict |
|---|---|---|
| 0.2–0.6 | +2…+30 | clean |
| 0.7–0.8 | brighter, colour holds | **ceiling for a coloured glow** |
| 0.9 | one channel clips (G 239–255) → hue shifts toward cyan/white | hot — avoid except for a flash |
| 1.0 | (255,255,255) at size 6–12; (220,255,255) at 24 | **BURNT** |

| size | halo reach above the edge (amount 0.6, lum > 20) |
|---|---|
| 6 | ~18 px |
| 12 | ~30 px |
| 24 | ~50 px |
| 48 | 100 px+ (wide wash) |

**Reach comes from `size`; intensity from `amount`.** Want a bigger glow → raise size, not amount.

| blend | effect (amount 0.3–1, size 18) |
|---|---|
| 0.1–0.3 (default 0.2) | crisp core + halo — use this |
| 0.5 | core visibly softened/dimmed |
| 1.0 | core replaced by the soft glow (element looks out of focus); with amount ≥ 0.6 it blows out |

## Safe presets
| Look | size | amount | blend |
|---|---|---|---|
| Subtle UI glow / premium | 8–12 | 0.4–0.5 | 0.2 |
| Neon line / sign | 12–24 | 0.6–0.75 | 0.2 |
| Big soft aura | 36–48 | 0.4–0.6 | 0.15 |
| One-frame flash on an impact | 24 | 0.8 → 0.95 → 0.6 over 6 f | 0.2 |

## Animation
- **Pulse:** amount 0.5 ↔ 0.8, S-curve, 20–40 f period. Never pulse into 0.9+.
- **Power-on:** amount 0 → 0.75 over 10 f Ease out, then settle 0.65.
- Animate `size` for "breathing" auras (12 ↔ 20) — keeps the core colour stable.

## Rules
1. **White elements:** measured, the core stays at 240–247 for amount 0.2–0.7 (it is already at the top), so it doesn't burn further — but the halo is colourless and the element loses its edge. For "white light", tint the element slightly (0.8–0.9 grey or a pale hue) and colour the halo with the secondary glow's red/green/blue scales.
2. Glow only the hero (one element per frame). Two glowing things compete.
3. On light backgrounds glow barely reads; use [shadow.md](shadow.md) or a coloured soft-edge shape behind instead.
4. **Secondary glow** (a second chained glow with its own amount/size/colour) lives in the basement: `param.promote {id, path:"fx.<entry>.secondary", on:true}` then `property.set … secondary true` (both batchable). **Verified:** at amount 0.5, size 12, adding the secondary (defaults: amount 0.5, size 40) extended the halo from ~30 px to ~58 px with the core colour unchanged — the right way to get a wide halo without burning. See basement-promote-ropes.md.
5. Measure, don't guess: `carvercat_render` a frame and check the core pixel stays below 250 in every channel.
