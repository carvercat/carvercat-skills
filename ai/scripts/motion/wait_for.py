"""Wait for marker files: the harness jobs here (regen_all.py, run_job.py) write <name>.done when they end, and this waits on those
files (exit 0 = all appeared, the exit code they hold is printed; 2 = timed out). Never wait with `pgrep -f`: it matches its own
command line and the shell that launched it, so it either never ends or ends at once.

    python3 wait_for.py DIR/ALL.done [DIR/other.done ...] [--timeout 3600] [--poll 5]
"""
import argparse, os, sys, time

ap = argparse.ArgumentParser()
ap.add_argument('files', nargs='+'); ap.add_argument('--timeout', type=float, default=3600); ap.add_argument('--poll', type=float, default=5)
a = ap.parse_args()
t0 = time.time()
left = list(a.files)
while left:
    for f in list(left):
        if os.path.exists(f): left.remove(f); print('%s: %s' % (f, open(f).read().strip()), flush=True)
    if left and time.time() - t0 > a.timeout:
        print('timed out waiting for: ' + ', '.join(left)); sys.exit(2)
    if left: time.sleep(a.poll)
