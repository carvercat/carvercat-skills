---
id: workflow/briefs
title: Briefs
section: workflow
tags: [brief, client, requirements, deliverables, audience, scope, kickoff]
styles: [all]
topics: [workflow, planning]
related: [workflow/storyboards, workflow/animatics, workflow/review, workflow/delivery]
verified: no (theory only)
source_inspiration: [https://milanote.com/guide/motion-graphics-pre-production, https://milanote.com/templates/motion-design/motion-design-brief, https://paperform.co/templates/motion-graphics-project-brief-1, https://hivo.co/templates/motion-design-brief-template]
---

# Briefs

A brief is the short document everyone agrees on before anything is designed. It saves more time than any
technique on this wiki: most rework in motion design comes from questions nobody asked at the start.

## The idea

A good motion brief answers, in one page:

| Question | Example answer |
|---|---|
| What is it for? | launch the new reporting feature to existing customers |
| Who watches it, where? | product managers, on LinkedIn and in-app, mostly muted, mostly on phones |
| What one thing must they remember? | "reports write themselves every Monday" |
| What should they feel? | relieved, confident |
| What should they do next? | click "Try reports" |
| Deliverables | 30 s 16:9 master, 15 s 9:16 cut, 6 s bumper; captions burned in and as SRT |
| Length and pacing | 30 s, hook in the first 2 s |
| Look and style | existing brand system; reference films; which [style pack](../../ai/references/craft/style-families.md) |
| Assets | logo files, fonts (installed?), UI captures, voice-over script, music licence |
| Technical specs | resolution, frame rate, codec, loudness target, safe areas |
| Dates and rounds | first look, review rounds (how many), final delivery |
| Constraints | legal lines, accessibility requirements, words to avoid |

- **The single message** is the heart of the brief. If it cannot be written in one sentence, the film will
  not have one.
- **Write the brief back** in your own words and get it confirmed; this catches misunderstandings early.
- Keep it a living document: update it when decisions change, and date the changes.

## Rules of thumb

- One brief per film; versions get their own row in the deliverables table.
- Agree the number of review rounds and what counts as a revision before starting.
- Confirm fonts and frame rate in the brief; both are expensive to change later
  ([frame rates](../sound-and-timing/frame-rates.md), [typography pairing](../design/typography-pairing.md)).

## Do and don't

- Do ask who watches it, where, with or without sound.
- Do get the voice-over script and music direction before storyboarding.
- Don't start animating from a reference film alone.
- Don't accept "make it pop" as a style direction; ask for references and three adjectives.

## Checklist

- [ ] One-sentence message agreed.
- [ ] Audience, platform and sound-on/off known.
- [ ] Deliverables, specs and dates listed.
- [ ] Review rounds agreed.
- [ ] Fonts, logo and assets received and checked.

## In Carvercat

No Carvercat measurements on this page. Turning a brief into a Carvercat plan:

- Pick the style family and pack: [style families](../../ai/references/craft/style-families.md).
- Check fonts resolve before committing to them: `carvercat_authoring {mode:"fonts"}` and `font_exact`.
- Set up comps at the delivery size and rate from the start (`comp.format {width, height, fps}`).
- The job loop from brief to hand-over: [job playbook](../../ai/references/workflows/job-playbook.md).
