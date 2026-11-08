# Lower third with an accent bar

**Template:** `Lower third - accent bar` (mp_lt_accent_bar) · **Verified 0.1.8.1 (rev 1127)** · 120 f · overlay (no background)

## Timing chart

```
LT bar   6 grow Y (expo, 16 f) ........................ 92 scale Y -> 0 (accelerating arrival `cubic-bezier(0.333, 0, 0.667, 0.333)`, 9 f) 101
LT name     9 words rise (gap 3) ............... 89 exit down (12 f) 100
LT role         13 rise expo ....................... 93 fade (8 f) 100
```
Entrances are spaced 3–4 f apart: bar, then name, then role. Exits go in reverse order and are faster (8–12 f against 16–18 f).


**Measured** on `MP LT Accent bar` (one definition for every number below: the lab comp rendered at 320x180, `starts` = first frame that differs from frame 0 by at least 0.5 (mean channel value, 0-255), `steady` = the frames whose picture matches the settled one within 0.5; harness `ai/scripts/motion/verify_pack.py`): first change f15, steady from f17 to f97, exit visible from f98, last visible frame f99 (harness `gone` = 100). The name's exit moves the whole name; its entrance is per word. Lint 0/0/0; object check against v1 passes (largest box offset 0.3 px, ink overlap 0.93-0.99).

## Layout used
 (1920×1080)

- Bar: 11.5 × 144 px at x = 167 (left edge), centred on the two lines.
- Name: Open Sans Bold, 51.6 px, left-aligned, its drawn letters start at x = 196, y = 828 (box top 814.4). Put the playhead at frame 40, because the clip starts at frame 9.
- Role: Open Sans Regular, 29.8 px (58% of the name), grey `#DDDDDD`, drawn letters start at x = 196, y = 882.
- All inside the 16:9 title-safe area. For 9:16, see `../references/craft/vertical-and-safe-areas.md`.

## Pitfalls

- Do not slide the name in from the left across the bar. With no mask it passes over the bar and looks cheap; that was our first attempt. Use a rise, or mask the text.
- Lint warns that the name and role overlap for about 1 frame during the exit (both fading). That's acceptable; to make it clean, exit the role 4 f earlier.
