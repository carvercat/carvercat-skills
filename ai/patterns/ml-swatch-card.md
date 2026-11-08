# Material swatches

**Template** `ml_swatch_card` (Library name "Material swatches") · Minimal Luxury pack · **Verified 0.1.8.1 (rev 1127)**, comp `ML Swatch card` in `categories/minimal-luxury/ml-lab-3`.

For briefs like "show the materials", "three colourways", "the finishes on offer". Three swatches (320 × 400 px, cognac leather, brushed gold, ivory silk) under a tracked heading, each with a name and a code. Over the hold a soft lighter band crosses each swatch once, like light on a material, and the row keeps drifting up. 180 f, holds.

Frames are comp frames.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Heading "THE MATERIALS" (gold Regular 28 px, tracking 1.6) | 0 | Slow fade in (baked); tracking 1.60 → 1.64 to the end | opacity settles **f31**, size **f27** |
| Swatches (centres x 480 / 960 / 1440, y 500) | 16, 30, 44 | up 16 px over 44 f (decelerate) and opacity over 36 f; then a 0.4% H drift up to the clip end | **0% overshoot**; Swatch 1 opaque **f47**, Swatch 3 **f75** |
| Sheen (shape gradient: base / lighter band / base, stops 0.3 / 0.5 / 0.7) | | gradient start −1 → 1 and end 0 → 2 (object-local), f70–150, f80–160, f90–170, S curve cubic-bezier(0.333, 0, 0.667, 1), the curve arriving at the key | Swatch 1 settles **f142**, Swatch 3 **f162** |
| Names (ivory Regular 28 px, tracking 1.25, y 762) | swatch + 14 | opacity in 36 f | Name 3 opaque **f89** |
| Codes (muted Regular 26 px, tracking 1.2, y 812) | swatch + 20 | opacity in 36 f | Code 3 opaque **f95** |

Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 21 pairs, closest 30.5 px (Name 3 / Code 3). Ink at f170 (`carvercat_authoring geometry`): Name 1 x 309–651, Name 2 795–1125, Name 3 1320–1560, so 144 px and 195 px between the names; Code 1 ends at 657 and Code 2 starts at 828.

## Steps
1. New materials: edit `SWATCHES` (name, code, base colour, sheen colour) in `ai/scripts/motion/minimal_luxury_lab3.py` and rebuild, or change the texts and the swatch colours after placing.
2. Keep the sheen colour one step lighter than the base; a white band reads as a stripe, not a light.

## Pitfalls
- **The first build ran the names into each other.** At 400 px apart and tracking 1.3, "NAPPA LEATHER" and "BRUSHED GOLD" were each about 400 px wide and nearly touched, and lint said nothing ([KI-138](../references/known-issues.md#ki-138)). 480 px apart at tracking 1.25 leaves 144 px. Measure longer names before placing.
- The sheen is a shape gradient with keyed endpoints. Shape gradient endpoints are live; text gradient endpoints are not ([KI-009](../references/known-issues.md#ki-009) c).

Inspiration: material and colourway cards in fashion and interiors films. No external text or code was used.
