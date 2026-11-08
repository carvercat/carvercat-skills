# Player lower third

**Template** `sp_lower_third` (Library name "Player lower third") · Sports pack · **Verified 0.1.8.1 (rev 1127)**, comp `SP Lower third` in `categories/sports/sp-lab-2`.

Two slanted panels at bottom left: a red number panel (the shirt number, ExtraBold 96 px) and a navy name panel with the name (ExtraBold 56 px) and a yellow stat line. 150 f (5 s) with its own exit.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| LT number panel, LT name panel | 0, 3 | Slash in; Zoom past (last 8 f) | number panel settles **f7** |
| LT name, LT stat | 8, 12 | Slash in; Exit fade - fast | name settles **f15** |
| LT number | 18 | Slash in; Exit fade - fast | |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Pitfalls
- Slash in comes from the lower left, so the name slides across the number's spot. With the number on screen from f6, lint flagged `text_overlap` (26–36%); the number now starts at f18, after the name has passed.
- Impact slam (220%) on the number and Zoom past (300%) on any text also overlapped the next line. Texts exit with a fade; only the panels zoom past.

Inspiration: broadcast player supers. No external text or code was used.
