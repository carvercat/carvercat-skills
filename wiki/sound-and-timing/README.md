# Sound and timing

Time is the medium. These pages turn music, frame rates and reading speed into frame numbers.

| Page | One line | Key numbers |
|---|---|---|
| [Beat sync](beat-sync.md) | Landings on beats, reveals on phrases | frames per beat = fps × 60 ÷ BPM |
| [Frame rates](frame-rates.md) | 24/25/30/60 and what changing them does | `comp.format` keeps frame numbers, not time |
| [Reading time](reading-time.md) | How long text must hold | lint: 17 characters a second, at least 5/6 s, any frame rate |
| [Duration tokens in frames](duration-tokens.md) | Design-system milliseconds as frames | 300 ms = 9 f at 30 fps |
| [Audio clips, levels and fades (measured)](audio-in-carvercat.md) | Sync, gain, fades, mixing, WAV export | clip at f15 → sound at 0.500 s; fades are linear in dB; sums are not limited |
| [Spotting sound effects to motion](sfx-spotting.md) | Which events get a sound, and where | impacts on contact, whooshes lead |
| [Editing music to picture](music-edits.md) | Cutting library music to length | edits on downbeats, back-timed endings |
| [Voice-over pacing](voice-over-pacing.md) | The voice as the clock | 130–160 wpm = 11–14 f per word |
| [Converting a comp to another frame rate](frame-rate-conversion.md) | Rescale every frame number by new ÷ old | fractional keys work; rounding moved a 1 s move by a frame |

Sound design itself (SFX per event, levels, music beds) is in the craft reference
[sound design](../../ai/references/craft/sound-design.md).
