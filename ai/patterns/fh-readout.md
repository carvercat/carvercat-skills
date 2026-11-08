# Data readout

**Template** `fh_readout` · Futuristic HUD pack · **verified 0.1.8.1 (rev 1127 build; headless, isolated folders, pack added to a scratch user Library; `ai/scripts/motion/verify_pack.py`)**, comp `FH Readout`.

A 300 px glowing accent bar and four rows (y 435–645): labels in dim cyan at x 600, values in cyan right-aligned at x 1320, all SemiBold 34 px tracked caps. The rows are SYS STATUS / NOMINAL, CORE TEMP / 41.8 C, LINK / ENCRYPTED and SIGNAL / 98%.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Accent bar | 0–14 | scale Y 0 → 1, expo | settles **f9** |
| Row *i* label | from 8 + 10*i* | **Flicker on** | |
| Row *i* value | from 12 + 10*i* | type-on: Stagger Text by character (gap 2) on the relative opacity, keyed 0 → 1 with Hold | first character at 13 + 10*i* |

Lint 0/0. Change the rows inside the comp and keep values short (12 characters or fewer). For counting numbers, use the SaaS [rolling counter](su-rolling-counter.md).
