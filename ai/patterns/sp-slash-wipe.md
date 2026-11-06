# Slash wipe

**Template** `sp_slash_wipe` · Sports pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SP Slash wipe` in `categories/sports/sp-lab-2`.

A transition: blue, red and navy slashes (1000 px drawn, scale 2.2 × 2.4, turned −25° (stored value)) whip across the frame 2 f apart; the last, navy one covers the frame. 30 f.

| Part | Clip | Motion | Measured |
|---|---|---|---|
| Slash 1–3 | f0/2/4, 26 f each | from −2880 px, 10 f, Custom whip cubic-bezier(0.7, 0, 0.1, 1); drift 57.6 px for 4 f; out to +2880 px (accelerating) | frame covered about **f12–18** (look) |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place 15 f before your cut, above both scenes; cut at its f15.

## Pitfalls
- A slash 1200 px wide turned 25° does not span the 1920 px frame; 2200 px does.
- Oversized shapes waiting still trip `cropped_at_rest`; they keep drifting while they cover.

Inspiration: diagonal team-colour wipes in sports edits. No external text or code was used.
