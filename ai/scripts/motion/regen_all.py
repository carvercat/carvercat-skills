"""Regenerate every design-unit pack of this checkout (templates, lab and showcase projects, showcase-2 projects) in one serial run
and say whether anything changed.

    CARVERCAT_HOST=/path/to/carvercat-host CARVERCAT_RESOURCE_ROOT=/path/to/the-app-resource-folder \
        python3 regen_all.py [--only pack ...] [--out DIR] [--no-showcase2]

For each pack it runs regen_pack.py for the lab modules (round 1, 2, 3: templates + `--keep` project) and the showcase (project
only), then regen_showcase2.py for the packs' showcase-2 projects. Jobs run ONE AT A TIME (the host is heavy); each writes
<out>/<job>.log and, when it ends, <out>/<job>.done holding the exit code, and the run ends with <out>/ALL.done: wait on those
marker files (see `wait_for.py`), never on `pgrep -f`. Afterwards `git status --short library categories` shows what changed: after a
run on the same host the answer must be nothing (the chain is deterministic).
"""
import argparse, os, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
# pack folder -> (lab module prefix, category folder, project id prefix); the labs are <prefix>_lab, _lab2, _lab3 and _showcase
PACKS = {
    'cartoon-bounce': ('cartoon_bounce', 'cartoon-bounce', 'ct'),
    'corporate-brand': ('corporate_brand', 'corporate-brand', 'cb'),
    'data-viz': ('data_viz', 'data-viz', 'dv'),
    'explainer': ('explainer', 'explainer', 'ex'),
    'funky': ('funky', 'funky', 'fk'),
    'futuristic-hud': ('futuristic_hud', 'futuristic-hud', 'fh'),
    'glitch': ('glitch', 'glitch', 'gl'),
    'kinetic-typography': ('kinetic_type', 'kinetic-typography', 'kt'),
    'minimal-luxury': ('minimal_luxury', 'minimal-luxury', 'ml'),
    'retro': ('retro', 'retro', 'rt'),
    'saas-ui': ('saas_ui', 'saas-launch', 'saas-ui'),
    'social-short-form': ('social_short_form', 'social-media-reels', 'ss'),
    'sports': ('sports', 'sports', 'sp'),
}


def jobs(only):
    out = []
    cat = lambda c, p: os.path.join(REPO, 'categories', c, p, 'project.carverproj')
    if not only or 'transitions' in only:
        out += [('transitions-lab', ['transitions_lab', '--pack', 'transitions', '--keep', cat('transitions', 'tx-lab')]),
                ('transitions-showcase', ['transitions_showcase', '--pack', 'transitions', '--no-templates', '--keep', cat('transitions', 'tx-showcase')])]
    if not only or 'motion-patterns' in only:
        out += [('motion-patterns-lab', ['motion_patterns_lab', '--pack', 'motion-patterns', '--keep', cat('motion-patterns', 'pattern-lab')])]
    for pack, (mod, c, pid) in PACKS.items():
        if only and pack not in only: continue
        for suffix, proj in (('lab', pid + '-lab'), ('lab2', pid + '-lab-2'), ('lab3', pid + '-lab-3')):
            out.append(('%s-%s' % (pack, suffix), ['%s_%s' % (mod, suffix), '--pack', pack, '--keep', cat(c, proj)]))
        out.append(('%s-showcase' % pack, ['%s_showcase' % mod, '--pack', pack, '--no-templates', '--keep', cat(c, pid + '-showcase')]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only', nargs='*', default=None); ap.add_argument('--out', default='/tmp/regen-all')
    ap.add_argument('--no-showcase2', action='store_true')
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    for f in os.listdir(a.out):
        if f.endswith('.done'): os.remove(os.path.join(a.out, f))
    bad = []
    todo = [(n, [sys.executable, os.path.join(HERE, 'regen_pack.py')] + args) for n, args in jobs(a.only)]
    if not a.no_showcase2:
        keys = [p for p in PACKS] if not a.only else [p for p in PACKS if p in a.only]
        if keys: todo.append(('showcase2', [sys.executable, os.path.join(HERE, 'regen_showcase2.py')] + keys))
    for name, cmd in todo:
        t0 = time.time()
        with open(os.path.join(a.out, name + '.log'), 'w') as log:
            rc = subprocess.call(cmd, stdout=log, stderr=subprocess.STDOUT, cwd=HERE)
        open(os.path.join(a.out, name + '.done'), 'w').write(str(rc))
        print('%-30s exit %d  %.0fs' % (name, rc, time.time() - t0), flush=True)
        if rc: bad.append(name)
    open(os.path.join(a.out, 'ALL.done'), 'w').write(','.join(bad) or 'ok')
    print('FAILED: ' + ', '.join(bad) if bad else 'all jobs ran')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
