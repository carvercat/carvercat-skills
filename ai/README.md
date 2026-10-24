# Carvercat motion skill

This folder is the Carvercat motion-graphics skill: vendor-neutral instructions,
references, a verified pattern library and helper scripts for any AI agent that
can call the Carvercat MCP tools (Claude, GPT/Codex, Gemini and others), or for a
person reading along.

## Start here

- [SKILL.md](SKILL.md) is the entry point. Its front matter (`name`, `description`)
  follows the common agent-skill format, so the folder can be installed as a skill as is.
- [references/INDEX.md](references/INDEX.md) answers "where is X" for the whole skill.
  References are grouped by topic: `craft/` (motion design), `app/` (driving
  Carvercat, scripted builds), `effects/`, `drawing/`, `maps/`, `workflows/`
  (captions and voice-over, RTL, Resolve, export, the job loop) and `known-issues.md`.
- [patterns/](patterns/README.md) is the **Motion Patterns** library: 25 presets and
  5 templates verified on Carvercat 0.0.72, plus recipes. The installable pack is in
  [`../library/templates/motion-patterns/`](../library/templates/motion-patterns/).
- [scripts/](scripts/) holds the Python helpers (MCP client and scene builders,
  motion curves, pattern-pack builder, maps, SFX, voice-over alignment).
- Credits and licences for the ideas behind the craft references: [SOURCES.md](SOURCES.md).

## Status

The references describe Carvercat behaviour as tested on the builds named in each
file. Always confirm against the live app (`carvercat_state`, the MCP resources)
before relying on a detail; [references/known-issues.md](references/known-issues.md)
records known app issues and their workarounds.
