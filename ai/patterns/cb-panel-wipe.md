# Brand panel wipe

**Template** `cb_panel_wipe` (Library name "Brand panel wipe") · Corporate Brand pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `CB Panel wipe` in `categories/corporate-brand/cb-lab-2`.

A two-colour transition: a navy panel and a teal panel cross the frame left to right. Navy is the back panel; it enters first and leaves last, so it shows as a band at both edges of the move. 40 f.

| Part | Clip | Motion | Measured |
|---|---|---|---|
| Panel navy (1000 px drawn, scale X 1.94) | f0–39 | −1 W → 0, f0–16; hold; 0 → +1 W, f23–39 (stored values); S curve cubic-bezier(0.333, 0, 0.667, 1) | settles **f37** (end of the exit) |
| Panel teal (on top) | f3–36 | −1 W → 0, f3–19; hold; 0 → +1 W, f20–36 | settles **f34** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0. No overshoot anywhere (the pack's style rule). The frame is fully covered from f16 to f23; cut between the two scenes at f20.

## Steps
1. Place the instance 20 f before your cut, on a track above both scenes.

## Pitfalls
- Each panel's clip spans only its motion. With full-length clips, lint flagged `cropped_at_rest` ("only 1% on screen while still") on the off-screen frames before and after the move.
- Shapes are cropped to the comp size before scaling ([KI-137](../references/known-issues.md#ki-137)), so each panel is drawn 1000 px wide and scaled to 1940 px.
- The front panel must leave first. In the first build both panels left in the order they arrived, and the navy exit was hidden under the teal one.

Inspiration: brand-colour panel wipes in corporate edits. No external text or code was used.
