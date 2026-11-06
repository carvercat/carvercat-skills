# Style families: which pack, which timing, which look

One row per verified style pack. Each pack's doc has the presets, templates, measured numbers and a sample project. Use this page to pick a pack from a brief, then open that pack. Measured frame counts per style are in [timing-by-style.md](timing-by-style.md), and the style's review list in [review-by-style.md](review-by-style.md).

| Style | Pack (prefix) | When the brief says | Easing family | Typical entrance / exit | Palette (ground / accent) | Signature pieces |
|---|---|---|---|---|---|---|
| SaaS / product UI | [SaaS UI](../../patterns/saas-ui.md) (`su_`) | app launch, feature demo, dashboard, onboarding | expo landings, small springs (4%) on drops | 18–22 f / 9–10 f | deep indigo / indigo `#5B5BF6` | cursor click, toast, toggle, KPI tile, rolling counter, typing; feature title, chat thread, dropdown, modal over app, chart card, CTA end card |
| Kinetic typography | [Kinetic Typography](../../patterns/kinetic-typography.md) (`kt_`) | words carry the piece, lyric/quote/manifesto | expo + back, slams | 10–16 f per part, words 2–5 f apart | near-black / orange-red | word swap, impact stack, line reveal, beat words, focus pull; split title, highlight sweep, quote, stat punch, numbered list |
| Data viz | [Data Viz](../../patterns/data-viz.md) (`dv_`) | numbers, results, reports, investors | expo, gentle springs on bars | 14–20 f, rows 4 f apart | slate / cyan + series | line chart, donut, ranked bars, gauge; column, stacked bar, progress rings, comparison bars, timeline, waffle, area chart, data table |
| Corporate brand | [Corporate Brand](../../patterns/corporate-brand.md) (`cb_`) | company film, annual report, event | standard / decelerate, no overshoot | 20–24 f / 16 f | navy or light / teal | split-rule title, two-box lower third, frame logo resolve, three stats; chapter title, quote, agenda, team row, split screen, leader callout, panel wipe |
| Minimal luxury | [Minimal Luxury](../../patterns/minimal-luxury.md) (`ml_`) | fashion, fragrance, jewellery, hospitality | standard, ease-in-out, slow | 36–60 f / 30 f | warm black / gold | tracked title, feather wipe, product frame, slow quote; light sweep, collection title, price card, attribute row, monogram end card, slow dip |
| Social short-form (9:16) | [Social Short-form](../../patterns/social-short-form.md) (`ss_`) | Reels, Shorts, TikTok | hard expo, quick springs | 8–10 f, words 3 f apart | dark / hot pink + yellow | hook title, caption pages, progress bar, follow card; name tag, listicle, poll, countdown, post card, highlight caption, swipe up |
| Cartoon | [Cartoon Bounce](../../patterns/cartoon-bounce.md) (`ct_`) | kids, playful explainer, characters | springs 16–31%, squash and stretch | 18–28 f | cream / red, yellow, blue | bouncing ball, boing title, blinking face, smear; speech bubble, button press, rigged character hop, hanging sign, bouncy list, sticker burst |
| Funky | [Funky](../../patterns/funky.md) (`fk_`) | youth brand, music, food, events | wobbly springs, tilts, spins | 18–24 f | peach / purple, orange, pink, teal | Memphis shapes, offset title, zigzag, stickers; sale badge, swing headline, pattern drift, squiggle underline, orbit end card, photo stack, star cover |
| Futuristic HUD | [Futuristic HUD](../../patterns/futuristic-hud.md) (`fh_`) | tech, gaming, security, space | expo, stepped flickers | 10–14 f | near-black / cyan glow + amber | reticle, brackets scan, readout, radar; ID lower third, segment loader, hex grid, signal bars, target lock, alert banner, map ping, scan wipe |
| Retro | [Retro](../../patterns/retro.md) (`rt_`) | 70s/80s, nostalgia, synthwave | any curve **on twos** (Hold) | 12–16 f | cream or night / orange or pink | sunburst title, synthwave sun, stripes, checker wipe; chrome title, neon sign, VHS overlay, arcade start, TV switch-off, venetian blinds |
| Glitch | [Glitch](../../patterns/glitch.md) (`gl_`) | edgy tech, gaming, music, error states | stepped jumps (Hold) | 8–12 f | black / red + cyan | RGB split, slice shift, noise bars, glitch cut; block artifact title, error cascade, terminal type-on, stutter words, tracking band, pixel dissolve |
| Sports | [Sports](../../patterns/sports.md) (`sp_`) | match graphics, highlights, sponsors | expo slashes, impact slams | 8–14 f | navy / team colours + yellow | score bug, player card, head to head, GOAL slam; match up, standings, lineup, full-time score, player spotlight, replay stinger, slash wipe |
| Explainer | [Explainer](../../patterns/explainer.md) (`ex_`) | how it works, tutorial, onboarding | decelerate, back pops, one pulse | 12–14 f, reading-order stagger | light / blue, coral, green | process steps, icon grid, pointer callout, timeline; key term, flow diagram, compare columns, checklist, Venn, quiz, cycle loop |

## From a brief to a build

Turning a brief into a style, a recipe and a shot list is in [reading-a-brief.md](reading-a-brief.md).

## Mixing styles

- **Keep one easing family per piece** ([brand-systems.md](brand-systems.md)). Borrow a *template* from another pack, but restyle its curves if they clash (no springs inside a luxury film).
- **Safe combinations:**
  - SaaS + Data Viz + Explainer (all calm, expo or decelerate);
  - Kinetic Typography + Social Short-form (fast type);
  - Retro + Funky (playful);
  - Futuristic HUD + Glitch (tech, stepped).
- **Every pack needs Rethink Sans installed** ([../known-issues.md#ki-136](../known-issues.md#ki-136)) and installs into `library/templates/` next to Motion Patterns.
