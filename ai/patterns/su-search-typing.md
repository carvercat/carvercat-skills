# Search typing

**Recipe** · SaaS UI pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SU Search typing`; generator `typing()` in `ai/scripts/motion/saas_ui_lab.py`.

A 680×84 px search bar. The placeholder "Search customers" shows for 1 s, then "acme corp" types itself one character every 2 f, with a caret that follows and then blinks.

## Build
1. **Type-on, natively:** one text object holding the whole word, with a **Stagger Text** effect (by character, order forward, gap 2, mode each) whose slot is the text's relative opacity. The relative opacity is keyed 0 at f30 and 1 at f31 with **Hold**. Character *i* (1-based) appears at f30 + 1 + 2(i − 1). This replaces back-to-back clips ([KI-051](../references/known-issues.md#ki-051)) and is lint-clean.
2. **Placeholder:** a muted text from f0 to f30 (30 f, enough for lint's reading time of 15 characters).
3. **Caret:** a 3×44 px accent rectangle with position keys on **Hold** at the same frames as the characters. x = text x + the ink right edge of that prefix (measured with `carvercat_authoring geometry` on throwaway prefix texts) + 4 px; a space adds 10 px at 38 px type. Before typing it sits 6 px left of the placeholder.
4. **Blink** after the last character: opacity Hold keys, off 8 f / on 8 f.

Measured: the caret steps settle at **f47**; lint 0 errors, 0 warnings. The look confirms the caret sits at the end of "a", "acm", "acme c" and "acme corp".

## Pitfalls
- Text under about 35 px fails lint's 18 px minimum line height for lowercase without ascenders (measured: 26 px gives 13.5 px). The recipe uses 38 px.
- Hold arrives AT its key: put the caret key on the same frame the character appears (f0 + 1 + gap × (i − 1)), or the caret jumps one frame early.
