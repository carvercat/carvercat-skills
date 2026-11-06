# Agent entry point

Motion-graphics work in Carvercat: start at [ai/SKILL.md](ai/SKILL.md), then
[ai/references/INDEX.md](ai/references/INDEX.md) to find a topic. Every call and value is in
the app's design units: [ai/references/app/design-units.md](ai/references/app/design-units.md).
The verified preset and template packs are in `library/templates/`, documented in `ai/patterns/`;
whole-video recipes are in `ai/recipes/`; the motion-design wiki is in `wiki/`.

Sample projects: read `INDEX.json`, then a project's `card.json`, before opening
any `.carverproj`. How to add one is in [README.md](README.md).

Before proposing a change to this repository, run `node tools/build_index.mjs --check`,
`python tools/check_links.py` and `python wiki/tools/wiki_index.py`.
