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
| [../../wiki/](../../wiki/README.md) | The Carvercat motion-design wiki: principles, design, techniques, sound and timing, genres, workflow, accessibility, history, styles, a how-to cookbook; [index.json](../../wiki/index.json) has one record per page |
| [known-issues.md](known-issues.md) | Every known app issue (KI-###) and feature request (FR-###) with workarounds |
| [../patterns/](../patterns/README.md) | The verified Motion Patterns library: 25 presets, 5 templates, recipes |
| [../patterns/transitions.md](../patterns/transitions.md) | Transitions pack (verified 0.1.6): 7 cover templates cut under, 4 reveal recipes; shape size and stroke limits |
| [../patterns/explainer.md](../patterns/explainer.md) | Explainer pack (verified 0.1.6): step in, emphasis pulse, process steps, icon grid, pointer callout, timeline, speaker lower third, compare columns, flow diagram, key term, checklist, Venn, quiz, cycle, cause and effect, pros and cons, labelled diagram, icon steps, FAQ card, word definition, tip carousel, problem and solution |
| [../patterns/sports.md](../patterns/sports.md) | Sports pack (verified 0.1.6): slash in, impact slam, zoom past, score bug, player card, head to head, GOAL slam, player lower third, match up, standings, full-time score, lineup, spotlight, replay stinger, slash wipe, live score clock, substitution card, signing announcement, touchdown burst, bracket, table movement, fixture list, match-day poster |
| [../patterns/glitch.md](../patterns/glitch.md) | Glitch pack (verified 0.1.6, no flashes): glitch in/out, stretch hit, RGB split, slice shift, noise bars, glitch cut, lower third, block artifacts, error cascade, terminal type-on, stutter words, RGB mark, tracking band, pixel dissolve, video title, news ticker, hacker alert, cyber sale, signal-lost end card, error 404, game over, chromatic logo sting |
| [../patterns/retro.md](../patterns/retro.md) | Retro pack (verified 0.1.6): motion on twos, sunburst title, synthwave sun and grid, rainbow stripes, checker wipe, stripe lower third, VHS overlay, groovy badge, neon sign, chrome title, TV switch-off, arcade start, venetian blinds, 80s action title, mixtape tracklist, under construction page, film countdown leader, pixel level up, 70s TV ident, polaroid memory, retro weather map |
| [../patterns/futuristic-hud.md](../patterns/futuristic-hud.md) | Futuristic HUD pack (verified 0.1.6): flicker on, scan open, power down, reticle, brackets scan, data readout, radar, ID lower third, segment loader, hex grid, signal bars, target lock, alert banner, map ping, scan wipe, biometric scan, drone telemetry, boot sequence, holo turntable (faux 3D), mission briefing, voice waveform, orbit tracker, warning cascade |
| [../patterns/funky.md](../patterns/funky.md) | Funky pack (verified 0.1.6): tilt pop, wiggle, spins, Memphis shapes, offset shadow title, zigzag ribbon, sticker stack, lower third, sale badge, swing headline, pattern drift, squiggle underline, orbit end card, photo stack, star cover, gig poster, menu special, new drop, marquee bands, blob photo frame, party invite, countdown, zine quote |
| [../patterns/cartoon-bounce.md](../patterns/cartoon-bounce.md) | Cartoon Bounce pack (verified 0.1.6): squash land, anticipation jump, jelly, wobbly pop, bouncing ball, boing title, blinking face, smear, speech bubble, button press, character hop, sticker burst, end card, ribbon lower third, hanging sign, bouncy list, walk cycle, map pin, thought bubble, logo reveal, price tag, boing arrow, comic POW, lesson title |
| [../patterns/social-short-form.md](../patterns/social-short-form.md) | Social Short-form pack, 9:16 (verified 0.1.6): hook punch, word captions, whip-in, hook title, caption pages, progress bar, follow end card, name tag, listicle, before/after, poll, countdown, post card, highlight caption, swipe up, story tap-through, link in bio, POV hook, comment reply, this or that, price drop, giveaway, reaction PiP |
| [../patterns/minimal-luxury.md](../patterns/minimal-luxury.md) | Minimal Luxury pack (verified 0.1.6): slow fades, drift, tracked title, feather wipe, product frame, slow quote, lower third, monogram end card, price card, collection title, light sweep, attribute row, framed word, slow dip, material swatches, property feature, collection index, fragrance notes, save the date, boutique address, limited edition number, editorial spread |
| [../patterns/corporate-brand.md](../patterns/corporate-brand.md) | Corporate Brand pack (verified 0.1.6): soft rise/fade, photo push, split-rule title, two-box lower third, logo resolve, three stats, chapter title, quote, end card, agenda, team row, split screen, leader callout, panel wipe, org chart, values grid, anniversary, office card, award badge, partner logo wall, careers card, safety notice |
| [../patterns/data-viz.md](../patterns/data-viz.md) | Data Viz pack (verified 0.1.6): spring bars, point pops, line chart, donut, ranked bars, gauge, column chart, stacked bar, progress rings, comparison bars, timeline, waffle, area chart, data table, conversion funnel, bubble chart, bar chart race, stacked area, tile-grid map, icon array, calendar heatmap; ellipse-trim and rotation facts |
| [../patterns/kinetic-typography.md](../patterns/kinetic-typography.md) | Kinetic Typography pack (verified 0.1.6): slams, zooms, pops, word swap, impact stack, line reveal, beat words, focus pull, lower third, split title, highlight sweep, quote, stat punch, numbered list, follow end card, karaoke line, manifesto scroll, echo stack, opening credits, strike and replace, zoom through letter, poster lockup |
| [../patterns/saas-ui.md](../patterns/saas-ui.md) | SaaS UI pack (verified 0.1.6): toasts, cards, drawers, cursor click, toggle, KPI tile, lower third, feature title, CTA end card, modal over app, chart card, chat thread, dropdown, pricing plans, browser window load, submit to success, kanban drag, integrations hub, zoom to card, review card, rolling counter, search typing |
| [../scripts/](../scripts/) | Python tools: client/scene builders, motion curves, pattern pack, maps, SFX, VO alignment |

## Find by question

### Starting and driving the app
| Question | Read |
|---|---|
| How do I connect, check the build, list ids, and run the build → look → validate loop? | [app/mcp-essentials.md](app/mcp-essentials.md) |
| What units are positions, sizes, rotation, colours, text sizes, easing in? How do I build a whole scene in one call, select objects, check before a send? | [app/design-units.md](app/design-units.md) |
| Old names (`center`, `angle`, `Ease in`, fractions of width) and what replaces them | [app/design-units.md](app/design-units.md) (Old names) |
| Which commands can't go in a batch? Why did my batch roll back? | [app/mcp-essentials.md](app/mcp-essentials.md), [known-issues.md](known-issues.md) |
| Generate a whole film straight into the project JSON (stored format: fractions, y up; units, nested keys, anchor, continuous subscenes) | [app/json-authoring.md](app/json-authoring.md), `../scripts/motion/json_author/` |
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
| Type sizes, read time, text entrances, emphasis; measured tracking/leading widths and lint's reading-time rule | [craft/typography.md](craft/typography.md) |
| Frame counts per style: entrance, overshoot, stagger, exit, hold | [craft/timing-by-style.md](craft/timing-by-style.md) |
| Are any template texts too close together? (the lint gap lint misses) | [audits/text-gap-audit-2026-10-28.md](audits/text-gap-audit-2026-10-28.md), `ai/scripts/motion/audit_text_gaps.py` |
| Is a template's gradient the right way up? Which space do gradient endpoints use? | [audits/gradient-direction-audit-2026-10-28.md](audits/gradient-direction-audit-2026-10-28.md), [KI-155](known-issues.md#ki-155) |
| How to read a brief: facts to pull out, frame budget, style, recipe, what to confirm | [craft/reading-a-brief.md](craft/reading-a-brief.md) |
| Turn a 16:9 film into 9:16: what comp.format carries over, zooming placed templates, what to re-cut | [../recipes/vertical-recuts.md](../recipes/vertical-recuts.md) |
| A whole short video for a common brief (shot list, packs, timings, sample project) | [../recipes/README.md](../recipes/README.md) |
| One principle of animation in depth (squash and stretch, anticipation, staging, … appeal), with measured Carvercat examples | [craft/principles/README.md](craft/principles/README.md) |
| Which transition, how long, what happens at the cut | [craft/transitions.md](craft/transitions.md) |
| SFX per event, levels, music beds | [craft/sound-design.md](craft/sound-design.md) |
| 9:16 and social safe areas, converting 16:9 | [craft/vertical-and-safe-areas.md](craft/vertical-and-safe-areas.md) |
| Is it done? | [craft/review-checklist.md](craft/review-checklist.md), then the style's list in [craft/review-by-style.md](craft/review-by-style.md) |

### Ready-made motion
| Question | Read |
|---|---|
| Is there a preset/template for this (rise, pop, stamp, exit, text cascades, wipes, iris, lower third, logo, bar chart)? | [../patterns/README.md](../patterns/README.md) |
| Push / zoom-through / card stack / highlight sweep recipes | [../patterns/](../patterns/README.md) |
| Product UI motion: toast, card/modal, drawer, cursor click, toggle, KPI tile, chart card, chat thread, dropdown | [../patterns/saas-ui.md](../patterns/saas-ui.md) |
| SaaS launch titles: lower third, feature title, CTA end card | [../patterns/su-lower-third.md](../patterns/su-lower-third.md), [su-feature-title.md](../patterns/su-feature-title.md), [su-cta-end-card.md](../patterns/su-cta-end-card.md) |
| SaaS briefs (round 3): pricing, product hero shot with loading, sign-up success, task board drag, integrations, camera zoom on a UI card, testimonial | [su-pricing-plans.md](../patterns/su-pricing-plans.md), [su-browser-load.md](../patterns/su-browser-load.md), [su-submit-success.md](../patterns/su-submit-success.md), [su-kanban-drag.md](../patterns/su-kanban-drag.md), [su-integrations-hub.md](../patterns/su-integrations-hub.md), [su-zoom-focus.md](../patterns/su-zoom-focus.md), [su-review-card.md](../patterns/su-review-card.md) |
| Kinetic type: word slams, letter zoom/pop, rotating word slot, impact stack, rule reveal, words cut to the beat, blur focus pull | [../patterns/kinetic-typography.md](../patterns/kinetic-typography.md) |
| Data briefs (round 3): conversion funnel, two measures and a size, ranking over years (bar race), mix over time (stacked area), results by state (tile map), "1 in 4 people", daily activity / streak | [dv-funnel.md](../patterns/dv-funnel.md), [dv-bubble-chart.md](../patterns/dv-bubble-chart.md), [dv-bar-race.md](../patterns/dv-bar-race.md), [dv-stacked-area.md](../patterns/dv-stacked-area.md), [dv-tile-map.md](../patterns/dv-tile-map.md), [dv-icon-array.md](../patterns/dv-icon-array.md), [dv-heatmap.md](../patterns/dv-heatmap.md) |
| Kinetic type briefs (round 3): lyric video karaoke fill, manifesto, repetition / hype, opening credits, myth vs fact, zoom through a letter, justified event poster | [kt-karaoke-line.md](../patterns/kt-karaoke-line.md), [kt-manifesto-scroll.md](../patterns/kt-manifesto-scroll.md), [kt-echo-stack.md](../patterns/kt-echo-stack.md), [kt-opening-credits.md](../patterns/kt-opening-credits.md), [kt-strike-replace.md](../patterns/kt-strike-replace.md), [kt-zoom-through.md](../patterns/kt-zoom-through.md), [kt-poster-lockup.md](../patterns/kt-poster-lockup.md) |
| A marker highlight behind one word of a sentence | [../patterns/kt-highlight-sweep.md](../patterns/kt-highlight-sweep.md) |
| A big number in a drawn ring (stat beat) | [../patterns/kt-stat-punch.md](../patterns/kt-stat-punch.md) |
| A testimonial / quote card | [../patterns/kt-quote.md](../patterns/kt-quote.md) |
| Slow tracking expand on a held title (no frozen hold) | [../patterns/kt-focus-pull.md](../patterns/kt-focus-pull.md) |
| Charts: line that draws itself, donut/ring fill, ranked or horizontal bars, gauge/meter, columns, stacked share bar, progress rings, waffle, area | [../patterns/data-viz.md](../patterns/data-viz.md) |
| A timeline of milestones that draws itself | [../patterns/dv-timeline.md](../patterns/dv-timeline.md) |
| A table of numbers with a highlighted row | [../patterns/dv-data-table.md](../patterns/dv-data-table.md) |
| Reveal a filled shape with a moving mask window (area chart) | [../patterns/dv-area-chart.md](../patterns/dv-area-chart.md) |
| Where does an ellipse's stroke start? Which way is positive rotation? | [../patterns/data-viz.md](../patterns/data-viz.md) §measured geometry |
| Calm corporate motion, annual-report titles, brand lower thirds, logo end cards | [../patterns/corporate-brand.md](../patterns/corporate-brand.md) |
| Label a point in footage with a leader line | [../patterns/cb-leader-callout.md](../patterns/cb-leader-callout.md) |
| An agenda / contents slide with a moving active marker | [../patterns/cb-agenda.md](../patterns/cb-agenda.md) |
| Corporate briefs (round 3): leadership / org chart, company values, anniversary, new office, award win, client logos, we're hiring, safety or compliance notice | [cb-org-chart.md](../patterns/cb-org-chart.md), [cb-values-grid.md](../patterns/cb-values-grid.md), [cb-anniversary.md](../patterns/cb-anniversary.md), [cb-office-card.md](../patterns/cb-office-card.md), [cb-award-badge.md](../patterns/cb-award-badge.md), [cb-partner-wall.md](../patterns/cb-partner-wall.md), [cb-careers-card.md](../patterns/cb-careers-card.md), [cb-safety-notice.md](../patterns/cb-safety-notice.md) |
| Luxury briefs (round 3): materials / colourways, hotel or villa feature, lookbook contents, fragrance notes or ingredients, wedding or gala save-the-date, store opening address, numbered limited edition, magazine spread | [ml-swatch-card.md](../patterns/ml-swatch-card.md), [ml-property-feature.md](../patterns/ml-property-feature.md), [ml-collection-index.md](../patterns/ml-collection-index.md), [ml-fragrance-notes.md](../patterns/ml-fragrance-notes.md), [ml-invitation.md](../patterns/ml-invitation.md), [ml-boutique-address.md](../patterns/ml-boutique-address.md), [ml-limited-edition.md](../patterns/ml-limited-edition.md), [ml-editorial-spread.md](../patterns/ml-editorial-spread.md) |
| Cartoon briefs (round 3): a mascot walks in, find us / map pin, a character wonders, playful logo sting, price drop or sale tag, tap here / point at a button, a comic hit (POW), kids' lesson or episode title | [ct-walk-cycle.md](../patterns/ct-walk-cycle.md), [ct-map-pin.md](../patterns/ct-map-pin.md), [ct-thought-bubble.md](../patterns/ct-thought-bubble.md), [ct-logo-reveal.md](../patterns/ct-logo-reveal.md), [ct-price-tag.md](../patterns/ct-price-tag.md), [ct-boing-arrow.md](../patterns/ct-boing-arrow.md), [ct-comic-pow.md](../patterns/ct-comic-pow.md), [ct-lesson-title.md](../patterns/ct-lesson-title.md) |
| Palette roles, contrast, gradients, linear-light colour values | [craft/colour.md](craft/colour.md) |
| A brand's motion system: one easing family, durations, signature move, brand packs | [craft/brand-systems.md](craft/brand-systems.md) |
| Luxury, fashion, fragrance: slow fades, wide tracking, feathered wipe, product frame | [../patterns/minimal-luxury.md](../patterns/minimal-luxury.md) |
| A gleam / sheen passing through logo letters | [../patterns/ml-light-sweep.md](../patterns/ml-light-sweep.md) |
| Which fonts render? Text fell back to Arial | [known-issues.md](known-issues.md#ki-136) |
| Vertical Reels/Shorts/TikTok pieces: hook, captions, progress bar, follow card, listicle, poll, countdown, post card; authoring 9:16 in JSON | [../patterns/social-short-form.md](../patterns/social-short-form.md), [craft/vertical-and-safe-areas.md](craft/vertical-and-safe-areas.md) |
| Social briefs (round 3, 9:16): story with tap-through, link in bio / swipe-up CTA, POV text hook, reply to a comment, this or that, price drop, giveaway rules, reaction / duet face cam | [ss-story-tap.md](../patterns/ss-story-tap.md), [ss-link-in-bio.md](../patterns/ss-link-in-bio.md), [ss-pov-hook.md](../patterns/ss-pov-hook.md), [ss-comment-reply.md](../patterns/ss-comment-reply.md), [ss-this-or-that.md](../patterns/ss-this-or-that.md), [ss-price-drop.md](../patterns/ss-price-drop.md), [ss-giveaway.md](../patterns/ss-giveaway.md), [ss-reaction-pip.md](../patterns/ss-reaction-pip.md) |
| Squash and stretch, anticipation, smear frames, a bouncing ball, character blink | [../patterns/cartoon-bounce.md](../patterns/cartoon-bounce.md) |
| A rigged character or a swinging object (parent to a pivot) written as JSON | [../patterns/ct-character-hop.md](../patterns/ct-character-hop.md), [../patterns/ct-hanging-sign.md](../patterns/ct-hanging-sign.md), [drawing/rigging.md](drawing/rigging.md) |
| Loud, playful graphics: Memphis shapes, offset-shadow type, stickers, zigzags, sale badges, pattern backgrounds | [../patterns/funky.md](../patterns/funky.md) |
| Funky briefs (round 3, 16:9): gig / club-night poster, food or menu special, streetwear "new drop", scrolling marquee bands, blob-shaped photo frame, party invite with RSVP, 3-2-1 countdown, cut-out zine quote | [fk-gig-poster.md](../patterns/fk-gig-poster.md), [fk-menu-special.md](../patterns/fk-menu-special.md), [fk-new-drop.md](../patterns/fk-new-drop.md), [fk-marquee-bands.md](../patterns/fk-marquee-bands.md), [fk-blob-frame.md](../patterns/fk-blob-frame.md), [fk-party-invite.md](../patterns/fk-party-invite.md), [fk-countdown.md](../patterns/fk-countdown.md), [fk-zine-quote.md](../patterns/fk-zine-quote.md) |
| Hard offset (drop) shadow on text that steps out | [../patterns/fk-offset-title.md](../patterns/fk-offset-title.md) |
| Sci-fi HUD: flicker-on, reticle, scan brackets, typed readout, radar sweep (pie slice from a stroke), loaders, stepped meters, alerts, map pings | [../patterns/futuristic-hud.md](../patterns/futuristic-hud.md) |
| Faux 3D baked to keys: a turning wireframe box (edges as thin rectangles), globe meridians, an object passing behind another | [../patterns/fh-holo-turntable.md](../patterns/fh-holo-turntable.md), [../patterns/fh-orbit-tracker.md](../patterns/fh-orbit-tracker.md) |
| HUD readouts that pass contrast (4.5:1), boot logs, telemetry overlays, voice-assistant waveforms (sine paths under masks) | [../patterns/futuristic-hud.md](../patterns/futuristic-hud.md#round-3-briefs-the-pack-could-not-serve-before) |
| 70s/80s looks, animation on twos (stepped Hold keys), synthwave grid, checkerboard transition | [../patterns/retro.md](../patterns/retro.md) |
| Retro briefs (round 3, 16:9): 80s action-movie title, mixtape / playlist tracklist, 90s "under construction" web page, film countdown leader, pixel game level-up, 70s TV ident, polaroid throwback photo, retro TV weather map; several parts moved as one piece on twos (`group2()`) | [rt-action-title.md](../patterns/rt-action-title.md), [rt-mixtape.md](../patterns/rt-mixtape.md), [rt-under-construction.md](../patterns/rt-under-construction.md), [rt-film-leader.md](../patterns/rt-film-leader.md), [rt-level-up.md](../patterns/rt-level-up.md), [rt-tv-ident.md](../patterns/rt-tv-ident.md), [rt-polaroid.md](../patterns/rt-polaroid.md), [rt-weather-map.md](../patterns/rt-weather-map.md) |
| Chrome / gradient-filled type (a static text gradient) | [../patterns/rt-chrome-title.md](../patterns/rt-chrome-title.md) |
| Glitch: RGB split on text, slice shift with masks, noise overlay, glitch transition, photosensitivity checks, terminal typing, pixel dissolve | [../patterns/glitch.md](../patterns/glitch.md) |
| Glitch briefs (round 3, 16:9, qc no flashes): corrupted video title, breaking-news / stream ticker, hacker "intrusion detected" alert, Cyber Monday sale with promo code, signal-lost end screen with subscribe, error 404 page with a cursor click, game over with a 3-2-1 continue, RGB logo sting (Screen-blended copies); a native datamosh smear (masked adjustment layer) | [gl-video-title.md](../patterns/gl-video-title.md), [gl-news-ticker.md](../patterns/gl-news-ticker.md), [gl-hack-alert.md](../patterns/gl-hack-alert.md), [gl-cyber-sale.md](../patterns/gl-cyber-sale.md), [gl-signal-end.md](../patterns/gl-signal-end.md), [gl-error-404.md](../patterns/gl-error-404.md), [gl-game-over.md](../patterns/gl-game-over.md), [gl-chroma-sting.md](../patterns/gl-chroma-sting.md), [glitch.md](../patterns/glitch.md) (round-3 pitfalls) |
| Match graphics: score bug with a score change, player card, team stat bars, goal celebration, versus card, league table, lineup, replay stinger | [../patterns/sports.md](../patterns/sports.md) |
| Live match graphics: a running match clock with added time, a substitution card, a transfer signing, a tournament bracket, a league table climb, a fixture list, a celebration burst with baked confetti | [../patterns/sports.md](../patterns/sports.md#round-3-briefs-the-pack-could-not-serve-before) |
| How-it-works steps with arrows, icon grids, pointer callouts, milestone timelines, comparisons, definitions, checklists, Venn, quiz, cycles | [../patterns/explainer.md](../patterns/explainer.md) |
| Branching cause-and-effect chains, pros and cons with a tipping seesaw (a ball baked to ride a turning beam), labelled diagrams with leader lines, icon steps, FAQ accordions, word definitions with pronunciation, carousels whose cards never overlap, problem and solution splits; explainer accents that pass contrast | [../patterns/explainer.md](../patterns/explainer.md#round-3-briefs-the-pack-could-not-serve-before) |
| Which style pack fits this brief? Timing and palette per style | [craft/style-families.md](craft/style-families.md) |
| Focal point, reading order, grids, hierarchy, safe areas and how to prove them | [craft/composition-and-layout.md](craft/composition-and-layout.md) |
| Which transition, cut on which frame: wipes, doors, bars, clock wipe, bubbles, dip, shape reveal, line sweep, whip pan, zoom blur | [../patterns/transitions.md](../patterns/transitions.md) |
| My big shape renders as a rectangle / is cut off | [known-issues.md](known-issues.md#ki-137) |
| A number that counts up / rolls (odometer) | [../patterns/su-rolling-counter.md](../patterns/su-rolling-counter.md) |
| Text that types itself, with a caret | [../patterns/su-search-typing.md](../patterns/su-search-typing.md) |
| A whole multi-beat promo in one comp | [../patterns/promo-assembly.md](../patterns/promo-assembly.md) |
| Turn my comp into a reusable template with controls on its face | [../patterns/README.md](../patterns/README.md) §template, `../scripts/motion/comp_to_template.py` |

### Motion-design knowledge (the wiki)
| Question | Read |
|---|---|
| Why does this move feel wrong? Easing, spacing, arcs, weight, overshoot, follow-through, measured in Carvercat | [../../wiki/principles/](../../wiki/principles/README.md) |
| How is this technique built (masks, parallax, morphs, trim draw-on, loops, match cuts, camera nulls, faux 3D)? | [../../wiki/techniques/](../../wiki/techniques/README.md) |
| Beats to frames, frame-rate changes, reading time per frame rate | [../../wiki/sound-and-timing/](../../wiki/sound-and-timing/README.md) |
| Hierarchy, grids and safe boxes, colour meaning and linear colour, contrast limits of lint, type pairing, negative space, Gestalt, eye path | [../../wiki/design/](../../wiki/design/README.md) |
| Flash limits and what qc catches, motion sickness, readability rules lint applies, captions | [../../wiki/accessibility/](../../wiki/accessibility/README.md) |
| Briefs, storyboards, animatics, review rounds, delivery formats and export settings | [../../wiki/workflow/](../../wiki/workflow/README.md) |
| How a genre works (explainer, launch, titles, broadcast, social ad, lyric video, data story, UI demo, logo, infographic, opener) and how to build it in Carvercat | [../../wiki/genres/](../../wiki/genres/README.md) |
| Where a style comes from: movements and influential styles, in words | [../../wiki/history/](../../wiki/history/README.md) |
| How do I make one concrete thing (type on, count up, draw a path, logo sting, loop, readable lower third, camera push, beat hit, ducking, progress bar, ripple, split-screen, image in text, word highlight, chart bars, 9:16 captions, wipe, screen shake, pop, pulse, countdown, donut fill, fade to black, cross-dissolve, glint, neon flicker, bullet list, card flip, orbit, underline, word swap, headline by word, background drift, rounded image card, callout, clock hand, tile grid, focus pull)? Steps, measured result, traps | [../../wiki/cookbook/](../../wiki/cookbook/README.md) |
| One hub per style family: the pack, the timing and the wiki pages that matter for it | [../../wiki/styles/](../../wiki/styles/README.md) |
| A term I don't know | [../../wiki/glossary.md](../../wiki/glossary.md) |
| Every wiki page with tags, styles and verification status | [../../wiki/INDEX.md](../../wiki/INDEX.md), [../../wiki/index.json](../../wiki/index.json) |

### Effects and paint
| Question | Read |
|---|---|
| How effects are added, aliased, keyed, promoted | [effects/README.md](effects/README.md) |
| Blur in/out, defocus | [effects/blur.md](effects/blur.md) |
| Glow without burning the element (limits, halo reach) | [effects/glow.md](effects/glow.md) |
| Drop shadow / lift | [effects/shadow.md](effects/shadow.md) |
| Motion blur | [effects/motion-blur.md](effects/motion-blur.md) |
| Aimed speed streaks: whip, slam, push, slide (`directionalBlur`) | [effects/directional-blur.md](effects/directional-blur.md) |
| Film grain, tape and digital noise (`grain`), film looks | [effects/grain.md](effects/grain.md) |
| Fill, linear/radial gradients, shimmer | [effects/fill-and-gradients.md](effects/fill-and-gradients.md) |
| Stroke, dashes, caps, draw-on (trim) | [effects/stroke-and-trim.md](effects/stroke-and-trim.md) |
| Soft edge (`softEdge`, one per shape) and mask feather in px, glows, vignettes, the feathered mask reveal, carve status | [effects/soft-edge.md](effects/soft-edge.md) |
| Outlined text, text paint | [effects/text-paint.md](effects/text-paint.md) |
| Word/character stagger | [effects/stagger.md](effects/stagger.md) |
| Blend modes, masks, wipes | [effects/compositing-and-masks.md](effects/compositing-and-masks.md) |
| Hidden (basement) params, promoting them, ropes between params | [effects/basement-promote-ropes.md](effects/basement-promote-ropes.md) |

### Drawing, objects, characters
| Question | Read |
|---|---|
| Rectangle, ellipse, star, polygon, paths: sizes, corners, recipes, arranging | [drawing/shapes.md](drawing/shapes.md) |
| Draw a character/object from parts, group it, set anchors/pivots, parent and animate; a null object as the rig's pivot or handle | [drawing/rigging.md](drawing/rigging.md#null-object) |
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
