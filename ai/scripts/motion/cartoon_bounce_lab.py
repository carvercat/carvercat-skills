"""Cartoon Bounce lab (round 1) in design units: four comps (bouncing ball, boing title, blink face, smear whoosh).

    import cartoon_bounce_lab as L; doc = L.build(); doc.send(client, PROJECT.carverproj)   # scene.apply per comp, then edit.save

cc2.py kit: px from the top-left, y down; degrees CLOCKWISE; frames; '#RRGGBB'; CSS easing. A key's ease shapes the move
ARRIVING at it (cc2 stores it on the segment): a fall into the ground arrives with 'Ease in', a rise to a peak with 'Ease out'.
Library presets named in PRESETS are applied after each comp's scene (preset.apply, see PDoc) so the templates hold the same
keys the app writes; the .carverpreset builders themselves are build_cartoon_bounce_pack.py (stored preset format, unchanged).
Fonts: Rethink Sans must be installed (KI-136). Docs: ai/patterns/cartoon-bounce.md. Frame 1920x1080, 30 fps.
Extract templates with regen_pack.py (the lab bg is dropped by name).

Helpers shared with the other cartoon_bounce_lab*.py modules live here: PDoc (applies presets), textw/txt (text placed by its
optical centre, left aligned texts by their left edge), outline, origin (pivot as a transformOrigin), line/shape (paths).
"""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "json_author"))
sys.path.insert(0, HERE)
from cc2 import Doc, css, BEZ, bezier
from curves import named, bake
# The old kit's named eases ('Ease in', 'Ease out', 'S-curve') are the app's model curves, and its corner radius was capped at a quarter of
# the short side: cc2's Doc(legacy_ease=True, cap_radius=True) keeps both (PDoc below passes them).

COL = dict(cream=css('FFF4E0'), ink=css('2B1B3D'), red=css('FF5A5F'), yellow=css('FFC93C'), blue=css('3D7DFF'),
           green=css('3CCB7F'), shadow=css('2B1B3D'), white=css('FFFFFF'))
EXPO, BACK = BEZ['expo'], BEZ['back']
PRESETS = []                      # (comp name, object name, library preset name), applied by PDoc after the comp's scene
W, H = 1920, 1080


# ---------------------------------------------------------------- the document: scene.apply + library presets
class PDoc(Doc):
    """cc2.Doc that also runs preset.apply for the (comp, object, preset) rows of `presets` right after a comp's scene is
    applied. The pack's own .carverpreset files are copied into the scratch host's user Library first (library.folder +
    library.reload), so the presets exist in a fresh headless host. Nothing outside that host is touched."""
    def __init__(self, presets=(), pack='cartoon-bounce'):
        super().__init__(legacy_ease=True, cap_radius=True); self.presets, self.pack = presets, pack

    def send(self, client, save_path):
        return super().send(_PresetClient(client, self), save_path)


class _PresetClient:
    def __init__(self, c, doc):
        self._c, self._doc, self._comp, self._done = c, doc, None, set()
        if doc.pack and doc.presets:
            import shutil
            lib = c.run('library.folder')['readings'][0]['path']
            dst = os.path.join(lib, 'templates', doc.pack); os.makedirs(dst, exist_ok=True)
            src = os.path.join(HERE, '..', '..', '..', 'library', 'templates', doc.pack)
            for f in os.listdir(src):
                if f.endswith('.carverpreset'): shutil.copy(os.path.join(src, f), dst)
            c.run('library.reload')

    def __getattr__(self, name): return getattr(self._c, name)

    def run(self, command, **kw):
        if command == 'comp.new': self._comp = kw.get('name')
        return self._c.run(command, **kw)

    def apply_scene(self, scene):
        # A child is placed against its parent's pose at the moment the scene is applied (a parent that starts at scale 0 or a
        # turn of 160 degrees would bake an infinite scale / a wrong place into its children). So the parents' keys are held
        # back, the scene is applied with every parent at rest, and the keys are set afterwards with anim.set.
        import copy
        scene = copy.deepcopy(scene); held = {}
        def hold(n):
            if n.get('children') and n.get('keyframes'): held[n['id']] = n.pop('keyframes')
            for c in n.get('children', []): hold(c)
        for n in scene['children']: hold(n)
        reply = self._c.apply_scene(scene)
        for sid, keys in held.items():
            self._c.run('anim.set', id=(reply.get('scene') or {}).get('ids', {})[sid], keyframes=keys)
        if self._comp not in self._done:                  # the first apply of a comp holds its objects; a second is the mask pass
            self._done.add(self._comp)
            ids = (reply.get('scene') or {}).get('ids', {})
            comp = next(c for c in self._doc.comps if c.name == self._comp)
            by_name = {}
            def walk(o): by_name.setdefault(o.name, o); [walk(k) for k in o.children]
            for o in comp.objs: walk(o)
            for cname, oname, preset in self._doc.presets:
                if cname == self._comp: self._c.run('preset.apply', id=ids[by_name[oname].id], name=preset)
            for o in by_name.values():                        # settings a scene cannot say yet (text outline): property.set
                for key, value in getattr(o, 'post', []):
                    self._c.run('property.set', id=ids[o.id], key=key.replace('{id}', ids[o.id]), value=value)
        return reply


# ---------------------------------------------------------------- text
_FONTS = {}


def textw(s, px, weight=800):
    """advance width in px of Rethink Sans text (800 = ExtraBold, 700 = Bold)"""
    from PIL import ImageFont
    k = (round(px * 4), weight)
    if k not in _FONTS:
        f = ImageFont.truetype(os.path.join(HERE, 'json_author', 'RethinkSans.ttf'), max(1, round(px * 4)))
        f.set_variation_by_name({800: b'ExtraBold', 700: b'Bold'}[weight]); _FONTS[k] = f
    return _FONTS[k].getlength(s) / 4


def lsb(s, px, weight=800):
    """left side bearing of the first letter in px: a left aligned text's box starts this far left of its first ink"""
    from PIL import Image, ImageDraw
    textw(s, px, weight)
    f = _FONTS[(round(px * 4), weight)]
    im = Image.new('L', (int(px * 8), int(px * 8)), 0)
    ImageDraw.Draw(im).text((int(px), int(px)), s[0], font=f, fill=255)
    return (im.getbbox()[0] - int(px)) / 4


def txt(k, name, s, x, y, px, col, f0=0, dur=None, weight=800, align='center', track=None):
    """A one-line text. (x, y) is its optical centre: the middle of the capitals, which the app draws at the middle of the 1.34 x
    size line box (measured against the old files: the ink starts 0.303 x size below the box top, caps are 0.729 x size tall).
    A left aligned text has its first ink at x. `track` is the tracking multiplier of the old kit (1.0 = none): letter
    spacing is (track - 1) / 0.597 em."""
    w = math.ceil(textw(s, px, weight) + (0 if track is None else len(s) * (track - 1) / 0.597 * px)) + 16
    o = k.text(name, s, x, y, px, col, f0=f0, dur=dur, weight=weight, align=align, width=w,
               tracking=None if track is None else round((track - 1) / 0.597 * px, 3))
    o.set('overflow', 'visible')
    o.box = ((x - lsb(s, px, weight) + w / 2) if align == 'left' else x, y, w, round(1.34 * px, 2))
    o.base = (o.box[0], o.box[1])
    if align == 'left': o.set('transformOrigin', '%gpx 50%%' % round(lsb(s, px, weight), 2))   # turns and scales about its first ink, as before
    return o


def outline(t, th=0.08):
    """thick round outline in ink around the letters (centred on the glyph edge, so only its outer half shows); th is the text outline thickness (0..0.2). A scene cannot
    say it, so PDoc sets it with property.set after the scene is applied."""
    p = 'src.e_src_text_outline_{id}.'
    t.post = [(p + 'color', COL['ink']), (p + 'thickness', th), (p + 'corners', 'round')]
    return t


def letter_rows(rows, fade_to=None):
    """stagger keyframes [(at, {props}, ease)] from rows; rows at the same frame are merged (the first row's ease is kept)"""
    out = {}
    for at, props, ease in rows:
        k = round(at, 4)
        if k in out: out[k][1].update(props)
        else: out[k] = [at, dict(props), ease]
    return [tuple(v) for _, v in sorted(out.items())]


def bounce_letters(t, f, each=3, d=18, dy=0.12):
    """each letter drops from dy x frame height above its place and bounces to rest, `each` frames after the one before. The
    tween is the stagger's own keyframes (y is the box top, y down), so every letter plays it in turn; the
    letter fades in over the first d / 2 frames."""
    top = t.box[1] - t.box[3] / 2                  # a stagger key's y is where the letter's box top is, not an offset
    rows = [(p_t * d, {'y': round(top - dy * H * (1 - p), 3)}, 'linear') for p_t, p in bake(named['bounce'], d, 0.01)]
    rows[0] = (rows[0][0], dict(rows[0][1], opacity=0.0), 'Ease out')
    rows.append((max(3, d // 2), {'opacity': 1.0}, 'linear'))
    return t.stagger(by='chars', each=each, keyframes=letter_rows(rows))


def rise(o, f, dy=40, d=18, ease='expo'):
    """starts dy px lower and rises to its place, fading in"""
    bx, by = o.base
    o.pos([(f, (bx, by + dy), 'Linear'), (f + d, (bx, by), ease)])
    o.op([(f, 0.0, 'Linear'), (f + max(4, d // 2), 1.0, 'Ease out')])
    return o


# ---------------------------------------------------------------- shapes
def origin(o, ax, ay):
    """pivot in half-sizes: ax -1 left .. +1 right, ay -1 bottom .. +1 top (0, -1 = the middle of the bottom edge)"""
    return o.set('transformOrigin', '%g%% %g%%' % (50 + 50 * ax, 50 - 50 * ay))


def line(k, name, pts, col, px=2, f0=0, dur=None, handles=None):
    """an open stroked path through pts [(x, y)]; handles [(in, out)] are px offsets from each node (None = none)"""
    if handles is None: d = bezier([tuple(p) for p in pts])
    else: d = bezier([(p[0], p[1], h[0], h[1]) for p, h in zip(pts, handles)])
    return k.path(name, d, col, px, f0=f0, dur=dur)


def shape(k, name, pts, fill, handles=None, f0=0, dur=None):
    """a closed filled path with no stroke (add one with .stroke())"""
    d = bezier([tuple(p) for p in pts], closed=True) if handles is None else \
        bezier([(p[0], p[1], h[0], h[1]) for p, h in zip(pts, handles)], closed=True)
    return k.path(name, d, fill, 0, f0=f0, dur=dur, fill=fill).set('stroke', 'none')


def lab_bg(k, n):
    k.rect("Lab bg", 0, 0, W, H, COL['cream'], f0=0, dur=n)


# ---------------------------------------------------------------- the comps
def bouncing_ball(d):
    n = 90
    k = d.comp("CT Bouncing ball", n, "cbb"); lab_bg(k, n)
    ground = 900; r = 60
    k.rect("Ground", 0, ground, W, 6, COL['ink'], f0=0, dur=n)
    yc = ground - r
    # (frame, centre y, arriving ease): fall, rise, fall, rise, fall, settle
    path = [(0, 220, 'Linear'), (18, yc, 'Ease in'), (31, 460, 'Ease out'), (44, yc, 'Ease in'), (53, 660, 'Ease out'),
            (62, yc, 'Ease in'), (67, yc - 40, 'Ease out'), (72, yc, 'Ease in')]
    contacts = [18, 44, 62, 72]
    sh = k.ell("Shadow", 300, ground + 2, 150, 26, COL['shadow'], f0=0, dur=n)
    ball = k.ell("Ball", 300, yc, 2 * r, 2 * r, COL['red'], f0=0, dur=n)
    origin(ball, 0, -1)                                      # squash on the ground: pivot at the bottom edge
    x0, x1, xf = 300, 1500, 62
    def x_at(f): return x0 + (x1 - x0) * min(f, xf) / xf
    ball.pos([(f, (x_at(f), y), e) for f, y, e in path])
    sh.pos([(f, (x_at(f), ground + 2), 'Linear') for f, y, e in path])
    # shadow grows as the ball nears the ground and fades at height
    sh.scale([(f, 0.45 + 0.55 * (y - 220) / (yc - 220), 'Linear') for f, y, e in path])
    sh.op([(f, round(0.12 + 0.18 * (y - 220) / (yc - 220), 3), 'Linear') for f, y, e in path])
    sc = [(0, [1.0, 1.0], 'Linear')]
    for c in contacts:
        sq = 0.7 if c < 70 else 0.9
        sc += [(c - 2, [0.88, 1.15], 'Linear'), (c, [2 - sq, sq], 'Linear'), (c + 3, [1.0, 1.0], 'Ease out')]
    ball.scale(sc)


def boing_title(d):
    n = 90
    k = d.comp("CT Boing title", n, "cbt"); lab_bg(k, n)
    star = k.star("Burst", 960, 540, 760, 12, 0.72, COL['red'], f0=0, dur=n)
    star.rot([(0, 0.0, 'Linear'), (n, -20.0, 'Linear')])
    PRESETS.append(("CT Boing title", "Burst", "Pop - wobbly"))
    t = txt(k, "Title", "BOING!", 960, 540, 220, COL['yellow'], f0=6, dur=n - 6)
    outline(t, 0.08)
    bounce_letters(t, 6, each=3)                             # each letter drops and bounces, 3 f apart


def blink_face(d):
    n = 100
    k = d.comp("CT Blink face", n, "cbf"); lab_bg(k, n)
    head = k.ell("Head", 960, 540, 420, 420, COL['yellow'], f0=0, dur=n); head.stroke(COL['ink'], 8)
    PRESETS.append(("CT Blink face", "Head", "Jelly in"))
    for side, x in (("Left", 890), ("Right", 1030)):
        e = k.ell(f"Eye {side.lower()}", x, 500, 46, 70, COL['ink'], f0=10, dur=n - 10)
        PRESETS.append(("CT Blink face", f"Eye {side.lower()}", "Pop - wobbly"))
        sc = [(10, [1, 1], 'Linear')]
        for b in (44, 80):                                   # two blinks: 2 f closing, 3 f opening
            sc += [(b, [1, 1], 'Linear'), (b + 2, [1.1, 0.1], 'Ease in'), (b + 5, [1, 1], 'Ease out')]
        e.scale(sc)
    mouth = k.ell("Smile", 960, 600, 180, 140, None, f0=18, dur=n - 18); mouth.stroke(COL['ink'], 12)
    mouth.trim([(18, 0.75, 'Linear'), (30, 0.55, EXPO)], which='start')    # bottom arc grows out from 6 o'clock
    mouth.trim([(18, 0.75, 'Linear'), (30, 0.95, EXPO)], which='end')


def smear_whoosh(d):
    n = 45
    k = d.comp("CT Smear whoosh", n, "csw"); lab_bg(k, n)
    for i, y in enumerate((500, 540, 580)):
        ln = line(k, f"Speed line {i + 1}", [(380, y), (820, y)], COL['ink'], px=6, f0=0, dur=n)
        ln.trim([(2, 0.0, 'Linear'), (8, 1.0, EXPO)], which='end')
        ln.trim([(6, 0.0, 'Linear'), (16, 1.0, 'Ease in')], which='start')
    car = k.rect("Blob", 960, 540, 260, 140, COL['blue'], r=60, f0=0, dur=n, center=True)
    origin(car, 1, 0)                                        # stretch and squash from its leading (right) edge
    bx, by = car.base
    car.pos([(0, (bx - 1200, by), 'Linear'), (8, (bx, by), EXPO)])
    car.scale([(0, [2.4, 0.8], 'Linear'), (8, [0.8, 1.15], 'Ease out'), (12, [1.08, 0.94], 'S-curve'), (16, [1.0, 1.0], 'S-curve')])
    car.dirblur_keys([(0, 160, 0, 'Linear'), (8, 40, 0, 'Linear'), (12, 0, 0, 'Linear')])     # a streak along the run, clear on the stop


def build():
    d = PDoc(PRESETS)
    PRESETS.clear()
    bouncing_ball(d); boing_title(d); blink_face(d); smear_whoosh(d)
    return d


if __name__ == "__main__":
    print(__doc__)
