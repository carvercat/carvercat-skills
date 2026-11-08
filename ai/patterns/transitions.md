# Transitions pack (`tx_`)

A cross-style set of scene changes.

- **7 cover templates**: shapes cover the frame around one frame; you cut under them.
- **4 reveal recipes**: scene B comes through a mask or moves over scene A; they need your two scenes.

This pack adds to Motion Patterns (two-tone wipe, colour iris, push, zoom-through). Colours are neutral stand-ins (accent `#5B5BF6`, ink `#14151C`, coral `#FF6B5B`); recolour them to the brand.

- Templates live in `library/templates/transitions/`, extracted from `categories/transitions/tx-lab`, which is written by `ai/scripts/motion/transitions_lab.py`.
- The sample, `categories/transitions/tx-showcase`, cuts eight scenes through all seven covers.

**Status: all 7 cover templates and the 4 reveal recipes verified 0.1.8.1 (rev 1127 build, headless, isolated folders, pack added to a scratch user Library), measured by `ai/scripts/motion/verify_pack.py transitions`.**
- The lab (`transitions_lab.py`) and the showcase (`transitions_showcase.py`) speak design units (`json_author/cc2.py`: px from the top-left, y down, degrees clockwise, CSS colours and easing) and are sent with `scene.apply`; the showcase places the seven covers as nested comps. `regen_pack.py` rebuilds the templates and the two sample projects (carvercat/2).
- Each cover template was placed into a fresh 16:9 comp and a fresh 9:16 comp: lint 0 errors / 0 warnings / 0 notes for all seven; qc found no flashes. The showcase master lints 0/0/0.
- Against the v1 originals (7 frames each, over a magenta underlay, silhouette and colour compared on the raw channels): silhouettes match (at most 0.02 % of pixels differ). Colours are now exactly the stated hex values (the accent panel reads `#5B5BF6`; the old files read `#4C4CF5`, because the old authoring kit linearised colours with a curve the app does not use). The compare also caught two sign errors of the first design-unit conversion (the old kit stored counter-clockwise rotations): the diagonal wipe was mirrored and the clock wipe 180 deg off; both are fixed.
- Timings under one definition ("covered" = the underlay is hidden; "moves" = from the first frame that differs from frame 0 to the first frame that equals the last): the windows in the table and in the cover page are those numbers. Two windows changed against the 0.1.6 pages: bars 16-23 (was 20-22), bubbles 17-29 (was 20-24).
- Template names were checked against every other pack and the essentials: no collisions.

| Transition | Kind | Doc | Length | Cut frame (cover window) |
|---|---|---|---|---|
| Slide wipe | template | [tx-cover-transitions.md](tx-cover-transitions.md) | 36 f | 18 (16–20) |
| Diagonal wipe | template | same | 36 f | 18 (17–19) |
| Split doors | template | same | 36 f | 18 (17–20) |
| Bars stagger | template | same | 40 f | 20 (16–23) |
| Clock wipe | template | same | 40 f | 20 (19–21) |
| Bubble cover | template | same | 40 f | 20 (17–29) |
| Dip to colour | template | same | 30 f | 15 (13–17) |
| Shape reveal | recipe | [tx-reveal-recipes.md](tx-reveal-recipes.md) | 24 f | — (moves f18–27) |
| Line sweep | recipe | same | 24 f | — (moves f4–27) |
| Whip pan | recipe | same | 14 f | 15 (moves f9–21) |
| Zoom blur punch | recipe | same | 23 f | 15 (moves f8–20) |

## Using a cover transition
1. Place the template on the **top** track so that its cut frame lands on your edit point (instance start = cut − cut frame). The showcase does exactly this for seven cuts.
2. Make the cut between your two scenes on that frame. The cover hides it.
3. Recolour the pieces inside the nested comp to the brand. Keep the curves: the pieces accelerate **into** the cut (Custom 0.7, 0, 0.84, 0) and leave on an expo-out, which puts the speed at the cut and the calm on either side.

## Measured facts (0.1.6 findings; the cover windows in the table re-measured on 0.1.8.1)
1. **Shapes larger than the comp are cropped to a comp-sized box before their scale** ([KI-137](../references/known-issues.md#ki-137)).
   - A 1800 px circle lost its top and bottom; a 2400 px circle and a 3800 px star became rectangles.
   - Draw cover shapes no bigger than the comp (1000 px here) and scale them up (2.4–5×).
2. **Stroke width tops out at 0.2 of comp width (384 px).** For the clock wipe's pie, draw a 380 px ellipse with a 380 px butt-capped stroke and scale it 2.95×.
3. **An oversized shape held still is `cropped_at_rest` in lint.** Covers keep a slight motion while they hold (a 6° drift, or 3% growth), so they never rest larger than the frame.
4. **Two half-frame doors meeting edge to edge leave a 1 px seam.** Overlap them by 8 px.

Inspiration: common editing-transition vocabulary (wipes, doors, iris and clock wipes, whip pans). No external text or code was used.
