# Follow end card (9:16)

**Template** `ss_follow_cta` · Social Short-form pack · **verified 0.1.8.1 (rev 1127)**, comp `SS Follow CTA`.

**Measured on 0.1.8.1 (rev 1127, harness `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0, no flashes; against the v1 original the worst silhouette difference is 0.00 % (limit 2 %) and every object is present with the same text (box offset at most 0.0 px); colours are now the exact hex the page states (mean shift 11.7 of 255, intended). The frame numbers in the table above are the keys of the generator (`design units`), unchanged.


A 260 px avatar ring (8 px yellow stroke) at y 760, the handle "@carvercat" (ExtraBold 64 px), a pink pill button "Follow for part 2" (a 2-point path with a 110 px round-capped stroke) at y 1100, and a yellow arrow under it.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Avatar | 0–12 | scale 0 → 1, Custom back | **9.8% overshoot**, settles **f11** |
| Handle / Button label | from 8 / 20 | **Hook punch** | |
| Button | 16–28 | scale 0 → 1, Custom back | **9.8% overshoot**, settles **f27** |
| Arrow | 30–42 | rises 40 px, expo; then holds (no bob: see pack pitfall 1) | |

Lint 0/0; the safe box passes for all five objects. Put the creator's photo in the ring (a media object masked by a circle) and change the handle.
