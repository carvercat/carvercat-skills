"""sfx_render.py - render a cue sheet into individual WAV files, one per cue.

  python sfx_render.py cues.json --out ./sfx --prefix Brand_SFX --gain-db -8

cues.json: [{"name": "logo_petal_1", "hit": 14, "sound": "pop", "args": {"p": 1.12},
             "peak_db": -6, "lead_s": 0}]
  hit      comp frame where the event happens
  sound    any generator in sfx_kit.py; args are passed to it
  lead_s   seconds of sound BEFORE the hit (whoosh_hit lead), so the clip starts at
           hit - lead_s*fps
Writes WAVs plus placement.json [{file, start_frame, hit, dur_s}] for placing each
file as its own clip on its own audio track (frame -> `left` = frame*ppf).
"""
import argparse, json, os, wave
import numpy as np
import sfx_kit as K

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('cues'); ap.add_argument('--out', default='sfx'); ap.add_argument('--prefix', default='SFX')
    ap.add_argument('--fps', type=float, default=30); ap.add_argument('--gain-db', type=float, default=-8,
                    help='extra gain baked into every file (the editor has no clip gain)')
    ap.add_argument('--stereo-width', type=float, default=0.6)
    a = ap.parse_args()
    cues = json.load(open(a.cues)); os.makedirs(a.out, exist_ok=True)
    cues.sort(key=lambda c: c['hit'] - c.get('lead_s', 0) * a.fps)
    place = []
    for i, c in enumerate(cues):
        x = getattr(K, c['sound'])(**c.get('args', {}))
        x = K.norm(x, c.get('peak_db', -8)) * 10 ** (a.gain_db / 20)
        st = K.stereo(x, a.stereo_width, 6)
        fn = '%s_%02d_%s.wav' % (a.prefix, i + 1, c['name'])
        with wave.open(os.path.join(a.out, fn), 'wb') as w:
            w.setnchannels(2); w.setsampwidth(2); w.setframerate(K.SR)
            w.writeframes((np.clip(st, -1, 1) * 32767).astype('<i2').tobytes())
        place.append({'file': fn, 'start_frame': max(0, int(round(c['hit'] - c.get('lead_s', 0) * a.fps))),
                      'hit': c['hit'], 'dur_s': round(len(x) / K.SR, 3)})
    json.dump(place, open(os.path.join(a.out, 'placement.json'), 'w'), indent=1)
    print(len(place), 'files ->', a.out)

if __name__ == '__main__':
    main()
