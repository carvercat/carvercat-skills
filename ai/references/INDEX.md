# Carvercat motion — find anything

One index for the whole skill. Find your question, open that file, read only that. Paths are relative to `ai/references/` unless they start with `../`.

## Layout
| Folder | Holds |
|---|---|
| [craft/](craft/) | Motion-design judgment: timing, easing, type, transitions, sound, 9:16, review |
| [app/](app/) | Driving Carvercat: MCP loop, units, batching, scripted builds, API quirks, controls |
| [effects/](effects/README.md) | One page per effect, with verified settings and limits |
| [drawing/](drawing/) | Shapes, arranging, characters/objects, anchors, parenting, rigs |
| [maps/](maps/maps.md) | Map animation from real geography: borders, roads, pins, routes, pop-ups, zoom |
| [workflows/](workflows/) | Whole jobs: captions + voice-over, RTL/Arabic, Resolve hand-off, export, the job loop |
| [known-issues.md](known-issues.md) | Every known app issue (KI-###) and feature request (FR-###) with workarounds |
| [../patterns/](../patterns/README.md) | The verified Motion Patterns library: 25 presets, 5 templates, recipes |
| [../scripts/](../scripts/) | Python tools: client/scene builders, motion curves, pattern pack, maps, SFX, VO alignment |

## Find by question

### Starting and driving the app
| Question | Read |
|---|---|
| How do I connect, check the build, list ids, and run the build → look → validate loop? | [app/mcp-essentials.md](app/mcp-essentials.md) |
| What units are positions, sizes, anchors, colours, text sizes in? | [app/mcp-essentials.md](app/mcp-essentials.md) §units |
| Which commands can't go in a batch? Why did my batch roll back? | [app/mcp-essentials.md](app/mcp-essentials.md), [known-issues.md](known-issues.md) |
| Generate a whole film straight into the project JSON (units, nested keys, anchor, continuous subscenes) | [app/json-authoring.md](app/json-authoring.md), `../scripts/motion/json_author/` |
| No MCP tools in this chat / big scripted build | [app/programmatic-build-relay.md](app/programmatic-build-relay.md), [app/creative-toolkit.md](app/creative-toolkit.md) |
| Typed, report-driven authoring and native acceptance | [app/current-artwork-contract.md](app/current-artwork-contract.md) |
| Odd API behaviour, legacy builds, Resolve scripting quirks | [app/api-gotchas.md](app/api-gotchas.md) |
| Which native controls exist (machine-readable) | [app/native-controls.json](app/native-controls.json), table: [effects/PARAMETERS.md](effects/PARAMETERS.md) |
| Canvas tools, navigator, workspace panels | [app/canvas-tools.md](app/canvas-tools.md), [app/project-navigator.md](app/project-navigator.md) |
| The app lags / audio starves / duplicate clip ids | [app/performance.md](app/performance.md) |
| Media went offline, relink or consolidate | [app/media-recovery.md](app/media-recovery.md) |

### Motion craft
| Question | Read |
|---|---|
| How long should this move be? Which easing? Exact cubic-bezier curves? | [craft/motion-principles.md](craft/motion-principles.md), [../patterns/custom-curves.md](../patterns/custom-curves.md) |
| Springs, bounces, overshoot baked into keys | [../patterns/custom-curves.md](../patterns/custom-curves.md), `../scripts/motion/curves.py` |
| Type sizes, read time, text entrances, emphasis | [craft/typography.md](craft/typography.md) |
| Which transition, how long, what happens at the cut | [craft/transitions.md](craft/transitions.md) |
| SFX per event, levels, music beds | [craft/sound-design.md](craft/sound-design.md) |
| 9:16 and social safe areas, converting 16:9 | [craft/vertical-and-safe-areas.md](craft/vertical-and-safe-areas.md) |
| Is it done? | [craft/review-checklist.md](craft/review-checklist.md) |

### Ready-made motion
| Question | Read |
|---|---|
| Is there a preset/template for this (rise, pop, stamp, exit, text cascades, wipes, iris, lower third, logo, bar chart)? | [../patterns/README.md](../patterns/README.md) |
| Push / zoom-through / card stack / highlight sweep recipes | [../patterns/](../patterns/README.md) |
| A whole multi-beat promo in one comp | [../patterns/promo-assembly.md](../patterns/promo-assembly.md) |
| Turn my comp into a reusable template with controls on its face | [../patterns/README.md](../patterns/README.md) §template, `../scripts/motion/comp_to_template.py` |

### Effects and paint
| Question | Read |
|---|---|
| How effects are added, aliased, keyed, promoted | [effects/README.md](effects/README.md) |
| Blur in/out, defocus | [effects/blur.md](effects/blur.md) |
| Glow without burning the element (limits, halo reach) | [effects/glow.md](effects/glow.md) |
| Drop shadow / lift | [effects/shadow.md](effects/shadow.md) |
| Motion blur | [effects/motion-blur.md](effects/motion-blur.md) |
| Fill, linear/radial gradients, shimmer | [effects/fill-and-gradients.md](effects/fill-and-gradients.md) |
| Stroke, dashes, caps, draw-on (trim) | [effects/stroke-and-trim.md](effects/stroke-and-trim.md) |
| Soft / feathered / smooth edges of shapes | [effects/soft-edge.md](effects/soft-edge.md) |
| Outlined text, text paint | [effects/text-paint.md](effects/text-paint.md) |
| Word/character stagger | [effects/stagger.md](effects/stagger.md) |
| Blend modes, masks, wipes | [effects/compositing-and-masks.md](effects/compositing-and-masks.md) |
| Hidden (basement) params, promoting them, ropes between params | [effects/basement-promote-ropes.md](effects/basement-promote-ropes.md) |

### Drawing, objects, characters
| Question | Read |
|---|---|
| Rectangle, ellipse, star, polygon, paths: sizes, corners, recipes, arranging | [drawing/shapes.md](drawing/shapes.md) |
| Draw a character/object from parts, group it, set anchors/pivots, parent and animate | [drawing/rigging.md](drawing/rigging.md) |
| Recreate a UI pointer or switch for a tutorial | [drawing/shapes.md](drawing/shapes.md) §UI |

### Maps
| Question | Read |
|---|---|
| Country/emirate/city maps from real data, projections, licences | [maps/maps.md](maps/maps.md) §1 |
| Road draw-on, pins, routes, catchment rings, landmark pop-ups, arrows | [maps/maps.md](maps/maps.md) §3–3b, `../scripts/maps/map_overlay.py` |
| Zoom in / zoom out on a location | [maps/maps.md](maps/maps.md) §3b camera |

### Whole jobs
| Question | Read |
|---|---|
| The generic job loop, permissions, revisions, hand-over | [workflows/job-playbook.md](workflows/job-playbook.md) |
| Captions timed to voice-over, retiming, multi-section jobs | [workflows/captions-and-voiceover.md](workflows/captions-and-voiceover.md) |
| Arabic / RTL text, fonts, mixed numbers | [workflows/rtl-and-arabic.md](workflows/rtl-and-arabic.md) |
| Sending to DaVinci Resolve (PNG, Fusion, stills, audio) | [workflows/resolve-handoff.md](workflows/resolve-handoff.md) |
| Export settings, async export jobs, verifying outputs | [workflows/export-and-delivery.md](workflows/export-and-delivery.md) |

## Conventions for adding knowledge
- Put a finding where an agent will look for it (the topic file), not in a dated or client-named report. No client or project names in references.
- New app bug or limit → a `KI-###` row in [known-issues.md](known-issues.md); link it from the topic file.
- Mark what you verified and on which build ("verified 0.0.72"). Unverified ideas say so.
- Add a row to this index for any new file. Run `node tools/build_index.mjs --check` and the link check (`python tools/check_links.py`) before committing.
