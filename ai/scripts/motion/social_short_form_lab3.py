"""Social Short-form round 3 in design units (vertical 1080 x 1920): eight lab comps for briefs the pack could not serve before
(story tap-through, link in bio, POV hook, comment reply, this or that, price drop, giveaway rules, reaction picture-in-picture).

    import social_short_form_lab3 as L; doc = L.build(); doc.send(client, PROJECT.carverproj)

Same palette, vertical authoring and safe area as social_short_form_lab.py: everything inside the social safe box SAFE
[61, 268, 955, 1270] (x 61-1016, y 268-1538), and nothing right of x 851 below y 1151 (the button column). Every move is baked as
keys (no presets to apply): punch(), pop() and whip() write the keys of the pack's Hook punch and Whip in - left presets and of the
round-2 badge pop. Plates behind text are sized with cc.textw (needs Pillow). Names, handles, prices and panels are stand-ins.
Fonts: Rethink Sans must be installed (KI-136). Docs: ai/patterns/social-short-form.md (round 3). Rotation clockwise.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from social_short_form_lab import (EASE_OUT, SDoc, COL, EXPO, BACK, SAFE, W, H, comp, lab_bg, outline, text, line, css, anchor, more, bezier)
from cc import textw

GREY = css('6B6880')            # secondary text on white cards (as the post card)
PURPLE = css('6C5CE7')          # the poll's second colour
PANEL = css('2A2833')           # clip / photo stand-ins (as the before/after panels)
PANEL2 = css('3A2F55')


def punch(o, f, s0=1.25, d=10):
    """the pack's Hook punch as keys: size 1.25 -> 1 on expo in 10 f, opaque in 2 f"""
    o.scale([(f, s0, 'Linear'), (f + d, 1.0, EXPO)])
    return o.op([(f, 0.0, 'Linear'), (f + 2, 1.0, 'Linear')])


def pop(o, f, d=10, s0=0.0):
    """badge pop (as the round-2 listicle badges): size s0 -> 1 on the back curve, opaque in 3 f"""
    o.scale([(f, s0, 'Linear'), (f + d, 1.0, BACK)])
    return o.op([(f, 0.0, 'Linear'), (f + 3, 1.0, 'Linear')])


def whip(o, f, d=10, dx=-0.30):
    """the pack's Whip in - left as keys (dx > 0 comes from the right): 30% of the width in 10 f, expo"""
    bx, by = o.base
    return o.pos([(f, (bx + dx * W, by), 'Linear'), (f + d, (bx, by), EXPO)])


def fade(o, f, d=4, to=1.0, frm=0.0):
    return o.op([(f, frm, 'Linear'), (f + d, to, EASE_OUT)])


def grow_x(o, f, d=8, ax=-1):
    anchor(o, ax, 0); o.scale([(f, [0.0, 1.0], 'Linear'), (f + d, [1.0, 1.0], EXPO)]); return o


def draw(o, f, d=8):
    o.trim([(f, 0.0, 'Linear'), (f + d, 1.0, EXPO)]); return o


def tick(k, name, x, y, s, col, px, f0, dur):
    """a check mark: short leg down-right, long leg up-right; (x, y) is the corner"""
    return line(k, name, [(x - 0.55 * s, y - 0.5 * s), (x, y), (x + s, y - 1.05 * s)], col, px, f0=f0, dur=dur)


def ripple(k, name, x, y, dia, f, d=14, col=None):
    """one tap ring: a stroked circle grows 0.6 -> 1.5 and fades out; its own short clip"""
    r = k.ell(name, x, y, dia, dia, None, f0=f, dur=d); r.stroke(col or COL['white'], 6)
    r.scale([(f, 0.6, 'Linear'), (f + d, 1.5, EXPO)]); r.op([(f, 0.9, 'Linear'), (f + d, 0.0, EASE_OUT)])
    return r


# ---------------------------------------------------------------- 1. story tap-through
ST_SEG, ST_PER = 4, 40


def story_tap(d):
    n = ST_SEG * ST_PER
    k = comp(d, "SS Story tap", n, "sst"); lab_bg(k, n)
    x0, x1, y, gap = 90, 990, 290, 16
    w = (x1 - x0 - gap * (ST_SEG - 1)) / ST_SEG
    for i in range(ST_SEG):
        a = x0 + i * (w + gap)
        line(k, f"Segment track {i + 1}", [(a, y), (a + w, y)], COL['muted'], 8, f0=0, dur=n).opv(0.35)
        fill = line(k, f"Segment {i + 1}", [(a, y), (a + w, y)], COL['white'], 8, f0=0, dur=n)
        f = i * ST_PER
        fill.trim([(f, 0.0, 'Linear'), (f + ST_PER - 1, 1.0, 'Linear')], which='end')   # holds 0 before, 1 after
    for i in range(ST_SEG - 1):                                   # a tap on the right half ends each page
        f = (i + 1) * ST_PER - 4
        dot = k.ell(f"Tap dot {i + 1}", 780, 960, 70, 70, COL['white'], f0=f, dur=12)
        dot.op([(f, 0.55, 'Linear'), (f + 12, 0.0, EASE_OUT)])
        ripple(k, f"Tap ring {i + 1}", 780, 960, 120, f)
    # the hint cuts out with the first page (a story tap is a hard cut); 32 opaque frames
    hint = text(k, "Tap hint", "Tap for the next one", 490, 1250, 52, COL['white'], f0=6, dur=ST_PER - 6, style='ExtraBold')
    outline(hint); punch(hint, 6)


# ---------------------------------------------------------------- 2. link in bio
def link_in_bio(d):
    n = 120
    k = comp(d, "SS Link in bio", n, "slb"); lab_bg(k, n)
    punch(text(k, "Kicker", "Want the full list?", 540, 540, 56, COL['yellow'], f0=0, dur=n, style='Bold'), 0)
    punch(text(k, "Link line 1", "LINK", 540, 690, 150, COL['white'], f0=4, dur=n - 4, style='ExtraBold'), 4)
    pw = textw("IN BIO", 150, 'ExtraBold') + 70
    grow_x(k.rect("Bio plate", 540, 850, pw, 150, COL['pink'], r=18, f0=10, dur=n - 10, center=True), 10, 8)
    punch(text(k, "Link line 2", "IN BIO", 540, 850, 150, COL['white'], f0=8, dur=n - 8, style='ExtraBold'), 8)
    cy, cw = 1020, 620
    chip = k.rect("Link chip", 540, cy, cw, 104, COL['white'], r=52, f0=20, dur=n - 20, center=True)
    whip(chip, 20); chip.mblur(180)
    ic = k.ell("Link icon", 540 - cw / 2 + 58, cy, 68, 68, COL['pink'], f0=20, dur=n - 20); whip(ic, 20)
    a1 = line(k, "Link arrow", [(540 - cw / 2 + 46, cy + 12), (540 - cw / 2 + 70, cy - 12)], COL['white'], 6, f0=20, dur=n - 20)
    a2 = line(k, "Link arrow head", [(540 - cw / 2 + 54, cy - 13), (540 - cw / 2 + 71, cy - 13), (540 - cw / 2 + 71, cy + 4)],
              COL['white'], 6, f0=20, dur=n - 20)
    whip(a1, 20); whip(a2, 20)
    t = text(k, "Link text", "mayamakes.co/list", 540 + 34, cy, 44, COL['black'], f0=22, dur=n - 22, style='Bold')
    whip(t, 22)
    pulse = k.rect("Chip pulse", 540, cy, cw, 104, None, r=52, f0=40, dur=18, center=True); pulse.stroke(COL['white'], 6)
    pulse.scale([(40, [1.0, 1.0], 'Linear'), (58, [1.12, 1.5], EXPO)]); pulse.op([(40, 0.9, 'Linear'), (58, 0.0, EASE_OUT)])
    punch(text(k, "Link note", "tap the link on my profile", 540, 1122, 40, COL['muted'], f0=32, dur=n - 32, style='Medium'), 32)


# ---------------------------------------------------------------- 3. POV hook
POV_LINES = ["you finally cleaned", "your camera roll"]


def pov_hook(d):
    n = 90
    k = comp(d, "SS POV hook", n, "spv"); lab_bg(k, n)
    y0 = 470
    pw = textw("POV:", 72, 'ExtraBold') + 56
    pop(k.rect("POV plate", 540, y0, pw, 104, COL['pink'], r=22, f0=0, dur=n, center=True), 0, 8, 0.4)
    pop(text(k, "POV", "POV:", 540, y0, 72, COL['white'], f0=0, dur=n, style='ExtraBold'), 0, 8, 0.4)
    for i, s in enumerate(POV_LINES):
        y, f = y0 + 128 + i * 106, 6 + i * 4
        w = textw(s, 64, 'Bold') + 60
        punch(k.rect(f"Line plate {i + 1}", 540, y, w, 96, COL['white'], r=20, f0=f, dur=n - f, center=True), f, 1.15)
        punch(text(k, f"Line {i + 1}", s, 540, y, 64, COL['black'], f0=f, dur=n - f, style='Bold'), f, 1.15)


# ---------------------------------------------------------------- 4. comment reply
def comment_reply(d):
    n = 120
    k = comp(d, "SS Comment reply", n, "scr"); lab_bg(k, n)
    L, T, w, h = 150, 470, 780, 220
    card = k.rect("Reply card", L + w / 2, T + h / 2, w, h, COL['white'], r=28, f0=0, dur=n, center=True)
    anchor(card, -1, -1); pop(card, 0, 10, 0.8)                   # grows out of its bottom-left corner, like a sticker
    tail = k.rect("Reply tail", L + 70, T + h, 40, 40, COL['white'], r=4, f0=4, dur=n - 4, center=True); tail.rotv(-45)
    fade(tail, 4, 4)
    av = k.ell("Reply avatar", L + 58, T + 62, 60, 60, COL['pink'], f0=4, dur=n - 4); pop(av, 4, 10, 0.4)
    head = text(k, "Reply to", "Reply to @jordan.k's comment", L + 104, T + 62, 32, GREY, f0=6, dur=n - 6, style='Medium', align='left')
    fade(head, 6, 5)
    body = text(k, "Comment", "how do you edit so fast??", L + 40, T + 148, 48, COL['black'], f0=10, dur=n - 10, style='Bold', align='left')
    bx, by = body.base
    body.pos([(10, (bx, by + 20), 'Linear'), (20, (bx, by), EXPO)]); fade(body, 10, 4)
    cap = text(k, "Answer caption", "Here's how", 490, 1250, 72, COL['white'], f0=36, dur=n - 36, style='ExtraBold')
    outline(cap); punch(cap, 36)


# ---------------------------------------------------------------- 5. this or that
TT = [("Sunrise", PANEL2), ("Sunset", css('5A2F45'))]


def this_or_that(d):
    n = 150
    k = comp(d, "SS This or that", n, "sto"); lab_bg(k, n)
    punch(text(k, "Question", "THIS OR THAT?", 540, 420, 96, COL['white'], f0=0, dur=n, style='ExtraBold'), 0)
    cy, cw, ch = 830, 420, 520
    xs = [310, 770]
    cards = []
    for i, ((label, col), x) in enumerate(zip(TT, xs)):
        f = 8 + i * 4
        c = k.rect(f"Choice {i + 1}", x, cy, cw, ch, col, r=32, f0=f, dur=n - f, center=True)
        whip(c, f, 10, -0.30 if i == 0 else 0.30); c.mblur(180)
        t = text(k, f"Choice label {i + 1}", label, x, cy + 180, 60, COL['white'], f0=f + 2, dur=n - f - 2, style='ExtraBold')
        outline(t); whip(t, f + 2, 10, -0.30 if i == 0 else 0.30)
        cards.append((c, t))
    pf = 70                                                         # the pick: B wins, A dims
    ring = k.rect("Pick outline", xs[1], cy, cw + 24, ch + 24, None, r=40, f0=pf, dur=n - pf, center=True)   # under the VS badge
    ring.stroke(COL['yellow'], 10); punch(ring, pf, 1.06, 10)
    vs = k.ell("VS badge", 540, cy, 150, 150, COL['yellow'], f0=22, dur=n - 22); pop(vs, 22)
    pop(text(k, "VS", "VS", 540, cy, 60, COL['black'], f0=22, dur=n - 22, style='ExtraBold'), 22, 10, 0.6)
    for o in cards[0]:
        more(o, 'opacity', [(pf, 1.0, 'Linear'), (pf + 8, 0.35, EASE_OUT)])
    bx, by = xs[1] + cw / 2 - 40, cy - ch / 2 + 40
    pop(k.ell("Pick badge", bx, by, 96, 96, COL['yellow'], f0=pf + 2, dur=n - pf - 2), pf + 2)
    draw(tick(k, "Pick tick", bx - 6, by + 16, 30, COL['black'], 9, pf + 6, n - pf - 6), pf + 6, 8)


# ---------------------------------------------------------------- 6. price drop
def price_drop(d):
    n = 120
    k = comp(d, "SS Price drop", n, "spd"); lab_bg(k, n)
    punch(text(k, "Kicker", "PRICE DROP", 540, 380, 80, COL['yellow'], f0=0, dur=n, style='ExtraBold', track=1.1), 0)
    punch(k.rect("Product panel", 540, 720, 600, 560, PANEL, r=36, f0=4, dur=n - 4, center=True), 4, 1.1)
    fade(text(k, "Product label", "product shot", 540, 720, 36, COL['muted'], f0=8, dur=n - 8, style='Medium'), 8, 6)
    ox, py = 330, 1090
    old = text(k, "Old price", "$89", ox, py, 84, COL['muted'], f0=12, dur=n - 12, style='Bold')
    punch(old, 12)
    ow = textw("$89", 84, 'Bold')
    draw(line(k, "Strike", [(ox - ow / 2 - 12, py + 4), (ox + ow / 2 + 12, py - 8)], COL['pink'], 10, f0=22, dur=n - 22), 22, 8)
    pop(text(k, "New price", "$49", 650, py, 170, COL['yellow'], f0=30, dur=n - 30, style='ExtraBold'), 30, 10, 0.4)
    bd = k.ell("Discount badge", 790, 530, 190, 190, COL['pink'], f0=42, dur=n - 42); bd.rotv(12); pop(bd, 42)
    bt = text(k, "Discount", "-45%", 790, 530, 58, COL['white'], f0=42, dur=n - 42, style='ExtraBold')
    bt.rotv(12); pop(bt, 42)
    cap = text(k, "Ends", "Ends Sunday", 490, 1250, 56, COL['white'], f0=50, dur=n - 50, style='ExtraBold')
    outline(cap); punch(cap, 50)


# ---------------------------------------------------------------- 7. giveaway rules
RULES = ["Follow @mayamakes", "Like this video", "Tag a friend"]


def giveaway(d):
    n = 150
    k = comp(d, "SS Giveaway", n, "sga"); lab_bg(k, n)
    punch(text(k, "Title", "GIVEAWAY", 540, 400, 130, COL['yellow'], f0=0, dur=n, style='ExtraBold'), 0)
    punch(text(k, "Prize", "Win a camera kit", 540, 525, 56, COL['white'], f0=6, dur=n - 6, style='Bold'), 6)
    for i, s in enumerate(RULES):
        y, f = 690 + i * 130, 16 + i * 10
        pop(k.ell(f"Rule badge {i + 1}", 175, y, 84, 84, COL['pink'], f0=f, dur=n - f), f)
        fade(text(k, f"Rule num {i + 1}", str(i + 1), 175, y, 48, COL['white'], f0=f + 2, dur=n - f - 2, style='ExtraBold'), f + 2, 3)
        t = text(k, f"Rule {i + 1}", s, 245, y, 52, COL['white'], f0=f + 3, dur=n - f - 3, style='Bold', align='left')
        bx, by = t.base
        t.pos([(f + 3, (bx, by + 20), 'Linear'), (f + 13, (bx, by), EXPO)]); fade(t, f + 3, 3)
        tf = 54 + i * 6
        draw(tick(k, f"Rule tick {i + 1}", 830, y + 18, 36, COL['yellow'], 10, tf, n - tf), tf, 8)
    punch(text(k, "Ends", "Ends Fri 8 pm. Winner by DM.", 540, 1060, 42, COL['white'], f0=60, dur=n - 60, style='Medium'), 60)
    fade(text(k, "Disclaimer", "Not sponsored by the platform.", 540, 1122, 36, COL['muted'], f0=66, dur=n - 66, style='Medium'), 66, 6)


# ---------------------------------------------------------------- 8. reaction picture-in-picture
def reaction(d):
    n = 120
    k = comp(d, "SS Reaction pip", n, "srx"); lab_bg(k, n)
    punch(k.rect("Clip panel", 540, 700, 920, 780, PANEL, r=36, f0=0, dur=n, center=True), 0, 1.06)
    fade(text(k, "Clip label", "the clip you react to", 540, 700, 36, COL['muted'], f0=4, dur=n - 4, style='Medium'), 4, 6)
    tw = textw("REACTING TO", 34, 'ExtraBold') + 44
    tag = k.rect("Reacting tag", 120 + tw / 2, 372, tw, 64, COL['pink'], r=32, f0=12, dur=n - 12, center=True)
    whip(tag, 12)
    whip(text(k, "Reacting", "REACTING TO", 120 + tw / 2, 372, 34, COL['white'], f0=12, dur=n - 12, style='ExtraBold'), 12)
    cr = text(k, "Credit", "@originalcreator", 960, 1040, 36, COL['white'], f0=18, dur=n - 18, style='Bold', align='right')
    outline(cr); fade(cr, 18, 5)
    cam = k.ell("Reaction cam", 230, 1120, 300, 300, PANEL2, f0=10, dur=n - 10); cam.stroke(COL['yellow'], 8)
    pop(cam, 10, 12)
    fade(text(k, "Cam label", "you", 230, 1120, 36, COL['muted'], f0=14, dur=n - 14, style='Medium'), 14, 6)
    cw = textw("wait for it...", 64, 'ExtraBold')
    cap = text(k, "Caption", "wait for it...", 830 - cw / 2, 1230, 64, COL['white'], f0=30, dur=n - 30, style='ExtraBold')
    outline(cap); punch(cap, 30)


def comps(d):
    story_tap(d); link_in_bio(d); pov_hook(d); comment_reply(d); this_or_that(d); price_drop(d); giveaway(d); reaction(d)


def build():
    d = SDoc(); comps(d)
    return d


if __name__ == "__main__":
    print(__doc__)
