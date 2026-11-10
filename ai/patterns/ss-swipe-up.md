# Swipe up (9:16)

**Template** `ss_swipe_up` · Social Short-form pack · **verified 0.1.8.1 (rev 1127)**, comp `SS Swipe up` in `categories/social-media-reels/ss-lab-2`.

**Measured on 0.1.8.1 (rev 1127, harness `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0, no flashes; against the v1 original the worst silhouette difference is 3.01 % (limit 2 %) and every object is present with the same text (box offset at most 0.0 px); colours are now the exact hex the page states (mean shift 9.9 of 255, intended). The frame numbers in the table above are the keys of the generator (`design units`), unchanged.


**Re-checked with the new effects on Carvercat 0.1.10, 2026-11-10 (`verify_pack.py`):** lint 0/0/0 in 16:9 and 9:16, objects pass. The v1 comparison reads DIFF with a worst silhouette difference of 2.31 % (limit 2 %; 3.01 % before the streak): the soft streak edge is the intended difference, not a missing shape.

A transition: a pink full-frame panel whips up from below, covers the frame and leaves through the top, with motion blur (shutter 360) and a vertical `directionalBlur` (240 px at 90deg falling to 0 while the panel covers, rising again as it leaves; [directional blur](../references/effects/directional-blur.md)). 24 f.

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
