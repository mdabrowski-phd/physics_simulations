#!/usr/bin/env python

a=['cat','window','defenestrate']
for x in a:
     print x, len(x)

b=['Mary','had','a','little','lamb']
print b[3]
print b[3][1:2]

for i in xrange(len(b)):
     print i, b[i], len(b[i])

for x in b:
     print b.index(x), x, len(x)