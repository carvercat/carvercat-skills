"""carverproj.py - small, dependency-free helpers for reading and editing
Carvercat .carverproj files (JSON). Agent-neutral: any agent or person can use it.

Rules that matter (learned the hard way, Carvercat Dev 0.0.69):
  * Edit only clips that the app created. Never clone a clip in JSON - the copy shows
    keys but does not animate. Create clips through MCP (object.new / object.path),
    then retime or restyle them here.
  * The app must not hold unsaved edits while you write: edit.save -> edit here ->
    edit.open {path, force:true} -> comp.switch.
  * Units: position is normalised [x/W, y/H] with y UP. Shape sizes (rect width AND
    height, ellipse, stroke, text font size, text layout box) are fractions of the
    comp WIDTH. Text px = size * width * 0.597. Path points are object-local and
    normalised per axis around 0.5. Audio/clip `left` is in pixels = frame * scene.ppf.
"""
import json, re, copy

def load(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def save(doc, path, indent=1):
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(doc, f, indent=indent, ensure_ascii=False)

def timelines(doc):
    return doc['timelines']

def timeline(doc, name_or_id):
    for t in doc['timelines']:
        if t['id'] == name_or_id or t['name'] == name_or_id or t['name'].startswith(name_or_id):
            return t
    raise KeyError(name_or_id)

def walk(clips, depth=0, parent=None):
    """Yield (clip, depth, parent) for every clip, recursing into groups."""
    for c in clips:
        yield c, depth, parent
        for tr in c.get('tracks', []):
            yield from walk(tr.get('clips', []), depth + 1, c)

def all_clips(tl, audio=False):
    sc = tl['scene']
    tracks = sc['tracks'] + (sc.get('audioTracks', []) if audio else [])
    for tr in tracks:
        yield from walk(tr['clips'])

def find(tl, clip_id):
    for c, _, _ in all_clips(tl, audio=True):
        if c['id'] == clip_id:
            return c
    raise KeyError(clip_id)

def prop(clip, suffix):
    """Find a property by the tail of its key, e.g. 'placement.position' or
    'rectangle.width' -> matches 'tr.e_tr_placement_<id>.position'."""
    a, b = suffix.rsplit('.', 1)
    pat = re.compile(r'%s_%s\.%s$' % (re.escape(a), re.escape(clip['id']), re.escape(b)))
    for k, v in clip.get('properties', {}).items():
        if pat.search(k):
            return k, v
    return None, None

def value_at(p, frame):
    """Evaluate a property linearly between keys (good enough for checks)."""
    kf = p.get('keyframes') or []
    if not kf:
        return p.get('static')
    if frame <= kf[0]['frame']:
        return kf[0]['value']
    for a, b in zip(kf, kf[1:]):
        if a['frame'] <= frame <= b['frame']:
            if a.get('easing') == 'Hold' or isinstance(a['value'], str):
                return a['value']
            t = (frame - a['frame']) / max(1e-9, b['frame'] - a['frame'])
            if isinstance(a['value'], list):
                return [x + (y - x) * t for x, y in zip(a['value'], b['value'])]
            return a['value'] + (b['value'] - a['value']) * t
    return kf[-1]['value']

def set_keys(clip, suffix, keys):
    """keys: list of (frame, value, easing). Easing: Linear, Ease in, Ease out,
    S-curve, Hold. Replaces existing keys on that property."""
    k, p = prop(clip, suffix)
    if p is None:
        raise KeyError('%s has no %s' % (clip['id'], suffix))
    p['keyframes'] = [{'frame': float(f), 'value': v, 'easing': e} for f, v, e in sorted(keys, key=lambda x: x[0])]
    return k

def set_static(clip, suffix, value):
    k, p = prop(clip, suffix)
    if p is None:
        raise KeyError('%s has no %s' % (clip['id'], suffix))
    p['static'] = value
    p['keyframes'] = []
    return k

def shift_keys(clip, frames):
    """Retime every keyframe of a clip by +frames."""
    for p in clip.get('properties', {}).values():
        if isinstance(p, dict):
            for kf in p.get('keyframes', []):
                kf['frame'] += frames

def duplicate_ids(doc):
    """Clip ids that appear in more than one timeline. Two timelines sharing ids
    (e.g. after comp.duplicate) made the editor ~6x slower (20 -> 115 ms/frame)."""
    seen = {}
    for t in doc['timelines']:
        for c, _, _ in all_clips(t, audio=True):
            seen.setdefault(c['id'], set()).add(t['id'])
    return {cid: sorted(ts) for cid, ts in seen.items() if len(ts) > 1}

def make_ids_unique(doc, timeline_id, prefix='clipv_'):
    """Rename every clip id (and every property key / reference that contains it)
    inside one timeline. Returns the number of replaced references."""
    for i, t in enumerate(doc['timelines']):
        if t['id'] == timeline_id:
            s = json.dumps(t)
            n = len(re.findall(r'\bclip_(nest_tl\w+|\d+)\b', s))
            s = re.sub(r'\bclip_(nest_tl\w+|\d+)\b', prefix + r'\1', s)
            doc['timelines'][i] = json.loads(s)
            return n
    raise KeyError(timeline_id)

def entrances(tl, start=0):
    """Frames where a clip becomes visible (opacity or scale goes ~0 -> >0.3).
    Useful for SFX cue sheets and timing audits."""
    out = []
    for c, depth, parent in all_clips(tl):
        first = None
        for k, v in c.get('properties', {}).items():
            if not re.search(r'(placement_%s\.(opacity|scale)|text_relative_%s\.opacity)$' % (c['id'], c['id']), k):
                continue
            kf = v.get('keyframes', [])
            for a, b in zip(kf, kf[1:]):
                av = a['value'][0] if isinstance(a['value'], list) else a['value']
                bv = b['value'][0] if isinstance(b['value'], list) else b['value']
                if isinstance(av, (int, float)) and abs(av) < 0.05 and abs(bv) > 0.3:
                    first = a['frame'] if first is None else min(first, a['frame']); break
        if first is not None and first > 0:
            out.append({'frame': int(start + first), 'clip': c['id'], 'name': c.get('name'), 'group': parent['id'] if parent else None})
    return sorted(out, key=lambda x: x['frame'])
