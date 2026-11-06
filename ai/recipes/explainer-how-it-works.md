# Explainer: how it works, 25 s

**Brief:** teach one idea: name it, show the flow, list the steps, check understanding. **Verified 0.1.6 (rev 1105), 2026-10-28; builder and measures re-run on Carvercat 0.1.8, 2026-11-04** Sample: `categories/recipes/explainer-how-it-works` (750 f, 1920 × 1080, light ground). Builder: `ai/scripts/motion/recipes/rc_explainer.py` (the master is a `carvercat/2` file or one `scene.apply`: [how](README.md#how-the-samples-are-built)).

## Shot list
| Time | Frames | Template (Explainer) | Job |
|---|---|---|---|
| 0:00 | 0–149 | Key term card | the idea and its definition |
| 0:05 | 150–299 | Flow diagram | how it flows |
| 0:09.5 | 285–314 | Dip to colour (Transitions) | from "what" to "how"; cut at f300 |
| 0:10 | 300–419 | Process steps | the steps |
| 0:14 | 420–569 | Checklist | what to check |
| 0:19 | 570–749 | Quiz question | check understanding; answer at +100 f |

## Timing logic
- Scenes run 4–6 s, at narration speed; each template builds in reading order.
- The quiz is last and longest: 50 f of think time before the answer.

## Measured on the master
- Lint 0 / 0 / 0.
- `qc` (240 px) notes the holds after each build (f36–149, f204–285, f359–419, f489–569, f683–749) as freezes; under narration these are reading time. It also notes f298–302 as black: the dip.

Inspiration: the define → show → steps → check structure of short lessons. No external text or code was used.
