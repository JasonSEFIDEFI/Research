"""Exploratory DEFI-inspired linear solver pilot. See PROTOCOL.md before running."""
import os
for key in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):
    os.environ[key]='1'
import json, time, platform, sys, hashlib
from pathlib import Path
import numpy as np

OUT=Path(__file__).resolve().parent
TOL=1e-6

def op(a,b,x):
    y=x.copy()
    y[:,0]+=a*x[:,1]+b*x[:,2]
    y[:,1]+=a*x[:,0]
    y[:,2]+=b*x[:,0]
    return y

def direct(a,b,u,rmax,**kw):
    x=u.copy()
    x[:,0]=(u[:,0]-a*u[:,1]-b*u[:,2])/(1-a*a-b*b)
    x[:,1]=u[:,1]-a*x[:,0]
    x[:,2]=u[:,2]-b*x[:,0]
    return x,1,0

def cg(a,b,u,rmax,**kw):
    x=np.zeros_like(u); r=u.copy(); p=r.copy(); rr=np.sum(r*r)
    norm=np.linalg.norm(u); calls=0
    for k in range(1,4*u.size+1):
        ap=op(a,b,p); calls+=1
        alpha=rr/np.sum(p*ap); x+=alpha*p
        r-=alpha*ap; rrnew=np.sum(r*r)
        true=np.linalg.norm(op(a,b,x)-u)/norm; calls+=1
        if true<=TOL: return x,k,calls
        if rrnew==0: return x,k,calls
        p=r+(rrnew/rr)*p; rr=rrnew
    return x,k,calls

def dynamics(a,b,u,rmax,h=.1,**kw):
    x=np.zeros_like(u); v=np.zeros_like(u); norm=np.linalg.norm(u)
    c=2*np.sqrt(1-rmax); streak=0
    def force(q,w): return u-op(a,b,q)-c*w
    for k in range(1,20001):
        q1=v; w1=force(x,v)
        q2=v+h*w1/2; w2=force(x+h*q1/2,q2)
        q3=v+h*w2/2; w3=force(x+h*q2/2,q3)
        q4=v+h*w3; w4=force(x+h*q3,q4)
        x=x+h*(q1+2*q2+2*q3+q4)/6
        v=v+h*(w1+2*w2+2*w3+w4)/6
        good=(np.linalg.norm(op(a,b,x)-u)/norm<=TOL and np.linalg.norm(v)/norm<=TOL)
        streak=streak+1 if good else 0
        if streak>=5: break
    return x,k,5*k

def instance(n,rmax,seed,dtype=np.float64):
    rng=np.random.default_rng(seed); m=n//3
    angle=rng.uniform(-np.pi,np.pi,m); radius=rng.uniform(.2*rmax,rmax,m)
    return (radius*np.cos(angle)).astype(dtype),(radius*np.sin(angle)).astype(dtype),rng.normal(size=(m,3)).astype(dtype)

def reference(a,b,u):
    m=len(a); B=np.broadcast_to(np.eye(3),(m,3,3)).copy()
    B[:,0,1]=B[:,1,0]=a; B[:,0,2]=B[:,2,0]=b
    return np.linalg.solve(B,u[...,None])[...,0]

def quality(a,b,u,x,ref):
    return dict(residual=float(np.linalg.norm(op(a,b,x)-u)/np.linalg.norm(u)),
                forward_error=float(np.linalg.norm(x-ref)/np.linalg.norm(ref)))

def main():
    protocol_hash=hashlib.sha256((OUT/'PROTOCOL.md').read_bytes()).hexdigest()
    methods={'algebraic':direct,'cg':cg,'oscillator':dynamics}
    for fun in methods.values(): fun(*instance(3,.5,1),.5)
    rows=[]; diagnostics=[]
    for ni,n in enumerate([3,30,300,3000]):
      for ri,rmax in enumerate([.5,.9,.99]):
       for case in range(10):
        seed=11001+ni*3000+ri*1000+case
        t=time.perf_counter(); a,b,u=instance(n,rmax,seed); prep=time.perf_counter()-t
        t=time.perf_counter(); ref=reference(a,b,u); ref_time=time.perf_counter()-t
        samples={name:[] for name in methods}; last={}
        order_rng=np.random.default_rng(seed+500000)
        for repeat in range(3):
         for name in order_rng.permutation(list(methods)):
          t=time.perf_counter(); x,k,calls=methods[name](a.copy(),b.copy(),u.copy(),rmax)
          elapsed=time.perf_counter()-t
          samples[name].append(elapsed); last[name]=(x,k,calls)
        for name in methods:
         x,k,calls=last[name]
         rows.append(dict(n=n,rmax=rmax,seed=seed,method=name,seconds=float(np.median(samples[name])),
             repeats_seconds=samples[name],iterations=k,operator_calls=calls,
             dimensionless_duration=k*.1 if name=='oscillator' else None,
             shared_preparation_seconds=prep,reference_seconds=ref_time,**quality(a,b,u,x,ref)))
        if n==30 and case==0:
         for tag,h,dtype,bits,noise in [('half_step',.05,np.float64,None,0),('float32',.1,np.float32,None,0),
                 ('coeff8',.1,np.float64,8,0),('coeff12',.1,np.float64,12,0),('coeff16',.1,np.float64,16,0),
                 ('readout_noise',.1,np.float64,None,1e-6)]:
          aa=a.astype(dtype); bb=b.astype(dtype); uu=u.astype(dtype)
          if bits: aa=np.round(aa*2**bits)/2**bits; bb=np.round(bb*2**bits)/2**bits
          x,k,calls=dynamics(aa,bb,uu,rmax,h=h)
          if noise: x=x+np.random.default_rng(seed+777).normal(0,noise,x.shape)
          diagnostics.append(dict(n=n,rmax=rmax,seed=seed,test=tag,iterations=k,**quality(a,b,u,x,ref)))
    summary=[]; rng=np.random.default_rng(7701)
    for n in [3,30,300,3000]:
     for rmax in [.5,.9,.99]:
      subset=[r for r in rows if r['n']==n and r['rmax']==rmax]
      osc=[r for r in subset if r['method']=='oscillator']
      ratios=[]
      for o in osc:
       base=[r['seconds'] for r in subset if r['seed']==o['seed'] and r['method']!='oscillator' and r['residual']<=TOL]
       ratios.append(o['seconds']/min(base))
      boot=np.median(rng.choice(ratios,(2000,10),replace=True),axis=1)
      summary.append(dict(n=n,rmax=rmax,median_time_ratio=float(np.median(ratios)),
          ratio_ci95=np.quantile(boot,[.025,.975]).tolist(),
          median_seconds={name:float(np.median([r['seconds'] for r in subset if r['method']==name])) for name in methods},
          oscillator_passes=sum(r['residual']<=TOL and r['forward_error']<=1e-3 for r in osc),
          median_iterations={name:float(np.median([r['iterations'] for r in subset if r['method']==name])) for name in methods}))
    report=dict(protocol_sha256=protocol_hash,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        environment=dict(python=sys.version,numpy=np.__version__,platform=platform.platform(),processor=platform.processor(),
        thread_env={key:os.environ.get(key) for key in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS')}),
        cases=rows,diagnostics=diagnostics,summary=summary,
        note='Wall clock on one host. No physical energy measurements. No parameter fitting.')
    (OUT/'results.json').write_text(json.dumps(report,indent=2))
    print(json.dumps(summary,indent=2))

if __name__=='__main__': main()
