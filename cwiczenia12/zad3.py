#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 12 (pryzma piasku Baka)
import sys, math
import matplotlib.pyplot as plt 
from numpy import *

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/python/cwiczenia12/"

#stale fizyczne i warunki poczatkowe
N=31
c=4

M=zeros([N,N])
for m in xrange(N):
	for n in xrange(N):
		M[m][n]=7

flag=True
i=0
while flag:
	i+=1
	tabx,taby=nonzero(M>=c)
	n=tabx.size
	if(n==0):
		flag=False
	else:
		for j in xrange(n):
			a=tabx[j]
			b=taby[j]
			M[a][b]-=4
			if(a+1)<N:
                   		M[a+1][b]+=1
                	if(a-1)>=0:    
                    		M[a-1][b]+=1
                	if(b+1)<N:
                    		M[a][b+1]+=1
                	if(b-1)>=0:
                    		M[a][b-1]+=1

	if(i%10==0):
		nazwa=str(i)
		nazwa = nazwa.rjust(5, '0')
		fig=plt.figure()
		ax=fig.add_subplot(211)
		cax= ax.imshow(M, interpolation='nearest')
		cax.set_clim(vmin=0, vmax=8)
		cbar= fig.colorbar(cax, ticks=[0,3,5,8], orientation='vertical')
		plt.savefig(folder+"zad3_"+nazwa+".png")
		plt.clf()
