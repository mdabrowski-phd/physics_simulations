#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 2 (osemka Chencinera)
import sys, math
import matplotlib.pyplot as plt 
import numpy as np
from pylab import *

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/python/cwiczenia2/film/"

#parametry symulacji 
dt=0.001
N=20000

#warunki poczatkowe
r01=np.array([0.97000436,-0.24308753])		
v01=np.array([-0.93240737/2.,-0.86473146/2.])
r02=np.array([-0.97000436,0.24308753])		
v02=np.array([-0.93240737/2.,-0.86473146/2.])
r03=np.array([0.,0.])		
v03=np.array([0.93240737,0.86473146])

#sila
def f(x,y):
  return -(x-y)/(np.dot((x-y),(x-y)))**1.5

#algorytm Leapfrog
vw01=v01-0.5*(f(r01,r02)+f(r01,r03))*dt
vw02=v02-0.5*(f(r02,r03)+f(r02,r01))*dt
vw03=v03-0.5*(f(r03,r01)+f(r03,r02))*dt

def frog1(r1,r2,r3,v,vw):
  vp=vw+(f(r1,r2)+f(r1,r3))*dt
  rn=r1+vp*dt
  vn=(vp+vw)/2
  return np.array([rn,vn,vp])

def frog2(r1,r2,r3,v,vw):
  vp=vw+(f(r2,r3)+f(r2,r1))*dt
  rn=r2+vp*dt
  vn=(vp+vw)/2
  return np.array([rn,vn,vp])

def frog3(r1,r2,r3,v,vw):
  vp=vw+(f(r3,r1)+f(r3,r2))*dt
  rn=r3+vp*dt
  vn=(vp+vw)/2
  return np.array([rn,vn,vp])

#balet planetarny
tab1=range(0,N)
tab2=range(0,N)
tab3=range(0,N)
tor_x1=r01[0]
tor_y1=r01[1]
tor_x2=r02[0]
tor_y2=r02[1]
tor_x3=r03[0]
tor_y3=r03[1]
tab1[0]=np.array([r01,v01,vw01])
tab2[0]=np.array([r02,v02,vw02])
tab3[0]=np.array([r03,v03,vw03])
en=0
for x in xrange(1,N):
  tab1[x]=frog1(tab1[x-1][0],tab2[x-1][0],tab3[x-1][0],tab1[x-1][1],tab1[x-1][2])
  tor_x1=np.append(tor_x1,tab1[x][0][0])
  tor_y1=np.append(tor_y1,tab1[x][0][1])
  tab2[x]=frog2(tab1[x-1][0],tab2[x-1][0],tab3[x-1][0],tab2[x-1][1],tab2[x-1][2])
  tor_x2=np.append(tor_x2,tab2[x][0][0])
  tor_y2=np.append(tor_y2,tab2[x][0][1])
  tab3[x]=frog3(tab1[x-1][0],tab2[x-1][0],tab3[x-1][0],tab3[x-1][1],tab3[x-1][2])
  tor_x3=np.append(tor_x3,tab3[x][0][0])
  tor_y3=np.append(tor_y3,tab3[x][0][1])
  if(en%100==0):
    plt.clf()
    axis([-1.5,1.5,-0.4,0.4])
    plt.plot(tab1[x][0][0],tab1[x][0][1],'ro',lw=12)
    plt.plot(tab2[x][0][0],tab2[x][0][1],'go',lw=12)
    plt.plot(tab3[x][0][0],tab3[x][0][1],'bo',lw=12)
    plt.plot(tor_x1,tor_y1,'r--')
    plt.plot(tor_x2,tor_y2,'g--')
    plt.plot(tor_x3,tor_y3,'b--')
    nStr=str(en)
    nStr=nStr.rjust(3,'0') 
    plt.title("Osemka Chencinera")
    plt.savefig(folder+'img'+nStr+'.png')
  en+=1
