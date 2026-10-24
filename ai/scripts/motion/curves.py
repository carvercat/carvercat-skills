"""Motion curves as plain functions of t in [0,1] -> progress (may overshoot).

Agent-neutral and dependency-free. Used to bake exact curves into keyframes
for tools that only offer a few named easings (Carvercat presets, Fusion
spline defaults, Lottie, CSS keyframes...).

    bezier(x1, y1, x2, y2)      CSS-style cubic-bezier
    spring(zeta, frames)        damped spring that settles inside `frames`
    spring_physics(m, k, c, fps) -> (curve, settle_frames)   Remotion-style params
    bounce()                    ease-out bounce (3 hits)
    named[...]                  the vocabulary used in references/craft/motion-principles.md

bake(curve, frames, tol) -> [(at, progress)] keeps only the keys needed so a
LINEAR join of them stays within `tol` of the true curve (Douglas-Peucker on
per-frame samples). Linear joins are deliberate: they reproduce any curve in
any tool that supports keyframes at all.
"""
import math


def bezier(x1, y1, x2, y2):
    def bx(s): return 3*x1*s*(1-s)**2 + 3*x2*s*s*(1-s) + s**3
    def by(s): return 3*y1*s*(1-s)**2 + 3*y2*s*s*(1-s) + s**3
    def f(t):
        if t <= 0: return 0.0
        if t >= 1: return 1.0
        lo, hi = 0.0, 1.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if bx(mid) < t: lo = mid
            else: hi = mid
        return by((lo + hi) / 2)
    return f


def _simulate(zeta, omega, T, steps=4000):
    """x'' = -w^2 (x-1) - 2 z w x', x(0)=0, x'(0)=0. Returns samples over [0,T]."""
    dt = T / steps
    x, v, out = 0.0, 0.0, [0.0]
    for _ in range(steps):
        a = -omega*omega*(x - 1) - 2*zeta*omega*v
        v += a*dt; x += v*dt          # semi-implicit Euler, stable at this dt
        out.append(x)
    return out


def spring_physics(mass=1.0, stiffness=100.0, damping=10.0, fps=30, settle=0.005, max_s=4.0):
    """Remotion/Framer-style spring. Returns (curve over its own settle time, settle_frames)."""
    omega = math.sqrt(stiffness / mass)
    zeta = damping / (2 * math.sqrt(stiffness * mass))
    xs = _simulate(zeta, omega, max_s)
    n = len(xs) - 1
    last = 0
    for i, x in enumerate(xs):
        if abs(x - 1) > settle: last = i
    settle_s = max_s * last / n
    frames = max(2, math.ceil(settle_s * fps))
    T = frames / fps
    def f(t):
        if t >= 1: return 1.0
        i = t * T / max_s * n
        a = int(i); b = min(a + 1, n)
        return xs[a] + (xs[b] - xs[a]) * (i - a)
    return f, frames


def spring(zeta=0.5, frames=24, settle=0.005):
    """A spring with damping ratio `zeta` that reaches within `settle` of 1 at t=1."""
    # find omega so the envelope e^{-z w t} reaches settle at T=1
    zeta = max(0.05, zeta)
    omega = max(4.0, -math.log(settle) / zeta) if zeta < 1 else 9.0
    xs = _simulate(zeta, omega, 1.0)
    n = len(xs) - 1
    def f(t):
        if t <= 0: return 0.0
        if t >= 1: return 1.0
        i = t * n; a = int(i); b = min(a + 1, n)
        return xs[a] + (xs[b] - xs[a]) * (i - a)
    return f


def bounce():
    def f(t):
        n1, d1 = 7.5625, 2.75
        if t < 1/d1: return n1*t*t
        if t < 2/d1: t -= 1.5/d1; return n1*t*t + .75
        if t < 2.5/d1: t -= 2.25/d1; return n1*t*t + .9375
        t -= 2.625/d1; return n1*t*t + .984375
    return f


def anticipate_out(back=0.08):
    """Exit with a small wind-up: dips to -back then accelerates out (ease-in)."""
    acc = bezier(0.3, 0, 0.8, 0.15)
    def f(t):
        if t < 0.3: return -back * math.sin(t / 0.3 * math.pi / 2)
        u = (t - 0.3) / 0.7
        return -back + (1 + back) * acc(u)
    return f


named = {
    "linear":            lambda t: t,
    "expo-out":          bezier(0.16, 1, 0.3, 1),
    "emphasized-decel":  bezier(0.05, 0.7, 0.1, 1),
    "standard":          bezier(0.2, 0, 0, 1),
    "emphasized-accel":  bezier(0.3, 0, 0.8, 0.15),
    "expressive-in":     bezier(0, 0, 0.3, 1),
    "accel":             bezier(0.4, 0.14, 1, 1),
    "s-curve":           bezier(0.65, 0, 0.35, 1),
    "spring-bouncy":     spring(0.5),    # ~16% overshoot (Remotion default feel)
    "spring-gentle":     spring(0.7),    # ~4.6% overshoot
    "spring-wobbly":     spring(0.35),   # ~31% overshoot, 2-3 visible wobbles
    "spring-critical":   spring(1.0),    # no overshoot, physical settle
    "bounce":            bounce(),
    "anticipate-out":    anticipate_out(),
}


def bake(curve, frames, tol=0.006):
    """Per-frame samples reduced to the keys a LINEAR join needs. Returns [(at, p)]."""
    n = max(2, int(round(frames)))
    pts = [(i / n, curve(i / n)) for i in range(n + 1)]
    keep = {0, n}
    def rdp(a, b):
        (ta, pa), (tb, pb) = pts[a], pts[b]
        worst, wi = 0.0, None
        for i in range(a + 1, b):
            t, p = pts[i]
            lin = pa + (pb - pa) * (t - ta) / (tb - ta)
            if abs(p - lin) > worst: worst, wi = abs(p - lin), i
        if wi is not None and worst > tol:
            keep.add(wi); rdp(a, wi); rdp(wi, b)
    rdp(0, n)
    return [pts[i] for i in sorted(keep)]


def stats(curve, n=400):
    ys = [curve(i / n) for i in range(n + 1)]
    peak = max(ys)
    return {"overshoot_pct": round(max(0.0, peak - 1) * 100, 1),
            "undershoot_pct": round(max(0.0, -min(ys)) * 100, 1),
            "t90": next(i / n for i, y in enumerate(ys) if y >= 0.9)}


if __name__ == "__main__":
    for k, c in named.items():
        print(f"{k:18s}", stats(c), len(bake(c, 18)), "keys @18f")
    f, fr = spring_physics(1, 100, 10); print("remotion default spring settles in", fr, "f", stats(f))
    f, fr = spring_physics(1, 100, 200); print("damping 200 settles in", fr, "f", stats(f))
