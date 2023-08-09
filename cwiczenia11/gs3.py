#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 11 (model reakcji-dyfuzji Graya-Scotta 2D)
import sys, math
import matplotlib.pyplot as plt 
from numpy import *

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/python/cwiczenia11/"

#stale fizyczne i warunki poczatkowe
Du=2*10**(-5)
Dv=1*10**(-5)
dx=0.02
dy=dx
dt=1
T=20000
N=100
random.seed()

f=linspace(0.06,0.08,41)	#parametry symulacji
k=0.062

#obliczanie wspolczynnika 1 reakcji-dyfuzji
def F1():
    du_dt=(roll(u,1,axis=0)-2*u+roll(u,-1,axis=0))*Du/dx**2
    du_dt=du_dt +(roll(u,1,axis=1)-2*u+roll(u,-1,axis=1))*Du/dy**2
    du_dt+=-u*v*v+F*(1-u)
    return du_dt

#obliczanie wspolczynnika 2 reakcji-dyfuzji
def F2():
    dv_dt=(roll(v,1,axis=0)-2*v+roll(v,-1,axis=0))*Dv/dx**2
    dv_dt+=(roll(v,1,axis=1)-2*v+roll(v,-1,axis=1))*Dv/dy**2
    dv_dt+=u*v*v-(F+k)*v
    return dv_dt

for F in f:
	#warunki poczatkowe ukladu
	u=ones([N,N])
	v=zeros([N,N])
	xs= arange(N)
	for i in range(N/4,3*N/4):
    		for j in range(N/4,3*N/4):
        		u[i][j] = random.random()*0.2+0.4
        		v[i][j] = random.random()*0.2+0.2

	#ewolucja ukladu reakcja+dyfuzja
	for j in xrange(T):
    		x=F1()
    		y=F2()
    		u=u+x*dt
    		v=v+y*dt
    		#rysowanie wykresow do animacji
	print F
        import matplotlib
        import matplotlib.pyplot as plt
        fig=plt.figure()
        ax=fig.add_subplot(211)
	plt.title("k="+str(k)+" F="+str(F))
       	cax= ax.imshow(u, interpolation='nearest')
        cax.set_clim(vmin=0, vmax=1)
        cbar= fig.colorbar(cax, ticks=[0,0.3, 0.5,1], orientation='vertical')
       	plt.savefig("zad2/zad2_k="+str(k)+"_F="+str(F)+".png")
       	plt.clf()   
