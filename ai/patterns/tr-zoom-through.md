# Zoom-through transition

**Recipe** · **verified 0.0.72** (`RECIPES`, frames 48–94) · 12 f out + 20 f in

1. On the last clip of Scene A (or its comp instance): `preset.apply "Exit zoom through"`, which scales 1 → 2.4 and fades out over the last 12 f.
2. On the first clip of Scene B: `preset.apply "Zoom settle"`, which scales 1.22 → 1 with expo-out and fades in.
3. **Overlap B 3–4 f before A ends.** Back to back, as we first built it, there is an empty frame between them (seen at f68) that reads as a dip.

Knobs: for a hotter cut, raise Exit zoom through's end size in a copy of the preset (3–4×) and add a short whoosh plus an impact on B's first frame. A motion-blur effect on both (`effect.add {cap:"motionblur"}`) should sell the speed (not yet verified in this pattern).
