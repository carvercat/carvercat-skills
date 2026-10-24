# Licence: to be chosen before publishing

This repository has no licence yet. Without one, others may read it but have no
right to copy, modify or redistribute it. Pick one option, add the matching
`LICENSE` file (and `LICENSE-docs` if splitting), update the README's Licence
section and the `license` field in each `card.json`, then delete this file.

| Option | Covers | Fits when |
|---|---|---|
| **MIT** | everything | Simplest permissive licence; anyone can reuse the skill, scripts and pack with attribution. |
| **Apache-2.0** | everything | Permissive like MIT, plus an explicit patent grant and a NOTICE convention. Several sources credited in `ai/SOURCES.md` are Apache-2.0. |
| **MIT or Apache-2.0 for code + CC BY 4.0 for docs and samples** | split | Scripts and tools under a software licence; Markdown references, pattern docs, presets/templates, thumbnails and sample projects under CC BY 4.0 (attribution required). |

Items with their own terms, whatever is chosen:

- `ai/scripts/motion/json_author/RethinkSans.ttf`: Rethink Sans, SIL Open Font
  License 1.1. The OFL text should ship next to the font (for example `OFL.txt`).
- `ai/scripts/maps/data/*.json`: derived from public geographic data; confirm the
  source and its licence (see `ai/references/maps/maps.md` §1) before publishing.
- `ai/SOURCES.md` lists the outside material the references learned from; it is
  credited there and no text or code was copied.
