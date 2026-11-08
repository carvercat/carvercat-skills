"""Kept so the old command still works: verify_pack_wrap.py is now verify_pack.py.

The three corrections it added (no measuring before a clip starts, a shared background colour for the two ink masks, and
`--ink-templates` for rendered-ink text boxes) are part of verify_pack.py (see its HARNESS CORRECTIONS), and
so is `--timeout`. Same arguments:

    python3 verify_pack_wrap.py <pack> [verify_pack args] [--ink-templates 'Title A,Title B']
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verify_pack

if __name__ == '__main__':
    verify_pack.main()
