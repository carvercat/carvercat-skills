# Swipe up (9:16)

**Template** `ss_swipe_up` · Social Short-form pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SS Swipe up` in `categories/social-media-reels/ss-lab-2`.

A transition: a pink full-frame panel whips up from below, covers the frame and leaves through the top, with motion blur (shutter 360). 24 f.

| Part | Clip | Motion | Measured |
|---|---|---|---|
| Swipe panel (1000 px drawn, scale 1.08 × 1.92) | f0–23 | y offset +1920 px → 0, f0–10 (Custom whip cubic-bezier(0.7, 0, 0.1, 1)); hold to f14; 0 → −1920 px, f14–24 (accelerating) | covers **f10–14** |

Lint 0 errors, 0 warnings. Placed into a fresh 1080 × 1920 comp: applied at 1080 × 1920, lint 0/0/0.

## Steps
1. Place 12 f before your cut, above both scenes; cut at its f12. Add a whoosh 3 f before.

## Pitfalls
- Shapes are cropped to the comp size before scaling ([KI-137](../references/known-issues.md#ki-137)): the panel is drawn 1000 px and scaled to 1080 × 1920.
- With motion blur the leading edge is soft, so the cover holds only from f10 to f14. Do not move the cut outside that window.

Inspiration: vertical swipe transitions in short-form edits. No external text or code was used.
