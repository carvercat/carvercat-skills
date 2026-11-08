"""dvsu_kit.py - helpers shared by the Data Viz and SaaS UI labs, on top of json_author/cc2.py (design units).

cc2 is the design-unit author kit. These two packs were written against the older cc.py with a few conveniences cc2 does not
have; they live here, not in cc2, so the shared kit stays as it is:

  KComp.text(...)     the old call: (x, y) is the text's ANCHOR (its left edge for align='left', its right edge for
                      'right', its middle for 'center'; and 38.4 % down the line box), the weight is a style name.
                      The box is a fixed-width box text that does not wrap; scale and rotation turn about the anchor.
  KComp.line / poly   an open stroked polyline / a closed filled polygon as a path object
  KObj.anchor(ax, ay) the pivot in half-sizes (-1 left or bottom, +1 right or top) -> transformOrigin
  KObj.pos(spec)      keys in px for the ANCHOR (the bbox centre of a path), y down
  KObj.trim_static    a held trim value
  KDoc                a cc2 Doc that also applies library presets (KComp.preset) after the comps exist; the pack's own
                      presets (library/templates/<pack>/*.carverpreset) are copied into the scratch library first.

Units everywhere: px from the top-left, y down, degrees clockwise, '#RRGGBB', frames, CSS easing (old names kept as tuples).
"""
import glob, os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'json_author'))
import cc2
from cc2 import Doc, Comp, Obj, css, bezier, BEZ, HOLD

REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
W, H = 1920, 1080

# the three named curves of the old kit, as the CSS cubic-bezier they were (cc2.OLD_EASE)
OLD_EASE = cc2.OLD_EASE
EASE_OUT, EASE_IN, S_CURVE = OLD_EASE['Ease out'], OLD_EASE['Ease in'], OLD_EASE['S-curve']
WEIGHT = {'Regular': 400, 'Medium': 500, 'SemiBold': 600, 'Bold': 700}
LINE = 1.34                  # the font's line height, a multiple of the size
ANCHOR_Y = 0.496271          # the anchor sits this far down the line box (the digits' ink centre lands on it: measure.boxes)
SOFT = 831.36                # old shadow softness (a fraction of the frame width) -> blur px


def e(x):
    """old ease name -> a value cc2 takes"""
    return OLD_EASE.get(x, x)


def shadow_args(y, soft, op):
    """the old shadow(y=-0.004, soft=0.02, op=0.25) in design units: (y px down, blur px, '#000000AA')"""
    return dict(x=0, y=round(-y * H, 2), blur=round(soft * SOFT, 2), color=css('000000', op))


class KObj(Obj):
    off = (0.0, 0.0)         # box centre minus anchor
    bbox = None              # (left, top, w, h) of a path in px

    def _keys(self, spec): return [(f, v, e(ea)) for f, v, ea in spec]

    def key(self, key, spec): return Obj.key(self, key, self._keys(spec))

    def pos(self, spec):
        """spec [(frame, (x, y), ease)]: the anchor in px (the bbox centre of a path)"""
        out = []
        for f, v, ea in spec:
            x, y = v[0], v[1]
            if self.bbox:                                   # a path keys the bbox top-left; cc2 subtracts half the frame
                x, y = x - self.bbox[2] / 2 + W / 2, y - self.bbox[3] / 2 + H / 2
            else:
                x, y = x + self.off[0], y + self.off[1]
            out.append((f, (x, y), ea))
        return Obj.key(self, 'pos', self._keys(out))

    def addkeys(self, key, spec):
        """more keys on a property that already has some ('pos' spec in anchor px, or scale/opacity/rotate); sorted by frame"""
        before = list(self.tracks.get('pos' if key == 'pos' else key, []))
        if key == 'pos': self.pos(spec)
        else: self.key(key, spec)
        new = self.tracks['pos' if key == 'pos' else key]
        merged = {f: (f, v, ea) for f, v, ea in before}
        merged.update({f: (f, v, ea) for f, v, ea in new})
        self.tracks['pos' if key == 'pos' else key] = [merged[f] for f in sorted(merged)]
        return self

    def trim(self, spec, which='end'):
        return Obj.key(self, 'trim' + which.capitalize(), [(f, '%g%%' % round(v * 100, 4), e(ea)) for f, v, ea in spec])

    def trim_static(self, which, v):
        if v == (1.0 if which == 'end' else 0.0): return self          # the default: a scene refuses 'unchanged'
        return self.set('trim' + which.capitalize(), '%g%%' % round(v * 100, 4))

    def anchor(self, ax, ay):
        """pivot in half-sizes: -1 left/bottom, +1 right/top (y up, as the old kit said it)"""
        return self.set('transformOrigin', '%g%% %g%%' % (round((ax + 1) * 50, 4), round((1 - ay) * 50, 4)))

    def shadow(self, y=-0.005, soft=0.02, op=0.35, **kw):
        return Obj.shadow(self, **shadow_args(y, soft, op))

    def nostroke(self): return self.set('stroke', 'none')

    def tint(self, spec, prop='fill'):
        """a colour key"""
        return Obj.key(self, prop, self._keys(spec))


class KComp(Comp):
    def _new(self, kind, name, box, style, f0, dur):
        self.n += 1
        o = KObj(self, '%s_%d' % (self.code, self.n), kind, name, box, style, f0, dur)
        self.objs.append(o); return o

    def nest_edit(self, child, f0, scale=None, trim_in=None):
        """after the instance of `child` placed at comp frame f0 exists (Doc.send): key its scale [(frame, factor, ease)] in this
        comp's frames, and/or move its in edge to comp frame `trim_in` (what dragging the left edge does; the source then starts later).
        The corner cap, the mask second pass and this are cc2's own now (Doc cap_radius, unparent_masks; Comp.nest_keys)."""
        return self.nest_keys(child, f0, scale=[(f, v, e(ea)) for f, v, ea in scale] if scale else None, trim_in=trim_in)

    def preset(self, label, name):
        """apply a library preset to the object `label` once the comp exists (KDoc.send)"""
        self.doc.presets.append((self.name, label, name))

    def text(self, name, s, x, y, px, col, f0=0, dur=None, style='Bold', family='Rethink Sans', align='left', track=None, lh=None,
             width=None):
        """(x, y) is the anchor (see the module doc). `track` is the old tracking value (1.0 = none): extra space between letters = (track - 1) * 1.58 * size, matched to v1's render."""
        lines = s.split('\n')
        h = round(px * LINE * len(lines), 2)
        sp = round((track - 1) * 1.58 * px, 3) if track is not None else 0     # v1 tracking 1.4 / 1.2 drew 0.62 / 0.33 em wider, measured
        w = width or max(px, round(max(len(l) for l in lines) * (px * 0.56 + sp) + 0.5 * px, 2))
        cx = {'left': x + w / 2, 'right': x - w / 2}.get(align, x)
        ay = ((len(lines) - 1) / 2 + ANCHOR_Y) * px * LINE      # a many-line text is anchored in its middle line
        st = {'fill': col, 'fontSize': px, 'fontFamily': family, 'fontWeight': WEIGHT[style], 'textAlign': align,
              'whiteSpace': 'normal', 'verticalAlign': 'middle', 'overflow': 'visible',
              'transformOrigin': '%s %spx' % ({'left': '0px', 'right': '%gpx' % w}.get(align, '50%'), round(ay, 3))}
        if track is not None: st['letterSpacing'] = sp
        if lh: st['lineHeight'] = lh
        cy = y + h / 2 - ay
        o = self._new('text', name, (cx, cy, w, h), st, f0, dur)
        o.text = s; o.base = (x, y); o.off = (cx - x, cy - y)
        return o

    def _poly(self, name, pts, col, px, f0, dur, closed, fill):
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        o = self.path(name, bezier(pts, closed), col if col else 'none', px or 0, f0, dur, cap='round', fill=fill)
        o.bbox = (min(xs), min(ys), max(xs) - min(xs), max(ys) - min(ys))
        o.base = ((min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2)
        if not col: o.set('stroke', 'none')
        return o

    def line(self, name, pts, col, px=2, f0=0, dur=None):
        """an open stroked polyline through pts (px)"""
        return self._poly(name, pts, col, px, f0, dur, False, None)

    def poly(self, name, pts, f0=0, dur=None):
        """a closed polygon, unfilled and unstroked until you .fill() / .stroke() it"""
        return self._poly(name, pts, None, 0, f0, dur, True, None)


class KDoc(Doc):
    def __init__(self, bin=None):
        Doc.__init__(self, cap_radius=True, unparent_masks=True, client_timeout=900)   # big comps (waffle, heatmap) take minutes on a busy Mac
        self.presets = []

    def comp(self, name, length, code, **kw):
        c = KComp(self, name, length, code, **kw); self.comps.append(c); return c

    def _install_presets(self, client):
        folder = client.run('library.folder')['readings'][0]['path']
        dest = os.path.join(folder, 'templates', 'dvsu-presets')
        os.makedirs(dest, exist_ok=True)
        for pack in ('data-viz', 'saas-ui'):
            for f in glob.glob(os.path.join(REPO, 'library', 'templates', pack, '*.carverpreset')):
                shutil.copy(f, dest)
        client.run('library.reload')

    def send(self, client, save_path):
        if self.presets: self._install_presets(client)
        # the project records the comp that is active when it is saved; these packs have always ended on the last comp their post steps touched
        # (instance edits, else presets, else mask windows), so the files keep the same lastCompId
        ops = [c for c in self.comps if c.instance_ops]
        masked = [c for c in self.comps if c.masks]
        last = ops[-1].name if ops else (self.presets[-1][0] if self.presets else (masked[-1].name if masked else None))
        self.final_comp = last
        Doc.send(self, client, save_path)
        if self.presets:
            comps = {c['name']: c['index'] for c in client.tool('carvercat_list')['comps']}
            cur = None
            for comp, label, name in self.presets:
                if cur != comp: client.run('comp.switch', comp=comps[comp]); cur = comp
                client.run('preset.apply', id='[name="%s"]' % label, name=name)
            if last: client.run('comp.switch', comp=comps[last])
            client.run('edit.save', path=save_path)
        return save_path
