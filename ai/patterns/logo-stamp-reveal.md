# Logo: stamp reveal

**Template:** `Logo - stamp reveal` (mp_logo_stamp_reveal) · **verified 0.0.72** · 90 f · overlay

## Timing chart

```
Logo mark   4 Stamp (1.9 -> 1, 14 f, rebound at about f11) ...........
Wordmark       12 Letters cascade (char gap 2) ... last letter lands ~f48
Underline              20 Grow across X from its left edge (anchor [-1,0]) 18 f
SFX         impact at f6 (landing), soft ticks per letter (optional), riser into the next scene
```

## Steps

1. The mark: an ellipse here; replace it with your logo image or shape, then `preset.apply Stamp`.
2. The wordmark: tracking 1.15 and bold. `Letters cascade - spring`. **For more than 8 letters use gap 1** (`stagger.set {id: <text id>, gap: 1}`), or the reveal takes longer than a second.
3. The underline: a rectangle with height 0.004 W. Set `anchor [-1,0]` BEFORE positioning it (the anchor keeps the picture still), then apply `Grow across (X)`.
4. Hold: add a slow 2–3% scale drift on the whole group, or the mark, over the hold, so the end card is never frozen.

## Pitfalls

- Stamp starts at 190%. On a large logo that can leave the frame for 2 f; check with `inspect lint` (off frame), or lower the start to 1.5 in a copy of the preset.

## Variant: multi-piece logo pop
Leave every piece at its final position, rotation 0; key scale 0 → 1.12 → 1 (Ease out, then S-curve, ~12 f), staggered ~4 f. Pitch-step a pop SFX per piece (×1.12 each). Flying pieces in from random offsets reads messy.
