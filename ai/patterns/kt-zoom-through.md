# Zoom through letter

**Template** `kt_zoom_through` (Library name "Zoom through letter"; the bundled essentials already have an "Exit zoom through") · Kinetic Typography pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `KT Zoom through` in `categories/kinetic-typography/kt-lab-3`.

For briefs like "dive in", "look closer", "a type-led transition into the next idea". "LOOK" (ExtraBold 260 px) slams in and holds. Then the camera flies through the counter of its first O until the frame is all background, and "CLOSER" (220 px, accent) grows in inside it. 120 f.

Frames are comp frames.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Word ("LOOK") | 0 (ends f58) | scale 1.4 → 1, 10 f (expo), opacity in 3 f | settles **f7**; still f10–40 |
| The zoom | f40–58 | scale 1 → 34 and position so the O's centre travels in a straight line onto the frame centre (same accelerating curve on both) | the counter fills the frame by **f56**; 0% overshoot |
| Word 2 ("CLOSER") | 58 | scale 0.6 → 1, 18 f (expo), fade 4 f | opaque **f62**, settles **f70** |

Lint 0 errors, 0 warnings (2 notes: the held scale and the start of the zoom). Placed into a fresh comp: lint 0/0/0. Full-frame looks of the placed instance at f44, 50, 54, 56, 57 and 58 show the letter passing the frame edges as intended, then plain background ([KI-144](../references/known-issues.md#ki-144): lint does not check what moves inside an instance). Text-gap audit: the two words never share a rest frame.

## Steps
1. Another word: change `ZOOM_WORDS` in `ai/scripts/motion/kinetic_type_lab3.py` and rebuild. The O's centre comes from measured ink bounds ("LO" right edge minus half an "O"). A word without an O: zoom into another closed counter (A, B, D, P, R, 0, 8) and change the measured pair.
2. For a zoom factor z and target T (in pixels): end position = C − z·(T − C), with C the frame centre. Scale and position must share one easing, or T drifts off the line.
3. Pick z so the counter covers the frame corners, not only its width; check the last zoom frames with a full-frame look. For this O at 260 px, 34× leaves plain background from f56.

## Pitfalls
- The text is drawn at its own size and scaled by the transform, so a 34× text is not cropped first (unlike shapes larger than the comp, [KI-137](../references/known-issues.md#ki-137)).
- The first word's clip ends on the frame the second starts. A shared frame would put a 34× word over the new one.

Inspiration: the zoom-through-a-letter transition in kinetic typography. No external text or code was used.
