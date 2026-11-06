# Manifesto scroll

**Template** `kt_manifesto_scroll` (Library name "Manifesto scroll") · Kinetic Typography pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `KT Manifesto scroll` in `categories/kinetic-typography/kt-lab-3`.

For briefs like "brand manifesto", "mission statement", "our values": more copy than a quote, one line at a time. Four left-aligned lines (ExtraBold 84 px, x 260; the last in accent) arrive one after another at the same row (y 700). Each new line pushes the stack up one row (128 px) and the previous line steps back to 30% opacity. At f170 every line comes back to full for the final read. 240 f (8 s), holds.

Frames are comp frames.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Line 1–4 entrance | 10, 50, 90, 130 (40 f apart) | rise 60 px, 16 f (expo), fade 5 f | settles **10 f** after its start (Line 4 f140) |
| Stack push | f50, f90, f130 | every older line up 128 px, 16 f (expo) | 0% overshoot; still by **f140** |
| Previous line dims | 40 f after its start | opacity 1 → 0.3, 8 f | |
| Final read | f170 | opacity 0.3 → 1, 10 f | all full by **f179**; 60 f hold |

Lint 0 errors, 0 warnings (15 notes: held key values and the instant start of each expo push, both intended). Placed into a fresh comp: lint 0/0/0, and full-frame looks of the instance at f96 and f239 show nothing cut. Text-gap audit: no tight pairs (48.2 px between rows).

## Steps
1. Edit `MANIFESTO` in `ai/scripts/motion/kinetic_type_lab3.py` and rebuild; the pushes and dims are generated per line.
2. **Each line needs its reading time at full opacity before it dims.** Lint counts only fully opaque frames, and asks for max(25, characters × 30 / 17) of them: the 40 f step gives 35 opaque frames, enough for about 19 characters without spaces. Longer lines: raise `step`.
3. Five lines or more: lower `y0` so the first line stays inside the title-safe area after the last push (first line ends at y0 − (lines − 1) × 128).

## Pitfalls
- Dimming to 30% reads as about 50% grey on #0B0B0F; lower than that and the earlier lines stop being readable as context.
- The final read matters: without it the manifesto ends on one line, and the earlier ones were only on screen for their 35 f.

Inspiration: teleprompter-style manifesto films. No external text or code was used.
