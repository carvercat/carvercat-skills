"""Run one long harness command detached from your shell, with a log and a marker file.

    python3 run_job.py DIR NAME -- python3 verify_pack.py glitch --out DIR/verify-glitch

Starts the command in the background (its output goes to DIR/NAME.log) and returns at once. When the command ends, DIR/NAME.done holds
its exit code. Wait with `python3 wait_for.py DIR/NAME.done`. Jobs that share the host run one after another: start the next
one after the first one's marker is there.
"""
import os, subprocess, sys

if '--' not in sys.argv or len(sys.argv) < 5: sys.exit(__doc__)
i = sys.argv.index('--')
d, name, cmd = sys.argv[1], sys.argv[2], sys.argv[i + 1:]
os.makedirs(d, exist_ok=True)
done = os.path.join(d, name + '.done')
if os.path.exists(done): os.remove(done)
script = 'import subprocess,sys; rc=subprocess.call(sys.argv[3:], stdout=open(sys.argv[1],"w"), stderr=subprocess.STDOUT); open(sys.argv[2],"w").write(str(rc))'
subprocess.Popen([sys.executable, '-c', script, os.path.join(d, name + '.log'), done] + cmd, start_new_session=True,
                 stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print('started %s -> %s.log / %s' % (name, os.path.join(d, name), done))
