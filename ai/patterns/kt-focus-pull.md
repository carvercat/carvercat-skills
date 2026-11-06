# Focus pull, and the tracking breathe recipe

**Template** `kt_focus_pull` · Kinetic Typography pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `KT Focus pull`.

"Into focus" (150 px ExtraBold, centred). Each letter arrives out of focus and sharpens, 2 f after the previous one, while the letter spacing closes. Once landed, the spacing keeps opening very slowly, so the hold never freezes.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Per-letter focus | 0–18 per letter, gap 2 | Stagger Text (by character, gap 2) with three slots: a blur 24 → 0 on the card's `fill.blur` slot (stored value, about 28 px; Custom expo; a stagger tween does not take blur, so this is the manual build in [../references/effects/stagger.md](../references/effects/stagger.md)), relative opacity 0 → 1 (f0–9, the decelerating arrival curve cubic-bezier(0.333, 0.667, 0.667, 1)), relative position (no travel) | blur settles **f12**, opacity **f9** per letter |
| Tracking | 0–30, then 30–60 | 1.6 → 1.0, Custom expo; then 1.0 → 1.06, Linear (the breathe) | reaches 1.0 at f30; inspect reports the breathe as 11.1% "overshoot" because it measures past the f30 target |

Lint 0/0/0.

## Tracking breathe on any text (recipe)
For a hold of 1.5 s or more, key `text.font.tracking` from 1.0 at the end of the entrance to 1.04–1.08 at the end of the clip (stored values; in design units `letterSpacing`), linear. It reads as calm and expensive (luxury, minimal, editorial), and `inspect qc` stops reporting a freeze. Over MCP: `key.set {key:"text.font.tracking", value:1.0}` at the start of the hold, and `key.set {..., value:1.06, ease:"linear"}` at its end (the easing arrives at the key). Keep the breathe under 10%; above that, centred text visibly drifts sideways.
