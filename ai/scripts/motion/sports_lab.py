"""Write the Sports lab comps in design units (cc2.py: px from the top-left, y down, degrees clockwise, CSS colours and easing).

    import sports_lab as L; doc = L.build(); doc.send(client, PROJECT.carverproj)   # scene.apply per comp, then edit.save

Four comps: score bug (a score that rolls through a window), player card, head to head stat bars, GOAL slam.

This module is also the Sports kit the other Sports labs import (sports_lab2, sports_lab3, sports_showcase):

- `T()` places a text by its alignment point: x is the left edge for 'left', the right edge for 'right', the middle for 'center';
  y is the line's middle. `track` is the tracking multiplier the pages state (1.3 = 130%); the text carries it as px.
- `slash()`, `slam()`, `zoom_past()`, `exit_fade()` bake the pack's presets (Slash in, Impact slam, Zoom past, Exit fade - fast)
  as plain keys, so the lab needs no library and no preset.apply. Their numbers are the preset's: Slash in starts 22 % of the
  width to the left and 12 % of the height lower (422.4 px, 129.6 px), expo, opaque in 2 f; Impact slam is 220 % -> 92 % at f5
  -> 100 % by f8; Zoom past is 100 % -> 300 % over the last 8 f; Exit fade - fast is 8 f.
- Text outlines (Number, GOAL!, REPLAY, TOUCHDOWN!) are not in the scene document yet, so `SDoc.send` sets them after the apply
  with property.set (text.outline.*).
- Masks: `Comp.mask(content, window)` declares them; `SDoc.send` makes them with mask.make (see SDoc).

Fonts: Rethink Sans must be installed (KI-136). Docs: ai/patterns/sports.md. Comp frames, 30 fps. Teams, players and scores are
invented sample copy.
"""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "json_author"))
from cc2 import Doc, css, bezier, BEZ, HOLD
from cc import textw            # measuring only: the advance width of Rethink Sans text, to size boxes

W, H = 1920, 1080
COL = dict(bg=css('0B1020'), panel=css('141B33'), red=css('E63946'), blue=css('1D7CF2'), yellow=css('FFD60A'),
           white=css('FFFFFF'), grey=css('8892AA'), ink=css('0B1020'))
EXPO, BACK, ACCEL = BEZ['expo'], BEZ['back'], BEZ['accel']
EASE_IN, EASE_OUT = (1 / 3, 0, 2 / 3, 1 / 3), (1 / 3, 2 / 3, 2 / 3, 1)   # the old app model's Ease in / Ease out (cc2's CSS ease-in / ease-out differ)
SLAM = ZOOM = (0.07, 0.0, 0.44, 0.23)    # fitted to the preset's baked steps: Impact slam (2.2 -> 0.92 over 5 f) and Zoom past (1 -> 3 over 8 f)
WEIGHT = dict(Bold=700, SemiBold=600, ExtraBold=800)
TRACK_PX = 1.675                       # tracking multiplier t -> letter spacing (t - 1) * 1.675 * font px
SLASH_DX, SLASH_DY = 0.22 * W, 0.12 * H


# ---------------------------------------------------------------- building blocks
class SDoc(Doc):
    """Doc that finishes what the scene document cannot say yet, once the comps exist: the text outlines (text.outline.*), and
    the masks. cc2's scene-mask pass (style.mask) left the second content (Score new) matted by the first window, so its text never showed;
    mask.make per pair then parent.clear (a window parented to its content would move with it) renders right."""
    def send(self, client, save_path):
        masks = {id(c): c.masks for c in self.comps}
        for c in self.comps: c.masks = []                  # cc2's scene-mask pass binds every content to the first window (see below)
        super().send(client, save_path)
        for c in self.comps: c.masks = masks[id(c)]
        todo = [c for c in self.comps if c.masks or any(getattr(o, 'outline', None) for o in c.objs)]
        if todo:
            index = {c['name']: c['index'] for c in client.tool('carvercat_list')['comps']}
            for c in todo:
                client.run('comp.switch', comp=index[c.name])
                for o in c.objs:
                    ol = getattr(o, 'outline', None)
                    if not ol: continue
                    cid = client.ids('#' + o.id)[0]
                    for key, val in (('text.outline.paint', 'solid'), ('text.outline.color', ol[0]),
                                     ('text.outline.thickness', ol[1])) + ((('text.outline.align', 'outside'),) if ol[2] else ()):
                        client.run('property.set', id=cid, key=key, value=val)
                for content, window in c.masks:             # mask.make: the FIRST id is the matte; it parents the window, so clear that
                    client.run('mask.make', ids=[client.ids('#' + window.id)[0], client.ids('#' + content.id)[0]])
                    client.run('select.match', selector='#' + window.id)
                    client.run('parent.clear')
            client.run('comp.switch', comp=index[self.comps[-1].name])
            client.run('edit.save', path=save_path)
        return save_path


def addkeys(o, key, spec):
    """add keys to a property that may already have some (spec: [(comp frame, value, arriving ease)])"""
    ks = o.tracks.setdefault(key, [])
    ks.extend((f - o.f0, v, e) for f, v, e in spec)
    ks.sort(key=lambda r: r[0]); return o


def origin(o, ax, ay):
    """pivot in half-sizes as the pages say it: ax -1 left, +1 right; ay -1 bottom, +1 top"""
    return o.set('transformOrigin', '%g%% %g%%' % ((ax + 1) * 50, (1 - ay) * 50))


def T(k, name, s, x, y, px, col, f0=0, dur=None, style='ExtraBold', align='left', track=None):
    """text placed by its alignment point (see the module docstring)"""
    ls = round((track - 1) * TRACK_PX * px, 2) if track else None
    w = int(math.ceil(textw(s, px, style) + len(s) * (ls or 0) + 24))
    cx = x + w / 2 if align == 'left' else x - w / 2 if align == 'right' else x
    o = k.text(name, s, cx, y, px, col, f0=f0, dur=dur, weight=WEIGHT[style], align=align, width=w, tracking=ls)
    o.set('overflow', 'visible')
    # the pivot is the alignment point, 38.43 % down the line box (where the old kit's text anchor sat), so a slam or a zoom
    # scales about the same point as before
    o.set('transformOrigin', '%g%% 38.43%%' % {'left': 0, 'center': 50, 'right': 100}[align])
    return o


def outline(o, color, thickness, outside=False):
    o.outline = (color, thickness, outside); return o


def poly(k, name, pts, col, f0=0, dur=None):
    """a closed filled shape through straight-line points"""
    p = k.path(name, bezier(pts, closed=True), '#FFFFFF', 0, f0=f0, dur=dur, fill=col)
    return anchor_path(p, pts)


def anchor_path(p, pts):
    """A path's x/y keys are the top-left of its bounding box in the comp (not offsets from where it was drawn), and cc2 maps a
    `pos` key v to x = v - W/2 for a path. So the path's rest `base` is its box's top-left plus (W/2, H/2): keys written as
    base + a move then land the box where it should be."""
    p.base = (min(x for x, _ in pts) + W / 2, min(y for _, y in pts) + H / 2)
    return p.set('stroke', 'none') if p.style.get('strokeWidth') == 0 else p


def line(k, name, pts, col, px, f0=0, dur=None, cap='round'):
    return anchor_path(k.path(name, bezier(pts), col, px, f0=f0, dur=dur, cap=cap), pts)


def curve(k, name, pts, handles, col, f0=0, dur=None, closed=True):
    """a closed filled path with bezier handles; handles = [((inDx, inDy), (outDx, outDy), corner)] per point (px offsets)"""
    bp = []
    for (x, y), (hi, ho, corner) in zip(pts, handles):
        bp.append((x, y, tuple(hi) if any(hi) else None, tuple(ho) if any(ho) else None))
    p = k.path(name, bezier(bp, closed=closed), '#FFFFFF', 0, f0=f0, dur=dur, fill=col)
    return anchor_path(p, pts)


def lab_bg(k, n):
    k.rect("Lab bg", 0, 0, 1920, 1080, COL['bg'], f0=0, dur=n)


def grow_x(o, f, d=10, ax=-1):
    origin(o, ax, 0); o.scale([(f, [0.0, 1.0], 'linear'), (f + d, [1.0, 1.0], EXPO)]); return o


def last(o):
    """the object's last frame"""
    return o.f0 + o.dur - 1


# ---------------------------------------------------------------- the pack's presets, baked as keys
def slash(o, f=None):
    """Slash in: from 22 % W left and 12 % H lower diagonally to rest on a hard expo (10 f), opaque in 2 f"""
    f = o.f0 if f is None else f
    bx, by = o.base
    addkeys(o, 'pos', [(f, (bx - SLASH_DX, by + SLASH_DY), 'linear'), (f + 10, (bx, by), EXPO)])
    addkeys(o, 'opacity', [(f, 0.0, 'linear'), (f + 2, 1.0, 'linear')])
    return o


def slam(o, f=None, s0=2.2, ease=SLAM):
    """Impact slam: scale s0 (220 %) -> 92 % accelerating (impact at f+5), springs back to 100 % by f+8"""
    f = o.f0 if f is None else f
    addkeys(o, 'scale', [(f, s0, 'linear'), (f + 5, 0.92, ease), (f + 8, 1.0, EASE_OUT)])
    addkeys(o, 'opacity', [(f, 0.0, 'linear'), (f + 2, 1.0, 'linear')])
    return o


def zoom_past(o):
    """Zoom past: 100 % -> 300 % over the last 8 f, fading, accelerating"""
    e = last(o)
    addkeys(o, 'scale', [(e - 8, 1.0, 'linear'), (e, 3.0, ZOOM)])
    addkeys(o, 'opacity', [(e - 5, 1.0, 'linear'), (e, 0.0, ACCEL)])
    return o


def exit_fade(o):
    """Exit fade - fast: opacity 1 -> 0 over the last 8 f, accelerating"""
    e = last(o)
    addkeys(o, 'opacity', [(e - 8, 1.0, 'linear'), (e, 0.0, ACCEL)])
    return o


# ---------------------------------------------------------------- 1. score bug
def score_bug(d):
    n = 120
    k = d.comp("SP Score bug", n, "ssb"); lab_bg(k, n)
    x, y, h = 96, 64, 64
    parts = [("Team A box", 120, COL['red']), ("Score box", 140, COL['panel']), ("Team B box", 120, COL['blue']), ("Clock box", 130, COL['grey'])]
    cx, xs = x, []
    for i, (name, w, col) in enumerate(parts):
        b = k.rect(name, cx, y, w, h, col, f0=0, dur=n)
        grow_x(b, i * 3)
        xs.append(cx); cx += w
    T(k, "Team A", "LIV", xs[0] + 60, y + h / 2, 34, COL['white'], 6, n - 6, align='center')
    T(k, "Team B", "MCI", xs[2] + 60, y + h / 2, 34, COL['white'], 12, n - 12, align='center')
    T(k, "Clock", "67:12", xs[3] + 65, y + h / 2, 30, COL['ink'], 15, n - 15, align='center')
    sx, sw = xs[1], 140
    old = T(k, "Score old", "2 - 1", sx + sw / 2, y + h / 2, 34, COL['white'], 9, 58 - 9, align='center')
    ox, oy = old.base
    old.pos([(52, (ox, oy), 'linear'), (58, (ox, oy - 50), EASE_IN)])            # leaves upward through the window
    new = T(k, "Score new", "3 - 1", sx + sw / 2, y + h / 2, 34, COL['yellow'], 58, n - 58, align='center')
    nx, ny = new.base
    new.pos([(58, (nx, ny + 50), 'linear'), (68, (nx, ny), EXPO)])                 # enters as the old one has left: never both
    wins = [k.rect(nm, sx, y, sw, h, COL['white'], f0=f0, dur=dur) for nm, f0, dur in (("Score window old", 9, 58 - 9), ("Score window new", 58, n - 58))]
    k.mask(old, wins[0]); k.mask(new, wins[1])
    ul = k.rect("Goal underline", sx, y + h, sw, 6, COL['yellow'], f0=60, dur=n - 60)
    grow_x(ul, 60, 8)


# ---------------------------------------------------------------- 2. player card
def player_card(d):
    n = 90
    k = d.comp("SP Player card", n, "spc"); lab_bg(k, n)
    slant = 120
    panel = poly(k, "Panel", [(300 + slant, 260), (1620, 260), (1620 - slant, 820), (300, 820)], COL['panel'], 0, n)
    slash(panel)
    stripe = line(k, "Stripe", [(1380, 260), (1260, 820)], COL['red'], 40, f0=4, dur=n - 4, cap='butt')
    stripe.trim([(4, 0.0, 'linear'), (14, 1.0, EXPO)], which='end')
    num = T(k, "Number", "10", 1380, 540, 360, COL['yellow'], 8, n - 8, align='center')
    num.set('fill', 'none'); outline(num, COL['yellow'], 0.025); slam(num)
    slash(T(k, "Name", "ALEX MORGAN", 470, 500, 88, COL['white'], 10, n - 10))
    slash(T(k, "Position", "FORWARD  ·  #10", 474, 600, 38, COL['yellow'], 16, n - 16, style='SemiBold', track=1.3))


# ---------------------------------------------------------------- 3. head to head
def head_to_head(d):
    n = 90
    k = d.comp("SP Head to head", n, "shh"); lab_bg(k, n)
    slash(T(k, "H2H title", "HEAD TO HEAD", 960, 250, 48, COL['white'], 0, n, align='center', track=1.3))
    rows = [("SHOTS", 14, 9, "14", "9"), ("POSSESSION", 58, 42, "58%", "42%"), ("CORNERS", 7, 3, "7", "3")]
    for i, (lab, a, b, ta, tb) in enumerate(rows):
        y = 420 + i * 150; f = 8 + i * 8
        T(k, f"Row label {i + 1}", lab, 960, y - 48, 30, COL['grey'], f, n - f, style='SemiBold', align='center', track=1.3)
        tot = a + b; wa, wb = 560 * a / tot * 2 * 0.9, 560 * b / tot * 2 * 0.9
        la = k.rect(f"Bar A {i + 1}", 940 - wa / 2, y, wa, 34, COL['red'], f0=f, dur=n - f, center=True)
        grow_x(la, f, 14, ax=1)                                                    # grows left from the centre line
        lb = k.rect(f"Bar B {i + 1}", 980 + wb / 2, y, wb, 34, COL['blue'], f0=f, dur=n - f, center=True)
        grow_x(lb, f, 14, ax=-1)                                                   # grows right
        T(k, f"Value A {i + 1}", ta, 940 - wa - 24, y, 40, COL['white'], f + 12, n - f - 12, align='right')
        T(k, f"Value B {i + 1}", tb, 980 + wb + 24, y, 40, COL['white'], f + 12, n - f - 12)


# ---------------------------------------------------------------- 4. GOAL slam
def goal_slam(d):
    n = 60
    k = d.comp("SP Goal slam", n, "sgs"); lab_bg(k, n)
    cx, cy = 960, 540
    for i in range(10):
        a = math.radians(i * 36 + 12)
        p0 = (cx + 260 * math.cos(a), cy - 160 * math.sin(a)); p1 = (cx + 900 * math.cos(a), cy - 520 * math.sin(a))
        p1 = (min(max(p1[0], 0), 1920), min(max(p1[1], 0), 1080))
        ln = line(k, f"Speed line {i + 1}", [p0, p1], COL['white'] if i % 2 else COL['yellow'], 8, f0=0, dur=n)
        ln.trim([(0, 0.0, 'linear'), (8, 1.0, EXPO)], which='end')
        ln.trim([(6, 0.0, 'linear'), (18, 1.0, EASE_IN)], which='start')
    band = poly(k, "Band", [(200, 430), (1800, 380), (1720, 700), (120, 650)], COL['red'], 0, n)
    slash(band)
    g = T(k, "Goal", "GOAL!", cx, cy, 260, COL['yellow'], 4, n - 4, align='center')
    outline(g, COL['ink'], 0.05, True); slam(g)


def build():
    d = SDoc()
    score_bug(d); player_card(d); head_to_head(d); goal_slam(d)
    return d


if __name__ == "__main__":
    print(__doc__)
