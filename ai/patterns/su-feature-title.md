# Feature title

**Template** `su_feature_title` · SaaS UI pack · **Verified 0.1.8.4 (rev 1130)**, comp `SU Feature title` in `categories/saas-launch/saas-ui-lab-2`.

A centred feature announcement: an accent "NEW" eyebrow tag, a headline, a subline and a gradient underline. 90 f, holds (add an exit on the instance).

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Eyebrow tag (220×52 px pill, accent, y 380) | 0 | Pop - gentle | |
| Eyebrow ("NEW", Bold 30 px, tracking 1.4) | 2 | Card lift | |
| Headline ("Reports that write themselves", Bold 84 px, y 500) | 6 | Words rise - expo | position settles **f17**, opaque by f14 |
| Subline ("Every Monday, in your inbox.", Medium 38 px, muted) | 18 | Card lift | |
| Underline (420×8 px, gradient `#5B5BF6` → `#B07CFF`, y 660) | 24 | scale X 0 → 1 from its centre, f24–38, Custom expo | settles **f33** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place and apply. Edit the eyebrow, headline and subline. Headlines up to about 32 characters fit one line at 84 px.
2. Exit: Modal dismiss on the instance, or cut on a transition from the transitions pack.

## Pitfalls
- The eyebrow label first used a pop from 60%; lint flagged `text_too_small` at 30 px on the first frames. It now uses Card lift (94%).
- The underline's gradient end points are object-local (`[0, 0]` top-left to `[1, 1]` bottom-right of the bar), so they stretch with it. In the template they are `[0.39, 0.39]` → `[0.61, 0.39]`: the blend covers the middle 22% of the bar, with flat accent on the left and flat violet on the right ([KI-155](../references/known-issues.md#ki-155)). The direction is right, so the template is unchanged; for a full-length blend set them to `[0, 0.5]` → `[1, 0.5]`.

Inspiration: product-launch title cards ("new" badge over a benefit headline). No external text or code was used.
