# Chromatic logo sting

**Template** `gl_chroma_sting` (Library name "Chromatic logo sting") · Glitch pack · **verified 0.1.8.1 (rev 1127 build; headless, isolated folders, pack added to a scratch user Library; `ai/scripts/motion/verify_pack.py`)**, comp `GL Chroma sting` in `categories/glitch/gl-lab-3`.

For briefs like "glitch logo ident", "RGB logo reveal", "channel sting". Three copies of a mark (a stand-in bolt) in pure red, green and blue, each blended with **Screen**, step together from 70 px apart; where they line up they add to white. Then the wordmark lands with a red/cyan split and a tagline; one short re-split at f50. 90 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Mark red / green / blue (path, `transform.compositing.blend` Screen) | 0 | Hold steps: red −70 → −36 → −14 → 0 px, blue the mirror, green ±40 → 0 px vertically; scale 118 → 108 → 103 → 100%; re-split f50–54 | white at **f12**; steady **f54** |
| Wordmark (ExtraBold 110, tracked) | 16 | split 22 → 12 → 16 → 4 → 0 px; re-glitch f50–54 | **f28** |
| Tagline (green SemiBold 40) | 30 | opacity Hold steps | **f35** |

Lint 0 errors, 0 warnings; `inspect qc` (240 px): **no flashes**. Placed into a fresh comp: lint 0/0/0, qc no flashes; a full-frame look of the placed instance at f0 shows the three copies, split, inside the frame and still adding up through Screen. Text-gap audit: closest pair wordmark / tagline, 55.6 px.

## Steps
1. Replace the bolt with your mark: three copies, filled pure red `[1, 0, 0]`, green and blue, each with blend Screen. Screen works on any ground; on a light ground the colour fringes almost vanish, so use it over dark.
2. Blend modes are not keyframeable ([blend modes](../../wiki/techniques/blend-modes.md)); the copies stay Screen for the whole clip.

Inspiration: RGB channel-split idents. No external text or code was used.
