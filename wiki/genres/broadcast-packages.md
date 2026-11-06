---
id: genres/broadcast-packages
title: Broadcast design packages
section: genres
tags: [broadcast, ident, bumper, lower third, strap, package, channel branding, opens, closes, safe area]
styles: [corporate-brand, sports, kinetic-typography, futuristic-hud, glitch]
topics: [genre, brand system, templates]
related: [genres/logo-animation, design/grids-and-layout, workflow/delivery, history/broadcast-graphics-80s-90s, accessibility/readability]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://blog.motionarray.com/learn/motion-design/broadcast-design-terms/, https://keepthescore.com/blog/posts/lower-thirds/, https://blog.frame.io/2017/12/04/create-lower-thirds-titles-that-dont-suck/, https://en.wikipedia.org/wiki/BBC_Two_1991%E2%80%932001_idents, https://www.newscaststudio.com/2023/10/02/abc-owned-graphics-package-2023/2/]
---

# Broadcast design packages

A broadcast package is a coordinated set of graphics that give a channel, show or event one identity:
opens and closes, idents, bumpers, lower thirds (straps), full-frame cards, transitions, and the rules for
using them. It is a system, used by other people, often live, for years.

## The idea

- **Elements**: open (title), close (credits), ident (channel identity between programmes), bumper (short
  break link), lower third / strap (names, places), full-frame (quotes, stats, scores), locator and clock
  bugs, transition (stinger).
- **One system, many uses**: a shared grid, type, palette, easing family and signature move. Every element
  is recognisable from a single frame.
- **Flexible identity**: one fixed brand element placed in endlessly varied situations keeps a channel fresh
  without losing recognition.
- **Built for operators**: templates with editable text, fixed lengths, clear in/out points, and graphics
  that survive any background footage.

## Rules of thumb

- Lower third: animate in 10–15 f, hold for the read (about 2–4 s for a name and role), out 8–12 f.
- Names and roles inside graphics-safe; on-air text never smaller than lint's minimum.
- Bumpers 3–5 s; stingers (transitions) under 1 s with the full cover at the cut.
- Plate behind text so any footage works; test over white, black and busy footage.
- Deliver as templates plus a style guide (sizes, timings, colours, do/don't), and with alpha where an
  editor or vision mixer keys them over pictures.

## Measured in Carvercat

On a 1920 × 1080 comp, `carvercat_look {overlay:["safe"]}` draws an action-safe box at about 3.5% and the
graphics-safe box at 5% `[96, 54, 1824, 1026]` that lint uses; text crossing the inner box gets an
`outside_graphics_safe` note ([grids and layout](../design/grids-and-layout.md)). ProRes 4444 with alpha and
PNG sequences with alpha export headless for keying ([delivery](../workflow/delivery.md)). On a 4K comp the
safe box scales (`[192, 108, 3648, 2052]`) but the minimum text size does not
([event openers](event-openers.md#measured-in-carvercat)).

## Do and don't

- Do design the strap first; it appears most often and sets the system.
- Do write the package's timing rules as numbers (in, hold, out) and keep them identical across elements.
- Don't make templates whose text breaks when names are long; test the longest name.
- Don't animate elements that sit over speech too energetically; viewers read and listen at once.

## Checklist

- [ ] Every element shares grid, type, palette, easing family and signature move.
- [ ] Lower thirds tested with the longest name and role, over light, dark and busy footage.
- [ ] Text inside graphics-safe; lint clean.
- [ ] Alpha deliverables for keyed elements; a style guide with timings.

## In Carvercat

- Packs to start a package from: [Corporate Brand](../../ai/patterns/corporate-brand.md) (`Lower third - two boxes`,
  `Chapter title`, `Brand end card`, `Brand panel wipe`), [Sports](../../ai/patterns/sports.md)
  (`Score bug`, `Player card`, `Head to head stats`), [Kinetic Typography](../../ai/patterns/kinetic-typography.md)
  (`Kinetic lower third`).
- Live match graphics (Sports round 3): `Live score clock` (a running clock with added time; [sp-live-clock](../../ai/patterns/sp-live-clock.md)),
  `Substitution card` ([sp-substitution](../../ai/patterns/sp-substitution.md)), `League table movement` (a row climbs three places;
  [sp-table-move](../../ai/patterns/sp-table-move.md)), `Tournament bracket` ([sp-bracket](../../ai/patterns/sp-bracket.md)) and
  `Fixture list` ([sp-fixtures](../../ai/patterns/sp-fixtures.md)).
- Edgy or gaming channels: [Glitch](../../ai/patterns/glitch.md) round 3, `Scan-line news ticker` (BREAKING tag, LIVE
  chip, headlines crawling at 7 px a frame; [gl-news-ticker](../../ai/patterns/gl-news-ticker.md)), `Hacker alert`
  ([gl-hack-alert](../../ai/patterns/gl-hack-alert.md)) and `Game over screen` (3-2-1 continue;
  [gl-game-over](../../ai/patterns/gl-game-over.md)); all pass `inspect qc` with no flashes.
- Retro broadcast pieces (Retro round 3, 16:9): `70s TV ident` (rainbow rings drawing on twos, a channel number, a dot
  circling one way; [rt-tv-ident](../../ai/patterns/rt-tv-ident.md)) and `Retro weather map` (towns with sun, cloud and rain
  icons and temperature tiles popping on twos; [rt-weather-map](../../ai/patterns/rt-weather-map.md)).
- Templates with controls on their face for operators: `comp_to_template.py`
  ([patterns README](../../ai/patterns/README.md)).
- A brand's motion system (one easing family, durations, signature move): [brand systems](../../ai/references/craft/brand-systems.md).
- Exports with alpha: `export.set {settings:{format:"video", videoCodec:"prores4444", container:"mov", videoAlpha:true}}`.
