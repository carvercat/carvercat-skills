"""Corporate Brand round 3: eight lab comps for briefs the pack could not serve before (org chart,
values grid, anniversary card, office location card, award badge, partner logo wall, careers card,
safety notice), written straight into a .carverproj.

    import corporate_brand_lab3 as L; presets, masks = L.build(PROJECT.carverproj)

Same palette, font and style rules as corporate_brand_lab.py: standard and decelerate curves only,
no springs, 0% overshoot, one accent (teal). The safety notice adds signal amber, the convention for
warning signs, and uses it only there. Unlike rounds 1 and 2, every move is baked as keys (no presets
to apply): soft_rise() and card_settle() below write the keys of the pack's Soft rise and Card settle
presets. After writing: edit.open {path, force:true}; edit.save. Check with carvercat_inspect and
carvercat_look; extract templates with comp_to_template.py (--drop "Lab bg").
Names, places and logos are stand-ins (invented); replace them before delivery.
Fonts: Rethink Sans must be installed (KI-136). Docs: ai/patterns/corporate-brand.md (round 3).
Pixel space 1920x1080, y down; comp frames, 30 fps.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corporate_brand_lab import Doc, lin, COL, EXPO, DECEL, lab_bg
from cc import BEZ

STD = BEZ['std']
AMBER = lin('F2A900')
CARD = lin('FFFFFF')                       # cards on the light background
PRESETS, MASKS = [], []


def soft_rise(o, f, d=24, dy=16):
    """the pack's Soft rise as keys: 16 px (1.5% H) up into place, standard curve; opaque by 60% of the move"""
    bx, by = o.base
    o.pos([(f, [bx, by - dy / 1080], 'Linear'), (f + d, [bx, by], STD)])
    o.op([(f, 0.0, 'Linear'), (f + round(d * 0.6), 1.0, 'Ease out')])
    return o


def card_settle(o, f, d=20, dy=22, s0=0.97):
    """the pack's Card settle as keys: 22 px (2% H) up and size 0.97 -> 1, strong decelerate; opaque by half-way"""
    bx, by = o.base
    o.pos([(f, [bx, by - dy / 1080], 'Linear'), (f + d, [bx, by], DECEL)])
    o.scale([(f, s0, 'Linear'), (f + d, 1.0, DECEL)])
    o.op([(f, 0.0, 'Linear'), (f + d // 2, 1.0, 'Ease out')])
    return o


def draw(o, f, d=16, ease=DECEL):
    o.trim([(f, 0.0, 'Linear'), (f + d, 1.0, ease)]); return o


def grow_x(o, f, d=16):
    o.anchor(-1, 0); o.scale([(f, [0.0, 1.0], 'Linear'), (f + d, [1.0, 1.0], DECEL)]); return o


def ring(k, name, x, y, dia, col, px, f, d=30):
    """a stroked circle drawn clockwise from 12 o'clock (ellipse paths start at 3 o'clock, CCW: rotate +90, trim the start 1 -> 0)"""
    o = k.ell(name, x, y, dia, dia, None, f0=f, dur=k.length - f); o.stroke(col, px)
    o.rotv(90)
    tp = o.trim([(f, 1.0, 'Linear'), (f + d, 0.0, DECEL)], which='start'); o.set(tp + '.end', 1.0)
    return o


# ---------------------------------------------------------------- 1. org chart
ORG_TOP = ("Amara Mensah", "Chief Executive")
ORG_REPORTS = [("Lee Varga", "Chief Technology Officer"), ("Dana Okafor", "Chief Operating Officer"),
               ("Sam Ruiz", "Chief Financial Officer")]


def org_chart(d):
    n = 150
    k = d.comp("CB Org chart", n, "cog"); lab_bg(k, n)
    soft_rise(k.text("Title", "Leadership team", 240, 170, 56, COL['white'], f0=0, dur=n, style='SemiBold'), 0)
    soft_rise(k.text("Subtitle", "From 1 March 2027", 240, 234, 30, COL['grey'], f0=4, dur=n - 4, style='Regular'), 4)
    xs, ty, cy, cw, ch, bus = [440, 960, 1480], 380, 690, 440, 150, 540
    # connectors first (under the cards): stem down, the bus out both ways from the centre, three drops
    draw(k.line("Stem", [(960, ty + ch / 2), (960, bus)], COL['grey'], px=3, f0=16, dur=n - 16), 16, 10)
    draw(k.line("Bus left", [(960, bus), (xs[0], bus)], COL['grey'], px=3, f0=24, dur=n - 24), 24, 16)
    draw(k.line("Bus right", [(960, bus), (xs[2], bus)], COL['grey'], px=3, f0=24, dur=n - 24), 24, 16)
    for i, x in enumerate(xs):
        f = 36 if i != 1 else 26
        draw(k.line(f"Drop {i + 1}", [(x, bus), (x, cy - ch / 2)], COL['grey'], px=3, f0=f, dur=n - f), f, 10)
    top = k.rect("Top card", 960, ty, cw, ch, COL['navy2'], r=12, f0=4, dur=n - 4, center=True); top.stroke(COL['teal'], 3)
    card_settle(top, 4)
    soft_rise(k.text("Top name", ORG_TOP[0], 960, ty - 26, 38, COL['white'], f0=8, dur=n - 8, style='SemiBold', align='center'), 8)
    soft_rise(k.text("Top role", ORG_TOP[1], 960, ty + 32, 28, COL['teal'], f0=12, dur=n - 12, style='Medium', align='center'), 12)
    for i, ((name, role), x) in enumerate(zip(ORG_REPORTS, xs)):
        f = 42 + i * 6
        card_settle(k.rect(f"Card {i + 1}", x, cy, cw, ch, COL['navy2'], r=12, f0=f, dur=n - f, center=True), f)
        soft_rise(k.text(f"Name {i + 1}", name, x, cy - 26, 36, COL['white'], f0=f + 4, dur=n - f - 4, style='SemiBold', align='center'), f + 4)
        soft_rise(k.text(f"Role {i + 1}", role, x, cy + 32, 28, COL['grey'], f0=f + 8, dur=n - f - 8, style='Regular', align='center'), f + 8)


# ---------------------------------------------------------------- 2. values grid
VALUES = [("Clients first", "Start with the people we serve."), ("Own the outcome", "Finish what we start."),
          ("Speak plainly", "Clear words, no jargon."), ("Build to last", "Make things that keep working.")]


def values_grid(d):
    n = 150
    k = d.comp("CB Values grid", n, "cvg"); lab_bg(k, n); k.rect("Light background", 0, 0, 1920, 1080, COL['light'], f0=0, dur=n)
    soft_rise(k.text("Title", "What we stand for", 240, 190, 56, COL['ink'], f0=0, dur=n, style='SemiBold'), 0)
    cw, ch = 680, 250
    for i, (title, line) in enumerate(VALUES):
        r, c = divmod(i, 2)
        cx, cy = 600 + c * 720, 470 + r * 290
        l, t = cx - cw / 2, cy - ch / 2
        f = 8 + i * 6                                                    # reading order: left to right, then down
        card_settle(k.rect(f"Card {i + 1}", cx, cy, cw, ch, CARD, r=16, f0=f, dur=n - f, center=True), f)
        grow_x(k.rect(f"Rule {i + 1}", l + 48, t + 40, 56, 5, COL['teal'], f0=f + 6, dur=n - f - 6), f + 6)
        soft_rise(k.text(f"Number {i + 1}", f"0{i + 1}", l + 128, t + 43, 28, COL['teal'], f0=f + 6, dur=n - f - 6, style='SemiBold'), f + 6)
        soft_rise(k.text(f"Value {i + 1}", title, l + 48, t + 118, 44, COL['ink'], f0=f + 8, dur=n - f - 8, style='SemiBold'), f + 8)
        soft_rise(k.text(f"Line {i + 1}", line, l + 48, t + 184, 30, COL['grey'], f0=f + 12, dur=n - f - 12, style='Regular'), f + 12)


# ---------------------------------------------------------------- 3. anniversary card
def anniversary(d):
    n = 120
    k = d.comp("CB Anniversary", n, "can"); lab_bg(k, n)
    cx, cy = 960, 400
    soft_rise(k.text("Kicker", "CELEBRATING", cx, 150, 30, COL['teal'], f0=0, dur=n, style='SemiBold', align='center', track=1.3), 0)
    ring(k, "Ring", cx, cy, 380, COL['teal'], 4, 2, 32)
    card_settle(k.text("Number", "25", cx, cy, 200, COL['white'], f0=8, dur=n - 8, style='SemiBold', align='center'), 8, d=24)
    soft_rise(k.text("Years", "years of Northwind", cx, 680, 52, COL['white'], f0=18, dur=n - 18, style='SemiBold', align='center'), 18)
    soft_rise(k.text("From", "2002", cx - 110, 770, 34, COL['grey'], f0=26, dur=n - 26, style='Medium', align='right'), 26)
    draw(k.line("Span", [(cx - 80, 770), (cx + 80, 770)], COL['teal'], px=3, f0=30, dur=n - 30), 30, 18)
    soft_rise(k.text("To", "2027", cx + 110, 770, 34, COL['teal'], f0=40, dur=n - 40, style='SemiBold'), 40)
    soft_rise(k.text("Thanks", "Thank you for every year.", cx, 860, 30, COL['grey'], f0=46, dur=n - 46, style='Regular', align='center'), 46)


# ---------------------------------------------------------------- 4. office location card
def office(d):
    n = 150
    k = d.comp("CB Office card", n, "cof"); lab_bg(k, n); k.rect("Light background", 0, 0, 1920, 1080, COL['light'], f0=0, dur=n)
    # map stand-in: a pale panel with a few streets (replace with a map still or footage)
    soft = lambda o, f: o.op([(f, 0.0, 'Linear'), (f + 16, 1.0, 'Ease out')])
    soft(k.rect("Map panel", 480, 540, 960, 1080, lin('DCE2EA'), f0=0, dur=n, center=True), 0)
    streets = [[(0, 300), (960, 420)], [(0, 760), (960, 640)], [(260, 0), (380, 1080)], [(700, 0), (620, 1080)],
               [(0, 980), (520, 1080)], [(380, 520), (960, 180)]]
    for i, pts in enumerate(streets):
        soft(k.line(f"Street {i + 1}", pts, COL['white'], px=18, f0=0, dur=n), 2 + i * 2)
    px, py = 540, 520
    pulse = k.ell("Pin pulse", px, py, 64, 64, None, f0=34, dur=n - 34); pulse.stroke(COL['teal'], 3)
    pulse.scale([(34, 1.0, 'Linear'), (64, 2.2, DECEL)]); pulse.op([(34, 0.0, 'Linear'), (36, 0.9, 'Linear'), (64, 0.0, 'Ease out')])
    card_settle(k.ell("Pin", px, py, 64, 64, COL['teal'], f0=18, dur=n - 18), 18)
    card_settle(k.ell("Pin dot", px, py, 22, 22, COL['white'], f0=22, dur=n - 22), 22, d=16)
    x0 = 1080
    soft_rise(k.text("Kicker", "NEW OFFICE", x0, 330, 28, COL['teal'], f0=10, dur=n - 10, style='SemiBold', track=1.3), 10)
    soft_rise(k.text("City", "Lisbon", x0, 430, 96, COL['ink'], f0=14, dur=n - 14, style='SemiBold'), 14)
    soft_rise(k.text("Address", "Avenida da Liberdade 110\n1250-146 Lisboa, Portugal", x0, 560, 32, COL['grey'], f0=22, dur=n - 22,
                     style='Regular', lh=1.25), 22)
    grow_x(k.rect("Rule", x0, 648, 120, 3, COL['teal'], f0=30, dur=n - 30), 30, 18)
    soft_rise(k.text("Opening", "Opening 2 March 2027", x0, 702, 36, COL['ink'], f0=34, dur=n - 34, style='Medium'), 34)


# ---------------------------------------------------------------- 5. award badge
def award(d):
    n = 120
    k = d.comp("CB Award badge", n, "caw"); lab_bg(k, n)
    cx, cy = 960, 400
    ring(k, "Badge ring", cx, cy, 380, COL['teal'], 4, 0, 30)
    card_settle(k.ell("Badge disc", cx, cy, 336, 336, COL['navy2'], f0=8, dur=n - 8), 8)
    star = k.star("Star", cx, cy - 64, 96, 5, 0.45, COL['teal'], f0=16, dur=n - 16)
    star.rotv(90)                       # first point to the top (stars start pointing right, like polygons)
    card_settle(star, 16)
    soft_rise(k.text("Winner", "WINNER", cx, cy + 40, 36, COL['white'], f0=20, dur=n - 20, style='SemiBold', align='center', track=1.3), 20)
    soft_rise(k.text("Year", "2026", cx, cy + 96, 30, COL['grey'], f0=24, dur=n - 24, style='Medium', align='center'), 24)
    soft_rise(k.text("Award", "Best Place to Work", cx, 700, 60, COL['white'], f0=32, dur=n - 32, style='SemiBold', align='center'), 32)
    soft_rise(k.text("Awarded by", "Regional Business Awards", cx, 776, 32, COL['grey'], f0=38, dur=n - 38, style='Regular',
                     align='center'), 38)


# ---------------------------------------------------------------- 6. partner logo wall
PARTNERS = [("HALDEN", 'SemiBold', 1.3), ("Brightwater", 'Bold', None), ("ORBITAL", 'Medium', 1.5), ("Kestrel & Co", 'SemiBold', None),
            ("Meridian", 'Bold', None), ("FIELDSTONE", 'SemiBold', 1.2), ("Nova Rail", 'Medium', None), ("LARCHMONT", 'Bold', 1.1),
            ("Quayside", 'SemiBold', None), ("TESSELLATE", 'Medium', 1.0), ("Ashgrove", 'Bold', None), ("PINECREST", 'SemiBold', 1.2)]


def partner_wall(d):
    n = 120
    k = d.comp("CB Partner wall", n, "cpl"); lab_bg(k, n); k.rect("Light background", 0, 0, 1920, 1080, COL['light'], f0=0, dur=n)
    soft_rise(k.text("Title", "Trusted by teams at", 960, 210, 52, COL['ink'], f0=0, dur=n, style='SemiBold', align='center'), 0)
    logo = lin('4A5568')
    for i, (name, style, track) in enumerate(PARTNERS):
        r, c = divmod(i, 4)
        x, y = 390 + c * 380, 420 + r * 190
        f = 6 + (r + c) * 4                                              # a diagonal sweep from the top left
        card_settle(k.rect(f"Tile {i + 1}", x, y, 340, 150, CARD, r=14, f0=f, dur=n - f, center=True), f)
        t = k.text(f"Logo {i + 1}", name, x, y, 34, logo, f0=f + 4, dur=n - f - 4, style=style, align='center', track=track)
        t.op([(f + 4, 0.0, 'Linear'), (f + 16, 1.0, 'Ease out')])
    soft_rise(k.text("More", "and 400 more organisations", 960, 960, 30, COL['grey'], f0=40, dur=n - 40, style='Regular', align='center'), 40)


# ---------------------------------------------------------------- 7. careers card
PILLS = ["Lisbon or remote", "Full time", "Data platform"]


def careers(d):
    n = 150
    k = d.comp("CB Careers card", n, "chr"); lab_bg(k, n)
    x0 = 240
    bar = k.rect("Accent bar", 180, 280, 6, 560, COL['teal'], f0=0, dur=n)
    bar.anchor(0, 1); bar.scale([(0, [1.0, 0.0], 'Linear'), (24, [1.0, 1.0], DECEL)])      # draws down from its top
    soft_rise(k.text("Kicker", "WE'RE HIRING", x0, 320, 30, COL['teal'], f0=4, dur=n - 4, style='SemiBold', track=1.3), 4)
    soft_rise(k.text("Role", "Senior Data Engineer", x0, 420, 84, COL['white'], f0=8, dur=n - 8, style='SemiBold'), 8)
    x = x0
    for i, s in enumerate(PILLS):
        w = round(len(s) * 15.5 + 64)
        f = 18 + i * 5
        card_settle(k.rect(f"Pill {i + 1}", x + w / 2, 530, w, 56, COL['navy2'], r=28, f0=f, dur=n - f, center=True), f)
        t = k.text(f"Pill text {i + 1}", s, x + w / 2, 530, 28, COL['white'], f0=f + 2, dur=n - f - 2, style='Medium', align='center')
        t.op([(f + 2, 0.0, 'Linear'), (f + 14, 1.0, 'Ease out')])
        x += w + 16
    soft_rise(k.text("Body", "Help us build the data platform\n2 million people rely on.", x0, 650, 34, COL['grey'], f0=32, dur=n - 32,
                     style='Regular', lh=1.25), 32)
    card_settle(k.rect("Button", x0 + 230, 790, 460, 80, COL['teal'], r=12, f0=44, dur=n - 44, center=True), 44)
    soft_rise(k.text("Button text", "northwind.com/careers", x0 + 230, 790, 32, COL['navy'], f0=48, dur=n - 48, style='SemiBold',
                     align='center'), 48)


# ---------------------------------------------------------------- 8. safety notice
def safety(d):
    n = 150
    k = d.comp("CB Safety notice", n, "csn"); lab_bg(k, n)
    band = k.rect("Signal band", 0, 1040, 1920, 40, AMBER, f0=0, dur=n)
    grow_x(band, 0, 20)
    tx, ty = 420, 500
    sign = k.ngon("Sign", tx, ty, 340, 3, AMBER, f0=6, dur=n - 6)
    sign.rotv(90)                       # a polygon's first corner points right and its Angle does not turn it (KI-150): rotate the transform
    card_settle(sign, 6, d=24)
    soft_rise(k.text("Sign mark", "!", tx, ty + 18, 110, COL['navy'], f0=14, dur=n - 14, style='Bold', align='center'), 14)
    x0 = 680
    soft_rise(k.text("Kicker", "SAFETY NOTICE", x0, 330, 30, AMBER, f0=10, dur=n - 10, style='SemiBold', track=1.3), 10)
    soft_rise(k.text("Heading", "Hard hats beyond\nthis point", x0, 455, 76, COL['white'], f0=14, dur=n - 14, style='SemiBold', lh=1.1), 14)
    soft_rise(k.text("Body", "Site B, all zones. From 1 March 2027.", x0, 600, 34, COL['grey'], f0=24, dur=n - 24, style='Regular'), 24)
    grow_x(k.rect("Rule", x0, 664, 120, 3, AMBER, f0=30, dur=n - 30), 30, 18)
    soft_rise(k.text("Policy", "Policy HS-04, section 2", x0, 712, 30, COL['grey'], f0=34, dur=n - 34, style='Medium'), 34)


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    org_chart(d); values_grid(d); anniversary(d); office(d); award(d); partner_wall(d); careers(d); safety(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
