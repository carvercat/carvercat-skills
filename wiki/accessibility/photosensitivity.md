---
id: accessibility/photosensitivity
title: Photosensitivity and flashing
section: accessibility
tags: [photosensitive epilepsy, flash, strobe, wcag 2.3.1, harding, red flash, glitch, flicker, qc]
styles: [glitch, futuristic-hud, sports, social-short-form, funky]
topics: [accessibility, safety, delivery]
related: [accessibility/motion-sensitivity, techniques/rhythm-editing, design/contrast, workflow/delivery, workflow/review]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html, https://en.wikipedia.org/wiki/Harding_test, https://www.hardingfpa.com/technical-support/how-to-interpret-hardingfpa-results/, https://www.itu.int/rec/R-REC-BT.1702-3-202311-I, https://www.epilepsy.org.uk/?p=1833, https://en.wikipedia.org/wiki/Denn%C5%8D_Senshi_Porygon, https://www.asa.org.uk/news/flashing-images-in-advertising.html]
---

# Photosensitivity and flashing

Rapid flashes and some regular patterns can trigger seizures in people with photosensitive epilepsy (a few
in every hundred people with epilepsy), and make many more viewers feel unwell. Broadcasters and ad
regulators test for it; a famous 1997 cartoon broadcast sent hundreds of children to hospital. Glitch, HUD,
sports and hype styles are where it most often goes wrong.

## The idea

- **A flash** is a pair of opposing brightness changes (dark → light → dark). The common limit: **no more
  than three flashes in any one-second window**.
- **Area matters**: a flash is only counted when it covers a large part of the view (about a quarter of the
  screen in the WCAG approximation).
- **Red is special**: transitions to and from saturated red are counted separately and are more dangerous.
- **Regular patterns** (stripes, checkerboards) that move, flicker or fill the screen are a separate risk.
- The most provocative rates are roughly 5–30 a second, exactly the rates of strobes and glitch effects.

## Rules of thumb

- Keep full-screen brightness changes at **3 per second or fewer**, and better 2.
- Large flashes: reduce contrast (dark grey to mid grey instead of black to white) or reduce area (under a
  quarter of the frame).
- Avoid saturated red flicker entirely.
- Glitch styles: short bursts (under 0.5 s), small areas, low contrast steps; never strobe the full frame.
- Broadcast and UK advertising need a formal test (for example Harding); in-app checks are indicative.

## Measured in Carvercat

`carvercat_inspect {mode:"qc"}` checks for "over 3 flashes in a second over a quarter of the picture".
Comps of 60 f at 30 fps alternating between two states:

| Test | State length | Flashes a second | qc result |
|---|---|---|---|
| Full frame black/white | 15 f, 10 f, 6 f | 1, 1.5, 2.5 | no flash finding |
| Full frame black/white | **5 f** | 3 | no flash finding (3 is allowed) |
| Full frame black/white | **4 f** | 3.75 | `flashes`, 4 in a second, from f4 |
| Full frame black/white | 3 f | 5 | `flashes`, 5 in a second |
| White box 25% of the frame | 4 f | 3.75 | `flashes` |
| White box 6.25% of the frame | 4 f | 3.75 | no finding (area too small) |
| Full frame black/red | 4 f | 3.75 | `flashes` (counted as general flashes; no separate red check is reported) |
| Mid greys #606060 ↔ #707070 | 4 f | 3.75 | no finding |
| Dark greys #101010 ↔ #3A3A3A | 4 f | 3.75 | `flashes` |

- The threshold behaves as documented: 3 a second passes, anything over fails, and areas below a quarter
  of the frame are ignored.
- qc counted the dark-grey flicker (a small absolute change between dark tones) but not the mid-grey one;
  WCAG would count neither. Treat qc as conservative for dark flicker and confirm with a formal test when it
  matters.
- qc does not test spatial patterns or report red flashes separately; check striped and red content by eye
  and with a formal tool.
- Cutting between dark and bright shots twice a second produced no flash finding
  ([rhythm editing](../techniques/rhythm-editing.md)).

## Do and don't

- Do run qc on every deliverable and on every glitch or strobe moment.
- Do replace full-frame strobes with a single flash, a slow pulse, or a small-area flicker.
- Don't rely on qc for broadcast clearance; it says itself it is "indicative, not a Harding test".
- Don't use red/blue alternating full-screen flashes.

## Checklist

- [ ] `carvercat_inspect {mode:"qc"}` reports no `flashes` findings over the whole film.
- [ ] No flickering stripes or checkerboards larger than a quarter of the frame.
- [ ] No saturated red flicker.
- [ ] Formal test booked for broadcast or UK advertising.

## In Carvercat

- Check: `carvercat_inspect {mode:"qc", from, to}`; findings name the frame where the flashes start and the
  count in that second. Glitch moments are the usual culprits; check them with a narrow range.
- Safer glitch building blocks: the [Glitch pack](../../ai/patterns/glitch.md) was built to pass qc with no
  flashes (stepped jumps with small areas); `Noise bars overlay` and `Glitch cut` keep flicker local.
- Brightness pulses: key `opacity` or `brightness` (a factor; old: the `colour` effect `Gain`) slowly (6+ f per change).
- Lab: comps `F full 15f` … `F dark grey 4f` in [the accessibility lab](../labs/README.md).
