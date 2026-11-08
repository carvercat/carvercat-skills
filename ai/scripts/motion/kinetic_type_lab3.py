"""Kinetic Typography round 3 in design units: seven lab comps for briefs the pack could not serve before (karaoke lyric line, manifesto
scroll, echo stack, opening credits, strike and replace, zoom through a letter, poster lockup).

    import kinetic_type_lab3 as L; doc = L.build(); doc.send(client, PROJECT.carverproj)

Same palette, kit and font as kinetic_type_lab.py. Every move is baked as keys (no presets to apply). INK (in kinetic_type_lab.py)
gives the ink widths the app measures: the poster lockup is justified on them, the zoom finds the counter of the O with them, and the
strike line is sized to the struck word. The echo stack's hollow texts get their outline after the apply (a scene cannot say a text
outline: KDoc.post). Rotation signs, units and colours: design units (clockwise degrees, exact hex). Docs: ai/patterns/kinetic-typography.md.
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kinetic_type_lab import (KDoc, COL, EXPO, ACCEL, FONT_STYLE, INK, lab_bg, KT, textw, addkeys, fade, rise, slam, line, W, H)
from explainer_lab import px_ls

DIM = '#6F6B64'          # unsung / dimmed words: still readable on #0B0B0F
LOCKUP = ["NEW TYPE", "FESTIVAL", "LISBON", "MAY 12–14"]
LOCKUP_W, LOCKUP_GAP = 1000, 34                       # ink width of every line; gap between cap boxes
ZOOM_WORDS, ZOOM_PX, ZOOM_Z = ("LOOK", "CLOSER"), 260, 34.0
STRIKE = ("It isn't luck.", "luck", 110)


def ink(label): return INK[label]


def hollow(d, k, o, col):
    """outline-only text: no fill now, the outline colour and thickness after the apply"""
    o.set('fill', 'none')
    def outline(c, i):
        c.run('property.set', id=i, key='stroke', value=col)
        c.run('property.set', id=i, key='text.outline.thickness', value=0.035)
    d.post.append((k.name, o.name, outline))
    return o


# ---------------------------------------------------------------- 1. karaoke lyric line
KARAOKE = [["We", "were", "running", "out", "of", "time,"], ["but", "the", "night", "was", "ours."]]
SUNG = [[14, 20, 26, 38, 44, 50], [70, 76, 82, 94, 100]]     # the frame each word is sung (from the vocal)


def karaoke(d):
    n, px = 150, 88
    k = d.comp("KT Karaoke line", n, "kko"); lab_bg(k, n)
    sp = textw(" ", px, FONT_STYLE)
    for r, (words, sung) in enumerate(zip(KARAOKE, SUNG)):
        ws = [textw(w, px, FONT_STYLE) for w in words]
        x = 960 - (sum(ws) + sp * (len(ws) - 1)) / 2
        y = 476 + r * 128
        for i, (w, ww, f) in enumerate(zip(words, ws, sung)):
            e = r * 4 + i                                        # the line rises in as one (2 f per word)
            o = KT(k, f"Word {r + 1}.{i + 1}", w, x + ww / 2, y, px, DIM, e, n - e, align='center')
            rise(o, e, dy=20, d=14)
            o.colour([(f, DIM, 'Linear'), (f + 3, COL['sun'], 'app-out')])           # the sung word fills
            addkeys(o, 'scale', [(f, 1.0, 'Linear'), (f + 3, 1.08, 'app-out'), (f + 12, 1.0, EXPO)])
            x += ww + sp


# ---------------------------------------------------------------- 2. manifesto scroll
MANIFESTO = ["We don't chase trends.", "We build what lasts.", "We say less.", "We mean all of it."]


def manifesto(d):
    n, px, step, row, y0, x0 = 240, 84, 40, 128, 700, 260
    k = d.comp("KT Manifesto scroll", n, "kms"); lab_bg(k, n)
    last = len(MANIFESTO) - 1
    end = 10 + len(MANIFESTO) * step                             # f170: every line comes back for the final read
    for i, s in enumerate(MANIFESTO):
        f = 10 + i * step
        o = KT(k, f"Line {i + 1}", s, x0, y0, px, COL['accent'] if i == last else COL['ink'], f, n - f)
        bx, by = o.base
        ks = [(f, (bx, by + 60), 'Linear'), (f + 16, (bx, by), EXPO)]
        for j in range(i + 1, len(MANIFESTO)):                   # each new line pushes the stack up one row
            g = 10 + j * step
            ks += [(g, (bx, by - (j - 1 - i) * row), 'Linear'), (g + 16, (bx, by - (j - i) * row), EXPO)]
        o.pos(ks)
        ops = [(f, 0.0, 'Linear'), (f + 5, 1.0, 'app-out')]
        if i < last:
            ops += [(f + step, 1.0, 'Linear'), (f + step + 8, 0.3, 'app-out'), (end, 0.3, 'Linear'), (end + 10, 1.0, 'app-out')]
        o.op(ops)


# ---------------------------------------------------------------- 3. echo stack
def echo(d):
    n, px, word, rowh = 120, 150, "LOUDER", 150
    k = d.comp("KT Echo stack", n, "kes"); lab_bg(k, n)
    for ring, (dy, col) in enumerate([(1, COL['ink']), (2, COL['muted'])]):      # inner echoes first, outer 4 f later
        for side in (-1, 1):                                                       # -1 up the screen, +1 down
            f = 10 + ring * 4
            o = KT(k, f"Echo {'up' if side < 0 else 'down'} {ring + 1}", word, 960, 540, px, COL['ink'], f, n - f, align='center')
            hollow(d, k, o, col)
            bx, by = o.base
            o.pos([(f, (bx, by + side * (dy * rowh - 36)), 'Linear'),           # starts 36 px nearer the centre: never over a neighbour
                   (f + 14, (bx, by + side * dy * rowh), EXPO),
                   (n, (bx, by + side * (dy * rowh + 6 * dy)), 'Linear')])      # keeps spreading a little through the hold
            o.scale([(f, 0.94, 'Linear'), (f + 14, 1.0, EXPO)])
            fade(o, f, 4)
    hero = KT(k, "Word", word, 960, 540, px, COL['accent'], 0, n, align='center')
    slam(hero, 0, s0=1.5, d=10, fade_in=3)


# ---------------------------------------------------------------- 4. opening credits
CREDITS = [("DIRECTED BY", "Lena Okafor"), ("WRITTEN BY", "Tomás Reyes"), ("MUSIC BY", "Ines Varga")]
TITLE = "NORTHBOUND"


def credits(d):
    n, per = 210, 50
    k = d.comp("KT Opening credits", n, "kcr"); lab_bg(k, n)
    for i, (role, name) in enumerate(CREDITS):
        a = i * per; b = a + per
        r = KT(k, f"Role {i + 1}", role, 960, 470, 40, COL['muted'], a, per, 'Medium', 'center', track=1.6, width=1500)
        r.tracking([(a, px_ls(2.0, 40), 'Linear'), (a + 24, px_ls(1.6, 40), EXPO)])
        r.op([(a, 0.0, 'Linear'), (a + 8, 1.0, 'app-out'), (b - 8, 1.0, 'Linear'), (b, 0.0, ACCEL)])
        t = KT(k, f"Name {i + 1}", name, 960, 570, 110, COL['ink'], a + 2, per - 2, FONT_STYLE, 'center', track=1.0, width=1700)
        t.tracking([(a + 2, px_ls(1.25, 110), 'Linear'), (a + 32, 0.0, EXPO)])
        t.op([(a + 2, 0.0, 'Linear'), (a + 10, 1.0, 'app-out'), (b - 8, 1.0, 'Linear'), (b, 0.0, ACCEL)])
    a = len(CREDITS) * per
    t = KT(k, "Main title", TITLE, 960, 520, 200, COL['ink'], a, n - a, align='center', width=1800)
    t.scale([(a, 1.12, 'Linear'), (a + 20, 1.0, EXPO), (n, 0.98, 'Linear')])     # lands, then a slow pull back
    fade(t, a, 6)
    half = textw(TITLE, 200, FONT_STYLE) * 0.48
    rule = line(k, "Title rule", [(960 - half, 650), (960 + half, 650)], COL['accent'], px=8, f0=a + 10, dur=n - a - 10)
    rule.trim([(a + 10, 0.5, 'Linear'), (a + 26, 0.0, EXPO)], which='start')    # draws out from the centre
    rule.key('trimEnd', [(a + 10, '50%', 'Linear'), (a + 26, '100%', EXPO)])


# ---------------------------------------------------------------- 5. strike and replace
def strike(d):
    n = 120
    k = d.comp("KT Strike replace", n, "ksr"); lab_bg(k, n)
    line_s, word, px = STRIKE
    head = line_s[:line_s.index(word) + 1]
    shift = 960 - (200 + ink(f"S {line_s}")[2] / 2)                 # centre the measured line
    wl = ink(f"S {head}")[0] + ink(f"S {head}")[2] - ink(f"S {word[0]}")[2] + shift
    wr = wl + ink(f"S {word}")[2]
    y1 = 430
    xh = ink("S uc")[1] + ink("S uc")[3] / 2 - 540                 # x-height centre relative to the text's y
    row1 = KT(k, "Claim", line_s, 200 + shift, y1, px, COL['ink'], 0, n)
    rise(row1, 0, dy=24, d=14)
    row1.colour([(42, COL['ink'], 'Linear'), (52, DIM, 'app-out')])          # the whole wrong claim steps back
    st = line(k, "Strike", [(wl - 4, y1 + xh), (wr + 10, y1 + xh)], COL['accent'], px=12, f0=34, dur=n - 34)
    st.trim([(34, 0.0, 'Linear'), (44, 1.0, EXPO)])
    parts = ["It's", "practice."]
    sp = textw(" ", px, FONT_STYLE)
    ws = [textw(s, px, FONT_STYLE) for s in parts]
    x = 960 - (sum(ws) + sp) / 2
    for i, (s, w) in enumerate(zip(parts, ws)):
        f = 54 + i * 5
        o = KT(k, f"Fix {i + 1}", s, x + w / 2, 590, px, COL['accent'] if i else COL['ink'], f, n - f, align='center')
        if i == 0: slam(o, f, s0=1.3, d=8)                                  # the first word hits
        else: rise(o, f, dy=40, d=12)                                       # the answer rises beside it: a slam would grow into "It's"
        x += w + sp


# ---------------------------------------------------------------- 6. zoom through a letter
def zoom_through(d):
    n, px = 120, ZOOM_PX
    k = d.comp("KT Zoom through", n, "kzt"); lab_bg(k, n)
    w1, w2 = ZOOM_WORDS
    x0 = 960 - ink(f"Z {w1}")[2] / 2 - (ink(f"Z {w1}")[0] - 200)  # left edge for a centred word
    ox = x0 + (ink("Z LO")[0] + ink("Z LO")[2] - 200) - ink("Z O")[2] / 2     # centre of the first O
    oy = ink("Z O")[1] + ink("Z O")[3] / 2
    a, z1 = 40, 58                                                  # hold to f40, through the O by f58
    t = KT(k, "Word", w1, 960, 540, px, COL['ink'], 0, z1, align='center')
    slam(t, 0, s0=1.4, d=10, fade_in=3)
    # screen point of the O's centre = p + z * (O - p); keep it moving in a straight line onto the frame centre
    dx, dy = ox - 960, oy - 540
    bx, by = t.base
    t.pos([(a, (bx, by), 'Linear'), (z1, (960 - ZOOM_Z * dx, 540 - ZOOM_Z * dy), ACCEL)])
    addkeys(t, 'scale', [(a, 1.0, 'Linear'), (z1, ZOOM_Z, ACCEL)])
    t2 = KT(k, "Word 2", w2, 960, 540, 220, COL['accent'], z1, n - z1, align='center')
    t2.scale([(z1, 0.6, 'Linear'), (z1 + 18, 1.0, EXPO)])
    fade(t2, z1, 4)


# ---------------------------------------------------------------- 7. poster lockup
def lockup(d):
    n = 120
    k = d.comp("KT Poster lockup", n, "kjl"); lab_bg(k, n)
    cols = [COL['ink'], COL['ink'], COL['accent'], COL['sun']]
    sizes = [100 * LOCKUP_W / ink(f"L100 {s}")[2] for s in LOCKUP]
    caps = [ink(f"L100 {s}")[3] * z / 100 for s, z in zip(LOCKUP, sizes)]
    total = sum(caps) + LOCKUP_GAP * (len(LOCKUP) - 1)
    top = 540 - total / 2
    for i, (s, z, h) in enumerate(zip(LOCKUP, sizes, caps)):
        m = ink(f"L100 {s}")
        ink_x = (m[0] - 200) * z / 100                  # left bearing at this size
        ink_c = (m[1] + m[3] / 2 - 540) * z / 100
        cy = top + h / 2
        f = i * 5
        o = KT(k, f"Line {i + 1}", s, 960 - LOCKUP_W / 2 - ink_x, cy - ink_c, z, cols[i], f, n - f)
        rise(o, f, dy=0, d=18, dx=240 if i % 2 == 0 else -240)
        top += h + LOCKUP_GAP


def build(path=None, m=None):
    d = KDoc()
    karaoke(d); manifesto(d); echo(d); credits(d); strike(d); zoom_through(d); lockup(d)
    return d


if __name__ == "__main__":
    print(__doc__)
