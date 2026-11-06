# Luxury product teaser, 28 s

**Brief:** a slow, quiet teaser for a product or collection: brand, season, product, craft, price, signature. **Verified 0.1.6 (rev 1105), 2026-10-28; builder and measures re-run on Carvercat 0.1.8, 2026-11-04** Sample: `categories/recipes/luxury-product-teaser` (840 f, 1920 × 1080, warm black). Builder: `ai/scripts/motion/recipes/rc_luxury.py` (the master is a `carvercat/2` file or one `scene.apply`: [how](README.md#how-the-samples-are-built)).

## Shot list
| Time | Frames | Template (Minimal Luxury) | Job |
|---|---|---|---|
| 0:00 | 0–119 | Light sweep | the brand, with a gleam |
| 0:04 | 120–269 | Collection title | the season |
| 0:08 | 240–299 | Slow dip | into the product; black f266–274, cut at f270 |
| 0:09 | 270–389 | Product frame | the product (replace the stand-in) |
| 0:13 | 390–539 | Attribute row | the craft |
| 0:18 | 540–689 | Price card | name, material, price |
| 0:22 | 660–719 | Slow dip | into the signature; cut at f690 |
| 0:23 | 690–839 | Monogram end card | the house |

## Timing logic
- 4–5 s per scene: everything in this style is slower than you think (entrances 30–60 f).
- Dips only at the two changes of register; no other transitions.

## Measured on the master
- Lint 0 / 0 / 0.
- `qc` (240 px) reports almost the whole film as "black" and "freeze": the warm-black ground is under its 4% luminance line, and the drifts, tracking breathes and thin gold lines are below its change threshold. The looks show the motion. For this style judge with `carvercat_look`, not `qc`.
- The Attribute row in this sample is the fixed one (2026-10-28; [../patterns/ml-attribute-row.md](../patterns/ml-attribute-row.md)): the first release ran its words together.
- The Product frame in this sample is the fixed one (2026-10-28, [KI-155](../references/known-issues.md#ki-155); [../patterns/ml-product-frame.md](../patterns/ml-product-frame.md)): the first release lit the stand-in from below. Fixed in the saved sample with `property.set`; master lint 0/0/0 before and after.

Inspiration: fragrance and fashion teasers. No external text or code was used.
