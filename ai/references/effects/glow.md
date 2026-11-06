# Glow: controlled, never burnt

`glow "radius [colour] [strength 0-1] [mix 0-1]"`: radius in px (the glow's blur, a Gaussian sigma, 0 to 115 x W/1920 px), strength 0 to 1 (default 0.8), mix 0 to 1 (default 0.2). `property.set {key: "glow", value: "18px #1a99ff 0.7 0.2"}`; `"none"` removes it. Verified: glow-presets-and-pulse.

Glow ADDS light onto the element, so it brightens the core as well as making a halo. Past a limit the core clips to white and "burns". The numbers below were **measured on the stored parameters** on 0.0.72 (comp `FX Glow calibration`: a 115 x 12 px bar, linear colour [0.1, 0.6, 1], rendered and measured per pixel; and `FX Glow grid` for mix). They carry over unchanged in the new units: **strength is the stored amount (same number), mix is the stored blend (same number), radius px is the stored size x 1.15 at 1920 wide** (a stored size of 6, 12, 24 and 48 is a radius of 6.9, 13.8, 27.6 and 55.2 px). The conversion is checked in glow-presets-and-pulse (18 px reads back as stored size 15.65).

## Measured
| strength | core (8-bit RGB, original about 66,178,231) | verdict |
|---|---|---|
| 0.2 to 0.6 | +2 to +30 | clean |
| 0.7 to 0.8 | brighter, colour holds | **ceiling for a coloured glow** |
| 0.9 | one channel clips (G 239 to 255), hue shifts toward cyan/white | hot: avoid except for a flash |
| 1.0 | (255,255,255) at radius 7 to 14 px; (220,255,255) at 28 px | **BURNT** |

| radius | halo reach above the edge (strength 0.6, luminance above 20) |
|---|---|
| 7 px (stored size 6) | about 18 px |
| 14 px (size 12) | about 30 px |
| 28 px (size 24) | about 50 px |
| 55 px (size 48) | 100 px and more (a wide wash) |

**Reach comes from the radius; intensity from the strength.** Want a bigger glow: raise the radius, not the strength.

| mix | effect (strength 0.3 to 1, radius 21 px) |
|---|---|
| 0.1 to 0.3 (default 0.2) | crisp core plus halo: use this |
| 0.5 | core visibly softened and dimmed |
| 1.0 | core replaced by the soft glow (the element looks out of focus); with strength 0.6 or more it blows out |

## Safe presets
| Look | radius | strength | mix | call |
|---|---|---|---|---|
| Subtle UI glow / premium | 9 to 14 px | 0.4 to 0.5 | 0.2 | `"10px #1a99ff 0.45 0.2"` |
| Neon line / sign | 14 to 28 px | 0.6 to 0.75 | 0.2 | `"18px #1a99ff 0.7 0.2"` |
| Big soft aura | 41 to 55 px | 0.4 to 0.6 | 0.15 | `"42px #1a99ff 0.5 0.15"` |
| One-frame flash on an impact | 28 px | 0.8, 0.95, 0.6 over 6 f | 0.2 | key the strength (below) |

## The colour is a tint
The colour of a glow multiplies the element's own channels: a white element glows in that colour (verified: glow-tints-a-white-element: a white bar with `"24px #1a99ff 0.6 0.2"` has a blue halo, about (13,57,101) just above the bar, and a core still near white), while a blue element with a `#ffcc00` glow gets a green halo (seen in the glow-presets look). Pick a colour close to the element's hue for a clean glow, or white-ish elements for any colour.

## Animation
Strength, radius, colour and mix key together through the `glow` design key (verified: keyed-glow-shadow-brightness), or one at a time on the stored parameters.

- **Pulse:** strength 0.5 to 0.8 and back, `ease-in-out`, 20 to 40 f period. Never pulse into 0.9 or more. By design name (verified: keyed-glow-shadow-brightness):

  ```json
  {"command": "anim.set", "args": {"id": "#neon", "keyframes": [
    {"at": 0, "glow": "18px #1a99ff 0.5 0.2", "ease": "ease-in-out"}, {"at": 15, "glow": "18px #1a99ff 0.75 0.2", "ease": "ease-in-out"}, {"at": 30, "glow": "18px #1a99ff 0.5 0.2"}]}}
  ```

  The stored route (verified: glow-presets-and-pulse), keyed on the entry's `amount`, which is the strength:

  ```json
  {"command": "property.set", "args": {"id": "#neon", "key": "glow", "value": "18px #1a99ff 0.7 0.2"}}
  {"command": "key.set", "args": {"id": "#neon", "key": "fx.e_fx_glow_clip_3.amount", "value": 0.5, "at": 0, "ease": "ease-in-out"}}
  {"command": "key.set", "args": {"id": "#neon", "key": "fx.e_fx_glow_clip_3.amount", "value": 0.75, "at": 15, "ease": "ease-in-out"}}
  {"command": "key.set", "args": {"id": "#neon", "key": "fx.e_fx_glow_clip_3.amount", "value": 0.5, "at": 30}}
  ```

  `key.list {id, key}` returns the frames and values back. Find the entry path with `param.list {id, match: "glow"}`.
- **Power-on:** strength 0 to 0.75 over 10 f `ease-out`, then settle 0.65.
- Animate the radius for "breathing" auras (14 to 23 px, stored `size` 12 to 20): it keeps the core colour stable.

## Rules
1. **White elements:** measured on the stored parameters, the core stays at 240 to 247 for strength 0.2 to 0.7 (it is already at the top), so it does not burn further. With no colour (or a white one) the halo is colourless and the element loses its edge: give the glow a colour and it tints the halo (see above); tinting the element slightly (0.8 to 0.9 grey or a pale hue) still helps the edge.
2. Glow only the hero (one element per frame). Two glowing things compete.
3. On light backgrounds glow barely reads; use [shadow.md](shadow.md) or a coloured soft-edge shape behind instead ([soft-edge.md](soft-edge.md)).
4. **Secondary glow** (a second chained glow with its own amount/size/colour) lives in the basement: `param.promote {id, path: "fx.<entry>.secondary", on: true}` then `property.set {key: "fx.<entry>.secondary", value: true}` (both batchable); `secondaryAmount` (strength) and `secondarySize` (stored size units) are then stored paths. **Verified** (glow-secondary-in-the-basement): promote and set both accepted and the stored values read back `on`. Measured on 0.0.72 at amount 0.5, size 12 (a 14 px radius): adding the secondary (defaults amount 0.5, size 40, a 46 px radius) extended the halo from about 30 px to about 58 px with the core colour unchanged: the right way to get a wide halo without burning. See [basement-promote-ropes.md](basement-promote-ropes.md).
5. Measure, don't guess: `carvercat_render` a frame and check the core pixel stays below 250 in every channel (the cases above read pixels with Pillow).
