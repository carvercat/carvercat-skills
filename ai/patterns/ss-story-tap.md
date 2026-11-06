# Story tap-through (9:16)

**Template** `ss_story_tap` (Library name "Story tap-through (9:16)") · Social Short-form pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SS Story tap` in `categories/social-media-reels/ss-lab-3`.

For briefs like "make it feel like a story", "a 4-part story with tap-through", "day 1 to day 4". Four segment bars across the top (8 px, x 90–990, y 290) fill one after another; a tap ring and dot on the right half mark each page change. 160 f (4 pages × 40 f). It is an overlay: put each page's clip under it, cut on f40 / f80 / f120.

Frames are comp frames.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Segment tracks 1–4 (muted, 35%) | 0 | none | |
| Segment 1–4 (white, 8 px) | 0 | trimEnd 0% → 100%, linear, one page each | full at **f39 / f79 / f119 / f159** |
| Tap dot 1–3 (70 px, 55% → 0) and tap ring 1–3 (120 px, 6 px stroke) | 36, 76, 116 (14 f clips) | ring scale 0.6 → 1.5 (expo), fades out | ring 1 scale **f45**, gone **f49**; ring 3 **f125 / f129** |
| Tap hint "Tap for the next one" (ExtraBold 52 px, outline) | 6 | Hook punch (as keys) | settles **f13**; cuts out with page 1 at f40 (32 opaque frames) |

**0% overshoot** on every curve. Lint 0 errors, 0 warnings, 0 notes. `bounds_inside` the safe box [61, 268, 955, 1270] passed for every object, and nothing reaches right of x 851 below y 1151. Placed into a fresh 1080 × 1920 comp: applied at 1080 × 1920, lint 0/0/0. Text-gap audit: one text, no pairs. A full-frame look of the placed instance (f0–159) shows the bars and taps uncut.

## Steps
1. Place and apply over your clips. For more pages change `ST_SEG` (and `ST_PER` for page length) in `ai/scripts/motion/social_short_form_lab3.py` and rebuild; the bar width is shared out automatically.
2. Cut the clips on the page frames (multiples of 40).

## Pitfalls
- A fade-out on the hint (opacity held at 1, then keyed to 0) gave a `repeated_key_value` note; the hint now ends with its clip at the first tap, which is also how a story page behaves (a hard cut).
- Keep the bars at y 290 or lower: the top 14% belongs to the platform's profile row.

Inspiration: segmented story bars and tap-to-advance in vertical story formats. No external text or code was used.
