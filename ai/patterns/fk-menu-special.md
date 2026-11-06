# Menu special

**Template** `fk_menu_special` (Library name "Menu special") · Funky pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FK Menu special` in `categories/funky/fk-lab-3`.

For briefs like "today's special", "lunch deal", "new on the menu". A pink TODAY'S SPECIAL ribbon, the dish on two lines with hard ink shadows, a short description, a serving-time pill, a plate stand-in that spins in, and a starburst price badge. 150 f, holds. Dish and price are invented.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Ribbon (pink, +3°) | 0 | grows from its left edge, expo, 10 f | **f7** |
| Ribbon text (ExtraBold 52 px, white) | 4 | fade 4 f | **f8** |
| "SPICY MANGO" (ExtraBold 120 px, orange) | 8 | stamp 1.15 → 1 and a 4° turn, 12 f | **9.8%**, **f19** |
| "TACOS" (ExtraBold 170 px, purple) | 16 | stamp 1.15 → 1, 10° turn, 8 f | **9.3%**, **f24** |
| Dish plate (560 px white, ink ring) and photo disc (440 px teal) | 4 | Spin in as keys: rotate 180° → 0 (stored angle −180° → 0; expo), scale 0.3 → 1 (back), 16 f | angle **f16** (0%), size **9.7%**, **f21** |
| Price badge (14-point star 250 px, yellow, ink outline) | 24 | pop 0 → 1 on the pop curve with a −20° turn, then turns 0 → −30° to the end | size **15.8%**, **f36** |
| Price "$9" (ExtraBold 110 px) | 26 | stamp, turn into +8° | **9.3%**, **f34** |
| Description (Bold 44 px, ink) | 28 | rise 24 px | **f35** |
| Served pill and text | 36 | stamp into −3° | **9.3%**, **f44** |

Lint 0/0/0 in the lab and placed. Text-gap audit: closest pair 58.8 px (the two dish lines). Full-frame looks of the placed instance at f12 and f149: nothing cut.

## Steps
1. Put the dish photo over the teal disc (440 px circle; mask it with the disc) and delete "dish photo".
2. Edit the price; two or three characters fit the 250 px badge at 110 px.

## Pitfalls
- A turn that lands on the same frame where a drift starts writes two keys on one frame: lint **error** `same_frame_keys`. `drift_spin()` in the lab script skips the landing key when it is already there.
- Description and badge outline are ink: keep a light ground.

Inspiration: café chalkboards and fast-food menu boards. No external text or code was used.
