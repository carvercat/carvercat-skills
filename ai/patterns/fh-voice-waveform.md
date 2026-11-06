# Voice waveform

**Template** `fh_voice_waveform` (Library name "Voice waveform") · Futuristic HUD pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FH Voice waveform` in `categories/futuristic-hud/fh-lab-3`.

For briefs like "AI voice assistant", "voice command", "podcast or audio teaser". Three sine waves slide one way under soft mask windows while their height follows a voice; the spoken line types on and a confirmation flickers in. 150 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Mic ring, Mic dot, Mic ping 1–2, Listening | 0 / 4 / 20, 42 / 2 | ring scans open; dot and label flicker on; two rings grow 0.3 → 2× | |
| Wave base | 0 | Trim end, f0–14 | |
| Wave 1–3 (sine paths; λ 400 / 300 / 240 px, amplitude 110 / 84 / 64 px, strokes 5 / 4 / 4 px, cyan / white 70% / amber 60%) | 0 | slide left 800 / 900 / 960 px at constant speed over the clip (two keys, Linear); height (scale y) 35% idle → 100% (f24) → 60 (f44) → 95 (f62) → 50 (f82) → 90 (f100) → 35% (f122), S curve cubic-bezier(0.333, 0, 0.667, 1) | position Linear to **f149**; scale settles **f122** |
| Wave window 1–3 (1200 × 300 px, fill soft edge 90 px) | 0 | static masks, one per wave (`property.set` key `mask` with `{"ref": <window id>}`, then `parent.clear {ids:[window, wave]}` when the window must move independently) | |
| Transcript "Set course for the north relay" (Medium 52 px) | 30 | types on, 1 f a character | |
| Confirm "ROUTE CONFIRMED" (green 30 px) | 110 | Flicker on | on **f120** |

Lint (with `contrast:true`) 0 errors, 0 warnings, 3 notes (`repeated_key_value` on the idle holds; intended). `inspect qc` (240 px): no flashes. Placed into a fresh comp: lint 0/0/0; the three masks survive placement. Text-gap audit: 9 pairs, closest 33 px. Full-frame looks of the placed comp at f24 and f62 (tallest waves): the waves stay inside their soft windows.

## Steps
1. Retime `amp_keys` in `waveform()` to the voice-over's loud and quiet passages (S curve between hand-set extremes, not a baked wobble).
2. Change the transcript; keep it under about 40 characters for the 150 f clip (reading time).

## Pitfalls
- **Scale y thins the stroke too.** A wave squashed to 8% drew its 5 px stroke as broken dashes; the idle height is 35%, never less.
- A sine path needs tangent handles at the zero crossings (slope 2π·A/λ) and flat handles at the peaks, a third of a quarter wavelength long; corner nodes make a zigzag.
- The path is wider than the window by the travel plus a wavelength, so its end never shows; masks hide everything outside the window ([KI-151](../references/known-issues.md#ki-151): keep the window inside the frame).

Inspiration: common sci-fi HUD and interface conventions. No external text or code was used.
