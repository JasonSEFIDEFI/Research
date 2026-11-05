"""Independent correctness checks for saved results and solver algebra."""
import json, hashlib
from pathlib import Path
import numpy as np
from benchmark import op, direct, dynamics, instance, reference

root=Path(__file__).resolve().parent
d=json.loads((root/'results.json').read_text())
assert hashlib.sha256((root/'PROTOCOL.md').read_bytes()).hexdigest()==d['protocol_sha256']
assert hashlib.sha256((root/'benchmark.py').read_bytes()).hexdigest()==d['script_sha256']
assert len(d['cases'])==360
for row in d['cases']:
    assert row['residual']<=1e-6
    assert row['forward_error']<=1e-3
    assert len(row['repeats_seconds'])==3
for seed in range(40):
    a,b,u=instance(30,.99,90000+seed)
    x,_,_=direct(a,b,u,.99)
    assert np.allclose(x,reference(a,b,u),rtol=1e-12,atol=1e-12)
    for j in range(len(a)):
        matrix=np.array([[1,a[j],b[j]],[a[j],1,0],[b[j],0,1]])
        assert np.allclose(op(a,b,u)[j],matrix@u[j],atol=1e-14)
        r=np.hypot(a[j],b[j])
        assert np.allclose(np.linalg.eigvalsh(matrix),[1-r,1,1+r],atol=1e-14)
# Analytic undamped control: x=1-cos(t), v=sin(t) for B=1,u=1;
# it does not converge to x*=1 even though the forced trajectory is bounded.
times=2*np.pi*np.arange(1,11)
assert np.allclose(1-np.cos(times),0)
# Compare entire fixed-time RK4 trajectories with exact diagonal oscillator
# solutions, independently of residual-triggered stopping.
errors=[]
for h in [.2,.1,.05]:
    c=.7; x=0.; v=0.; T=4.; w=np.sqrt(1-c*c/4)
    def f(z): return np.array([z[1],1-z[0]-c*z[1]])
    z=np.array([x,v])
    for _ in range(round(T/h)):
        k1=f(z);k2=f(z+h*k1/2);k3=f(z+h*k2/2);k4=f(z+h*k3)
        z+=h*(k1+2*k2+2*k3+k4)/6
    exact=1-np.exp(-c*T/2)*(np.cos(w*T)+c/(2*w)*np.sin(w*T))
    errors.append(abs(z[0]-exact))
assert errors[0]/errors[1]>10 and errors[1]/errors[2]>10
result={'saved_method_cases_passed':360,'independent_block_instances':40,
        'rk4_exact_scalar_errors':errors,'undamped_control':'bounded but not convergent',
        'passed':True}
(root/'verification.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
