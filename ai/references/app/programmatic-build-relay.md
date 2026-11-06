# Current authoring entrypoint

For new builds use [creative-toolkit.md](creative-toolkit.md) and cc_scene. The normalized recipes below document older delivered jobs. The maintained client discovers the current editor endpoint; old job-local copied clients may not. Never use clear/rebuild on a user document.

# Programmatic build over the relay (no MCP tools required)

Gotchas: `api-gotchas.md`. Delivery details: `workflows/captions-and-voiceover.md`, `workflows/resolve-handoff.md`. The calls are in [design-units.md](design-units.md).

## Toolkit (stdlib; Pillow only for pixel checks)
| File | Purpose |
|---|---|
| `ai/scripts/cc_client.py` | JSON-RPC over the loopback relay or a private headless process: `run`, `tool`, `look`, `apply_scene`, `scene`, `query`, `set`, `animate`, `preflight`, `path`. Port auto-read from the pid file |
| `ai/scripts/cc_scene.py` | `Scene`, `Box`, `gradient`: a scene document in design units sent with one `scene.apply` |
| `ai/scripts/cc_build.py` | procedural helpers (`card`, `text`, `new`, `stagger_caption`) over the same design keys |
| `ai/scripts/resolve_tools.py` | `import_place(seq_dir,prefix,n,track,local_start)` with assertions; `stills(out,a,b,step)` composite grabs |

## Job loop (per clip / comp)
1. Prepare (see `prepare-resolve-project.md`): duplicate the timeline, one comp per clip at the timeline size/fps, named after the clip; `edit.save`. Keep a `subs.json` of subtitle cues (Resolve `GetSubtitles`-style read or export) with timeline-local frames.
2. Sample stills of the clip (`resolve_tools.stills`) every ~20 frames; find framing changes, face zone (keep it free) and gesture frames (the hand-point / finger count moments -> place live graphics there; note centre and size in fractions of frame).
3. Plan track rows: row 0 captions (no box); rows 1..N highlights, one row per simultaneous item (occupied rows refuse). `track.add` as needed.
4. Captions: 3-4 word phrases, `cc_build.stagger_caption` per phrase (or one scene with a word stagger), start = first word frame - 1, out = last word end; keep phrases from overlapping on a row. Position the lower third at about 72 % of the frame height from the top (user request: y_up 0.28). No background box on captions; card only on highlights.
5. Highlights: `card` + `text` (gradient fills) with pop/slide keys; hand-point rings via ellipse with a gradient stroke and `trimEnd` 0% -> 100% (keyed by name); number reveals (Montserrat ExtraBold) with gradient fills.
6. Verify with `look` at entrance, hold and exit frames of each item (force:true). Check row layering, text overflow and that nothing sits on the face.
7. `edit.save`, export PNG sequence (see gotchas), verify pixels, `import_place`, composite stills, save Resolve.
8. Log the job in your own work history and new Carvercat issues in `ai/references/known-issues.md` (generic, no client names).

For a final cross-clip Resolve sheet, do not infer requested-frame order from Gallery-generated still filenames. Seek each frame, allow the compositor to settle, assert the current timecode, and call `Project.ExportCurrentFrameAsStill` with an explicit frame-named path. This made a 19-frame timeline check deterministic after the Gallery workflow produced a shuffled/stale sheet.

## Conventions that held up
- One comp per clip, comp name = clip name (e.g. C2264); output folder `<job>/carvercat/out/<clip>/<clip>/`.
- Time base: comp frame = timeline-local frame; Resolve record frame = timeline start + local.
- Palette used for a generic (non-brand) job: ink #0A0F1F, teal #20D6C7, violet #7A5CFF, gold #FFC65A, pink #FF7AB6, white captions in Poppins Bold; numbers Montserrat ExtraBold; labels Poppins SemiBold.
- Expect roughly 150 relay calls per comp; only reselect/seek when needed, and write builders as functions in one script so a redo is a single run: `clear()` then build.

## Portrait design-system defaults from mixed-clip review
- Build mixed-font titles from measured widths, then center the combined group. Do not position each word from independent hard-coded left coordinates.
- Visually bottom-align condensed display type (for example Impact) with Poppins/Montserrat labels; font bounding boxes alone do not create a clean baseline, so render and tune the vertical offsets.
- Keep headings inside a conservative top safe area and center the underline beneath the full group. A rule about 25-40 px below the visible text bottom usually reads as attached rather than floating.
- When a speaker occupies the center, prefer one modest photo card at a time centered just above the head. Keep photo-label plates inside the card and schedule cards sequentially; avoid simultaneous corner cards unless the shot explicitly provides those zones.
- Reserve gradients for one focal layer (number, border, icon, or rule). Use solid palette colors and low-opacity ink containers for the remaining hierarchy so the frame does not become a rainbow.
- Default to restrained entrances: typography approximately 86-94% to 100%, photo cards about 94% to 100%, 10-14 eased frames, short position travel, and opacity fades. Include the animated overshoot in safe-area checks.
- For a multi-clip chapter system, share alignment, baseline, spacing, and motion helpers while varying icons/containers and accent colors to keep individual designs from feeling copied.
- Never converge mirrored arrows, rays or bursts on a presenter's chest or torso. A graphic can be geometrically clear on transparency yet create unintended anatomical emphasis on the live plate; include subject-sensitivity in combined-video review.
- Treat a full-width caption as a timing/layout defect, not a reason to shrink the entire caption system. Split it at a semantic boundary into sequential phrases and retain the source word timing.

## Untested (do not assume)
WebP import (convert to PNG/JPG first) and multi-comp template reuse.
## Workflow additions (C2267)
- Per-clip flow: sample stills (Resolve `grab.py`) -> read subs.json (track 2 for text; track 1 for word timings, has ASR errors) -> write bN.py from b2/b3 template -> build -> export `<clip>_vN` -> composite over stills + alpha head-box check -> `import_place` on V2 -> Resolve stills check -> save -> log/commit.
- Head boxes differ per framing: check each shot's box (close shot vs wide shot) and keep text out of it; sides/top band are the free zones.
- Fonts: Impact for numbers, Montserrat ExtraBold labels, Poppins Bold captions; avoid Sora/Outfit/Manrope/Lexend (fallback).
- Row plan: captions row 0; highlights rows 1-10 reused when time-disjoint; cards rows 11+ (image, mask, frame) with pills/labels on higher rows; add spare tracks first.
- Subtitle SRT export of on-screen captions: see video_edit job folder `carvercat/srt`.
- Archive the editable project and reproducibility scripts at the approved job destination. Do not assume `video_edit` is that destination: its general policy currently excludes job binaries, while older Carvercat notes placed projects and zipped sequences there. Follow an explicit job instruction until those policies are reconciled.
