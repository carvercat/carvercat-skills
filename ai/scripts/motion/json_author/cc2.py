"""cc2.py - author Carvercat comps in DESIGN UNITS and send them with scene.apply.

The design-unit successor of cc.py. Same builder shape (Doc > Comp > Obj), but every number is a design unit
(see ai/references/app/design-units.md):

    px from the frame's top-left, y down  |  degrees clockwise  |  frames  |  CSS colours ('#RRGGBB')
    CSS easing ('linear', 'ease-out', 'cubic-bezier(...)', 'steps(1, jump-end)' = hold)  |  fontSize in px

Nothing here writes the stored file. A Comp becomes ONE scene document (carvercat/2.0); `Doc.send(client)` creates the
comps in the app with scene.apply, adds what a scene cannot say yet (motion blur, nested comps, null parents), and
`edit.save` writes the carvercat/2 project. Template extraction then reads that saved file (comp_to_template.py).

Position keys (`pos`) take the CENTRE of the object in px, like `at()`; the builder turns them into the box x/y the
scene wants. `base` is the centre at rest, in px.
"""
import json, math, os, re

W, H = 1920, 1080
HERE = os.path.dirname(os.path.abspath(__file__))

# CSS easings. The named curves are the same ones the old kit called expo, accel, smooth ...
BEZ = dict(expo=(0.16, 1, 0.3, 1), decel=(0.05, 0.7, 0.1, 1), std=(0.2, 0, 0, 1), accel=(0.3, 0, 0.8, 0.15),
           inout=(0.87, 0, 0.13, 1), back=(0.34, 1.56, 0.64, 1), pop=(0.34, 1.75, 0.64, 1), soft=(0.45, 0, 0.2, 1),
           smooth=(0.65, 0, 0.35, 1), quint=(0.22, 1, 0.36, 1), whip=(0.7, 0, 0.1, 1))
HOLD = 'steps(1, jump-end)'

# The old app model's three named curves (the v1 kit's 'Ease in', 'Ease out', 'S-curve'). `ease()` maps those NAMES to the CSS curves
# (ease-in / ease-out / ease-in-out), which are other curves: a ball falling 160 -> 780 px sat 28 px off at frame 15. A pack converted
# from v1 keeps its look with `Doc(legacy_ease=True)` (the names then mean the model curves), or by naming the curve outright:
# 'v1-ease-in', 'v1-ease-out', 'v1-s-curve' (or the tuples OLD_EASE[...]) in any key.
OLD_EASE = {'Ease in': (1 / 3, 0, 2 / 3, 1 / 3), 'Ease out': (1 / 3, 2 / 3, 2 / 3, 1), 'S-curve': (1 / 3, 0, 2 / 3, 1)}
V1_EASE = {'v1-ease-in': OLD_EASE['Ease in'], 'v1-ease-out': OLD_EASE['Ease out'], 'v1-s-curve': OLD_EASE['S-curve']}
LINE = 1.34            # the font's line height as a multiple of the size (the app's default line box)
TRACK_PX = 1.675       # v1 tracking factor t -> letter spacing (t - 1) * 1.675 * font px (read back from the v1 templates)
HARD_SHADOW_DY = 1080 / 1920   # v1 stored a shadow's x against the frame width and its y against the height: "12, 12" drew 12 px right, 6.75 down
WEIGHTS = dict(Light=300, Regular=400, Medium=500, SemiBold=600, Bold=700, ExtraBold=800)


def css(h, a=1.0):
    """'#RRGGBB' (with an optional alpha 0..1) -> a CSS colour string; '#RRGGBBAA' when alpha is below 1."""
    h = h.lstrip('#').upper()
    if len(h) == 3: h = ''.join(c * 2 for c in h)
    return '#' + h if a >= 1 else '#%s%02X' % (h, round(a * 255))


def ease_(e): return ease(e)


def ease(e):
    """An easing name, a bezier tuple or a CSS string -> CSS easing text."""
    if isinstance(e, (tuple, list)): return 'cubic-bezier(%s)' % ', '.join('%g' % round(x, 5) for x in e)
    if e in BEZ: return ease(BEZ[e])
    if e in V1_EASE: return ease(V1_EASE[e])
    return {'Linear': 'linear', 'linear': 'linear', 'Ease out': 'ease-out', 'Ease in': 'ease-in', 'S-curve': 'ease-in-out',
            'Hold': HOLD, 'hold': HOLD}.get(e, e)


def bezier(points, closed=False):
    """SVG path data (px, y down) from bezier points.

    Each point is (x, y) or (x, y, (inDx, inDy), (outDx, outDy)): handle OFFSETS from the node, as the pen tool keeps them
    (a missing handle is a corner on that side). Segments between two points with no handles are straight lines."""
    pts = []
    for p in points:
        x, y = p[0], p[1]
        hin = tuple(p[2]) if len(p) > 2 and p[2] else None
        hout = tuple(p[3]) if len(p) > 3 and p[3] else None
        pts.append((x, y, hin, hout))
    d = ['M %g %g' % (pts[0][0], pts[0][1])]
    seq = pts + ([pts[0]] if closed else [])
    for a, b in zip(seq, seq[1:]):
        if a[3] is None and b[2] is None: d.append('L %g %g' % (b[0], b[1]))
        else:
            c1 = (a[0] + a[3][0], a[1] + a[3][1]) if a[3] else (a[0], a[1])
            c2 = (b[0] + b[2][0], b[1] + b[2][1]) if b[2] else (b[0], b[1])
            d.append('C %g %g %g %g %g %g' % (c1[0], c1[1], c2[0], c2[1], b[0], b[1]))
    if closed: d.append('Z')
    return ' '.join(d)


def path_box(d):
    """The true bounding box (x, y, w, h) in px of SVG path data made of M, L, C and Z (what `bezier()` writes): the extent of the
    drawn centre line, curves included. An extent under 1 px counts as 1 px (the app reads a zero extent that way)."""
    nums = lambda t: [float(v) for v in re.findall(r'-?\d+(?:\.\d+)?(?:e-?\d+)?', t)]
    toks = re.findall(r'([MLCZ])([^MLCZ]*)', d)
    xs, ys, cur = [], [], None
    for cmd, args in toks:
        v = nums(args)
        if cmd in 'ML': cur = (v[0], v[1]); xs.append(cur[0]); ys.append(cur[1])
        elif cmd == 'C':
            c1, c2, p = (v[0], v[1]), (v[2], v[3]), (v[4], v[5])
            for ax, out in ((0, xs), (1, ys)):
                p0, p1, p2, p3 = cur[ax], c1[ax], c2[ax], p[ax]
                qa, qb, qc = -p0 + 3 * p1 - 3 * p2 + p3, 2 * (p0 - 2 * p1 + p2), p1 - p0
                roots = []
                if abs(qa) < 1e-9:
                    if abs(qb) > 1e-9: roots = [-qc / qb]
                else:
                    disc = qb * qb - 4 * qa * qc
                    if disc >= 0: roots = [(-qb + sg * math.sqrt(disc)) / (2 * qa) for sg in (1, -1)]
                for t in roots:
                    if 0 < t < 1: out.append((1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t * t * p2 + t ** 3 * p3)
                out.append(p3)
            cur = p
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    w, h = x1 - x0, y1 - y0
    if w < 1: x0, w = x0 - (1 - w) / 2, 1.0
    if h < 1: y0, h = y0 - (1 - h) / 2, 1.0
    return x0, y0, w, h


def track_px(track, px, per_em=TRACK_PX):
    """A v1 tracking factor (1.0 normal, 1.3 wide) -> letter spacing in px"""
    return 0.0 if not track else round((track - 1.0) * per_em * px, 3)


class Obj:
    def __init__(self, comp, sid, kind, name, box, style, f0, dur):
        self.c, self.id, self.kind, self.name = comp, sid, kind, name
        self.box = box                      # (cx, cy, w, h) at rest, px
        self.base = (box[0], box[1])
        self.style, self.f0, self.dur = style, f0, dur
        self.tracks = {}                    # key -> [(frame, value, arriving ease)]
        self.children = []
        self.motionblur = None
        self.parent = None
        self.d = None                       # path data (kind 'path')
        self.stagger_spec = None            # text stagger (kind 'text')

    # -- static values -------------------------------------------------------------------------------------------
    def set(self, key, v): self.style[key] = v; return self
    def sc(self, v): return self.set('scale', v)
    def opv(self, v): return self.set('opacity', v)
    def rotv(self, v): return self.set('rotate', v)
    def mode(self, m): return self.set('mixBlendMode', m)

    # -- animated values (frames are COMP frames; stored object-relative) ------------------------------------------
    def key(self, key, spec):
        self.tracks[key] = [(f - self.f0, v, e) for f, v, e in spec]; return self
    def pos(self, spec):
        """spec [(frame, (cx, cy), ease)] - the centre in px"""
        return self.key('pos', spec)
    def scale(self, spec): return self.key('scale', spec)
    def op(self, spec): return self.key('opacity', spec)
    def rot(self, spec): return self.key('rotate', spec)
    def blur(self, spec): return self.key('blur', spec)
    def trim(self, spec, which='end'): return self.key('trim' + which.capitalize(), [(f, '%g%%' % (v * 100 if v <= 1 else v), e) for f, v, e in spec])

    # -- text: one key per property, each with its own ease; a stagger plays a tween over the parts --------------------------
    def tracking(self, spec): return self.key('letterSpacing', spec)
    def line_height(self, v): return self.set('lineHeight', round(v, 4))
    def size(self, spec): return self.key('fontSize', spec)
    def leading(self, spec): return self.key('lineHeight', spec)
    def colour(self, spec, prop='fill'): return self.key(prop, spec)
    def stagger(self, by='chars', each=None, amount=None, from_='start', ease=None, keyframes=None):
        """Play `keyframes` on every part of this text (by 'chars', 'words' or 'lines'), `each` frames/time apart (or
        `amount` in total). The tween every part plays is either `keyframes` [(at, {props}, ease)] here, or, when none are
        given, the object's own keys (pos/opacity/tracking ...): the scene takes them in ONE place, so a text with its own
        keys and `keyframes` here is refused when the scene is built."""
        st = {'target': by, 'from': from_}
        if amount is not None: st['amount'] = amount
        else: st['each'] = each if each is not None else 2
        if ease: st['ease'] = ease
        if keyframes:
            st['keyframes'] = [dict(at=a, props=p, **({'ease': self.c.doc.ease(e)} if e else {})) for a, p, e in keyframes]
        self.stagger_spec = st; return self
    def child(self, other):
        """parent `other` to this object: its box is then measured from this object's top-left (set by the builder)"""
        other.parent = self; self.children.append(other)
        if other in self.c.objs: self.c.objs.remove(other)
        return other
    def origin(self):
        """top-left of this object's own box in comp px: where its children's x, y count from"""
        cx, cy, w, h = self.box
        return (cx - 50, cy - 50) if self.kind == 'null' else (cx - w / 2, cy - h / 2)

    # -- looks -----------------------------------------------------------------------------------------------------
    def fill(self, col): return self.set('fill', col)
    def nofill(self): return self.set('fill', 'none')
    def stroke(self, col, px=1.5, cap='round'):
        self.set('stroke', col).set('strokeWidth', px); return self.set('strokeLinecap', cap)
    def glow(self, size=10, amount=0.55, blend=0.2, color='#FFFFFF'):
        return self.set('glow', '%gpx %s %g %g' % (size, color, amount, blend))
    def shadow(self, x=0, y=6, blur=8, color='#00000066'):
        return self.set('dropShadow', '%gpx %gpx %gpx %s' % (x, y, blur, color))
    def hard_shadow(self, color, dx=12, dy=None):
        """A hard offset shadow (no blur): dx px right, dy px down. The default dy is dx * 9/16, how the v1 kit drew a square "dx, dy"
        shadow (its y was a share of the frame height, its x of the width)."""
        dy = dx * HARD_SHADOW_DY if dy is None else dy
        return self.set('dropShadow', '%gpx %gpx 0px %s' % (dx, round(dy, 3), color))
    def mblur(self, shutter=180): self.motionblur = shutter; return self
    def gradient_keys(self, spec):
        """Key a shape gradient's endpoints (object-local, 0..1, y down): spec [(frame, (sx, sy), (ex, ey), ease)], the ease leaves that
        key. A scene key cannot carry gradient endpoints, so `Doc.send` sets them with key.set (`shape.fill.gradientStart/End`)."""
        self.gkeys = [(f, e, {'gradientStart': list(a), 'gradientEnd': list(b)}) for f, a, b, e in spec]; return self
    def tracking_factor(self, spec, per_em=TRACK_PX):
        """Key the letter spacing from v1 tracking factors (1.0 = normal): spec [(frame, factor, ease)]; needs `px` (set by text_at)"""
        return self.tracking([(f, track_px(v, self.px, per_em), e) for f, v, e in spec])
    def gradient(self, stops, start, end):
        """stops [(0..1, '#hex')]; start/end in comp px (y down). Written as a CSS linear gradient at that angle."""
        dx, dy = end[0] - start[0], end[1] - start[1]
        ang = round(math.degrees(math.atan2(dx, -dy)) % 360, 2)
        return self.set('fill', 'linear-gradient(%gdeg, %s)' % (ang, ', '.join('%s %g%%' % (c, round(p * 100, 2)) for p, c in stops)))

    # -- scene document ------------------------------------------------------------------------------------------
    def node(self):
        cx, cy, w, h = self.box
        ox, oy = self.parent.origin() if self.parent is not None else (0, 0)
        nullish = self.kind == 'null'
        pathish = self.kind == 'path'
        if pathish: style = {}
        elif nullish: style = {'x': round(cx - 50 - ox, 3), 'y': round(cy - 50 - oy, 3)}
        else: style = {'x': round(cx - w / 2 - ox, 3), 'y': round(cy - h / 2 - oy, 3)}
        if self.kind in ('rect', 'ellipse', 'polygon', 'star', 'text'): style.update(width=w, height=h)
        style.update(self.style)
        n = {'id': self.id, 'type': self.kind, 'name': self.name, 'style': style}
        if self.f0: n['start'] = self.f0
        if self.dur is not None: n['duration'] = self.dur
        if getattr(self, 'text', None) is not None: n['text'] = self.text
        if self.d is not None: n['d'] = self.d
        if self.stagger_spec:
            if self.stagger_spec.get('keyframes') and self.tracks:
                raise ValueError('%s: stagger keyframes and the object\'s own keys are two places for one tween; use one' % self.name)
            n['stagger'] = self.stagger_spec
        self.late = {}
        by_frame = {}
        for key, ks in sorted(self.tracks.items()):
            rowsk = []
            for i, (f, v, _) in enumerate(ks):
                e = self.c.doc.ease(ks[i + 1][2]) if i + 1 < len(ks) else None   # arriving -> leaving
                if key == 'pos':
                    dx, dy = (50, 50) if nullish else (w / 2, h / 2)
                    props = {'x': round(v[0] - dx - ox, 3), 'y': round(v[1] - dy - oy, 3)}
                else: props = {key: v}
                rowsk.append((f, e, props))
            clash = any(f in by_frame and e and by_frame[f].get('ease') and by_frame[f]['ease'] != e for f, e, _ in rowsk)
            if clash:                                  # a scene key has ONE ease: this property is keyed after the apply
                self.late[key] = rowsk; continue
            for f, e, props in rowsk:
                row = by_frame.setdefault(f, {'at': f, 'props': {}})
                row['props'].update(props)
                if e and not row.get('ease'): row['ease'] = e
        n['keyframes'] = [by_frame[f] for f in sorted(by_frame)]
        if not n['keyframes']: del n['keyframes']
        if self.children: n['children'] = [c.node() for c in self.children]
        return n


def find_instance(objects, name, start):
    """The nested-comp instance called `name` that starts at comp frame `start`, from a carvercat_list `objects` list: kind
    'nestedTimeline' (0.1.8.1 reports no `comp` to match on). Raises when none or several fit."""
    hit = [o for o in objects if o.get('kind') == 'nestedTimeline' and o.get('name') == name and abs(float(o.get('start', -1)) - start) < 0.5]
    if len(hit) != 1: raise LookupError('instance %r at frame %s: %d found' % (name, start, len(hit)))
    return hit[0]


class Comp:
    def __init__(self, doc, name, length, code, width=W, height=H, fps=30):
        self.doc, self.name, self.length, self.code = doc, name, length, code
        self.width, self.height, self.fps = width, height, fps
        self.objs, self.n, self.masks, self.nests, self.conflicts = [], 0, [], [], []
        self.instance_ops = []              # (child, f0, scale keys, trim_in): what is done to a nested instance once it is placed

    def _new(self, kind, name, box, style, f0, dur):
        self.n += 1
        o = Obj(self, '%s_%d' % (self.code, self.n), kind, name, box, style, f0, dur)
        self.objs.append(o); return o

    def rect(self, name, x, y, w, h, col=None, r=0, f0=0, dur=None, center=False):
        if not center: x, y = x + w / 2, y + h / 2
        st = {'fill': col if col else 'none', 'stroke': 'none'}
        if r: st['borderRadius'] = r
        return self._new('rect', name, (x, y, w, h), st, f0, dur)

    def ell(self, name, x, y, w, h=None, col=None, f0=0, dur=None):
        h = w if h is None else h
        return self._new('ellipse', name, (x, y, w, h), {'fill': col if col else 'none', 'stroke': 'none'}, f0, dur)

    def ngon(self, name, x, y, w, sides, col, f0=0, dur=None, angle=0.0):
        st = {'fill': col, 'stroke': 'none', 'sides': sides}
        if angle: st['rotate'] = angle
        return self._new('polygon', name, (x, y, w, w), st, f0, dur)

    def star(self, name, x, y, w, points, inner, col, f0=0, dur=None):
        """inner is the inner radius as a fraction of the outer one (0.5 = 50%)"""
        return self._new('star', name, (x, y, w, w), {'fill': col, 'stroke': 'none', 'points': points,
                                                      'innerRadius': '%g%%' % (inner * 100)}, f0, dur)

    def text(self, name, s, x, y, px, col, f0=0, dur=None, weight=700, family='Rethink Sans', align='center',
             width=None, tracking=None):
        """Box text centred on (x, y). `width` defaults to a generous box; the text sits in its middle."""
        width = width or max(200, min(W, int(len(s) * px * 0.75) + 40))
        st = {'fill': col, 'fontSize': px, 'fontFamily': family, 'fontWeight': weight, 'textAlign': align,
              'whiteSpace': 'normal', 'verticalAlign': 'middle'}
        if tracking is not None: st['letterSpacing'] = tracking
        o = self._new('text', name, (x, y, width, round(px * 1.4)), st, f0, dur)
        o.text = s; return o

    def null(self, name, x, y, f0=0, dur=None):
        """A null object centred at (x, y): a transform only. Children go under it with `nul.child(obj)`."""
        return self._new('null', name, (x, y, 100, 100), {}, f0, dur)

    def path(self, name, d, col='#FFFFFF', width=2, f0=0, dur=None, cap='round', fill=None, true_box=None):
        """A path object from SVG path data (px, y down, one subpath) or from `bezier(points)`. Open and stroked by
        default; key trimEnd 0 -> 100 to draw it on.

        A path is saved with its points in comp px, and its x/y keys are the top-left of its bounding box. By default the object's box is
        the whole frame (so a `pos` key is that top-left plus half the frame, the v1 convention of the sports/data-viz labs). With
        `true_box=True` (or `Doc(path_boxes=True)`) the box and `base` are the path's TRUE bounding box (path_box): `pos` keys are then the
        CENTRE of the drawn path, like every other object, and `o.box` can be measured."""
        o = self._new('path', name, (self.width / 2, self.height / 2, self.width, self.height),
                      {'fill': fill or 'none', 'stroke': col, 'strokeWidth': width, 'strokeLinecap': cap}, f0, dur)
        o.d = d
        if true_box if true_box is not None else self.doc.path_boxes:
            x, y, w, h = path_box(d)
            o.box = (x + w / 2, y + h / 2, w, h); o.base = (x + w / 2, y + h / 2)
        return o

    def text_at(self, name, s, x, y, px, col, f0=0, dur=None, weight='Bold', align='left', track=None, lh=None, width=None,
                family='Rethink Sans', line=LINE, per_em=TRACK_PX, cap=0.0, char_w=0.62, pad=40):
        """Text anchored at a point: `x` is the left edge, the centre or the right edge (`align`), `y` the centre of the text block (the
        text box is centred on y; `cap` moves it down by that many em). `weight` is a number or a name (Light .. ExtraBold). `track` is a
        v1 tracking factor (1.0 = normal, 1.3 wide), turned into px (track_px). `lh` is the line height as a multiple of the default
        (`line` x size). The box is as wide as the words (`char_w` em a letter plus the tracking, plus `pad` px) unless `width` is given;
        the text never wraps and its overflow is visible. The tracking helpers (`tracking_factor`) need the size, kept as `o.px`."""
        lines = s.split('\n')
        L = line * (lh or 1.0)
        h = round(len(lines) * px * L, 3)
        w = width or min(W, round(max(len(t) for t in lines) * (px * char_w + (track_px(track, px, per_em) if track else 0)) + pad))
        cx = {'left': x + w / 2, 'right': x - w / 2, 'center': x}[align]
        wt = WEIGHTS[weight] if isinstance(weight, str) else weight
        o = self.text(name, s, cx, y + cap * px, px, col, f0=f0, dur=dur, weight=wt, family=family, align=align, width=w)
        o.box = (cx, y + cap * px, w, h); o.base = (cx, y + cap * px)
        o.set('lineHeight', round(L, 4)).set('overflow', 'visible')
        if track: o.set('letterSpacing', track_px(track, px, per_em))
        o.px = px
        return o

    def nest(self, comp, name=None, f0=0, dur=None, track=None):
        """Place another comp of this document in this one as an instance (a precomp), starting at comp frame f0 on `track` (an index,
        'top' = one above every object already there, None = a track with room).
        The child is sent first; the instance is placed after this comp's scene is applied."""
        self.nests.append((comp, name or comp.name, f0, dur, track)); return comp

    def nest_keys(self, child, f0, scale=None, trim_in=None):
        """After the instance of `child` (a comp or its name) placed at comp frame f0 exists (Doc.send): key its scale [(frame, factor, ease)] in this comp's
        frames, and/or move its in edge to comp frame `trim_in` (what dragging the left edge does; the source then starts later). The
        instance is found by kind (nestedTimeline), name and start, as 0.1.8.1 reports no `comp` for it."""
        self.instance_ops.append((child.name if hasattr(child, 'name') else child, f0, scale, trim_in)); return self

    def mask(self, content, window):
        """`window` (an object) cuts `content`: scene mask on the content (the window's shape is the matte)."""
        self.masks.append((content, window))

    def mask_scene(self, ids):
        """second pass (merge): the masks, once every object exists"""
        kids = [{'id': c.id, 'type': c.kind, 'style': {'mask': {'ref': ids[w.id]}}} for c, w in self.masks]
        for node, (c, w) in zip(kids, self.masks):        # a merge needs to know the content: a path says its `d`, a text its words
            if c.kind == 'path': node['d'] = c.d          # (without them the masked path is refused, the masked text comes out empty)
            elif c.kind == 'text': node['text'] = c.text
        return {'schema': 'carvercat/2.0', 'comp': {'width': self.width, 'height': self.height, 'fps': self.fps, 'duration': self.length},
                'children': kids}

    def scene(self):
        return {'schema': 'carvercat/2.0', 'comp': {'width': self.width, 'height': self.height, 'fps': self.fps,
                                                    'duration': self.length},
                'children': [o.node() for o in self.objs]}


class Doc:
    """A set of comps, sent with `send`. Options (all off by default, so a document written before they existed sends exactly as it did):

    legacy_ease   the v1 kit's named eases 'Ease in', 'Ease out', 'S-curve' mean the app model's curves (OLD_EASE), not CSS ease-in/out
    cap_radius    a rect's corner radius is capped at a quarter of its short side (the v1 kit read a pill r = h / 2 as h / 4)
    unparent_masks  after a mask pass, the window is let go of its content (scene masks parent the window to the content they cut;
                  a window that stays where it is drawn must be un-parented: parent.clear)
    path_boxes    paths get their true bounding box as box and base (Comp.path true_box)
    fix_star_names  re-name stars after the apply (an app bug of 0.1.8: a star made by scene.apply lost its name on save)
    final_comp    name of the comp left active when the project is saved (the file records it as lastCompId); default: the last one built
    client_timeout  seconds: raise the client's reply timeout to at least this for the send (big comps take minutes on a busy Mac)
    v1_look       shorthand for legacy_ease + cap_radius + unparent_masks, the three corrections a pack converted from v1 needs
    """
    legacy_ease = cap_radius = unparent_masks = path_boxes = fix_star_names = False
    client_timeout = None
    final_comp = None

    def __init__(self, bin=None, *, legacy_ease=False, cap_radius=False, unparent_masks=False, path_boxes=False, fix_star_names=False,
                 v1_look=False, client_timeout=None):
        self.comps = []
        self.client_timeout = client_timeout
        self.legacy_ease = legacy_ease or v1_look
        self.cap_radius = cap_radius or v1_look
        self.unparent_masks = unparent_masks or v1_look
        self.path_boxes, self.fix_star_names = path_boxes, fix_star_names

    def ease(self, e):
        """an easing name, tuple or CSS string -> CSS easing text, honouring `legacy_ease`"""
        if self.legacy_ease and isinstance(e, str) and e in OLD_EASE: e = OLD_EASE[e]
        return ease(e)

    def cap_radii(self):
        """cap every rect's corner radius at a quarter of its short side (see `cap_radius`)"""
        def walk(o):
            yield o
            for k in o.children: yield from walk(k)
        for c in self.comps:
            for o0 in c.objs:
                for o in walk(o0):
                    r = o.style.get('borderRadius')
                    if r and o.kind == 'rect': o.style['borderRadius'] = round(min(r, min(o.box[2], o.box[3]) / 4), 3)
    def comp(self, name, length, code, **kw):
        c = Comp(self, name, length, code, **kw); self.comps.append(c); return c

    def order(self):
        """comps with every nested comp before the comps that place it"""
        done, out = set(), []
        def visit(c):
            if id(c) in done: return
            done.add(id(c))
            for child, *_ in c.nests: visit(child)
            out.append(c)
        for c in self.comps: visit(c)
        return out

    def send(self, client, save_path):
        """Create every comp in the open document with scene.apply (children of nests first), add motion blur, late keys
        and nested instances, save carvercat/2."""
        index = {}
        if self.client_timeout: client.timeout = max(getattr(client, 'timeout', 120), self.client_timeout)
        if self.cap_radius: self.cap_radii()
        for c in self.order():
            client.run('comp.new', name=c.name)
            reply = client.apply_scene(c.scene())
            ids = dict((reply.get("scene") or {}).get("ids", {}))
            allobjs = []
            def walk(o): allobjs.append(o); [walk(k) for k in o.children]
            for o in c.objs: walk(o)
            if self.fix_star_names:
                for o in allobjs:
                    if o.kind == 'star' and o.id in ids: client.run('clip.rename', id=ids[o.id], name=o.name)
            if c.masks:
                client.apply_scene(c.mask_scene(ids))
                if self.unparent_masks:                      # the pass parented each window to its content: let it go, where it is
                    for content, window in c.masks:
                        client.run('parent.clear', ids=[ids[window.id], ids[content.id]])
            for o in allobjs:
                if o.motionblur is not None:
                    client.run('effect.add', id=ids[o.id], cap='motionblur')
            for o in allobjs:
                for key, rows in o.late.items():
                    client.run('anim.set', id=ids[o.id], keyframes=[dict(at=f, ease=e or 'linear', **p) for f, e, p in rows])
            for o in allobjs:
                for f, e, props in getattr(o, 'gkeys', ()):       # gradient endpoints: stored keys (anim.set has no gradient key); the ease leaves the key
                    for pk, pv in props.items():
                        client.run('key.set', id=ids[o.id], key='shape.fill.' + pk, value=pv, at=f - o.f0, ease=self.ease(e))
            comps = client.tool('carvercat_list')['comps']
            index[id(c)] = next(i['index'] for i in comps if i['name'] == c.name)
            top = None
            for child, name, f0, dur, track in c.nests:
                if track == 'top' and top is not None: track = top
                elif track == 'top':                     # one track above everything already in this comp
                    lst = client.tool('carvercat_list')
                    used = [o['track'] for o in lst['objects']]
                    video = [t['index'] for t in lst['tracks'] if t['kind'] == 'video']
                    above = [t for t in video if not used or t > max(used)]
                    if not above:
                        client.run('track.add'); lst = client.tool('carvercat_list')
                        above = [t['index'] for t in lst['tracks'] if t['kind'] == 'video' and t['index'] > max(used)]
                    track = top = above[0]
                extra = {} if track is None else {'track': track}
                client.run('comp.place', comp=index[id(child)], at=f0, **extra)
            for child, f0, scale, trim_in in c.instance_ops:
                inst = find_instance(client.tool('carvercat_list')['objects'], child, f0)
                if scale:
                    client.run('anim.set', id=inst['id'], keyframes=[dict(at=f - f0, scale=v, ease=self.ease(e) if e else 'linear') for f, v, e in scale])
                if trim_in is not None:
                    client.run('clip.trim', id=inst['id'], edge='in', frame=trim_in)
        lst = client.tool('carvercat_list')                      # the empty default comp a fresh document starts with
        mine = {c.name for c in self.comps}
        busy = {o.get('comp') for o in lst['objects']}
        for c in lst['comps']:
            if c['name'] == 'Comp 1' and 'Comp 1' not in mine and c['id'] == 'tl1':
                client.run('comp.delete', comp=c['index'], check=False)
        if self.final_comp:
            client.run('comp.switch', comp=next(i['index'] for i in client.tool('carvercat_list')['comps'] if i['name'] == self.final_comp))
        client.run('edit.save', path=save_path)
        return save_path
