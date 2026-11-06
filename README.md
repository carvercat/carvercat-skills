# Carvercat skills

Agent skills and sample projects for [Carvercat](https://carvercat.com), a free,
agent-ready native motion-graphics editor.

Carvercat exposes its editor to AI agents over MCP (Model Context Protocol). This
repository teaches an agent to use it well: how to plan motion like a designer,
drive the app safely, build from a verified pattern library, and check the result
before calling it done.

## What's inside

```
ai/                                   the motion skill (start at ai/SKILL.md)
  SKILL.md                            entry point for agents
  references/                         craft, app (incl. design-units.md), effects, drawing, maps, workflows, known issues
  patterns/                           docs for every preset and template pack
  recipes/                            whole short videos for common briefs, built from the packs
  scripts/                            Python helpers (MCP client, scene builder, project writer, curves, maps, SFX, VO)
wiki/                                 the motion-design wiki: principles, techniques, genres, cookbook, labs
library/templates/<pack>/             the preset and template packs (Motion Patterns plus 14 style packs), with thumbnails
categories/<category>/<slug>/         sample .carverproj projects, each with a card.json
INDEX.json  INDEX.md                  generated index of the sample projects
tools/                                index builder, link checker, skill installer
```

Everything is written for Carvercat 0.1.8 in its design units: pixels from the top-left with y down,
CSS colours and easing, frames or seconds for time. Carvercat 0.1.8 saves projects as `carvercat/2`;
files saved in 0.1.8 do not open in 0.1.7. Older files still open in 0.1.8.

## Use the skill with an agent

You need Carvercat installed with MCP enabled, and an agent that can call MCP tools.

**Claude Code / Claude desktop**: copy the `ai/` folder into your skills folder as
`carvercat-motion`:

```bash
python tools/install_local_skill.py ~/.claude/skills/carvercat-motion
```

**Codex and other agents**: run the same script with that agent's skills folder
(the default is `~/.codex/skills/carvercat-motion`), or point the agent at
`ai/SKILL.md` and let it read the references it needs.

Then ask for motion work in plain words, for example "add a lower third for Alex
Morgan, Senior Motion Designer, at 2 seconds" or "make a 9:16 version of this comp".
The skill tells the agent which reference to read for each part of the job.

## Install a pack

Copy a pack folder from `library/templates/` (for example `motion-patterns/`) into the
Library folder of the app, then run `library.reload` (or restart the app).
Details are in [ai/patterns/README.md](ai/patterns/README.md#installing-a-pack).

## Sample projects

Each sample project has a `card.json` that says what it contains, when to use it,
what to edit after copying, and known traps. Agents should read the card, not the
whole project file.

1. Read `INDEX.json`: one line per category and per project.
2. Read `categories/<category>/INDEX.json` to narrow down.
3. Read the project's `card.json`, then copy `project.carverproj` and any `media/`.

A project's id is `<category>/<slug>` and never changes. `.carverproj` files can
store absolute media paths from the machine that made them; after copying, relink
them using `media/MANIFEST.json` when the project has one.

### Adding a project

1. Create `categories/<category>/<slug>/` with `project.carverproj` and `card.json`.
2. Put referenced media in `media/`, with a `MANIFEST.json` mapping each path stored
   in the project to the file here. Only include media you have the right to share.
3. Run `node tools/build_index.mjs` to regenerate the indexes.

## Checks

```bash
node tools/build_index.mjs --check
```

```bash
python tools/check_links.py
```

```bash
python wiki/tools/wiki_index.py
```

## Contact

Questions, bugs and ideas: [hello@carvercat.com](mailto:hello@carvercat.com) ·
[carvercat.com](https://carvercat.com)

## Licence

Free to use for personal and professional or paid work, including client projects.
Redistributing or copying the skills elsewhere is not allowed. See [LICENSE](LICENSE).
Rethink Sans ships under the SIL Open Font License ([OFL.txt](ai/scripts/motion/json_author/OFL.txt)).
