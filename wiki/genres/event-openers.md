---
id: genres/event-openers
title: Event openers and stage screens
section: genres
tags: [event, opener, conference, keynote, stage, led wall, 4k, countdown, walk-in, sizzle]
styles: [kinetic-typography, futuristic-hud, corporate-brand, sports]
topics: [genre, large format, delivery]
related: [genres/title-sequences, genres/broadcast-packages, sound-and-timing/beat-sync, accessibility/photosensitivity, workflow/delivery, techniques/looping]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.avfx.com/event-elements-show-openers/, https://www.sirkproductions.com/news/fintechnerdcon]
---

# Event openers and stage screens

An event opener turns a room of people chatting into one audience. It plays on huge screens, often loud,
before a keynote or a show, and around it sit the walk-in loops, countdowns, speaker cards and stings
that make up the event's screen package.

## The idea

- **Purpose**: energy and focus. The opener says "it is starting" and sets the event's theme.
- **Scale changes everything**: a stage screen can be 10 m wide; a fast whip that works on a phone can be
  overwhelming in a hall. Text can be smaller relative to the frame, motion should be calmer.
- **Odd formats**: ultra-wide LED walls, multiple screens, 4K or bespoke pixel maps. Get the exact pixel
  dimensions and frame rate from the AV team first.
- **Package**: walk-in loop (seamless, long), countdown, opener (1–2 min), speaker/section cards, stings,
  walk-out loop, plus social cut-downs.

## Rules of thumb

- Opener 60–120 s; stings 3–8 s; walk-in loops 2–10 min (built from a seamless 20–60 s cycle).
- Build for the real canvas size; a 4K or LED-wall comp from the start, not an upscaled HD comp.
- Audio is loud: land big moments on the music, and keep sub-bass hits for the payoff.
- Flashes on a huge screen are more dangerous: stay well inside the 3-a-second limit and small areas
  ([photosensitivity](../accessibility/photosensitivity.md)).
- Plan timing: about 3–4 weeks with two review rounds for a bespoke opener.

## Measured in Carvercat

A 3840 × 2160 comp, linted:

- The graphics-safe box scales with the frame: `[192, 108, 3648, 2052]` (5%).
- The minimum text size does **not** scale: `text_too_small` still fires under 18 px of line height in comp
  pixels. "24 px" text measured 17.1 px and was flagged, but 28 px text (about 20 px tall, the same as 14 px
  on an HD frame) passed. On 4K, run lint with `min_text_px: 36` to get the HD-equivalent check
  ([KI-143](../../ai/references/known-issues.md#ki-143)).
- `carvercat_look {overlay:["safe"]}` scales its boxes to the 4K frame.

## Do and don't

- Do get the exact output resolution, frame rate, codec and playback system from the AV team.
- Do preview at real scale if you can (a projector, a big TV) and from the back of the room in your head.
- Don't use fast full-frame flashes or strobes on LED walls.
- Don't forget a clean loop for walk-in; it plays for a long time and every seam shows.

## Checklist

- [ ] Canvas size and frame rate from the AV spec.
- [ ] `inspect lint {min_text_px: 36}` on 4K comps.
- [ ] `qc` clean; no large flashes.
- [ ] Loops close cleanly ([looping](../techniques/looping.md)).
- [ ] Social cut-downs planned.

## In Carvercat

- Set the canvas: `comp.format {width, height, fps}` before building (converting later rescales sizes, see
  [vertical and safe areas](../../ai/references/craft/vertical-and-safe-areas.md)).
- High-energy packs: [Kinetic Typography](../../ai/patterns/kinetic-typography.md), [Futuristic HUD](../../ai/patterns/futuristic-hud.md),
  [Sports](../../ai/patterns/sports.md); calmer: [Corporate Brand](../../ai/patterns/corporate-brand.md).
- Corporate event cards (round 3): `Anniversary card` ([cb-anniversary](../../ai/patterns/cb-anniversary.md)), `Award badge`
  ([cb-award-badge](../../ai/patterns/cb-award-badge.md)) and `Partner logo wall` for sponsors
  ([cb-partner-wall](../../ai/patterns/cb-partner-wall.md)).
- Quiet invitations and save-the-dates (weddings, galas): `Save the date` (a drawn double frame, names, date, venue;
  [ml-invitation](../../ai/patterns/ml-invitation.md), Minimal Luxury round 3).
- Loud event promos (Funky round 3, 16:9): `Gig poster` (act, date, venue, a spinning record;
  [fk-gig-poster](../../ai/patterns/fk-gig-poster.md)), `Party invite` (date / time / place pills, RSVP, confetti;
  [fk-party-invite](../../ai/patterns/fk-party-invite.md)), `Funky countdown` (3-2-1-GO on starbursts, hard cuts on the beat;
  [fk-countdown](../../ai/patterns/fk-countdown.md)) and `Marquee bands` (two scrolling tape bands that loop seamlessly, for
  walk-in screens; [fk-marquee-bands](../../ai/patterns/fk-marquee-bands.md)).
- Game and esports openers (Futuristic HUD round 3): `Mission briefing` (operation name, map route, objectives;
  [fh-mission-briefing](../../ai/patterns/fh-mission-briefing.md)) and `Warning cascade` (warnings stack, then SYSTEM OVERRIDE;
  [fh-warning-cascade](../../ai/patterns/fh-warning-cascade.md)).
- Match-day openers (Sports round 3): `Match-day poster` (MATCH DAY, two crests, date, time and venue;
  [sp-match-day](../../ai/patterns/sp-match-day.md)) and `Touchdown burst` for a celebration sting
  ([sp-touchdown-burst](../../ai/patterns/sp-touchdown-burst.md)).
- Recipe close to an opener: [annual report opener](../../ai/recipes/annual-report-opener.md).
- Export masters: ProRes 422 or the AV team's codec ([delivery](../workflow/delivery.md)).
- Lab: comp `G 4K 3840x2160` in [the genres lab](../labs/README.md).
