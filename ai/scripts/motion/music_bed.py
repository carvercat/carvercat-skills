"""music_bed.py - one-file, beat-driven promo music bed (C major vi-IV-I-V, 4-on-the-floor,
claps, offbeat bass, 3-3-2 pluck hook, sidechain pump, risers), ducked under the VO.

  python music_bed.py --frames 1125 --downbeat 18 --drop 198 --lift 853 --outro 972 \\
         --stab 1062 --vo VO.wav --vo-at 12 --out music.wav

Pick --downbeat so the main cut (--drop) lands on a bar: (drop-downbeat) % (4*60/bpm*fps) == 0.
Synthesized: a placeholder-quality bed. Swap in licensed music for final delivery if wanted.
"""
import numpy as np,wave,os
from sfx_kit import *
import argparse
_ap=argparse.ArgumentParser(description='Beat-driven promo music bed (one file), ducked under a VO.')
_ap.add_argument('--frames',type=int,required=True,help='comp length in frames')
_ap.add_argument('--fps',type=float,default=30)
_ap.add_argument('--bpm',type=float,default=120)
_ap.add_argument('--downbeat',type=int,default=0,help='frame of the first downbeat; choose it so the main drop lands on a bar')
_ap.add_argument('--drop',type=int,required=True,help='frame where the full groove starts (first big cut)')
_ap.add_argument('--lift',type=int,default=None,help='frame of a second lift (e.g. CTA scene), riser before it')
_ap.add_argument('--outro',type=int,default=None,help='frame where the outro (half-time) starts')
_ap.add_argument('--stab',type=int,default=None,help='frame of the final chord stab')
_ap.add_argument('--vo',default=None,help='VO wav for ducking'); _ap.add_argument('--vo-at',type=float,default=0,help='VO start frame')
_ap.add_argument('--duck-db',type=float,default=6); _ap.add_argument('--gain-db',type=float,default=-6)
_ap.add_argument('--out',default='music_bed.wav')
A=_ap.parse_args()
FPS=A.fps; BPM=A.bpm; BEAT=60/BPM; T0=A.downbeat/FPS
TOTAL=A.frames/FPS+1.0; N=int(TOTAL*SR)
L=np.zeros(N); R=np.zeros(N)
def add(x,tsec,g=1.0,pan=0.0):
    s=int(tsec*SR)
    if s>=N or s+len(x)<=0: return
    if s<0: x=x[-s:]; s=0
    e=min(N,s+len(x)); L[s:e]+=x[:e-s]*g*(1-max(0,pan)); R[s:e]+=x[:e-s]*g*(1+min(0,pan))
fr=lambda f:f/FPS
def kick():
    d=0.35; return sat(mix(sweep(150,48,d,k=32)*env(d,0.0005,0.14),bp(noise(0.01),2000,8000)*env(0.01,0.0001,0.002)*0.3),2.5)
def clap():
    d=0.25; n=noise(d); e=np.zeros(int(d*SR))
    for o in [0,0.008,0.016]: s=int(o*SR); e[s:]+=env(d-o,0.0003,0.012 if o<0.016 else 0.07)[:len(e)-s]
    return bp(n,900,6000)*e*0.9
def hat(open_=False):
    d=0.25 if open_ else 0.05; return hp(noise(d),7000)*env(d,0.0002,0.08 if open_ else 0.012)*0.5
def bass(f,d):
    x=t(d); y=sat(np.sin(2*np.pi*f*x)+0.4*np.sin(2*np.pi*2*f*x)+0.15*np.sign(np.sin(2*np.pi*f*x)),1.8)
    return y*env(d,0.003,d*0.6)
def pluck(f,d=0.3):
    x=t(d); saw=sum((-1)**(k+1)*np.sin(2*np.pi*f*k*x)/k for k in range(1,9))
    return lp(saw,3500)*env(d,0.001,0.09)
def chord_stab(fs,d=0.35): return sum(pluck(f,d) for f in fs)/len(fs)
def padv(fs,d):
    x=t(d); y=sum(np.sin(2*np.pi*f*x+0.3*np.sin(2*np.pi*0.3*x))+0.3*np.sin(2*np.pi*f*1.003*x) for f in fs)/len(fs)
    a=np.minimum(1,x/0.4)*np.minimum(1,(d-x)/0.3); return y*a
def riser(d):
    x=t(d); f=200*np.exp(np.log(3000/200)*x/d); return (hp(noise(d),1500)*(x/d)**2*0.4+np.sin(2*np.pi*np.cumsum(f)/SR)*(x/d)**3*0.15)
# progression (C major, catchy vi-IV-I-V): Am F C G
CH=[[220,261.63,329.63],[174.61,220,261.63],[196,261.63,329.63],[196,246.94,293.66]]
ROOT=[55,43.65,65.41,49]
def bar_t(b): return T0+b*4*BEAT
nbars=int((TOTAL-T0)/(4*BEAT))+1
DROP1=fr(A.drop); DOWNLOAD=fr(A.lift) if A.lift else None; OUTRO=fr(A.outro) if A.outro else TOTAL+10
side=np.ones(N)  # sidechain pump
for b in range(-1,nbars):
    bt=bar_t(b); ci=b%4; ch=CH[ci]
    for be in range(4):
        tb=bt+be*BEAT
        if tb<0 or tb>TOTAL-0.3: continue
        intro=tb<DROP1; outro=tb>=OUTRO
        # drums
        if not intro or (tb>fr(150) and be%2==0):
            if not (outro and be%2==1):
                add(kick(),tb,0.95)
                s=int(tb*SR); n=int(0.22*SR); e=min(N,s+n); side[s:e]=np.minimum(side[s:e],1-0.55*np.exp(-np.arange(e-s)/SR/0.08))
        if not intro and be in(1,3) and not outro: add(clap(),tb,0.55)
        if not intro:
            add(hat(),tb+BEAT/2,0.35,0.3); 
            if be==3: add(hat(True),tb+BEAT/2,0.25,-0.3)
            add(hat(),tb+BEAT/4,0.15,-0.2); add(hat(),tb+3*BEAT/4,0.15,0.2)
        # bass offbeat 8ths
        if not intro and not outro:
            add(bass(ROOT[ci],BEAT/2*0.9),tb+BEAT/2,0.55)
            add(bass(ROOT[ci],BEAT/2*0.6),tb,0.35)
        # plucks: catchy rhythm 3-3-2 per bar
        for off in ([0,0.75,1.5,2,2.75,3.5] if not intro else [0,1.5,3]):
            if abs(off-be)<1e-6 or (be<off<be+1):
                pass
    # pluck pattern per bar
    for off,step in [(0,0),(0.75,1),(1.5,2),(2.0,1),(2.75,0),(3.5,2)]:
        tt=bt+off*BEAT
        if tt<0 or tt>TOTAL-0.3: continue
        intro=tt<DROP1; outro=tt>=OUTRO+4*BEAT
        if intro and off not in (0,1.5,3.5): continue
        f=ch[step]*2; g=0.22 if intro else 0.3
        if outro: g*=0.6
        add(pluck(f,0.28),tt,g,0.25 if step==1 else -0.25)
    if bt>=0: add(padv([c for c in ch],4*BEAT+0.3),bt,0.18 if bt<DROP1 else 0.12)
# risers and hits
add(riser(1.6),DROP1-1.6,0.7)
if DOWNLOAD: add(riser(1.0),DOWNLOAD-1.0,0.5)
if A.outro: add(riser(1.2),OUTRO-1.2,0.6)
# outro final chord stab + tail
if A.stab: add(chord_stab([261.63*2,329.63*2,392*2],0.9),fr(A.stab),0.5)
L*=side; R*=side
mus=np.stack([L,R],1)
mus[:int(0.02*SR)]*=np.linspace(0,1,int(0.02*SR))[:,None]
fe=int(1.2*SR); mus[-fe:]*=np.linspace(1,0,fe)[:,None]
mus=mus/np.abs(mus).max()*10**(-1/20)
# VO duck: follow the VO envelope, -6 dB under speech
def rd(p):
  w=wave.open(p); ch=w.getnchannels(); x=np.frombuffer(w.readframes(w.getnframes()),'<i2').astype(float)/32768; return x.reshape(-1,ch).mean(1)
if A.vo:
    vo=rd(A.vo); off=int(fr(A.vo_at)*SR)
    v=np.zeros(N); v[off:off+len(vo)]=np.abs(vo)[:max(0,N-off)]
    win=int(0.12*SR); envv=np.convolve(v,np.ones(win)/win,'same'); envv=envv/max(envv.max(),1e-9)
    duck=1-(1-10**(-A.duck_db/20))*np.clip(envv*4,0,1)
    k=int(0.15*SR); duck=np.convolve(duck,np.ones(k)/k,'same')
    mus*=duck[:,None]
mus*=10**(A.gain_db/20)
with wave.open(A.out,'wb') as w: w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((np.clip(mus,-1,1)*32767).astype('<i2').tobytes())
print('music',len(mus)/SR,'s')
