# Substitution card

**Template** `sp_substitution` (Library name "Substitution card") · Sports pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SP Substitution` in `categories/sports/sp-lab-3`.

For briefs like "substitution", "player change", "on and off". A yellow SUBSTITUTION 67' header and two slanted panels slash in at the lower left: the player coming OFF (red arrow down) and then the player coming ON (green arrow up). 150 f, with its own exit.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Header panel (670 px wide, slanted) + text + minute (30 px, dark on yellow) | 0 / 3 / 5 | Slash in (from −422.4 px, 129.6 px lower, hard expo, 10 f) | header settles **f7** |
| OFF row panel, arrow (red, points down), number (yellow 44 px), name (white 46 px), OFF tag (#FF6B5E, 28 px) | 8 / 14 / 11 / 13 / 20 | panel slashes in; the arrow drops 40 px into place; the name slides 96 px in from the right; the tag fades | arrow settles **f21** |
| ON row panel, arrow (green, points up), number, name, ON tag (#3FD08A) | 22 / 28 / 25 / 27 / 34 | the same, 14 f later; the arrow rises 40 px | name settles **f34** |
| Exit | 140 | every part fades out together, 8 f | gone **f148** |

Lint (with `contrast:true`) 0 errors, 0 warnings, 13 notes (`repeated_key_value` on the opacity holds before the exit; intended). `inspect qc` (240 px): no flashes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 44 pairs, closest 40.4 px (ON number / ON arrow). Full-frame looks of the placed comp at f20, f60 and f149: nothing cut; the last frame is empty by design.

## Steps
1. Edit `rows` in `substitution()`: shirt number, name, tag text and colour. Names up to about 12 characters at 46 px fit the 670 px panel.
2. For a basketball or hockey line change, only the copy changes; the arrows carry the direction.

## Pitfalls
- A name that slashes in from the left crosses its own number: lint flagged `text_overlap` (26% and 23%) while it passed. The name comes in from the right instead (`from_right`).
- The triangle is a 3-gon that points right; rotate +90 for up and −90 for down (stored values; in design units, clockwise: −90 for up, +90 for down) ([KI-150](../references/known-issues.md#ki-150)).
- Red and green as text on the dark panel fail contrast; the tags use #FF6B5E and #3FD08A, converted with the renderer's BT.709 curve ([KI-141](../references/known-issues.md#ki-141)). The arrows are shapes and keep the team colours.

Inspiration: common broadcast sports graphics conventions. No external text or code was used. Teams, players and leagues are invented.
