# Signal lost end card

**Template** `gl_signal_end` (Library name "Signal lost end card") · Glitch pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `GL End card` in `categories/glitch/gl-lab-3`.

For briefs like "end screen with subscribe", "outro for a tech channel", "stay tuned card". A green "// SIGNAL LOST — STAY TUNED" kicker, two 760 × 428 video slots (where the platform's end-screen videos go) with labels, the channel handle with a red/cyan split and a red SUBSCRIBE plate; a faint tracking band rolls down once. 150 f, holds (end screens need 5–20 s; extend the clips).

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Kicker | 0 | opacity Hold steps | **f5** |
| Slot 1 / Slot 2 | 4 / 10 | switch on like tubes (height 2 → 40 → 104 → 100%); one 14 px jump each at f60 / f100 for 2 f | **f10 / f16** (4.1%) |
| Slot label 1 / 2 (SemiBold 36) | 12 / 18 | opacity Hold steps | |
| Handle (ExtraBold 72) | 24 | jumps +24, −12, 0 px; split 18 → 10 → 14 → 0 px; re-glitch f110–112 | split **f33**; position **f30** |
| Subscribe plate / text | 30 / 34 | plate switches on; text steps in | **f36 / f39** |
| Tracking band (120 px, soft 40, 2%) | 0 | rolls from top to bottom once, linear | |

Lint 0 errors, 0 warnings; `inspect qc` (240 px): **no flashes**. Placed into a fresh comp: lint 0/0/0, qc no flashes. Text-gap audit: closest pair label 1 / handle, 106.6 px.

## Pitfalls
- A tracking band at 6% opacity read as a grey bar over the slots: opacity is in linear light, so 6% white on near-black shows as about 27% grey. 2% reads as a faint roll.

Inspiration: video end screens and lost-signal cards. No external text or code was used.
