# Caption pages (9:16)

**Template** `ss_caption_pages` · Social Short-form pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SS Caption pages`.

Three pages ("I tried this", "for 30 days", "and it worked"), each a 40 f text clip: ExtraBold 72 px white with a black outline (`text.outline`: paint solid, thickness 0.12, outside only, round corners), centred at (490, 1250).

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Caption *i* | clip 40*i* to 40*i* + 40 | **Caption words pop**, word gap 3 | 4.4% overshoot, settles 8 f after each word starts |

Lint 0/0 (40 f is enough to read three words). The safe box passes. Pages are centred at x 490, not 540, so their right edge stays left of the platform's button column (x > 851 below y 1151).

## Steps
Replace the pages with your transcript: one clip per 2–4 words, clip length = the spoken phrase (at least 25 f). For words from a voice-over, cut the clips on the word times from `ai/scripts/motion/vo_align.py`.
