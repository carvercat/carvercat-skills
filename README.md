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
  references/                         craft, app, effects, drawing, maps, workflows, known issues
  patterns/                           docs for the Motion Patterns presets and templates
  scripts/                            Python helpers (MCP client, scene builder, curves, maps, SFX, VO)
library/templates/motion-patterns/    the Motion Patterns pack: 25 presets + 5 templates, with thumbnails
categories/<category>/<slug>/         sample .carverproj projects, each with a card.json
INDEX.json  INDEX.md                  generated index of the sample projects
tools/                                index builder, link checker, skill installer
```

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

## Install the Motion Patterns pack

Copy `library/templates/motion-patterns/` into the installed app's
`library/templates/` folder, then run `library.reload` (or restart the app).
Details are in [ai/patterns/README.md](ai/patterns/README.md).

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

## Contact

Questions, bugs and ideas: [hello@carvercat.com](mailto:hello@carvercat.com) ·
[carvercat.com](https://carvercat.com)

## Licence

Not chosen yet. See [LICENSE-TODO.md](LICENSE-TODO.md).
