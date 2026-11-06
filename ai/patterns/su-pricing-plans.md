# Pricing plans

**Template** `su_pricing_plans` (Library name "Pricing plans") · SaaS UI pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SU Pricing plans` in `categories/saas-launch/saas-ui-lab-3`.

For briefs like "announce new pricing", "launch the Pro plan" or "show the tiers". Three 400×500 px plan cards (radius 28): Starter and Business white, the featured Pro card in the accent colour. Each card holds a plan name (Bold 32), a price (Bold 80) with "/mo", a rule, three ticked features (Medium 24) and a button (label Bold 28). 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Card 1–3 | 0, 4, 8 | lift: up from 32 px below, scale 0.94 → 1 (expo, 18 f), opaque in 7 f | Card 1 opaque **f7**, position settles **f12** |
| Card contents (parented to their card) | card + 3 … + 12 | fade in 7 f and rise 12 px (expo, 14 f); features 2 f apart | |
| Featured card (Pro) | f40–56 | up 24 px and scale 1 → 1.06, small spring cubic-bezier(0.34, 1.36, 0.64, 1) | **1.8% overshoot on position (settles f53), 2.1% on scale (settles f54)** |
| Card 1 and 3 | f40–56 | scale 1 → 0.97 (expo) | step back, no overshoot |
| Badge "MOST POPULAR" (230×48 pill, Bold 24) | 50 | pop 0 → 1 (small spring, 12 f); label fades in at f52 | **4.3% overshoot, settles f61** |

Lint 0 errors, 0 warnings (notes: `repeated_key_value` on the holds). Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (smallest gap 15.5 px, a tick to its feature line).

## Steps
1. Place and apply. Edit names, prices and features; keep each feature to about 18 characters at 24 px.
2. A different featured plan: copy the Pro card's keys (position, size) to that card, recolour it, and move the badge's parent to it.
3. Two or four plans: delete or copy a card and its children, then respace the cards 460 px apart.

## Pitfalls
- Everything inside a card is **parented** to it, so the featured card can step forward as one piece and its text scales with it. Without the parent, the text stays behind when the card grows.
- Text below about 26 px fails lint's 18 px line height (`text_too_small`): the button labels were 24 px at first and failed at 16.6–17.4 px.
- `curves` reports a 100% "overshoot" on Card 1's size: that is the two moves (0.94 → 1, then 1 → 0.97) read as one. The look shows none.

Inspiration: common SaaS pricing-page layouts. No external text or code was used.
