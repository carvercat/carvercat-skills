# Chart card

**Template** `su_chart_card` · SaaS UI pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SU Chart card` in `categories/saas-launch/saas-ui-lab-2`.

A 640×400 px dashboard card with a title, seven bars (the last one in the accent colour) and a green delta. 90 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Chart card (radius 28, shadow) | 0 | Card lift | |
| Chart title ("Weekly active users", Bold 30 px) | 4 | Card lift | |
| Bar 1–7 (48 px wide, heights 38–96% of 200 px, transformOrigin "50% 100%", the bottom edge) | 10, 13 … 28 | Bar grow up - spring (data-viz pack) | **4.4% overshoot; Bar 1 settles f28, Bar 7 f46** |
| Chart delta ("+18%", Bold 30 px, `#16A34A`, right-aligned) | 34 | Card lift | |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place and apply. Set each bar's height in the comp (the anchor stays on the baseline, y 680).
2. More or fewer bars: keep the 82 px pitch and the 3 f stagger; the card is 640 px wide, so 7 is the maximum.
3. Exit: Modal dismiss on the instance.

## Pitfalls
- The bars' motion is Bar grow up - spring from the data-viz pack, baked into the template as keys, so the template works without that pack. To re-time a bar by applying the preset again, the data-viz pack must be installed.
- The delta lands after the last bar starts (f34), so the number reads as the result of the chart.

Inspiration: dashboard cards in product demos. No external text or code was used.
