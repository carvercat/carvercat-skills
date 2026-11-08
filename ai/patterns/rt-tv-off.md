# TV switch-off

**Template** `rt_tv_off` (Library name "TV switch-off") · Retro pack · **verified 0.1.8.1 (rev 1127)**, comp `RT TV off` in `categories/retro/rt-lab-2`.

**Measured on 0.1.8.1 (rev 1127, harness `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0, no flashes; against the v1 original the worst silhouette difference is 0.00 % (limit 2 %) and every object is present with the same text (box offset at most 0.0 px); colours are now the exact hex the page states (mean shift 2.0 of 255, intended); windows over a magenta/green underlay: covered f0-23 (cut f0). The frame numbers in the table above are the keys of the generator (`design units`), unchanged.


The CRT switch-off as an ending: a bright picture collapses to a horizontal line, then to a dot, then the set is dark. 24 f.

| Part | Motion | Measured |
|---|---|---|
| TV black (frame-size) | still | |
| TV screen (1000 px drawn, scale 1.92 × 1.08) | scale Y → 0.6% on twos (f0–8, accelerating), then scale X → 1% (f8–16); opacity off at f20 (Hold) | line by **f8**, dot by **f16**, dark at **f20** |

Lint 0 errors, 0 warnings; `inspect qc` (240 px) found no flashes. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Put the instance after the last shot and cut to it at f0. For the picture to collapse instead of a white panel, nest your last shot and give it the same scale keys.

Inspiration: the CRT power-off. No external text or code was used.
