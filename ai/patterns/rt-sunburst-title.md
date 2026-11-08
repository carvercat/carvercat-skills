# Sunburst title

**Template** `rt_sunburst_title` · Retro pack · **verified 0.1.8.1 (rev 1127)**, comp `RT Sunburst title` in `categories/retro/rt-lab`.

**Measured on 0.1.8.1 (rev 1127, harness `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0, no flashes; against the v1 original the worst silhouette difference is 0.00 % (limit 2 %) and every object is present with the same text (box offset at most 0.1 px); colours are now the exact hex the page states (mean shift 4.5 of 255, intended); windows over a magenta/green underlay: covered f0-89 (cut f0). The frame numbers in the table above are the keys of the generator (`design units`), unchanged.


A 2600 px, 24-ray mustard sunburst (star, inner radius 0.12) behind "SINCE 1975" (ExtraBold 160 px, brown, hard orange drop shadow 10 px down-right, softness 0) and "FAMILY RECIPES" (SemiBold 44 px, tracked).

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Rays | 0–8, then 0–90 | opacity 0 → 0.55 on twos; rotation 0 → 15°, linear | opaque **f8** |
| Title | from 6 | **Pop - on twos** | 3.9% overshoot, settles **f18** |
| Subtitle | from 14 | **Rise - on twos** | settles **f24** |

Lint 0/0. Swap the words; keep the sunburst centred on the title.
