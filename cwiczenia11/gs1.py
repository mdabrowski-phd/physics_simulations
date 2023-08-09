#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 11 (model reakcji-dyfuzji Graya-Scotta 1D)
import sys, math
import matplotlib.pyplot as plt 
from numpy import *

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/python/cwiczenia11/"

#stale fizyczne i warunki poczatkowe
Du=2*10**(-5)
Dv=1*10**(-5)
dx=0.02
dt=1
T=10000
N=100
random.seed()

F=0.037		#parametry symulacji
k=0.06

#obliczanie wspolczynnika 1 reakcji-dyfuzji
def F1(u,v,i):
    if i+1>N-1:	#periodyczne warunki brzegowe
        a=0
    else:
        a=i+1
    if i-1<0:
        b=N-1
    else:
        b=i-1
    poch=(u[a]-2*u[i]+u[b])/(dx**2)
    return Du*poch-u[i]*((v[i])**2)+F*(1-u[i])

#obliczanie wspolczynnika 2 reakcji-dyfuzji
def F2(u,v,i):
    if i+1>N-1:	#periodyczne warunki brzegowe
        a=0
    else:
        a=i+1
    if i-1<0:
        b=N-1
    else:
        b=i-1
    poch=(v[a]-2*v[i]+v[b])/(dx**2)
    return Dv*poch+u[i]*((v[i])**2)-(F+k)*v[i]

#warunki poczatkowe ukladu
u= ones(N)
v= zeros(N)
xs= arange(N)
for i in range(N/4,3*N/4):
    u[i] = random.random()*0.2+0.4
    v[i] = random.random()*0.2+0.2

#ewolucja ukladu reakcja+dyfuzja
for j in xrange(T):
    for m in xrange (N):
        u[m]=u[m]+F1(u,v,m)*dt
        v[m]=v[m]+F2(u,v,m)*dt
    #rysowanie wykresow do animacji
    if j%100==0:
        print j
        plt.clf()
        plt.plot(xs*dx,u, "g-", lw=1)
        plt.plot(xs*dx,v, "r-", lw=1)
        nazwa=str(j)
	nazwa = nazwa.rjust(5, '0')
	plt.title("Uklad Graya-Scotta k="+str(k)+" F="+str(F)+" "+nazwa)
        plt.savefig("zad1/zad1_k="+str(k)+"_F="+str(F)+"_"+nazwa+".png")    
