"""Write the SaaS UI lab comps (round 1) in design units (cc2.py through dvsu_kit.py).

    import saas_ui_lab as L; doc = L.build(); doc.send(client, PROJECT.carverproj)   # scene.apply per comp, presets, edit.save

The rolling counter and the typing caret are placed from text measurements. They are fixed numbers below (MEASURED), read once on
0.1.8.1 with measure.boxes (the ink box of a point text at x = 760, Rethink Sans Bold 120 px, and at x = 712, Regular 38 px), so
the lab builds without a running app. Presets (Toast drop - spring, Card lift, Toast exit up, Tap ripple) are applied after the
comps exist (KDoc.send); the counter's windows are scene masks.
Docs: ai/patterns/saas-ui.md. Design units: px from the top-left, y down; frames, 30 fps.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dvsu_kit import KDoc, css, BEZ, LINE

COL = dict(bg=css('0E1020'), card=css('FFFFFF'), ink=css('14151C'), muted=css('6B7080'), accent=css('5B5BF6'),
           ok=css('16A34A'), off=css('D5D8E0'), line=css('E6E8EF'), canvas=css('F4F5F8'), side=css('14151C'),
           side2=css('2A2C38'))
EXPO = BEZ['expo']
SMOOTH = BEZ['smooth']
SNAP = (0.34, 1.2, 0.64, 1)   # small overshoot for a toggle knob
CURSOR = [(0, 0), (0, 34), (9, 26), (15, 40), (21, 37), (15, 24), (26, 24)]

COUNT = "$48,200"; COUNT_X, COUNT_Y, COUNT_PX = 760, 540, 120
LOOPS = {1: 0, 2: 0, 4: 1, 5: 1, 6: 2}     # extra full turns per digit column (index in COUNT)
TYPED = "acme corp"; TYPE_PX = 38; TYPE_X = 712

# (ink x, ink width) in px; a point text left at x = 760 (counter) or 712 (typed): the first i letters, and single characters
MEASURED = dict(
    count=[(764.68, 61.2), (764.68, 132.307), (764.68, 197.674), (764.68, 225.36), (764.68, 293.318), (764.68, 364.085), (764.68, 432.571)],
    char={'$': (764.68, 61.2), ',': (761.68, 21.72), '0': (763.24, 63.24), '2': (766.36, 57.84), '4': (763.84, 63.48), '8': (765.52, 58.68)},
    typed=[(713.9, 18.582), (713.9, 38.838), (713.9, 72.122), (713.9, 93.807), (713.9, 93.807), (713.9, 124.802), (713.9, 147.408),
           (713.9, 161.709), (713.9, 184.478)])


def lab_bg(k, n):
    k.rect("Lab bg", 0, 0, 1920, 1080, COL['bg'], f0=0, dur=n)


def cursor_click(d):
    n = 60
    k = d.comp("SU Cursor click", n, "cur"); lab_bg(k, n)
    tip = (960, 540); s = 2.4
    pts = [(tip[0] + x * s, tip[1] + y * s) for x, y in CURSOR]
    ring = k.ell("Ripple", tip[0], tip[1], 120, 120, None, f0=28, dur=18); ring.stroke(COL['accent'], 5)
    k.preset("Ripple", "Tap ripple")
    cur = k.poly("Cursor", pts, f0=0, dur=n); cur.fill(COL['card']); cur.stroke(COL['ink'], 2.5)
    cx, cy = cur.base
    dx, dy = 300, 220                       # travel: from lower right to the target
    cur.pos([(0, (cx + dx, cy + dy), 'Linear'), (22, (cx, cy), SMOOTH)])
    cur.op([(0, 0, 'Linear'), (5, 1, 'Ease out')])
    cur.anchor(-1, 1)                       # pivot at the tip (left, top)
    cur.scale([(26, 1.0, 'Linear'), (29, 0.85, 'Ease out'), (36, 1.0, BEZ['back'])])
    cur.shadow(y=-0.003, soft=0.01, op=0.3)


def toast(d):
    n = 120
    k = d.comp("SU Notification toast", n, "tst"); lab_bg(k, n)
    cx, cy, w, h = 960, 136, 580, 124
    card = k.rect("Toast card", cx, cy, w, h, COL['card'], r=22, f0=0, dur=n, center=True)
    card.shadow(y=-0.004, soft=0.02, op=0.25)
    k.ell("Toast icon", cx - w / 2 + 52, cy, 56, 56, COL['accent'], f0=2, dur=n - 2)
    k.text("Toast title", "New signup", cx - w / 2 + 96, cy - 22, 26, COL['ink'], f0=6, dur=n - 6, style='SemiBold')
    k.text("Toast body", "Maya joined the Pro plan  ·  now", cx - w / 2 + 96, cy + 22, 21, COL['muted'], f0=9, dur=n - 9, style='Regular')
    for o, entrance in (("Toast card", "Toast drop - spring"), ("Toast icon", "Toast drop - spring"),
                        ("Toast title", "Card lift"), ("Toast body", "Card lift")):
        k.preset(o, entrance)               # text rises inside the card, never above it
        k.preset(o, "Toast exit up")


def toggle(d):
    n = 48
    k = d.comp("SU Toggle switch", n, "tgl"); lab_bg(k, n)
    cx, cy = 960, 540; u = 2.0              # drawn at 2x a desktop switch so it reads in a full video frame
    half, th, kd = 28 * u, 64 * u, 52 * u   # knob travel / 2, track thickness, knob diameter
    off = k.line("Track off", [(cx - half, cy), (cx + half, cy)], COL['off'], px=th, f0=0, dur=n)
    on = k.line("Track on", [(cx - half, cy), (cx + half, cy)], COL['accent'], px=th, f0=0, dur=n)
    on.op([(14, 0, 'Linear'), (24, 1, 'Ease out')])
    off.op([(14, 1, 'Linear'), (24, 0, 'Ease out')])   # no grey rim around the finished on state
    knob = k.ell("Knob", cx - half, cy, kd, kd, COL['card'], f0=0, dur=n)
    knob.shadow(y=-0.002 * u, soft=0.006 * u, op=0.3)
    knob.pos([(14, (cx - half, cy), 'Linear'), (24, (cx + half, cy), SNAP)])
    knob.scale([(14, [1.0, 1.0], 'Linear'), (18, [1.12, 1.0], 'Ease out'), (26, [1.0, 1.0], 'S-curve')])


def kpi(d):
    n = 90
    k = d.comp("SU KPI tile", n, "kpi"); lab_bg(k, n)
    cx, cy, w, h = 960, 540, 440, 240
    L, T = cx - w / 2 + 32, cy - h / 2
    card = k.rect("KPI card", cx, cy, w, h, COL['card'], r=24, f0=0, dur=n, center=True)
    card.shadow(y=-0.004, soft=0.02, op=0.22)
    k.text("KPI label", "Monthly revenue", L, T + 46, 24, COL['muted'], f0=3, dur=n - 3, style='Medium')
    k.text("KPI value", "$48,200", L, T + 112, 64, COL['ink'], f0=6, dur=n - 6, style='Bold')
    k.text("KPI delta", "+12.4%", cx + w / 2 - 32, T + 46, 28, COL['ok'], f0=26, dur=n - 26, style='SemiBold', align='right')
    k.line("KPI track", [(L, T + 190), (cx + w / 2 - 32, T + 190)], COL['line'], px=10, f0=10, dur=n - 10)
    fil = k.line("KPI fill", [(L, T + 190), (cx + w / 2 - 32, T + 190)], COL['accent'], px=10, f0=10, dur=n - 10)
    fil.trim([(22, 0.0, 'Linear'), (52, 0.72, EXPO)], which='end')
    for o in ("KPI card", "KPI label", "KPI value", "KPI track", "KPI fill", "KPI delta"):
        k.preset(o, "Card lift")


def sidebar(d):
    n = 60
    k = d.comp("SU Sidebar drawer", n, "sbd")
    k.rect("Canvas", 0, 0, 1920, 1080, COL['canvas'], f0=0, dur=n)
    k.rect("Header", 0, 0, 1920, 88, COL['card'], f0=0, dur=n)
    k.text("Header title", "Dashboard", 96, 44, 30, COL['ink'], f0=0, dur=n, style='Bold')
    for i in range(3):
        k.rect(f"Card {i + 1}", 96 + i * 584, 160, 544, 360, COL['card'], r=20, f0=0, dur=n)
    sw = 360; f0, f1 = 6, 28
    scrim = k.rect("Scrim", 0, 0, 1920, 1080, COL['ink'], f0=0, dur=n)
    scrim.op([(f0, 0, 'Linear'), (f1, 0.4, EXPO)])
    side = [k.rect("Sidebar", 0, 0, sw, 1080, COL['side'], f0=0, dur=n),
            k.ell("Brand dot", 66, 64, 36, 36, COL['accent'], f0=0, dur=n)]
    for i in range(4):
        side.append(k.rect(f"Menu {i + 1}", 48, 180 + i * 64, 240 - i * 30, 18, COL['side2'], r=9, f0=0, dur=n))
    for o in side:                         # all parts share one key pair, so the drawer moves as one piece
        bx, by = o.base
        o.pos([(f0, (bx - sw, by), 'Linear'), (f1, (bx, by), EXPO)])


def counter(d):
    """rolling digits behind masks; MEASURED places each column on its glyph in the set number"""
    n = 60
    k = d.comp("SU Counter", n, "cnt"); lab_bg(k, n)
    f0, f1 = 6, 36
    pitch = COUNT_PX * LINE                          # line pitch of a digit column
    M = MEASURED
    for i, ch in enumerate(COUNT):
        right = M['count'][i][0] + M['count'][i][1]                 # ink right edge of the number up to this glyph
        ink_left = right - M['char'][ch][1]                          # where this glyph's ink starts in the set number
        x = ink_left - (M['char'][ch][0] - COUNT_X)                  # the pen origin that puts the ink there
        if not ch.isdigit():
            k.text(f"Static {i}", ch, x, COUNT_Y, COUNT_PX, COL['card'], f0=0, dur=n, style='Bold')
            continue
        seq = "0123456789" * LOOPS[i] + "0123456789"[:int(ch) + 1]
        lines = len(seq); half = (lines - 1) / 2 * pitch
        o = k.text(f"Digit {i}", "\n".join(seq), x, COUNT_Y, COUNT_PX, COL['card'], f0=0, dur=n, style='Bold')
        o.pos([(f0, (x, COUNT_Y + half), 'Linear'), (f1, (x, COUNT_Y - half), EXPO)])
        o.mblur(180)
        win = k.rect(f"Window {i}", x - 8, COUNT_Y - 62, M['char'][ch][1] + 60, 124, COL['card'], f0=0, dur=n)
        k.mask(o, win)
    k.text("Count label", "Revenue this month", COUNT_X, COUNT_Y + 110, 32, COL['muted'], f0=0, dur=n, style='Medium')


def typing(d):
    n = 80
    k = d.comp("SU Search typing", n, "typ"); lab_bg(k, n)
    f0, per = 30, 2
    bx, by, bw, bh = 960, 540, 680, 84
    k.rect("Search bar", bx, by, bw, bh, COL['card'], r=20, f0=0, dur=n, center=True)
    ic = k.ell("Search icon", bx - bw / 2 + 44, by - 4, 26, 26, None, f0=0, dur=n); ic.stroke(COL['muted'], 3.5)
    k.line("Search icon handle", [(bx - bw / 2 + 53, by + 6), (bx - bw / 2 + 61, by + 14)], COL['muted'], px=3.5, f0=0, dur=n)
    tx = TYPE_X
    k.text("Placeholder", "Search customers", tx, by, TYPE_PX, COL['muted'], f0=0, dur=f0, style='Regular')
    t = k.text("Typed", TYPED, tx, by, TYPE_PX, COL['ink'], f0=f0, dur=n - f0, style='Regular')
    t.stagger(by='chars', each=per, keyframes=[(0, {'opacity': 0}, 'Hold'), (1, {'opacity': 1}, None)])
    caret = k.rect("Caret", tx, by, 3, 44, COL['accent'], f0=0, dur=n, center=True)
    ks = [(0, (tx - 6, by), 'Hold')]            # before the placeholder's first letter
    prev = 0
    for i in range(1, len(TYPED) + 1):
        ix, iw = MEASURED['typed'][i - 1]
        wpx = prev + 10 if TYPED[i - 1] == " " else ix + iw - tx
        prev = wpx
        ks.append((f0 + 1 + (i - 1) * per, (tx + wpx + 4, by), 'Hold'))   # character i shows at f0 + 1 + (i-1)*gap
    caret.pos(ks)
    end = f0 + len(TYPED) * per
    blink = [(0, 1, 'Hold')]; t2 = end + 8
    while t2 + 8 < n:
        blink += [(t2, 0, 'Hold'), (t2 + 8, 1, 'Hold')]; t2 += 16
    caret.op(blink)


def build(path=None, m=None):
    d = KDoc()
    cursor_click(d); toast(d); toggle(d); kpi(d); sidebar(d); counter(d); typing(d)
    return d


if __name__ == "__main__":
    print(__doc__)
