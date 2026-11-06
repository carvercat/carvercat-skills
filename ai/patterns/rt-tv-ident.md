# 70s TV ident

**Template** `rt_tv_ident` (Library name "70s TV ident") · Retro pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `RT TV ident` in `categories/retro/rt-lab-3`.

For briefs like "70s channel ident", "station logo bumper", "now in colour". Four concentric rings in red, orange, mustard and teal draw on twos from 12 o'clock, a cream 7 pops in the middle, CHANNEL SEVEN and NOW IN COLOUR rise, and a small dot keeps circling the rings. 150 f, holds. Full-frame brown ground included. The channel is invented.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Ring 1–4 (620 / 520 / 420 / 320 px, 34 px butt-capped strokes, turned +90°) | 0, 4, 8, 12 | Trim end 0 → 1 on an expo curve, on twos, 16 f | **f10** to **f22** |
| Number "7" (ExtraBold 230 px) | 24 | Pop - on twos as keys | **3.9%**, **f36** |
| Channel (ExtraBold 72 px, tracking 1.4) | 34 | Rise - on twos | **f44** |
| Tagline (Bold 40 px, mustard) | 42 | the same | **f52** |
| Orbit dot (26 px) | 30 | circles at 350 px, 3° a frame one way (a turn every 120 f), sampled on twos | moving to f150 |

Lint 0 errors, 0 warnings in the lab (3 notes, `speed_jump` on the stepped rises); placed 0/0/0. `inspect qc`: no flashes. Text-gap audit: closest pair 51.6 px (channel and tagline). Full-frame looks of the placed instance at f12 and f100: nothing cut.

## Steps
1. Replace the 7 with the channel's number or initial; a wide mark needs the inner ring (320 px) or smaller type.
2. For a loop, keep the orbit dot: a turn every 120 f; cut the ident at f150 or extend it to f270.

## Pitfalls
- Round caps on a drawing ring overshoot the start point; use `cap='butt'` for rings that close.
- Over 120 f the orbit dot has 61 Hold keys: retime it in the script, not by hand.

Inspiration: 1970s broadcast idents and their rainbow-ring marks. No external text or code was used.
