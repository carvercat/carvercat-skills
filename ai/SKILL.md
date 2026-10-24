---
name: carvercat-motion
description: Author, animate, revise, inspect, score, reformat, render or deliver editable native Carvercat motion graphics through its MCP tools - kinetic type, transitions, lower thirds, logo reveals, charts, UI motion, sound design and 9:16 versions - with a verified pattern library and craft rules. Use for app operation and creative graphics, not Carvercat source implementation.
---

# Carvercat motion graphics

**Can't find something? [references/INDEX.md](references/INDEX.md) answers "where is X" for the whole skill (craft, app, effects, drawing, maps, workflows, known issues).**

Works with any agent that can call the Carvercat MCP tools: Claude, GPT/Codex, Gemini, or a person reading along. Nothing here depends on one vendor. Tool names may carry a client prefix (for example `mcp__carvercat__carvercat_run`).

## 0. Before touching anything
- This skill is enough for creative jobs. Locate the installed Carvercat app and this skills folder on the machine you are working on; do not assume a fixed path.
- `carvercat_session` (attach) then `carvercat_state`: verify the build, the open project and the comp before you change anything. `carvercat_list` gives the ids.
- Ask the person not to click in the app while you build: their comp switch redirects your next commands.
- Never clear a user's document to rebuild. Save the editable `.carverproj` at the job's destination.

## 1. Plan like a motion designer (craft)
Read only what the job needs:

| Need | Read |
|---|---|
| Durations, easing, the 12 principles, choreography, pacing to music, anti-patterns | [references/craft/motion-principles.md](references/craft/motion-principles.md) |
| Type scale, read time, entrance styles, emphasis | [references/craft/typography.md](references/craft/typography.md) |
| Which transition, how long, the hand-off at the cut | [references/craft/transitions.md](references/craft/transitions.md) |
| SFX and music: one clip per event, levels, pop/whoosh specs | [references/craft/sound-design.md](references/craft/sound-design.md) |
| 9:16 / social safe areas, converting a 16:9 piece | [references/craft/vertical-and-safe-areas.md](references/craft/vertical-and-safe-areas.md) |

Rules that hold everywhere:
- One hero per scene.
- Supporting items enter on expo-out or decelerate.
- Exits accelerate and take about 70% of the entrance time.
- Stagger neighbours by 3–6 f.
- Every scene has an entrance, some motion in the middle and an exit (never a frozen hold).
- Text holds for at least max(25 f, 10 f per word) + 10 f.

## 2. Build from the pattern library first
[patterns/README.md](patterns/README.md) holds **25 presets and 5 templates, all verified on 0.0.72** with measured overshoot and settle frames, plus recipes for push, zoom-through, card stack and highlight sweep. The pack is `../library/templates/motion-patterns/`. Check it is installed with `library.list {query:"expo"}`; if not, copy the folder into the INSTALLED app's library (Windows: `%LOCALAPPDATA%\carvercat-development\installed\current\library\templates\`; the app loads `library/templates` next to its executable), then `library.reload`. A placed template becomes a nested comp — see the patterns README.
- One object: `preset.apply {name, id}`, for example `Rise - expo`, `Pop - spring`, `Stamp`, `Exit up - accelerate`.
- Text: `Words rise - expo`, `Letters cascade - spring`, `Lines reveal - decelerate`, and others.
- Several objects: `library.place {name, frame}` then `template.apply {id}`. For example `Two-tone wipe`, `Colour iris`, `Lower third - accent bar`, `Logo - stamp reveal`, `Bar chart - grow`.
- A whole multi-beat piece in one comp: [patterns/promo-assembly.md](patterns/promo-assembly.md).
- An exact curve: two keys plus `key.handle`, which reproduces a CSS cubic-bezier exactly ([patterns/custom-curves.md](patterns/custom-curves.md)).
- Springs and bounces: `scripts/motion/curves.py` bakes them into keys.

## 3. Drive the app
**Standing rule:** build and change scenes by editing the `.carverproj` JSON directly, then `edit.open {force:true}`. Use MCP only for the steps the file can't do (measuring text, font checks, look, save, Resolve transfer, live one-line tweaks) and return to the file afterwards. Procedure and fallbacks: [references/app/json-authoring.md](references/app/json-authoring.md#standing-rule-edit-the-project-file-directly).

[references/app/mcp-essentials.md](references/app/mcp-essentials.md) covers the build → look → validate loop, units (**position y up; sizes in fractions of comp width; anchor in half-sizes**), the commands worth knowing, what is not batchable, and the pitfalls that cost hours (`clip.move` overwrites, place_bounds needs a frame, ids restart per comp). The machine-readable catalogue is the app's agent schema, read through the `carvercat://` MCP resources (`commands.json`, `authoring.json`, `workflows.json`, `errors.json`): read the entry before using an unfamiliar command; never guess arguments or generated entry ids.

For scripted, report-driven work, read [references/app/current-artwork-contract.md](references/app/current-artwork-contract.md) and [references/app/creative-toolkit.md](references/app/creative-toolkit.md), and use the maintained scripts (Client + Scene for pixel layout, explicit frame timing, native batching and named revisions). Use `carvercat_authoring` for actual native controls, measured geometry and installed font resolution. Effects, fill/stroke, gradients, colours, transforms, stagger and path trim are in [references/app/creative-controls.md](references/app/creative-controls.md). Treat `native-controls.json` as bounded discovery data and confirm what is live. Older normalized `cc_build` jobs are still supported, but new jobs use `cc_scene`. Measure actual shaped text; choose fonts deliberately, including separate LTR numeric runs in mixed RTL text. Pending plans can be measured through provisional dry-run observations; do not keep dry-run ids.

## 3b. Effects, drawing, maps and whole jobs
| Need | Read |
|---|---|
| Blur, glow (with burn limits), shadow, motion blur, gradients, stroke/trim draw-on, soft edges, text outline, stagger, masks | [references/effects/README.md](references/effects/README.md) |
| Hidden basement params, promoting them, ropes between params | [references/effects/basement-promote-ropes.md](references/effects/basement-promote-ropes.md) |
| All shapes (rectangle, ellipse, star, polygon, path), arranging and grouping | [references/drawing/shapes.md](references/drawing/shapes.md) |
| Characters/objects from parts: anchors as joints, parenting, pivot nulls | [references/drawing/rigging.md](references/drawing/rigging.md) |
| Maps: borders, roads, pins, routes, rings, landmark pop-ups, arrows, zoom in/out | [references/maps/maps.md](references/maps/maps.md) |
| Captions + VO, RTL/Arabic, Resolve hand-off, export, the job loop | [references/workflows/](references/workflows/job-playbook.md) |
| Something misbehaves | [references/known-issues.md](references/known-issues.md) |

Effect rules that hold everywhere: glow amount ≤ 0.8 (0.9 clips, 1.0 burns to white), size sets the halo reach; blur and shadow for depth only on the hero; trim draw-on for lines; soft edge ≤ 0.02 W for UI shapes.

## 4. Check before you say it is done
- **Look** at the entrance, hold and exit (`carvercat_look`). **Measure** with `carvercat_inspect` (`timing`, `curves` for overshoot and settle, `lint`, `expect`, `qc` for flashes). **Validate** layout with `carvercat_authoring mode:"validate"` (`bounds_inside` safe areas, `no_overlap`, `font_exact`).
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
Use `Scene.component` namespaces for revisions that keep child ids; patch only the intended stable ids, properties and channels. After a refusal, stop the work that depends on it. After an unknown outcome, inspect identity and state before any further change; never replay a write or export whose outcome you don't know. Resolve operations need the user's current authorization; without it, author and test natively only. When authorized, verify the actual project, timeline and format, preserve the original edit, and inspect composite samples. The unit of Carvercat work is a comp; a Resolve timeline is separate. For transfer inspection, consolidation, relocation and relinking, read [references/app/media-recovery.md](references/app/media-recovery.md); where cleanup reference coverage is incomplete, keep the files.

Credits and licences for the ideas behind the craft references: [SOURCES.md](SOURCES.md).
