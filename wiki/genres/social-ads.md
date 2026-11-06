---
id: genres/social-ads
title: Social ads and short-form
section: genres
tags: [social, ads, reels, tiktok, shorts, 9:16, vertical, hook, safe zone, captions, sound off]
styles: [social-short-form, kinetic-typography, funky, saas-ui, glitch]
topics: [genre, vertical, attention]
related: [accessibility/captions, techniques/kinetic-type, techniques/rhythm-editing, design/grids-and-layout, accessibility/readability, genres/product-launches]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.houseofmarketers.com/guide-to-safe-zones-tiktok-facebook-instagram-stories, https://www.poster.ly/tools/tiktok-safe-zone-checker, https://billo.app/blog/meta-ads-safe-zones, https://www.remotion.dev/elements/overlays/social-safe-zones/]
---

# Social ads and short-form

Short vertical video competes with an infinite feed. It has under two seconds to stop the thumb, is mostly
watched muted, and is partly covered by the platform's own buttons and captions. Everything follows from
those three facts.

## The idea

- **Hook first**: the payoff, the product or the most surprising frame within the first 1–2 s. No slow logo
  build at the start.
- **Sound off by default**: the story must work in text and pictures; captions are not optional.
- **Platform UI covers the edges**: profile and title at the top, captions, music and call-to-action bars at
  the bottom, a column of buttons on the right.
- **Fast rhythm, few words**: a scene change every 1.5–2.5 s, one idea per card, big type.
- **Native look beats polish**: content that looks like the platform (captions, stickers, polls) performs
  better than a TV ad squeezed into 9:16.

## Rules of thumb (1080 × 1920)

| Zone | Keep clear |
|---|---|
| Top | about 14% (≈ 270 px) |
| Bottom | 20–35% depending on platform (design for 35%, ≈ 670 px) |
| Sides | about 6% (≈ 65 px) |
| Right column | below about y 1150, keep x > 850 clear |

- Lengths: 6 s bumper, 15 s, 30 s; loopable endings help on some platforms.
- Type: headlines 90 px or more, body at least 40–48 px on a 1080-wide frame.
- Captions word by word or in short pages, inside the safe zone, high contrast.
- End with one clear call to action, held at least 2 s.

## Measured in Carvercat

A 1080 × 1920 comp linted like any other: the safe box is 5% of each side, `[54, 96, 1026, 1824]`, and
`carvercat_look {overlay:["safe"]}` draws only those 5% boxes. Text placed at 80% and 65% of the height
(inside the platform's bottom zone) raised **no finding**: lint does not know platform zones. Check them
yourself with `carvercat_authoring {mode:"validate", checks:[{type:"bounds_inside", id, box:[61, 268, 955, 1270]}]}`
(the box from [vertical and safe areas](../../ai/references/craft/vertical-and-safe-areas.md)). The minimum
text size is the same 18 px line height as on 16:9 (24 px Rethink Sans measured 17.1 px and was flagged), which
is far below what reads on a phone in a feed: use 40 px and up.

## Do and don't

- Do put the product or payoff on frame 0 and make frame 0 a readable image.
- Do design the 9:16 version natively, not as a cropped 16:9.
- Don't put text, logos or faces in the platform zones.
- Don't rely on the voice-over; many viewers never hear it.

## Checklist

- [ ] Hook within 2 s; frame 0 readable.
- [ ] Captions on, inside the safe zone; body text 40 px or more.
- [ ] `bounds_inside` passes for every text against the platform box.
- [ ] Call to action held 2 s or more; `qc` clean (no flashes).

## In Carvercat

- Pack: [Social Short-form](../../ai/patterns/social-short-form.md) (9:16): `Hook punch`, `Caption words pop`,
  `Whip in - left`, `Hook title (9:16)`, `Caption pages (9:16)`, `Story progress bar (9:16)`,
  `Follow end card (9:16)`, `Listicle (9:16)`, `Poll sticker (9:16)`, `Countdown (9:16)` and more.
- Social round 3 (9:16): `Story tap-through` (segmented story bars with taps; [ss-story-tap](../../ai/patterns/ss-story-tap.md)),
  `Link in bio` (CTA chip; [ss-link-in-bio](../../ai/patterns/ss-link-in-bio.md)), `POV hook` (native text plates;
  [ss-pov-hook](../../ai/patterns/ss-pov-hook.md)), `Comment reply` ([ss-comment-reply](../../ai/patterns/ss-comment-reply.md)),
  `This or that` ([ss-this-or-that](../../ai/patterns/ss-this-or-that.md)), `Price drop` ([ss-price-drop](../../ai/patterns/ss-price-drop.md)),
  `Giveaway rules` ([ss-giveaway](../../ai/patterns/ss-giveaway.md)) and `Reaction picture-in-picture`
  ([ss-reaction-pip](../../ai/patterns/ss-reaction-pip.md)); all pass `bounds_inside` the platform box and keep the button column clear.
- Job ads: `Careers card` ("we're hiring": role, detail pills, URL button; [cb-careers-card](../../ai/patterns/cb-careers-card.md)),
  16:9 from the Corporate Brand pack; recut it to 9:16 as its own layout.
- Playful offers (16:9, Cartoon Bounce round 3): `Swinging price tag` (old price struck, new price stamps;
  [ct-price-tag](../../ai/patterns/ct-price-tag.md)) and `Comic POW` for a hit moment ([ct-comic-pow](../../ai/patterns/ct-comic-pow.md)).
- Funky round 3 (16:9; recut to 9:16 as its own layout): `Menu special` (food offer with a price starburst;
  [fk-menu-special](../../ai/patterns/fk-menu-special.md)), `New drop reveal` (streetwear or merch drop;
  [fk-new-drop](../../ai/patterns/fk-new-drop.md)), `Blob photo frame` (meet the team in a turning blob mask;
  [fk-blob-frame](../../ai/patterns/fk-blob-frame.md)) and `Zine quote` (cut-out words for a loud quote or review;
  [fk-zine-quote](../../ai/patterns/fk-zine-quote.md)).
- Glitch round 3 (16:9, every one passes `inspect qc` with no flashes): `Cyber sale` (−50% with an RGB split and a promo
  code; [gl-cyber-sale](../../ai/patterns/gl-cyber-sale.md)), `Corrupted video title` (creator title card;
  [gl-video-title](../../ai/patterns/gl-video-title.md)) and `Signal lost end card` (end screen with two video slots and
  subscribe; [gl-signal-end](../../ai/patterns/gl-signal-end.md)).
- Throwback posts (Retro round 3, 16:9; recut to 9:16 as its own layout): `Mixtape tracklist` (a playlist on a cassette;
  [rt-mixtape](../../ai/patterns/rt-mixtape.md)), `Polaroid memory` (an instant photo drops in and develops;
  [rt-polaroid](../../ai/patterns/rt-polaroid.md)), `Under construction page` (a 90s web page for "coming soon";
  [rt-under-construction](../../ai/patterns/rt-under-construction.md)) and `Pixel level up` (game-stream achievement;
  [rt-level-up](../../ai/patterns/rt-level-up.md)).
- Club news (16:9, Sports round 3; recut to 9:16 as its own layout): `Signing announcement` (a player photo, from club to club,
  contract years, a SIGNED stamp; [sp-signing](../../ai/patterns/sp-signing.md)) and `Match-day poster`
  ([sp-match-day](../../ai/patterns/sp-match-day.md)).
- Recipe: [tip reel 9:16](../../ai/recipes/tip-reel-9x16.md).
- Converting a 16:9 piece: [vertical and safe areas](../../ai/references/craft/vertical-and-safe-areas.md)
  (`reformat.py`; `comp.format` alone shrinks content).
- Lab: comp `G Vertical 1080x1920` in [the genres lab](../labs/README.md).
