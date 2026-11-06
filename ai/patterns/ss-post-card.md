# Post card (9:16)

**Template** `ss_post_card` · Social Short-form pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SS Post card` in `categories/social-media-reels/ss-lab-2`.

An 860 × 520 px white post (radius 36): avatar, name and handle, a three-line post (Bold 52 px, line spacing 1.15) and a likes count. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Post | 0 | Hook punch | settles **f7** |
| Post avatar, name, handle | 4, 6, 8 | Hook punch | |
| Post text | 14 | Caption words pop (3 f per word) | first word settles **f22** |
| Post stats | 50 | Hook punch | |

Lint 0 errors, 0 warnings. `bounds_inside` the safe box [61, 268, 955, 1270] passed for every object. Placed into a fresh 1080 × 1920 comp (`comp.format`): applied at 1080 × 1920, lint 0/0/0.

## Steps
1. Place and apply. Edit the name, handle and post (newlines for the line breaks). The tested lines are up to 22 characters.

## Pitfalls
- **Fixed 2026-10-28 (overlap audit).** The handle sat 10.7 px under the name (geometry at rest); it moved down 8 px: an 18.7 px gap ([KI-138](../references/known-issues.md#ki-138)).

Inspiration: screenshot-style post cards in commentary videos. No external text or code was used.
