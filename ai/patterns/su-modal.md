# Modal over app

**Template** `su_modal` (Library name "Modal over app") · SaaS UI pack · **Verified 0.1.8.4 (rev 1130)**, comp `SU Modal` in `categories/saas-launch/saas-ui-lab-2`.

A full app frame: a light app canvas with three cards, a scrim, and a 640×360 px confirmation modal ("Delete project?") with Cancel and Delete buttons. 90 f; opens, holds and closes.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| App canvas (`#F4F5F8`) and App card 1–3 | 0 | none (stand-ins for your UI) | |
| Scrim (frame-size, ink) | 0 | opacity 0 → 0.45 f6–20 (expo), hold, 0.45 → 0 f70–82 (accelerating) | settles at 0.45 by **f20**, clear at f82 |
| Modal (radius 28, shadow) | 8 | Card lift, then Modal dismiss | position settles **f20** |
| Title, body | 10, 12 | Card lift, then Modal dismiss | |
| Cancel, Delete (160×64 px pills) and labels (Bold 30 px) | 14, 16 | Card lift, then Modal dismiss | |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place and apply. Replace App canvas and the App cards with a screenshot or your own UI comp (keep it below the Scrim).
2. Edit the title, body and button labels. A non-destructive action: recolour Delete to the accent.
3. To keep the modal open, delete the Modal dismiss keys from each part (or lengthen the clips) and remove the Scrim's last two keys.

## Pitfalls
- This template keeps its background on purpose (it is a whole app frame). It is not an overlay.
- `curves` reports an "overshoot" of 500 on the modal's scaleUniform. That figure comes from stacking Card lift and Modal dismiss on one property; the look shows no overshoot.

Inspiration: the standard UI dialog pattern (dim the app, raise the dialog, accelerate it away). No external text or code was used.
