#!/usr/bin/env python
import math
from scipy import integrate

def myfunc(x):
     return math.sin(x)

res, err = integrate.quad(myfunc,0,math.pi)
print res, err

def yourfunc(x,a,b):
     return a+b*math.sin(x)

p,q = 0, 1
res, err = integrate.quad(yourfunc, 0, math.pi, args=(p,q), epsabs=1.0e-9)
print res, err