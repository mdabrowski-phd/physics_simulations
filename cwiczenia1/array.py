#!/usr/bin/env python

import numpy as np
n=5
A=np.zeros((n,n))
x=np.zeros(n)

for i in xrange(n):
     x[i]=i/2.0
     for j in xrange(n):
          A[i,j]=2.0+(i+1.0)/(j+i+1.0)

print x
print A

b=np.dot(A,x)
y=np.linalg.solve(A,b)

print y