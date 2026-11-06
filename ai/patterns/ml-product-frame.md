# Product frame

**Template** `ml_product_frame` · Minimal Luxury pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `ML Product frame`.

A 520 × 680 px frame (2 px gold stroke, no fill). Inside it a 300 px product stand-in: a radial gradient from ivory to a deep shadow tone. Under the frame, the caption "No. 7 · EAU DE PARFUM" (30 px, tracking 1.4).

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Frame | 0–40 | Trim Stroke end 0 → 1, S curve cubic-bezier(0.333, 0, 0.667, 1), the curve arriving at the key; the path starts at the middle of the right side | settles **f36** |
| Product | from 20 | **Slow fade in** + **Drift up - 4 s** on the same clip | size settles **f48**; drifts to the end |
| Caption | from 44 | **Slow fade in** | opacity settles **f76** |

**Fixed 2026-10-28 ([KI-155](../references/known-issues.md#ki-155)).** The radial highlight sat below and left of the centre, so the stand-in looked lit from underneath. The builder meant the light at the top-left corner (`(cx − 150, cy − 150)` → `(cx + 150, cy + 150)` in comp pixels), but `cc.py` wrote it as comp coordinates with y up. The radial now has its centre at the box's top-left `[0, 0]` and reaches `[1, 1]`. Measured on 0.1.6 (rev 1105) at f100 along the diagonal: `(206, 199, 183)` at the upper left, `(166, 160, 147)` at the centre, `(112, 108, 98)` at the lower right. Placed into a fresh comp: lint 0/0/0. `categories/minimal-luxury/ml-lab`, `ml-showcase` and the recipe `luxury-product-teaser` carry the same fix ([audit](../references/audits/gradient-direction-audit-2026-10-28.md)).

Lint 0/0/0. Replace the stand-in with the product cut-out (a media object) and keep both presets on it. Keep the product inside the frame with at least 80 px of air.
