# Word definition

**Template** `ex_word_definition` (Library name "Word definition") · Explainer pack · **verified 0.1.8.1 (rev 1127; `ai/scripts/motion/verify_pack.py`: placed in a fresh 16:9 and a fresh 9:16 comp, lint 0/0/0, qc no flash; against the v1 original the silhouette differs by at most 0.00 % of pixels over 7 frames; object-level check pass)**, comp `EX Word definition` in `categories/explainer/ex-lab-3`.

For briefs like "word of the day", glossary entries, language and vocabulary lessons. A word, how to say it (a speaker icon and a respelling whose two syllables light up in turn), the part of speech, a definition and an example. Key term card gives a term and a definition; this adds the pronunciation. Light background included. 150 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Word "motion" (190 px ExtraBold) | 0 | Step in | settles **f9** |
| Underline (coral, 220 px) | 12 | scale X 0 → 1 from the left (expo, 14 f) | done **f26** |
| Speaker disc (88 px) and speaker body | 22 / 26 | disc pops, body fades | disc overshoot **9.8%**, settles **f33** |
| Respelling: MOH (56 px ExtraBold blue), dash, shun (Bold muted) | 30 / 30 / 33 | Step in; dash draws (8 f) | |
| Speaker waves (two arcs) | 26 | on f47, off f67 (Hold) | |
| Syllable pulses | 48 (MOH) / 60 (shun) | scale 1 → 1.12 → 1, once each, never together | back to 100% at **f64**, **f76** |
| Part of speech: NOUN pill and tag | 36 / 38 | Step in | |
| Definition (50 px Medium, two lines) | 50 | Step in | settles **f59** |
| Example (38 px muted) | 74 | Step in | settles **f83** |

Lab comp lint on 0.1.8.1 (native size): 0 errors, 2 warnings, 6 notes (`text_overlap` between neighbouring text boxes at single frames while the parts move; the v1 lab linted 0 warnings on the same build, not yet traced). `inspect qc` (240 px): no flashes, a freeze after f83. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 39 pairs, closest 20.0 px (shun / the dash). Full-frame looks of the placed comp at f52 (waves on, MOH pulsing) and f149: nothing cut.

## Steps
1. Edit the word, the respelling and the texts in `definition()`; the syllable positions are measured with `textw()`, so a longer word moves the dash, the second syllable and the pill with it.
2. Time the pulses (`pulse(s1, 48)`, `pulse(s2, 60)`) and the waves (f47–66) to the voice-over; add a third syllable the same way.

## Pitfalls
- The dash as a "-" text was reported by lint as `text_too_small` (6 px tall) and as an overlap with the next syllable; a drawn 22 px line has neither problem.
- The part of speech in lower case ("noun", 30 px) is 15.6 px tall and also trips `text_too_small` (under 18); capitals at 28 px are 20 px tall.
- Respelling (MOH-shun) rather than IPA: IPA glyphs in Rethink Sans were not tested.

Inspiration: common dictionary and language-lesson conventions. No external text or code was used.
