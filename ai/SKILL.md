---
name: carvercat-motion
description: Author, animate, revise, inspect, score, reformat, render or deliver editable native Carvercat motion graphics through its MCP tools - kinetic type, transitions, lower thirds, logo reveals, charts, UI motion, sound design and 9:16 versions - with a verified pattern library and craft rules. Use for app operation and creative graphics, not Carvercat source implementation.
---

# Carvercat motion graphics

**Can't find something? [references/INDEX.md](references/INDEX.md) answers "where is X" for the whole skill (craft, app, effects, drawing, maps, workflows, known issues).**

Works with any agent that can call the Carvercat MCP tools: Claude, GPT/Codex, Gemini, or a person reading along. Nothing here depends on one vendor. Tool names may carry a client prefix (for example `mcp__carvercat__carvercat_run`).

## 0. Units and the new surface (read this first)
Everything you write is in **design units**: px from the frame's top-left with y down, degrees clockwise, CSS colours and easing, `fontSize` px, times as frames, `"1.5s"` or `"500ms"`. Build a whole scene in one validated call (`scene.apply`, dry run first), select objects with CSS-like selectors, use the helpers (`layout.*`, `text.fit`, `motion.apply`, `measure.*`) and run `carve.preflight {host}` before any send. Guide: [references/app/design-units.md](references/app/design-units.md). Old names still work for one release and are listed there once; do not write them.

## 0b. Before touching anything
- Locate the installed Carvercat app on this machine and use this skill's folder as installed; for creative jobs this skill is enough. Do not use a fixed historical path.
- `carvercat_session` (attach) then `carvercat_state`: verify the build, the open project and the comp before you change anything. `carvercat_list` gives the ids.
- Ask the person not to click in the app while you build: their comp switch redirects your next commands.
- Never clear a user's document to rebuild. Save the editable `.carverproj` at the job's destination.

## 1. Plan like a motion designer (craft)
Read only what the job needs:

| Need | Read |
|---|---|
| Durations, easing, the 12 principles, choreography, pacing to music, anti-patterns | [references/craft/motion-principles.md](references/craft/motion-principles.md); one page per principle in [references/craft/principles/](references/craft/principles/README.md) |
| Type scale, read time, entrance styles, emphasis; measured tracking, leading and lint thresholds | [references/craft/typography.md](references/craft/typography.md) |
| Which transition, how long, the hand-off at the cut | [references/craft/transitions.md](references/craft/transitions.md) |
| SFX and music: one clip per event, levels, pop/whoosh specs | [references/craft/sound-design.md](references/craft/sound-design.md) |
| 9:16 / social safe areas, converting a 16:9 piece | [references/craft/vertical-and-safe-areas.md](references/craft/vertical-and-safe-areas.md) |
| Palette roles, contrast, gradients, colour values | [references/craft/colour.md](references/craft/colour.md) |
| A brand's motion system: easing family, durations, signature move, brand packs | [references/craft/brand-systems.md](references/craft/brand-systems.md) |
| Focal point, reading order, grids, hierarchy, safe areas | [references/craft/composition-and-layout.md](references/craft/composition-and-layout.md) |
| Reading a brief: facts, frame budget, style, recipe | [references/craft/reading-a-brief.md](references/craft/reading-a-brief.md) |
| Which style pack for a brief | [references/craft/style-families.md](references/craft/style-families.md) |
| Measured frame counts per style; the style's review list | [references/craft/timing-by-style.md](references/craft/timing-by-style.md), [references/craft/review-by-style.md](references/craft/review-by-style.md) |
| Why a move works: the 12 principles and beyond, design fundamentals, techniques, genres, timing, workflow, accessibility, history (each page ends with how to do it in Carvercat) | [../wiki/README.md](../wiki/README.md), machine index [../wiki/index.json](../wiki/index.json) |

Rules that hold everywhere:
- One hero per scene.
- Supporting items enter on expo-out or decelerate.
- Exits accelerate and take about 70% of the entrance time.
- Stagger neighbours by 3–6 f.
- Every scene has an entrance, some motion in the middle and an exit (never a frozen hold).
- Text holds for at least max(25 f, 10 f per word) + 10 f. Carvercat's lint asks for 17 characters a second (spaces not counted), at least 25 fully opaque frames.

## 2. Build from the pattern library first
[patterns/README.md](patterns/README.md) holds **25 presets and 5 templates, all verified on 0.0.72** with measured overshoot and settle frames, plus recipes for push, zoom-through, card stack and highlight sweep. The pack is `../library/templates/motion-patterns/`. Check it is installed with `library.list {query:"expo"}`; if not, install it into the user Library folder (Help > Library Folder or `library.folder`, copy into `templates/`, then `library.reload`; needs Carvercat 0.1.8+; see [patterns/README.md](patterns/README.md#installing-a-pack)). Before 0.1.8 an installed app cannot load it. A placed template becomes a nested comp — see the patterns README.
- One object: `preset.apply {name, id}`, for example `Rise - expo`, `Pop - spring`, `Stamp`, `Exit up - accelerate`.
- Text: `Words rise - expo`, `Letters cascade - spring`, `Lines reveal - decelerate`, and others.
- Several objects: `library.place {name, frame}` then `template.apply {id}`. For example `Two-tone wipe`, `Colour iris`, `Lower third - accent bar`, `Logo - stamp reveal`, `Bar chart - grow`.
- A whole multi-beat piece in one comp: [patterns/promo-assembly.md](patterns/promo-assembly.md).
- Style packs (same install as Motion Patterns): [SaaS UI](patterns/saas-ui.md), [Kinetic Typography](patterns/kinetic-typography.md), [Data Viz](patterns/data-viz.md), [Corporate Brand](patterns/corporate-brand.md), [Minimal Luxury](patterns/minimal-luxury.md), [Social Short-form 9:16](patterns/social-short-form.md), [Cartoon Bounce](patterns/cartoon-bounce.md), [Funky](patterns/funky.md), [Futuristic HUD](patterns/futuristic-hud.md), [Retro](patterns/retro.md), [Glitch](patterns/glitch.md), [Sports](patterns/sports.md), [Explainer](patterns/explainer.md); pick one with [references/craft/style-families.md](references/craft/style-families.md). They need Rethink Sans installed (text cannot use the app-bundled fonts, KI-136). Each has a lab and a showcase project under `../categories/`.
- Recipes for common briefs (SaaS launch, sports score update, 9:16 tip reel, annual-report opener, quarterly results, luxury teaser, explainer lesson, kinetic quote reel, kids explainer, sale promo, tech trailer, retro night, music teaser): shot lists with frames and verified sample projects built only from Library templates, in [recipes/README.md](recipes/README.md).
- An exact curve: `ease: "cubic-bezier(a, b, c, d)"` on the key that leaves ([patterns/custom-curves.md](patterns/custom-curves.md)).
- Springs and bounces: `scripts/motion/curves.py` bakes them into keys.

## 3. Drive the app
**Standing rule (23 Oct 2026):** build and change scenes by editing the `.carverproj` JSON directly, then `edit.open {force:true}`. A whole scene also goes over MCP in one validated, atomic `scene.apply`; the project file is now `carvercat/2` (px, y down, frames; every save writes it, v1 files still open), and the JSON route below describes the older v1 shape (fractions, y up) that `json_author/cc.py` writes and the app still loads; for a new generator write `carvercat/2` ([cc_project.py](scripts/cc_project.py), as the recipe builders do). Use MCP for the steps the file can't do (measuring text, look, save, Resolve transfer, live tweaks). Procedure and fallbacks: [references/app/json-authoring.md](references/app/json-authoring.md#standing-rule-user-23-oct-2026-edit-the-project-file-directly).

[references/app/design-units.md](references/app/design-units.md) is the working guide: units, `scene.apply`, selectors, `anim.set` (tweens, easing, stagger), effects in CSS terms, helpers, headless notes. [references/app/mcp-essentials.md](references/app/mcp-essentials.md) covers the build -> look -> check loop, the commands worth knowing and the pitfalls that cost hours (`clip.move` overwrites, ids restart per comp). The machine-readable catalogue is `carvercat://schema/design`, `carvercat://schema/commands` and `carvercat://schema/scene` (the app repo's `schema/agent/json-schema/`): read the entry before using an unfamiliar key; never guess arguments or generated entry ids.

For scripted work use the maintained Python scripts: `ai/scripts/cc_client.py` + `cc_scene.py` ([references/app/creative-toolkit.md](references/app/creative-toolkit.md)); the app has its own Python helper too (`carvercat_py`). Effects, fill/stroke, gradients, colours, transforms, stagger and path trim are in [references/app/creative-controls.md](references/app/creative-controls.md). Pending plans can be checked with `scene.apply {dry_run: true}` and `measure.*`; nothing is stored beside the document. Measure actual shaped text; choose fonts deliberately, including separate LTR numeric runs in mixed RTL text. Every example in the guides is run by `ai/scripts/verify_examples.py` against a headless Carvercat.

## 3b. Effects, drawing, maps and whole jobs
| Need | Read |
|---|---|
| Blur, glow (with burn limits), shadow, motion blur, gradients, stroke/trim draw-on, soft edges and mask feather, text outline, stagger, masks | [references/effects/README.md](references/effects/README.md) |
| Hidden basement params, promoting them, ropes between params | [references/effects/basement-promote-ropes.md](references/effects/basement-promote-ropes.md) |
| All shapes (rectangle, ellipse, star, polygon, path), arranging and grouping | [references/drawing/shapes.md](references/drawing/shapes.md) |
| Characters/objects from parts: anchors as joints, parenting, the null object (`object.new {kind: "null"}`) as a pivot or handle | [references/drawing/rigging.md](references/drawing/rigging.md) |
| Maps: borders, roads, pins, routes, rings, landmark pop-ups, arrows, zoom in/out | [references/maps/maps.md](references/maps/maps.md) |
| Captions + VO, RTL/Arabic, Resolve hand-off, export, the job loop | [references/workflows/](references/workflows/job-playbook.md) |
| Something misbehaves | [references/known-issues.md](references/known-issues.md) |

Effect rules that hold everywhere: `glow` strength ≤ 0.8 (0.9 clips, 1.0 burns to white), the radius sets the halo reach; blur and shadow for depth only on the hero; trim draw-on for lines; `softEdge` of 2 to 6 px for UI shapes, 160 to 320 px for ambient light ([references/effects/soft-edge.md](references/effects/soft-edge.md), with the feathered mask reveal).

## 4. Check before you say it is done
- **Look** at the entrance, hold and exit (`carvercat_look`). **Measure** with `carvercat_inspect` (`timing`, `curves` for overshoot and settle, `lint`, `expect`, `qc` for flashes) and the no-render helpers (`measure.boxes`, `measure.overlaps {within: "safe"}`, `measure.contrast`). **Preflight** with `carve.preflight {host}` before a send.
- Walk [references/craft/review-checklist.md](references/craft/review-checklist.md): story, timing, text, UI, transitions, look, sound, hygiene.
- Build one representative comp first, review it, then expand. Recipes are starting points: adapt the hierarchy, imagery and timing to the brief and footage. Safe bounds do not replace visual judgment.
- Lag or audio starving: [references/app/performance.md](references/app/performance.md).

## 5. Tools that live outside the app (`scripts/motion/`, Python 3, standard library + ffmpeg)
- `vo_align.py`: voice-over → word and line frames.
- `sfx_kit.py` / `sfx_render.py`: synthesised SFX (pop, whoosh-hit, tick, impact...) → one WAV per cue.
- `music_bed.py`: a bed that fits the cut; `mix_check.py`: stem LUFS and a reference mix.
- `reformat.py`: a 16:9 project → 9:16 comps.
- `carverproj.py`: project JSON helpers (ids, keys).
- `build_pattern_pack.py` / `comp_to_template.py`: regenerate the pack.
- `effects_param_tables.py`: regenerate the effect parameter table.
- `../maps/geo_paths.py` / `../maps/map_overlay.py`: real geography → paths; explainer overlay (pins, rings, routes, cards, arrows).

## 6. Safety and delivery
Use scene ids (and `Scene.component` namespaces) so a revision updates the same objects: apply the same document again and only differences change. After a refusal, stop the work that depends on it. After an unknown outcome, inspect identity and state before any further change; never replay a write or export whose outcome you don't know. Resolve operations need the user's current authorization; without it, author and test natively only. When authorized, verify the actual project, timeline and format, preserve the original edit, and inspect composite samples. The unit of Carvercat work is a comp; a Resolve timeline is separate. For transfer inspection, consolidation, relocation and relinking, read [references/app/media-recovery.md](references/app/media-recovery.md); where cleanup reference coverage is incomplete, keep the files.

Credits and licences for the ideas behind the craft references: [SOURCES.md](SOURCES.md).
