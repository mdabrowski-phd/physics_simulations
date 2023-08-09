#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 4 (gaz dwuwymiarowy + termostat Browna-Clarka)
import sys, math, os
import matplotlib.pyplot as plt 
import numpy as np
from numpy import *
from matplotlib.patches import Circle

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/python/cwiczenia4/"

#stale fizyczne i warunki poczatkowe
particleNumber=64
nx=8
ny=8
b=16.0
eps=1.0
sigma=1.0
promien=0.4
delta=2.0
temp=8.0
dt=0.01
T=100
kinet=0.0
poten=0.0
energia=0.0
tab=[]
rad=[]
histp=[]
delg=0.1
bins=arange(0,b/2.0,delg)

#sila Lennarda-Jonesa
def f(r):
  r0=sqrt(np.dot(r,r))
  if(r0>2.5*sigma):
    k=0
  elif(r0<=2.5*sigma):
    k=-48*r*(eps/sigma**2)*(((sigma**2/dot(r,r))**7)-0.5*((sigma**2/dot(r,r))**4))
  return k

#potencjal Lennarda-Jonesa
def V(r):
  r0=sqrt(np.dot(r,r))
  if(r0>2.5*sigma):
    k=0
  elif(r0<=2.5*sigma):
    k=4*eps*(((sigma**2/dot(r,r))**6)-((sigma**2/dot(r,r))**3))
  return k

#periodyczne warunki brzegowe (PDC) dla sily
def sily():
  tabf=[]
  for i in xrange(particleNumber):
    tabf.append(array([0.0,0.0]))
    for j in xrange(particleNumber):
      if(i!=j):
        r_vect=particles[j].r-particles[i].r #wektor miedzy czastkami i oraz j
        if r_vect[0] > b/2:		#b - bok pudelka
          r_vect[0] =r_vect[0]-b 	#przesuwamy wspolrzedne wektorar_vect
        elif r_vect[0] <-b/2:
          r_vect[0] =r_vect[0]+b
        if r_vect[1] > b/2:
          r_vect[1] =r_vect[1] -b
        elif r_vect[1] <-b/2:
          r_vect[1] =r_vect[1] +b
        tabf[i]=tabf[i]+f(r_vect)
  return tabf

#periodyczne warunki brzegowe (PDC) dla potencjalu
def potencjal():
  tabf=0.0
  for i in xrange(particleNumber):
    for j in xrange(particleNumber):
      if(i<j):
        r_vect=particles[j].r-particles[i].r #wektor miedzy czastkami i oraz j
        if r_vect[0] > b/2:		#b - bok pudelka
          r_vect[0] =r_vect[0]-b 	#przesuwamy wspolrzedne wektorar_vect
        elif r_vect[0] <-b/2:
          r_vect[0] =r_vect[0]+b
        if r_vect[1] > b/2:
          r_vect[1] =r_vect[1] -b
        elif r_vect[1] <-b/2:
          r_vect[1] =r_vect[1] +b
        tabf=tabf+V(r_vect)
  return tabf

#obliczanie energii kinetycznej
def kinetyczna():
  K=0.0
  for i in xrange(particleNumber):
    K=0.5*dot(particles[i].v,particles[i].v)+K
  return K
  
#radialna funkcja rozkladu
def radial():
  d=0.0
  n=0
  pom=[]
  while(d<b/2.0):
    k=0.0
    for i in xrange(particleNumber):
      if(i>0):
        odl=sqrt(np.dot(particles[i].r-particles[0].r,particles[i].r-particles[0].r))
        if(odl>=d and odl<d+delg):
          k=k+1.0
    pom.append(k)
    d=d+delg
    n=n+1
  return pom
       
#obliczanie czynnika skalujacego temperature
def term():
  tabv=[]
  tau=0.0
  sum=0.0
  for i in xrange(particleNumber):
    tabv.append(0.0)
    tabv[i]=particles[i].vw+tab[i]*dt/2
    sum=sum+tabv[i]**2
  tau=sum/(2*particleNumber)
  return sqrt(temp/tau)
  
#klasa czastka
class czastka:
    """ Klasa opisujaca pojedyncza czastke gazu"""
    def __init__(self,promien,pos,vel,velw):
        self.rad= promien
        self.r=pos	#polozenie
        self.v=vel	#predkosc
        self.vw=velw	#poprzednia predkosc

#inicjalizacja siatki czastek
particles=[]
for i in range(nx):
    for j in range(ny):
        polozenie= array([i*delta+1, j*delta+1])
        predkosc=array([10.0*(random.random()-1./2),10.0*(random.random() -1./2)])
        particles.append(czastka(promien,polozenie,predkosc,predkosc))
	
#algorytm Leapfrog - termostat Browna-Clarka
def frog(r,v,vw,k):
  vp=(2*eta-1)*vw+eta*tab[k]*dt
  rn=r+vp*dt
  vn=(vp+vw)/2
  return czastka(promien,rn,vn,vp)

#rysowanie klatek animacji
def rys():
  if (en%100==0):	#co 100-na klatka
      plt.clf()		#wyczysc obrazek
      F = plt.gcf()	#zdefiniuj nowy
      for i in range(particleNumber):	#petla po czastkach
        p = particles[i]
        a = plt.gca()
        cir = Circle((p.r[0],p.r[1]), radius=p.rad) #kolko w miejscu czastki
        a.add_patch(cir)	#dodaj to kolko do rysunku
        plt.plot()		#narysuj
      plt.xlim((0,b))	#obszar do narysowania
      plt.ylim((0,b))
      F.set_size_inches((6,6))	# rozmiar rysunku
      nStr=str(en)		#indeks pliku z klatka animacji
      nStr=nStr.rjust(5,'0')	#numer pliku z 5 cyframi, na poczatku zera
      plt.title("Symulacja gazu Lennarda-Jonesa, krok" +nStr)
      plt.savefig(folder+'anim1/img'+nStr+'.png')
     
#pocztkowe parametry animacji
t=0.0
en=0
orbE=0.0
orbK=0.0
orbV=0.0
time=0.0

#dynamika ukladu czastek (najblizszy obraz)
while t<T:
    for i in xrange(particleNumber):
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
	if(en%100==0):	#co 100-na klatka
          kinet=kinetyczna()
          orbK=append(orbK,kinet)
          poten=potencjal()
          orbV=append(orbV,poten)
          energia=kinet+poten
          orbE=append(orbE,energia)
          time=append(time,t)
	  rad=rad+radial()
        rys()
        en=en+1

#normalizacja danych do histogramu
for i in range(0,len(bins)):
  rad[i]=rad[i]/(T/(dt*100))

#histogram funkcji rozkladu
#histp,bin_edges=histogram(rad,bins=bins,normed=True)
histp=rad
histn=[0]*len(bins)
for i in range(0,len(bins)):
  fg=1.0*pi*(((i+1)**2-i**2)*delg**2)*particleNumber/(b**2)
  histn[i]=histp[i]/(fg)
  
#rysowanie wykresow energii i histogramu predkosci
plt.subplot(211)
plt.title("Zaleznosc energii od czasu")
plt.plot(time,orbK, "r-")
plt.plot(time,orbV, "g-")
plt.plot(time,orbE, "b-")
plt.xlabel("czas t")
plt.ylabel("T(t), V(t), T(t)+V(t)")
plt.legend(("T", "V", "T+V"))
plt.grid(True)
plt.subplot(212)
#plt.plot(.5*(bin_edges[1:]+bin_edges[:-1]),histn)
plt.plot(bins,histn, "r-")
plt.title("Radialna funkcja rozkladu")
plt.xlabel("odleglosc d")
plt.ylabel("czestosc wystepowania")
plt.savefig(folder + "radial_fun.pdf", format="pdf")
plt.show()
