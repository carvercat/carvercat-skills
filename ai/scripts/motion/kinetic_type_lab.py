"""Write the Kinetic Typography lab comps in design units (cc2.py: px from the top-left, y down, degrees clockwise, CSS colours and easing).

    import kinetic_type_lab as L; doc = L.build(); doc.send(client, PROJECT.carverproj)   # scene.apply per comp, then edit.save

Also the small kit of the Kinetic Typography labs 2 and 3 and the showcase. The pack's stored presets (Letters zoom in, Words slam,
Lines slide in - left, Words rise - expo, Letters shimmer in, Stamp, Pop - spring, the exits) are BAKED here as plain keys or as the
tween of a text stagger, so the templates need no preset applied afterwards. Springs are sampled once per frame from curves.py.
A text that staggers cannot also carry keys of its own in a scene, so its exit rides in the stagger tween, and any other
text key (tracking) is keyed after the apply (KDoc.post).

Word positions come from INK, the ink boxes measure.boxes gave for each text at x 200, y 540 (the old kit measured them the
same way). Regenerate them with `python3 kinetic_type_lab.py --measure` against a host (CARVERCAT_HOST).
Docs: ai/patterns/kinetic-typography.md. Design units: 1920 x 1080 px, y down, comp frames, 30 fps. Fonts: Rethink Sans (KI-136).
"""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "json_author"))
from cc2 import Doc, Comp, css, bezier, BEZ, HOLD
from explainer_lab import T as _T, textw, addkeys, origin, line, W, H
from curves import named

COL = dict(bg='#0B0B0F', ink='#F4F1EA', muted='#9A968E', accent='#FF4D2E', sun='#FFD23F')
EXPO, ACCEL, BACK, STD = BEZ['expo'], BEZ['accel'], BEZ['back'], BEZ['std']
FONT_STYLE = 'ExtraBold'
SWAP_STATIC, SWAP_WORDS, SWAP_PX = "We build", ["faster", "smarter", "together"], 96

INK = {   # label: [x, y, width, height] px of the ink box of the text set at x 200, y 540 (measure.boxes in 0.1.8.1, Rethink Sans ExtraBold)
    'We build': [200.0, 503.04, 355.27, 71.23],
    'We build x': [200.0, 503.04, 425.28, 71.23],
    'faster': [200.0, 505.92, 237.24, 68.35],
    'smarter': [200.0, 513.7, 326.02, 60.58],
    'together': [200.0, 505.92, 343.71, 89.47],
    'x': [200.0, 525.5, 49.44, 47.62],
    'L100 NEW TYPE': [200.0, 504.5, 460.85, 70.0],
    'L100 FESTIVAL': [200.0, 503.3, 413.1, 72.4],
    'L100 LISBON': [200.0, 503.3, 332.59, 72.4],
    'L100 MAY 12–14': [200.0, 503.3, 499.5, 71.2],
    'Z LOOK': [200.0, 444.58, 677.9, 188.24],
    'Z LO': [200.0, 444.58, 305.88, 188.24],
    'Z O': [200.0, 444.58, 190.32, 188.24],
    "S It isn't luck.": [200.0, 497.65, 518.86, 81.62],
    "S It isn't l": [200.0, 497.65, 320.31, 81.62],
    'S l': [200.0, 500.95, 16.94, 77.0],
    'S luck': [200.0, 500.95, 194.19, 78.32],
    'S uc': [200.0, 522.07, 112.67, 57.2],
}

# ---------------------------------------------------------------- the doc: keys a scene cannot carry are set after the apply
class KDoc(Doc):
    """a Doc with `post`: [(comp name, object name, fn(client, id))] run after the comps are applied (text keys beside a stagger,
    an outline on a text), then the project is saved again"""
    def __init__(self):
        Doc.__init__(self); self.post = []; self.unparent = []

    def comp(self, name, length, code, **kw):
        c = Comp(self, name, length, code, **kw); self.comps.append(c); return c

    def send(self, client, save_path):
        Doc.send(self, client, save_path)
        if not self.post and not self.unparent: return save_path
        comps = {c['name']: c['index'] for c in client.tool('carvercat_list')['comps']}
        last = self.comps[-1].name
        for cname, wname, frame, wx, wy in self.unparent:   # a mask window is made a child of its content: cut it loose, back at its own place
            client.run('comp.switch', comp=comps[cname])
            objs = {o['name']: o['id'] for o in client.tool('carvercat_list')['objects']}
            client.run('view.seek', frame=frame)
            client.run('select.clip', id=objs[wname]); client.run('parent.clear')
            client.run('property.set', id=objs[wname], key='x', value=wx); client.run('property.set', id=objs[wname], key='y', value=wy)
        for cname in dict.fromkeys(p[0] for p in self.post):
            client.run('comp.switch', comp=comps[cname])
            objs = {o['name']: o['id'] for o in client.tool('carvercat_list')['objects']}
            for c2, oname, fn in self.post:
                if c2 == cname: fn(client, objs[oname])
        client.run('comp.switch', comp=comps[last])
        client.run('edit.save', path=save_path)
        return save_path


def mask(d, k, content, window, rest):
    """the window cuts the content; after the apply the window is un-parented at comp frame `rest` (the content at rest)"""
    k.mask(content, window)
    cx, cy, w, h = window.box
    d.unparent.append((k.name, window.name, rest, round(cx - w / 2, 3), round(cy - h / 2, 3)))


def lab_bg(k, n):
    k.rect("Lab bg", 0, 0, W, H, COL['bg'], f0=0, dur=n)


def KT(k, name, s, x, y, px, col, f0=0, dur=None, style=FONT_STYLE, align='left', lh=None, track=None, width=None):
    """a text from frame f0 for dur frames, set as the explainer kit's T (x is the left edge, centre or right edge by align)"""
    return _T(k, name, s, x, y, px, col, f0, dur, style, align, lh, track, width=width)


def fade(o, f, d=5, to=1.0):
    return addkeys(o, 'opacity', [(f, 0.0, 'Linear'), (f + d, to, 'app-out')])


def rise(o, f, dy=24, d=14, dx=0, op=True):
    """enters from dy px below (and dx px to the left) over d frames, expo"""
    bx, by = o.base
    addkeys(o, 'pos', [(f, (bx - dx, by + dy), 'Linear'), (f + d, (bx, by), EXPO)])
    if op: fade(o, f)
    return o


def slam(o, f, s0=1.35, d=8, fade_in=0):
    """beat-words hit: big to 1 (expo); a cut in at full opacity unless fade_in"""
    addkeys(o, 'scale', [(f, s0, 'Linear'), (f + d, 1.0, EXPO)])
    if fade_in: fade(o, f, fade_in)
    return o


def spring(name, frames):
    """a stored spring curve sampled once per frame: [(frame offset, progress 0..1 with overshoot)]"""
    c = named[name]
    return [(i, c(i / frames)) for i in range(frames + 1)]


# ---------------------------------------------------------------- presets as keys on the object
def stamp(o, f):
    """Stamp: from 190 % to 1 with a small rebound over 14 f, a 2.5 f fade"""
    addkeys(o, 'scale', [(f + i, round(1.9 + (1.0 - 1.9) * p, 4), 'Linear') for i, p in spring('spring-gentle', 14)])
    return addkeys(o, 'opacity', [(f, 0.0, 'Linear'), (f + 3, 1.0, 'Linear')])


def pop_spring(o, f):
    """Pop - spring: 0 to 1 with a 16 % overshoot over 24 f, a 5 f fade"""
    addkeys(o, 'scale', [(f + i, round(p, 4), 'Linear') for i, p in spring('spring-bouncy', 24)])
    return addkeys(o, 'opacity', [(f, 0.0, 'Linear'), (f + 5, 1.0, 'Linear')])


def exit_fade(o, n, d=8):
    return addkeys(o, 'opacity', [(n - 1 - d, 1.0, 'Linear'), (n - 1, 0.0, ACCEL)])


# ---------------------------------------------------------------- presets as the tween of a text stagger
def _rows(o, rows):
    cx, cy, w, h = o.box; out = []
    for at, p, e in rows:
        q = dict(p)
        if 'dx' in q or 'dy' in q:
            q['x'] = round(cx - w / 2 + q.pop('dx', 0), 3); q['y'] = round(cy - h / 2 + q.pop('dy', 0), 3)
        out.append((at, q, e))
    return out


def merge_rows(rows):
    by = {}
    for at, p, e in rows:
        r = by.setdefault(at, [at, {}, None]); r[1].update(p); r[2] = e or r[2]
    return [tuple(by[a]) for a in sorted(by)]


def staggered(o, by, each, rows, from_='start'):
    return o.stagger(by=by, each=each, from_=from_, keyframes=_rows(o, merge_rows(rows)))


def tween_letters_zoom():          # chars 1 f apart: 240 % to 1 on an expo landing, 16 f
    return 'chars', 1, [(0, dict(scale=2.4, opacity=0.0), EXPO), (16, dict(scale=1.0, opacity=1.0), 'linear')]


def tween_lines_left():            # lines 5 f apart: 115 px in from the left, 20 f
    return 'lines', 5, [(0, dict(dx=-115.2, opacity=0.0), EXPO), (20, dict(dx=0, opacity=1.0), 'linear')]


def tween_words_rise():            # words 3 f apart: 32 px up into place, 16 f
    return 'words', 3, [(0, dict(dy=32.4, opacity=0.0), EXPO), (16, dict(dy=0, opacity=1.0), 'linear')]


def tween_words_slam():            # words 5 f apart: 180 % to 1 with a small rebound, 14 f
    rows = [(i, dict(scale=round(1.8 + (1.0 - 1.8) * p, 4)), 'linear') for i, p in spring('spring-gentle', 14)]
    return 'words', 5, rows + [(0, dict(opacity=0.0), 'linear'), (3, dict(opacity=1.0), 'linear')]


def tween_shimmer():               # chars 1 f apart in random order: a 10 f fade
    return 'chars', 1, [(0, dict(opacity=0.0), STD), (10, dict(opacity=1.0), 'linear')]


def shimmer(o):
    by, each, rows = tween_shimmer()
    return staggered(o, by, each, rows, from_='random')


def window_for(k, name, x, y, w, h, col, f0, dur):
    return k.rect(name, x, y, w, h, col, f0=f0, dur=dur)


# ---------------------------------------------------------------- 1. word swap
def word_swap(d):
    """A fixed phrase with a slot whose word rolls up to the next one, three times."""
    n, per, f0 = 120, 36, 10
    k = d.comp("KT Word swap", n, "kws"); lab_bg(k, n)
    # the slot starts where " x" puts its x: the static ink width plus the space
    x_slot = 200 + INK[SWAP_STATIC + " x"][2] - INK["x"][2]
    widest = max(INK[w][2] for w in SWAP_WORDS)
    x0 = 960 - ((x_slot - 200) + widest) / 2              # centre the longest phrase
    shift = x0 - 200
    y, line_h = 540, SWAP_PX * 1.25
    KT(k, "Static", SWAP_STATIC, x0, y, SWAP_PX, COL['ink'], 0, n)
    top = min(INK[w][1] for w in SWAP_WORDS) - 6          # measured ink (incl. descenders) + 6 px
    bot = max(INK[w][1] + INK[w][3] for w in SWAP_WORDS) + 6
    for i, w in enumerate(SWAP_WORDS):
        a = f0 + i * per
        last = i == len(SWAP_WORDS) - 1
        dur = (n - a) if last else per                    # the exit ends as the next word starts: no two words share a frame
        o = KT(k, f"Word {i + 1}", w, x_slot + shift, y, SWAP_PX, COL['accent'], a, dur)
        bx, by = o.base
        ks = [(a, (bx, by + line_h), 'Linear'), (a + 12, (bx, by), EXPO)]
        if not last:
            ks += [(a + per - 8, (bx, by), 'Linear'), (a + per, (bx, by - line_h), ACCEL)]
        o.pos(ks)
        win = k.rect(f"Window {i + 1}", x_slot + shift - 12, top, widest + 40, bot - top, COL['ink'], f0=a, dur=dur)
        mask(d, k, o, win, a + 20)


def impact_stack(d):
    n = 90
    k = d.comp("KT Impact stack", n, "kis"); lab_bg(k, n)
    for i, (s, y, col) in enumerate([("NO", 330, COL['ink']), ("MORE", 540, COL['ink']), ("BORING", 750, COL['accent'])]):
        f = i * 8
        o = KT(k, f"Line {i + 1}", s, 960, y, 180, col, f, n - f, align='center')
        o.scale([(f, 1.7, 'Linear'), (f + 10, 1.0, BACK)])
        o.op([(f, 0, 'Linear'), (f + 3, 1, 'Linear')])
    bar = k.rect("Underline", 960, 862, 520, 16, COL['sun'], f0=26, dur=n - 26, center=True)
    bar.scale([(26, [0.0, 1.0], 'Linear'), (40, [1.0, 1.0], EXPO)])


def line_reveal(d):
    n = 60
    k = d.comp("KT Line reveal", n, "klr"); lab_bg(k, n)
    ly = 610
    rule = line(k, "Rule", [(560, ly), (1360, ly)], COL['accent'], px=6, f0=0, dur=n)
    rule.trim([(0, 0.5, 'Linear'), (14, 0.0, EXPO)], which='start')       # draws out from the centre
    rule.key('trimEnd', [(0, '50%', 'Linear'), (14, '100%', EXPO)])
    head = KT(k, "Headline", "Launch day", 960, 520, 140, COL['ink'], 0, n, align='center')
    bx, by = head.base
    head.pos([(8, (bx, by + 180), 'Linear'), (26, (bx, by), EXPO)])
    k.rect("Above the rule", 0, 300, 1920, ly - 3 - 300, COL['ink'], f0=0, dur=n)
    mask(d, k, head, k.objs[-1], 40)
    sub = KT(k, "Subline", "October 27  ·  10:00", 960, 680, 40, COL['muted'], 18, n - 18, 'Medium', 'center')
    sx, sy = sub.base
    sub.pos([(18, (sx, sy + 24), 'Linear'), (32, (sx, sy), EXPO)])
    sub.op([(18, 0, 'Linear'), (26, 1, 'app-out')])


def beat_words(d):
    n, per = 100, 25
    k = d.comp("KT Beat words", n, "kbw"); lab_bg(k, n)
    for i, (w, col) in enumerate([("THINK", COL['ink']), ("BUILD", COL['accent']), ("SHIP", COL['ink']), ("REPEAT", COL['sun'])]):
        f = i * per
        o = KT(k, f"Beat {i + 1}", w, 960, 540, 220, col, f, per, align='center')
        o.scale([(f, 1.35, 'Linear'), (f + 8, 1.0, EXPO)])      # a hard cut in, no fade: readable for all 25 f


def focus_pull(d):
    n = 60
    k = d.comp("KT Focus pull", n, "kfp"); lab_bg(k, n)
    t = KT(k, "Title", "Into focus", 960, 540, 150, COL['ink'], 0, n, align='center', width=2600)
    # chars 2 f apart, each from 24 px of blur and transparent to sharp over 18 f
    t.stagger(by='chars', each=2, keyframes=[(0, dict(opacity=0.0, blur=24), EXPO), (18, dict(opacity=1.0, blur=0), 'linear')])
    ls = lambda t_: round((t_ - 1) * 150 * W / 1146.24, 3)
    def connect_blur(c, i):                    # the blur rides the stagger too: every letter plays it late (a scene keys it on the whole text)
        c.run('select.clip', id=i); c.run('stagger.connect', param='fx.e_fx_blur_%s.blur' % i)
    d.post.append(("KT Focus pull", "Title", connect_blur))
    d.post.append(("KT Focus pull", "Title", lambda c, i: c.run('anim.set', id=i, keyframes=[
        dict(at=0, ease=EXPO_CSS, letterSpacing=ls(1.6)), dict(at=30, ease='linear', letterSpacing=0), dict(at=n, letterSpacing=ls(1.06))])))


EXPO_CSS = 'cubic-bezier(0.16, 1, 0.3, 1)'


def build(path=None, m=None):
    d = KDoc()
    word_swap(d); impact_stack(d); line_reveal(d); beat_words(d); focus_pull(d)
    return d


if __name__ == "__main__":
    print(__doc__)
