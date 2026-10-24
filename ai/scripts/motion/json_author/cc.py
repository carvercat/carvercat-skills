"""cc.py - write Carvercat comps straight into a .carverproj (verified 0.0.72: JSON-authored clips render and animate).
Pixel space 1920x1080, y down. Times in comp frames."""
import json, copy, math, os
HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1920, 1080
EM = 1146.24          # px per 1.0 text size
TPL = json.load(open(os.path.join(HERE, 'templates.json')))
ASSETS = json.load(open(os.path.join(HERE, 'assets.json'))) if os.path.exists(os.path.join(HERE, 'assets.json')) else {}

def lin(h, a=1.0):
    h = h.lstrip('#'); o = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        o.append(round(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4, 5))
    return o + [a]

C = dict(paper=lin('F4F1EA'), paper2=lin('E9E3D7'), ink=lin('121212'), ink2=lin('262626'), grey=lin('8C8A86'),
         orange=lin('F08A24'), orange2=lin('F7A54A'), amber=lin('F2B03C'), deep=lin('0B0B0C'), deep2=lin('141416'),
         win=lin('161617'), panel=lin('1C1C1E'), panel2=lin('242427'), line=lin('2F2F33'), field=lin('2C2C30'),
         txt=lin('ECECEE'), txt2=lin('A0A0A8'), txt3=lin('63636B'), pink=lin('C9577F'), blue=lin('4C7BD9'),
         green=lin('3FAE6A'), red=lin('E5483B'), white=[1, 1, 1, 1], canvas=lin('0F0F10'), black=[0, 0, 0, 1])
BEZ = dict(expo=(0.16, 1, 0.3, 1), decel=(0.05, 0.7, 0.1, 1), std=(0.2, 0, 0, 1), accel=(0.3, 0, 0.8, 0.15),
           inout=(0.87, 0, 0.13, 1), back=(0.34, 1.56, 0.64, 1), pop=(0.34, 1.75, 0.64, 1), soft=(0.45, 0, 0.2, 1),
           smooth=(0.65, 0, 0.35, 1), quint=(0.22, 1, 0.36, 1), whip=(0.7, 0, 0.1, 1))

def P(x, y): return [round(x / W, 5), round(1 - y / H, 5)]

def keys(spec):
    """spec: [(frame, value, ease)]; ease = Linear|Ease in|Ease out|S-curve|Hold|bez-name|(x1,y1,x2,y2), arriving."""
    out = []
    for f, v, e in spec:
        k = {'frame': float(f), 'value': v}
        if isinstance(e, str) and e in BEZ: e = BEZ[e]
        if isinstance(e, (tuple, list)):
            k['easing'] = 'Custom'; k['customEase'] = [float(x) for x in e]
        else:
            k['easing'] = e
        out.append(k)
    return out


class Obj:
    def __init__(self, comp, clip, kind):
        self.c = comp; self.clip = clip; self.id = clip['id']; self.kind = kind
        self.base = None; self.f0 = clip.get('left', 0.0) / 4.0 - (clip.get('sourceIn', 0.0) if kind == 'nest' else 0.0)   # keys: clip-local (nested: source) frames
    def tr(self, p): return f'tr.e_tr_placement_{self.id}.{p}'
    def src(self, cap, p): return f'src.e_src_{cap}_{self.id}.{p}'
    def set(self, key, v):
        pr = self.clip['properties'].setdefault(key, {'keyframes': [], 'static': v})
        pr['static'] = v; return self
    def key(self, key, spec):
        pr = self.clip['properties'].setdefault(key, {'keyframes': [], 'static': spec[-1][1]})
        pr['keyframes'] = keys([(f - self.f0, v, e) for f, v, e in spec]); return self
    def addkeys(self, key, spec):
        pr = self.clip['properties'].setdefault(key, {'keyframes': [], 'static': spec[-1][1]})
        ks = pr['keyframes'] + keys([(f - self.f0, v, e) for f, v, e in spec]); ks.sort(key=lambda k: k['frame']); pr['keyframes'] = ks; return self
    def pos(self, spec): return self.key(self.tr('position'), spec)
    def at(self, x, y): self.base = P(x, y); return self.set(self.tr('position'), self.base)
    def scale(self, spec): return self.key(self.tr('scale'), [(f, [v, v] if not isinstance(v, list) else v, e) for f, v, e in spec])
    def sc(self, v): return self.set(self.tr('scale'), [v, v] if not isinstance(v, list) else v)
    def op(self, spec): return self.key(self.tr('opacity'), spec)
    def opv(self, v): return self.set(self.tr('opacity'), v)
    def rot(self, spec): return self.key(self.tr('rotation'), spec)
    def rotv(self, v): return self.set(self.tr('rotation'), v)
    def anchor(self, ax, ay):
        """pivot in half-sizes (-1 left/bottom, +1 right/top). In raw JSON the position stays the geometry centre (no compensation)."""
        return self.set(self.tr('anchor'), [ax, ay])
    def mode(self, m): return self.set(f'tr.e_tr_compositing_{self.id}.blend', m)
    def fx(self, cap, **params):
        ents = self.clip['containers'].setdefault('effects', {'entries': [], 'promoted': []})['entries']
        n = sum(1 for e in ents if e['cap'] == cap)
        eid = f'e_fx_{cap}_{self.id}' + ('' if n == 0 else f'_{n + 1}')
        ents.append({'id': eid, 'cap': cap, 'on': True})
        dflt = dict(glow=dict(amount=0.6, size=10.0, blend=0.2), trim=dict(start=0.0, end=1.0, offset=0.0),
                    blur=dict(size=0.0, clipping='frame'), shadow=dict(x=0.0, y=-0.006, softness=0.02, opacity=0.4),
                    motionblur=dict(shutter=180.0, samples=16.0)).get(cap, {})
        dflt.update(params)
        for k, v in dflt.items(): self.set(f'fx.{eid}.{k}', v)
        return f'fx.{eid}'
    def glow(self, size=10, amount=0.55, blend=0.2): return self.fx('glow', size=float(size), amount=amount, blend=blend)
    def shadow(self, y=-0.005, soft=0.02, op=0.35, x=0.0): return self.fx('shadow', x=x, y=y, softness=soft, opacity=op)
    def mblur(self, shutter=180): return self.fx('motionblur', shutter=float(shutter), samples=16.0)
    def blur(self, spec=None, size=0.0):
        p = self.fx('blur', size=float(size))
        if spec: self.key(p + '.size', spec)
        return p
    def trim(self, spec, which='end'):
        p = self.fx('trim', start=0.0, end=1.0, offset=0.0); self.key(p + '.' + which, spec); return p
    def fill(self, col, paint='solid'):
        self.set(self.src('shape_fill', 'paint'), paint); return self.set(self.src('shape_fill', 'color'), col)
    def nofill(self): return self.set(self.src('shape_fill', 'paint'), 'none')
    def stroke(self, col, px=1.5, cap='round', line='solid', dash=None, gap=None):
        self.set(self.src('shape_stroke', 'paint'), 'solid'); self.set(self.src('shape_stroke', 'color'), col)
        self.set(self.src('shape_stroke', 'width'), round(px / W, 6)); self.set(self.src('shape_stroke', 'cap'), cap)
        if line != 'solid':
            self.set(self.src('shape_stroke', 'line'), line)
            if dash: self.set(self.src('shape_stroke', 'dashLength'), dash / W)
            if gap: self.set(self.src('shape_stroke', 'dashGap'), gap / W)
        return self
    def nostroke(self): return self.set(self.src('shape_stroke', 'paint'), 'none')
    def soft(self, px): return self.set(self.src('shape_fill', 'softEdge'), round(px / W, 5))
    def gradient(self, stops, start, end, mode='linear'):
        self.set(self.src('shape_fill', 'paint'), 'gradient')
        g = {'mode': mode, 'stops': [{'p': p, 'color': c[:3], 'a': c[3]} for p, c in stops], 'start': P(*start), 'end': P(*end)}
        return self.set(self.src('shape_fill', 'gradient'), g)
    def pop(self, f, d=14, ease='pop', frm=0.0, to=1.0):
        self.scale([(f, frm, 'Linear'), (f + d, to, ease)]); self.op([(f, 0, 'Linear'), (f + 3, 1, 'Linear')]); return self
    def rise(self, f, dy=40, d=18, ease='expo', fade=True, dx=0):
        bx, by = self.base
        self.pos([(f, [bx - dx / W, by - dy / H], 'Linear'), (f + d, [bx, by], ease)])
        if fade: self.op([(f, 0, 'Linear'), (f + max(4, d // 2), 1, 'Ease out')])
        return self
    def life(self, f_in, f_out, d_in=8, d_out=8):
        return self.op([(f_in, 0, 'Linear'), (f_in + d_in, 1, 'Ease out'), (f_out, 1, 'Linear'), (f_out + d_out, 0, 'accel')])
    def stagger(self, f, by='word', gap=3, dy=0.035, d=14, blur=14, order='forward', scale=None, exit=None):
        rp = f'src.e_src_text_relative_{self.id}.'
        conn = [rp + 'position', rp + 'opacity']
        ents = self.clip['containers'].setdefault('effects', {'entries': [], 'promoted': []})['entries']
        bp = None
        if blur:
            bp = self.blur(size=0.0); conn.append(bp + '.size')
        if scale is not None: conn.append(rp + 'scale')
        ents.insert(0, {'id': f'e_fx_stagger_{self.id}', 'cap': 'stagger', 'on': True, 'by': by, 'order': order,
                        'amount': float(gap), 'amountMode': 'each', 'seed': 1, 'connected': conn})
        ps = [(f, [0, -dy], 'Linear'), (f + d, [0, 0], 'expo')]
        os_ = [(f, 0, 'Linear'), (f + max(3, d // 2), 1, 'Ease out')]
        bs = [(f, blur, 'Linear'), (f + d, 0, 'expo')] if blur else None
        ss = [(f, [scale, scale], 'Linear'), (f + d, [1, 1], 'back')] if scale is not None else None
        if exit:
            ef, ed, edy = exit
            ps += [(ef, [0, 0], 'Linear'), (ef + ed, [0, edy], 'accel')]
            os_ += [(ef, 1, 'Linear'), (ef + ed, 0, 'accel')]
            if bs: bs += [(ef, 0, 'Linear'), (ef + ed, blur * 0.7, 'accel')]
        self.key(rp + 'position', ps); self.key(rp + 'opacity', os_)
        if bs: self.key(bp + '.size', bs)
        if ss: self.key(rp + 'scale', ss)
        return self


class Comp:
    def __init__(self, doc, name, length, code, bin=None):
        self.doc, self.name, self.length, self.code, self.bin = doc, name, length, code, bin
        self.n = 0; self.vtracks = []; self.atracks = []; self.tlid = 'tl_' + code
    def _id(self):
        self.n += 1; return f'{self.code}_{self.n}'
    def _clip(self, tkey, name, f0, dur):
        t = copy.deepcopy(TPL[tkey]); oid = t['id']; nid = self._id()
        t = json.loads(json.dumps(t).replace(oid, nid))
        t['left'] = float(f0) * 4; t['duration'] = float(dur if dur is not None else self.length - f0); t['label'] = name
        for k in t['properties']: t['properties'][k]['keyframes'] = []
        t.setdefault('containers', {}).setdefault('effects', {'entries': [], 'promoted': []})['entries'] = []
        t['properties'] = {k: v for k, v in t['properties'].items() if not k.startswith('fx.')}
        t.pop('parentId', None)
        self.vtracks.append([t]); return t
    def rect(self, name, x, y, w, h, col=None, r=0, f0=0, dur=None, center=False):
        if not center: x, y = x + w / 2, y + h / 2
        o = Obj(self, self._clip('rect', name, f0, dur), 'rect')
        g = 'shape_geometry_rectangle'
        o.set(o.src(g, 'width'), round(w / W, 6)).set(o.src(g, 'height'), round(h / W, 6))
        o.set(o.src(g, 'cornerRadius'), round(min(0.5, 2 * r / max(1e-6, min(w, h))), 4) if r else 0.0)
        o.nostroke(); o.fill(col) if col is not None else o.nofill()
        return o.at(x, y)
    def ell(self, name, x, y, w, h=None, col=None, f0=0, dur=None):
        h = w if h is None else h
        o = Obj(self, self._clip('ellipse', name, f0, dur), 'ellipse')
        g = 'shape_geometry_ellipse'
        o.set(o.src(g, 'width'), round(w / W, 6)).set(o.src(g, 'height'), round(h / W, 6))
        o.nostroke(); o.fill(col) if col is not None else o.nofill()
        return o.at(x, y)
    def ngon(self, name, x, y, w, sides, col, f0=0, dur=None, angle=0.0):
        o = Obj(self, self._clip('polygon', name, f0, dur), 'ngon'); g = 'shape_geometry_ngon'
        o.set(o.src(g, 'width'), round(w / W, 6)).set(o.src(g, 'height'), round(w / W, 6)).set(o.src(g, 'sides'), sides).set(o.src(g, 'angle'), angle)
        o.nostroke(); o.fill(col); return o.at(x, y)
    def star(self, name, x, y, w, sides, inner, col, f0=0, dur=None):
        o = Obj(self, self._clip('star', name, f0, dur), 'star'); g = 'shape_geometry_star'
        o.set(o.src(g, 'width'), round(w / W, 6)).set(o.src(g, 'height'), round(w / W, 6)).set(o.src(g, 'sides'), sides).set(o.src(g, 'innerRadius'), inner)
        o.nostroke(); o.fill(col); return o.at(x, y)
    def path(self, name, pts, f0=0, dur=None, closed=False, handles=None):
        o = Obj(self, self._clip('path', name, f0, dur), 'path')
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
        nodes = []
        for i, (x, y) in enumerate(pts):
            hi, ho, cr = ((0, 0), (0, 0), True) if handles is None else handles[i]
            nodes.append({'x': 0.5 + (x - cx) / W, 'y': 0.5 + (y - cy) / H, 'inX': hi[0] / W, 'inY': hi[1] / H,
                          'outX': ho[0] / W, 'outY': ho[1] / H, 'corner': bool(cr)})
        o.clip['shape'] = {'kind': 'path', 'params': {'closed': closed, 'points': nodes}}
        o.nostroke(); o.nofill()
        return o.at(cx, cy)
    def line(self, name, pts, col, px=2, f0=0, dur=None, closed=False, handles=None):
        o = self.path(name, pts, f0, dur, closed, handles); o.stroke(col, px); return o
    def asset(self, prefix, key, cx, cy, s, f0=0, dur=None, fill=None, tile=None):
        out = []
        for i, part in enumerate(ASSETS[key]):
            pts = []; hs = []
            for q in part['pts']:
                pts.append((cx + q[0] * s, cy + q[1] * s))
                hs.append(((q[2] * s, q[3] * s), (q[4] * s, q[5] * s), bool(q[6])) if len(q) > 2 else ((0, 0), (0, 0), True))
            col = part['fill']
            if fill is not None and col != 'tile': col = fill
            if col == 'tile': col = tile
            col = list(col) + [1] if len(col) == 3 else list(col)
            o = self.path(f'{prefix} {i}', pts, f0, dur, True, hs); o.fill(col); out.append(o)
        return out
    def text(self, name, s, x, y, px, col, f0=0, dur=None, style='Bold', font='Rethink Sans', align='left', track=None, lh=None):
        o = Obj(self, self._clip('textplain', name, f0, dur), 'text')
        o.clip['text'] = s; size = round(max(0.01, px / EM), 5)
        o.clip['textProps'].update(font=font, style=style, size=size, fontResolved=font)
        o.set(o.src('text_content', 'content'), s)
        o.set(o.src('text_font', 'family'), font).set(o.src('text_font', 'style'), style).set(o.src('text_font', 'size'), size)
        o.set(o.src('text_fill', 'color'), col).set(o.src('text_fill', 'paint'), 'solid')
        o.set(o.src('text_layout', 'align'), align); o.set(o.src('text_layout', 'clip'), False)
        if track: o.set(o.src('text_font', 'tracking'), track); o.clip['textProps']['tracking'] = track
        if lh: o.set(o.src('text_font', 'lineSpacing'), lh); o.clip['textProps']['lineSpacing'] = lh
        return o.at(x, y)
    def nest(self, name, comp, f0=0, dur=None, src_in=0, x=960, y=540):
        tid = comp.tlid if isinstance(comp, Comp) else comp
        t = copy.deepcopy(TPL['nest']); oid = t['id']; nid = self._id()
        t = json.loads(json.dumps(t).replace(oid, nid))
        t.update(nestedTimelineId=tid, left=float(f0) * 4, duration=float(dur if dur is not None else self.length - f0),
                 sourceIn=float(src_in), text=name, label=name)
        for k in t['properties']: t['properties'][k]['keyframes'] = []
        t['containers'].setdefault('effects', {'entries': [], 'promoted': []})
        self.vtracks.append([t]); o = Obj(self, t, 'nest'); return o.at(x, y)
    def null(self, name, x=960, y=540, f0=0, dur=None):
        o = self.ell(name, x, y, 4, 4, C['orange'], f0, dur); o.opv(0.0); return o
    def adjust(self, name, f0=0, dur=None):
        return Obj(self, self._clip('adjust', name, f0, dur), 'adj')
    def parent(self, children, par):
        for ch in children: ch.clip['parentId'] = par.id
    def audio(self, name, path, f0, dur_frames, gain_db=0.0):
        mid = self.doc.media_id(path)
        t = copy.deepcopy(TPL['audio']); oid = t['id']; nid = self._id()
        t = json.loads(json.dumps(t).replace(oid, nid))
        t.update(left=float(f0) * 4, duration=float(dur_frames), text=os.path.basename(path.replace('\\', '/')), label=name)
        t['media'] = {'id': mid, 'path': path, 'kind': 'audio'}
        t['properties'][f'src.e_src_media_audio_{nid}.gain'] = {'keyframes': [], 'static': gain_db}
        self.atracks.append([t]); return t
    def scene(self):
        tracks = [{'id': f'track_v{i + 1}', 'enabled': True, 'clips': cl} for i, cl in enumerate(self.vtracks)]
        atr = [{'id': f'atrack_{i + 1}', 'enabled': True, 'clips': cl} for i, cl in enumerate(self.atracks)] or [{'id': 'atrack_1', 'enabled': True, 'clips': []}]
        return {'ppf': 4, 'sceneFps': 30.0, 'duration': float(self.length), 'timelineWidth': 1920, 'timelineHeight': 1080,
                'width': 1920, 'height': 1080, 'tracks': tracks, 'audioTracks': atr, 'clipCounter': self.n}


class Doc:
    def __init__(self, path):
        self.path = path; self.d = json.load(open(path)); self.comps = []
    def media_id(self, path):
        for m in self.d['media']:
            if m['path'] == path: return m['id']
        mid = f'media_v3_{len(self.d["media"]) + 1}'
        self.d['media'].append({'id': mid, 'name': os.path.basename(path.replace('\\', '/')), 'path': path, 'kind': 'audio'})
        return mid
    def bin(self, name):
        for b in self.d['bins']:
            if b['name'] == name: return b['id']
        bid = f'bin_v3_{len(self.d["bins"]) + 1}'
        self.d['bins'].append({'id': bid, 'name': name, 'parent': None}); return bid
    def comp(self, name, length, code, bin=None):
        c = Comp(self, name, length, code, bin); self.comps.append(c); return c
    def save(self, keep=()):
        tls = [t for t in self.d['timelines'] if t['name'] in keep]
        for c in self.comps:
            tls.append({'id': c.tlid, 'name': c.name, 'scene': c.scene(), 'bin': self.bin(c.bin) if c.bin else None})
        self.d['timelines'] = tls; self.d['lastTimelineId'] = tls[-1]['id']
        used = {t.get('bin') for t in tls}
        self.d['bins'] = [b for b in self.d['bins'] if b['id'] in used]
        json.dump(self.d, open(self.path, 'w'), separators=(',', ':'))


# ---------------------------------------------------------------- master-time curves split across subscenes
def _bez(e):
    if isinstance(e, str):
        if e in BEZ: return BEZ[e]
        return {'Linear': (0, 0, 1, 1), 'Ease out': (0, 0, 0.58, 1), 'Ease in': (0.42, 0, 1, 1), 'S-curve': (0.42, 0, 0.58, 1)}[e]
    return tuple(e)

def _cub(p0, p1, p2, p3, u):
    a = 1 - u
    return a * a * a * p0 + 3 * a * a * u * p1 + 3 * a * u * u * p2 + u * u * u * p3

def _solve_u(x1, x2, t):
    lo, hi = 0.0, 1.0
    for _ in range(60):
        m = (lo + hi) / 2
        if _cub(0, x1, x2, 1, m) < t: lo = m
        else: hi = m
    return (lo + hi) / 2

def _split(b, ua, ub):
    """sub-curve of unit bezier b between params ua..ub, renormalised -> (x1,y1,x2,y2) or None if flat"""
    P = [(0.0, 0.0), (b[0], b[1]), (b[2], b[3]), (1.0, 1.0)]
    def dc(pts, u):
        a = [((1 - u) * pts[i][0] + u * pts[i + 1][0], (1 - u) * pts[i][1] + u * pts[i + 1][1]) for i in range(3)]
        bb = [((1 - u) * a[i][0] + u * a[i + 1][0], (1 - u) * a[i][1] + u * a[i + 1][1]) for i in range(2)]
        c = ((1 - u) * bb[0][0] + u * bb[1][0], (1 - u) * bb[0][1] + u * bb[1][1])
        return [pts[0], a[0], bb[0], c], [c, bb[1], a[2], pts[3]]
    _, right = dc(P, ua)
    ub2 = (ub - ua) / (1 - ua) if ua < 1 else 1.0
    left, _ = dc(right, ub2)
    q0, q1, q2, q3 = left
    dx, dy = q3[0] - q0[0], q3[1] - q0[1]
    if abs(dx) < 1e-9: return None
    if abs(dy) < 1e-9: return 'flat'
    return ((q1[0] - q0[0]) / dx, (q1[1] - q0[1]) / dy, (q2[0] - q0[0]) / dx, (q2[1] - q0[1]) / dy)

def _lerp(a, b, t):
    if isinstance(a, list): return [x + (y - x) * t for x, y in zip(a, b)]
    return a + (b - a) * t

class Curve:
    """master keys [(frame, value, ease_arriving)] -> local key specs for any window."""
    def __init__(self, spec): self.k = sorted(spec, key=lambda s: s[0])
    def value(self, f):
        k = self.k
        if f <= k[0][0]: return k[0][1]
        if f >= k[-1][0]: return k[-1][1]
        for i in range(len(k) - 1):
            f0, v0, _ = k[i]; f1, v1, e = k[i + 1]
            if f0 <= f <= f1:
                b = _bez(e); u = _solve_u(b[0], b[2], (f - f0) / (f1 - f0))
                return _lerp(v0, v1, _cub(0, b[1], b[3], 1, u))
    def window(self, a, b, shift=None):
        """keys for master window [a,b] expressed in local frames (local = master - a, or - shift)."""
        sh = a if shift is None else shift
        out = [(0 + a - sh, self.value(a), 'Linear')]
        k = self.k
        if a < k[0][0] < b: out.append((k[0][0] - sh, k[0][1], 'Linear'))   # hold before the first key
        for i in range(len(k) - 1):
            f0, v0, _ = k[i]; f1, v1, e = k[i + 1]
            lo, hi = max(f0, a), min(f1, b)
            if hi <= lo: continue
            bz = _bez(e)
            ua = _solve_u(bz[0], bz[2], (lo - f0) / (f1 - f0)); ub = _solve_u(bz[0], bz[2], (hi - f0) / (f1 - f0))
            s = _split(bz, ua, ub)
            ee = 'Linear' if s in (None, 'flat') else s
            if out[-1][0] == lo - sh and lo != a: pass
            out.append((hi - sh, self.value(hi), ee))
        if out[-1][0] < b - sh: out.append((b - sh, self.value(b), 'Linear'))
        # drop duplicate first key frames
        res = []
        for kk in out:
            if res and abs(res[-1][0] - kk[0]) < 1e-6: res[-1] = kk
            else: res.append(kk)
        return res


_FONTS = {}
def textw(s, px, style='Bold'):
    """advance width in px of Rethink Sans text (matches Carvercat within ~1%)."""
    from PIL import ImageFont
    k = (round(px * 4), style)
    if k not in _FONTS:
        f = ImageFont.truetype(os.path.join(HERE, 'RethinkSans.ttf'), max(1, round(px * 4)))
        f.set_variation_by_name(style.encode()); _FONTS[k] = f
    return _FONTS[k].getlength(s) / 4
