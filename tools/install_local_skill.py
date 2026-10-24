"""Install the motion skill (ai/ tree: SKILL.md, references/, patterns/, scripts/) into an agent's skill folder.

Usage: python tools/install_local_skill.py [dest]   (default ~/.codex/skills/carvercat-motion;
       Claude: ~/.claude/skills/carvercat-motion). Relative links inside the tree keep working.
"""
import hashlib, json, shutil, sys
from pathlib import Path
root = Path(__file__).resolve().parents[1]
dest = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else Path.home() / '.codex/skills/carvercat-motion'
src = root / 'ai'
receipts = []
for p in src.rglob('*'):
    if p.is_dir() or '__pycache__' in p.parts: continue
    t = dest / p.relative_to(src); t.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(p, t)
    receipts.append({'path': str(t), 'sha256': hashlib.sha256(t.read_bytes()).hexdigest()})
print(json.dumps({'destination': str(dest), 'files': len(receipts)}, indent=2))
