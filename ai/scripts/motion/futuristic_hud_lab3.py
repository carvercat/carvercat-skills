"""Futuristic HUD round 3: eight lab comps for briefs the pack could not serve before (a biometric
scan, drone flight telemetry, a boot-up sequence, a holographic product turntable with faux 3D, a
mission briefing card, a voice-assistant waveform, a satellite orbit tracker and a system warning
cascade), written straight into a .carverproj.

    import futuristic_hud_lab3 as L; presets, masks = L.build(PROJECT.carverproj)

Same palette and rules as futuristic_hud_lab.py (near-black, cyan with glow 0.45-0.6, amber for
alerts, thin strokes, tracked SemiBold caps, stepped Hold changes for digital readouts, continuous
motion one way only). Every move is baked as keys here (no presets to apply): flick() writes the
pack's Flicker-on steps as Hold keys, type_on() types a text 1-2 f per character.
Readable text is never the old dim cyan #0E6F86 (3.5:1 on the ground): labels use #4FA8BF (7.3:1
nominal) and alerts #FF6B5E (7.2:1), converted with the renderer's BT.709 curve (KI-141), so lint
contrast:true passes at 4.5:1.
Faux 3D (turntable, orbit meridians) is computed here and baked to keys every 2 f: each edge of the
turning box is a thin rectangle whose position, rotation, length (scale x) and depth (opacity) are
keyed (Linear joins). The waveform's three sine paths slide one way under mask windows: after
edit.open {path, force:true} run mask.make {ids:[window, content]} (the window FIRST) + parent.clear
for each MASKS entry, then edit.save. Check with carvercat_inspect (curves, lint contrast:true, qc)
and carvercat_look; extract templates with comp_to_template.py (--drop "Lab bg").
Fonts: Rethink Sans must be installed (KI-136). Docs: ai/patterns/futuristic-hud.md (round 3).
Pixel space 1920x1080, y down; comp frames, 30 fps. Names, numbers and places are sample copy.
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from futuristic_hud_lab import Doc, lin, P, COL, EXPO, lab_bg
from futuristic_hud_lab2 import corner_set
from cc import BEZ

PRESETS, MASKS = [], []
W, H = 1920.0, 1080.0


def lin709(h):
    """hex -> linear light with the renderer's BT.709 curve (KI-141: cc.lin renders mid-tones ~10% dark)"""
    h = h.lstrip('#'); v = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return [round(c / 4.5 if c < 0.081 else ((c + 0.099) / 1.099) ** (1 / 0.45), 5) for c in v] + [1.0]


C3 = dict(label=lin709('4FA8BF'), red=lin709('FF6B5E'), green=lin709('3FD08A'), white=lin709('E6FBFF'),
          panel=lin('08121A'), warm=lin('140D04'), crit=lin('2A0806'), ink=lin('05080F'))


def squeeze(spec):
    """drop baked keys that only repeat their neighbours (a hold needs just its two ends)"""
    out = []
    for i, k_ in enumerate(spec):
        if 0 < i < len(spec) - 1 and spec[i - 1][1] == k_[1] == spec[i + 1][1]: continue
        out.append(k_)
    return out


def flick(o, f):
    """the pack's Flicker on as Hold keys: 0 -> 80 -> 15 -> 90 -> 50 -> 100%, 2 f apart (fully on at f + 10)"""
    return o.op([(f, 0.0, 'Hold'), (f + 2, 0.8, 'Hold'), (f + 4, 0.15, 'Hold'), (f + 6, 0.9, 'Hold'), (f + 8, 0.5, 'Hold'),
                 (f + 10, 1.0, 'Hold')])


def type_on(o, f, gap=1.0):
    """types the text on: each character snaps on `gap` frames after the previous one (stagger on opacity only)"""
    rpo = f'src.e_src_text_relative_{o.id}.opacity'
    ents = o.clip['containers'].setdefault('effects', {'entries': [], 'promoted': []})['entries']
    ents.insert(0, {'id': f'e_fx_stagger_{o.id}', 'cap': 'stagger', 'on': True, 'by': 'character', 'order': 'forward',
                    'amount': float(gap), 'amountMode': 'each', 'seed': 1, 'connected': [rpo]})
    o.key(rpo, [(f, 0, 'Linear'), (f + 1, 1, 'Hold')])
    return o


def scan_open(o, f, d=10, sx=1.0):
    """the pack's Scan open (Y) as keys: scale Y 2% -> 100% (expo), fade in over the first 20%"""
    o.scale([(f, [sx, 0.02], 'Linear'), (f + d, [sx, 1.0], EXPO)])
    o.op([(f, 0.0, 'Linear'), (f + max(2, d // 5), 1.0, 'Linear')])
    return o


def draw(o, f, d=14, ease=EXPO):
    o.trim([(f, 0.0, 'Linear'), (f + d, 1.0, ease)], which='end'); return o


def T(k, name, s, x, y, px, col, f, n, align='left', track=1.3, style='SemiBold', mode='flick'):
    t = k.text(name, s, x, y, px, col, f0=f, dur=n - f, style=style, align=align, track=track)
    if mode == 'flick': flick(t, f)
    elif mode == 'type': type_on(t, f)
    return t


def label_value(k, name, lab, val, x, y, f, n, vpx=56, vcol=None, align='left'):
    """a readout: small label (26 px, label colour) over a big value that types on 4 f later"""
    T(k, f"{name} label", lab, x, y, 26, C3['label'], f, n, align=align, track=1.2)
    return T(k, f"{name} value", val, x, y + 52, vpx, vcol or COL['cyan'], f + 4, n, align=align, track=1.1, mode='type')


def ring(k, name, x, y, dia, col, px, f, n):
    o = k.ell(name, x, y, dia, dia, None, f0=f, dur=n - f); o.stroke(col, px); return o


def ping(k, name, x, y, f, dia=60, to=3.0, d=30, col=None):
    """a ring that only grows and fades (one way)"""
    o = ring(k, name, x, y, dia, col or COL['cyan'], 3, f, f + d); o.glow(size=6, amount=0.45)
    o.scale([(f, 0.3, 'Linear'), (f + d, to, BEZ['decel'])]); o.op([(f, 1.0, 'Linear'), (f + d, 0.0, 'Linear')])
    return o


# ---------------------------------------------------------------- 1. biometric scan
ECG_BEAT = [(0, 0), (40, 0), (52, -12), (64, 0), (82, 0), (90, 14), (100, -66), (112, 40), (122, 0), (140, 0), (158, -22), (176, 0),
            (200, 0)]


def bio_scan(d):
    n = 150
    k = d.comp("FH Bio scan", n, "fbs"); lab_bg(k, n)
    cx = 560
    head = k.ell("Head outline", cx, 290, 124, 152, None, f0=0, dur=n); head.stroke(COL['cyan'], 3); head.glow(size=6, amount=0.45)
    draw(head, 0, 18)
    body = k.line("Body outline", [(528, 366), (528, 398), (430, 428), (392, 470), (372, 770), (748, 770), (728, 470), (690, 428),
                                   (592, 398), (592, 366)], COL['cyan'], px=3, f0=0, dur=n,
                  handles=[((0, 0), (0, 0), True), ((0, 0), (0, 0), True), ((40, -6), (-30, 8), False), ((10, -20), (-4, 30), False),
                           ((0, 0), (0, 0), True), ((0, 0), (0, 0), True), ((4, 30), (-10, -20), False), ((30, 8), (-40, -6), False),
                           ((0, 0), (0, 0), True), ((0, 0), (0, 0), True)])
    body.glow(size=6, amount=0.45); draw(body, 2, 20)
    for i, y in enumerate((520, 600, 680)):                        # faint section lines inside the torso
        ln = k.line(f"Section {i + 1}", [(400, y), (720, y)], COL['grid'], px=2, f0=10, dur=n - 10); draw(ln, 10 + 3 * i, 12)
    # the scan: a beam at constant speed from the crown to the waist (y 230 -> 770, f18 -> f78), one pass
    y0, y1, fa, fb = 230, 770, 18, 78
    band = k.rect("Scan glow", cx, y0 - 30, 470, 60, COL['cyan'], f0=fa, dur=fb + 8 - fa, center=True); band.soft(26)
    beam = k.rect("Scan beam", cx, y0, 470, 4, COL['cyan'], f0=fa, dur=fb + 8 - fa, center=True); beam.glow(size=10, amount=0.6)
    for o, dy in ((band, -30), (beam, 0)):
        bx, _ = o.base
        o.pos([(fa, P(cx, y0 + dy), 'Linear'), (fb, P(cx, y1 + dy), 'Linear')])
    band.op([(fa, 0.0, 'Linear'), (fa + 4, 0.22, 'Linear'), (fb, 0.22, 'Linear'), (fb + 8, 0.0, 'Linear')])
    beam.op([(fa, 0.0, 'Linear'), (fa + 4, 1.0, 'Linear'), (fb, 1.0, 'Linear'), (fb + 8, 0.0, 'Linear')])
    at = lambda y: int(round(fa + (y - y0) / (y1 - y0) * (fb - fa)))     # the frame the beam passes y
    for name, x, y, col in (("Brain marker", cx, 280, COL['cyan']), ("Heart marker", 600, 520, COL['amber'])):
        f = at(y)
        m = ring(k, name, x, y, 44, col, 3, f, n); m.glow(size=6, amount=0.5)
        m.scale([(f, 0.0, 'Linear'), (f + 6, 1.15, 'Ease out'), (f + 10, 1.0, 'S-curve')])
        ping(k, f"{name} ping", x, y, f, dia=44, to=2.4, d=24, col=col)
    # right: header, ECG trace, three readouts, status
    x0 = 900
    T(k, "Scan title", "BIOMETRIC SCAN", x0, 230, 40, C3['white'], 4, n, track=1.4)
    T(k, "Subject", "SUBJECT 0427  //  CREW", x0, 282, 26, C3['label'], 10, n, track=1.4)
    frame = k.rect("ECG frame", 1230, 410, 660, 170, None, f0=6, dur=n - 6, center=True); frame.stroke(COL['dim'], 2)
    scan_open(frame, 6, 10)
    pts = []
    for b in range(3):
        pts += [(920 + b * 200 + x, 410 + y) for x, y in (ECG_BEAT if b == 0 else ECG_BEAT[1:])]
    pts.append((1540, 410))
    ecg = k.line("ECG trace", pts, COL['cyan'], px=3, f0=20, dur=n - 20); ecg.glow(size=6, amount=0.5)
    ecg.set(ecg.src('shape_stroke', 'corners'), 'round')
    fe0, fe1 = 20, 110
    ecg.trim([(fe0, 0.0, 'Linear'), (fe1, 1.0, 'Linear')], which='end')
    # the pen rides the tip of the trace: arc-length position baked every frame
    seg = [math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:])]; L = sum(seg)
    def tip(u):
        s = u * L
        for (a, b), l in zip(zip(pts, pts[1:]), seg):
            if s <= l: return (a[0] + (b[0] - a[0]) * s / l, a[1] + (b[1] - a[1]) * s / l)
            s -= l
        return pts[-1]
    pen = k.ell("ECG pen", 920, 410, 12, 12, C3['white'], f0=fe0, dur=n - fe0); pen.glow(size=8, amount=0.6)
    pen.pos([(f, P(*tip((f - fe0) / (fe1 - fe0))), 'Linear') for f in range(fe0, fe1 + 1)])
    pen.op([(fe0, 1.0, 'Linear'), (fe1, 1.0, 'Linear'), (fe1 + 6, 0.0, 'Linear')])
    hf = at(520)
    label_value(k, "Heart rate", "HEART RATE", "72 BPM", x0, 540, hf + 2, n, vpx=50, vcol=COL['amber'])
    label_value(k, "Oxygen", "SPO2", "98 %", 1180, 540, hf + 10, n, vpx=50)
    label_value(k, "Temp", "TEMP", "36.7 C", 1560, 540, hf + 18, n, vpx=50, align='right')
    T(k, "Status", "SCAN COMPLETE", x0, 720, 40, C3['green'], 86, n, track=1.4)


# ---------------------------------------------------------------- 2. drone telemetry
def telemetry(d):
    n = 150
    k = d.comp("FH Telemetry", n, "ftm"); lab_bg(k, n)
    corner_set(k, "Frame corner", 960, 540, 1680, 900, 60, 0, px=4)
    # artificial horizon: a rig on the horizon line (visible, centred); the ladder rolls with it
    cx, cy = 960, 540
    hz = k.line("Horizon", [(cx - 330, cy), (cx + 330, cy)], COL['cyan'], px=3, f0=0, dur=n)
    hz.glow(size=6, amount=0.45)
    kids = []
    for i, dy in enumerate((-160, -80, 80, 160)):
        w = 140 if abs(dy) == 160 else 220
        ln = k.line(f"Pitch {i + 1}", [(cx - w / 2, cy + dy), (cx - 30, cy + dy)], COL['dim'], px=2, f0=0, dur=n)
        rn = k.line(f"Pitch {i + 1} right", [(cx + 30, cy + dy), (cx + w / 2, cy + dy)], COL['dim'], px=2, f0=0, dur=n)
        kids += [ln, rn]
    from cartoon_bounce_lab2 import rig
    rig(kids, hz)
    for o in [hz] + kids: o.op([(4, 0.0, 'Linear'), (12, 1.0, 'Linear')])
    hz.trim([(0, 0.5, 'Linear'), (14, 0.0, EXPO)], which='start')
    tp = [e for e in hz.clip['containers']['effects']['entries'] if e['cap'] == 'trim'][0]['id']
    hz.key(f'fx.{tp}.end', [(0, 0.5, 'Linear'), (14, 1.0, EXPO)])
    # a banking turn: roll eases out to -9 deg, back through +4, settles level (S-curves between extremes)
    hz.rot([(0, 0.0, 'Linear'), (20, 0.0, 'Linear'), (50, -9.0, 'S-curve'), (95, 4.0, 'S-curve'), (125, 0.0, 'S-curve')])
    hz.pos([(0, P(cx, cy), 'Linear'), (20, P(cx, cy), 'Linear'), (60, P(cx, cy + 24), 'S-curve'), (110, P(cx, cy - 12), 'S-curve'),
            (135, P(cx, cy), 'S-curve')])
    ac = k.line("Aircraft", [(cx - 120, cy), (cx - 40, cy), (cx - 20, cy + 22), (cx, cy), (cx + 20, cy + 22), (cx + 40, cy), (cx + 120, cy)],
                COL['amber'], px=4, f0=0, dur=n)
    ac.glow(size=6, amount=0.5); flick(ac, 8)
    # heading dial: the tick ring turns one way as the heading rises 042 -> 071
    dx, dy_ = 960, 880
    dial = k.ell("Heading ring", dx, dy_, 220, 220, None, f0=0, dur=n); dial.stroke(COL['cyan'], 10, cap='butt', line='dashed', dash=3, gap=18)
    dial.rot([(0, 0.0, 'Linear'), (n, 29.0, 'Linear')]); scan_open(dial, 6, 10)
    edge = ring(k, "Heading edge", dx, dy_, 250, COL['dim'], 2, 6, n); scan_open(edge, 6, 10)
    ptr = k.ngon("Heading pointer", dx, dy_ - 140, 26, 3, COL['amber'], f0=10, dur=n - 10); ptr.rotv(-90.0); flick(ptr, 10)
    for i, (hdg, f0, f1) in enumerate((("042", 10, 60), ("056", 60, 105), ("071", 105, n))):
        t = k.text(f"Heading {i + 1}", hdg, dx, dy_, 44, C3['white'], f0=f0, dur=f1 - f0, style='SemiBold', align='center', track=1.2)
        if i == 0: flick(t, f0)
    T(k, "Heading label", "HDG", dx, dy_ - 46, 26, C3['label'], 14, n, align='center', track=1.4)
    # speed (left) and altitude (right) boxes, values step (each held >= 40 f: lint reading time)
    for side, x, lab, vals in (("Speed", 470, "SPD  M/S", ("12.4", "14.1", "15.8")), ("Altitude", 1450, "ALT  M", ("118", "124", "131"))):
        box = k.rect(f"{side} box", x, cy, 190, 76, None, f0=6, dur=n - 6, center=True); box.stroke(COL['cyan'], 3); scan_open(box, 6, 10)
        T(k, f"{side} label", lab, x, cy - 92, 26, C3['label'], 12, n, align='center', track=1.4)
        for i, (v, f0, f1) in enumerate(zip(vals, (14, 55, 100), (55, 100, n))):
            t = k.text(f"{side} {i + 1}", v, x, cy, 44, C3['white'], f0=f0, dur=f1 - f0, style='SemiBold', align='center', track=1.1)
            if i == 0: flick(t, f0)
        for j in range(5):                                            # a static scale beside the box
            tx = x - 145 if side == "Speed" else x + 145
            tk = k.line(f"{side} tick {j + 1}", [(tx - 14, cy - 120 + j * 60), (tx + 14, cy - 120 + j * 60)], COL['dim'], px=2, f0=8, dur=n - 8)
            flick(tk, 8 + j)
    # status corners
    rec = k.ell("Rec dot", 196, 154, 20, 20, C3['red'], f0=4, dur=n - 4)
    rec.op([(4, 0.0, 'Hold'), (6, 1.0, 'Hold'), (36, 0.25, 'Hold'), (51, 1.0, 'Hold'), (81, 0.25, 'Hold'), (96, 1.0, 'Hold'),
            (126, 0.25, 'Hold'), (141, 1.0, 'Hold')])                  # a slow blink: 1 a second
    T(k, "Rec", "REC  00:12:48", 222, 154, 30, C3['red'], 4, n, track=1.3)
    T(k, "Battery", "BAT  78%", 1724, 154, 30, C3['white'], 8, n, align='right', track=1.3)
    T(k, "GPS", "GPS  14 SAT", 196, 886, 26, C3['label'], 12, n, track=1.4)
    T(k, "Coords", "47.3769 N  8.5417 E", 196, 926, 30, C3['white'], 16, n, track=1.2)
    T(k, "Mode", "MODE  CRUISE", 1724, 926, 30, C3['white'], 20, n, align='right', track=1.3)


# ---------------------------------------------------------------- 3. boot-up sequence
def boot(d):
    n = 150
    k = d.comp("FH Boot sequence", n, "fbt"); lab_bg(k, n)
    x0, x1, y0, step = 260, 1160, 250, 66
    T(k, "Boot header", "CORE OS  v4.2  //  COLD START", x0, 180, 26, C3['label'], 0, n, track=1.4)
    lines = ["BIOS CHECK", "MEMORY 64 GB", "NEURAL CORE", "SENSOR ARRAY", "UPLINK", "SECURITY KEYS"]
    from cc import textw
    done = []
    for i, s in enumerate(lines):
        f = 8 + i * 13
        y = y0 + i * step
        T(k, f"Line {i + 1}", "> " + s, x0, y, 38, C3['white'], f, n, track=1.15, mode='type')
        fo = f + len(s) + 4                                         # OK lands after the line has typed
        ww = textw("> " + s, 38, 'SemiBold') * 1.1
        lead = k.line(f"Leader {i + 1}", [(x0 + ww + 24, y + 4), (x1 - 110, y + 4)], COL['dim'], px=3, f0=f + 2, dur=n - f - 2)
        lead.stroke(COL['dim'], 3, cap='butt', line='dotted', dash=3, gap=12)
        draw(lead, f + 2, fo - f - 2, 'Linear')
        T(k, f"OK {i + 1}", "[ OK ]", x1, y, 38, C3['green'], fo, n, align='right', track=1.15)
        done.append(fo)
    # progress: a frame with a fill that steps on as each line reports OK
    by = y0 + 6 * step + 40
    fr = k.rect("Progress frame", (x0 + x1) / 2, by, x1 - x0, 26, None, f0=4, dur=n - 4, center=True); fr.stroke(COL['dim'], 2)
    scan_open(fr, 4, 8)
    fill = k.rect("Progress fill", x0 + 6, by - 7, x1 - x0 - 12, 14, COL['cyan'], f0=4, dur=n - 4); fill.anchor(-1, 0)
    fill.glow(size=6, amount=0.45)
    fill.scale([(4, [0.0, 1.0], 'Hold')] + [(f, [round((i + 1) / 6, 4), 1.0], 'Hold') for i, f in enumerate(done)])
    # the mark draws on and the system comes online
    mx, my = 1480, 400
    hexo = k.ngon("Core mark", mx, my, 220, 6, None, f0=0, dur=n); hexo.nofill(); hexo.stroke(COL['cyan'], 4); hexo.glow(size=8, amount=0.5)
    hexo.rotv(90.0); draw(hexo, done[-1] - 6, 18)
    orbit = ring(k, "Core ring", mx, my, 300, COL['dim'], 2, done[-1] - 4, n); orbit.set(orbit.src('shape_stroke', 'cap'), 'butt')
    tp = orbit.trim([(done[-1] - 4, 0.0, 'Linear'), (done[-1] + 10, 0.3, EXPO)], which='end')
    orbit.rot([(done[-1] - 4, 0.0, 'Linear'), (n, 120.0, 'Linear')])
    core = k.ell("Core dot", mx, my, 40, 40, COL['amber'], f0=done[-1] + 6, dur=n - done[-1] - 6); core.glow(size=8, amount=0.55)
    flick(core, done[-1] + 6)
    T(k, "Online", "SYSTEM ONLINE", mx, my + 220, 44, COL['cyan'], done[-1] + 10, n, align='center', track=1.3)


# ---------------------------------------------------------------- 4. holographic turntable (faux 3D)
def turntable(d):
    n = 150
    k = d.comp("FH Holo turntable", n, "fho"); lab_bg(k, n)
    cx, cy, base_y = 860, 470, 770
    a, h, c = 150, 190, 105                                         # half width, half height, half depth (px)
    el = math.radians(20.0); focal = 1700.0
    verts = [(sx * a, sy * h, sz * c) for sy in (-1, 1) for sz in (-1, 1) for sx in (-1, 1)]
    edges = [(i, j) for i in range(8) for j in range(i + 1, 8)
             if sum(1 for p, q in zip(verts[i], verts[j]) if p != q) == 1]
    def theta(f): return math.radians(25.0 + 360.0 * f / n)        # one full turn in 150 f (5 s), one way
    def proj(v, f):
        x, y, z = v; t = theta(f)
        X = x * math.cos(t) + z * math.sin(t); Z = -x * math.sin(t) + z * math.cos(t)
        Y2 = y * math.cos(el) - Z * math.sin(el); D = y * math.sin(el) + Z * math.cos(el)
        s = focal / (focal - D)
        return cx + X * s, cy - Y2 * s, D
    fs = list(range(0, n + 1, 2))
    # projector base and light cone first (under the model)
    cone = k.path("Light cone", [(cx - 200, base_y), (cx - 150, cy + 210), (cx + 150, cy + 210), (cx + 200, base_y)], f0=8, dur=n - 8, closed=True)
    cone.fill(COL['cyan']); cone.op([(8, 0.0, 'Linear'), (20, 0.08, 'Linear')])
    for i, (w_, hh, col, px) in enumerate(((460, 96, COL['cyan'], 3), (340, 70, COL['dim'], 2))):
        b = k.ell(f"Base ring {i + 1}", cx, base_y, w_, hh, None, f0=0, dur=n); b.stroke(col, px); b.glow(size=6, amount=0.45)
        scan_open(b, i * 3, 10)
    arc_ = k.ell("Base scan", cx, base_y, 400, 84, None, f0=6, dur=n - 6); arc_.stroke(COL['cyan'], 5, cap='butt'); arc_.glow(size=8, amount=0.55)
    tp = arc_.trim([(6, 0.0, 'Linear'), (16, 0.22, EXPO)], which='end'); arc_.set(tp + '.start', 0.0)
    arc_.key(tp + '.offset', [(6, 0.0, 'Linear'), (n, 1.5, 'Linear')])  # the arc runs round the base, one way
    # the model: 12 edges and 8 corner dots, baked every 2 f; brightness follows depth (near 1.0, far 0.35)
    def depth_op(D): return round(0.35 + 0.65 * (D + 260) / 520, 3)
    for ei, (i, j) in enumerate(edges):
        e = k.rect(f"Edge {ei + 1}", cx, cy, 100, 3, COL['cyan'], f0=0, dur=n, center=True); e.glow(size=6, amount=0.5)
        pos, rot, sc, op = [], [], [], []
        prev = None
        for f in fs:
            x1, y1, d1 = proj(verts[i], f); x2, y2, d2 = proj(verts[j], f)
            ang = -math.degrees(math.atan2(y2 - y1, x2 - x1))
            if prev is not None:                                      # a line has no direction: unwrap by 180
                while ang - prev > 90: ang -= 180
                while ang - prev < -90: ang += 180
            prev = ang
            pos.append((f, P((x1 + x2) / 2, (y1 + y2) / 2), 'Linear')); rot.append((f, round(ang, 3), 'Linear'))
            sc.append((f, [round(max(0.02, math.hypot(x2 - x1, y2 - y1) / 100), 4), 1.0], 'Linear'))
            op.append((f, depth_op((d1 + d2) / 2), 'Linear'))
        e.pos(pos); e.rot(rot); e.scale(sc)
        op = [(f, v * min(1.0, max(0.0, (f - 10 - 2 * ei % 8) / 8)), ez) for f, v, ez in op]   # edges switch on f10-24
        e.op(squeeze([(f, round(v, 3), ez) for f, v, ez in op]))
    for vi, v in enumerate(verts):
        dot = k.ell(f"Corner {vi + 1}", cx, cy, 12, 12, C3['white'], f0=0, dur=n); dot.glow(size=6, amount=0.55)
        dot.pos([(f, P(*proj(v, f)[:2]), 'Linear') for f in fs])
        dot.op(squeeze([(f, round(depth_op(proj(v, f)[2]) * (1.0 if f >= 24 else 0.0), 3), 'Linear') for f in fs]))
    # a scan line passes down the model once
    sl = k.rect("Model scan", cx, cy - 250, 420, 3, COL['cyan'], f0=30, dur=60, center=True); sl.glow(size=10, amount=0.6)
    sl.pos([(30, P(cx, cy - 250), 'Linear'), (84, P(cx, cy + 250), 'S-curve')]); sl.op([(30, 0.0, 'Linear'), (34, 0.8, 'Linear'),
                                                                                         (80, 0.8, 'Linear'), (88, 0.0, 'Linear')])
    # callout
    lx = 1220
    ld = k.line("Callout leader", [(cx + 190, cy - 170), (lx - 30, cy - 250), (lx + 380, cy - 250)], COL['dim'], px=2, f0=20, dur=n - 20)
    draw(ld, 20, 14)
    T(k, "Model name", "MODEL  X-7", lx, cy - 300, 48, C3['white'], 26, n, track=1.3)
    label_value(k, "Scan", "360 SCAN", "COMPLETE", lx, cy - 200, 34, n, vpx=40)
    label_value(k, "Dims", "DIMENSIONS  MM", "300 x 380 x 210", lx, cy - 70, 42, n, vpx=40, vcol=C3['white'])
    label_value(k, "Mass", "MASS", "2.4 KG", lx, cy + 60, 50, n, vpx=40, vcol=C3['white'])


# ---------------------------------------------------------------- 5. mission briefing card
def mission(d):
    n = 180
    k = d.comp("FH Mission briefing", n, "fmb"); lab_bg(k, n)
    cx, cy, pw, ph = 960, 560, 1300, 660
    l, t = cx - pw / 2, cy - ph / 2
    pan = k.rect("Panel", cx, cy, pw, ph, C3['panel'], f0=0, dur=n, center=True); pan.stroke(COL['dim'], 2); scan_open(pan, 0, 12)
    corner_set(k, "Panel corner", cx, cy, pw + 24, ph + 24, 46, 0, px=4)
    strip = k.rect("Header strip", cx, t + 40, pw, 80, COL['grid'], f0=4, dur=n - 4, center=True); scan_open(strip, 4, 10)
    T(k, "Mission no", "MISSION 07", l + 60, t + 40, 30, COL['amber'], 10, n, track=1.5)
    T(k, "Clearance", "CLEARANCE  //  OMEGA", l + pw - 60, t + 40, 26, C3['label'], 14, n, align='right', track=1.4)
    T(k, "Operation", "OPERATION NIGHTFALL", l + 40, t + 130, 60, C3['white'], 18, n, track=1.2, mode='type')
    # map window: grid, contours, a route that draws to the target, pings at the target (one way)
    mx0, my0, mw, mh = l + 40, t + 190, 560, 400
    mxc, myc = mx0 + mw / 2, my0 + mh / 2
    mf = k.rect("Map frame", mxc, myc, mw, mh, None, f0=10, dur=n - 10, center=True); mf.stroke(COL['dim'], 2); scan_open(mf, 10, 10)
    for i in range(1, 7):
        g = k.line(f"Grid V{i}", [(mx0 + i * mw / 7, my0 + 6), (mx0 + i * mw / 7, my0 + mh - 6)], COL['grid'], px=2, f0=14, dur=n - 14)
        draw(g, 14 + i, 10)
    for i in range(1, 5):
        g = k.line(f"Grid H{i}", [(mx0 + 6, my0 + i * mh / 5), (mx0 + mw - 6, my0 + i * mh / 5)], COL['grid'], px=2, f0=14, dur=n - 14)
        draw(g, 16 + i, 10)
    for i, (w_, h_) in enumerate(((330, 210), (230, 140), (130, 80))):
        ct = k.ell(f"Contour {i + 1}", mxc + 70, myc - 40, w_, h_, None, f0=18, dur=n - 18); ct.stroke(COL['dim'], 2); draw(ct, 18 + 3 * i, 16)
    sx, sy, tx, ty = mx0 + 70, my0 + mh - 60, mxc + 120, myc - 50
    route = k.line("Route", [(sx, sy), (tx, ty)], COL['cyan'], px=4, f0=40, dur=n - 40, handles=[((0, 0), (40, -200), False), ((-220, 60), (0, 0), False)])
    route.stroke(COL['cyan'], 4, cap='butt', line='dashed', dash=14, gap=10); route.glow(size=6, amount=0.45)
    draw(route, 40, 30, BEZ['smooth'])
    st = k.rect("Start marker", sx, sy, 18, 18, COL['cyan'], f0=36, dur=n - 36, center=True); st.rotv(45.0); flick(st, 36)
    tg = ring(k, "Target", tx, ty, 34, COL['amber'], 4, 66, n); tg.glow(size=8, amount=0.55)
    tg.scale([(66, 0.0, 'Linear'), (72, 1.2, 'Ease out'), (76, 1.0, 'S-curve')])
    for i in range(3):
        ping(k, f"Target ping {i + 1}", tx, ty, 70 + 30 * i, dia=34, to=3.2, d=30, col=COL['amber'])
    T(k, "Target tag", "RELAY 3", tx, ty + 50, 26, COL['amber'], 74, n, align='center', track=1.4)
    # objectives
    ox = l + 660
    T(k, "Objectives", "OBJECTIVES", ox, t + 230, 26, C3['label'], 30, n, track=1.5)
    for i, s in enumerate(("REACH THE NORTH RELAY", "RECOVER THE DATA CORE", "EXTRACT BEFORE DAWN")):
        f = 44 + 12 * i; y = t + 300 + i * 72
        bx = k.rect(f"Check {i + 1}", ox + 13, y, 26, 26, None, f0=f, dur=n - f, center=True); bx.stroke(COL['cyan'], 3); flick(bx, f)
        T(k, f"Objective {i + 1}", s, ox + 50, y, 32, C3['white'], f + 4, n, track=1.1, mode='type')
    # deploy line
    T(k, "Deploy label", "DEPLOY IN", ox, t + 540, 26, C3['label'], 96, n, track=1.5)
    T(k, "Deploy time", "00:30:00", ox, t + 590, 52, COL['amber'], 100, n, track=1.3)


# ---------------------------------------------------------------- 6. voice-assistant waveform
def sine_path(x0, y, lam, amp, width):
    """a sine wave from x0 rightwards, nodes every quarter wavelength with tangent handles"""
    pts, hs = [], []
    k_ = lam / 4; m = 2 * math.pi * amp / lam * k_ / 3            # handle height that follows the slope at the zero crossings
    nq = int(width / k_) + 1
    for i in range(nq + 1):
        ph = i % 4                                                  # 0 zero rising, 1 peak, 2 zero falling, 3 trough
        yy = y + (0, -amp, 0, amp)[ph]
        slope = (-1, 0, 1, 0)[ph] * m                               # y down: rising means negative dy
        pts.append((x0 + i * k_, yy))
        hs.append(((-k_ / 3, -slope), (k_ / 3, slope), False))
    return pts, hs


def waveform(d):
    n = 150
    k = d.comp("FH Voice waveform", n, "fvw"); lab_bg(k, n)
    cx, cy, ww, wh = 960, 540, 1200, 300
    x0 = cx - ww / 2
    T(k, "Listening", "LISTENING", cx, 300, 30, C3['label'], 2, n, align='center', track=1.6)
    mic = ring(k, "Mic ring", cx, 224, 64, COL['cyan'], 3, 0, n); mic.glow(size=8, amount=0.5); scan_open(mic, 0, 10)
    md = k.ell("Mic dot", cx, 224, 18, 18, COL['cyan'], f0=4, dur=n - 4); md.glow(size=6, amount=0.5); flick(md, 4)
    for i in range(2):
        ping(k, f"Mic ping {i + 1}", cx, 224, 20 + 22 * i, dia=64, to=2.0, d=26)
    base = k.line("Wave base", [(x0, cy), (x0 + ww, cy)], COL['grid'], px=2, f0=0, dur=n); draw(base, 0, 14)
    # amplitude (scale y) idles low, follows the voice f18-118 with hand-set extremes, settles low again
    amp_keys = [(0, 0.35, 'Linear'), (14, 0.35, 'Linear'), (24, 1.0, 'S-curve'), (44, 0.6, 'S-curve'), (62, 0.95, 'S-curve'),
                (82, 0.5, 'S-curve'), (100, 0.9, 'S-curve'), (122, 0.35, 'S-curve')]   # scale y also thins the stroke: never under 35%
    for i, (lam, amp, travel, col, px, opv, sc) in enumerate(((400, 110, 800, COL['cyan'], 5, 1.0, 1.0), (300, 84, 900, C3['white'], 4, 0.7, 1.0),
                                                               (240, 64, 960, COL['amber'], 4, 0.6, 1.0))):
        pts, hs = sine_path(x0, cy, lam, amp, ww + travel + lam)
        wv = k.line(f"Wave {i + 1}", pts, col, px=px, f0=0, dur=n, handles=hs); wv.glow(size=8, amount=0.5)
        bx, by = wv.base
        wv.pos([(0, [bx, by], 'Linear'), (n, [bx - travel / W, by], 'Linear')])     # slides left, one way, constant speed
        wv.scale([(f, [1.0, round(v * sc, 3)], e) for f, v, e in amp_keys])
        wv.op([(0, 0.0, 'Linear'), (8, opv, 'Linear')])
        win = k.rect(f"Wave window {i + 1}", cx, cy, ww, wh, COL['cyan'], f0=0, dur=n, center=True); win.soft(90)
        MASKS.append(("FH Voice waveform", f"Wave {i + 1}", f"Wave window {i + 1}"))
    T(k, "Transcript", "Set course for the north relay", cx, 790, 52, C3['white'], 30, n, align='center', track=1.0, style='Medium',
      mode='type')
    T(k, "Confirm", "ROUTE CONFIRMED", cx, 870, 30, C3['green'], 110, n, align='center', track=1.5)


# ---------------------------------------------------------------- 7. satellite orbit tracker
def orbit(d):
    n = 150
    k = d.comp("FH Orbit tracker", n, "fob"); lab_bg(k, n)
    px_, py_, R = 700, 540, 210
    oa, ob, tilt = 380, 120, math.radians(16.0)
    def opos(u):
        ph = 2 * math.pi * u
        x, y = oa * math.cos(ph), -ob * math.sin(ph)                 # ellipse path: starts at 3 o'clock, counter-clockwise
        return px_ + x * math.cos(tilt) + y * math.sin(tilt), py_ - x * math.sin(tilt) + y * math.cos(tilt)
    back = k.ell("Orbit", px_, py_, 2 * oa, 2 * ob, None, f0=0, dur=n); back.stroke(COL['dim'], 2, line='dashed', dash=10, gap=10)
    back.rotv(math.degrees(tilt)); draw(back, 4, 24)
    globe = k.ell("Planet", px_, py_, 2 * R, 2 * R, C3['panel'], f0=0, dur=n); globe.stroke(COL['cyan'], 3); globe.glow(size=8, amount=0.45)
    scan_open(globe, 0, 12)
    for i, lat in enumerate((-40, 0, 40)):
        w_ = 2 * R * math.cos(math.radians(lat)); y = py_ - R * math.sin(math.radians(lat))
        e = k.ell(f"Latitude {i + 1}", px_, y, w_, w_ * 0.22, None, f0=8, dur=n - 8); e.stroke(COL['dim'], 2); draw(e, 8 + 2 * i, 14)
    # meridians: width = 2R |sin(phi)|, phi turning one way (half a turn in 150 f repeats the pattern)
    fs = list(range(0, n + 1, 2))
    for i, ph0 in enumerate((20, 80, 140)):
        m = k.ell(f"Meridian {i + 1}", px_, py_, 2 * R, 2 * R, None, f0=8, dur=n - 8); m.stroke(COL['dim'], 2)
        m.scale([(max(8, f), [round(max(0.01, abs(math.sin(math.radians(ph0 + 180.0 * f / n)))), 4), 1.0], 'Linear') for f in fs if f >= 8])
        m.op([(8, 0.0, 'Linear'), (16, 1.0, 'Linear')])
    front = k.ell("Orbit front", px_, py_, 2 * oa, 2 * ob, None, f0=0, dur=n); front.stroke(COL['cyan'], 2, line='dashed', dash=10, gap=10)
    front.rotv(math.degrees(tilt)); tp = front.trim([(4, 0.5, 'Linear'), (28, 1.0, EXPO)], which='end'); front.set(tp + '.start', 0.5)
    # ground station on the near side, and the satellite: one way along the orbit, hidden behind the planet
    gx, gy = px_ + 60, py_ + 150
    gs = k.rect("Station", gx, gy, 16, 16, COL['amber'], f0=12, dur=n - 12, center=True); gs.rotv(45.0); flick(gs, 12)
    u0, du = 0.56, 0.95
    def u(f): return u0 + du * f / n
    def hidden(uu):
        x, y = opos(uu); ph = (uu % 1.0)
        return ph < 0.5 and math.hypot(x - px_, y - py_) < R - 4
    for j, (lag, size, opv) in enumerate(((0.0, 18, 1.0), (0.018, 12, 0.5), (0.036, 8, 0.25))):
        nm = "Satellite" if j == 0 else f"Satellite trail {j}"
        s = k.ell(nm, *opos(u0 - lag), size, size, COL['amber'] if j == 0 else COL['cyan'], f0=0, dur=n); s.glow(size=8, amount=0.55)
        s.pos([(f, P(*opos(u(f) - lag)), 'Linear') for f in fs])
        ops, last = [], None
        for f in range(0, n + 1):
            v = 0.0 if f < 20 else (0.0 if hidden(u(f) - lag) else opv)
            if v != last: ops.append((f, v, 'Hold')); last = v
        s.op(ops)
    # acquisition: the satellite passes nearest the station (u = 0.75)
    fa = int(round((0.75 - u0) / du * n))
    for i in range(2):
        ping(k, f"Station ping {i + 1}", gx, gy, fa - 6 + 14 * i, dia=30, to=3.0, d=28, col=COL['amber'])
    # readouts
    rx = 1150
    T(k, "Sat name", "SAT-04  //  LEO", rx, 260, 44, C3['white'], 6, n, track=1.2)
    label_value(k, "Alt", "ALTITUDE", "412 KM", rx, 350, 12, n, vpx=48)
    label_value(k, "Vel", "VELOCITY", "7.66 KM/S", rx, 470, 18, n, vpx=48)
    label_value(k, "Inc", "INCLINATION", "51.6 DEG", rx, 590, 24, n, vpx=48)
    T(k, "Signal", "SIGNAL ACQUIRED", rx, 760, 34, C3['green'], fa, n, track=1.3)


# ---------------------------------------------------------------- 8. system warning cascade
def warnings(d):
    n = 120
    k = d.comp("FH Warning cascade", n, "fwc"); lab_bg(k, n)
    ww_, wh_ = 780, 216
    items = (("WARNING 01", "CORE TEMP  98 C"), ("WARNING 02", "COOLANT FLOW LOW"), ("WARNING 03", "LINK UNSTABLE"),
             ("CRITICAL 04", "POWER BUS FAULT"))
    for i, (head, body) in enumerate(items):
        f = 4 + i * 9
        x, y = 200 + i * 150, 110 + i * 150                         # each window covers only the empty lower part of the last
        crit = i == 3
        acc = C3['red'] if crit else COL['amber']
        win = k.rect(f"Window {i + 1}", x + ww_ / 2, y + wh_ / 2, ww_, wh_, C3['crit'] if crit else C3['warm'], f0=f, dur=n - f, center=True)
        win.stroke(acc, 3); scan_open(win, f, 8)
        hb = k.rect(f"Window {i + 1} bar", x + ww_ / 2, y + 27, ww_, 54, acc, f0=f, dur=n - f, center=True); scan_open(hb, f, 8)
        T(k, f"Window {i + 1} head", head, x + 28, y + 27, 30, C3['ink'], f + 6, n, track=1.2)
        T(k, f"Window {i + 1} code", f"ERR 0x{(0x3A + 17 * i):02X}", x + ww_ - 28, y + 27, 30, C3['ink'], f + 6, n, align='right', track=1.1)
        T(k, f"Window {i + 1} text", body, x + 28, y + 108, 46, C3['white'], f + 8, n, track=1.15, mode='type')
    # the final banner: scan open, one slow dip to 40% (f90-98, far under 3 flashes a second), then steady
    fb = 56
    band = k.rect("Critical band", 960, 930, 1640, 110, C3['crit'], f0=fb, dur=n - fb, center=True); scan_open(band, fb, 10)
    for j, y in enumerate((875, 985)):
        e = k.rect(f"Critical edge {j + 1}", 960, y, 1640, 5, C3['red'], f0=fb, dur=n - fb, center=True); e.glow(size=8, amount=0.5)
        scan_open(e, fb, 10)
    t = k.text("Critical text", "SYSTEM OVERRIDE REQUIRED", 960, 930, 56, C3['red'], f0=fb + 6, dur=n - fb - 6, style='SemiBold',
               align='center', track=1.3)
    t.glow(size=8, amount=0.45)
    t.op([(fb + 6, 0.0, 'Hold'), (fb + 8, 1.0, 'Hold'), (fb + 34, 0.4, 'Hold'), (fb + 42, 1.0, 'Hold')])


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    bio_scan(d); telemetry(d); boot(d); turntable(d); mission(d); waveform(d); orbit(d); warnings(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
