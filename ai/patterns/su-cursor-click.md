# Cursor click

**Template** `su_cursor_click` · SaaS UI pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SU Cursor click` in `categories/saas-launch/saas-ui-lab`.

A white pointer glides in from the lower right, presses, and a ring opens under its tip. Use it for "click here" moments in product demos.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Cursor (path, 2.4× a 26×40 px arrow, white with a 2.5 px ink stroke, soft shadow) | 0–22 | position +300, +220 px (stored values) → target, Custom S curve cubic-bezier(0.65, 0, 0.35, 1); opacity 0 → 1 over 0–5 | position settles **f20**, opacity f5 |
| Press | 26–36 | scale 1 → 0.85 (f26–29, decelerating arrival cubic-bezier(0.333, 0.667, 0.667, 1)) → 1 (f36, back curve), pivot at the tip (transformOrigin "0% 0%", anchor [−1, 1]) | settles **f36** |
| Ripple (120 px ring, 5 px accent stroke) | 28–46 | the **Tap ripple** preset | size settles **f39**, gone by **f44** |

## Steps
1. `library.place {name:"Cursor click", frame}` then `template.apply {id}`.
2. The tip sits at the comp centre. Move the INSTANCE so that the centre lands on your button, and press at instance f26 (ripple at f28).
3. To start your own UI reaction on the click, key it at instance start + 28. The showcase does this: the toggle knob starts on the ripple frame.
4. Change the travel: `comp.switch` into the nested comp, then edit the cursor's two position keys. Keep the Custom S curve cubic-bezier(0.65, 0, 0.35, 1) on the first key (it shapes the segment arriving at the target).

## Pitfalls
- The press only reads if the scale pivots at the tip. If you redraw the arrow, set its transformOrigin to the tip again.
- The cursor has no exit. Cut it, or give the instance Exit fade - fast (Motion Patterns).
- Lint notes `repeated_key_value` on the ripple's opacity (0.7 held for two keys). This comes from the baked preset and is harmless.
