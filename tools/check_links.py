"""Check every relative Markdown link in the repo resolves. Usage: python tools/check_links.py"""
import os, re, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
link = re.compile(r'\]\(([^)\s#]+)(#[^)\s]*)?\)')
bad = 0
for d, dirs, files in os.walk(root):
    dirs[:] = [x for x in dirs if x not in ('.git', 'lab', 'node_modules', '__pycache__')]
    for f in files:
        if not f.endswith('.md'): continue
        p = os.path.join(d, f)
        for n, line in enumerate(open(p, encoding='utf-8'), 1):
            for m in link.finditer(line):
                t = m.group(1)
                if re.match(r'^[a-z]+:', t) or t.startswith('<'): continue
                if not os.path.exists(os.path.normpath(os.path.join(d, t))):
                    bad += 1; print(f"{os.path.relpath(p, root)}:{n}: {t}")
print(f"{bad} broken link(s)"); sys.exit(1 if bad else 0)
