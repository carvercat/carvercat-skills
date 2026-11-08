# Terminal type-on

**Template** `gl_terminal` (Library name "Terminal type-on") · Glitch pack · **verified 0.1.8.1 (rev 1127 build; headless, isolated folders, pack added to a scratch user Library; `ai/scripts/motion/verify_pack.py`)**, comp `GL Terminal` in `categories/glitch/gl-lab-2`.

Four console lines (green SemiBold 44 px, the last in white) that type on at one character a frame, then a blinking block cursor after the last line. 150 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Term line 1–4 | 6, 32, 58, 84 | a Stagger effect by character (1 f each) on relative opacity, Hold 0 → 1 | line 4 fully typed by **f100** |
| Term cursor (26 × 44 px, placed after the last line with `cc.textw`) | 104 | opacity Hold: 14 f on, 14 f off | |

Lint 0 errors, 0 warnings; `inspect qc` (240 px) found no flashes. Placed into a fresh comp: lint 0/0/0. The type-on is built like the HUD readout ([fh-readout.md](fh-readout.md)): a stagger on the text's relative opacity, not a key on the text content ([KI-051](../references/known-issues.md#ki-051)).

Inspiration: hacker-terminal scenes. No external text or code was used.
