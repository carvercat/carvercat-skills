# Recipes for common briefs

A recipe is a whole short video for a common brief, built **only from verified Library templates**: a shot list with frames, the packs it needs, the timing logic, and a sample project you can open. Every sample was assembled headless with `library.place` + `template.apply` on a master comp with a background (a `carvercat/2` file or one `scene.apply`), then checked with lint, timing, `qc` and a look.

| Brief | Recipe | Length | Sample project |
|---|---|---|---|
| SaaS feature launch | [saas-feature-launch-30s.md](saas-feature-launch-30s.md) | 30 s, 1920 × 1080 | `categories/recipes/saas-feature-launch-30s` |
| Sports score update / goal | [sports-score-update.md](sports-score-update.md) | 14 s, 1920 × 1080 | `categories/recipes/sports-score-update` |
| Social tip reel (9:16) | [tip-reel-9x16.md](tip-reel-9x16.md) | 15.5 s, 1080 × 1920 | `categories/recipes/tip-reel-9x16` |
| Annual report / company film opener | [annual-report-opener.md](annual-report-opener.md) | 22 s, 1920 × 1080 | `categories/recipes/annual-report-opener` |
| Quarterly results in charts | [quarterly-results.md](quarterly-results.md) | 21.5 s, 1920 × 1080 | `categories/recipes/quarterly-results` |
| Luxury product teaser | [luxury-product-teaser.md](luxury-product-teaser.md) | 28 s, 1920 × 1080 | `categories/recipes/luxury-product-teaser` |
| Explainer: how it works | [explainer-how-it-works.md](explainer-how-it-works.md) | 25 s, 1920 × 1080 | `categories/recipes/explainer-how-it-works` |
| Kinetic quote / manifesto reel | [kinetic-quote-reel.md](kinetic-quote-reel.md) | 18.3 s, 1920 × 1080 | `categories/recipes/kinetic-quote-reel` |
| Kids explainer | [kids-explainer.md](kids-explainer.md) | 24.5 s, 1920 × 1080 | `categories/recipes/kids-explainer` |
| Funky sale promo | [funky-sale-promo.md](funky-sale-promo.md) | 18.0 s, 1920 × 1080 | `categories/recipes/funky-sale-promo` |
| HUD tech trailer | [hud-tech-trailer.md](hud-tech-trailer.md) | 23.3 s, 1920 × 1080 | `categories/recipes/hud-tech-trailer` |
| Retro night promo | [retro-night-promo.md](retro-night-promo.md) | 12.8 s, 1920 × 1080 | `categories/recipes/retro-night-promo` |
| Glitch music teaser | [glitch-music-teaser.md](glitch-music-teaser.md) | 14.3 s, 1920 × 1080 | `categories/recipes/glitch-music-teaser` |

## 9:16 versions
| Recipe | 9:16 version | Length |
|---|---|---|
| SaaS feature launch | [saas-launch-9x16.md](saas-launch-9x16.md) | 18.5 s, 1080 × 1920 |
| Quarterly results | [quarterly-results-9x16.md](quarterly-results-9x16.md) | 17.5 s |
| Kinetic quote reel | [kinetic-quote-reel-9x16.md](kinetic-quote-reel-9x16.md) | 17.3 s |

What `comp.format` and placing 16:9 templates into a 9:16 comp do and don't carry over, and what needs a manual re-cut: [vertical-recuts.md](vertical-recuts.md).

## How the samples are built
- `ai/scripts/motion/recipes/recipe_kit.py` makes the master comp (one "Background" rectangle, solid or a top-to-bottom gradient; sizes in px, length in frames), then places each shot: `library.place {name, frame, track}` and `template.apply {id}` on the returned id (check with `carve.preflight` before a send). Transitions go on a higher track, centred on the cut. `install_packs` copies the packs from `library/templates/` of this repo into the user Library (`library.folder`) and runs `library.reload`.
- **Two routes make the master, and the rest is the same.** *File route (default, the 23 Oct rule):* `ai/scripts/cc_project.py` writes a project file in the stored format `carvercat/2` (px with y down, frames, CSS-style easing, `color(srgb ...)` colours), then `edit.open {path, force: true}`. *Apply route (`RECIPE_ROUTE=apply`, the shorter one for a master this small):* one `scene.apply` document into a fresh project, no file until `edit.save`. Both read back identically through `scene.get`; `edit.save` always writes `carvercat/2`. An older file in the v1 format still opens, and the first save keeps the original as `<file>.v1.bak`.
- Long holds get a slow push: `key.set {id, key: "scale", value, atComp: <comp frame>, ease: "linear"}` at the end frame first, then at the start frame (an `ease` shapes the segment that leaves its key, and a key with nothing after it keeps none: keyed start first, the push eases out and lint flags the last frames).
- `scale` is absolute. `template.apply` fits a 16:9 template into a 9:16 comp at scale 0.5625; a zoom of 2.4 on its content means `scale` 0.5625 x 2.4 = 1.35 (the builders read the fitted scale and multiply).
- Run headless with isolated folders: `CARVERCAT_EXE`, `CARVERCAT_RESOURCE_ROOT`, `CARVERCAT_STATE`, `RECIPE_LAB` (see the script header), then `ai/scripts/motion/recipes/verify_recipes.py` builds every recipe on both routes and reads each back with `scene.get`. Never `--connect` to someone's running app.

## Rules every recipe follows
- Each scene is one template; scenes butt-join on the frame the previous one ends.
- A transition is placed so its full-cover window spans the cut (each transition doc gives its cut frame).
- The CTA or result lands last and holds at least 2 s.
- Master lint 0 errors / 0 warnings / 0 notes. `qc` notes holds of 2 s or more as "freeze", which is fine for a hold; the docs list them.
- `qc` at 240 px does not see thin lines, slow drifts or dark grounds (the luxury teaser reads as black and frozen to it); judge those styles with `carvercat_look`.

**Builders re-verified on Carvercat 0.1.8, 2026-11-04** (both routes; samples verified 0.1.6, 2026-10-27)
