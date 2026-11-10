# SaaS launch, 9:16, 18.5 s

The vertical version of [saas-feature-launch-30s](saas-feature-launch-30s.md). **Verified 0.1.6 (rev 1105), 2026-10-28; builder and measures re-run on Carvercat 0.1.8, 2026-11-04** Sample: `categories/recipes/saas-launch-9x16` (555 f, 1080 × 1920). Builder: `ai/scripts/motion/recipes/rc_saas_9x16.py` (the master is a `carvercat/2` file or one `scene.apply`: [how](README.md#how-the-samples-are-built)). Method and traps: [vertical-recuts.md](vertical-recuts.md).

| Time | Frames | Template | Zoom | Job |
|---|---|---|---|---|
| 0:00 | 0–74 | Hook title (9:16) | — | stop the scroll |
| 0:02.5 | 75–164 | Highlight caption (9:16) | — | the claim in one line |
| 0:05.1 | 153–176 | Swipe up (9:16) | — | cut at f165 |
| 0:05.5 | 165–254 | Chart card | 2.4 + 3% push | the result |
| 0:08.5 | 255–344 | KPI tile | 3.4 + push | the number |
| 0:11.5 | 345–434 | Stat punch | 2.8 + push | the headline claim |
| 0:14.1 | 423–446 | Swipe up (9:16) | — | cut at f435 |
| 0:14.5 | 435–554 | CTA end card | 2.2 + push | one action |

Dropped from the 16:9 cut: the chat thread (its bubbles sit at the far left and right), dropdown, modal over app and notification toast: wide app layouts that need a vertical rebuild.

Measured: lint 0 / 0 / 0; `qc` notes the caption hold (f91–153) and the end card (f468–554). Looks checked.

Speed streak (0.1.10): the Swipe up transition carries a vertical `directionalBlur` (240 px at 90deg while the panel travels, 0 while it covers; [directional blur](../references/effects/directional-blur.md)); exact in Resolve, approximate in After Effects.
