---
id: cookbook/pop-in
title: Pop something in
section: cookbook
tags: [pop, scale in, overshoot, spring, stamp, icon, badge, entrance, preset]
styles: [all]
topics: [easing, entrances]
related: [principles/exaggeration, principles/springs, principles/easing-reference, cookbook/ripple, cookbook/draw-attention-pulse]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://m3.material.io/styles/motion/easing-and-duration/tokens-specs, https://www.nngroup.com/articles/animation-duration/]
---

# Pop something in

**Goal.** An icon, badge, card or word that arrives with a pop, picking the right amount of bounce.

## Steps

1. Start the object's clip on the frame it should appear.
2. Apply one of the Library pops with `preset.apply {name, id}`:
   - **`Pop - spring`**: playful, for icons, badges, stickers;
   - **`Pop - gentle`**: premium, for cards, photos, UI panels;
   - **`Stamp`**: lands from above size, for a price, a logo, one hero word;
   - **`Data point pop`**: quick, for chart markers.
3. Keep the **same pop** for the same kind of object across the film; mix at most two.
4. Stagger neighbours 3–6 f.

## Measured in Carvercat 0.1.6

Comp `K Pop in` in [cookbook lab 2](../labs/README.md#cookbook-lab-2carverproj): four 200 px squares,
clips at f10, one preset each; `carvercat_inspect curves` on what each preset wrote:

| Preset | Scale | Peak / dip | Settles | Opacity in |
|---|---|---|---|---|
| `Pop - spring` | 0 → 1 | 1.162 at +8 f (**16.2%** over) | +20 f | 5 f |
| `Pop - gentle` | 0.6 → 1 | 1.018 at +11 f (**4.4%** of the move) | +18 f | 7 f, eased |
| `Stamp` | 1.9 → 1 | 0.959 at +8 f (**4.6%** under) | +13 f | 3 f |
| `Data point pop` | 0 → 1 | 1.162 at +4 f (**16.2%** over) | +11 f | 3 f |

- All four are baked as many `linear` keys (9–12 per scale curve), so they can be retimed only by moving
  the keys or the clip.
- `inspect lint`: 0 errors, 0 warnings, 4 notes (`repeated_key_value` for the held opacity).

## Traps

- `preset.apply` takes one `id` at a time: [KI-113](../../ai/references/known-issues.md#ki-113).
- A preset on a text with Stagger Text: one staggered preset per property:
  [KI-050](../../ai/references/known-issues.md#ki-050).
- Popping from scale 0 makes strokes and shadows scale too ([scale vs size](../techniques/scale-vs-size.md)).

## In Carvercat

- Presets: `Pop - spring`, `Pop - gentle`, `Stamp`, `Drop - bounce` (Carvercat Essentials), `Data point pop`
  (Data Viz), `Jelly in`, `Pop - wobbly` (Cartoon Bounce), `Toast drop - spring` (SaaS UI).
- An exact curve of your own: two keys plus `key.handle` ([custom curves](../../ai/patterns/custom-curves.md)).
- Background: [exaggeration](../principles/exaggeration.md), [springs](../principles/springs.md),
  [easing reference](../principles/easing-reference.md).
