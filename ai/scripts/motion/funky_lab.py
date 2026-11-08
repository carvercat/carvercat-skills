"""Funky lab (round 1) in design units: four comps (memphis shapes, offset title, zigzag ribbon, sticker stack).

    import funky_lab as L; doc = L.build(); doc.send(client, PROJECT.carverproj)   # scene.apply per comp, then edit.save

cc2.py kit: px from the top-left, y down; degrees CLOCKWISE; frames; '#RRGGBB'; CSS easing (a key's ease shapes the move
ARRIVING at it). Library presets named in PRESETS are applied after each comp's scene by PDoc (preset.apply); the .carverpreset
builders are build_funky_pack.py (stored preset format, unchanged).

Continuous motion after an entrance is one-directional (linear rotation or drift), never a back-and-forth loop: lint reads a
ping-pong as jitter. Fonts: Rethink Sans must be installed (KI-136). Docs: ai/patterns/funky.md. Frame 1920x1080, 30 fps.

Helpers shared with funky_lab2.py and funky_lab3.py live here: PDoc, textw/txt (text placed by its optical centre, left aligned
texts by their left edge), origin, line/shape (paths), hard_shadow, zigzag.
"""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "json_author"))
sys.path.insert(0, HERE)
from cc2 import Doc, css, BEZ, bezier
# The old kit's named eases ('Ease in', 'Ease out', 'S-curve') are the app's model curves, and its corner radius was capped at a quarter of
# the short side: cc2's Doc(legacy_ease=True, cap_radius=True) keeps both (PDoc below passes them).

COL = dict(peach=css('FFE8D6'), purple=css('7B2FF7'), orange=css('FF7A00'), pink=css('FF4FA3'), teal=css('00C2A8'),
           ink=css('1B1035'), yellow=css('FFD000'), white=css('FFFFFF'))
EXPO, BACK, POP = BEZ['expo'], BEZ['back'], BEZ['pop']
PRESETS = []                      # (comp name, object name, library preset name), applied by PDoc after the comp's scene
W, H = 1920, 1080


# ---------------------------------------------------------------- the document: scene.apply + library presets
class PDoc(Doc):
    """cc2.Doc that also runs preset.apply for the (comp, object, preset) rows of `presets` right after a comp's scene is
    applied. The pack's own .carverpreset files are copied into the scratch host's user Library first (library.folder +
    library.reload). Settings a scene cannot say are listed in an object's `post` as (property path with {id}, value) and set
    with property.set. Nothing outside that scratch host is touched."""
    def __init__(self, presets=(), pack='funky'):
        super().__init__(legacy_ease=True, cap_radius=True, unparent_masks=True); self.presets, self.pack = presets, pack

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
            for o in by_name.values():
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


SY = 1080 / 1920      # the old kit stored a shadow's x against the frame width and its y against the frame HEIGHT: a "12, 12" shadow
                      # was drawn 12 px right and 6.75 px down (measured on the v1 renders); the model keeps that look


def hard_shadow(t, col, dx=12, dy=None):
    """a hard offset shadow (no blur) in `col`, dx px right and dy px down (default dx * 9/16, as the old kit drew a square
    "dx, dy" shadow); returns the dropShadow text at rest"""
    return t.hard_shadow(col, dx, dy)             # cc2 Obj.hard_shadow


def soft_shadow(o):
    """the sticker and photo shadow: 6.5 px down (the old kit's 0.006 against the frame height), 3 px blur, black at 35 %"""
    return o.shadow(0, 6.48, 3.3, '#00000059')


# ---------------------------------------------------------------- shapes
def origin(o, ax, ay):
    """pivot in half-sizes: ax -1 left .. +1 right, ay -1 bottom .. +1 top (0, -1 = the middle of the bottom edge)"""
    return o.set('transformOrigin', '%g%% %g%%' % (50 + 50 * ax, 50 - 50 * ay))


def line(k, name, pts, col, px=2, f0=0, dur=None):
    """an open stroked path through pts [(x, y)], straight segments"""
    return k.path(name, bezier([tuple(p) for p in pts]), col, px, f0=f0, dur=dur)


def shape(k, name, pts, fill, handles=None, f0=0, dur=None):
    """a closed filled path with no stroke (add one with .stroke()); handles [(in, out)] are px offsets from each node"""
    d = bezier([tuple(p) for p in pts], closed=True) if handles is None else \
        bezier([(p[0], p[1], h[0], h[1]) for p, h in zip(pts, handles)], closed=True)
    return k.path(name, d, fill, 0, f0=f0, dur=dur, fill=fill).set('stroke', 'none')


def lab_bg(k, n):
    k.rect("Lab bg", 0, 0, W, H, COL['peach'], f0=0, dur=n)


def zigzag(x0, x1, y, amp, steps):
    return [(x0 + (x1 - x0) * i / steps, y + (amp if i % 2 else -amp)) for i in range(steps + 1)]


# ---------------------------------------------------------------- the comps
def memphis(d):
    n = 90
    k = d.comp("FK Memphis shapes", n, "fms"); lab_bg(k, n)
    items = [("Triangle", lambda f: k.ngon("Triangle", 420, 300, 220, 3, COL['purple'], f0=f, dur=n - f)),
             ("Circle", lambda f: k.ell("Circle", 1500, 260, 200, 200, COL['orange'], f0=f, dur=n - f)),
             ("Squiggle", lambda f: line(k, "Squiggle", zigzag(1180, 1620, 780, 40, 8), COL['teal'], px=18, f0=f, dur=n - f)),
             ("Dot", lambda f: k.ell("Dot", 520, 800, 220, 220, COL['pink'], f0=f, dur=n - f)),
             ("Ring", lambda f: k.ell("Ring", 960, 540, 300, 300, None, f0=f, dur=n - f)),
             ("Star", lambda f: k.star("Star", 1280, 470, 180, 5, 0.45, COL['yellow'], f0=f, dur=n - f))]
    for i, (name, make) in enumerate(items):
        f = i * 3
        o = make(f)
        if name == "Ring": o.stroke(COL['ink'], 14)
        PRESETS.append(("FK Memphis shapes", name, "Tilt pop"))
        spin = -25.0 if i % 2 else 25.0                    # one-way drift spin after the pop (clockwise positive)
        o.rot([(f + 18, 0.0, 'Linear'), (n, spin, 'Linear')])


def offset_title(d):
    n = 90
    k = d.comp("FK Offset title", n, "fot"); lab_bg(k, n)
    t = txt(k, "Title", "GROOVY", 960, 520, 240, COL['orange'], f0=0, dur=n)
    PRESETS.append(("FK Offset title", "Title", "Tilt pop"))
    # the offset shadow is the native Drop shadow on the same text (hard, no blur), so no second text overlaps it
    t.key('dropShadow', [(14, '0px 0px 0px %s' % COL['purple'], 'Linear'), (24, '14px %gpx 0px %s' % (round(14 * SY, 3), COL['purple']), EXPO)])
    wave = line(k, "Wave", zigzag(640, 1280, 700, 18, 10), COL['teal'], px=14, f0=18, dur=n - 18)
    wave.trim([(18, 0.0, 'Linear'), (36, 1.0, EXPO)], which='end')


def zigzag_ribbon(d):
    n = 60
    k = d.comp("FK Zigzag ribbon", n, "fzr"); lab_bg(k, n)
    rib = line(k, "Ribbon", zigzag(120, 1800, 540, 120, 9), COL['pink'], px=44, f0=0, dur=n)
    rib.trim([(0, 0.0, 'Linear'), (24, 1.0, BEZ['smooth'])], which='end')
    rib.trim([(18, 0.0, 'Linear'), (44, 1.0, BEZ['smooth'])], which='start')           # the tail chases the head: a snake


def sticker_stack(d):
    n = 75
    k = d.comp("FK Sticker stack", n, "fss"); lab_bg(k, n)
    stickers = [("NEW", COL['yellow'], COL['ink'], 760, 460, -8), ("HOT", COL['pink'], COL['white'], 1120, 520, 6),
                ("WOW", COL['teal'], COL['ink'], 940, 640, -3)]
    for i, (word, bg, fg, x, y, ang) in enumerate(stickers):
        f = i * 8
        card = k.rect(f"Sticker {i + 1}", x, y, 300, 170, bg, r=28, f0=f, dur=n - f, center=True)
        card.stroke(COL['ink'], 8); soft_shadow(card)
        label = txt(k, f"Sticker label {i + 1}", word, x, y, 84, fg, f0=f, dur=n - f)
        for o in (card, label):
            o.rotv(-float(ang))                           # the old kit stored the angle counter-clockwise
            o.scale([(f, 1.45, 'Linear'), (f + 8, 1.0, BACK)])
            o.op([(f, 0, 'Linear'), (f + 2, 1, 'Linear')])


def build():
    d = PDoc(PRESETS)
    PRESETS.clear()
    memphis(d); offset_title(d); zigzag_ribbon(d); sticker_stack(d)
    return d


if __name__ == "__main__":
    print(__doc__)
