
#Bessel's identity
#(2) cos(x) = jn(0,x) + 2*∑_(n=1)^∞▒〖(-1)^n*jn(2n,x)〗

import numpy as np
from scipy.special import jn
from scipy.integrate import quad
from scipy.misc import derivative

x=float(input("Enter the x: "))
s=0.0
n=1
LHS=np.cos(x)
term=2*(-1)**n*jn(2*n,x)
RHS=jn(0,x)+term
while(abs(LHS-RHS)>1.0e-5):
    term=2*(-1)**n*jn(2*n,x)
    s=s+term
    RHS=jn(0,x)+s
    n=n+1
print("LHS: ",LHS)
print("RHS: ",RHS)
