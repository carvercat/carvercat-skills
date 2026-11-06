# Comment reply (9:16)

**Template** `ss_comment_reply` (Library name "Comment reply (9:16)") · Social Short-form pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SS Comment reply` in `categories/social-media-reels/ss-lab-3`.

For briefs like "answer a viewer's question", "reply to a comment with a video", "FAQ from the comments". A white reply sticker (780 × 220 px) with an avatar, "Reply to @name's comment" and the comment, a small tail, and a low caption that starts the answer. 120 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Reply card (transformOrigin "0% 100%", its bottom-left corner) | 0 | pop 0.8 → 1, back curve, 10 f | **9.7% overshoot**, settles **f10** |
| Reply tail (40 px square turned 45°) | 4 | fade 4 f | **f8** |
| Avatar (60 px, pink) | 4 | pop 0.4 → 1 | **f14** |
| "Reply to @jordan.k's comment" (Medium 32 px, grey) | 6 | fade 5 f | **f11** |
| Comment (Bold 48 px, black) | 10 | 20 px rise, expo, fade 4 f | **f17** |
| Answer caption "Here's how" (ExtraBold 72 px, outline, x 490, y 1250) | 36 | Hook punch (as keys) | **f43** |

Lint 0/0/0. `bounds_inside` passed for every object. Placed into a fresh 1080 × 1920 comp: lint 0/0/0. Text-gap audit: closest pair 16.0 px (reply-to line / avatar), above the 12 px flag.

## Steps
1. Place and apply; edit the handle, the comment and the caption. A comment up to about 26 characters fits one line at 48 px.
2. Cut to the answer clip under it; keep the sticker for the first 2–3 s, then trim the instance.

## Pitfalls
- The first build popped the card from 0.5 and lint gave a `speed_jump` note (11.6 → 1.9 px/frame at f5–6): a 780 px card scaled from a corner moves its far edge fast. From 0.8 the note is gone and the pop still reads.

Inspiration: reply-to-comment stickers in short-form apps. No external text or code was used.
