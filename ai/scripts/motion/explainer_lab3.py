"""Explainer round 3: eight lab comps for briefs the pack could not serve before (a cause-and-effect
chain that branches, pros and cons with a tipping seesaw, a labelled diagram with leader lines,
three steps with drawn icons, an FAQ accordion, a word definition with pronunciation, a tip
carousel and a problem-to-solution split), written straight into a .carverproj.

    import explainer_lab3 as L; presets, masks = L.build(PROJECT.carverproj)

Same rules as explainer_lab.py: light ground, everything enters in reading order at the speed of
narration, one emphasis at a time, and the last item gets time to be read. Every move is baked
as keys here (no presets to apply): step_in() writes the pack's Step in (centre -2.5% W -> 0,
expo, fade over 7 f) and pulse() the Emphasis pulse (1 -> 1.06 -> 1, once).
Every text passes lint contrast:true at 4.5:1: the round-1/2 accents (coral #FF6B5B, green #2BB673)
measure 2.9-4.3:1 under white text, so round 3 uses deeper accents (blue #2B58D6, coral #B93222, green
#17794A, muted #565C70), converted with the renderer's BT.709 curve (KI-141).
Full-frame layouts carry their own "Light background". After writing: edit.open {path, force:true};
edit.save; check with carvercat_inspect (curves, lint contrast:true, qc) and carvercat_look; extract
with comp_to_template.py (--drop "Lab bg"). Fonts: Rethink Sans must be installed (KI-136).
Docs: ai/patterns/explainer.md (round 3). Pixel space 1920x1080, y down; comp frames, 30 fps.
Names, numbers and claims are sample copy.
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author"))
from explainer_lab import Doc, P, EXPO, BACK, lab_bg
from cc import lin, textw

PRESETS, MASKS = [], []
W, H = 1920.0, 1080.0


def lin709(h):
    """hex -> linear light with the renderer's BT.709 curve (KI-141: cc.lin renders mid-tones ~10% dark)"""
    h = h.lstrip('#'); v = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return [round(c / 4.5 if c < 0.081 else ((c + 0.099) / 1.099) ** (1 / 0.45), 5) for c in v] + [1.0]


C = dict(bg=lin709('F7F7FA'), ink=lin709('1F2333'), muted=lin709('565C70'), blue=lin709('2B58D6'), coral=lin709('B93222'),
         green=lin709('17794A'), grey=lin709('C9CDD8'), grey2=lin709('8A93AD'), white=[1.0, 1.0, 1.0, 1.0],
         blue_t=lin709('E6ECFD'), coral_t=lin709('FDE8E4'), green_t=lin709('E2F4EA'), body1=lin709('1F2333'), body2=lin709('48517A'))


def light_bg(k, n):
    k.rect("Light background", 0, 0, 1920, 1080, C['bg'], f0=0, dur=n)


def step_in(o, f, dx=48):
    """the pack's Step in as baked keys: centre -2.5% W -> 0 (expo, 14 f), opaque in 7 f"""
    return o.rise(f, dy=0, d=14, ease='expo', fade=True, dx=dx)


def pulse(o, f, peak=1.06):
    """the pack's Emphasis pulse, once: 1 -> peak -> 1"""
    return o.scale([(f, 1.0, 'Linear'), (f + 6, peak, 'Ease out'), (f + 16, 1.0, 'S-curve')])


def pop(o, f, d=12):
    o.scale([(f, 0.0, 'Linear'), (f + d, 1.0, BACK)]); o.op([(f, 0.0, 'Linear'), (f + 3, 1.0, 'Linear')]); return o


def draw(o, f, d=12, ease=None):
    return o.trim([(f, 0.0, 'Linear'), (f + d, 1.0, ease or EXPO)])


def T(k, name, s, x, y, px, col, f, n, style='Medium', align='left', lh=None, track=None, maxw=None, step=True):
    """a text from frame f to the end, with Step in; maxw asserts the widest line fits (KI-157: lint does not)"""
    w = max(textw(l, px, style) for l in s.split('\n'))
    if maxw is not None and w > maxw:
        raise ValueError(f"{name}: {w:.0f} px wide, limit {maxw}")
    o = k.text(name, s, x, y, px, col, f0=f, dur=n - f, style=style, align=align, lh=lh, track=track)
    if step: step_in(o, f, dx=48 if align != 'right' else -48)
    return o


def card(k, name, x, y, w, h, f, n, fill=None, stroke=None, sw=4, r=26, shadow=True, step=True):
    o = k.rect(name, x, y, w, h, fill if fill is not None else C['white'], r=r, f0=f, dur=n - f)
    if stroke is not None: o.stroke(stroke, sw)
    if shadow: o.shadow(y=-0.004, soft=0.014, op=0.14)
    if step: step_in(o, f)
    return o


def link(k, name, pts, f, n, col, d=14, px=6, head=True):
    """a polyline (rounded corners) that draws on, with a triangle head popping where it ends; the head
    centre sits on the last point, so end the line 18 px short of the target"""
    ln = k.line(name, pts, col, px=px, f0=f, dur=n - f)
    ln.set(ln.src('shape_stroke', 'corners'), 'round')
    draw(ln, f, d)
    if head:
        (x0, y0), (x1, y1) = pts[-2], pts[-1]
        ang = math.degrees(math.atan2(-(y1 - y0), x1 - x0))        # math angle, y up; a 3-gon at rotation 0 points right
        h = k.ngon(name + " head", x1, y1, 34, 3, col, f0=f + d - 4, dur=n - f - d + 4, angle=0.0)
        h.rotv(round(ang, 2)); pop(h, f + d - 4, 8)
    return ln


def tick(k, name, x, y, s, col, f, n, px=9, d=10):
    o = k.line(name, [(x - s * 0.45, y), (x - s * 0.1, y + s * 0.35), (x + s * 0.5, y - s * 0.35)], col, px=px, f0=f, dur=n - f)
    o.set(o.src('shape_stroke', 'corners'), 'round'); draw(o, f, d); return o


def mark(k, name, pts, col, f, n, px=9, d=8):
    o = k.line(name, pts, col, px=px, f0=f, dur=n - f); draw(o, f, d); return o


def badge(k, name, x, y, dia, col, f, n):
    b = k.ell(name, x, y, dia, dia, col, f0=f, dur=n - f); pop(b, f); return b


# ---------------------------------------------------------------- 1. cause and effect (a chain that branches)
def cause_effect(d):
    n = 150
    k = d.comp("EX Cause effect", n, "ece"); lab_bg(k, n); light_bg(k, n)
    xs = (370, 960, 1550); cw = 440
    for i, (tag, col) in enumerate((("CAUSE", C['blue']), ("EFFECT", C['coral']), ("RESULT", C['green']))):
        T(k, f"Column tag {i + 1}", tag, xs[i], 205, 30, col, (0, 30, 60)[i], n, style='Bold', align='center', track=1.07)
    card(k, "Cause card", xs[0] - cw / 2, 450, cw, 180, 4, n, stroke=C['blue'], sw=6)
    T(k, "Cause text", "Prices rise", xs[0], 540, 56, C['ink'], 8, n, style='ExtraBold', align='center', maxw=380)
    mid = 540
    for j, (cy, txt) in enumerate(((395, "Customers\nbuy less"), (685, "Rivals\nundercut us"))):
        f = 34 + j * 8
        card(k, f"Effect card {j + 1}", xs[1] - cw / 2, cy - 95, cw, 190, f, n, stroke=C['coral'], sw=6)
        T(k, f"Effect text {j + 1}", txt, xs[1], cy, 44, C['ink'], f + 4, n, style='Bold', align='center', lh=0.95, maxw=360)
        link(k, f"Cause link {j + 1}", [(596, mid), (665, mid), (665, cy), (718, cy)], 24, n, C['muted'], d=12)
        link(k, f"Result link {j + 1}", [(xs[1] + cw / 2 + 6, cy), (1255, cy), (1255, mid), (1308, mid)], 58, n, C['muted'], d=12, head=(j == 0))
    rc = card(k, "Result card", xs[2] - cw / 2, 430, cw, 220, 68, n, stroke=C['green'], sw=6)
    rt = T(k, "Result text", "Sales fall", xs[2], 505, 60, C['ink'], 72, n, style='ExtraBold', align='center', maxw=380)
    rn = T(k, "Result note", "12% less revenue", xs[2], 580, 32, C['muted'], 80, n, style='Medium', align='center', maxw=380)
    for o in (rc, rt, rn): pulse(o, 96, 1.05)                           # one emphasis: the outcome
    return k


# ---------------------------------------------------------------- 2. pros and cons (a seesaw tips to the heavier side)
def pros_cons(d):
    n = 165
    k = d.comp("EX Pros cons", n, "epc"); lab_bg(k, n); light_bg(k, n)
    T(k, "Pros cons title", "Working from home", 960, 100, 60, C['ink'], 0, n, style='ExtraBold', align='center')
    cols = (("PROS", C['green'], 520, ("Flexible hours", "No commute", "Deep focus time"), 6, True),
            ("CONS", C['coral'], 1400, ("Feeling isolated", "Late-night pings"), 50, False))
    for name, col, cx, items, f0, plus in cols:
        card(k, f"{name.title()} header", cx - 330, 170, 660, 76, f0, n, fill=col, shadow=False, r=20)
        T(k, f"{name.title()} tag", name, cx, 208, 36, C['white'], f0 + 3, n, style='Bold', align='center', track=1.07)
        for i, it in enumerate(items):
            y, f = 320 + i * 105, f0 + 10 + i * 12
            badge(k, f"{name.title()} icon {i + 1}", cx - 280, y, 58, col, f, n)
            mark(k, f"{name.title()} sign {i + 1}", [(cx - 297, y), (cx - 263, y)], C['white'], f + 4, n, px=7, d=6)
            if plus: mark(k, f"{name.title()} sign {i + 1} up", [(cx - 280, y - 17), (cx - 280, y + 17)], C['white'], f + 4, n, px=7, d=6)
            T(k, f"{name.title()} item {i + 1}", it, cx - 225, y, 40, C['ink'], f + 3, n, style='Medium', maxw=540)
            div = k.line(f"{name.title()} rule {i + 1}", [(cx - 330, y + 52), (cx + 330, y + 52)], C['grey'], px=3, f0=f + 4, dur=n - f - 4)
            draw(div, f + 4, 14)
    # the seesaw: beam turns about the pivot; each ball is baked to ride its beam end (positions every frame)
    px_, py_, L, bh = 960, 830, 380, 14
    rl, rr = 64, 44
    f_in, f_t = 84, 96
    fulc = k.ngon("Seesaw fulcrum", px_, py_ + 63, 110, 3, C['ink'], f0=f_in, dur=n - f_in); fulc.rotv(90.0); pop(fulc, f_in)
    plate = k.rect("Seesaw base", px_, 940, 260, 12, C['ink'], r=6, f0=f_in, dur=n - f_in, center=True)
    plate.scale([(f_in, [0.0, 1.0], 'Linear'), (f_in + 14, [1.0, 1.0], EXPO)])
    beam = k.rect("Seesaw beam", px_, py_, 2 * L, bh, C['ink'], r=7, f0=f_in, dur=n - f_in, center=True)
    beam.scale([(f_in, [0.0, 1.0], 'Linear'), (f_in + 14, [1.0, 1.0], EXPO)])
    TILT = 8.0
    def tilt(f):                                                    # degrees, left end down; one overshoot (about 16%), settles by ~f136
        u = f - f_t
        if u <= 0: return 0.0
        return TILT * (1 - math.exp(-u / 5.0) * math.cos(2 * math.pi * u / 18.0))
    frames = list(range(f_t, f_t + 46))
    beam.rot([(f_in, 0.0, 'Linear')] + [(f, round(tilt(f), 3), 'Linear') for f in frames])
    def end_ball(sign, r, f):
        t = math.radians(tilt(f)); ex = px_ + sign * L * math.cos(t)
        ey = py_ - sign * L * math.sin(t)                          # left end (sign -1) drops when t > 0; the right end rises
        nx, ny = -math.sin(t), -math.cos(t)
        return ex + nx * (r + bh / 2), ey + ny * (r + bh / 2)
    for name, sign, r, col, nm in (("Pros ball", -1, rl, C['green'], "L"), ("Cons ball", 1, rr, C['coral'], "R")):
        b = k.ell(name, *end_ball(sign, r, 0), 2 * r, 2 * r, col, f0=f_in + 4, dur=n - f_in - 4)
        pop(b, f_in + 4)
        b.pos([(f_in + 4, P(*end_ball(sign, r, 0)), 'Linear')] + [(f, P(*end_ball(sign, r, f)), 'Linear') for f in frames])
    T(k, "Verdict", "Worth it, on balance", 960, 1005, 40, C['ink'], 120, n, style='Bold', align='center', maxw=700)
    return k


# ---------------------------------------------------------------- 3. labelled diagram with leader lines
def labelled_diagram(d):
    n = 165
    k = d.comp("EX Labelled diagram", n, "eld"); lab_bg(k, n); light_bg(k, n)
    T(k, "Diagram title", "Inside the phone", 960, 90, 56, C['ink'], 0, n, style='ExtraBold', align='center')
    body = k.rect("Phone body", 810, 170, 300, 720, C['body1'], r=64, f0=0, dur=n)
    body.gradient([(0.0, C['body1']), (1.0, C['body2'])], (960, 170), (960, 890))
    body.shadow(y=-0.01, soft=0.03, op=0.25)
    body.scale([(2, 0.92, 'Linear'), (18, 1.0, EXPO)]); body.op([(2, 0.0, 'Linear'), (10, 1.0, 'Ease out')])
    scr = k.rect("Phone screen", 830, 270, 260, 560, C['blue_t'], r=26, f0=8, dur=n - 8)
    scr.gradient([(0.0, C['blue_t']), (1.0, C['white'])], (960, 270), (960, 830))
    scr.op([(8, 0.0, 'Linear'), (16, 1.0, 'Ease out')])
    cam = k.ell("Phone camera", 960, 220, 26, 26, C['grey'], f0=10, dur=n - 10); pop(cam, 10)
    btn = k.rect("Phone button", 1110, 380, 9, 90, C['grey2'], r=4, f0=12, dur=n - 12); pop(btn, 12)
    bat = k.rect("Phone battery", 860, 640, 200, 110, None, r=18, f0=14, dur=n - 14); bat.stroke(C['blue'], 5, line='dashed', dash=16, gap=10)
    draw(bat, 14, 14)
    # parts: (name, part point, label side, label y, title, note)
    parts = (("Camera", (960, 220), 'L', 228, "Camera", "12 MP, front facing", 34),
             ("Button", (1114, 425), 'R', 425, "Power button", "Hold 2 s to switch on", 56),
             ("Screen", (850, 520), 'L', 520, "Screen", "6.1 in, 120 Hz", 78),
             ("Battery", (1050, 700), 'R', 700, "Battery", "All day, 4,500 mAh", 100))
    for nm, (px_, py_), side, ly, ttl, note, f in parts:
        dot = k.ell(f"{nm} dot", px_, py_, 22, 22, C['blue'], f0=f, dur=n - f); pop(dot, f, 8)
        ring_ = k.ell(f"{nm} dot ring", px_, py_, 22, 22, None, f0=f, dur=n - f); ring_.stroke(C['white'], 4); pop(ring_, f, 8)
        if side == 'L':
            ln = k.line(f"{nm} leader", [(px_ - 11, py_), (735, py_)], C['blue'], px=4, f0=f + 2, dur=n - f - 2)
            lx, al = 715, 'right'
        else:
            ln = k.line(f"{nm} leader", [(px_ + 11, py_), (1205, py_)], C['blue'], px=4, f0=f + 2, dur=n - f - 2)
            lx, al = 1225, 'left'
        draw(ln, f + 2, 12)
        T(k, f"{nm} label", ttl, lx, ly, 44, C['ink'], f + 10, n, style='Bold', align=al, maxw=420)
        T(k, f"{nm} note", note, lx, ly + 56, 30, C['muted'], f + 14, n, style='Medium', align=al, maxw=420)
    return k


# ---------------------------------------------------------------- 4. three steps with drawn icons
def icon_steps(d):
    n = 150
    k = d.comp("EX Icon steps", n, "eis"); lab_bg(k, n); light_bg(k, n)
    xs = (400, 960, 1520); cw, ch, cy0 = 440, 580, 250
    steps = (("Upload", "Drop in your\nclips or photos.", C['blue'], C['blue_t']),
             ("Customise", "Pick a look and\nadjust the timing.", C['coral'], C['coral_t']),
             ("Share", "Export once and\nsend it anywhere.", C['green'], C['green_t']))
    for i, (ttl, txt, col, tint) in enumerate(steps):
        cx, f = xs[i], i * 34
        card(k, f"Step card {i + 1}", cx - cw / 2, cy0, cw, ch, f, n, r=32)
        tile = k.ell(f"Icon tile {i + 1}", cx, 390, 176, 176, tint, f0=f + 4, dur=n - f - 4); pop(tile, f + 4)
        g = f + 12
        if i == 0:                                                   # an arrow rising out of a tray
            mark(k, "Upload shaft", [(cx, 412), (cx, 352)], col, g, n, px=10)
            mark(k, "Upload head", [(cx - 26, 376), (cx, 348), (cx + 26, 376)], col, g + 6, n, px=10)
            mark(k, "Upload tray", [(cx - 46, 400), (cx - 46, 430), (cx + 46, 430), (cx + 46, 400)], col, g, n, px=10, d=10)
        elif i == 1:                                                 # three sliders
            for j, (yy, kx) in enumerate(((352, -18), (390, 22), (428, -26))):
                mark(k, f"Slider {j + 1}", [(cx - 48, yy), (cx + 48, yy)], col, g + j * 3, n, px=8, d=8)
                kn = k.ell(f"Knob {j + 1}", cx + kx, yy, 26, 26, C['white'], f0=g + 8 + j * 3, dur=n - g - 8 - j * 3); kn.stroke(col, 7)
                pop(kn, g + 8 + j * 3, 8)
        else:                                                        # three connected nodes
            pts = ((cx - 40, 390), (cx + 34, 350), (cx + 34, 430))
            mark(k, "Share line 1", [pts[0], pts[1]], col, g, n, px=8, d=8)
            mark(k, "Share line 2", [pts[0], pts[2]], col, g + 3, n, px=8, d=8)
            for j, (px_, py_) in enumerate(pts):
                nd = k.ell(f"Node {j + 1}", px_, py_, 34, 34, col, f0=g + 4 + j * 3, dur=n - g - 4 - j * 3); pop(nd, g + 4 + j * 3, 8)
        T(k, f"Step tag {i + 1}", f"STEP {i + 1}", cx, 520, 28, col, f + 14, n, style='Bold', align='center', track=1.07)
        T(k, f"Step title {i + 1}", ttl, cx, 585, 52, C['ink'], f + 18, n, style='ExtraBold', align='center', maxw=380)
        T(k, f"Step text {i + 1}", txt, cx, 700, 32, C['muted'], f + 22, n, style='Medium', align='center', lh=1.0, maxw=380)
        if i < 2:
            link(k, f"Step arrow {i + 1}", [(cx + cw / 2 + 12, 390), (xs[i + 1] - cw / 2 - 36, 390)], f + 24, n, C['muted'], d=10, px=5)
    return k


# ---------------------------------------------------------------- 5. FAQ accordion (one answer opens)
def faq(d):
    n = 165
    k = d.comp("EX FAQ card", n, "efq"); lab_bg(k, n); light_bg(k, n)
    x0, w_ = 360, 1200
    T(k, "FAQ title", "Questions people ask", x0, 140, 64, C['ink'], 0, n, style='ExtraBold', maxw=w_)
    qs = ("Is it free to use?", "Can I work offline?", "How do I get support?")
    y0, rh, gap, grow = 250, 120, 20, 210                           # rows 140 apart; row 1 grows by 210 px
    f_open, d_open = 44, 14
    # the answer panel sits under the first row and grows downward (anchored at its top)
    pan = k.rect("Answer panel", x0, y0 + rh - 24, w_, grow + 24, C['blue_t'], r=26, f0=f_open - 4, dur=n - f_open + 4)
    pan.anchor(0, 1); pan.scale([(f_open - 4, [1.0, 0.0], 'Linear'), (f_open + d_open, [1.0, 1.0], EXPO)])
    for i, q in enumerate(qs):
        f = 6 + i * 8
        y = y0 + i * (rh + gap)
        shift = grow if i > 0 else 0
        row = card(k, f"Row {i + 1}", x0, y, w_, rh, f, n, stroke=C['grey'] if i else C['blue'], sw=4, r=26, step=False)
        bx, by = row.base
        row.pos([(f, [bx - 48 / W, by], 'Linear'), (f + 14, [bx, by], EXPO)] + (
            [(f_open, [bx, by], 'Linear'), (f_open + d_open, [bx, by - shift / H], EXPO)] if shift else []))
        row.op([(f, 0, 'Linear'), (f + 7, 1, 'Ease out')])
        qb = badge(k, f"Q badge {i + 1}", x0 + 75, y + rh / 2, 84, C['blue'], f + 4, n)
        qt = k.text(f"Q letter {i + 1}", "Q", x0 + 75, y + rh / 2, 40, C['white'], f0=f + 6, dur=n - f - 6, style='ExtraBold', align='center')
        qq = k.text(f"Question {i + 1}", q, x0 + 150, y + rh / 2, 42, C['ink'], f0=f + 4, dur=n - f - 4, style='Bold')
        if textw(q, 42, 'Bold') > 800: raise ValueError(q)
        chev = k.line(f"Chevron {i + 1}", [(x0 + w_ - 100, y + rh / 2 - 8), (x0 + w_ - 80, y + rh / 2 + 10), (x0 + w_ - 60, y + rh / 2 - 8)],
                      C['muted'], px=7, f0=f + 6, dur=n - f - 6)
        for o, fs in ((qb, f + 4), (qt, f + 6), (qq, f + 4), (chev, f + 6)):
            bx2, by2 = o.base
            o.pos([(fs, [bx2 - 48 / W, by2], 'Linear'), (fs + 14, [bx2, by2], EXPO)] + (
                [(f_open, [bx2, by2], 'Linear'), (f_open + d_open, [bx2, by2 - shift / H], EXPO)] if shift else []))
        qq.op([(f + 4, 0, 'Linear'), (f + 11, 1, 'Ease out')]); qt.op([(f + 6, 0, 'Linear'), (f + 11, 1, 'Ease out')])
        chev.op([(f + 6, 0, 'Linear'), (f + 13, 1, 'Ease out')])
        if i == 0:
            chev.rot([(f_open, 0.0, 'Linear'), (f_open + d_open, 180.0, 'S-curve')])
    ans = ("Yes. The free plan has every feature,\nno time limit and no watermark.")
    ao = k.text("Answer text", ans, x0 + 150, y0 + rh + 82, 36, C['ink'], f0=f_open + 8, dur=n - f_open - 8, style='Medium', lh=1.05)
    if max(textw(l, 36, 'Medium') for l in ans.split('\n')) > 900: raise ValueError("answer")
    step_in(ao, f_open + 8)
    return k


# ---------------------------------------------------------------- 6. definition with pronunciation
def definition(d):
    n = 150
    k = d.comp("EX Word definition", n, "ewd"); lab_bg(k, n); light_bg(k, n)
    x0 = 340
    T(k, "Word", "motion", x0, 360, 190, C['ink'], 0, n, style='ExtraBold', maxw=900)
    ul = k.rect("Word underline", x0, 480, 220, 10, C['coral'], r=5, f0=12, dur=n - 12)
    ul.anchor(-1, 0); ul.scale([(12, [0.0, 1.0], 'Linear'), (26, [1.0, 1.0], EXPO)])
    # speaker, respelling and part of speech
    sy = 580
    sp = k.ell("Speaker disc", x0 + 44, sy, 88, 88, C['blue'], f0=22, dur=n - 22); pop(sp, 22)
    sx = x0 + 30
    body_ = k.path("Speaker body", [(sx - 4, sy - 9), (sx + 8, sy - 9), (sx + 24, sy - 24), (sx + 24, sy + 24), (sx + 8, sy + 9), (sx - 4, sy + 9)],
                   f0=26, dur=n - 26, closed=True)
    body_.fill(C['white']); body_.op([(26, 0.0, 'Linear'), (29, 1.0, 'Linear')])
    waves = []
    for j, off in enumerate((12, 28)):
        wv = k.line(f"Speaker wave {j + 1}", [(x0 + 42 + off, sy - 10 - j * 6), (x0 + 50 + off, sy), (x0 + 42 + off, sy + 10 + j * 6)], C['white'], px=5, f0=26, dur=n - 26)
        wv.set(wv.src('shape_stroke', 'corners'), 'round'); waves.append(wv)
        wv.op([(26, 0.0, 'Linear'), (46, 0.0, 'Hold'), (47, 1.0, 'Hold'), (66, 1.0, 'Hold'), (67, 0.0, 'Hold')])
    w1, w2 = textw("MOH", 56, 'ExtraBold'), textw("shun", 56, 'Bold')
    sx1 = x0 + 120; dx_ = sx1 + w1 + 20; sx2 = dx_ + 22 + 20; px2 = sx2 + w2 + 40
    s1 = T(k, "Syllable 1", "MOH", sx1, sy, 56, C['blue'], 30, n, style='ExtraBold', maxw=200)
    dash = k.line("Syllable dash", [(dx_, sy + 4), (dx_ + 22, sy + 4)], C['muted'], px=6, f0=30, dur=n - 30); draw(dash, 30, 8)
    s2 = T(k, "Syllable 2", "shun", sx2, sy, 56, C['muted'], 33, n, style='Bold', maxw=200)
    pulse(s1, 48, 1.12); pulse(s2, 60, 1.12)                          # spoken one after the other, never together
    pill = k.rect("Noun pill", px2, sy - 26, 130, 52, C['blue_t'], r=26, f0=36, dur=n - 36); step_in(pill, 36); pill.stroke(C['blue'], 3)
    T(k, "Noun tag", "NOUN", px2 + 65, sy, 28, C['blue'], 38, n, style='Bold', align='center', track=1.07, maxw=100)
    T(k, "Definition", "The act or process of changing\nposition or place.", x0, 750, 50, C['ink'], 50, n, style='Medium', lh=1.0, maxw=1100)
    T(k, "Example", "“The motion of the waves was slow.”", x0, 920, 38, C['muted'], 74, n, style='Medium', maxw=1100)
    return k


# ---------------------------------------------------------------- 7. tip carousel
def tip_carousel(d):
    n = 210
    k = d.comp("EX Tip carousel", n, "etp"); lab_bg(k, n); light_bg(k, n)
    T(k, "Carousel title", "Three tips for clearer videos", 960, 120, 56, C['ink'], 0, n, style='ExtraBold', align='center', maxw=1400)
    tips = (("Start with the end", "Say the result first,\nthen show how to get there."),
            ("One idea per scene", "Each scene earns one\nsentence. Cut the rest."),
            ("Leave room to read", "Hold every line long enough\nto read it twice."))
    f_slide, d_in = (6, 72, 138), 18
    cx0, cy0, cw, chh = 960, 480, 1000, 460
    for i, (ttl, txt) in enumerate(tips):
        f_in = f_slide[i]; f_out = f_slide[i + 1] if i < 2 else None
        end = (f_out + d_in) if f_out else n
        dur = end - f_in
        parts = []
        c = k.rect(f"Tip card {i + 1}", cx0 - cw / 2, cy0 - chh / 2, cw, chh, C['white'], r=36, f0=f_in, dur=dur); c.shadow(y=-0.006, soft=0.02, op=0.14)
        parts.append(c)
        nb = k.ell(f"Tip number disc {i + 1}", cx0 - 380, cy0, 130, 130, (C['blue'], C['coral'], C['green'])[i], f0=f_in, dur=dur); parts.append(nb)
        nt = k.text(f"Tip number {i + 1}", str(i + 1), cx0 - 380, cy0, 72, C['white'], f0=f_in, dur=dur, style='ExtraBold', align='center'); parts.append(nt)
        tt = k.text(f"Tip title {i + 1}", ttl, cx0 - 280, cy0 - 50, 56, C['ink'], f0=f_in, dur=dur, style='ExtraBold')
        if textw(ttl, 56, 'ExtraBold') > 700: raise ValueError(ttl)
        parts.append(tt)
        ts = k.text(f"Tip text {i + 1}", txt, cx0 - 280, cy0 + 65, 34, C['muted'], f0=f_in, dur=dur, style='Medium', lh=1.0)
        if max(textw(l, 34, 'Medium') for l in txt.split('\n')) > 700: raise ValueError(txt)
        parts.append(ts)
        for o in parts:
            bx, by = o.base
            keys = [(f_in, [bx + 1100 / W, by], 'Linear'), (f_in + d_in, [bx, by], 'quint')]
            if f_out: keys += [(f_out, [bx, by], 'Linear'), (f_out + d_in, [bx - 1100 / W, by], 'quint')]
            o.pos(keys)
    dots = [904, 960, 1016]
    for i, x in enumerate(dots):
        k.ell(f"Page dot {i + 1}", x, 850, 22, 22, C['grey'], f0=6, dur=n - 6)
    act = k.ell("Page dot active", dots[0], 850, 28, 28, C['blue'], f0=6, dur=n - 6)
    ay = act.base[1]
    act.pos([(6, P(dots[0], 850), 'Linear'), (72, P(dots[0], 850), 'Linear'), (72 + 18, P(dots[1], 850), 'quint'),
             (138, P(dots[1], 850), 'Linear'), (138 + 18, P(dots[2], 850), 'quint')])
    return k


# ---------------------------------------------------------------- 8. problem -> solution split
def problem_solution(d):
    n = 150
    k = d.comp("EX Problem solution", n, "epb"); lab_bg(k, n); light_bg(k, n)
    lp = k.rect("Problem panel", 0, 0, 960, 1080, C['coral_t'], f0=0, dur=n)
    pill = card(k, "Problem pill", 140, 190, 240, 62, 4, n, fill=C['coral'], shadow=False, r=31)
    T(k, "Problem tag", "PROBLEM", 260, 221, 32, C['white'], 6, n, style='Bold', align='center', track=1.07)
    T(k, "Problem headline", "Reports take\nhours", 140, 400, 84, C['ink'], 10, n, style='ExtraBold', lh=0.9, maxw=740)
    for i, s in enumerate(("Copying numbers by hand", "Waiting on exports", "Fixing errors at night")):
        y, f = 650 + i * 100, 26 + i * 10
        mark(k, f"Cross {i + 1} a", [(145, y - 15), (175, y + 15)], C['coral'], f, n, px=8, d=6)
        mark(k, f"Cross {i + 1} b", [(145, y + 15), (175, y - 15)], C['coral'], f + 2, n, px=8, d=6)
        T(k, f"Problem item {i + 1}", s, 205, y, 38, C['ink'], f + 2, n, style='Medium', maxw=700)
    rp = k.rect("Solution panel", 960, 0, 960, 1080, C['green_t'], f0=56, dur=n - 56)
    rp.anchor(-1, 0); rp.scale([(56, [0.0, 1.0], 'Linear'), (76, [1.0, 1.0], EXPO)])
    hub = k.ell("Divider disc", 960, 540, 120, 120, C['white'], f0=48, dur=n - 48); hub.stroke(C['grey'], 4); hub.shadow(y=-0.004, soft=0.014, op=0.16)
    pop(hub, 48)
    ar = k.line("Divider arrow", [(936, 540), (982, 540)], C['ink'], px=8, f0=52, dur=n - 52); draw(ar, 52, 8)
    ah = k.ngon("Divider arrow head", 988, 540, 28, 3, C['ink'], f0=58, dur=n - 58); ah.rotv(0.0); pop(ah, 58, 8)
    card(k, "Solution pill", 1100, 190, 260, 62, 72, n, fill=C['green'], shadow=False, r=31)
    T(k, "Solution tag", "SOLUTION", 1230, 221, 32, C['white'], 74, n, style='Bold', align='center', track=1.07)
    T(k, "Solution headline", "One click,\nready in seconds", 1100, 400, 84, C['ink'], 78, n, style='ExtraBold', lh=0.9, maxw=760)
    for i, s in enumerate(("Pulls live numbers", "Exports in one step", "Always up to date")):
        y, f = 650 + i * 100, 94 + i * 10
        tick(k, f"Tick {i + 1}", 1160, y, 40, C['green'], f, n, px=9)
        T(k, f"Solution item {i + 1}", s, 1210, y, 38, C['ink'], f + 2, n, style='Medium', maxw=640)
    return k


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    cause_effect(d); pros_cons(d); labelled_diagram(d); icon_steps(d); faq(d); definition(d); tip_carousel(d); problem_solution(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
