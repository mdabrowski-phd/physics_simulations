#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 12 (pryzma piasku Baka)
import sys, math
import matplotlib.pyplot as plt 
from numpy import *

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/python/cwiczenia12/"

#stale fizyczne i warunki poczatkowe
N=31
T=10000
c=4

law=zeros((N**2)+1)	#parametry symulacji
s=0
liczba=zeros(T)
M=zeros([N,N])

for i in xrange(T):
	M[N/2][N/2]+=1
	flag=True
	s=0
	A=zeros([N,N])
	while flag:
		tabx,taby=nonzero(M>=c)
		n=tabx.size
		if(n==0):
			flag=False
		else:
			for j in xrange(n):
				a=tabx[j]
				b=taby[j]
				A[a][b]=1
				M[a][b]-=4
				if(a+1)<N:
                   			M[a+1][b]+=1
                		if(a-1)>=0:    
                    			M[a-1][b]+=1
                		if(b+1)<N:
                    			M[a][b+1]+=1
                		if(b-1)>=0:
                    			M[a][b-1]+=1

	if i%100==0:
		nazwa=str(i)
		nazwa = nazwa.rjust(5, '0')
		import matplotlib
		import matplotlib.pyplot as plt
		fig=plt.figure()
		ax=fig.add_subplot(211)
		cax= ax.imshow(M, interpolation='nearest')
		cax.set_clim(vmin=0, vmax=8)
		cbar= fig.colorbar(cax, ticks=[0,3,5,8], orientation='vertical')
		plt.savefig(folder+"zad2_"+nazwa+".png")
		plt.clf()
