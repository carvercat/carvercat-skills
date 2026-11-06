"""Kinetic Typography round 3: seven lab comps for briefs the pack could not serve before (karaoke
lyric line, manifesto scroll, echo stack, opening credits, strike and replace, zoom through a letter,
poster lockup), written straight into a .carverproj.

    import kinetic_type_lab3 as L
    L.build(PROJECT, None)    # pass 1: only a "KT3 Measure" comp of throwaway texts
    m = {label: bounds}        # carvercat_authoring mode:geometry detail:bounds on each, at frame 5
    L.build(PROJECT, m)       # pass 2: the seven lab comps

Same palette and font as kinetic_type_lab.py. Every move is baked as keys here (no presets to apply),
so the templates need no other pack. The measurements give ink widths (Carvercat's bounds are about
4% narrower than the advance widths of cc.textw): the poster lockup is justified on them, the zoom
finds the counter of the O with them, and the strike line is sized to the struck word.
After pass 2: edit.open {path, force:true}; edit.save; check with carvercat_inspect and carvercat_look;
extract templates with comp_to_template.py (--drop "Lab bg"). Fonts: Rethink Sans must be installed
(KI-136). Docs: ai/patterns/kinetic-typography.md (round 3).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author"))
from kinetic_type_lab import Doc, lin, P, COL, EXPO, ACCEL, FONT_STYLE, lab_bg
from cc import textw

DIM = lin('6F6B64')          # unsung / dimmed words: still readable on #0B0B0F
SMOOTH = (0.65, 0, 0.35, 1)
PRESETS, MASKS = [], []

LOCKUP = ["NEW TYPE", "FESTIVAL", "LISBON", "MAY 12–14"]
LOCKUP_W, LOCKUP_GAP = 1000, 34                       # ink width of every line; gap between cap boxes
ZOOM_WORDS, ZOOM_PX, ZOOM_Z = ("LOOK", "CLOSER"), 260, 34.0
STRIKE = ("It isn't luck.", "luck", 110)


def fade(o, f, d=5, to=1.0):
    return o.op([(f, 0.0, 'Linear'), (f + d, to, 'Ease out')])


def rise(o, f, dy=24, d=14, dx=0, op=True):
    bx, by = o.base
    o.pos([(f, [bx - dx / 1920, by - dy / 1080], 'Linear'), (f + d, [bx, by], EXPO)])
    if op:
        fade(o, f)
    return o


def slam(o, f, s0=1.35, d=8, fade_in=0):
    """beat-words hit: big to 1 (expo); a cut in at full opacity unless fade_in"""
    o.scale([(f, s0, 'Linear'), (f + d, 1.0, EXPO)])
    if fade_in:
        fade(o, f, fade_in)
    return o


def colour(o, spec):
    return o.key(o.src('text_fill', 'color'), spec)


def hollow(o, col, th=0.035):
    """outline-only text (fill none, outline solid)"""
    o.set(o.src('text_fill', 'paint'), 'none')
    o.set(o.src('text_outline', 'paint'), 'solid').set(o.src('text_outline', 'color'), col[:3])
    o.set(o.src('text_outline', 'thickness'), th)
    return o


def measure(d):
    k = d.comp("KT3 Measure", 10, "k3m")
    for s in LOCKUP:
        k.text(f"M {s}", s, 200, 540, 100, COL['ink'], f0=0, dur=10, style=FONT_STYLE)
    for s in (ZOOM_WORDS[0], "LO", "O"):
        k.text(f"M {s}", s, 200, 540, ZOOM_PX, COL['ink'], f0=0, dur=10, style=FONT_STYLE)
    line, word, px = STRIKE
    head = line[:line.index(word) + 1]                       # "It isn't l"
    for s in (line, head, word[0], word, "uc"):
        k.text(f"M {s}", s, 200, 540, px, COL['ink'], f0=0, dur=10, style=FONT_STYLE)


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
            o = k.text(f"Word {r + 1}.{i + 1}", w, x + ww / 2, y, px, DIM, f0=e, dur=n - e, style=FONT_STYLE, align='center')
            rise(o, e, dy=20, d=14)
            colour(o, [(f, DIM, 'Linear'), (f + 3, COL['sun'], 'Ease out')])           # the sung word fills
            o.addkeys(o.tr('scale'), [(f, [1.0, 1.0], 'Linear'), (f + 3, [1.08, 1.08], 'Ease out'), (f + 12, [1.0, 1.0], EXPO)])
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
        o = k.text(f"Line {i + 1}", s, x0, y0, px, COL['accent'] if i == last else COL['ink'], f0=f, dur=n - f, style=FONT_STYLE)
        bx, by = o.base
        ks = [(f, [bx, by - 60 / 1080], 'Linear'), (f + 16, [bx, by], EXPO)]
        for j in range(i + 1, len(MANIFESTO)):                   # each new line pushes the stack up one row
            g = 10 + j * step
            ks += [(g, [bx, by + (j - 1 - i) * row / 1080], 'Linear'), (g + 16, [bx, by + (j - i) * row / 1080], EXPO)]
        o.pos(ks)
        ops = [(f, 0.0, 'Linear'), (f + 5, 1.0, 'Ease out')]
        if i < last:
            ops += [(f + step, 1.0, 'Linear'), (f + step + 8, 0.3, 'Ease out'), (end, 0.3, 'Linear'), (end + 10, 1.0, 'Ease out')]
        o.op(ops)


# ---------------------------------------------------------------- 3. echo stack
def echo(d):
    n, px, word, rowh = 120, 150, "LOUDER", 150
    k = d.comp("KT Echo stack", n, "kes"); lab_bg(k, n)
    for ring, (dy, col) in enumerate([(1, COL['ink']), (2, COL['muted'])]):      # inner echoes first, outer 4 f later
        for side in (-1, 1):
            f = 10 + ring * 4
            o = k.text(f"Echo {'up' if side < 0 else 'down'} {ring + 1}", word, 960, 540, px, COL['ink'], f0=f, dur=n - f,
                       style=FONT_STYLE, align='center')
            hollow(o, col)
            bx, by = o.base
            ty = by - side * dy * rowh / 1080
            drift = by - side * (dy * rowh + 6 * dy) / 1080              # keeps spreading a little through the hold
            near = by - side * (dy * rowh - 36) / 1080                  # starts 36 px nearer the centre: never over a neighbour
            o.pos([(f, [bx, near], 'Linear'), (f + 14, [bx, ty], EXPO), (n, [bx, drift], 'Linear')])
            o.scale([(f, 0.94, 'Linear'), (f + 14, 1.0, EXPO)])
            fade(o, f, 4)
    hero = k.text("Word", word, 960, 540, px, COL['accent'], f0=0, dur=n, style=FONT_STYLE, align='center')
    slam(hero, 0, s0=1.5, d=10, fade_in=3)


# ---------------------------------------------------------------- 4. opening credits
CREDITS = [("DIRECTED BY", "Lena Okafor"), ("WRITTEN BY", "Tomás Reyes"), ("MUSIC BY", "Ines Varga")]
TITLE = "NORTHBOUND"


def credits(d):
    n, per = 210, 50
    k = d.comp("KT Opening credits", n, "kcr"); lab_bg(k, n)
    for i, (role, name) in enumerate(CREDITS):
        a = i * per; b = a + per
        r = k.text(f"Role {i + 1}", role, 960, 470, 40, COL['muted'], f0=a, dur=per, style='Medium', align='center', track=1.6)
        r.key(r.src('text_font', 'tracking'), [(a, 2.0, 'Linear'), (a + 24, 1.6, EXPO)])
        r.op([(a, 0.0, 'Linear'), (a + 8, 1.0, 'Ease out'), (b - 8, 1.0, 'Linear'), (b, 0.0, ACCEL)])
        t = k.text(f"Name {i + 1}", name, 960, 570, 110, COL['ink'], f0=a + 2, dur=per - 2, style=FONT_STYLE, align='center', track=1.0)
        t.key(t.src('text_font', 'tracking'), [(a + 2, 1.25, 'Linear'), (a + 32, 1.0, EXPO)])
        t.op([(a + 2, 0.0, 'Linear'), (a + 10, 1.0, 'Ease out'), (b - 8, 1.0, 'Linear'), (b, 0.0, ACCEL)])
    a = len(CREDITS) * per
    t = k.text("Main title", TITLE, 960, 520, 200, COL['ink'], f0=a, dur=n - a, style=FONT_STYLE, align='center')
    t.scale([(a, 1.12, 'Linear'), (a + 20, 1.0, EXPO), (n, 0.98, 'Linear')])     # lands, then a slow pull back
    fade(t, a, 6)
    half = textw(TITLE, 200, FONT_STYLE) * 0.48
    rule = k.line("Title rule", [(960 - half, 650), (960 + half, 650)], COL['accent'], px=8, f0=a + 10, dur=n - a - 10)
    tp = rule.trim([(a + 10, 0.5, 'Linear'), (a + 26, 0.0, EXPO)], which='start')    # draws out from the centre
    rule.key(tp + '.end', [(a + 10, 0.5, 'Linear'), (a + 26, 1.0, EXPO)])


# ---------------------------------------------------------------- 5. strike and replace
def strike(d, m):
    n = 120
    k = d.comp("KT Strike and replace", n, "ksr"); lab_bg(k, n)
    line, word, px = STRIKE
    head = line[:line.index(word) + 1]
    shift = 960 - (200 + m[f"M {line}"]["w"] / 2)                 # centre the measured line
    wl = m[f"M {head}"]["x"] + m[f"M {head}"]["w"] - m[f"M {word[0]}"]["w"] + shift
    wr = wl + m[f"M {word}"]["w"]
    y1 = 430
    xh = m["M uc"]["y"] + m["M uc"]["h"] / 2 - 540                 # x-height centre relative to the text's y
    row1 = k.text("Claim", line, 200 + shift, y1, px, COL['ink'], f0=0, dur=n, style=FONT_STYLE)
    rise(row1, 0, dy=24, d=14)
    colour(row1, [(42, COL['ink'], 'Linear'), (52, DIM, 'Ease out')])          # the whole wrong claim steps back
    st = k.line("Strike", [(wl - 4, y1 + xh), (wr + 10, y1 + xh)], COL['accent'], px=12, f0=34, dur=n - 34)
    st.trim([(34, 0.0, 'Linear'), (44, 1.0, EXPO)], which='end')
    parts = ["It's", "practice."]
    sp = textw(" ", px, FONT_STYLE)
    ws = [textw(s, px, FONT_STYLE) for s in parts]
    x = 960 - (sum(ws) + sp) / 2
    for i, (s, w) in enumerate(zip(parts, ws)):
        f = 54 + i * 5
        o = k.text(f"Fix {i + 1}", s, x + w / 2, 590, px, COL['accent'] if i else COL['ink'], f0=f, dur=n - f, style=FONT_STYLE,
                   align='center')
        if i == 0:
            slam(o, f, s0=1.3, d=8)                                  # the first word hits
        else:
            rise(o, f, dy=40, d=12)                                  # the answer rises beside it: a slam would grow into "It's"
        x += w + sp


# ---------------------------------------------------------------- 6. zoom through a letter
def zoom_through(d, m):
    n, px = 120, ZOOM_PX
    k = d.comp("KT Zoom through", n, "kzt"); lab_bg(k, n)
    w1, w2 = ZOOM_WORDS
    x0 = 960 - m[f"M {w1}"]["w"] / 2 - (m[f"M {w1}"]["x"] - 200)  # left edge for a centred word
    ox = x0 + (m["M LO"]["x"] + m["M LO"]["w"] - 200) - m["M O"]["w"] / 2     # centre of the first O
    oy = m["M O"]["y"] + m["M O"]["h"] / 2 - 540 + 540
    a, z0, z1 = 40, 0, 58                                           # hold to f40, through the O by f58
    t = k.text("Word", w1, 960, 540, px, COL['ink'], f0=0, dur=z1, style=FONT_STYLE, align='center')
    slam(t, 0, s0=1.4, d=10, fade_in=3)
    # screen point of the O's centre = p + z * (O - p); keep it moving in a straight line onto the frame centre
    dx, dy = ox - 960, oy - 540
    end = P(960 - ZOOM_Z * dx, 540 - ZOOM_Z * dy)
    bx, by = t.base
    t.pos([(a, [bx, by], 'Linear'), (z1, end, ACCEL)])
    t.addkeys(t.tr('scale'), [(a, [1.0, 1.0], 'Linear'), (z1, [ZOOM_Z, ZOOM_Z], ACCEL)])
    t2 = k.text("Word 2", w2, 960, 540, 220, COL['accent'], f0=z1, dur=n - z1, style=FONT_STYLE, align='center')
    t2.scale([(z1, 0.6, 'Linear'), (z1 + 18, 1.0, EXPO)])
    fade(t2, z1, 4)


# ---------------------------------------------------------------- 7. poster lockup
def lockup(d, m):
    n = 120
    k = d.comp("KT Poster lockup", n, "kjl"); lab_bg(k, n)
    cols = [COL['ink'], COL['ink'], COL['accent'], COL['sun']]
    sizes = [100 * LOCKUP_W / m[f"M {s}"]["w"] for s in LOCKUP]
    caps = [m[f"M {s}"]["h"] * z / 100 for s, z in zip(LOCKUP, sizes)]
    total = sum(caps) + LOCKUP_GAP * (len(LOCKUP) - 1)
    top = 540 - total / 2
    for i, (s, z, h) in enumerate(zip(LOCKUP, sizes, caps)):
        ink_x = (m[f"M {s}"]["x"] - 200) * z / 100                  # left bearing at this size
        ink_c = (m[f"M {s}"]["y"] + m[f"M {s}"]["h"] / 2 - 540) * z / 100
        cy = top + h / 2
        f = i * 5
        o = k.text(f"Line {i + 1}", s, 960 - LOCKUP_W / 2 - ink_x, cy - ink_c, z, cols[i], f0=f, dur=n - f, style=FONT_STYLE)
        rise(o, f, dy=0, d=18, dx=240 if i % 2 == 0 else -240)
        top += h + LOCKUP_GAP


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    if m is None:
        measure(d)
    else:
        karaoke(d); manifesto(d); echo(d); credits(d); strike(d, m); zoom_through(d, m); lockup(d, m)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
