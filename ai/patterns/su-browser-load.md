# Browser window load

**Template** `su_browser_load` (Library name "Browser window load") · SaaS UI pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SU Browser load` in `categories/saas-launch/saas-ui-lab-3`.

For briefs like "show the product", "hero shot of the dashboard" or "it's fast". A 1280×760 px browser window (title bar with three dots and an address bar reading acme.app/dashboard) rises in; grey skeleton blocks pulse while the page "loads"; then the real dashboard appears: a greeting, three KPI tiles and a 12-bar chart. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Window and its chrome (parented to Window) | 0 | up from 60 px below, scale 0.96 → 1 (expo, 24 f), opaque in 8 f | opaque **f8**, position and size settle **f15** |
| KPI tiles, chart panel | 10 | fade in 6 f | |
| Skeleton blocks (pills) | 10 | opacity in 4 f, pulse 1 → 0.45 → 1 twice (12 f each, S curve cubic-bezier(0.333, 0, 0.667, 1)), out f62–70 (accelerating) | gone by **f70** |
| Greeting (Bold 36) | 64 | lift (16 px, 16 f) | |
| KPI labels (Medium 26) and values (Bold 44) | 68, 71, 74 (+2 for values) | fade and rise 12 px | |
| Bar 1–12 (last one accent) | 78 + 2 f each | height 0 → 1 from the baseline (transformOrigin "50% 100%", anchor bottom), small spring, 14 f | **4.3% overshoot**, Bar 12 settles **f113** |

Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (smallest gap 23.1 px).

## Steps
1. Place and apply. Edit the address, greeting, KPI labels and values; bar heights are the bars' heights in the lab script (`vals`).
2. A real screenshot instead of the mock: put it on a track above the skeleton, start it at f64 and fade it in; delete the mock content.
3. Shorter load: move the skeleton's last three keys and the content clips earlier together; one pulse (f10–38) still reads as loading.

## Pitfalls
- A rounded page under a square title bar: the page is a rounded rectangle plus a 40 px square strip at its top, so only its bottom corners stay round. A single rectangle cannot round only some corners.
- The skeleton fades out while the content fades in (f62–76); a hard cut between them reads as a flicker.

Inspiration: skeleton-screen loading conventions in web apps. No external text or code was used.
