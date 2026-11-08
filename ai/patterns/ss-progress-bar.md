# Story progress bar (9:16)

**Template** `ss_progress_bar` · Social Short-form pack · **verified 0.1.8.1 (rev 1127)**, comp `SS Progress bar`.

**Measured on 0.1.8.1 (rev 1127, harness `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0, no flashes; against the v1 original the worst silhouette difference is 0.00 % (limit 2 %) and every object is present with the same text (box offset at most 0.0 px); colours are now the exact hex the page states (mean shift 2.1 of 255, intended). The frame numbers in the table above are the keys of the generator (`design units`), unchanged.


A 900 px track (8 px, muted, 35% opacity) and a white fill on the top safe line (y 290, x 90–990). The fill's trimEnd goes 0% → 100%, **linear**, over the comp's 150 f.

Measured: linear, 0.0067 per frame. Lint 0/0/0.

## Steps
Place it on the top track over the whole video. Inside the nested comp, set `comp.duration` to your video's length and move the fill's last key to the last frame. The showcase builds it at 285 f.
