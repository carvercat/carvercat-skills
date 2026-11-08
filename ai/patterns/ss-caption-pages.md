# Caption pages (9:16)

**Template** `ss_caption_pages` · Social Short-form pack · **verified 0.1.8.1 (rev 1127)**, comp `SS Caption pages`.

**Measured on 0.1.8.1 (rev 1127, harness `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0, no flashes; against the v1 original the worst silhouette difference is 0.12 % (limit 2 %) and every object is present with the same text (box offset at most 0.0 px); colours are now the exact hex the page states (mean shift 19.6 of 255, intended). The frame numbers in the table above are the keys of the generator (`design units`), unchanged.


Three pages ("I tried this", "for 30 days", "and it worked"), each a 40 f text clip: ExtraBold 72 px white with a black outline (`text.outline`: paint solid, thickness 0.12, outside only, round corners), centred at (490, 1250).

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Caption *i* | clip 40*i* to 40*i* + 40 | **Caption words pop**, word gap 3 | 4.4% overshoot, settles 8 f after each word starts |

Lint 0/0 (40 f is enough to read three words). The safe box passes. Pages are centred at x 490, not 540, so their right edge stays left of the platform's button column (x > 851 below y 1151).

## Steps
Replace the pages with your transcript: one clip per 2–4 words, clip length = the spoken phrase (at least 25 f). For words from a voice-over, cut the clips on the word times from `ai/scripts/motion/vo_align.py`.
