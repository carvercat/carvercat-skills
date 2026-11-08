# Film countdown leader

**Template** `rt_film_leader` (Library name "Film countdown leader") · Retro pack · **verified 0.1.8.1 (rev 1127)**, comp `RT Film leader` in `categories/retro/rt-lab-3`.

**Measured on 0.1.8.1 (rev 1127, harness `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0, no flashes; against the v1 original the worst silhouette difference is 0.00 % (limit 2 %) and every object is present with the same text (box offset at most 0.0 px); colours are now the exact hex the page states (mean shift 9.7 of 255, intended); windows over a magenta/green underlay: covered f0-119 (cut f0). The frame numbers in the table above are the keys of the generator (`design units`), unchanged.


For briefs like "old film countdown", "projector leader 5-4-3-2", "vintage intro". A warm grey frame with a crosshair, a white outer ring and a thin dark inner ring; on every 30 f beat a dark slice sweeps clockwise from 12 o'clock behind a big number (5, 4, 3, 2). Hard cuts on the beat. 120 f. Full-frame ground included.

| Part (per 30 f beat) | Motion | Measured |
|---|---|---|
| Sweep 1–4 (ellipse 330 px with a butt-capped 330 px stroke: a pie of radius 330 px; turned +90°) | Trim **start** 1 → 0, linear, over the beat | a full turn in **30 f**, clockwise |
| Number 1–4 (ExtraBold 420 px, near black) | a hard cut on the beat | 30 f each |
| Rings and crosshair | static | |

Lint 0 errors, 0 warnings, 0 notes in the lab; placed 0/0/0. `inspect qc`: no flashes (the full dark slice returns to grey once a second). Text-gap audit: the numbers never share a frame. Full-frame look of the placed instance at f20: nothing cut.

## Steps
1. More beats: add numbers to `nums` in `retro_lab3.py` (8 to 2 is 210 f); each needs 25 opaque frames for lint's reading time.
2. Add a short beep on the "2" with the audio tools, then cut to the picture.

## Pitfalls
- An ellipse's stroke starts at 3 o'clock and runs counter-clockwise. Keying Trim `end` 0 → 1 with the shape turned +90° swept counter-clockwise (first build, checked with looks); keying `start` 1 → 0 grows the slice backwards from the end: clockwise from 12 o'clock.
- No grain or flicker: the old leaders flickered, but full-frame flicker is a flash risk.

Inspiration: academy and SMPTE-style countdown leaders on film prints. No external text or code was used.
