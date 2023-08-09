#!/usr/bin/env python

import random, sys
import numpy as np

n=int(sys.argv[1])
x=np.zeros(n)

for i in xrange(n):
	x[i]=random.uniform(-1,1)

s=np.sum(x)/n

sigma=np.sum((x-s)**2)/(n-1)
sigma=sigma**(0.5)

print round(s,4)
print round(sigma,4)
