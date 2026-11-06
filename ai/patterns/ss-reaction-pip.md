# Reaction picture-in-picture (9:16)

**Template** `ss_reaction_pip` (Library name "Reaction picture-in-picture (9:16)") · Social Short-form pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SS Reaction` in `categories/social-media-reels/ss-lab-3`.

For briefs like "react to a clip", "duet / stitch layout", "face cam over the video". A clip panel stand-in (920 × 780 px, y 310–1090) with a REACTING TO tag and the original creator's handle, a round reaction cam (300 px, yellow ring) over its bottom-left corner, and a caption. 120 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Clip panel (stand-in) and its label | 0, 4 | Hook punch from 1.06 (as keys); fade | panel **f7**, label **f10** |
| Reaction cam (300 px, 8 px yellow stroke) and label | 10, 14 | pop 0 → 1, back curve, 12 f; fade | **9.8% overshoot**, **f21**; label **f20** |
| REACTING TO tag (pink pill sized to the text) and text | 12 | Whip in - left (as keys) | **f19** |
| Credit "@originalcreator" (Bold 36 px, outline, right-aligned at x 960) | 18 | fade 5 f | **f23** |
| Caption "wait for it..." (ExtraBold 64 px, outline, right edge x 830) | 30 | Hook punch | **f37** |

Lint 0/0/0. `bounds_inside` passed for every object; the cam (x 80–380, y 970–1270) and the caption stay left of x 851. Placed into a fresh 1080 × 1920 comp: lint 0/0/0. Text-gap audit: closest pair 144.6 px.

## Steps
1. Put the clip you react to over the panel and your face clip in the cam (mask it with a 300 px circle), then delete the labels.
2. Always credit the original creator; keep the handle on screen as long as their clip is.

## Pitfalls
- The panel stops at y 1090 so the original clip is not under the like/comment column; a full-height clip would be.
- The cam first sat apart from the panel (y 1250) and read as a second element, not a picture-in-picture; overlapping the corner by 120 px reads as one layout. The credit moved to the right so the cam does not cover it.

Inspiration: reaction, duet and stitch layouts on short-form apps. No external text or code was used.
