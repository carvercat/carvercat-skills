# The Carvercat motion-design wiki

Motion-design knowledge for designing in **Carvercat**: principles, design fundamentals, techniques, genres,
timing, workflow, accessibility and history. Every page is written in our own words for Carvercat and ends
with an **In Carvercat** section naming the real objects, parameters, presets and templates that achieve it.
Values on pages marked `verified` were measured in Carvercat 0.1.6 (rev 1105) with
`carvercat_inspect`, `carvercat_look` and `carvercat_authoring`; the lab projects are in [labs/](labs/README.md). Newer pages
say `design/1` and were measured on a headless Carvercat 0.1.8 build. **Every call and value on every page is in
design units** (below); the measurements are unchanged, and each value the lab projects store was converted with the app's own
formulas and read back with `scene.get`.

## Design units on every page

Calls use the design keys of `carvercat://schema/design`:

| Quantity | Design unit | Old (accepted for one release, named only in each page's "old names" note) |
|---|---|---|
| Position, size | `x`, `y` = the top-left of the layout box, px, y down; `width`, `height` in px or `%` | `center`, centre as a fraction with y up, sizes as fractions of the width |
| Turn | `rotate` in degrees, **clockwise**; `"45deg"` | `angle`, `transform.placement.rotation`, counter-clockwise positive |
| Scale | `scale` 1.2 or `"120%"`; `[x, 1]` for one axis | `size`, `transform.placement.scale` |
| Pivot | `transformOrigin` as in CSS: `"0% 50%"` left edge, `"50% 100%"` bottom edge | `anchor` in half-sizes (`[-1, 0]`, `[0, -1]`) |
| Opacity | `opacity` 0 to 1 or `"50%"` | `blend`, `transform.placement.opacity` |
| Colour | CSS colours as displayed: `"#F2B03C"`, `rgb()`, `hsl()`, gradients as `linear-gradient(...)` | linear arrays |
| Text | `fontSize` px (a true em), `letterSpacing` px / pt / em, `lineHeight` a multiple or a length | `text.font.size` (a fraction), `tracking`, `lineSpacing` |
| Shape | `borderRadius` px or % (to half the short side), `sides`, `points`, `innerRadius` %, `strokeWidth` px, `strokeDasharray`, `trimStart` / `trimEnd` / `trimOffset` in % | `cornerRadius`, widths as fractions of the frame width, `shape.stroke.*`, `trim.*` as 0 to 1 |
| Soft edge | `softEdge` (one per shape; `strokeSoftEdge` is its old name), mask `feather` in px: the visible 10-90% ramp ([page](techniques/soft-edge-and-feather.md)) | `shape.fill.softEdge` as a fraction of the width |
| Effects | `blur` px (a sigma), `dropShadow` `"x y blur color"` (y down), `glow` `"radius color strength mix"`, `grain` `"amount size"`, `directionalBlur` `"length angle"`, `brightness`, `contrast`, `mixBlendMode`, `filter` | `blur.size`, `shadow` (`Offset`, `Softness`), `glow` (`Size`, `Amount`) |
| Mask | `mask` on the object to cut, `clipPath`, `feather` | `mask.make {ids}`, `mask.invert` |
| Easing | CSS on the key the segment **leaves**: `linear`, `ease-out`, `cubic-bezier(...)`, `steps(...)`, `spring(...)`, `hold` | `easing` on the arriving key: `Linear`, `Ease in`, `Ease out`, `S-curve`, `Hold`, `Custom` + `customEase` |
| Time | frames, `"1.5s"` or `"500ms"` | frames |
| Per-letter and per-word timing | `anim.set {from: {...}, stagger: {target: "chars" or "words" or "lines", each: "4f", from: "start"}}` | `stagger.set`, `text.relative.*` |

How the curve names on the pages ("S-curve", "expo out", "quad out", "decelerate") map to `ease` strings: [easing reference](principles/easing-reference.md#names-used-in-this-wiki).
A key that is not in the design list yet (a text outline's thickness, a gradient's start and end, a path's contour, `wordSpacing`, the motion-blur shutter) keeps its stored name on the page that uses it, and
the page says so. Project and lab files are **not** converted: they keep the stored format until B1 migrates them. Open one and read it with `scene.get`
([labs](labs/README.md#reading-the-labs-in-design-units)).

**Keying by design name works** (Carvercat 0.1.8): `softEdge`, `feather`, `trimStart` / `trimEnd` / `trimOffset`, `blur`,
`dropShadow`, `glow`, `borderRadius`, `innerRadius`, `strokeWidth` go through `anim.set`, `key.set` and `key.remove {key, at}` like any other number
(checked by `wiki/tools/verify_keyed_pages.py`). A shape has one `softEdge` (one soft edge per shape); `strokeSoftEdge` is its old name. A null object (null object) is a
parent that draws nothing: [null object](techniques/null-object.md).

## How to find things

- **Agents**: read [index.json](index.json): one record per page with `id`, `title`, `path`, `tags`,
  `styles`, `topics`, `related`, `verified` and `source_inspiration`. Filter by `topics` or `styles`, open
  only the pages you need.
- **People**: browse [INDEX.md](INDEX.md) (the same list as tables) or the sections below.
- **Words**: [glossary.md](glossary.md) defines every term and gives its Carvercat name.
- **Ready-made motion**: the verified style packs and craft references live in `ai/`; start at
  [ai/SKILL.md](../ai/SKILL.md) and [ai/references/INDEX.md](../ai/references/INDEX.md). The wiki explains
  *why* and *when*; the packs are *what to place*.

## Sections

| Section | What it covers |
|---|---|
| [Principles](principles/README.md) | The 12 principles of animation and beyond (timing and spacing, slow in and out, arcs, weight, rhythm), applied to 2D motion graphics |
| [Design](design/README.md) | Hierarchy, grids, colour, contrast, type pairing, negative space, Gestalt, visual flow |
| [Techniques](techniques/README.md) | Masking, parallax, morphing, kinetic type, line drawing, stagger systems, loops, match cuts, rhythm editing, 2D camera moves, faux 3D |
| [Sound and timing](sound-and-timing/README.md) | Beat sync, frame rates, reading time |
| [Genres](genres/README.md) | Explainers, product launches, title sequences, broadcast packages, social ads, lyric videos, data stories, UI demos, logo animation, infographics, event openers |
| [Workflow](workflow/README.md) | Briefs, storyboards, animatics, review, delivery |
| [Accessibility](accessibility/README.md) | Photosensitivity, motion sensitivity, readability, captions |
| [History](history/README.md) | Movements and influential styles, described in words |
| [Styles](styles/README.md) | One hub per style family (SaaS, cartoon, funky, futuristic, retro, glitch, luxury, corporate, kinetic, data, social, sports, explainer) linking its pack and the wiki pages that matter for it |
| [Cookbook](cookbook/README.md) | Task-shaped how-tos (type on, count up, draw a path, logo sting, loop, lower thirds, camera push, beats, ducking, progress, ripple, split-screen, text mask, highlight, chart bars, 9:16 captions, wipes, shake, pops, pulse, countdown, donut, endings, dissolves, glints, neon, lists, flips, orbits, underlines, word swaps, headlines, backgrounds, image cards, callouts, clock hands, tile grids, focus pulls), each built and measured in Carvercat |

## Measured references (the pages agents use most)

| Question | Page |
|---|---|
| Which curve? How much is done by each quarter, when does it settle? | [easing reference](principles/easing-reference.md), [springs](principles/springs.md) |
| How do blend modes, colours and fades compute? | [blend modes](techniques/blend-modes.md) (linear light), [colour](design/colour-psychology.md) (BT.709), [colour transitions](design/colour-transitions.md) |
| Shadow, glow and blur sizes in pixels | [shadow and glow](techniques/shadow-and-glow-in-motion.md), [motion blur](techniques/motion-blur.md) |
| What lint and qc actually check | [readability](accessibility/readability.md), [contrast](design/contrast.md), [photosensitivity](accessibility/photosensitivity.md), [reading time](sound-and-timing/reading-time.md) |
| Frame rates, audio sync and levels | [frame rates](sound-and-timing/frame-rates.md), [audio](sound-and-timing/audio-in-carvercat.md) |
| Arcs, parenting, nested comps | [arcs](principles/arcs.md), [camera moves](techniques/camera-moves-2d.md), [nested comps](techniques/nested-comps-and-time.md) |
| Export formats | [delivery](workflow/delivery.md) |
| "How do I make…?" (one task, steps and measured result) | [cookbook](cookbook/README.md) |

## Page format

Each page starts with front matter (one `key: value` per line, lists inline):

```
---
id: principles/arcs                 # the path without .md, never changes
title: Arcs
section: principles
tags: [...]                         # free words for search
styles: [all] or pack names         # saas-ui, kinetic-typography, data-viz, corporate-brand, minimal-luxury,
                                    # social-short-form, cartoon-bounce, funky, futuristic-hud, retro, glitch,
                                    # sports, explainer, transitions
topics: [...]                       # broader subjects: easing, timing, text, depth, ...
related: [section/page, ...]        # other wiki pages
verified: 0.1.6 (rev 1105) # or: design/1 (Carvercat 0.1.8), or: no (theory only)
source_inspiration: [https://...]   # where the ideas came from (ideas only; nothing copied)
---
```

Then: the idea, rules of thumb with concrete values, what was measured in Carvercat (for verified pages),
do and don't, a checklist, and **In Carvercat**.

## Rules for contributors

- Write everything yourself. Sources inspire ideas only: no copied passages, code or images; at most one
  short attributed quote (under 15 words) per page. Record every source in `source_inspiration`.
- No paywalled, pirated or leaked material; books are cited by name only (`book: Title, Author`).
- Any Carvercat value (duration, easing, size, parameter behaviour) must be measured in Carvercat (a headless Carvercat 0.1.8 build: `carvercat-host --mcp`) and the
  page marked `verified`. Otherwise mark it `no (theory only)` and say what is untested.
- Use the design key names (`scale`, `trimEnd`, `borderRadius`; the list is `carvercat://schema/design`) and real preset and
  template names from the Library. Name an old stored name (`transform.placement.scale`, `trim.end`) only in a short "old names, accepted for one release" note.
- New app problems go to [known-issues.md](../ai/references/known-issues.md) as KI or FR rows.
- After editing: `python3 wiki/tools/wiki_index.py --write`, then `python3 wiki/tools/wiki_index.py`
  (check), `python3 tools/check_links.py` and `node tools/build_index.mjs --check`.
