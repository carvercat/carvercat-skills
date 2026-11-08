"""Small helpers shared by the Corporate Brand and Minimal Luxury labs, written on cc2.py (design units).

On top of cc2.py (which now holds the shared parts: the v1 corrections as Doc options, text_at, gradient_keys, nest_keys). What it adds:
- text(): box text placed by the pack's own rule (a left/right/centre anchor point x, and y = the centre of the text box), tracking given as the pack's tracking factor (1.0 = normal) and turned into px.
- line(): a stroked open path through points (px), for rules, leaders and frames.
- the pack's moves as plain keys: soft_rise, card_settle, soft_out (Corporate Brand); slow_in, slow_out, drift_up, push
  (Minimal Luxury). Each is a bezier fitted to the curve the shipped preset bakes, so the object and the preset agree.
- grow(): scale from an edge (left/top) with the transform origin set, the way the packs draw rules and bars.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author"))
import cc2
from cc2 import Comp, Obj, css, bezier, BEZ, HOLD, W, H   # noqa: F401

class Doc(cc2.Doc):
    """cc2.Doc with the three corrections these packs need, now options of cc2 itself: a corner radius capped at a quarter of the short side
    (the old kit's look), mask windows un-parented from their content, and a star keeping its name (an app bug of 0.1.8)."""
    def __init__(self, **kw):
        super().__init__(**{**dict(cap_radius=True, unparent_masks=True, fix_star_names=True), **kw})

    def send(self, client, save_path):
        # the project records the comp active at save (lastCompId): these packs have always ended on the last comp their instance or gradient
        # keys touched, so the files keep the same value
        touched = [c for c in self.comps if c.instance_ops] + [c for c in self.comps if any(getattr(o, 'gkeys', None) for o in c.objs)]
        touched = list({id(c): c for c in touched}.values())
        self.final_comp = touched[-1].name if touched else None
        return super().send(client, save_path)


def gradient_keys(o, spec):
    """key a shape gradient's endpoints (object-local, 0..1, y down): spec [(frame, (sx, sy), (ex, ey), ease)]; the ease leaves that key"""
    return o.gradient_keys(spec)


def place_scaled(master, child, f0, keys, track=None):
    """nest `child` in `master` at frame f0 and push the instance's scale: keys [(frame, scale, ease)] in master frames"""
    master.nest(child, f0=f0, track=track)
    master.nest_keys(child, f0, scale=keys)


WEIGHT = dict(Regular=400, Medium=500, SemiBold=600, Bold=700, Light=300)
LINE = 1.34                      # the font's line height as a multiple of the size
CAP = 0.0                        # em: the box is centred on y (the v1 placement; a 0.155 em drop moved every text 0.155 em low)
STD, DECEL = BEZ['std'], BEZ['decel']
EASE_OUT = (1 / 3, 2 / 3, 2 / 3, 1)        # the old app model's 'Ease out' (cc2.ease maps the name to CSS ease-out, which is another curve)
FADE_OUT = (0.332, 0.116, 0.819, 0.743)    # fitted to Soft fade out


def track_px(track, px):
    """the pack's tracking factor (1.0 normal, 1.3 wide) -> letter spacing in px"""
    return cc2.track_px(track, px)


def text(k, name, s, x, y, px, col, f0=0, dur=None, style='Bold', align='left', track=None, lh=None, width=None, family='Rethink Sans'):
    """Text anchored at (x, y): x is the left edge, centre or right edge (align), y the optical centre of the text block (cc2 Comp.text_at)."""
    return k.text_at(name, s, x, y, px, col, f0=f0, dur=dur, weight=style, align=align, track=track, lh=lh, width=width, family=family,
                     line=LINE, cap=CAP)


def tracking(o, spec):
    """key the letter spacing from the pack's tracking factors: spec [(frame, factor, ease)]"""
    return o.tracking_factor(spec)


def line(k, name, pts, col, px=2, f0=0, dur=None):
    """A stroked open path. A path is saved with its points in comp px; a position key on it is the absolute position of the path's
    bounding box (its top-left), so `base` is set to (left + W/2, top + H/2), the value that keeps it where it is drawn."""
    o = k.path(name, bezier(pts), col, px, f0=f0, dur=dur)
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    o.base = (min(xs) + k.width / 2, min(ys) + k.height / 2)
    return o


def grow(o, f, d=14, ease=None, edge='left'):
    """scale from the left edge (width) or the top edge (height)"""
    ease = ease or BEZ['expo']
    if edge == 'left': o.set('transformOrigin', '0% 50%'); o.scale([(f, [0.0, 1.0], 'Linear'), (f + d, [1.0, 1.0], ease)])
    else: o.set('transformOrigin', '50% 0%'); o.scale([(f, [1.0, 0.0], 'Linear'), (f + d, [1.0, 1.0], ease)])
    return o


def merge(o, key, spec):
    """add keys to a property that already has some (a move on top of another)"""
    cur = {f: (v, e) for f, v, e in [(f + o.f0, v, e) for f, v, e in o.tracks.get(key, [])]}
    for f, v, e in spec: cur[f] = (v, e)
    o.key(key, [(f, v, e) for f, (v, e) in sorted(cur.items())]); return o


# ---------------------------------------------------------------- Corporate Brand moves
def soft_rise(o, f, d=24, dy=16.2):
    """Soft rise: dy px up into place under a fade that is opaque by 60 % of the move, standard curve"""
    bx, by = o.base
    o.pos([(f, (bx, by + dy), 'Linear'), (f + d, (bx, by), STD)])
    o.op([(f, 0.0, 'Linear'), (f + round(d * 0.6), 1.0, STD)])
    return o


def card_settle(o, f, d=20, dy=21.6, s0=0.97):
    """Card settle: dy px up and scale s0 -> 1 on a strong decelerate, opaque by half-way"""
    bx, by = o.base
    o.pos([(f, (bx, by + dy), 'Linear'), (f + d, (bx, by), DECEL)])
    o.scale([(f, s0, 'Linear'), (f + d, 1.0, DECEL)])
    o.op([(f, 0.0, 'Linear'), (f + d // 2, 1.0, STD)])
    return o


def soft_out(o, end, d=16, dy=10.8):
    """Soft fade out: the last d frames of the clip (ending at comp frame `end`), 1 % up, fading, accelerating"""
    bx, by = o.base
    s = end - 1 - d
    o.pos([(f + o.f0, v, e) for f, v, e in o.tracks.get('pos', [])] + [(s, (bx, by), 'Linear'), (end - 1, (bx, by - dy), FADE_OUT)])
    o.op([(f + o.f0, v, e) for f, v, e in o.tracks.get('opacity', [])] + [(s, 1.0, 'Linear'), (end - 1, 0.0, FADE_OUT)])
    return o


# ---------------------------------------------------------------- Minimal Luxury moves
def slow_in(o, f, d=36, s0=1.03):
    """Slow fade in: 36 f fade while the object eases down from 103 % (s0=0: the fade alone)"""
    if s0: o.scale([(f, s0, 'Linear'), (f + d, 1.0, DECEL)])
    o.op([(f, 0.0, 'Linear'), (f + d, 1.0, STD)])
    return o


def slow_out(o, end, d=30):
    """Slow fade out: the last d frames, a fade on a soft curve while the object grows 1.5 %"""
    s = end - 1 - d
    sc = [(f + o.f0, v, e) for f, v, e in o.tracks.get('scale', [])]
    o.scale(sc + [(s, 1.0, 'Linear'), (end - 1, 1.015, 'Linear')])
    ops = [(f + o.f0, v, e) for f, v, e in o.tracks.get('opacity', [])]
    o.op(ops + [(s, 1.0, 'Linear'), (end - 1, 0.0, STD)])
    return o


def drift_up(o, f, d=120, dy=6.48):
    """Drift up: a linear 0.6 % rise under a hold (shorter clips stretch the move to their length)"""
    bx, by = o.base
    cur = [(a + o.f0, v, e) for a, v, e in o.tracks.get('pos', [])]
    o.pos(cur + [(f, (bx, by + dy), 'Linear'), (f + d, (bx, by), 'Linear')])
    return o


def push(o, f, d=150, to=1.06):
    """Photo push: a linear push over d frames"""
    o.scale([(f, 1.0, 'Linear'), (f + d, to, 'Linear')])
    return o


# ---------------------------------------------------------------- looks
def lgrad(o, stops, deg=90):
    """linear gradient fill: stops [(0..1, '#hex')], CSS angle (0 = towards the top, 90 = towards the right). Gradients do not tween."""
    return o.set('fill', 'linear-gradient(%gdeg, %s)' % (deg, ', '.join('%s %g%%' % (c, round(p * 100, 2)) for p, c in stops)))


def rule_open(o, f, d=40, ease=None):
    """a thin line that opens from its centre"""
    ease = ease or BEZ['smooth']
    o.trim([(f, 0.5, 'Linear'), (f + d, 0.0, ease)], which='start')
    o.trim([(f, 0.5, 'Linear'), (f + d, 1.0, ease)], which='end')
    return o


def breathe(o, f, n, a=1.4, b=1.45):
    """a held text keeps moving: its tracking (the pack's factor) drifts from a to b"""
    return tracking(o, [(f, a, 'Linear'), (n, b, 'Linear')])
