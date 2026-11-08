# Link in bio (9:16)

**Template** `ss_link_in_bio` (Library name "Link in bio (9:16)") · Social Short-form pack · **verified 0.1.8.1 (rev 1127)**, comp `SS Link in bio` in `categories/social-media-reels/ss-lab-3`.

**Measured on 0.1.8.1 (rev 1127, harness `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0, no flashes; against the v1 original the worst silhouette difference is 0.00 % (limit 2 %) and every object is present with the same text (box offset at most 0.2 px); colours are now the exact hex the page states (mean shift 3.1 of 255, intended). The frame numbers in the table above are the keys of the generator (`design units`), unchanged.


For briefs like "send them to the link in bio", "swipe up for the guide", "where to get it". A yellow kicker, LINK / IN BIO (ExtraBold 150 px, IN BIO on a pink plate), a white link chip with an open-link icon and the URL, one pulse off the chip, and a small instruction line. 120 f, holds (a CTA needs at least 2 s).

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Kicker "Want the full list?" (Bold 56 px, yellow) | 0 | Hook punch (as keys) | settles **f7** |
| LINK, IN BIO (ExtraBold 150 px) | 4, 8 | Hook punch | **f11**, **f15** |
| Bio plate (pink, sized to the text + 70 px) | 10 | scale X 0 → 1 from the left, 8 f, expo | **f15** |
| Link chip (620 × 104 px pill), icon, arrow | 20 | Whip in - left (as keys), motion blur 180 on the chip | **f27** |
| Link text (Bold 44 px) | 22 | Whip in - left | **f29** |
| Chip pulse (pill outline, 6 px) | 40 (18 f clip) | scale 1 → 1.12 × 1.5, fades out | scale **f52**, gone **f57** |
| Link note "tap the link on my profile" (Medium 40 px) | 32 | Hook punch | **f39** |

**0% overshoot.** Lint 0/0/0. `bounds_inside` passed for every object; the chip ends at y 1072 and the note at about 1140, above the button column (y 1151). Placed into a fresh 1080 × 1920 comp: lint 0/0/0. Text-gap audit: closest pair 52.9 px (note / icon). The whip-in is inside the instance; a full-frame look of the placed comp shows nothing cut once it lands.

## Steps
1. Place and apply; edit the kicker, the URL and the note. A URL up to about 20 characters fits the chip at 44 px; for longer ones widen `cw` in the lab script.
2. Hold the end on screen for 2 s or more.

## Pitfalls
- A looping pulse is read by lint as jitter (pack pitfall 1); the chip pulses once.
- Do not move the chip below y 1100: the caption and CTA bar of the platform sit under it.

Inspiration: "link in bio" end cards on short-form video. No external text or code was used.
