# Price drop (9:16)

**Template** `ss_price_drop` (Library name "Price drop (9:16)") · Social Short-form pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SS Price drop` in `categories/social-media-reels/ss-lab-3`.

For briefs like "price drop", "now only $49", "flash deal ends Sunday". A tracked PRICE DROP kicker, a 600 × 560 px product stand-in, the old price struck through in pink, the new price popping in yellow, a tilted -45% badge, and the deadline. 120 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Kicker (ExtraBold 80 px, yellow, tracking 1.1) | 0 | Hook punch (as keys) | **f7** |
| Product panel (stand-in) and label | 4, 8 | Hook punch from 1.1; fade | panel **f11**, label **f14** |
| Old price "$89" (Bold 84 px, muted) | 12 | Hook punch | **f19** |
| Strike (pink 10 px, slight slope) | 22 | trimEnd 0% → 100%, 8 f, expo | **f27** |
| New price "$49" (ExtraBold 170 px, yellow) | 30 | pop 0.4 → 1, back curve | **9.7% overshoot**, **f40** |
| Discount badge (190 px, pink, −12° (stored value)) and "-45%" | 42 | pop | **f52** |
| "Ends Sunday" (ExtraBold 56 px, outline, x 490, y 1250) | 50 | Hook punch | **f57** |

Lint 0/0/0. `bounds_inside` passed for every object; the price row ends left of x 810 and above y 1151. Placed into a fresh 1080 × 1920 comp: lint 0/0/0. Text-gap audit: closest pair 66.2 px (new price / deadline).

## Steps
1. Put the product still over the panel (same size, rounded 36 px) and delete the label.
2. Edit the prices and the badge; keep the strike about 12 px wider than the old price on each side (`textw` in the lab script sizes it).

## Pitfalls
- Dimming the old price after the strike (opacity held at 1, then keyed down) gave a `repeated_key_value` note and `curves` reported it as a 66.7% "overshoot" ([KI-152](../references/known-issues.md#ki-152)); the old price is muted from the start instead.
- The badge first sat at y 460 and covered "OP" of the kicker. With a 190 px badge under an 80 px kicker at y 380, the badge centre must be at y 513 or lower; it is at 530.

Inspiration: price-drop and flash-sale posts on social. No external text or code was used.
