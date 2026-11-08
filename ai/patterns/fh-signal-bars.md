# Signal bars

**Template** `fh_signal_bars` · Futuristic HUD pack · **verified 0.1.8.1 (rev 1127 build; headless, isolated folders, pack added to a scratch user Library; `ai/scripts/motion/verify_pack.py`)**, comp `FH Signal bars` in `categories/futuristic-hud/fh-lab-2`.

Sixteen 28 px bars on a baseline (y 700, up to 300 px tall), cyan with every fifth amber, under a "SIGNAL ANALYSIS" label. Each bar takes a new level every 12 f. 120 f.

| Part | Motion | Measured |
|---|---|---|
| Bar 1–16 (anchor at the bottom) | scale Y on Hold keys: a new level (15–100%, seeded random) every 12 f, offset 1 f per bar | stepped; no in-betweens |

Lint 0 errors, 0 warnings; `inspect qc` (240 px) found no flashes. Placed into a fresh comp: lint 0/0/0.

## Why stepped
A smooth up-and-down equalizer is a ping-pong, which lint reads as `jitter` when its reversals are small. Hold keys jump, so there are no sub-pixel reversals, and the stepped look suits a digital readout.

Inspiration: audio and signal meters in HUDs. No external text or code was used.
