# Vertical (9:16) versions and social safe areas

Agent-neutral. Tool: `../scripts/motion/reformat.py` (+ `reformat_example.json`).

## Safe area for 1080 x 1920 (Reels / TikTok / Shorts)
Measured from the top-left, in pixels:
- Keep everything inside **x 61-1016, y 268-1538**.
- **Below y 1151, keep x > 851 clear** - the like/comment/share column sits there.
- Captions and headlines start **>= 130 px from the left** and stay <= ~790 px wide.
- The top ~14 % (profile/title UI) and bottom ~20-35 % (caption, music, CTA bar) are
  covered on most apps; never put key text there.
- Logo tiles and badges must stay inside the frame at every keyframe, not only at rest.

## Layout that worked (Carvercat intro)
| Scene type | 9:16 layout |
|---|---|
| App window + headline | window in the upper area at <= 0.88 scale (x 77-1003, ~300-900 px from top); captions stacked below it from x 130 |
| Centred logo / download card | centred, scaled ~1.6, lifted so the button row sits above y 1151 |
| End card (text + logo) | logo on top, text underneath (not logo bottom-right, which is under the buttons) |
| Corner brand mark | inside the top margin (~300 px from top) |
| Full-frame wipes / backgrounds | cover the whole 9:16 frame |

## How to convert
1. In the app: create **Horizontal** and **Vertical** bins (`bin.new`,
   `comp.move_to_bin`). `comp.duplicate {comp:index}` each comp (copies land in the
   source bin; move them). `edit.save`.
2. **Don't just run `comp.format`.** It changes only the frame: positions are normalised
   per axis, shape/text sizes are fractions of frame width, and path points are
   normalised per axis around 0.5 - so content shrinks to 56 % and paths stretch ~3.2x
   vertically.
3. Write a layout spec (old-pixel anchor -> new-pixel anchor, scale per region) and run
   `reformat.py project.carverproj spec.json`. It maps positions, sizes, text boxes,
   path points **and multi-part `contours[]`**, keeps full-width rects full-frame, sets
   the frame size, re-points the vertical assembly's nested comps, and gives the copies
   **unique clip ids** (shared ids made the editor ~6x slower - see
   [performance.md](../app/performance.md)).
4. Reopen (`edit.open {force:true}`) and look at every comp at entrance, hold and exit.
   Fix by hand:
   - shapes that become full-frame on a keyframe (e.g. a plate stretching to fill)
   - iris/circle reveals: scale up ~2.4x to cover the tall frame
   - hand-off points between scenes (collapse dot -> burst) must line up
   - anything that moves outside the frame or into the button column mid-animation
5. Check text sizes on a phone-sized preview: in-feed body >= 32 px, headline >= 90 px.
