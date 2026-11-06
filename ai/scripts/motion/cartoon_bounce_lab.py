"""Write the Cartoon Bounce lab comps into a .carverproj (direct project-file authoring).

    import cartoon_bounce_lab as L; presets, masks = L.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); edit.save.
Check with carvercat_inspect and carvercat_look; extract templates with
comp_to_template.py (--drop "Lab bg").

Easing on a key shapes the move ARRIVING at it: a fall into the ground arrives with
'Ease in' (accelerating), a rise to a peak with 'Ease out' (decelerating).
Fonts: Rethink Sans must be installed (KI-136).
Docs: ai/patterns/cartoon-bounce.md. Pixel space 1920x1080, y down; comp frames, 30 fps.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cc import Doc, lin, P, BEZ
from curves import named, bake

COL = dict(cream=lin('FFF4E0'), ink=lin('2B1B3D'), red=lin('FF5A5F'), yellow=lin('FFC93C'), blue=lin('3D7DFF'),
           green=lin('3CCB7F'), shadow=lin('2B1B3D'), white=lin('FFFFFF'))
EXPO, BACK = BEZ['expo'], BEZ['back']
PRESETS, MASKS = [], []


def lab_bg(k, n):
    k.rect("Lab bg", 0, 0, 1920, 1080, COL['cream'], f0=0, dur=n)


def bouncing_ball(d):
    n = 90
    k = comp = d.comp("CT Bouncing ball", n, "cbb"); lab_bg(k, n)
    ground = 900; r = 60
    k.rect("Ground", 0, ground, 1920, 6, COL['ink'], f0=0, dur=n)
    yc = ground - r
    # (frame, centre y, arriving ease): fall, rise, fall, rise, fall, settle
    path = [(0, 220, 'Linear'), (18, yc, 'Ease in'), (31, 460, 'Ease out'), (44, yc, 'Ease in'), (53, 660, 'Ease out'),
            (62, yc, 'Ease in'), (67, yc - 40, 'Ease out'), (72, yc, 'Ease in')]
    contacts = [18, 44, 62, 72]
    sh = k.ell("Shadow", 300, ground + 2, 150, 26, COL['shadow'], f0=0, dur=n)
    ball = k.ell("Ball", 300, yc, 2 * r, 2 * r, COL['red'], f0=0, dur=n)
    ball.anchor(0, -1)                                       # squash on the ground: pivot at the bottom edge
    x0, x1, xf = 300, 1500, 62
    def x_at(f): return x0 + (x1 - x0) * min(f, xf) / xf
    ball.pos([(f, P(x_at(f), y), e) for f, y, e in path])
    sh.pos([(f, P(x_at(f), ground + 2), 'Linear') for f, y, e in path])
    # shadow grows as the ball nears the ground and fades at height
    sh.scale([(f, [0.45 + 0.55 * (y - 220) / (yc - 220)] * 2, 'Linear') for f, y, e in path])
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
    star.rot([(0, 0.0, 'Linear'), (n, 20.0, 'Linear')])
    PRESETS.append(("CT Boing title", "Burst", "Pop - wobbly"))
    t = k.text("Title", "BOING!", 960, 540, 220, COL['yellow'], f0=6, dur=n - 6, style='ExtraBold', align='center')
    t.set(t.src('text_outline', 'paint'), 'solid').set(t.src('text_outline', 'color'), COL['ink'][:3])
    t.set(t.src('text_outline', 'thickness'), 0.08).set(t.src('text_outline', 'outsideOnly'), True).set(t.src('text_outline', 'corners'), 'round')
    t.stagger(6, by='character', gap=3, dy=0.12, d=18, blur=0)
    rp = f'src.e_src_text_relative_{t.id}.position'
    keys = [(6 + p_t * 18, [0, round(0.12 * (1 - p), 5)], 'Linear') for p_t, p in bake(named['bounce'], 18, 0.01)]
    t.key(rp, keys)                                          # each letter drops and bounces (Stagger Text replays it per letter)


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
    tp = mouth.trim([(18, 0.75, 'Linear'), (30, 0.55, EXPO)], which='start')   # bottom arc grows out from 6 o'clock
    mouth.key(tp + '.end', [(18, 0.75, 'Linear'), (30, 0.95, EXPO)])


def smear_whoosh(d):
    n = 45
    k = d.comp("CT Smear whoosh", n, "csw"); lab_bg(k, n)
    for i, y in enumerate((500, 540, 580)):
        ln = k.line(f"Speed line {i + 1}", [(380, y), (820, y)], COL['ink'], px=6, f0=0, dur=n)
        tp = ln.trim([(2, 0.0, 'Linear'), (8, 1.0, EXPO)], which='end')
        ln.key(tp + '.start', [(6, 0.0, 'Linear'), (16, 1.0, 'Ease in')])
    car = k.rect("Blob", 960, 540, 260, 140, COL['blue'], r=60, f0=0, dur=n, center=True)
    car.anchor(1, 0)                                         # stretch and squash from its leading (right) edge
    bx, by = car.base
    car.pos([(0, [bx - 1200 / 1920, by], 'Linear'), (8, [bx, by], EXPO)])
    car.scale([(0, [2.4, 0.8], 'Linear'), (8, [0.8, 1.15], 'Ease out'), (12, [1.08, 0.94], 'S-curve'), (16, [1.0, 1.0], 'S-curve')])


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    bouncing_ball(d); boing_title(d); blink_face(d); smear_whoosh(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
