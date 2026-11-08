# Venetian blinds

**Template** `rt_blinds` (Library name "Venetian blinds") · Retro pack · **verified 0.1.8.1 (rev 1127)**, comp `RT Blinds` in `categories/retro/rt-lab-2`.

**Measured on 0.1.8.1 (rev 1127, harness `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0, no flashes; against the v1 original the worst silhouette difference is 0.00 % (limit 2 %) and every object is present with the same text (box offset at most 0.0 px); colours are now the exact hex the page states (mean shift 11.2 of 255, intended); windows over a magenta/green underlay: covered f20-31 (cut f20), gone f52, settled f52. The frame numbers in the table above are the keys of the generator (`design units`), unchanged.


A transition: eight full-width slats (orange, mustard, teal, red) close from the top down, 2 f apart and on twos, then open again in the same order. 54 f.

| Part | Motion | Measured |
|---|---|---|
| Blind 1–8 (1000 × 136 px drawn, scale X 1.92, anchor at the top edge) | scale Y 0 → 1 on twos, 8 f, from f0, 2, … 14; 1 → 0 (accelerating), from f30, 32, … 44 | all closed **f22–30** by the keys; the harness's covered window (under 0.5 % of the underlay showing) is **f20–31**; Blind 8 gone at **f52** |

Lint 0 errors, 0 warnings; `inspect qc` (240 px) found no flashes. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place 26 f before your cut, above both scenes; cut at its f26.

## Pitfalls
- With the exits at +22 f, the last slat's keys ran to f44 in a 40 f comp: lint **errors** `key_outside_clip` and a `cut_off_by_comp_end` warning. The comp is 54 f and the exits start at +30 f, which also gives an 8 f full cover.

Inspiration: venetian-blind wipes in 70s TV graphics. No external text or code was used.
