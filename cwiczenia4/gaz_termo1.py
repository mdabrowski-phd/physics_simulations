#!/usr/bin/env python           

import sys, math
import matplotlib.pyplot as plt 
from numpy import *

particleNumber=16
boxsize=8.0
b=8.0
eps=1.0
sigma=1.0
promien=0.5
delta=2
temp=0.7
nx=4
ny=4
dt=0.001
T=100
kin=0.0
ep=0.0
ec=0.0
tab=[]
vel=[]



def f(r):
  return -48*r*(eps/sigma**2)*(((sigma**2/dot(r,r))**7)-0.5*((sigma**2/dot(r,r))**4))


def V(r):
  return 4*eps*(((sigma**2/dot(r,r))**6)-((sigma**2/dot(r,r))**3))

def pot():
  tabf=0.0
  for i in xrange(16):
    
    j=15
    while (j>i):
      if(i!=j):
        r_vect=particles[j].r-particles[i].r
         # wektor pomiędzy cząstkamiiorazj
        if r_vect[0] > b/2:
          # b2 –połowa pudełkab2=b/2
          r_vect[0] =r_vect[0]-b # przesuwamywspółrzędnąx wektorar_vect
        elif r_vect[0] <-b/2:
          r_vect[0] =r_vect[0]+b
            # b –bok pudełka
        if r_vect[1] > b/2:
              # to samo dla y
          r_vect[1] =r_vect[1] -b
        elif r_vect[1] <-b/2:
          r_vect[1] =r_vect[1] +b
          
        tabf=tabf+V(r_vect)
        j=j-1
  
  return tabf
  

def sily():
  tabf=[]
  for i in xrange(16):
    tabf.append(array([0.0,0.0]))
    for j in xrange(16):
      if(i!=j):
        r_vect=particles[j].r-particles[i].r
         # wektor pomiędzy cząstkamiiorazj
        if r_vect[0] > b/2:
          # b2 –połowa pudełkab2=b/2
          r_vect[0] =r_vect[0]-b # przesuwamywspółrzędnąx wektorar_vect
        elif r_vect[0] <-b/2:
          r_vect[0] =r_vect[0]+b
            # b –bok pudełka
        if r_vect[1] > b/2:
              # to samo dla y
          r_vect[1] =r_vect[1] -b
        elif r_vect[1] <-b/2:
          r_vect[1] =r_vect[1] +b
          
        tabf[i]=tabf[i]+f(r_vect)
  
  return tabf

def term():
  tabv=[]
  tau=0.0
  suma=0.0
  for i in xrange(16):
    tabv.append(array([0.0,0.0]))
    tabv[i]=particles[i].vw+tab[i]*dt/2
  for i in xrange(16):
    suma=suma+dot(tabv[i],tabv[i])
  tau=suma/(2*16)
  return sqrt(temp/tau)

def kinet():
  ki=0.0
  for i in xrange(16):
    ki=0.5*dot(particles[i].v,particles[i].v)+ki
  return ki
  
def histogra():
  tabv=[]
  for i in xrange(16):
    tabv.append(0.0)
    tabv[i]=sqrt(dot(particles[i].v,particles[i].v))+vel[i]
  return tabv
                          


class czastka:
    """ Klasa opisujaca pojedyncza czastke gazu"""
    def __init__(self,promien,pos,vel,velw):
        self.rad= promien
        self.r=pos# polożenie
        self.v=vel# prędkoscautomatycznie
        self.vw=velw


particles= []
for i in range(nx):
    for j in range(ny):
        polozenie= array([i*delta+1, j*delta+1])
        predkosc=array([(random.random()-1./2),(random.random() -1./2)])
        particles.append(czastka(promien,polozenie,predkosc,predkosc))
        vel.append(0.0)


sumv=0.0
sumv2=0.0
for p in particles:
    sumv=sumv+p.v
sumv=sumv/particleNumber
    # prędkośćśrodka masy
for p in particles:
    p.v=(p.v-sumv)
    # teraz środek masy spoczywa
for p in particles:
    sumv2=sumv2+dot(p.v,p.v)/2.0
sumv2=sumv2/particleNumber # średnia energia kinetyczna
fs=sqrt(temp/sumv2) # czynnik skalujący, temp -żądanatemperatura
for p in particles:
    p.v=p.v*fs# skalujemy
    p.vw=p.v*fs


#frog
#vw0=v0-0.25*f(r0)*dt/m

def frog(r,v,vw,k):
  vp=(2*eta-1)*vw+eta*tab[k]*dt
  rn=r+vp*dt
  vn=(vp+vw)/2
  return czastka(promien,rn,vn,vp)



from matplotlib.patches import Circle


def rys():

  if (en%1000==0):
    # co 100-na klatka
      plt.clf()# wyczyśćobrazek
      F = plt.gcf()# zdefiniuj nowy
      for i in range(particleNumber):
        # pętla po cząstka
        p = particles[i]
        a = plt.gca()
        cir = Circle((p.r[0],p.r[1]), radius=p.rad)
        # kółko tam gdzie jest cząstka
        a.add_patch(cir)
        # dodaj to kółko do rysunku
        plt.plot()# narysuj
      plt.xlim((0,boxsize))# obszar do narysowania
      plt.ylim((0,boxsize))
      F.set_size_inches((6,6))# rozmiar rysunku
      nStr=str(en)#nagraj na dysk–numer pliku z 5 cyframi, na początku zera, np00324.png
      nStr=nStr.rjust(5,'0')
      plt.title("Symulacja gazu Lennarda-Jonesa, krok" +nStr)
      plt.savefig('img'+nStr+'.png')




    

orbE=0.0
orbK=0.0
orbV=0.0
time=0.0

t=0.0
en=0

while t<T:
    for i in xrange(16):
        tab=sily()
        eta=term()
        particles[i]=frog(particles[i].r,particles[i].v,particles[i].vw,i)
        if particles[i].r[0]>b:
          particles[i].r[0]=particles[i].r[0]-b
        if particles[i].r[0]<0:
          particles[i].r[0]=particles[i].r[0]+b
        if particles[i].r[1]>b:
          particles[i].r[1]=particles[i].r[1]-b
        if particles[i].r[1]<0:
          particles[i].r[1]=particles[i].r[1]+b
        t=t+dt
        if(en%100==0):
          kin=kinet()
          orbK=append(orbK,kin)
          ep=pot()
          orbV=append(orbV,ep)
          ec=ep+kin
          orbE=append(orbE,ec)
          time=append(time,t)
          vel=histogra()
        rys()
        en=en+1


for i in xrange(16):
  vel[i]=vel[i]/(T/(dt*100))

plt.subplot(411)
plt.plot(time,orbK)
plt.subplot(412)
plt.plot(time,orbV)
plt.subplot(413)
plt.plot(time,orbE)
plt.subplot(414)
plt.hist(vel, bins=20, normed=1, facecolor='green')
plt.grid(True)
plt.show()
plt.savefig("cos.png")

        










