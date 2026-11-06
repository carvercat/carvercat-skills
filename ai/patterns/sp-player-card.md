# Player card

**Template** `sp_player_card` · Sports pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SP Player card`.

A slanted 1320 × 560 px panel (a closed 4-point path, 120 px slant), a 40 px red stripe, the shirt number "10" (360 px, outline only, yellow), "ALEX MORGAN" (ExtraBold 88 px) and "FORWARD · #10" (38 px, tracked, yellow).

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Panel | 0–10 | **Slash in** | settles **f7** |
| Stripe | 4–14 | trimEnd 0% → 100%, strokeLinecap butt, expo | |
| Number | from 8 | **Impact slam** | 6.7%, settles **f16** |
| Name / position | from 10 / 16 | **Slash in** | name settles **f17** |

Lint 0/0. Swap the name, number and position; put the player's cut-out (a media object) between the panel and the number.
