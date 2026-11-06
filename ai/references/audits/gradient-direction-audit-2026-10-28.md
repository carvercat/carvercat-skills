Historical report in the units of its time (fractions, y up); current work uses design units: ../app/design-units.md.

# Gradient direction audit, 2026-10-28 (KI-155)

**Why:** `ai/scripts/motion/json_author/cc.py` `Obj.gradient()` wrote its endpoints as comp coordinates with y up
(`P(x, y)` = `[x / 1920, 1 − y / 1080]`). The app reads a gradient's `start` / `end` as **object-local, y down**:
`[0, 0]` is the top-left and `[1, 1]` the bottom-right of the shape's box. So every vertical gradient written
through the helper came out upside down, and on anything smaller than the frame the blend was also squeezed or
moved ([KI-155](../known-issues.md#ki-155)).

**Measured on Carvercat 0.1.6 (rev 1105), headless, isolated state, never `--connect`.**

## The minimal case

Red (stop 0) → blue (stop 1), rendered at f5, pixels read from the PNG.

| Object | Written | Stored | Rendered |
|---|---|---|---|
| Full-frame rectangle, old helper | `(960, 0)` → `(960, 1080)` (meant red at the top) | `[0.5, 1]` → `[0.5, 0]` | top `(20, 0, 253)` blue, middle `(180, 0, 180)`, bottom `(253, 0, 19)` red: **upside down** |
| 400 px square at x 100–500, y 600–1000, old helper | `(300, 600)` → `(300, 1000)` | `[0.156, 0.444]` → `[0.156, 0.074]` | blue at the top, blend from 7% to 44%, red below: upside down and squeezed |
| 400 px square at x 1100–1500, old helper | `(1100, 300)` → `(1500, 300)` | `[0.573, …]` → `[0.781, …]` | red over the left 57%, blend 57–78%, blue after: right way, squeezed |
| 400 px square, raw object-local | `[0.5, 0]` → `[0.5, 1]` | same | top `(252, 0, 27)` red → bottom `(25, 0, 252)` blue: right |
| 400 px square, raw object-local | `[0, 0.5]` → `[1, 0.5]` | same | left red → right blue: right |
| Text "HHHH", raw object-local on `text_fill` | `[0.5, 0]` → `[0.5, 1]` | same | red at the top of the letters, blue at the bottom: text uses the same space |
| Radial, raw | centre `[0.5, 0.5]`, end `[1, 0.5]` | same | red at the centre, blue at the half-width circle: `start` is the centre, the distance to `end` the radius |

## The helper fix

`Obj.gradient(stops, start, end, mode='linear', local=False)` keeps its signature and its callers. `start` / `end`
are now what the module always said its space was: **comp pixels, y down**, read on the object at rest (its
`at()` position, scale 1, no rotation). The helper converts them to object-local units with the shape's box, so
the stored gradient moves, scales and turns with the object. `local=True` passes object-local units straight
through. Comp pixels work for `rect()` and `ell()` (their box is known); other kinds raise and ask for `local=True`.

Measured after the fix, the same calls:

| Object | Written | Stored | Rendered |
|---|---|---|---|
| Full-frame rectangle | `(960, 0)` → `(960, 1080)` | `[0.5, 0]` → `[0.5, 1]` | top `(253, 0, 20)` red → bottom `(19, 0, 253)` blue |
| 400 px square, vertical | `(300, 600)` → `(300, 1000)` | `[0.5, 0]` → `[0.5, 1]` | `(252, 0, 27)` → `(180, 0, 180)` → `(25, 0, 252)`, full height |
| 400 px square, horizontal | `(1100, 300)` → `(1500, 300)` | `[0, 0.5]` → `[1, 0.5]` | full-width blend, left red → right blue |
| 400 px ellipse | `(960, 100)` → `(960, 500)` | `[0.5, 0]` → `[0.5, 1]` | `(252, 0, 27)` → `(180, 0, 180)` → `(25, 0, 252)` |
| 400 px ellipse, radial | `(760, 600)` → `(1160, 1000)` | `[0, 0]` → `[1, 1]` | red towards the top-left, blue towards the bottom-right |
| 400 px square, `local=True` | `[0.5, 0]` → `[0.5, 1]` | same | top red → bottom blue |
| 1080 × 1920 comp, full-frame (as `recipe_kit.author` writes it) | `(540, 0)` → `(540, 1920)` | `[0.5, 0]` → `[0.5, 1]` | top `(254, 0, 10)` red → bottom `(10, 0, 254)` blue |

Lint on the test comp: 0/0/0.

## Every gradient checked

"Intended" comes from the pattern doc, the names and the colours; "rendered" is measured (fixed rows) or follows
from the stored endpoints and the measured convention above. Up/down means on screen.

| # | Where (template / sample) | Written by | Intended | Rendered before | Result |
|---|---|---|---|---|---|
| 1 | `rt_synthwave` Sun; samples `retro/rt-lab`, `retro/rt-showcase` | `retro_lab.py`, helper | yellow at the top → pink at the bottom (doc: "yellow → pink, top to bottom") | pink at the top, yellow at the bottom, blend squeezed to the middle | **Fixed**: `[0.5, 0]` → `[0.5, 1]` |
| 2 | `rt_chrome_title` Chrome word; samples `retro/rt-lab-2`, `retro/rt-showcase-2`, `recipes/retro-night-promo` | `retro_lab2.py`, raw text gradient written y up | pale sky at the top, bright band, hard step, magenta at the bottom (doc) | magenta at the top, sky at the bottom | **Fixed**: `[0.5, 0]` → `[0.5, 1]` |
| 3 | `ml_product_frame` Product (radial); samples `minimal-luxury/ml-lab`, `minimal-luxury/ml-showcase`, `recipes/luxury-product-teaser` | `minimal_luxury_lab.py`, helper | ivory light at the top-left corner, deep shadow to the bottom-right (written as `(cx − 150, cy − 150)` → `(cx + 150, cy + 150)`) | highlight below and left of centre, dark rim: lit from underneath | **Fixed**: `[0, 0]` → `[1, 1]` |
| 4 | `su_feature_title` Underline; samples `saas-launch/saas-ui-lab-2`, `saas-launch/saas-ui-showcase-2`, `recipes/saas-feature-launch-30s` | `saas_ui_lab2.py`, helper | accent on the left → violet on the right, along the bar | right direction; the blend covers only the middle 22% (`[0.39]` → `[0.61]`): measured flat `(76, 76, 245)` at x ≤ 902 and flat `(167, 111, 255)` at x ≥ 1022 on a 750–1170 bar | Unchanged (direction right); the doc's wrong "absolute pixels" pitfall corrected |
| 5 | `ml_property_feature` Photo stand-in; sample `minimal-luxury/ml-lab-3` | `minimal_luxury_lab3.py` `grad()`, raw object-local | "vertical warm gradient" (no direction given) | lighter warm brown at the bottom, near black at the top | Unchanged: a stand-in to be replaced; reads as a dark photo either way |
| 6 | `ml_editorial_spread` Photo stand-in; sample `minimal-luxury/ml-lab-3` | same | "diagonal warm gradient" (no direction given) | lighter at the bottom-left, darker at the top-right | Unchanged: as row 5 |
| 7 | `ml_swatch_card` Swatch 1–3, `ml_light_sweep` Gold fill, pattern-lab Gradient shimmer; samples `ml-lab-2`, `ml-lab-3`, `ml-showcase-2`, `motion-patterns/pattern-lab`, `recipes/luxury-product-teaser` | raw object-local, horizontal sheens | a light band crossing left → right | left → right (y does not matter for a horizontal sweep) | Unchanged: correct |
| 8 | Sports showcase Pitch stand-in; sample `sports/sp-showcase` | `sports_showcase.py`, helper | lighter green `#1E6B34` at the top → `#0E3B1C` at the bottom | darker at the top, lighter at the bottom | Unchanged: a footage stand-in in two greens; nobody could tell |
| 9 | Corporate showcase Footage stand-in; sample `corporate-brand/cb-showcase` | `corporate_brand_showcase.py`, helper | navy top-left → teal bottom-right | navy bottom-left → teal top-right (mirrored diagonal) | Unchanged: a stand-in; the mirror does not read |
| 10 | Transitions lab Scene A / Scene B stand-ins, 13 comps; sample `transitions/tx-lab` (not in any template) | `transitions_lab.py`, helper | colour top-left → second colour bottom-right | mirrored diagonal | Unchanged: lab stand-ins only |
| 11 | Recipe and showcase backgrounds: `recipes/quarterly-results`, `quarterly-results-9x16` (`#152036` → `#0B111E`), `saas-feature-launch-30s`, `saas-launch-9x16` (`#1B1B4D` → `#0E0E2A`), `sports-score-update` (`#2E7D32` → `#1B5E20`); `data-viz/dv-showcase-2`, `saas-launch/saas-ui-showcase-2`, `sports/sp-showcase-2` | `recipe_kit.author()` / `showcase2.py`, helper | lighter at the top → darker at the bottom | darker at the top, lighter at the bottom | Unchanged: two close dark tones under the scenes; reads as a plain backdrop either way |
| 12 | `social-media-reels/roi-explainer-reel`, about 100 fills | raw object-local, written y down (older build, not the helper) | top-to-bottom fills and centred radial glows | as intended | Unchanged: correct |
| 13 | `ai/scripts/cc_scene.py` `gradient()` | relay-side helper | object-local | object-local (default `(0, 0.5)` → `(1, 0.5)`) | Unchanged: correct |
| 14 | `fk_blob_frame` Photo stand-in; sample `funky/fk-lab-3` (Funky round 3, merged while this audit ran) | `funky_lab3.py`, helper | orange at the top → pink at the bottom | pink at the top, orange at the bottom, blend 15–85% of the square, seen through a turning blob window | Unchanged: a photo stand-in to be replaced; not touched here (Funky round 3 is another agent's) |
| 15 | Wiki lab projects `wiki/labs/*.carverproj` | cookbook and measurement lab scripts (outside this repo) | — | `cookbook-lab-1` Sky: written `(960, 1080)` → `(960, 0)` with the old helper, meant warm `#F4C27A` at the horizon and blue `#5B8FD9` above; stored `[0.5, 0]` → `[0.5, 1]`, so warm at the top and blue behind the hills. `cookbook-lab-4` Base: mirrored diagonal. The others are object-local and right | Unchanged: lab files of the wiki cookbook work, reported to its user; the Sky is a real upside-down sky |

**Totals:** 15 rows (20 stored templates and samples, the reel, `cc_scene` and the wiki labs). **3 templates fixed**
(`rt_synthwave`, `rt_chrome_title`, `ml_product_frame`) and **8 saved samples fixed** that carry them
(`rt-lab`, `rt-showcase`, `rt-lab-2`, `rt-showcase-2`, `retro-night-promo`, `ml-lab`, `ml-showcase`,
`luxury-product-teaser`). Everything else unchanged.

## How the fixes were made and checked

- Each saved sample was opened in Carvercat 0.1.6 and the packed gradient set with `property.set`
  (`shape.fill.gradient` / `text.fill.gradient`, the same stops, new endpoints), then saved, reopening on the
  same comp. A JSON diff against the old file shows only the endpoint numbers changed.
- The three templates were re-extracted from the fixed lab samples with `comp_to_template.py` and the old id,
  name, note, tags, category, fonts and id prefix. The diff against the old template is the endpoints only.
- Each template was placed into a fresh comp from the Library (`library.place` + `template.apply`): lint 0/0/0.
  Rendered direction after the fix: Synthwave at f60 down the sun's centre `(255, 202, 21)` → `(255, 129, 96)`;
  Chrome at f60 down the letters sky `(172, 233, 255)` → bright `(231, 248, 255)` → step `(95, 48, 135)` →
  magenta `(186, 92, 220)`; Product at f100 along the diagonal `(206, 199, 183)` → `(166, 160, 147)` → `(112, 108, 98)`.
- Master-comp lint of each fixed sample is the same before and after (0/0/0; `rt-lab-2`'s `RT Blinds` keeps its 8 notes).
- `retro_lab2.py` now writes the chrome the right way up. `retro_lab.py` and `minimal_luxury_lab.py` need no
  change: with the fixed helper they write the corrected endpoints.

## A rebuild now differs from some stored samples

The scripts kept their calls, so a fresh rebuild after this fix draws rows 4 and 8–11 as intended (full-length
underline blend, lighter tops, the top-left → bottom-right diagonals), while the stored samples and the
`su_feature_title` template keep the old, harmless look until someone rebuilds them.
