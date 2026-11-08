# Review card

**Template** `su_review_card` (Library name "Review card") · SaaS UI pack · **Verified 0.1.8.4 (rev 1130)**, comp `SU Review card` in `categories/saas-launch/saas-ui-lab-3`.

For briefs like "customers love it", "social proof", "a testimonial". A 1000×460 px white card (radius 28): five amber stars, a two-line quote (Bold 52), an avatar with initials, a name (Bold 32) and a role (Medium 26). The names are fictional stand-ins. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Review card | 0 | lift (32 px, scale 0.94 → 1, 18 f) | opaque **f7**, settles **f12** |
| Star 1–5 (52 px) | 10 + 3 f each | pop 0 → 1, small spring, 12 f | **4.3% overshoot**, settle **f21–33** |
| Quote 1–2 | 24, 28 | fade and rise 16 px (expo, 16 f) | Quote 1 settles **f34** |
| Avatar (initials parented to it) | 34 | pop | |
| Name, role | 38, 41 | fade and rise 12 px | |

Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (20.2 px between the quote lines).

## Steps
1. Place and apply. Use a real, approved customer quote; split it into two lines of up to about 26 characters at 52 px.
2. Reading time: a 40-character quote needs about 71 f fully on screen (17 characters a second); both lines are fully on screen from about f35 to f150 (115 f).
3. Several reviews: place the template again on the next track 150 f later, or cut between instances with Modal dismiss on the outgoing one.

## Pitfalls
- Initials in a small avatar fail lint's text size easily: "DR" at 24 px measured a 12.3 px line (capitals only, no ascenders or descenders). At 36 px in an 80 px avatar it passes.

Inspiration: testimonial cards on SaaS marketing pages. No external text or code was used.
