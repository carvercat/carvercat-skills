# Highlight sweep (marker reveal)

**Recipe** · **verified 0.0.72** (`RECIPES`, frames 150–200)

An accent bar draws across from its left edge, revealing text that is the same colour as the background. You only see the text where the marker is.

1. Text: bold, coloured exactly like the background, on the track ABOVE the bar. Give it `Words rise - expo` from 6 f before the bar.
2. Bar: rectangle 0.3 W × 0.06 W, accent colour. **`anchor [-1,0]` first**, then `authoring.place_bounds` it over the text (pass a `frame` inside the clip). Then `Grow across (X)` (18 f, expo).
3. The reveal reads complete at about +12 f; hold at least 1 s.

Variants:
- **Marker behind one word**: white text, with the bar sized to that word's bounds (`carvercat_authoring mode:geometry` gives the bounds) and on the track BELOW the text.
- **Strike-through**: bar height 0.004 W through the middle of the word.
- **Wipe-off exit** (not yet verified): key scaleX back to 0 at the end. To leave to the right instead of collapsing left, use a second bar anchored at `[1,0]` that takes over at the hold, rather than changing the anchor mid-animation.
