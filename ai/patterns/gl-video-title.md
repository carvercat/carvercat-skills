# Corrupted video title

**Template** `gl_video_title` (Library name "Corrupted video title") · Glitch pack · **verified 0.1.8.1 (rev 1127 build; headless, isolated folders, pack added to a scratch user Library; `ai/scripts/motion/verify_pack.py`)**, comp `GL Video title` in `categories/glitch/gl-lab-3`.

For briefs like "title card for my new video", "episode opener", "creator title with a glitch". An EP. 07 kicker, a two-line ExtraBold 150 px title that jolts in with a red/cyan split under block artefacts, a red underline that steps across and a channel line. 120 f, left-aligned at x 160.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Kicker (green SemiBold 40, tracked) | 0 | opacity Hold steps 0 → 100 → 40 → 100% | steady **f5** |
| Title 1 / Title 2 | 4 / 10 | Hold jumps +44, −26, +14, 0 px; two hard drop shadows (red −, cyan +) jump 28 → 16 → 24 → 8 → 0 px | split settles **f16 / f22**; position lane reads **59.1%** "overshoot" (a jump lane, [KI-152](../references/known-issues.md#ki-152)) |
| Block 1–8 (red / cyan / green / white, 75%) | f4–14 | each its own 2 or 4 f clip over the title | gone by **f18** |
| Underline (red, 12 px, title-2 width) | 20 | width steps 15 → 45 → 70 → 100% from the left | **f26** |
| Meta (grey Medium 40) | 26 | opacity Hold steps | **f31** |
| Re-glitch in the hold | 70 / 74 | split 10 → 4 → 0 px and one −18 px jump | steady **f74 / f78** |

Lint 0 errors, 0 warnings (speed_jump info notes on the jumps); `inspect qc` (240 px): **no flashes**. Placed into a fresh comp: lint 0/0/0, qc no flashes. Text-gap audit: closest pair Title 1 / Title 2, 55.0 px.

## Steps
1. Change the copy in `glitch_lab3.py` (`video_title`); the underline is sized to line 2 with `cc.textw`.
2. Over a thumbnail or footage, keep a dark area behind the title: the white type and the 2 f blocks need contrast, not a busy frame.

Inspiration: creator title cards and broken-signal type. No external text or code was used.
