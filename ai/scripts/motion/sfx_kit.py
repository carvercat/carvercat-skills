"""sfx_kit.py - synthesized motion-graphics sound effects (numpy + scipy).

Every generator returns a mono float array at 48 kHz. The design targets match
Carvercat's built-in starter SFX (attack < 2 ms, decay 40-180 ms, 0.1-0.3 s long)
and the approved pop (UPWARD pitch glide, no sub). See
ai/references/craft/sound-design.md for when to use which sound and at what level.

  pop(p)         bubble pop for things appearing (pitch-step x1.12 per repeat)
  click(p)       pointer click / button press
  tick(p)        tiny UI blip (panel builds, small reveals)
  swish(...)     airy text-reveal swish (keep ~ -20 dBFS)
  whoosh_hit()   rising air into a hard hit; place so the hit lands ON the cut
  impact()       saturated kick + snap + sub for big moments
  chime(f)/accent(f)  keyword accent (orange word, key claim)
  stretch, suck, scrub, typing, draw, sting   action-specific sounds
"""
import numpy as np
from scipy.signal import butter, sosfilt
SR=48000
rng=np.random.default_rng(7)
def t(d): return np.arange(int(d*SR))/SR
def env(d,a=0.0008,dec=0.08,curve=1.0):
    x=t(d); e=np.minimum(1,x/max(a,1e-5))*np.exp(-np.maximum(0,x-a)/dec); return e
def sweep(f0,f1,d,k=40):  # exponential glide
    x=t(d); f=f1+(f0-f1)*np.exp(-x*k); return np.sin(2*np.pi*np.cumsum(f)/SR)
def bp(x,lo,hi,o=2): return sosfilt(butter(o,[lo,hi],'band',fs=SR,output='sos'),x)
def hp(x,f,o=2): return sosfilt(butter(o,f,'high',fs=SR,output='sos'),x)
def lp(x,f,o=2): return sosfilt(butter(o,f,'low',fs=SR,output='sos'),x)
def noise(d): return rng.standard_normal(int(d*SR))
def pad(x,d):
    n=int(d*SR); y=np.zeros(n); y[:min(n,len(x))]=x[:n]; return y
def mix(*xs):
    n=max(len(x) for x in xs); y=np.zeros(n)
    for x in xs: y[:len(x)]+=x
    return y
def sat(x,drive=1.6): return np.tanh(x*drive)/np.tanh(drive)
def fade_tail(x,ms=8):
    n=int(ms/1000*SR); x=x.copy(); x[-n:]*=np.linspace(1,0,n); return x
def stereo(x,width=0.0,delay_ms=0.0):
    if width<=0: return np.stack([x,x],1)
    d=int(delay_ms/1000*SR); r=np.concatenate([np.zeros(d),x])[:len(x)]
    return np.stack([x*(1-width*0.3)+r*width*0.3, x*(1-width*0.3)+np.roll(x,d)*width*0.3],1)
def norm(x,peak_db):
    return x/np.abs(x).max()*10**(peak_db/20)

# ---------- generators ----------
def pop(p=1.0,sub=True,d=0.16):
    # bubble/mouth pop: fast UPWARD pitch glide, soft 8 ms onset, ~25 ms decay, small resonant ring, no sub
    x=t(d); f0,f1=390*p,860*p
    f=f1-(f1-f0)*np.exp(-x/0.009)
    body=np.sin(2*np.pi*np.cumsum(f)/SR)
    e=(1-np.exp(-x/0.0035))*np.exp(-x/0.024)
    ring=np.sin(2*np.pi*f1*1.0*x)*np.exp(-x/0.06)*(1-np.exp(-x/0.004))*0.12
    h2=np.sin(2*np.pi*np.cumsum(2*f)/SR)*e*0.12
    y=body*e+h2+ring
    return fade_tail(bp(y,300,4500)*1.0)
def click(p=1.0,d=0.12):
    tick=np.sin(2*np.pi*2200*p*t(d))*env(d,0.0002,0.012)
    snap=bp(noise(d),2500,9000)*env(d,0.0001,0.004)*0.8
    low=sweep(260,120,d,k=80)*env(d,0.0005,0.02)*0.7
    return fade_tail(sat(mix(tick,snap,low),1.5))
def tick(p=1.0,d=0.08):
    x=np.sin(2*np.pi*3200*p*t(d))*env(d,0.0002,0.008)+bp(noise(d),4000,12000)*env(d,0.0001,0.003)*0.4
    return fade_tail(x)
def swish(d=0.22,lo=1500,hi=9000,up=True):
    x=t(d); n=noise(d); e=np.sin(np.pi*np.clip(x/d,0,1))**(1.5)
    # moving bandpass approximated by crossfading two bands
    a=bp(n,lo,lo*2.2); b=bp(n,hi/2.5,hi)
    w=x/d if up else 1-x/d
    return fade_tail((a*(1-w)+b*w)*e)
def whoosh_hit(lead=0.32,tail=0.55,p=1.0):
    # rising noise into a hard transient at `lead` seconds
    d=lead+tail; x=t(d); n=noise(d)
    rise=np.where(x<lead,(x/lead)**2.5,np.exp(-(x-lead)/0.06))
    w=np.clip(x/lead,0,1)
    air=(bp(n,400,1800)*(1-w)+bp(n,1800,8000)*w)*rise*0.9
    k=pad(np.zeros(int(lead*SR)),lead); kk=impact(tail,p,shape=0.8)
    y=np.zeros(len(x)); y[:len(air)]+=air; s=int(lead*SR); y[s:s+len(kk)]+=kk[:len(y)-s]
    return fade_tail(sat(y,1.3))
def impact(d=0.6,p=1.0,shape=1.0):
    kick=sweep(170*p,44*p,d,k=28)*env(d,0.0006,0.18*shape)
    snap=bp(noise(0.05),1200,7000)*env(0.05,0.0002,0.012)*0.7
    sub=np.sin(2*np.pi*42*p*t(d))*env(d,0.004,0.3*shape)*0.5
    return fade_tail(sat(mix(kick,snap,sub),2.2))
def chime(f=1318.5,d=0.6,bright=1.0):
    x=t(d); y=(np.sin(2*np.pi*f*x)+0.5*np.sin(2*np.pi*f*2.0*x)*bright+0.25*np.sin(2*np.pi*f*3.01*x))*env(d,0.0006,0.16)
    return fade_tail(mix(y*0.8,pop(1.6,sub=False,d=0.15)*0.5))
def accent(f=1318.5):
    return fade_tail(mix(chime(f,0.7)*0.8,impact(0.35,1.2,0.5)*0.55))
def suck(d=0.45):
    x=t(d); n=noise(d); e=(x/d)**3
    y=(bp(n,300,1500)*(1-x/d)+bp(n,1500,7000)*(x/d))*e
    y[-int(0.004*SR):]*=np.linspace(1,0,int(0.004*SR)); return y
def stretch(d=0.3):
    return mix(swish(d,600,5000,True)*0.9, sweep(220,90,d,k=10)*env(d,0.02,0.12)*0.5)
def scrub(n=8,gap=0.035,p=1.0):
    d=n*gap+0.08; y=np.zeros(int(d*SR))
    for i in range(n):
        s=int(i*gap*SR); c=tick(p*(1+0.03*i),0.05)*(0.6+0.4*np.sin(np.pi*i/n)); y[s:s+len(c)]+=c
    return y
def typing(n=10,gap=0.05):
    d=n*gap+0.1; y=np.zeros(int(d*SR))
    for i in range(n):
        g=gap*(0.8+0.4*rng.random()); s=int(sum([gap]*i)*SR)
        c=click(0.8+0.3*rng.random(),0.06)*(0.5+0.3*rng.random()); y[s:s+len(c)]+=c
    return y
def draw(d=0.85):
    x=t(d); f=380*np.exp(np.log(1400/380)*x/d)
    y=np.sin(2*np.pi*np.cumsum(f)/SR)*np.sin(np.pi*x/d)**0.7*0.5+swish(d,2000,9000,True)*0.4
    return fade_tail(y)
def sting():
    d=2.2; x=t(d); ch=[523.25,659.25,783.99,1046.5]
    pad_=sum(np.sin(2*np.pi*f*x)*(1+0.3*np.sin(2*np.pi*5*x)) for f in ch)*env(d,0.003,0.7)*0.25
    return fade_tail(mix(impact(1.2,0.9,1.4),pad_,chime(1567.98,1.2)*0.5))
