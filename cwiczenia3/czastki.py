#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import math 
from math import sqrt
import random
import matplotlib.pyplot as plt 
from matplotlib.patches import Circle

## stale
sqpart = 5
particleNumber = sqpart**2
boxsize = 2*sqpart
eps = 1.0
sigma = 1.0
promien = 0.5
deltat = 0.0003
temp = 2.5
m = 1.
rc=2.5*sigma


def repopulate():
    for p in particles:
        celllist[p] = []
        for p2 in particles:
            if p != p2 and np.linalg.norm(odleglosc(p.r - p2.r)) < 3.5:
                celllist[p].append(p2)
            
def odleglosc(rrr):
    if rrr[0] > boxsize/2.:
        rrr[0] -= boxsize
    elif rrr[0] < -boxsize/2.:
        rrr[0] += boxsize
    if rrr[1] > boxsize/2.:
        rrr[1] -= boxsize
    elif rrr[1] < -boxsize/2.:
        rrr[1] += boxsize
    return np.linalg.norm(rrr)

def sila(r):
    rn = odleglosc(r)
    if rn < rc:
        return r/rn*48*eps/sigma*((sigma/rn)**13-0.5*(sigma/rn)**7)
    else:
        return np.array([0.,0.])

def skalowanko():
    sumv = 0
    sumv2 = 0
    for p in particles:
        sumv=sumv+p.v
        sumv=sumv/particleNumber # predkosc srodka masy
    for p in particles:
        p.v=(p.v-sumv) # teraz srodek masy spoczywa
    for p in particles:
        sumv2=sumv2+np.dot(p.v,p.v)/2.0
    sumv2=sumv2/particleNumber  # srednia energia kinetyczna
    fs=sqrt(temp/sumv2)        # czynnik skalujacy,  temp - zadana temperatura
    for p in particles:
        p.v=p.v*fs     # skalujemy
    return (sumv2)
        
## klasa czastka
class czastka:
    """Klasa opisuja pojedyncza czastke gazu."""
    def __init__(self,promien,pos,vel):
        self.promien = promien
        self.r=pos # polozenie
        self.v=vel # predkosc

## PBC
def pbc(r):
    if r[0] > boxsize:
        r[0] -= boxsize
    if r[0] < 0:
        r[0] += boxsize
    if r[1] > boxsize:
        r[1] -= boxsize
    if r[1] < 0:
        r[1] += boxsize  
    return r
  
## rysowanie
def rysowanie(en):
    if (en%100==0):     #  co 100-na klatka           
        plt.clf()               #  wyczysc obrazek
        F = plt.gcf()       #   zdefiniuj nowy
        for i in range(particleNumber):    # petla po czastkach
            p = particles[i]
            a = plt.gca() # "get current axes" (to add smth to them)
            cir = Circle((p.r[0],p.r[1]), radius=p.promien)  # kolko tam gdzie jest czastka
            a.add_patch(cir)                 # dodaj to kolko do rysunku
            plt.plot()                              # narysuj
            plt.xlim((0,boxsize))                # obszar do narysowania
            plt.ylim((0,boxsize))    
            F.set_size_inches((6,6))        # rozmiar rysunku
            nStr=str(en)     #nagraj na dysk - numer pliku z 5 cyframi, na poczatku zera, np 00324.png
            nStr=nStr.rjust(5,'0')
            plt.title("Symulacja gazu Lennarda-Jonesa, krok "+nStr)
            plt.savefig('img2/img'+nStr+'.png')



## inicjalizacja
t = 0
particles = []
t_temp_p = []
celllist={}
for i in range(sqpart):
    for j in range(sqpart):
        polozenie = np.array([(2*i+1),(2*j+1)])
        predkosc = np.array([(random.random()-0.5),(random.random()-0.5)])
        particles.append(czastka(promien,polozenie,predkosc))
skalowanko()
repopulate()

for i in range(7000):
    rysowanie(i)
    if (i%1000==0):
        repopulate()
    sily=[]
    rif = 0
    for p1 in particles:
        psila = np.array([0,0])
        for p2 in celllist[p1]:
            f=sila(p1.r-p2.r)
            psila += f
            rif -= np.dot(f,p1.r-p2.r)
        sily.append(psila)
    j = 0
    for p in particles:
        p.v += deltat*sily[j]/m
        p.r = pbc(p.v*deltat + p.r)
        j += 1
    tempe=skalowanko()
    t_temp_p.append((deltat*i,tempe,(tempe*particleNumber+0.25*rif)/boxsize/boxsize))

t = [t_temp_p[x][0] for x in range(len(t_temp_p))]
te = [t_temp_p[x][1] for x in range(len(t_temp_p))]
p = [t_temp_p[x][2] for x in range(len(t_temp_p))]
plt.clf()
F = plt.gcf()
F.set_size_inches((14,6))
plt.subplot(211)
plt.plot(t,te, color="r", linestyle="-", linewidth=2)
plt.subplot(212)
plt.plot(t,p, color="r", linestyle="-", linewidth=2)
plt.savefig('img2/pt.png')
