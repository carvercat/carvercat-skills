"""SaaS UI round 2: seven more lab comps (lower third, feature title, CTA end card, modal,
chart card, chat thread, dropdown menu), written straight into a .carverproj.

    import saas_ui_lab2 as L; presets, masks = L.build(PROJECT.carverproj)

Same palette, curves and verification as saas_ui_lab.py. After writing: edit.open
{path, force:true}; apply PRESETS (preset.apply); edit.save; check with carvercat_inspect
and carvercat_look; extract templates with comp_to_template.py (--drop "Lab bg").
Fonts: Rethink Sans must be installed (KI-136). Docs: ai/patterns/saas-ui.md.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from saas_ui_lab import Doc, lin, P, COL, EXPO, SMOOTH, lab_bg

BACK = (0.34, 1.56, 0.64, 1)
PRESETS, MASKS = [], []


def lower_third(d):
    n = 150
    k = d.comp("SU Lower third", n, "slt"); lab_bg(k, n)
    x, y = 120, 860
    pill = k.rect("Pill", x + 340, y, 680, 104, COL['card'], r=52, f0=0, dur=n, center=True)
    pill.anchor(-1, 0); pill.scale([(0, [0.0, 1.0], 'Linear'), (14, [1.0, 1.0], EXPO)])
    pill.shadow(y=-0.004, soft=0.02, op=0.25)
    chip = k.ell("Logo chip", x + 52, y, 72, 72, COL['accent'], f0=4, dur=n - 4)
    PRESETS.append(("SU Lower third", "Logo chip", "Pop - gentle"))
    k.text("Name", "Priya Shah", x + 108, y - 21, 34, COL['ink'], f0=8, dur=n - 8, style='Bold')
    PRESETS.append(("SU Lower third", "Name", "Card lift"))
    k.text("Role", "Product lead, Acme", x + 108, y + 26, 26,   # audit 2026-10-28: 11.6 px gap to the name before
           COL['muted'], f0=11, dur=n - 11, style='Medium')
    PRESETS.append(("SU Lower third", "Role", "Card lift"))
    for o in ("Pill", "Logo chip", "Name", "Role"):
        PRESETS.append(("SU Lower third", o, "Modal dismiss"))


def feature_title(d):
    n = 90
    k = d.comp("SU Feature title", n, "sft"); lab_bg(k, n)
    tag = k.rect("Eyebrow tag", 960, 380, 220, 52, COL['accent'], r=26, f0=0, dur=n, center=True)
    PRESETS.append(("SU Feature title", "Eyebrow tag", "Pop - gentle"))
    k.text("Eyebrow", "NEW", 960, 380, 30, COL['card'], f0=2, dur=n - 2, style='Bold', align='center', track=1.4)
    PRESETS.append(("SU Feature title", "Eyebrow", "Card lift"))   # text pops from 94%, not 60%: lint text size
    k.text("Headline", "Reports that write themselves", 960, 500, 84, COL['card'], f0=6, dur=n - 6, style='Bold', align='center')
    PRESETS.append(("SU Feature title", "Headline", "Words rise - expo"))
    k.text("Subline", "Every Monday, in your inbox.", 960, 600, 38, COL['muted'], f0=18, dur=n - 18, style='Medium', align='center')
    PRESETS.append(("SU Feature title", "Subline", "Card lift"))
    ul = k.rect("Underline", 960, 660, 420, 8, COL['accent'], r=4, f0=24, dur=n - 24, center=True)
    ul.scale([(24, [0.0, 1.0], 'Linear'), (38, [1.0, 1.0], EXPO)])       # grows from its centre
    ul.gradient([(0.0, COL['accent']), (1.0, lin('B07CFF'))], (750, 660), (1170, 660))


def cta_end_card(d):
    n = 120
    k = d.comp("SU CTA end card", n, "sec"); lab_bg(k, n)
    mark = k.rect("Logo mark", 960, 400, 140, 140, COL['accent'], r=36, f0=0, dur=n, center=True)
    PRESETS.append(("SU CTA end card", "Logo mark", "Pop - spring"))
    k.text("Wordmark", "Acme", 960, 530, 72, COL['card'], f0=8, dur=n - 8, style='Bold', align='center')
    PRESETS.append(("SU CTA end card", "Wordmark", "Card lift"))
    k.text("Tagline", "Ship faster. Sleep better.", 960, 610, 36, COL['muted'], f0=14, dur=n - 14, style='Medium', align='center')
    PRESETS.append(("SU CTA end card", "Tagline", "Card lift"))
    btn = k.rect("Button", 960, 720, 360, 84, COL['card'], r=42, f0=22, dur=n - 22, center=True)
    PRESETS.append(("SU CTA end card", "Button", "Pop - gentle"))
    k.text("Button label", "Start free trial", 960, 720, 32, COL['ink'], f0=24, dur=n - 24, style='Bold', align='center')
    PRESETS.append(("SU CTA end card", "Button label", "Card lift"))
    k.text("URL", "acme.app", 960, 820, 28, COL['muted'], f0=30, dur=n - 30, style='Medium', align='center', track=1.2)
    PRESETS.append(("SU CTA end card", "URL", "Card lift"))


def modal(d):
    n = 90
    k = d.comp("SU Modal", n, "smd")
    k.rect("App canvas", 0, 0, 1920, 1080, lin('F4F5F8'), f0=0, dur=n)
    for i in range(3):
        k.rect(f"App card {i + 1}", 120 + i * 580, 160, 520, 340, COL['card'], r=20, f0=0, dur=n)
    scrim = k.rect("Scrim", 0, 0, 1920, 1080, COL['ink'], f0=0, dur=n)
    scrim.op([(6, 0.0, 'Linear'), (20, 0.45, EXPO), (70, 0.45, 'Linear'), (82, 0.0, BEZ_ACCEL)])
    card = k.rect("Modal", 960, 540, 640, 360, COL['card'], r=28, f0=8, dur=n - 8, center=True)
    card.shadow(y=-0.006, soft=0.03, op=0.3)
    k.text("Modal title", "Delete project?", 700, 440, 40, COL['ink'], f0=10, dur=n - 10, style='Bold')
    k.text("Modal body", "This cannot be undone.", 700, 500, 28, COL['muted'], f0=12, dur=n - 12, style='Medium')
    k.rect("Cancel", 1000, 620, 160, 64, lin('E6E8EF'), r=32, f0=14, dur=n - 14, center=True)
    k.text("Cancel label", "Cancel", 1000, 620, 30, COL['ink'], f0=14, dur=n - 14, style='Bold', align='center')
    k.rect("Delete", 1170, 620, 160, 64, lin('E5484D'), r=32, f0=16, dur=n - 16, center=True)
    k.text("Delete label", "Delete", 1170, 620, 30, COL['card'], f0=16, dur=n - 16, style='Bold', align='center')
    for o in ("Modal", "Modal title", "Modal body", "Cancel", "Cancel label", "Delete", "Delete label"):
        PRESETS.append(("SU Modal", o, "Card lift"))
        PRESETS.append(("SU Modal", o, "Modal dismiss"))


def chart_card(d):
    n = 90
    k = d.comp("SU Chart card", n, "scc"); lab_bg(k, n)
    card = k.rect("Chart card", 960, 540, 640, 400, COL['card'], r=28, f0=0, dur=n, center=True)
    card.shadow(y=-0.004, soft=0.02, op=0.22)
    PRESETS.append(("SU Chart card", "Chart card", "Card lift"))
    k.text("Chart title", "Weekly active users", 680, 390, 30, COL['ink'], f0=4, dur=n - 4, style='Bold')
    PRESETS.append(("SU Chart card", "Chart title", "Card lift"))
    vals = [38, 52, 47, 66, 74, 88, 96]
    for i, v in enumerate(vals):
        h = 200 * v / 100; x = 700 + i * 82
        b = k.rect(f"Bar {i + 1}", x, 680 - h / 2, 48, h, COL['accent'] if i == len(vals) - 1 else lin('C9CCF9'), r=10,
                   f0=10 + i * 3, dur=n - 10 - i * 3, center=True)
        b.anchor(0, -1)
        PRESETS.append(("SU Chart card", f"Bar {i + 1}", "Bar grow up - spring"))
    k.text("Chart delta", "+18%", 1240, 390, 30, lin('16A34A'), f0=34, dur=n - 34, style='Bold', align='right')
    PRESETS.append(("SU Chart card", "Chart delta", "Card lift"))


def chat_thread(d):
    n = 120
    k = d.comp("SU Chat thread", n, "sct"); lab_bg(k, n)
    msgs = [("left", "Can we ship on Friday?", 0), ("right", "Tests are green. Yes.", 26), ("left", "Amazing, thank you!", 52)]
    for i, (side, text, f) in enumerate(msgs):
        y = 380 + i * 150; w = 560
        x = 520 if side == "left" else 1400
        col = COL['card'] if side == "left" else COL['accent']
        bub = k.rect(f"Bubble {i + 1}", x, y, w, 104, col, r=40, f0=f, dur=n - f, center=True)
        bub.anchor(-1 if side == "left" else 1, -1)                     # grows from the tail corner
        bub.scale([(f, 0.0, 'Linear'), (f + 12, 1.0, BACK)])
        bub.op([(f, 0.0, 'Linear'), (f + 3, 1.0, 'Linear')])
        k.text(f"Message {i + 1}", text, x, y, 32, COL['ink'] if side == "left" else COL['card'], f0=f + 5, dur=n - f - 5,
               style='Medium', align='center')
        PRESETS.append(("SU Chat thread", f"Message {i + 1}", "Card lift"))


def dropdown(d):
    n = 90
    k = d.comp("SU Dropdown", n, "sdd"); lab_bg(k, n)
    btn = k.rect("Menu button", 960, 300, 360, 72, COL['card'], r=16, f0=0, dur=n, center=True)
    k.text("Menu button label", "Sort by: Newest", 820, 300, 28, COL['ink'], f0=0, dur=n, style='Bold')
    panel = k.rect("Menu panel", 960, 352 + 4 * 64 / 2 + 12, 360, 4 * 64 + 24, COL['card'], r=16, f0=8, dur=n - 8, center=True)
    panel.anchor(0, 1); panel.scale([(8, [1.0, 0.0], 'Linear'), (20, [1.0, 1.0], EXPO)])   # unfolds downward from its top edge
    panel.shadow(y=-0.004, soft=0.02, op=0.25)
    hl = k.rect("Hover", 960, 396 + 2 * 64, 336, 52, lin('EEF0FE'), r=12, f0=40, dur=n - 40, center=True)
    hl.op([(40, 0.0, 'Linear'), (46, 1.0, 'Ease out')])                      # under the items: made before them
    for i, t in enumerate(["Newest", "Oldest", "Most popular", "Alphabetical"]):
        f = 12 + i * 3
        k.text(f"Item {i + 1}", t, 820, 396 + i * 64, 28, COL['ink'] if i else COL['accent'], f0=f, dur=n - f, style='Medium')
        PRESETS.append(("SU Dropdown", f"Item {i + 1}", "Card lift"))


BEZ_ACCEL = (0.3, 0.0, 0.8, 0.15)


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    lower_third(d); feature_title(d); cta_end_card(d); modal(d); chart_card(d); chat_thread(d); dropdown(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
