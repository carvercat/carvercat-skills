# Lower third with an accent bar

**Template:** `Lower third - accent bar` (mp_lt_accent_bar) · **verified 0.0.72** · 120 f · overlay (no background)

## Timing chart

```
LT bar   6 grow Y (expo, 16 f) ........................ 92 scaleY -> 0 (Ease in, 9 f) 101
LT name     9 words rise (gap 3) ............... 89 exit down (12 f) 100
LT role         13 rise expo ....................... 93 fade (8 f) 100
```
Entrances are spaced 3–4 f apart: bar, then name, then role. Exits go in reverse order and are faster (8–12 f against 16–18 f).

## Layout used (1920×1080)

- Bar: 11 × 144 px at x = 173, centred on the two lines.
- Name: Open Sans Bold, size 0.045, left-aligned, seated with `authoring.place_bounds {box:[196,822,900,52], horizontal:"left"}`. Use `frame: 40`, because the clip starts at frame 9.
- Role: size 0.026 (58% of the name), grey (0.75 linear), box `[196,880,900,34]`.
- All inside the 16:9 title-safe area. For 9:16, see `../references/craft/vertical-and-safe-areas.md`.

## Pitfalls

- Do not slide the name in from the left across the bar. With no mask it passes over the bar and looks cheap; that was our first attempt. Use a rise, or mask the text.
- Lint warns that the name and role overlap for about 1 frame during the exit (both fading). That's acceptable; to make it clean, exit the role 4 f earlier.
