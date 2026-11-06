# Beat words

**Template** `kt_beat_words` · Kinetic Typography pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `KT Beat words`.

One huge word at a time (220 px ExtraBold, centred): THINK / BUILD / SHIP / REPEAT, in alternating off-white, accent, off-white and yellow. Each word is a 25 f clip. It cuts in at full opacity at 135% and settles to 100% in 8 f (Custom expo).

Measured: scale settles 5 f after each cut (within 0.5%); lint 0/0/0. Each word is readable for its full 25 f, which is lint's minimum for a short word.

## Timing to music
At 30 fps, 25 f per word is 72 BPM with one word per beat. For other tempos, use clip length = 1800 / BPM frames per beat: 120 BPM = 15 f, which lint will flag as too short to read, so use two beats per word (30 f). Cut ON the beat; the scale lands 3–4 f after it.

## Steps
Place and apply, edit the four words, and keep each word at 8 letters or fewer. To add words, duplicate the last clip inside the comp, move it 25 f on, and lengthen the comp.
