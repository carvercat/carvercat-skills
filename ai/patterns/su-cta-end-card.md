# CTA end card

**Template** `su_cta_end_card` · SaaS UI pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SU CTA end card` in `categories/saas-launch/saas-ui-lab-2`.

The closing card: logo mark, wordmark, tagline, a call-to-action button and a URL, stacked at the centre. 120 f (4 s), holds to the end.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Logo mark (140 px rounded square, radius 36, accent, y 400) | 0 | Pop - spring | **16.2% overshoot, settles f20** |
| Wordmark ("Acme", Bold 72 px) | 8 | Card lift | |
| Tagline ("Ship faster. Sleep better.", Medium 36 px, muted) | 14 | Card lift | |
| Button (360×84 px white pill, y 720) | 22 | Pop - gentle | **4.4% overshoot, settles f40** |
| Button label ("Start free trial", Bold 32 px) | 24 | Card lift | |
| URL ("acme.app", Medium 28 px, tracking 1.2) | 30 | Card lift | |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0. Everything is still by f40, which leaves 80 f (2.7 s) to read the URL.

## Steps
1. Place and apply on the last 4 s of the film. Swap the logo mark for your logo (an image clip at the same centre, with Pop - spring).
2. Edit the wordmark, tagline, label and URL.

## Pitfalls
- Only the logo uses the big spring. A second 16% spring on the button competes with it; the button uses the 4.4% pop.

Inspiration: the end-card convention of product ads (logo, line, one action, address). No external text or code was used.
