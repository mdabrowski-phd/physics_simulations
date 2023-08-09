#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 3 (dwuwymiarowy gaz Lennarda-Jonesa)
import sys, math, os
import matplotlib.pyplot as plt 
import numpy as np
from numpy import *
from matplotlib.patches import Circle

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/python/cwiczenia3/animacja/"

#stale fizyczne i warunki poczatkowe
particleNumber=16
b=8.0 	#boxsize
eps=1.0
sigma=1.0
promien=0.4
delta=2
temp=2.5
nx=4
ny=4
dt=0.001
T=10

#sila Lennarda-Jonesa
def f(r):
  r0=sqrt(np.dot(r,r))
  if(r0>2.5*sigma):
    k=0
  elif(r0<=2.5*sigma):
    k=-48*r*(eps/sigma**2)*(((sigma**2/dot(r,r))**7)-0.5*((sigma**2/dot(r,r))**4))
  return k

#periodyczne warunki brzegowe (PDC)
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
        predkosc=array([(random.random()-1./2),(random.random() -1./2)])
        particles.append(czastka(promien,polozenie,predkosc,predkosc))

#skalowanie temperatury po inicjalizacji
sumv=0.0
sumv2=0.0
for p in particles:
  sumv=sumv+p.v
sumv=sumv/particleNumber	#predkosc srodka masy
for p in particles:
  p.v=(p.v-sumv)		#teraz srodek masy spoczywa
for p in particles:
  sumv2=sumv2+dot(p.v,p.v)/2.0
sumv2=sumv2/particleNumber 	#srednia energia kinetyczna
fs=sqrt(temp/sumv2) 	#czynnik skalujacy, temp - zadana temperatura
for p in particles:
  p.v=p.v*fs		#skalujemy
  p.vw=p.v*fs

#algorytm Leapfrog - bez skalowania
def frog(r,v,vw,k):
  vp=vw+tab[k]*dt
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
      plt.savefig(folder+'img'+nStr+'.png')
     
#pocztkowe parametry animacji
t=0.0
en=0
tab=[]

#dynamika ukladu czastek (najblizszy obraz)
while t<T:
    for i in xrange(particleNumber):
        tab=sily()
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
        rys()
        en=en+1
