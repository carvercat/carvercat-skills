# Exaggeration

**What it does:** pushing a pose or a move past reality makes it read clearly and with character. The dose is a style decision.

## How in Carvercat
- Overshoot (springs, back ease), scale punches (start above 100%), stretch, and big rotations are the tools. Pick one per hero beat.
- Springs are baked from `curves.py`: gentle (about 4.4–4.6%), bouncy (about 16%), wobbly (about 31%).

## Measured overshoot by style
| Style | Max overshoot | Example |
|---|---|---|
| Corporate, Minimal Luxury, Explainer | 0% | Soft rise, Slow fade in, Step in |
| Retro | 3.9% | Pop - on twos |
| SaaS, Data Viz | 4.4% | Toast drop, Bar grow - spring |
| Kinetic | 4.6% (16.2% letter pop) | Words slam |
| Sports | 6.7% past the impact (from 220%) | Impact slam |
| Cartoon, Funky | 30.8–30.9% | Pop - wobbly, Tilt pop angle |

## Traps
- Big scale punches on text next to other text fail `text_overlap` (Impact slam 220% and Zoom past 300%: [sp-lower-third.md](../../../patterns/sp-lower-third.md)).
- Pops from 0 on small text fail `text_too_small` in the first frames (measured at 48 and 110 px; [funky.md](../../../patterns/funky.md)). Use Stamp or Words slam, which start large.
- `curves` reports large "overshoot" values for stacked entrance and exit presets; confirm with a look.
