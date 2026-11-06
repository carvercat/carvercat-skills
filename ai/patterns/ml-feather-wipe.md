# Feather wipe reveal

**Template** `ml_feather_wipe` · Minimal Luxury pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `ML Feather wipe`.

"Quiet confidence" (Regular 96 px, ivory, centred) is revealed left to right through a mask whose edge is feathered.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Wipe window (1500 × 400 px mask, Fill Soft edge 160 px) | 0–45 | position from −1660 px (its width + the feather) to rest, the curve cubic-bezier(0.65, 0, 0.35, 1) | settles **f41** |

Masking: `property.set {id:"Headline", key:"mask", value:{"ref":"<Wipe window id>"}}`, then `parent.clear {ids:[Wipe window, Headline]}`. Lint 0/0/0.

## Steps
Place and apply, then edit the headline. For a slower, more elegant reveal, stretch the window's two keys to 60 f. For a wipe that reveals and then hides, add a third key moving the window on by its width + 160 px.
