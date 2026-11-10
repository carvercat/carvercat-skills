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
2. **Don't just run `comp.format`.** It changes only the frame: the stored positions are normalised
   per axis, stored shape and text sizes are fractions of frame width, and stored path points are
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

## Authoring and checking 9:16 natively (measured on 0.1.6,)
- Direct JSON: `json_author/cc.py` with `cc.W, cc.H = 1080, 1920` and `cc.EM = 1146.24 * 1080 / 1920`. Write the scene's `width`/`height` as 1080/1920 (see `VComp` in `../../scripts/motion/social_short_form_lab.py`). Text size follows comp width: 100 px Bold caps are 71 px tall in both orientations.
- A new comp is 16:9. Run `comp.format {width:1080, height:1920}` before placing 9:16 templates; `template.apply` then reports "applied at 1080 x 1920".
- Check the safe area per object with `measure.overlaps {within: "safe"}` (the box [61,268,955,1270] in px). For text below y 1151, also keep the right edge under x 851.
- Ready-made 9:16 pieces: the Social Short-form pack ([../../patterns/social-short-form.md](../../patterns/social-short-form.md)).

## Converting a finished 16:9 film (measured 0.1.6)
`comp.format` changes the canvas, not the design: objects keep their size and are re-centred, so 16:9 layouts are cut at the sides. 16:9 templates placed into a 9:16 comp are fitted into a 1080 × 608 band and need an instance zoom plus a slow push. What carries over and what needs a manual re-cut: [../../recipes/vertical-recuts.md](../../recipes/vertical-recuts.md).
