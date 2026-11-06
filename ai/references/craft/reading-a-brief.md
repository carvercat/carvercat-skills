# Reading a brief

How to turn a client's few lines into a Carvercat build: what to pull out of the brief, how to budget the frames, which style and recipe to start from, and what to confirm before building. Every number here comes from verified packs and lint rules measured on Carvercat 0.1.6 (rev 1105).

## 1. Pull out seven facts
| Fact | Ask yourself | Where it decides |
|---|---|---|
| **Platform and frame** | Where will it play? 16:9 film, 9:16 Reels/Shorts/TikTok, square? | comp size; safe areas ([vertical-and-safe-areas.md](vertical-and-safe-areas.md)) |
| **Length** | Is there a hard limit (6, 15, 30 s)? | the frame budget (§2) |
| **Audience and tone** | Who watches, and how should it feel: calm, premium, playful, urgent, technical? | the style (§3) |
| **The one message** | If they remember one thing, what is it? | the hero beat; staging ([principles/staging.md](principles/staging.md)) |
| **Must-haves** | Logo, product shots, numbers, names, legal lines, a URL, a CTA? | the shot list; reading time |
| **Sound** | Voice-over, music with beats, or silent (most social is watched muted)? | pacing; captions ([../workflows/captions-and-voiceover.md](../workflows/captions-and-voiceover.md)) |
| **Brand system** | Colours, font, an existing motion language? | colour and easing family ([brand-systems.md](brand-systems.md)); Rethink Sans is the packs' font ([KI-136](../known-issues.md#ki-136)) |

If two of these are missing, ask before building. Platform and length are the two you can never guess.

## 2. Budget the frames
- Total frames = seconds × 30.
- **Every line of text costs reading time.** Lint asks for 17 characters a second, spaces not counted, and at least 25 opaque frames: `max(25, ceil(chars × 30 / 17))` ([typography.md](typography.md)). A 40-character line needs 71 f once it is fully on screen, plus its entrance.
- Add the entrance of the style ([timing-by-style.md](timing-by-style.md)): about 10 f in Social, 18 f in SaaS, 36 f in Minimal Luxury.
- The CTA or logo holds at least 2 s at the end.
- Worked example (30 s SaaS launch, 900 f): 9 scenes of 3–4 s, the end card 4 s; see [../../recipes/saas-feature-launch-30s.md](../../recipes/saas-feature-launch-30s.md).
- If the copy does not fit the budget, cut copy, not reading time.

## 3. Choose the style
Match the tone words to a style family ([style-families.md](style-families.md)). Keep one easing family per film; borrow a template from another pack only if its curves fit.

## 4. Start from a recipe when one fits
When the brief matches one of these, start from the recipe: it gives a shot list with frames and a sample project built only from Library templates ([../../recipes/README.md](../../recipes/README.md)). Otherwise pick the style above and assemble from its templates the same way.

| The brief says | Style | Recipe |
|---|---|---|
| launch a feature, announce a release, product demo | SaaS UI (+ one kinetic beat) | [saas-feature-launch-30s](../../recipes/saas-feature-launch-30s.md) |
| quarterly / annual numbers, KPIs, investor update | Data Viz | [quarterly-results](../../recipes/quarterly-results.md) |
| company film, annual report, event opener | Corporate Brand | [annual-report-opener](../../recipes/annual-report-opener.md) |
| fragrance, fashion, jewellery, hotel, premium product | Minimal Luxury | [luxury-product-teaser](../../recipes/luxury-product-teaser.md) |
| Reels / Shorts / TikTok tips, engagement | Social Short-form 9:16 | [tip-reel-9x16](../../recipes/tip-reel-9x16.md) |
| manifesto, quote, lyrics, type-only | Kinetic Typography | [kinetic-quote-reel](../../recipes/kinetic-quote-reel.md) |
| kids, playful lesson, mascot | Cartoon Bounce | [kids-explainer](../../recipes/kids-explainer.md) |
| sale, offer, youth brand, event promo | Funky | [funky-sale-promo](../../recipes/funky-sale-promo.md) |
| tech product, game, security, sci-fi teaser | Futuristic HUD | [hud-tech-trailer](../../recipes/hud-tech-trailer.md) |
| 80s night, nostalgia, synthwave | Retro | [retro-night-promo](../../recipes/retro-night-promo.md) |
| music drop, release teaser, edgy tech | Glitch | [glitch-music-teaser](../../recipes/glitch-music-teaser.md) |
| goal, score change, match day | Sports | [sports-score-update](../../recipes/sports-score-update.md) |
| how it works, lesson, onboarding | Explainer | [explainer-how-it-works](../../recipes/explainer-how-it-works.md) |

Every style also has a round-2 sample film (`categories/<style>/<x>-showcase-2`) that plays all its newest templates in order; open it to see the whole vocabulary before choosing.


## 5. Confirm before building
Send back, in a few lines: frame and length, style, the shot list with seconds, what you need from them (logo file, product shots, exact copy), and anything you assumed. Build one representative scene first and show it ([../workflows/job-playbook.md](../workflows/job-playbook.md) §1).

## 6. Typical traps
- **Too much copy for the length:** the reading-time rule makes it visible early; propose cuts.
- **"Make it pop" with a premium brand:** exaggeration belongs to the style; Corporate and Luxury have 0% overshoot ([principles/exaggeration.md](principles/exaggeration.md)).
- **One cut for every platform:** a 16:9 film does not become a good 9:16 one by changing the frame; plan the vertical version as its own layout ([vertical-and-safe-areas.md](vertical-and-safe-areas.md)).
- **Missing assets:** stand-ins (grey photo frames, Acme names) are fine for the first look; list what must be replaced.

Inspiration: common creative-brief practice in motion and advertising studios. No external text or code was used.
