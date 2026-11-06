---
id: workflow/delivery
title: Delivery
section: workflow
tags: [delivery, export, render, codec, h264, hevc, prores, alpha, png sequence, gif, loudness, specs]
styles: [all]
topics: [workflow, delivery]
related: [workflow/review, sound-and-timing/frame-rates, accessibility/photosensitivity, accessibility/captions, techniques/looping]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://tech.ebu.ch/publications/r128, https://thepostflow.com/filmmaker-resources/delivery-specs-cheat-sheet/, https://help-advancedtv.cape.io/hc/de/articles/19588437430929-ProRes-HQ-Export-Guide-Premiere-Pro-CC]
---

# Delivery

Delivery is producing exactly the files the destination expects: the right size, rate, codec, alpha,
loudness, length and name, plus the extras (captions, a clean version, stills). A beautiful film in the
wrong format is a rejected film.

## The idea

- **Read the spec** from the destination (broadcaster, platform, event AV team, developer) and turn it into a
  checklist.
- **Masters and versions**: one high-quality master (ProRes) and the compressed versions made from it
  (H.264/HEVC for web and social, GIF for chat and docs, PNG sequence or ProRes 4444 with alpha for overlays).
- **Overlays need alpha**: lower thirds and bugs for an editor are delivered with transparency.
- **Loudness**: broadcast typically integrates to −23 LUFS (EBU R128) with true peak at −1 dBTP or lower; web
  platforms normalise to around −14 LUFS. Check the spec.
- **Name files** predictably: project_version_aspect_length_date.

## Rules of thumb

| Destination | Typical file |
|---|---|
| Social and web | H.264 MP4, 1080p (or 1080 × 1920 vertical), the comp's frame rate, sound AAC 48 kHz |
| Broadcast / edit master | ProRes 422 (HQ if available) MOV at the programme's rate |
| Overlay for an editor | ProRes 4444 MOV with alpha, or a PNG sequence with alpha |
| Chat, docs, email | GIF at half size and 15 fps, short loop |
| Stills, thumbnails | PNG or JPEG of the key frame |

- Deliver captions as a sidecar file as well when the platform supports it ([captions](../accessibility/captions.md)).
- Run [photosensitivity](../accessibility/photosensitivity.md) checks on the final export, not only the project.

## Measured in Carvercat

Exported a 60 f, 1920 × 1080 comp headless with `export.set` / `export.run` / `export.status`:

| Format setting | Result |
|---|---|
| `format:"video", videoCodec:"h264", container:"mp4", quality:72` | MP4 written (a mostly static test comp: 100 KB) |
| `format:"video", videoCodec:"prores4444", container:"mov", videoAlpha:true` | MOV written, 10 MB for 2 s |
| `format:"gif"` (defaults `gifFps:15`, `gifScale:50`) | 30 frames at 960 × 540 |
| `format:"sequence", sequenceType:"png"` (default `alpha:true`) | 60 PNG files `name_00000.png` …, 8-bit RGBA |

What `export.plan` reports as possible on this build: video codecs h264, hevc, prores422, prores4444 in mp4
or mov (Apple encoders; ProRes needs MOV, alpha needs ProRes 4444); sequences as png, tiff, exr, dpx; stills
png, jpeg, tiff, exr; audio wav, mp3, flac, opus (Opus at 48 kHz only); scale 100/50/25; supersampling 0–4.

Things to know:
- The output folder must already exist; `export.set` does not create it.
- Each export leaves two hidden files next to the output: `.<name>.carvercat-export.json` (the job record:
  state, frames done, file, error) and `.<name>.carvercat-export-source.json` (a snapshot of the project,
  about 370 KB here). Remove them before handing over a folder, or deliver from a clean copy.
- `export.status` reports progress and "complete"; the job file's `state` is `complete` with `error: null`
  when it worked.

## Do and don't

- Do export the master first and make the versions from the same settings.
- Do check the exported file (duration, size, alpha, a few frames) rather than trusting the dialogue.
- Don't deliver H.264 when the spec says ProRes, or 30 fps when it says 25.
- Don't hand over a folder with the hidden job and source files in it.

## Checklist

- [ ] Spec read and turned into a list (size, rate, codec, alpha, audio, loudness, length, naming).
- [ ] `export.plan` matches the list before `export.run`.
- [ ] Output checked: plays, right length, right size, alpha where needed.
- [ ] qc clean on the final; captions file delivered; hidden job files removed.

## In Carvercat

- Commands: `export.set {settings:{format, range, videoCodec, container, quality, videoAlpha, sound, scale,
  supersampling, dir, name, collision}}`, `export.plan`, `export.run`, `export.status`, `export.stop`,
  `export.resume {job}`; the Deliver workspace (`deliver.*`) adds Resolve routes.
- Quick frames without an export job: `carvercat_render {dir, from, to, step}` writes `f00000.png` and so on.
- Async export details and verifying outputs: [export and delivery](../../ai/references/workflows/export-and-delivery.md);
  Resolve hand-off: [resolve handoff](../../ai/references/workflows/resolve-handoff.md); loudness tools:
  `ai/scripts/motion/mix_check.py`.
