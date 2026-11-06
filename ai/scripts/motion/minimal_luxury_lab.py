"""Write the Minimal Luxury lab comps into a .carverproj (direct project-file authoring).

    import minimal_luxury_lab as L; presets, masks = L.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); for each MASKS
pair (content, window) run mask.make {ids:[window, content]} - the FIRST id is the mask -
then parent.clear with the same ids; edit.save. Check with carvercat_inspect and
carvercat_look; extract templates with comp_to_template.py (--drop "Lab bg").

Fonts: Rethink Sans (Google Fonts, SIL OFL) must be installed; Carvercat resolves text
fonts from installed fonts only.
Docs: ai/patterns/minimal-luxury.md. Pixel space 1920x1080, y down; comp frames, 30 fps.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author"))
from cc import Doc, lin, P, BEZ

COL = dict(bg=lin('0E0D0B'), ivory=lin('EDE6D6'), gold=lin('C8A96A'), muted=lin('8C8574'), deep=lin('1A1814'))
DECEL, SMOOTH, EXPO = BEZ['decel'], BEZ['smooth'], BEZ['expo']
PRESETS, MASKS = [], []


def lab_bg(k, n):
    k.rect("Lab bg", 0, 0, 1920, 1080, COL['bg'], f0=0, dur=n)


def tracked_title(d):
    n = 120
    k = d.comp("ML Tracked title", n, "mtt"); lab_bg(k, n)
    t = k.text("Title", "MAISON ELAN", 960, 500, 72, COL['ivory'], f0=0, dur=n, style='Regular', align='center', track=1.8)
    t.key(t.src('text_font', 'tracking'), [(0, 1.8, 'Linear'), (60, 1.35, DECEL), (n, 1.38, 'Linear')])
    t.op([(0, 0, 'Linear'), (30, 1, 'Ease out')])
    rule = k.line("Rule", [(840, 580), (1080, 580)], COL['gold'], px=2, f0=0, dur=n)
    tp = rule.trim([(20, 0.5, 'Linear'), (50, 0.0, EXPO)], which='start')
    rule.key(tp + '.end', [(20, 0.5, 'Linear'), (50, 1.0, EXPO)])
    k.text("Tagline", "PARIS  ·  SINCE 1924", 960, 640, 28, COL['muted'], f0=40, dur=n - 40, style='Regular', align='center', track=1.5)
    PRESETS.append(("ML Tracked title", "Tagline", "Slow fade in"))


def feather_wipe(d):
    n = 75
    k = d.comp("ML Feather wipe", n, "mfw"); lab_bg(k, n)
    k.text("Headline", "Quiet confidence", 960, 540, 96, COL['ivory'], f0=0, dur=n, style='Regular', align='center')
    w = 1500
    win = k.rect("Wipe window", 960, 540, w, 400, COL['ivory'], f0=0, dur=n, center=True)
    win.soft(160)                                   # Fill soft edge: the feather of the wipe
    bx, by = win.base
    win.pos([(0, [bx - (w + 160) / 1920, by], 'Linear'), (45, [bx, by], SMOOTH)])
    MASKS.append(("ML Feather wipe", "Headline", "Wipe window"))


def product_frame(d):
    n = 120
    k = d.comp("ML Product frame", n, "mpf"); lab_bg(k, n)
    cx, cy, w, h = 960, 500, 520, 680
    fr = k.rect("Frame", cx, cy, w, h, None, f0=0, dur=n, center=True); fr.stroke(COL['gold'], 2)
    fr.trim([(0, 0.0, 'Linear'), (40, 1.0, SMOOTH)], which='end')
    prod = k.ell("Product", cx, cy, 300, 300, COL['gold'], f0=20, dur=n - 20)
    prod.gradient([(0.0, COL['ivory']), (1.0, COL['deep'])], (cx - 150, cy - 150), (cx + 150, cy + 150), mode='radial')
    PRESETS.append(("ML Product frame", "Product", "Slow fade in"))
    PRESETS.append(("ML Product frame", "Product", "Drift up - 4 s"))
    k.text("Caption", "No. 7  ·  EAU DE PARFUM", cx, cy + h / 2 + 70, 30, COL['ivory'], f0=44, dur=n - 44, style='Regular', align='center', track=1.4)
    PRESETS.append(("ML Product frame", "Caption", "Slow fade in"))


def slow_quote(d):
    n = 150
    k = d.comp("ML Slow quote", n, "msq"); lab_bg(k, n)
    q = k.text("Quote", "“Simplicity is the\nultimate sophistication.”", 960, 500, 64, COL['ivory'], f0=0, dur=n,
               style='Regular', align='center', lh=1.3)
    q.stagger(0, by='line', gap=12, dy=0.01, d=30, blur=10)
    q.key(q.src('text_font', 'tracking'), [(42, 1.0, 'Linear'), (n, 1.04, 'Linear')])   # breathe over the hold
    k.text("Author", "—  ANONYMOUS", 960, 660, 28, COL['muted'], f0=60, dur=n - 60, style='Regular', align='center', track=1.5)
    PRESETS.append(("ML Slow quote", "Author", "Slow fade in"))


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    tracked_title(d); feather_wipe(d); product_frame(d); slow_quote(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
