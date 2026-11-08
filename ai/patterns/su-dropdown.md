# Dropdown menu

**Template** `su_dropdown` (Library name "Dropdown menu") · SaaS UI pack · **Verified 0.1.8.4 (rev 1130)**, comp `SU Dropdown` in `categories/saas-launch/saas-ui-lab-2`.

A 360×72 px "Sort by: Newest" button, a menu panel that unfolds below it with four items, and a hover row on item 3. 90 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Menu button and label (Bold 28 px) | 0 | none | |
| Menu panel (360×280 px, radius 16, shadow) | 8 | scale Y 0 → 1 from its top edge (transformOrigin "50% 0%", anchor 0, 1), f8–20, Custom expo | settles **f16** |
| Hover (336×52 px, `#EEF0FE`) | 40 | opacity 0 → 1, f40–46, decelerating arrival cubic-bezier(0.333, 0.667, 0.667, 1) | |
| Item 1–4 (Medium 28 px; item 1 in the accent) | 12, 15, 18, 21 | Card lift | Item 4 settles **f33** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place and apply. Edit the button label and items.
2. Pair with the [cursor click](su-cursor-click.md): click the button at f8 of the dropdown; move the cursor to the hover row by f40.

## Pitfalls
- The Hover rectangle must sit under the items. It is created before them in the lab so it lands on a lower track.
- transformOrigin "50% 0%" (stored anchor (0, 1)) is the panel's top edge. With the default centre transformOrigin the panel opens in both directions and covers the button.

Inspiration: standard select-menu behaviour in web apps. No external text or code was used.
