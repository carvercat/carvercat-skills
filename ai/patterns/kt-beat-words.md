# Beat words

**Template** `kt_beat_words` · Kinetic Typography pack · **verified 0.1.8.1 (rev 1127; `ai/scripts/motion/verify_pack.py`: placed in a fresh 16:9 and a fresh 9:16 comp, lint 0/0/0, qc no flash; against the v1 original the silhouette differs by at most 0.00 % of pixels over 7 frames; object-level check pass)**, comp `KT Beat words`.

One huge word at a time (220 px ExtraBold, centred): THINK / BUILD / SHIP / REPEAT, in alternating off-white, accent, off-white and yellow. Each word is a 25 f clip. It cuts in at full opacity at 135% and settles to 100% in 8 f (Custom expo).

Measured: scale settles 5 f after each cut (within 0.5%); Lab comp lint on 0.1.8.1 (native size): 0 errors, 0 warnings, 0 notes. Each word is readable for its full 25 f, which is lint's minimum for a short word.

## Timing to music
At 30 fps, 25 f per word is 72 BPM with one word per beat. For other tempos, use clip length = 1800 / BPM frames per beat: 120 BPM = 15 f, which lint will flag as too short to read, so use two beats per word (30 f). Cut ON the beat; the scale lands 3–4 f after it.

## Steps
Place and apply, edit the four words, and keep each word at 8 letters or fewer. To add words, duplicate the last clip inside the comp, move it 25 f on, and lengthen the comp.
