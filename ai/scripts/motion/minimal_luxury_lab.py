"""The Minimal Luxury lab comps in design units (cc2.py: px, y down, degrees clockwise, CSS colours and easing).

    import minimal_luxury_lab as L; doc = L.build(); doc.send(client, PROJECT.carverproj)   # scene.apply per comp, then edit.save

Four comps: tracked title, feather wipe, product frame, slow quote. The pack's moves (Slow fade in, Slow fade out, Drift up) are
written as plain keys by corporate_luxury_kit.py and the masks are scene masks, so nothing is applied after `send`.
Fonts: Rethink Sans (Google Fonts, SIL OFL) must be installed; Carvercat resolves text fonts from installed fonts only.
Docs: ai/patterns/minimal-luxury.md. Design units: px from the top-left, y down; comp frames, 30 fps.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corporate_luxury_kit import EASE_OUT
from corporate_luxury_kit import (Doc, css, BEZ, text, line, tracking, slow_in, slow_out, drift_up, rule_open, breathe)

COL = dict(bg=css('0E0D0B'), ivory=css('EDE6D6'), gold=css('C8A96A'), muted=css('8C8574'), deep=css('1A1814'))
DECEL, SMOOTH, EXPO = BEZ['decel'], BEZ['smooth'], BEZ['expo']


def lab_bg(k, n):
    k.rect("Lab bg", 0, 0, 1920, 1080, COL['bg'], f0=0, dur=n)


def tracked_title(d):
    n = 120
    k = d.comp("ML Tracked title", n, "mtt"); lab_bg(k, n)
    t = text(k, "Title", "MAISON ELAN", 960, 500, 72, COL['ivory'], f0=0, dur=n, style='Regular', align='center', track=1.8)
    tracking(t, [(0, 1.8, 'Linear'), (60, 1.35, DECEL), (n, 1.38, 'Linear')])
    t.op([(0, 0, 'Linear'), (30, 1, EASE_OUT)])
    rule_open(line(k, "Rule", [(840, 580), (1080, 580)], COL['gold'], 2, f0=0, dur=n), 20, 30, EXPO)
    slow_in(text(k, "Tagline", "PARIS  ·  SINCE 1924", 960, 640, 28, COL['muted'], f0=40, dur=n - 40, style='Regular', align='center', track=1.5), 40)


def feather_wipe(d):
    n = 75
    k = d.comp("ML Feather wipe", n, "mfw"); lab_bg(k, n)
    h = text(k, "Headline", "Quiet confidence", 960, 540, 96, COL['ivory'], f0=0, dur=n, style='Regular', align='center')
    w = 1500
    win = k.rect("Wipe window", 960, 540, w, 400, COL['ivory'], f0=0, dur=n, center=True)
    win.set('softEdge', 160)                        # Fill soft edge: the feather of the wipe
    bx, by = win.base
    win.pos([(0, (bx - (w + 160), by), 'Linear'), (45, (bx, by), SMOOTH)])
    k.mask(h, win)


def product_frame(d):
    n = 120
    k = d.comp("ML Product frame", n, "mpf"); lab_bg(k, n)
    cx, cy, w, h = 960, 500, 520, 680
    fr = k.rect("Frame", cx, cy, w, h, None, f0=0, dur=n, center=True); fr.stroke(COL['gold'], 2)
    fr.trim([(0, 0.0, 'Linear'), (40, 1.0, SMOOTH)], which='end')
    prod = k.ell("Product", cx, cy, 300, 300, COL['gold'], f0=20, dur=n - 20)
    # a light spot at the top-left corner of the sphere's box, 424 px to the dark edge
    prod.set('fill', 'radial-gradient(ellipse 424.264px at 0%% 0%%, %s 0%%, %s 100%%)' % (COL['ivory'], COL['deep']))
    slow_in(prod, 20); drift_up(prod, 20, n - 21)
    slow_in(text(k, "Caption", "No. 7  ·  EAU DE PARFUM", cx, cy + h / 2 + 70, 30, COL['ivory'], f0=44, dur=n - 44, style='Regular', align='center', track=1.4), 44)


def slow_quote(d):
    n = 150
    k = d.comp("ML Slow quote", n, "msq"); lab_bg(k, n)
    q = text(k, "Quote", "“Simplicity is the\nultimate sophistication.”", 960, 500, 64, COL['ivory'], f0=0, dur=n,
             style='Regular', align='center', lh=1.3)
    # every line plays the object's own keys, 12 f apart: it rises 1 % and clears a 11.5 px blur. 
    bx, by = q.base
    q.pos([(0, (bx, by + 10.8), 'expo'), (30, (bx, by), 'Linear')])
    q.blur([(0, 11.5, 'expo'), (30, 0, 'Linear')])
    q.op([(0, 0, 'Linear'), (15, 1, EASE_OUT)])
    tracking(q, [(42, 1.0, 'Linear'), (150, 1.04, 'Linear')])     # the v1 template drifts the tracking 1.0 -> 1.04 over the hold
    q.stagger(by='lines', each=12)
    slow_in(text(k, "Author", "—  ANONYMOUS", 960, 660, 28, COL['muted'], f0=60, dur=n - 60, style='Regular', align='center', track=1.5), 60)


def build():
    d = Doc()
    tracked_title(d); feather_wipe(d); product_frame(d); slow_quote(d)
    return d


if __name__ == "__main__":
    print(__doc__)
