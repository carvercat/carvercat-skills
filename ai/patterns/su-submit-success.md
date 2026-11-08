# Submit to success

**Template** `su_submit_success` (Library name "Submit to success") · SaaS UI pack · **Verified 0.1.8.4 (rev 1130)**, comp `SU Submit success` in `categories/saas-launch/saas-ui-lab-3`.

For briefs like "sign up in one click", "checkout", "it just works". A 472×112 px accent button "Create account" (Bold 40) is pressed, closes into a circle, shows a spinner, turns into a green success circle with a tick, and two lines confirm it. Drawn at about 1.3× a desktop button so it reads in a full video frame. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Button (a 2-point path, 112 px round-capped stroke) | 0 | lift (24 px, 18 f) | position settles **f12** |
| Button press | f24–33 | scale 1 → 0.95 (3 f) → 1 (small spring) | **3.5% overshoot, settles f33** |
| Button label | 2 | in f2–9; out f30–34 (accelerating) | |
| Button closes to a circle | f32–44 | trimStart 0% → 49.95% and trimEnd 100% → 50.05% (S curve cubic-bezier(0.333, 0, 0.667, 1)) | both settle **f43** |
| Spinner (60 px ring, 7 px stroke, trimEnd 28%) | 42 | rotate 0 → 720° (two clockwise turns, linear; stored −720°) to f80; fades in 4 f, out f74–78 | |
| Success circle (green, 112 px) | 76 | scale 0.6 → 1, small spring, 12 f | **4.3% overshoot, settles f87** |
| Success ring | 78 | scale 1 → 1.7 (expo), opacity 0.7 → 0, 20 f | |
| Tick (9 px stroke) | 80 | trimEnd 0% → 100% (expo, 12 f) | settles **f88** |
| "Account created" (Bold 52), body (Medium 32) | 86, 92 | lift | |

Lint 0 errors, 0 warnings (3 notes). Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (35.3 px).

## Steps
1. Place and apply. Edit the label and the two success lines. A longer label: lengthen the path (both points) so the label keeps 40 px of padding.
2. With a cursor: place Cursor click so its press lands on f24.
3. A failure state instead: recolour Success to red and replace the tick with an × (two short paths, same trim).

## Pitfalls
- The pill is a **round-capped stroke**, not a rounded rectangle ([shapes in the round-1 pitfalls](saas-ui.md#pitfalls-found-while-building-this-pack-016)). Trimming both ends towards the middle leaves only the two round caps: a circle the height of the stroke. Do not trim to exactly 50% / 50%; leave a 0.1% sliver.
- The label must be gone before the button narrows (f34 < f44), or it spills out of the circle.

Inspiration: common form-submit feedback in web apps. No external text or code was used.
