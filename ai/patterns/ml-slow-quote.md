# Slow quote

**Template** `ml_slow_quote` · Minimal Luxury pack · **Verified 0.1.8.1 (rev 1127)**, comp `ML Slow quote`.

A two-line quote (Regular 64 px, ivory, centred, line spacing 1.3) with the author line "— ANONYMOUS" (28 px, muted, tracking 1.5) under it.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Quote lines | 0–30 per line, 12 f apart | Stagger Text by line: relative position rise 1%, opacity, and a Gaussian blur 10 → 0 (expo) | blur settles **f19**, opacity **f14** per line |
| Quote tracking | 42–150 | 1.0 → 1.04, linear (the breathe) | |
| Author | from 60 | **Slow fade in** | opacity settles **f92** |

Lint 0/0/0. Edit the quote inside the comp, keeping a line break (one line per thought, at most about 28 characters per line). Hold at least 4 s for two lines.
