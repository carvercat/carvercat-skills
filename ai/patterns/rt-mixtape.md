# Mixtape tracklist

**Template** `rt_mixtape` (Library name "Mixtape tracklist") · Retro pack · **verified 0.1.8.1 (rev 1127)**, comp `RT Mixtape` in `categories/retro/rt-lab-3`.

**Measured on 0.1.8.1 (rev 1127, harness `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0, no flashes; against the v1 original the worst silhouette difference is 0.48 % (limit 2 %) and every object is present with the same text (box offset at most 1.9 px); colours are now the exact hex the page states (mean shift 12.6 of 255, intended). The frame numbers in the table above are the keys of the generator (`design units`), unchanged.


For briefs like "mixtape", "playlist reveal", "tracklist for the episode", "side A". A brown cassette (cream label with three stripes, SUMMER MIX '86, a tape window with two reels, four screws) slides in from the left on twos, and its reels keep turning; SIDE A, a rule and five numbered tracks with their times rise on twos. 150 f, overlay. Song names and times are invented stand-ins.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Cassette (all 17 parts, one move) | 0 | slides in 420 px from the left, expo, stepped every 2 f; opaque by f4 | lands **f10** (0%) |
| Reel hubs (6-point stars) | 0 | from f16 turn −6° a frame to the end, one way, not stepped | turning to f149 |
| Side "SIDE A" (ExtraBold 44 px, orange) | 12 | Rise - on twos as keys (43 px) | **f22** |
| Side rule (700 × 6 px) | 16 | grows from the left on twos, 14 f | **f26** |
| Track 1–5 (number red ExtraBold, name brown Bold 48 px, time teal Bold 44 px right-aligned) | 22, 28, 34, 40, 46 | Rise - on twos, 6 f apart | **f32** to **f56** |

Lint 0 errors, 0 warnings in the lab (32 notes, all `speed_jump` on the stepped slide and rises); placed 0/0/0. `inspect qc`: no flashes (it reports the hold from f52 as a freeze: at 240 px the turning hubs are a few pixels). Text-gap audit: closest pair 40 px (one track row to the next). Full-frame looks of the placed instance at f2 (cassette coming in over the left edge) and f149: nothing cut.

## Steps
1. Edit `TRACKS` in `retro_lab3.py` and rebuild, or the texts by hand; keep names under about 520 px at 48 px so they end before the times.
2. Five rows fill x 1060–1760; a sixth row needs the 86 px step and starts at f52.

## Pitfalls
- The track names and the brown parts are drawn for the cream ground; on the black of a fresh comp the names almost vanish. Keep a light ground under it or recolour them.
- Each cassette part has the same slide keys, so the cassette moves as one piece; turning it would need `group2()` (as the polaroid) because each part turns about its own centre.

Inspiration: 80s cassette mixtapes and hand-written J-cards. No external text or code was used.
