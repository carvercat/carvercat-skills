# Impact stack

**Template** `kt_impact_stack` · Kinetic Typography pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `KT Impact stack`.

Three centred 180 px ExtraBold lines ("NO / MORE / BORING", the last in accent) slam in one after another, and an accent underline shoots across under the last line.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Line 1, 2, 3 (y 330, 540, 750) | 0, 8, 16 | scale 1.7 → 1 over 10 f, Custom back (0.34, 1.56, 0.64, 1); opacity 0 → 1 in 3 f | **9.7% overshoot**, settles 10 f after each start |
| Underline (520 × 16 px, `#FFD23F`, anchor left) | 26–40 | scale X 0 → 1, Custom expo | settles **f35** |

Lint 0/0/0. Put an impact sound on frames 0, 8 and 16 (each landing reads at about +4 f), and a whoosh on 26.

## Steps
Place and apply, then edit the three texts. Keep every line at three words or fewer. For holds past about 1.5 s, push the instance slowly (the showcase scales it 1 → 1.04 over its 90 f).
