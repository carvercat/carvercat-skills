# Bouncing ball

**Template** `ct_bouncing_ball` · Cartoon Bounce pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `CT Bouncing ball` in `categories/cartoon-bounce/ct-lab`.

A 120 px red ball travels left to right (x 300 → 1500 by f62) and bounces on a ground line at y 900, with a soft shadow under it.

| Event | Frame | Keys |
|---|---|---|
| Drop from y 220 | 0 → 18 | position arriving with the accelerating arrival curve cubic-bezier(0.333, 0, 0.667, 0.333) (accelerating into the ground) |
| Contacts | 18, 44, 62, 72 | scale [0.88, 1.15] 2 f before (stretch), [1.3, 0.7] on contact (the last one [1.1, 0.9]), [1, 1] 3 f after (the decelerating arrival curve cubic-bezier(0.333, 0.667, 0.667, 1)); transformOrigin "50% 100%" (anchor [0, −1]) keeps the bottom on the ground |
| Peaks | 31 (y 460), 53 (y 660), 67 (y 800) | position arriving with the decelerating arrival curve (decelerating into the peak) |
| Shadow | throughout | follows x; scale 0.45 → 1 and opacity 0.12 → 0.30 as the ball nears the ground |

Measured: lint 0 errors, 0 warnings. The look shows the stretch in the falls and a flat squash at each contact.

## Rules it follows
- Each peak is lower and each bounce shorter: 18 → 13 + 13 → 9 + 9 → 5 + 5 frames.
- Squash on contact for 1–2 frames only, and keep the volume: width × height ≈ 1.
- The fall accelerates (the accelerating arrival curve arriving at the ground) and the rise decelerates (the decelerating arrival curve arriving at the peak). The keys' easing is the curve that arrives at each key.
