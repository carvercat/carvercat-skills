"""SaaS UI round 3 in design units: seven lab comps for briefs the pack could not serve before (pricing plans, browser window that
loads, submit button that turns into a success state, a kanban card dragged between columns, an integrations hub, a camera zoom
into one dashboard card, a review card), written with cc2.py (through dvsu_kit.py).

    import saas_ui_lab3 as L; doc = L.build(); doc.send(client, PROJECT.carverproj)

Same palette and font as saas_ui_lab.py. Every move is baked as keys here (no presets to apply), so the templates need no other
pack. Parented parts use Obj.child (cc2): a child's x, y count from its parent's top-left. Fonts: Rethink Sans must be installed
(KI-136). Docs: ai/patterns/saas-ui.md (round 3). Design units: px from the top-left, y down; frames, 30 fps.
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dvsu_kit import KDoc, css, HOLD
from saas_ui_lab import COL, EXPO, SMOOTH, lab_bg, CURSOR

SPRING = (0.34, 1.36, 0.64, 1)      # one-sided bezier, about 4% overshoot (the pack's small spring)
ACCEL = (0.3, 0.0, 0.8, 0.15)
WHITE = COL['card']
PRICE_W = {"$0": 92.1, "$24": 137.76, "$49": 137.76}   # advance of the price at Rethink Sans Bold 80 px (measure.boxes, 0.1.8.1)


def rig(kids, parent):
    """parent every part of kids to parent (Obj.child)"""
    for o in kids: parent.child(o)


def fade(o, f, d=7, to=1.0):
    return o.op([(f, 0.0, 'Linear'), (f + d, to, 'Ease out')])


def lift(o, f, dy=32, d=18, s0=0.94, scale=True):
    """The pack's Card lift baked as keys: up from dy px below, size s0 -> 1 (expo), opaque in 7 f."""
    bx, by = o.base
    o.pos([(f, (bx, by + dy), 'Linear'), (f + d, (bx, by), EXPO)])
    if scale:
        o.scale([(f, s0, 'Linear'), (f + d, 1.0, EXPO)])
    return fade(o, f)


def pop(o, f, d=12, s0=0.0):
    o.scale([(f, s0, 'Linear'), (f + d, 1.0, SPRING)])
    return o.op([(f, 0.0, 'Linear'), (f + 3, 1.0, 'Linear')])


def check(k, name, x, y, s, col, px, f0, dur):
    """a tick: short leg down-right, long leg up-right; (x, y) is the corner"""
    return k.line(name, [(x - 0.55 * s, y - 0.5 * s), (x, y), (x + s, y - 1.05 * s)], col, px=px, f0=f0, dur=dur)


# ---------------------------------------------------------------- 1. pricing plans
PLANS = [("Starter", "$0", ["1 project", "Basic reports", "Email support"], "Start free"),
         ("Pro", "$24", ["Unlimited projects", "Advanced reports", "Priority support"], "Choose Pro"),
         ("Business", "$49", ["Everything in Pro", "SSO and audit log", "Dedicated manager"], "Talk to sales")]


def pricing(d):
    n = 150
    k = d.comp("SU Pricing plans", n, "spp"); lab_bg(k, n)
    W_, H_, cy = 400, 500, 580
    top = cy - H_ / 2
    cards = {}
    # built 1, 3, 2: the featured card (parent of the badge) comes last, so the badge is the top layer as in v1 and the scene's
    # layer order equals its id order (measure.boxes pairs ids and names by position)
    for i, (name, price, feats, cta) in sorted(enumerate(PLANS), key=lambda p: (p[0] == 1, p[0])):
        cx = 500 + i * 460; L = cx - W_ / 2 + 40; f = i * 4
        hot = i == 1
        ink, sub = (WHITE, css('DCDDFE')) if hot else (COL['ink'], COL['muted'])
        card = k.rect(f"Card {i + 1}", cx, cy, W_, H_, COL['accent'] if hot else WHITE, r=28, f0=f, dur=n - f, center=True)
        card.shadow(y=-0.004, soft=0.02, op=0.25)
        kids = []
        t = k.text(f"Plan {i + 1}", name, L, top + 60, 32, ink, f0=f + 3, dur=n - f - 3, style='Bold'); kids.append(t)
        t = k.text(f"Price {i + 1}", price, L, top + 146, 80, ink, f0=f + 5, dur=n - f - 5, style='Bold'); kids.append(t)
        t = k.text(f"Per month {i + 1}", "/mo", L + PRICE_W[price] + 12, top + 162, 28, sub, f0=f + 5, dur=n - f - 5,
                   style='Medium'); kids.append(t)
        rule = k.line(f"Rule {i + 1}", [(L, top + 222), (cx + W_ / 2 - 40, top + 222)], css('7C7CF8') if hot else COL['line'],
                      px=2, f0=f + 6, dur=n - f - 6); kids.append(rule)
        for j, ft in enumerate(feats):
            y = top + 272 + j * 48; g = f + 8 + j * 2
            kids.append(check(k, f"Tick {i + 1}.{j + 1}", L + 8, y + 6, 12, WHITE if hot else COL['accent'], 3.5, g, n - g))
            kids.append(k.text(f"Feature {i + 1}.{j + 1}", ft, L + 36, y, 24, ink, f0=g, dur=n - g, style='Medium'))
        b = k.rect(f"Button {i + 1}", cx, top + 436, W_ - 80, 64, WHITE if hot else css('EEF0FE'), r=32, f0=f + 12, dur=n - f - 12,
                   center=True); kids.append(b)
        kids.append(k.text(f"Button label {i + 1}", cta, cx, top + 436, 28, COL['accent'], f0=f + 12, dur=n - f - 12, style='Bold',
                           align='center'))
        rig(kids, card)
        for o in kids:                                      # content follows the card: fade + a short rise inside it
            lift(o, o.f0, dy=12, d=14, scale=False)
        lift(card, f, dy=32, d=18)
        cards[i] = (card, kids)
    # the featured plan steps forward at f40, the others step back; the badge pops on top
    hot = cards[1][0]; bx, by = hot.base
    hot.pos([(4, (bx, by + 32), 'Linear'), (22, (bx, by), EXPO), (40, (bx, by), 'Linear'), (56, (bx, by - 24), SPRING)])
    hot.scale([(4, 0.94, 'Linear'), (22, 1.0, EXPO), (40, 1.0, 'Linear'), (56, 1.06, SPRING)])
    for i in (0, 2):
        c = cards[i][0]; f = i * 4
        c.scale([(f, 0.94, 'Linear'), (f + 18, 1.0, EXPO), (40, 1.0, 'Linear'), (56, 0.97, EXPO)])
    badge = k.rect("Badge", 960, top, 230, 48, css('FFB020'), r=22, f0=50, dur=n - 50, center=True)
    lab = k.text("Badge label", "MOST POPULAR", 960, top, 24, COL['ink'], f0=52, dur=n - 52, style='Bold', align='center', width=230)
    rig([badge, lab], hot)
    pop(badge, 50, 12); fade(lab, 52, 5)


# ---------------------------------------------------------------- 2. browser window that loads
def browser(d):
    n = 150
    k = d.comp("SU Browser load", n, "sbw"); lab_bg(k, n)
    cx, cy, w, h = 960, 560, 1280, 760
    top, left = cy - h / 2, cx - w / 2
    frame = [k.rect("Window", cx, cy, w, h, COL['line'], r=20, f0=0, dur=n, center=True)]
    frame[0].shadow(y=-0.006, soft=0.03, op=0.35)
    frame.append(k.rect("Page", cx, top + 56 + (h - 56) / 2, w, h - 56, WHITE, r=20, f0=0, dur=n, center=True))
    frame.append(k.rect("Page top", cx, top + 56 + 20, w, 40, WHITE, f0=0, dur=n, center=True))   # squares the page's top corners
    for i, c in enumerate(('FF5F57', 'FEBC2E', '28C840')):
        frame.append(k.ell(f"Dot {i + 1}", left + 32 + i * 24, top + 28, 14, 14, css(c), f0=0, dur=n))
    frame.append(k.rect("Address bar", cx, top + 28, 520, 32, WHITE, r=16, f0=0, dur=n, center=True))
    frame.append(k.text("Address", "acme.app/dashboard", cx, top + 28, 20, COL['muted'], f0=0, dur=n, style='Medium', align='center'))
    win = frame[0]
    rig(frame[1:], win)
    win.pos([(0, (cx, cy + 60), 'Linear'), (24, (cx, cy), EXPO)])
    win.scale([(0, 0.96, 'Linear'), (24, 1.0, EXPO)])
    for o in frame:
        fade(o, 0, 8)
    # skeleton (pulses while "loading"), then the real content
    L = left + 60
    skel = [("Sk title", L + 170, top + 120, 340, 30)]
    for i in range(3):
        x = L + 180 + i * 400
        skel += [(f"Sk label {i + 1}", x - 70, top + 220, 140, 16), (f"Sk value {i + 1}", x - 40, top + 262, 200, 32)]
    for j in range(3):
        skel.append((f"Sk line {j + 1}", L + 580 - j * 120, top + 450 + j * 70, 1160 - j * 240, 22))
    tiles = []
    for i in range(3):
        x = L + 180 + i * 400
        tiles.append(k.rect(f"KPI tile {i + 1}", x, top + 240, 360, 140, COL['canvas'], r=16, f0=10, dur=n - 10, center=True))
    tiles.append(k.rect("Chart panel", cx, top + 520, 1160, 300, COL['canvas'], r=16, f0=10, dur=n - 10, center=True))
    for o in tiles:
        fade(o, 10, 6)
    pulse = [(10, 0.0, 'Linear'), (14, 1.0, 'Ease out'), (26, 0.45, 'S-curve'), (38, 1.0, 'S-curve'), (50, 0.45, 'S-curve'),
             (62, 1.0, 'S-curve'), (70, 0.0, ACCEL)]
    for name, x, y, ww, hh in skel:
        k.rect(name, x, y, ww, hh, COL['line'], r=hh / 2, f0=10, dur=60, center=True).op(pulse)
    t = k.text("Greeting", "Good morning, Priya", L, top + 120, 36, COL['ink'], f0=64, dur=n - 64, style='Bold')
    lift(t, 64, dy=16, d=16)
    for i, (lab, val) in enumerate((("Revenue", "$48.2k"), ("Active users", "12,480"), ("Churn", "1.9%"))):
        x = L + 40 + i * 400; f = 68 + i * 3
        lift(k.text(f"KPI label {i + 1}", lab, x, top + 210, 26, COL['muted'], f0=f, dur=n - f, style='Medium'), f, dy=12, d=14, scale=False)
        lift(k.text(f"KPI value {i + 1}", val, x, top + 262, 44, COL['ink'], f0=f + 2, dur=n - f - 2, style='Bold'), f + 2, dy=12, d=14,
             scale=False)
    vals = [32, 45, 40, 58, 52, 66, 61, 74, 70, 84, 79, 92]
    for i, v in enumerate(vals):
        hh = 220 * v / 100; x = left + 140 + i * 92; f = 78 + i * 2
        b = k.rect(f"Bar {i + 1}", x, top + 640 - hh / 2, 52, hh, COL['accent'] if i == len(vals) - 1 else css('C9CCF9'), r=10,
                   f0=f, dur=n - f, center=True)
        b.anchor(0, -1)                                    # grows from its baseline
        b.scale([(f, [1.0, 0.0], 'Linear'), (f + 14, [1.0, 1.0], SPRING)])


# ---------------------------------------------------------------- 3. submit -> spinner -> success
def submit(d):
    n = 150
    k = d.comp("SU Submit success", n, "sss"); lab_bg(k, n)
    cx, cy, half, th = 960, 470, 180, 112
    btn = k.line("Button", [(cx - half, cy), (cx + half, cy)], COL['accent'], px=th, f0=0, dur=n)   # round caps: a true pill
    lift(btn, 0, dy=24)
    btn.trim([(32, 0.0, 'Linear'), (44, 0.4995, SMOOTH)], which='start')   # both ends close in: pill -> circle
    btn.trim([(32, 1.0, 'Linear'), (44, 0.5005, SMOOTH)], which='end')
    btn.addkeys('scale', [(24, 1.0, 'Linear'), (27, 0.95, 'Ease out'), (33, 1.0, SPRING)])      # the press, after the lift's keys
    lab = k.text("Button label", "Create account", cx, cy, 40, WHITE, f0=2, dur=34, style='Bold', align='center')
    lab.op([(2, 0.0, 'Linear'), (9, 1.0, 'Ease out'), (30, 1.0, 'Linear'), (34, 0.0, ACCEL)])
    sp = k.ell("Spinner", cx, cy, 60, 60, None, f0=42, dur=38); sp.stroke(WHITE, 7)
    sp.trim_static('end', 0.28)
    sp.rot([(42, 0.0, 'Linear'), (60, 360.0, HOLD), (61, 0.0, 'Linear'), (80, 360.0, 'Linear')])   # two clockwise turns (the app keeps an angle within 360, so the second turn restarts at the same picture)
    sp.op([(42, 0.0, 'Linear'), (46, 1.0, 'Ease out'), (74, 1.0, 'Linear'), (78, 0.0, ACCEL)])
    ok = k.ell("Success", cx, cy, th, th, COL['ok'], f0=76, dur=n - 76)
    pop(ok, 76, 12, s0=0.6)
    ring = k.ell("Success ring", cx, cy, th, th, None, f0=78, dur=20); ring.stroke(COL['ok'], 6)
    ring.scale([(78, 1.0, 'Linear'), (98, 1.7, EXPO)]); ring.op([(78, 0.7, 'Linear'), (96, 0.0, 'Ease out')])
    tick = check(k, "Tick", cx - 8, cy + 18, 30, WHITE, 9, 80, n - 80)
    tick.trim([(80, 0.0, 'Linear'), (92, 1.0, EXPO)], which='end')
    lift(k.text("Done title", "Account created", cx, cy + 140, 52, WHITE, f0=86, dur=n - 86, style='Bold', align='center'), 86, dy=16, d=16)
    lift(k.text("Done body", "Check your inbox to get started.", cx, cy + 206, 32, css('A3A7C2'), f0=92, dur=n - 92, style='Medium',
                align='center'), 92, dy=12, d=16, scale=False)


# ---------------------------------------------------------------- 4. kanban card dragged across columns
def kanban(d):
    n = 150
    k = d.comp("SU Kanban drag", n, "skd"); lab_bg(k, n)
    colx, cw, ch, ccy = (480, 960, 1440), 440, 520, 520
    ctop = ccy - ch / 2
    row = (ctop + 140, ctop + 270)
    for i, (x, name) in enumerate(zip(colx, ("To do", "In progress", "Done"))):
        c = k.rect(f"Column {i + 1}", x, ccy, cw, ch, css('1C1F3A'), r=24, f0=i * 3, dur=n - i * 3, center=True)
        lift(c, i * 3, dy=24)
        lift(k.text(f"Column title {i + 1}", name, x - cw / 2 + 32, ctop + 48, 28, WHITE, f0=i * 3 + 3, dur=n - i * 3 - 3, style='Bold'),
             i * 3 + 3, dy=12, d=14, scale=False)

    def card(name, title, tag, x, y, f):
        c = k.rect(name, x, y, 376, 110, WHITE, r=16, f0=f, dur=n - f, center=True)
        c.shadow(y=-0.003, soft=0.012, op=0.2)
        t = k.text(name + " title", title, x - 164, y - 16, 26, COL['ink'], f0=f, dur=n - f, style='Medium')
        g = k.rect(name + " tag", x - 128, y + 28, 72, 14, css(tag), r=7, f0=f, dur=n - f, center=True)
        rig([t, g], c)
        for o in (t, g):
            fade(o, f + 3, 6)
        lift(c, f, dy=24)
        return c
    # made bottom to top: the dragged card A must be drawn above the other cards, the slot and the columns
    B = card("Card B", "Write release notes", 'F59E0B', 480, row[1], 11)
    card("Card C", "Migrate billing", '10B981', 960, row[0], 14)
    card("Card D", "Fix login bug", 'EC4899', 1440, row[0], 17)
    slot = k.rect("Drop slot", 1440, row[1], 376, 110, None, r=16, f0=50, dur=40, center=True)
    slot.stroke(css('8B8FC7'), 3, cap='round'); slot.set('strokeDasharray', '14 10')
    slot.op([(50, 0.0, 'Linear'), (58, 1.0, 'Ease out'), (84, 1.0, 'Linear'), (89, 0.0, ACCEL)])
    A = card("Card A", "Ship pricing page", '5B5BF6', 480, row[0], 8)
    # drag: grab f42-48, carry f48-84 (smooth), drop f84-96 (small spring); the next card closes the gap
    ax, ay = A.base
    tx, ty = 1440, row[1]
    A.addkeys('pos', [(42, (ax, ay), 'Linear'), (48, (ax, ay - 8), 'Ease out'), (84, (tx, ty - 8), SMOOTH), (96, (tx, ty), SPRING)])
    A.addkeys('scale', [(42, 1.0, 'Linear'), (48, 1.04, 'Ease out'), (84, 1.04, 'Linear'), (96, 1.0, SPRING)])
    A.rot([(42, 0.0, 'Linear'), (48, 3.0, 'Ease out'), (84, 3.0, 'Linear'), (96, 0.0, SPRING)])    # a 3 degree clockwise tilt while carried
    bx, by = B.base
    B.addkeys('pos', [(88, (bx, by), 'Linear'), (102, (bx, row[0]), EXPO)])
    s = 2.0; tip = (480 + 110, row[0] + 12)
    pts = [(tip[0] + x * s, tip[1] + y * s) for x, y in CURSOR]
    cur = k.poly("Cursor", pts, f0=24, dur=n - 24); cur.fill(WHITE); cur.stroke(COL['ink'], 2.5)
    cur.shadow(y=-0.003, soft=0.01, op=0.3)
    cx0, cy0 = cur.base
    dx, dy = tx - ax, ty - ay
    cur.pos([(24, (cx0 + 260, cy0 + 300), 'Linear'), (40, (cx0, cy0), SMOOTH), (48, (cx0, cy0 - 8), 'Ease out'),
             (84, (cx0 + dx, cy0 + dy - 8), SMOOTH), (96, (cx0 + dx, cy0 + dy), SPRING),
             (102, (cx0 + dx, cy0 + dy), 'Linear'), (120, (cx0 + dx + 200, cy0 + dy + 160), SMOOTH)])
    cur.op([(24, 0.0, 'Linear'), (29, 1.0, 'Ease out'), (112, 1.0, 'Linear'), (120, 0.0, ACCEL)])
    cur.anchor(-1, 1)                                       # pivot at the tip
    cur.scale([(42, 1.0, 'Linear'), (45, 0.85, 'Ease out'), (84, 0.85, 'Linear'), (90, 1.0, SPRING)])


# ---------------------------------------------------------------- 5. integrations hub
ICONS = [('ell', 'F59E0B'), ('dia', 'EF4444'), ('star', '10B981'), ('sq', '3B82F6'), ('hex', '8B5CF6'), ('ring', 'EC4899')]


def integrations(d):
    n = 150
    k = d.comp("SU Integrations hub", n, "sih"); lab_bg(k, n)
    hx, hy, rx, ry = 960, 450, 380, 270
    spots = [(hx + rx * math.cos(math.radians(a)), hy + ry * math.sin(math.radians(a))) for a in (-90, -30, 30, 90, 150, 210)]
    order = [0, 1, 2, 3, 4, 5]
    for i, (x, y) in enumerate(spots):                          # lines first: they sit under the tiles and the hub
        f = 12 + i * 3
        ln = k.line(f"Link {i + 1}", [(hx, hy), (x, y)], css('3A3E66'), px=4, f0=f, dur=n - f)
        ln.trim([(f, 0.0, 'Linear'), (f + 14, 1.0, EXPO)], which='end')
    for i, (x, y) in enumerate(spots):                          # a data pulse runs out along each link, twice
        for rep, base in enumerate((54, 98)):
            f = base + i * 4
            p = k.ell(f"Pulse {i + 1}.{rep + 1}", hx, hy, 18, 18, css('B07CFF'), f0=f, dur=22)
            p.pos([(f, (hx, hy), 'Linear'), (f + 20, (x, y), SMOOTH)])
            p.op([(f, 0.0, 'Linear'), (f + 4, 1.0, 'Linear'), (f + 15, 1.0, 'Linear'), (f + 20, 0.0, 'Ease out')])
    hub = k.rect("Hub", hx, hy, 180, 180, COL['accent'], r=44, f0=0, dur=n, center=True)
    hub.shadow(y=-0.004, soft=0.02, op=0.3)
    mark = k.text("Hub mark", "A", hx, hy, 104, WHITE, f0=0, dur=n, style='Bold', align='center')
    rig([mark], hub); pop(hub, 0, 14); fade(mark, 2, 5)
    for i in order:
        x, y = spots[i]; f = 20 + i * 3; kind, c = ICONS[i]
        t = k.rect(f"Tile {i + 1}", x, y, 120, 120, WHITE, r=28, f0=f, dur=n - f, center=True)
        t.shadow(y=-0.003, soft=0.015, op=0.25)
        if kind == 'ell':
            ic = k.ell(f"Icon {i + 1}", x, y, 56, 56, css(c), f0=f, dur=n - f)
        elif kind == 'dia':
            ic = k.rect(f"Icon {i + 1}", x, y, 46, 46, css(c), r=8, f0=f, dur=n - f, center=True); ic.rotv(-45.0)
        elif kind == 'star':
            ic = k.star(f"Icon {i + 1}", x, y, 66, 5, 0.45, css(c), f0=f, dur=n - f)
        elif kind == 'sq':
            ic = k.rect(f"Icon {i + 1}", x, y, 52, 52, css(c), r=12, f0=f, dur=n - f, center=True)
        elif kind == 'hex':
            ic = k.ngon(f"Icon {i + 1}", x, y, 62, 6, css(c), f0=f, dur=n - f)
        else:
            ic = k.ell(f"Icon {i + 1}", x, y, 50, 50, None, f0=f, dur=n - f); ic.stroke(css(c), 10)
        rig([ic], t); pop(t, f, 12)
    lift(k.text("Headline", "Connects to the tools you already use", hx, 880, 44, WHITE, f0=36, dur=n - 36, style='Bold', align='center'),
         36, dy=16, d=16)


# ---------------------------------------------------------------- 6. camera zoom into one dashboard card
def zoom(d):
    n = 150
    k = d.comp("SU Zoom focus", n, "szf")
    world = k.rect("App canvas", 960, 540, 1920, 1080, COL['canvas'], f0=0, dur=n, center=True)   # the camera: everything rides on it
    kids = [k.rect("Sidebar", 140, 540, 280, 1080, COL['side'], f0=0, dur=n, center=True),
            k.ell("Brand dot", 70, 60, 36, 36, COL['accent'], f0=0, dur=n)]
    for i in range(5):
        kids.append(k.rect(f"Menu {i + 1}", 48 + (200 - i * 24) / 2, 180 + i * 64, 200 - i * 24, 18,
                           COL['accent'] if i == 1 else COL['side2'], r=9, f0=0, dur=n, center=True))
    kids.append(k.rect("Header", 1100, 44, 1640, 88, WHITE, f0=0, dur=n, center=True))
    kids.append(k.text("Header title", "Analytics", 340, 44, 30, COL['ink'], f0=0, dur=n, style='Bold'))
    for i, (lab, val) in enumerate((("Revenue", "$48.2k"), ("Active users", "12,480"), ("Open tickets", "32"))):
        x = 580 + i * 520
        kids.append(k.rect(f"Tile {i + 1}", x, 250, 480, 200, WHITE, r=20, f0=0, dur=n, center=True))
        kids.append(k.text(f"Tile label {i + 1}", lab, x - 208, 203, 26, COL['muted'], f0=0, dur=n, style='Medium'))
        kids.append(k.text(f"Tile value {i + 1}", val, x - 208, 275, 56, COL['ink'], f0=0, dur=n, style='Bold'))
    kids.append(k.rect("Chart", 1370, 650, 980, 520, WHITE, r=20, f0=0, dur=n, center=True))
    kids.append(k.text("Chart title", "Signups per week", 920, 430, 26, COL['ink'], f0=0, dur=n, style='Bold'))
    for i, v in enumerate([40, 52, 47, 63, 58, 71, 69, 84]):
        hh = 300 * v / 100; x = 960 + i * 112
        kids.append(k.rect(f"Bar {i + 1}", x, 860 - hh / 2, 64, hh, css('C9CCF9'), r=10, f0=0, dur=n, center=True))
    T = (590, 650)       # the card the camera visits; keep it 565..1355 x, 318..762 y so a 1.76x frame never leaves the app
    kids.append(k.rect("Focus card", T[0], T[1], 500, 520, WHITE, r=20, f0=0, dur=n, center=True))
    kids.append(k.text("Focus label", "Conversion rate", T[0] - 210, T[1] - 170, 26, COL['muted'], f0=0, dur=n, style='Medium'))
    kids.append(k.text("Focus value", "4.8%", T[0] - 214, T[1] - 70, 112, COL['ink'], f0=0, dur=n, style='Bold'))
    kids.append(k.text("Focus delta", "+0.9 pts this week", T[0] - 210, T[1] + 40, 26, COL['ok'], f0=0, dur=n, style='SemiBold'))
    kids.append(k.line("Focus track", [(T[0] - 210, T[1] + 140), (T[0] + 210, T[1] + 140)], COL['line'], px=12, f0=0, dur=n))
    fill = k.line("Focus fill", [(T[0] - 210, T[1] + 140), (T[0] + 210, T[1] + 140)], COL['accent'], px=12, f0=0, dur=n)
    fill.trim([(0, 0.3, 'Linear'), (56, 0.3, 'Linear'), (80, 0.62, EXPO)], which='end'); kids.append(fill)
    ring = k.rect("Focus ring", T[0], T[1], 520, 540, None, r=28, f0=48, dur=58, center=True); ring.stroke(COL['accent'], 4)
    ring.op([(48, 0.0, 'Linear'), (56, 1.0, 'Ease out'), (98, 1.0, 'Linear'), (104, 0.0, ACCEL)]); kids.append(ring)
    rig(kids, world)
    C = (960, 540)
    def at(z): return (C[0] - z * (T[0] - C[0]), C[1] - z * (T[1] - C[1]))   # parent position that puts T on the frame centre
    z1, z2 = 1.7, 1.76                                       # in, then a slow push through the hold so it never freezes
    rest = C                                             # at rest the camera is the identity (not at(1.0))
    world.pos([(20, rest, 'Linear'), (46, at(z1), SMOOTH), (104, at(z2), 'Linear'), (128, rest, SMOOTH)])
    world.scale([(20, 1.0, 'Linear'), (46, z1, SMOOTH), (104, z2, 'Linear'), (128, 1.0, SMOOTH)])


# ---------------------------------------------------------------- 7. review card
def review(d):
    n = 150
    k = d.comp("SU Review card", n, "srv"); lab_bg(k, n)
    cx, cy, w, h = 960, 540, 1000, 460
    L, top = cx - w / 2 + 64, cy - h / 2
    card = k.rect("Review card", cx, cy, w, h, WHITE, r=28, f0=0, dur=n, center=True)
    card.shadow(y=-0.004, soft=0.02, op=0.22)
    lift(card, 0)
    for i in range(5):
        f = 10 + i * 3
        pop(k.star(f"Star {i + 1}", L + 24 + i * 60, top + 84, 52, 5, 0.45, css('F5B301'), f0=f, dur=n - f), f, 12)
    for j, line in enumerate(("Setup took ten minutes.", "We never looked back.")):
        f = 24 + j * 4
        lift(k.text(f"Quote {j + 1}", line, L, top + 182 + j * 68, 52, COL['ink'], f0=f, dur=n - f, style='Bold'), f, dy=16, d=16,
             scale=False)
    av = k.ell("Avatar", L + 40, top + 366, 80, 80, css('C9CCF9'), f0=34, dur=n - 34)
    ini = k.text("Initials", "DR", L + 40, top + 366, 36, COL['accent'], f0=34, dur=n - 34, style='Bold', align='center')
    rig([ini], av); pop(av, 34, 12); fade(ini, 36, 5)
    lift(k.text("Name", "Dana Ruiz", L + 104, top + 346, 32, COL['ink'], f0=38, dur=n - 38, style='Bold'), 38, dy=12, d=14, scale=False)
    lift(k.text("Role", "Ops lead, Northwind", L + 104, top + 388, 26, COL['muted'], f0=41, dur=n - 41, style='Medium'), 41, dy=12, d=14,
         scale=False)


def build(path=None, m=None):
    d = KDoc()
    pricing(d); browser(d); submit(d); kanban(d); integrations(d); zoom(d); review(d)
    return d


if __name__ == "__main__":
    print(__doc__)
