# Carvercat AI skill

This folder is reserved for Carvercat's official, vendor-neutral AI skill and
machine-readable agent resources.

It lives in the `carvercat-skills` repository because the skill is a maintained
product resource rather than a website-page implementation. A later publishing
step can expose selected files from here at stable public URLs such as
`https://carvercat.com/ai/skill.md`.

## Planned contents

- `skill.md` — concise vendor-neutral instructions and discovery metadata.
- `manifest.json` — version, canonical URLs, hashes and related resources.
- `openapi.json` — HTTP API description when a public API exists.
- `llms.txt` — short map for website-reading agents.
- `references/` — commands, workflows, conventions and MCP guidance loaded only
  when relevant.
- `versions/` — immutable published releases after versioning is introduced.

## Current status

The official public skill contract is not published yet. Internal working tools and the maintained SKILL.md entrypoint below are usable. Do not link clients to it until the skill contract, permission boundaries,
versioning and publication route have been reviewed.


## Start here for agents

[SKILL.md](SKILL.md) is the entry point; [references/INDEX.md](references/INDEX.md) finds any topic. References are grouped by topic: `craft/` (motion design), `app/` (driving Carvercat, scripted builds), `effects/`, `drawing/`, `maps/`, `workflows/` (captions/VO, RTL, Resolve, export, job loop) and `known-issues.md`. Reusable code: [scripts/](scripts/). Still internal working guidance, not a published skill.

## Design units (Carvercat 0.1.8)

Every instruction, table and example here is in design units: px from the top-left with y down, CSS colours and easing, `fontSize` px, `scene.apply`, selectors, helpers and `carve.preflight` ([references/app/design-units.md](references/app/design-units.md)). The Python toolkit in [scripts/](scripts/) (`cc_client`, `cc_scene`, `cc_build`, `cc_components`) builds scenes in those units; `scripts/verify_examples.py` runs every call sequence in the guides, and `scripts/test_cc_toolkit.py` the toolkit, against a headless Carvercat (`CARVERCAT_EXE`, `CARVERCAT_RESOURCE_ROOT`). Project files are now stored as `carvercat/2` (design units; spec: the app's `carvercat://schema/scene` resource): every save writes it, and an older v1 file still opens. `scripts/cc_project.py` writes a `carvercat/2` project directly and the recipe builders in `scripts/motion/recipes/` use it ([recipes](recipes/README.md#how-the-samples-are-built)); the older pattern-pack and lab scripts under `scripts/motion/` still write v1 files, which load. Old names are accepted for one release and are listed once in design-units.md.

## Current creative toolkit (10 October 2026; now in design units)

Start with [SKILL.md](SKILL.md) and [creative-toolkit.md](references/app/creative-toolkit.md). These are usable internal agent instructions and tested helpers; public publication/version hosting is still a separate step. New creative builds use cc_scene and current native batching. Historical job references remain evidence, not universal current API contracts.

## Motion craft and pattern library (20 October 2026)

[SKILL.md](SKILL.md) now carries the motion-design layer: craft references (principles, typography, transitions, sound, vertical), the **Motion Patterns** library ([patterns/](patterns/README.md): 25 presets and 5 templates verified on Carvercat 0.0.72, plus recipes) and the motion scripts in [scripts/motion/](scripts/motion/). It is vendor-neutral, for any MCP-capable agent. Credits: [SOURCES.md](SOURCES.md).
