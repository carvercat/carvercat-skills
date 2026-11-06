# Replay stinger

**Template** `sp_replay_stinger` · Sports pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SP Replay stinger` in `categories/sports/sp-lab-2`.

A transition into a replay: three diagonal stripes (red, blue, yellow; 1000 × 500 px drawn, scale X 2.6, turned −20° (stored value)) sweep across 3 f apart while "REPLAY" (white, outlined, 200 px) slams in. 45 f.

| Part | Clip | Motion | Measured |
|---|---|---|---|
| Replay stripe 1–3 | f0/3/6, 30 f each | in from −3072 px (expo, 12 f), drift 57.6 px for 6 f, out to +3072 px (accelerating) | clear by **f33** |
| Replay word | f10–42 | Impact slam; Zoom past (last 8 f) | |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place so the stripes cover the cut into the replay footage (about f12–20).

## Pitfalls
- Stripes much larger than the frame that held still were `cropped_at_rest`; they drift 3% while they wait.
- REPLAY needs 25 readable frames (6 characters): the clip is 32 f.

Inspiration: replay stingers in sports broadcasts. No external text or code was used.
