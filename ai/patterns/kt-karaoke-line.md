# Karaoke line

**Template** `kt_karaoke_line` (Library name "Karaoke line") · Kinetic Typography pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `KT Karaoke line` in `categories/kinetic-typography/kt-lab-3`.

For briefs like "lyric video", "sing-along", "read-along captions for a song". Two lyric lines ("We were running out of time, / but the night was ours.", ExtraBold 88 px, centred, rows 128 px apart) rise in dim and readable ahead of the vocal. Each word then fills yellow on the frame it is sung, with a small 1.08 pop. One text object per word (a text has one fill colour). 150 f, holds.

Frames are comp frames.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Words (dim `#6F6B64`) | 0–8 (2 f per word, line 2 from f4) | rise 20 px, 14 f (expo), fade 5 f | first word settles **f9**, last **f22** |
| Word fill | its sung frame (`SUNG`: f14–50, f70–100) | Colour dim → `#FFD23F` in 3 f | settles **3 f** after the sung frame (first f17, last f103) |
| Word pop | its sung frame | scale 1 → 1.08 (3 f, the decelerating arrival curve cubic-bezier(0.333, 0.667, 0.667, 1)) → 1 (9 f, expo) | 0% overshoot; still **12 f** after the sung frame (first f26, last f112) |

Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (closest 17.0 px, "the" / "night").

## Steps
1. Mark each word's sung frame from the vocal (`ai/scripts/motion/vo_align.py`, then check against the waveform; [lyric videos](../../wiki/genres/lyric-videos.md) puts the word 0–4 f before the syllable).
2. Put the words in `KARAOKE` and the frames in `SUNG` in `ai/scripts/motion/kinetic_type_lab3.py` and rebuild: word positions come from `cc.textw`, so a new lyric is laid out for you.
3. Editing a placed instance by hand: retime the two Colour keys and three size keys of each word together.
4. A long song: one comp per line pair, nested in a master; cut to the next pair when its first word is 4–6 f away.

## Pitfalls
- **Scale each word from its centre.** The words are centre-aligned texts placed at their own centres, so the pop grows evenly both ways. A left-aligned text's position is its left edge (measured: its bounds start exactly at x), so the whole pop would land on the right-hand side, towards the next word.
- Keep the pop at 1.08 or less: a word grows about 4% each side, which stays inside one space width (about 20 px at 88 px).

Inspiration: sing-along and karaoke captions. No external text or code was used.
