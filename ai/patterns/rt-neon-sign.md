# Neon sign

**Template** `rt_neon_sign` · Retro pack · **verified 0.1.8.1 (rev 1127)**, comp `RT Neon sign` in `categories/retro/rt-lab-2`.

**Measured on 0.1.8.1 (rev 1127, harness `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0, no flashes; against the v1 original the worst silhouette difference is 0.22 % (limit 2 %) and every object is present with the same text (box offset at most 0.1 px); colours are now the exact hex the page states (mean shift 3.1 of 255, intended). The frame numbers in the table above are the keys of the generator (`design units`), unchanged.


"OPEN LATE" in pink neon (Bold 170 px, text glow 4 plus a Glow effect 0.55), a cyan neon underline and "diner & bar" in cyan. 120 f.

| Part | Motion | Measured |
|---|---|---|
| Neon word | opacity on Hold keys: 0 → 0.8 (f6) → 0.1 (f10) → 1 (f16) → 0.4 (f24) → 1 (f30) | steady from **f30** |
| Neon underline | Hold: on f20, 0.3 at f26, on f32 | |
| Neon small | Rise - on twos at f34 | |

Lint 0 errors, 0 warnings; `inspect qc` (240 px) found no flashes. Placed into a fresh comp: lint 0/0/0. Keys are 4–8 f apart and there are fewer than 3 bright-dark changes in any second.

Inspiration: warming-up neon signs. No external text or code was used.
