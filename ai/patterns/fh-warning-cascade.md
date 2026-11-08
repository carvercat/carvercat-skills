# Warning cascade

**Template** `fh_warning_cascade` (Library name "Warning cascade") · Futuristic HUD pack · **verified 0.1.8.1 (rev 1127 build; headless, isolated folders, pack added to a scratch user Library; `ai/scripts/motion/verify_pack.py`)**, comp `FH Warning cascade` in `categories/futuristic-hud/fh-lab-3`.

For briefs like "hacked", "cyber attack", "system overload", "malfunction", "game over". Four warning windows scan open in a cascade, the last one CRITICAL in red, then a red SYSTEM OVERRIDE REQUIRED banner scans open. 120 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Window 1–4 (780 × 216 px, stroked) + bar | 4, 13, 22, 31 | scan open, 8 f; each window is 150 px right and down from the last, so it covers only the empty lower part of the one behind | window 1 settles **f9**, window 4 **f36** |
| Window head / code (dark 30 px on the bar) | window + 6 | Flicker on | |
| Window text (46 px) | window + 8 | types on, 1 f a character | |
| Critical band + edge 1–2 | 56 | scan open, 10 f | settles **f63** |
| Critical text "SYSTEM OVERRIDE REQUIRED" (red #FF6B5E, 56 px) | 62 | Hold: on at f64, one dip to 40% f90–98 | on **f64** |

Lint (with `contrast:true`) 0 errors, 0 warnings, 0 notes; dark text on the amber and red bars passes too. `inspect qc` (240 px): no flashes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 78 pairs, closest 41.6 px (Window 3 text / Window 4 head). Full-frame look of the placed comp at f119: nothing cut.

## Steps
1. Edit `items` in `warnings()`; keep each body line under about 18 characters at 46 px.
2. For a calmer single warning, use the round-2 [Alert banner](fh-alert-banner.md).

## Pitfalls
- Stack windows so the one in front covers only empty panel: lint compares text boxes, so a covered line still reads as `text_overlap`, and a reader cannot read it either.
- Header words at 26 px with tracking 1.5 ran together ("WARNING 01 ERR 0x3A"); 30 px with tracking 1.1–1.2 reads.
- Red text on a red plate fails contrast (white on #FF6B5E is about 3:1); the banner uses red text on a dark plate (#2A0806).

Inspiration: common sci-fi HUD and interface conventions. No external text or code was used.
