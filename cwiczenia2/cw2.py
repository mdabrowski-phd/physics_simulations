#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 2 (symulacje ruchu planet)
import sys, math
import matplotlib.pyplot as plt 
import numpy as np
from pylab import *

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/python/cwiczenia2/"

#stale fizyczne 
G=0.01	
M=500.0
m=0.1
dt=0.001
N=30000

#warunki poczatkowe
r0=np.array([2.,0.])		
v0=np.array([0.0,0.1/m])

#sila
def f(r):	
  return -G*M*m*r/(np.dot(r,r))**1.5

#energia kinetyczna
def T(v):
  return m/2*np.dot(v,v)

#energia potencjalna
def V(r):
  return -G*M*m/(math.sqrt(np.dot(r,r)))

#algorytm Eulera
def euler(r,v):
  rn=r+v*dt+0.5*(f(r)/m)*(dt)**2
  vn=v+f(r)*dt/m
  return np.array([rn,vn])

#algorytm Verleta
rw0=r0-v0*dt

def verlet(r,v,rw):
  rn=2*r-rw+(f(r)/m)*(dt)**2
  vn=(rn-rw)/(2*dt)
  return np.array([rn,vn])

#algorytm Leapfrog
vw0=v0-0.5*f(r0)*dt/m

def frog(r,v,vw):
  vp=vw+f(r)*dt/m
  rn=r+vp*dt
  vn=(vp+vw)/2
  return np.array([rn,vn,vp])

#trajektoria i energia - Euler
tab1=range(0,N)
tor_x1=r0[0]
tor_y1=r0[1]
T1=T(v0)
V1=V(r0)
tab1[0]=np.array([r0,v0])
for x in xrange(1,N):
  tab1[x]=euler(tab1[x-1][0],tab1[x-1][1])
  tor_x1=np.append(tor_x1,tab1[x][0][0])
  tor_y1=np.append(tor_y1,tab1[x][0][1])
  T1=np.append(T1,T(tab1[x][1]))
  V1=np.append(V1,V(tab1[x][0]))
   
#trajektoria i energia - Verlet
tab2=range(0,N)
tor_x2=r0[0]
tor_y2=r0[1]
T2=T(v0)
V2=V(r0)
tab2[0]=np.array([r0,v0])
tab2[1]=verlet(tab2[0][0],tab2[0][1],rw0)
T2=np.append(T2,T(tab2[1][1]))
V2=np.append(V2,V(tab2[1][0]))
for x in xrange(2,N):
  tab2[x]=verlet(tab2[x-1][0],tab2[x-1][1],tab2[x-2][0])
  tor_x2=np.append(tor_x2,tab2[x][0][0])
  tor_y2=np.append(tor_y2,tab2[x][0][1])
  T2=np.append(T2,T(tab2[x][1]))
  V2=np.append(V2,V(tab2[x][0]))

#trajektoria i energia - Leapfrog
tab3=range(0,N)
tor_x3=r0[0]
tor_y3=r0[1]
T3=T(v0)
V3=V(r0)
tab3[0]=np.array([r0,v0,vw0])
for x in xrange(1,N):
  tab3[x]=frog(tab3[x-1][0],tab3[x-1][1],tab3[x-1][2])
  tor_x3=np.append(tor_x3,tab3[x][0][0])
  tor_y3=np.append(tor_y3,tab3[x][0][1])
  T3=np.append(T3,T(tab3[x][1]))
  V3=np.append(V3,V(tab3[x][0]))
    
#rysowanie wykresow    
ts=np.arange(0,N*dt,dt)
#algorytm Eulera
plt.subplot(331)
plt.title("Algorytm Eulera")
axis([-1,2.8,-1.3,1.3])
plt.plot(tor_x1 ,tor_y1, "g-")
plt.grid(True)
plt.xlabel("wsp x")
plt.ylabel("wsp y")
plt.subplot(334)
plt.plot(ts ,T1, "g-",ts ,V1, "r-")
plt.grid(True)
plt.xlabel("czas t")
plt.ylabel("T(t), V(t)") 
plt.legend(("T", "V"))
plt.subplot(337)
plt.plot(ts ,T1+V1, "b-")
plt.grid(True)
plt.xlabel("czas t")
plt.ylabel("E(t)=T(t)+V(t)")
#algorytm Verleta
plt.subplot(332)
plt.title("Algorytm Verleta")
axis([-1,2.8,-1.3,1.3])
plt.plot(tor_x2 ,tor_y2, "g-")
plt.grid(True)
plt.xlabel("wsp x")
plt.subplot(335)
plt.plot(ts ,T2, "g-",ts ,V2, "r-")
plt.grid(True)
plt.xlabel("czas t")
plt.legend(("T", "V", ))
plt.subplot(338)
plt.plot(ts ,T2+V2, "b-")
plt.grid(True)
plt.xlabel("czas t")
#algorytm Leapfrog
plt.subplot(333)
plt.title("Algorytm Leapfrog")
axis([-1,2.8,-1.3,1.3])
plt.plot(tor_x3 ,tor_y3, "g-")
plt.grid(True)
plt.xlabel("wsp x")
plt.subplot(336)
plt.plot(ts ,T3, "g-",ts ,V3, "r-")
plt.grid(True)
plt.xlabel("czas t")
plt.legend(("T", "V"))
plt.subplot(339)
plt.plot(ts ,T3+V3, "b-")
plt.grid(True)
plt.xlabel("czas t")
#zapis i wyswietlanie rysunkow
plt.savefig(folder + "orbity.pdf", format="pdf")
plt.show()
