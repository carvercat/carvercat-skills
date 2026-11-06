# Comic POW

**Template** `ct_comic_pow` (Library name "Comic POW") · Cartoon Bounce pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `CT Comic pow` in `categories/cartoon-bounce/ct-lab-3`.

For briefs like "a big hit", "BAM moment", "impact frame" in a comic or kids' film. Action lines shoot out, two jagged bursts slam in and POW! slams down into a squash and springs back. 75 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Action line 1–10 | 2 | shoot out (trim end f2–8, expo), then vanish (trim start f8–20, accelerating arrival cubic-bezier(0.333, 0, 0.667, 0.333)); clips end at f22 | |
| Burst back (red, 16 points) | 2 | pop 0 → 116 → 95 → 102 → 100%; rotation −8 → −14°, linear | scale settles **f17** |
| Burst (yellow, 13 points, ink outline) | 0 | pop 0 → 118 → 94 → 103 → 100%; rotation 0 → 6°, linear | scale settles **f15** |
| Pow "POW!" (ExtraBold 230 px, ink outline, −8°) | 3 | slams from 240% into 116 × 86% (f8), 94 × 106%, 102 × 98%, 100% (f20) | scale settles **f18**; x·y 0.996–1.0 |

Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: no pairs. Full-frame looks of the placed comp at f7 (the widest frame) and f74: nothing cut.

## Steps
1. Change the word (BAM!, ZAP!, BOOM!); at 230 px about five characters fit inside the 560 px burst at rest.
2. Hit it on a beat: the impact (the squash) is f8; shift the template so f8 lands on the hit.

## Pitfalls
- The slam is the overshoot: the text starts big and squashes when it "lands"; the squash keeps the volume, the 240% start does not need to.
- The bursts keep creeping round over the hold (linear, one way) so the hold is not frozen and nothing ping-pongs.

Inspiration: comic-book impact panels. No external text or code was used.
