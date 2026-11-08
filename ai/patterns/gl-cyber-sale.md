# Cyber sale

**Template** `gl_cyber_sale` (Library name "Cyber sale") · Glitch pack · **verified 0.1.8.1 (rev 1127 build; headless, isolated folders, pack added to a scratch user Library; `ai/scripts/motion/verify_pack.py`)**, comp `GL Cyber sale` in `categories/glitch/gl-lab-3`.

For briefs like "Cyber Monday", "Black Friday glitch ad", "flash sale with a promo code". CYBER MONDAY (cyan, tracked), a white −50% at 330 px that lands with the pack's stretch hit and a red/cyan split, an offer line, a green promo-code plate and a footer. 150 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Kicker | 0 | opacity Hold steps | **f5** |
| Discount "-50%" | 6 | Glitch stretch hit as Hold keys (160 × 60 → 85 × 110 → 112 × 95 → 100%); split 40 → 24 → 34 → 10 → 0 px; re-glitches f60–64 and f105–109 | size **f12** (25.0%, the first step); split **f18** |
| Block 1–8 | f6–12 | 2 or 4 f clips over the price, entrance only | gone by **f16** |
| Offer (SemiBold 48, tracked) | 20 | opacity Hold steps | **f25** |
| Code plate (green 4 px edge) / Code | 30 / 34 | plate switches on like a tube; text steps in | **f36 / f39** |
| Footer (grey Medium 36) | 40 | opacity Hold steps | **f45** |

Lint 0 / 0 / 0; `inspect qc` (240 px): **no flashes**. Placed into a fresh comp: lint 0/0/0, qc no flashes. Text-gap audit: closest pair price / offer, 74.6 px.

## Pitfalls
- Block artefacts only during the entrance. A block over the resting price at f60 was flagged by the text-gap audit (−85.8 px), so the re-glitches use the split alone.

Inspiration: e-commerce sale banners and broken-signal type. No external text or code was used.
