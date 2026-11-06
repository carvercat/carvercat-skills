# Brand systems in motion, in Carvercat

A brand's motion system is a short list of decisions that every shot obeys. Write it down before building, then build presets and templates from it, so 40 shots by different hands still feel like one film.

## The decisions

1. **Easing family: pick one.**
   - Corporate, editorial, luxury: standard or decelerate curves, no overshoot (Corporate Brand: Soft rise, Card settle).
   - Product and SaaS: expo landings with small springs (about 4–5%) only on things that drop in (SaaS UI).
   - Playful, funky, kids: springs at about 16% and bounces (Kinetic Typography's Letters pop, Words drop - bounce).
   Never mix families in one piece. Overshoot on a calm brand reads as a mistake.
2. **Duration scale.** Three sizes, for example 14 / 20 / 24 f entrances with exits at about 70% of the matching entrance. Hero moves take the long one.
3. **Direction.** Things arrive from one side and leave toward the other, or rise in and leave up. Keep one direction convention per film.
4. **Colour roles:** ground, ink, muted, one accent, support ([colour.md](colour.md)).
5. **Type:** one family, two weights for most work (a display weight and a text weight), and a fixed size scale. For type sizes and reading times see [typography.md](typography.md).
6. **Logo rules:**
   - clear space at least the mark's height;
   - never stretch, recolour outside the palette or animate the logo's internal shapes unless the brand allows it;
   - the resolve holds at least 2 s.
7. **Signature move:** one recognisable motion, used at the open and close and nowhere else (the Corporate pack's frame-drawn logo resolve, the Kinetic pack's split-rule reveal).

## In Carvercat

- **Encode the easing family once.** Bake it into presets (\`.carverpreset\`, curves as keys) or a cubic-bezier \`ease\` on keys (stored as \`customEase\` on the arriving key). Then every object gets the same motion by name: \`preset.apply {name:"Soft rise"}\`.
- **Encode layouts as templates.** A \`.carvertemplate\` holds the brand's lower third, title card and end card with their colours, fonts and timing. Placing one creates a nested comp; edit the text inside it, and keep the motion.
- **Make one pack per brand.** A folder in \`library/templates/<brand>/\` with a \`pack.carverpack\`, the brand's presets and its templates, prefixed ids (\`cb_\`, \`su_\`) so two brands never share clip ids. Install it like Motion Patterns. An installed public build loads packs only from its own bundle today ([FR-036](../known-issues.md#fr-036)).
- **Check consistency with numbers.** \`carvercat_inspect mode:curves\` on a few objects per comp: the overshoot and settle frames should match the brand's table. \`mode:timing\` shows whether exits are shorter than entrances.

## Brand sheet template (fill in per client)

| Decision | Value |
|---|---|
| Easing family | e.g. decelerate, Custom (0.05, 0.7, 0.1, 1), no overshoot |
| Entrance / exit | 24 / 16 f (hero 30 f) |
| Direction | rise in, leave up |
| Ground / ink / muted / accent / support | hex values |
| Fonts and weights | family, display weight, text weight |
| Logo | clear space, minimum size, resolve length |
| Signature move | name of the preset or template |
