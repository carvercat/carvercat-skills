# Directional blur

`directionalBlur` smears an object along one angle: every pixel becomes the mean of the picture over a line `length` px long, half each way (a centred box blur). It is the speed streak for whips, slams, slides and pushes, and unlike the shutter-based [motion blur](motion-blur.md) it does not follow the object's keys: you choose the length and the angle, and you key them. On an **adjustment layer** it streaks everything below. A design key (Carvercat 0.1.10 and later): `"length [angle]"`, or an object `{length, angle}`; also a function of `filter` (`directional-blur(40px 30deg)`).

```json
{"command": "property.set", "args": {"id": "#card", "key": "directionalBlur", "value": "40px 30deg"}}
{"command": "property.set", "args": {"id": "#card", "key": "directionalBlur", "value": "60px"}}
{"command": "property.set", "args": {"id": "#card", "key": "directionalBlur", "value": {"length": "80px", "angle": "45deg"}}}
{"command": "property.set", "args": {"id": "#card", "key": "filter", "value": "blur(4px) directional-blur(40px 30deg)"}}
{"command": "property.set", "args": {"id": "#card", "key": "directionalBlur", "value": "none"}}
```

Verified: directional-blur-design-units.

| Part | Form | Range | Default | Meaning |
|---|---|---|---|---|
| length | `40px`, or `length` | 0 to 500 px of a 1920 frame | 40 px | the streak's whole length. It scales with the frame and the object, like a blur. 0 draws nothing |
| angle | `30deg`, or `angle` | -360 to 360 deg | 0 | **counter-clockwise** from the right (90deg is vertical), the opposite sense of `rotate`. A centred blur has no direction of travel, so 180 and 0, or -90 and 90, draw the same pixels |

`"60px"` alone is a 60 px streak at 0deg; `"90deg"` alone is the default 40 px streak at 90deg. A blur's visible edge ramp is 0.8 x length along its own direction (a 40 px streak softens an edge over 32 px; measured by the app on 10, 40, 100 and 500 px).

## Keying

`directionalBlur` keys by name in `anim.set`, `key.set` and a scene node's `keyframes`; one key carries both length and angle. A whip is the length rising to the fastest frame and falling to 0 as the object lands:

```json
{"command": "anim.set", "args": {"id": "#panel", "keyframes": [
  {"at": 0, "x": -1200, "directionalBlur": "240px 0deg", "ease": "cubic-bezier(.16,1,.3,1)"},
  {"at": 10, "x": 0, "directionalBlur": "0px 0deg"}]}}
```

Verified: directional-blur-design-units (with `linear` easing a key at 5 f between 0 and 120 px reads back 60 px).

## Direction and the object's turn

The blur is applied to the object's own picture and then the object's transform is applied, so the streak turns and scales with the object: an object turned 90deg streaks vertically for angle 0, and one at half size streaks half as far. On a plain unturned object, angle 0 is horizontal and 90 vertical. On a turned object, add the turn to the angle (the sense is the one `rotate` runs in, clockwise, against this key's counter-clockwise) and check with a look; the simplest rule is to put the blur on an unturned object or on an adjustment layer. To move along a diagonal, use the move's own angle: a move that rises 12 % of H over 22 % of W is `atan(0.12 x 1080 / (0.22 x 1920))` = 17deg.

## Refusals

- `out-of-range`: a length above 500 px (scaled by W/1920) or below 0, an angle outside -360 to 360.
- `bad-unit`: a `%` length.
- `bad-value`: two angles (`"40px 30deg 10deg"`) or an unknown key.

Each carries `valid` and a corrected `example` (verified: directional-blur-design-units).

## Where it carves

| Host | Carve | What is sent |
|---|---|---|
| Resolve | **exact** | a Fusion Directional Blur of type Centered. Measured on Resolve Studio: mean abs difference 0.04 to 0.09 of 255, edges within 0.9 px |
| After Effects | **approximate** | a Directional Blur effect. Its kernel is a tent, not a box, so the shape of the streak differs a little (mean abs difference 0.2 to 0.7 of 255 up to 100 px, 2.0 at 200 px, edges within 1.3 px). A scaled object's streak is not scaled in After Effects, and only the first key of the object's own rotation is followed |

Run `carve.preflight` and accept the `approximate` line for After Effects. **Known gap on 0.1.10:** `carve.preflight` lists the effect as `filter:directional-blur`, status `unsupported` ("not an effect this build knows"), on both hosts, because the CSS name is not mapped to the carve row; the carve table above (`carvercat://schema/design`, `directionalBlur`) is the truth and the send carries the effect ([KI-171](../known-issues.md#ki-171)). Grain is listed correctly as `filter:grain`, `approximate`.

## Recipes

- **Whip in a panel or title:** the key above; 160 to 300 px at the fastest frame, 0 on arrival. Pair it with an `expo` ease so the streak is long only for the first frames.
- **Slam and impact:** a vertical streak (`90deg`) 60 to 120 px on the frame the object lands, gone in 3 to 4 f, with a `scale` overshoot.
- **Scene wipe or push:** a full-frame panel moving across, `160 to 240px` along its travel (verified in the Transitions pack: `tx_slide_wipe`).
- **Rise or reveal:** `"60px 90deg"` falling to 0 as a headline comes up into place (`kt_line_reveal`).
- **Diagonal slash:** the move's own angle (`sp_goal_slam`).

## Pitfalls

- Never on text the viewer must read: hold the streak to the move, and be at 0 for the reading frames.
- Not a replacement for [motion blur](motion-blur.md) on a long, curved move (the shutter blur follows each frame's real travel); use directional blur when you want to direct the streak.
- Length is px of a 1920 frame: a 1080 x 1920 vertical comp (W 1080) scales it by 1080/1920.
- A streak extends the object by half its length each way, so leave room or check a full-frame look.
