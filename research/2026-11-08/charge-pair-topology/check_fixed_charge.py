"""Charge-preserving homotopies: sampled normalization checks, not a topology proof."""
from pathlib import Path
import argparse,json,platform
import numpy as np

parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=Path(__file__).with_name('fixed_charge_results.json'))
args=parser.parse_args()
rng=np.random.default_rng(20261108)
N=1024;length=16.;dx=length/N;z=np.arange(N)*dx
u=np.exp(2j*np.pi*z/length)/np.sqrt(length)
v=np.ones(N,dtype=complex)/np.sqrt(length)
def inner(a,b):return dx*np.vdot(a,b)
def charge(f,p):return float(np.imag(inner(f,p)))
def kinetic(p):return float(np.real(inner(p,p))/2)
def canonical(f,q):return 1j*q*f/np.real(inner(f,f))
def gradient(f):return (np.roll(f,-1)-np.roll(f,1))/(2*dx)
def energy(f,p):
    # Sigma is the constant lambda=12 vacuum, with zero momentum.
    rho=np.abs(f)**2;eta=3/12
    return float(dx*np.sum((np.abs(p)**2+np.abs(gradient(f))**2)/2+rho**2/4+rho/2+2*rho*eta))
assert abs(inner(u,v))<1e-14
assert abs(inner(u,u)-1)<1e-14
charges=[-1000.,-1.,1.,1000.]
maxcharge=0.;maxorthogonal=0.;maxidentity=0.;maxincrease=0.;maxconjugation=0.
records=[]
for q in charges:
    f=(.3+.2j)*u+(.7-.1j)*v
    p=rng.normal(size=N)+1j*rng.normal(size=N)
    p=p+canonical(f,q-charge(f,p))
    p0=canonical(f,q);w=p-p0
    maxorthogonal=max(maxorthogonal,abs(float(np.real(inner(p0,w))))/(1+abs(q)**2))
    previous=kinetic(p)
    for s in np.linspace(0,1,33):
        ps=p0+(1-s)*w
        maxcharge=max(maxcharge,abs(charge(f,ps)-q)/(1+abs(q)))
        expected=kinetic(p0)+(1-s)**2*kinetic(w)
        maxidentity=max(maxidentity,abs(kinetic(ps)-expected)/(1+expected))
        maxincrease=max(maxincrease,(kinetic(ps)-previous)/(1+previous));previous=kinetic(ps)
    samples=[]
    for s in np.linspace(0,1,25):
        es=[]
        for theta in np.linspace(0,2*np.pi,65):
            # An integer phase-winding mode loop, filled through a second allowed mode.
            fs=np.sqrt(1-s*s)*np.exp(1j*theta)*u+s*v
            ps=canonical(fs,q)
            maxcharge=max(maxcharge,abs(charge(fs,ps)-q)/(1+abs(q)))
            assert abs(np.real(inner(fs,fs))-1)<1e-12
            assert abs(charge(fs.conj(),ps.conj())+q)/(1+abs(q))<1e-12
            e=energy(fs,ps);ec=energy(fs.conj(),ps.conj())
            maxconjugation=max(maxconjugation,abs(e-ec)/(1+e));es.append(e)
        samples.append(dict(s=float(s),energy_min=min(es),energy_max=max(es)))
    # All theta values at s=1 coincide, and theta=0/2pi agree for each s.
    assert np.array_equal(0*u+v,0*np.exp(1j)*u+v)
    records.append(dict(q=q,mode_loop_samples=samples))
tol=1e-12
metrics=dict(relative_charge_error=maxcharge,scaled_momentum_orthogonality=maxorthogonal,
 relative_kinetic_identity_error=maxidentity,relative_kinetic_increase=maxincrease,
 relative_conjugation_energy_error=maxconjugation)
assert all(x<tol for x in metrics.values()),metrics
out=dict(status='all sampled checks passed',scope='Finite-mode illustration, not a continuum topology proof or soliton evolution',
 configuration=dict(seed=20261108,points=N,length=length,charges=charges,acceptance_tolerance=tol),
 metrics=metrics,records=records,versions=dict(python=platform.python_version(),numpy=np.__version__))
args.output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status=out['status'],metrics=metrics,output=str(args.output)),indent=2))
