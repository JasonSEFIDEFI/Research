"""Prescribed n=1 smooth amplitude: Maxwell and J=nN diagnostic, NOT a soliton."""
from pathlib import Path
import json
import numpy as np
from scipy.sparse import diags,kron,eye
from scipy.sparse.linalg import spsolve
HERE=Path(__file__).resolve().parent

def minus_lap(n,h,d):
    r=(np.arange(n)+.5)*h
    left=np.maximum(r-h/2,0)**(d-1)/r**(d-1)/h**2
    right=(r+h/2)**(d-1)/r**(d-1)/h**2
    diagonal=left+right;diagonal[-1]+=right[-1]
    radial=diags([-left[1:],diagonal,-right[:-1]],[-1,0,1],format='csc')
    zd=np.full(n,2/h**2);zd[0]=1/h**2;zd[-1]=3/h**2
    vertical=diags([-np.ones(n-1)/h**2,zd,-np.ones(n-1)/h**2],[-1,0,1],format='csc')
    return kron(radial,eye(n,format='csc'),format='csc')+kron(eye(n,format='csc'),vertical,format='csc')

def run(h):
    L=6.;size=round(L/h);r=(np.arange(size)+.5)*h
    R,Z=np.meshgrid(r,r,indexing='ij');R=R.ravel();Z=Z.ravel()
    q=.2;w=1.4;n=1
    f=R*np.exp(-(R*R+Z*Z)/2)
    lap2=minus_lap(size,h,2);lap4=minus_lap(size,h,4);screen=diags(q*q*f*f,format='csc')
    a=spsolve(lap2+screen,q*w*f*f)
    u=spsolve(lap4+screen,-q*n*f*f/(R*R));b=R*R*u
    Om=w-q*a;k=n+q*b;weight=4*np.pi*h*h*R
    N=float(np.dot(weight,Om*f*f));Jmatter=float(np.dot(weight,Om*k*f*f))
    Jem=-float(np.dot(weight,b*(lap2@a)));J=Jmatter+Jem
    moment=q/2*float(np.dot(weight,k*f*f))
    result=dict(h=h,outer_R=L,outer_z=L,grid_points=size*size,q=q,omega=w,n=n,
        charge_number=N,electric_charge=q*N,matter_angular_momentum=Jmatter,electromagnetic_angular_momentum=Jem,
        total_angular_momentum=J,relative_J_minus_nN=abs(J-n*N)/abs(n*N),
        interior_current_dipole_integral=moment,
        electric_residual=float(max(abs((lap2+screen)@a-q*w*f*f))),
        magnetic_residual=float(max(abs((lap4+screen)@u+q*n*f*f/(R*R)))),
        minimum_k=float(min(k)),maximum_k=float(max(k)),
        scope='Prescribed amplitude, finite zero-potential outer boundary. Scalar field equations are NOT solved; no soliton, binding, asymptotic dipole or physical g is claimed.')
    return result

if __name__=='__main__':
    rows=[run(.1),run(.05)]
    result=dict(status='Exploratory / Not Promoted',kind='Forced Maxwell diagnostic, not a self-consistent scalar solution',results=rows)
    (HERE/'forced_maxwell_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    assert all(x['electric_residual']<1e-8 and x['magnetic_residual']<1e-8 and x['relative_J_minus_nN']<1e-9 for x in rows)
