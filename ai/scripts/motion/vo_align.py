"""vo_align.py - word-level timing for a voiceover, fully offline.

Gives every spoken word a time and a comp frame, so kinetic text can land on the
word. Accuracy ~1-2 frames at 30 fps.

  pip install pocketsphinx numpy        (pocketsphinx bundles an en-US model)
  ffmpeg must be on PATH (to resample the VO to 16 kHz mono)

  python vo_align.py VO.wav script.txt --fps 30 --offset-frames 12 \
        --extra-words "keyframe=K IY F R EY M" --out words.json

script.txt: one sentence/phrase per line, in spoken order. The tool splits the
audio at the longest silences (one split per line break), aligns each phrase,
and writes [{line, words:[{word, start_s, end_s, frame}]}].
Out-of-vocabulary words (product names, jargon) need --extra-words with an
ARPAbet pronunciation; split brand names into dictionary words where possible
(e.g. "carvercat" -> "carver cat").
"""
import argparse, json, re, subprocess, sys
import numpy as np

def read_16k(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', '1', '-ar', '16000', '-f', 's16le', '-'],
                         capture_output=True, check=True).stdout
    return raw, np.frombuffer(raw, '<i2').astype(np.float32) / 32768

def silence_splits(x, n_splits, sr=16000, win=0.02, min_gap=0.25):
    hop = int(win * sr)
    e = np.array([np.sqrt(np.mean(x[i:i + hop] ** 2) + 1e-12) for i in range(0, len(x) - hop, hop)])
    thr = max(np.percentile(e, 20) * 2.5, 1e-3)
    quiet = e < thr
    gaps, i = [], 0
    while i < len(quiet):
        if quiet[i]:
            j = i
            while j < len(quiet) and quiet[j]: j += 1
            dur = (j - i) * win
            if dur >= min_gap and i > 0 and j < len(quiet): gaps.append((dur, (i + j) / 2 * win))
            i = j
        else: i += 1
    gaps = sorted(gaps, reverse=True)[:n_splits]
    if len(gaps) < n_splits:
        sys.exit('found only %d pauses for %d line breaks; merge lines or lower --min-gap' % (len(gaps), n_splits))
    return sorted(t for _, t in gaps)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('wav'); ap.add_argument('script')
    ap.add_argument('--fps', type=float, default=30); ap.add_argument('--offset-frames', type=float, default=0,
                    help='frame where the VO clip starts in the comp')
    ap.add_argument('--extra-words', default='', help='comma list word=ARPABET')
    ap.add_argument('--min-gap', type=float, default=0.25); ap.add_argument('--out', default='words.json')
    a = ap.parse_args()
    from pocketsphinx import Decoder
    lines = [l.strip() for l in open(a.script, encoding='utf-8') if l.strip()]
    raw, x = read_16k(a.wav); SR = 16000
    cuts = silence_splits(x, len(lines) - 1, SR, min_gap=a.min_gap)
    bounds = [0.0] + cuts + [len(x) / SR]
    d = Decoder(samprate=SR, bestpath=False)
    for item in filter(None, a.extra_words.split(',')):
        w, pron = item.split('=', 1)
        try:
            d.add_word(w.strip().lower(), pron.strip(), True)
        except RuntimeError:
            print('note: %r already in the dictionary (or bad phones); using the existing entry' % w.strip())
    out = []
    for i, line in enumerate(lines):
        s, e = bounds[i], bounds[i + 1]
        txt = ' '.join(re.sub(r"[^a-z' ]", ' ', line.lower()).split())
        d.set_align_text(txt)
        d.start_utt(); d.process_raw(raw[int(s * SR) * 2:int(e * SR) * 2], full_utt=True); d.end_utt()
        words = []
        for seg in d.seg():
            if seg.word in ('<s>', '</s>', '<sil>'): continue
            st = s + seg.start_frame / 100; en = s + (seg.end_frame + 1) / 100
            words.append({'word': re.sub(r'\(\d+\)$', '', seg.word), 'start_s': round(st, 3), 'end_s': round(en, 3),
                          'frame': int(round(a.offset_frames + st * a.fps))})
        out.append({'line': line, 'words': words})
        print('%2d  %s' % (i + 1, '  '.join('%s@%d' % (w['word'], w['frame']) for w in words)))
    json.dump(out, open(a.out, 'w'), indent=1)

if __name__ == '__main__':
    main()
