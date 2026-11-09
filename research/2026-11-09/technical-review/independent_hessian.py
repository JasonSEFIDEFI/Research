"""Differentiate the original discrete canonical energy, not assembled blocks.
This is an independent implementation check by the same AI, not peer review.
"""
from pathlib import Path
import json
import sympy as sp
import numpy as np
n=3;r=sp.Matrix([1,2,3]);q=sp.Rational(1,5);w=sp.Rational(7,5);v=sp.Rational(1,2)
D=sp.Matrix([[2,-1,0],[-1,2,-1],[0,-1,2]]);De=D.copy();De[-1,-1]=1;G=De.inv()
f=sp.Matrix([sp.Rational(4,5),sp.Rational(1,2),sp.Rational(1,10)])
s=sp.Matrix([sp.Rational(1,10),sp.Rational(1,4),sp.Rational(2,5)])
screen=De+sp.diag(*[q*q*z*z for z in f])
abar=screen.inv()*(q*w*sp.Matrix([r[i]*f[i]**2 for i in range(n)]))
Om=sp.Matrix([w-q*abar[i]/r[i] for i in range(n)])
symbols=sp.symbols('x0:18',real=True)
X,Y,Z,PX,PY,PZ=[sp.Matrix(symbols[i*n:(i+1)*n]) for i in range(6)]
density=sp.Matrix([(Y[i]*PX[i]-X[i]*PY[i])/r[i] for i in range(n)])
H=((X.T*D*X)[0]+(Y.T*D*Y)[0]+(Z.T*D*Z)[0]+(PX.dot(PX)+PY.dot(PY)+PZ.dot(PZ)))/2
H+=q*q*(density.T*G*density)[0]/2
for i in range(n):
    rho=(X[i]**2+Y[i]**2)/r[i]**2;eta=(v+Z[i]/r[i])**2
    H+=r[i]**2*(rho**2/4+rho/2+2*rho*eta+3*(eta-sp.Rational(1,4))**2)
N=sum(Y[i]*PX[i]-X[i]*PY[i] for i in range(n))
K=H-w*N
values=list(sp.matrix_multiply_elementwise(r,f))+[0]*n+list(sp.matrix_multiply_elementwise(r,s-sp.ones(n,1)*v))+[0]*n+[-r[i]*Om[i]*f[i] for i in range(n)]+[0]*n
direct=np.array(sp.hessian(K,symbols).subs(dict(zip(symbols,values)))).astype(float)
f=np.array(f,dtype=float).ravel();s=np.array(s,dtype=float).ravel();Om=np.array(Om,dtype=float).ravel();G=np.array(G,dtype=float);D=np.array(D,dtype=float);q=float(q)
zero=np.zeros((n,n));I=np.eye(n);od=np.diag(Om)
electric=q*q*f[:,None]*G*f[None,:];mixed=od-Om[:,None]*electric
assembled=np.block([[D+np.diag(1+3*f*f+4*s*s)+Om[:,None]*electric*Om[None,:],zero,np.diag(8*f*s),zero,mixed,zero],
    [zero,D+np.diag(1+f*f+4*s*s),zero,-od,zero,zero],
    [np.diag(8*f*s),zero,D+np.diag(-3+4*f*f+36*s*s),zero,zero,zero],
    [zero,-od,zero,I,zero,zero],[mixed.T,zero,zero,zero,I+electric,zero],[zero,zero,zero,zero,zero,I]])
error=float(np.max(abs(direct-assembled)))
result=dict(status='Exploratory / Not Promoted',review_kind='Separate implementation, same AI; no independent reviewer',
    sympy=sp.__version__,dimension=6*n,maximum_absolute_hessian_difference=error,passed=error<1e-10)
Path(__file__).with_name('independent_hessian_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result));assert result['passed']
