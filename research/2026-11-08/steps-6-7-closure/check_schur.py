"""Independent finite-dimensional check of the fixed-charge Hamiltonian reduction."""
from pathlib import Path
import json
import numpy as np
from scipy.linalg import solve
n=100;h=.2;r=np.arange(1,n+1)*h
D=np.diag(np.full(n,2/h**2))+np.diag(np.full(n-1,-1/h**2),1)+np.diag(np.full(n-1,-1/h**2),-1)
D[-1,-1]-=1/h**2
f=.8*np.exp(-(r/5)**2);q=.2;w=1.4
screen=D+np.diag(q*q*f*f);u=1-q*q*solve(screen,r*f*f)/r;Om=w*u
G=solve(D,np.eye(n));electric=q*q*f[:,None]*G*f[None,:]
P=np.eye(n)+electric;B=np.diag(Om)-Om[:,None]*electric
Huu=np.diag(Om)@electric@np.diag(Om)
d=r*f;e=r*f*Om
pinv_bt=solve(P,B.T);pinv_d=solve(P,d)
v=e+B@pinv_d
schur=Huu-B@pinv_bt+np.outer(v,v)/np.dot(d,pinv_d)
C=4*np.pi*h*np.sum(r*r*f*f*u);b=r*f*u*u
expected=-np.diag(Om*Om)+4*q*q*(f*Om)[:,None]*solve(screen,np.diag(f*Om))
expected+=4*w*w/C*(4*np.pi*h)*np.outer(b,b)
error=float(np.max(abs(schur-expected)))
result=dict(status='Exploratory / Not Promoted',test='Coulomb-gauge Cartesian momentum Schur complement equals screened static fixed-N Hessian',maximum_absolute_error=error,passed=error<1e-11)
Path(__file__).with_name('schur_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result));assert result['passed']
