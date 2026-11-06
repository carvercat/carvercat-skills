# Story progress bar (9:16)

**Template** `ss_progress_bar` · Social Short-form pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SS Progress bar`.

A 900 px track (8 px, muted, 35% opacity) and a white fill on the top safe line (y 290, x 90–990). The fill's trimEnd goes 0% → 100%, **linear**, over the comp's 150 f.

Measured: linear, 0.0067 per frame. Lint 0/0/0.

## Steps
Place it on the top track over the whole video. Inside the nested comp, set `comp.duration` to your video's length and move the fill's last key to the last frame. The showcase builds it at 285 f.
