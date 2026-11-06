---
id: cookbook/countdown-clock
title: Make an mm:ss countdown clock
section: cookbook
tags: [countdown, timer, clock, mm:ss, minutes seconds, digits, event, launch, live stream]
styles: [saas-ui, corporate-brand, sports, social-short-form]
topics: [text, masking, timing]
related: [cookbook/count-a-number-up, cookbook/countdown, cookbook/split-flap-digit, techniques/masking, sound-and-timing/frame-rates]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Countdown]
---

# Make an mm:ss countdown clock

**Goal.** A real clock that counts down second by second ("01:05" … "00:00") and turns red for the last ten
seconds, for a stream starting soon or an event opener.

## Steps

Text content cannot be keyed, so each changing digit is a **column** "0⏎1⏎…⏎9" behind a window, as in
[count a number up](count-a-number-up.md), but stepped with `hold` keys instead of rolled.

1. **Measure once** at your size with `carvercat_authoring mode:geometry`: the column "0⏎…⏎9" and a single
   "0". Line pitch = (column height − digit height) / 9; slot width = digit width + 10 px.
2. Make four texts, centred: a fixed "0" (tens of minutes), the minutes column, a fixed ":", the
   tens-of-seconds column and the seconds column.
3. To show digit *d* in a slot at height *Y*, the column's centre goes to **Y + (4.5 − *d*) × pitch** (y down; its `y` is the top of the layout box, centre − height/2).
4. Key each column's position on every frame where its digit changes: frame = 30 × (seconds elapsed) at
   30 fps, easing **`hold`**, so the digit switches on that frame. Remaining *r* = start − ⌊f / 30⌋; seconds
   digit *r* mod 10, tens (*r* mod 60) div 10, minutes *r* div 60.
5. A window rectangle (slot width × 0.98 pitch) over each column; on each column `property.set {key: "mask", value: "<window>"}`,
   then `parent.clear` on the windows.
6. Last ten seconds: one `hold` colour key on every digit and the colon at frame 30 × (start − 10).

## Measured in Carvercat 0.1.6

Comp `K Countdown clock` in [cookbook lab 8](../labs/README.md#cookbook-lab-8carverproj): 160 px Rethink Sans
Bold, start 65 s, 1980 frames. Digit read back from each column's probed centre:

| Frame | 0 | 29 | 30 | 149 | 150 | 179 | 180 | 1649 | 1650 | 1950 |
|---|---|---|---|---|---|---|---|---|---|---|
| Reads | 01:05 | 01:05 | 01:04 | 01:01 | 01:00 | 01:00 | 00:59 | 00:11 | 00:10 | 00:00 |

- Line pitch at 160 px Bold: (2045.5 − 115.8) / 9 = **214.4 px** (1.34 × the font size, as for the counter).
  Every digit landed exactly on its line (whole numbers in the read-back).
- The minute rolls over on f180 in all three columns at once ("01:00" → "00:59").
- Colour: white (242, 242, 240) on f1649, red (229, 72, 59) on **f1650**.
- `inspect lint`: 0 errors, **77 warnings**: 75 `cropped_at_rest` (66 on the seconds column, one per held
  digit, 7 on the tens, 2 on the minutes) and 2 `text_overlap` (the whole columns overlap their neighbours),
  plus 3 `speed_jump` notes for the Hold jumps. All are mask-blind; `carvercat_look` shows a clean clock.

## Traps

- `text.content` is not keyframeable: [KI-051](../../ai/references/known-issues.md#ki-051); a native number
  text is [FR-034](../../ai/references/known-issues.md#fr-034).
- Lint ignores masks, hence the 77 warnings: [KI-133](../../ai/references/known-issues.md#ki-133).
- Use a monospace-like layout: each digit sits centred in its own fixed slot, so a "1" does not make the
  clock jump sideways.
- At 25 fps a second is 25 frames; compute key frames from the comp rate ([frame rates](../sound-and-timing/frame-rates.md)).

## In Carvercat

- Library: `Countdown (9:16)` (a 3-2-1 for vertical), `Big number`; for a short 3-2-1 see [countdown](countdown.md).
- Commands: `carvercat_authoring mode:geometry`, `property.set` (`mask`), `parent.clear`; keys with `hold` easing. Old name, accepted: `mask.make {ids:[window, column]}`.
