"""mix_check.py - loudness of VO / music / SFX stems and the full mix, as placed.

  python mix_check.py --fps 30 --frames 1125 --vo VO.wav@12 --music bed.wav@0 \
         --sfx-dir sfx --placement sfx/placement.json --out reference_mix.wav

Targets that the user approved (social promo, VO-led):
  VO ~ -16 LUFS, music ~ -23 LUFS (6-7 dB under VO), SFX bus ~ -24..-25 LUFS,
  full mix normalised to -14 LUFS, peaks <= -1 dBFS. Needs ffmpeg for LUFS.
"""
import argparse, json, os, subprocess, wave, tempfile
import numpy as np
SR = 48000

def rd(p):
    w = wave.open(p); ch = w.getnchannels(); sr = w.getframerate()
    x = np.frombuffer(w.readframes(w.getnframes()), '<i2').astype(float) / 32768
    x = x.reshape(-1, ch); x = x if ch == 2 else np.repeat(x, 2, 1)
    if sr != SR: raise SystemExit('%s is %d Hz; resample to 48 kHz first' % (p, sr))
    return x

def lufs(x):
    fd, p = tempfile.mkstemp(suffix='.wav'); os.close(fd)
    with wave.open(p, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(x, -1, 1) * 32767).astype('<i2').tobytes())
    o = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', p, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    os.remove(p)
    return float([l for l in o.splitlines() if 'I:' in l][-1].split()[1])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--fps', type=float, default=30); ap.add_argument('--frames', type=int, required=True)
    ap.add_argument('--vo', help='file@frame'); ap.add_argument('--music', help='file@frame')
    ap.add_argument('--sfx-dir'); ap.add_argument('--placement'); ap.add_argument('--out')
    a = ap.parse_args()
    N = int(a.frames / a.fps * SR); stems = {}
    def place(name, x, fr):
        s = stems.setdefault(name, np.zeros((N, 2))); st = int(fr / a.fps * SR); e = min(N, st + len(x)); s[st:e] += x[:e - st]
    for name, spec in (('vo', a.vo), ('music', a.music)):
        if spec:
            f, fr = spec.rsplit('@', 1); place(name, rd(f), float(fr))
    if a.placement:
        for c in json.load(open(a.placement)): place('sfx', rd(os.path.join(a.sfx_dir, c['file'])), c['start_frame'])
    for k, v in stems.items(): print('%-6s %6.1f LUFS  peak %6.1f dBFS' % (k, lufs(v), 20 * np.log10(np.abs(v).max() + 1e-9)))
    mix = sum(stems.values()); g = 10 ** ((-14 - lufs(mix)) / 20); mix = np.tanh(mix * g * 1.1) / 1.1
    mix = np.clip(mix, -0.89, 0.89)
    print('mix    %6.1f LUFS  peak %6.1f dBFS' % (lufs(mix), 20 * np.log10(np.abs(mix).max())))
    if a.out:
        with wave.open(a.out, 'wb') as w:
            w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype('<i2').tobytes())

if __name__ == '__main__':
    main()
