# Hacker alert

**Template** `gl_hack_alert` (Library name "Hacker alert") · Glitch pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `GL Hack alert` in `categories/glitch/gl-lab-3`.

For briefs like "you've been hacked", "intrusion detected", "security breach scene". A 1200 × 540 dark panel with a red edge, a red warning sign, INTRUSION DETECTED (white ExtraBold 96) with a red/cyan split, a green detail line and a red trace bar that fills in eight steps. 150 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Alert panel (red 6 px edge) | 0 | switches on like a tube (height 2 → 40 → 104 → 100%, Hold) | **f6** (4.1%) |
| Warning sign (path) / "!" | 6 | opacity Hold steps | |
| Alert title | 8 | jumps +30, −18, +8, 0 px; split 24 → 12 → 20 → 6 → 0 px; one re-glitch f90–92 | split **f20**; steady **f92** |
| Alert detail (green SemiBold 40) / Trace label | 16 / 24 | opacity Hold steps | **f21 / f29** |
| Trace fill (red, inside an 800 px grey track) | 24 | width 6 → 21 → 35 → 52 → 66 → 81 → 93 → 100%, a step every 14 f | full at **f122** |
| Noise block 1–6 (50%) | f8–64 | 2 or 4 f clips inside the panel | |
| Scan line 1–2 (4 px, 5%) | 10 | drift 250 px down, one way | |

Lint 0 errors, 0 warnings; `inspect qc` (240 px): **no flashes**. Placed into a fresh comp: lint 0/0/0, qc no flashes. Text-gap audit: closest pair title / detail, 38.6 px. The red panel edge, sign and bar never blink: saturated red flicker is the riskiest kind ([photosensitivity](../../wiki/accessibility/photosensitivity.md)).

Inspiration: film and game "access denied" screens. No external text or code was used.
