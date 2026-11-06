# Transitions pack (`tx_`)

A cross-style set of scene changes.

- **7 cover templates**: shapes cover the frame around one frame; you cut under them.
- **4 reveal recipes**: scene B comes through a mask or moves over scene A; they need your two scenes.

This pack adds to Motion Patterns (two-tone wipe, colour iris, push, zoom-through). Colours are neutral stand-ins (accent `#5B5BF6`, ink `#14151C`, coral `#FF6B5B`); recolour them to the brand.

- Templates live in `library/templates/transitions/`, extracted from `categories/transitions/tx-lab`, which is written by `ai/scripts/motion/transitions_lab.py`.
- The sample, `categories/transitions/tx-showcase`, cuts eight scenes through all seven covers.

**Status: verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test).**
- Public release binary, headless, isolated folders; the pack was added to a scratch copy's bundled Library ([FR-036](../references/known-issues.md#fr-036)).
- All 11 lab comps lint 0 errors / 0 warnings. qc at 240 px found no flashes (dip to colour included).
- Each cover template was placed into a fresh comp: lint 0/0/0 for all seven.
- The showcase (360 f) lints 0/0/0, with no qc findings.
- Template names were checked against every other pack and the essentials: no collisions.

| Transition | Kind | Doc | Length | Cut frame (cover window) |
|---|---|---|---|---|
| Slide wipe | template | [tx-cover-transitions.md](tx-cover-transitions.md) | 36 f | 18 (16–20) |
| Diagonal wipe | template | same | 36 f | 18 (17–19) |
| Split doors | template | same | 36 f | 18 (17–20) |
| Bars stagger | template | same | 40 f | 20 (20–22) |
| Clock wipe | template | same | 40 f | 20 (19–21) |
| Bubble cover | template | same | 40 f | 20 (20–24) |
| Dip to colour | template | same | 30 f | 15 (13–17) |
| Shape reveal | recipe | [tx-reveal-recipes.md](tx-reveal-recipes.md) | 24 f | — |
| Line sweep | recipe | same | 24 f | — |
| Whip pan | recipe | same | 14 f | 15 |
| Zoom blur punch | recipe | same | 23 f | 15 |

## Using a cover transition
1. Place the template on the **top** track so that its cut frame lands on your edit point (instance start = cut − cut frame). The showcase does exactly this for seven cuts.
2. Make the cut between your two scenes on that frame. The cover hides it.
3. Recolour the pieces inside the nested comp to the brand. Keep the curves: the pieces accelerate **into** the cut (Custom 0.7, 0, 0.84, 0) and leave on an expo-out, which puts the speed at the cut and the calm on either side.

## Measured facts (0.1.6)
1. **Shapes larger than the comp are cropped to a comp-sized box before their scale** ([KI-137](../references/known-issues.md#ki-137)).
   - A 1800 px circle lost its top and bottom; a 2400 px circle and a 3800 px star became rectangles.
   - Draw cover shapes no bigger than the comp (1000 px here) and scale them up (2.4–5×).
2. **Stroke width tops out at 0.2 of comp width (384 px).** For the clock wipe's pie, draw a 380 px ellipse with a 380 px butt-capped stroke and scale it 2.95×.
3. **An oversized shape held still is `cropped_at_rest` in lint.** Covers keep a slight motion while they hold (a 6° drift, or 3% growth), so they never rest larger than the frame.
4. **Two half-frame doors meeting edge to edge leave a 1 px seam.** Overlap them by 8 px.

Inspiration: common editing-transition vocabulary (wipes, doors, iris and clock wipes, whip pans). No external text or code was used.
