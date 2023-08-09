#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 5 (rownanie Duffinga)
import sys, math, os
import matplotlib.pyplot as plt 
import numpy as np
from numpy import *
from scipy import integrate
import pylab

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/python/cwiczenia5/"

#stale fizyczne i warunki poczatkowe
a=1.
b=1.
c=0.2
w=2*math.pi*0.2
f=0.3			#zachowanie chaotyczne
T = 2*math.pi/w		#przekroj Poincare
tmax=1000
MAX =int(tmax/T)
X0 = array([0, 0.1])
t = linspace(0, tmax, 1000*tmax)
xp=[]
vp=[]

#rozwiazywanie rownania Duffinga
def dX_dt(X, t=0):
  return array([X[1], b*X[0]-a*X[0]**3-c*X[1]+f*math.cos(w*t)])

#obliczanie macierzy Jacobiego
def d2X_dt2(X, t=0):
  return array([[0,1], [b-3*a*X[0]**2,-c]])

X = integrate.odeint(dX_dt, X0, t, Dfun=d2X_dt2)
x,v = X.T

#rysowanie wykresow fazowych
for m in xrange(MAX):
  xp.append(x[m*tmax*T])
  vp.append(v[m*tmax*T])
plt.scatter(xp, vp,s=5, facecolor='0.', lw=3)
plt.title("Przekroj Poincare rownania Duffinga, f="+str(f))
plt.xlabel("polozenie $x(t)$",fontsize=14)
plt.ylabel("predkosc $v(t)$",fontsize=14)
plt.grid(True)
plt.savefig(folder+"zad3_scatter.pdf", format="pdf")

#rysowanie wykresu pikselowego
from PIL import Image
Nimg=512
image=Image.new("L",(Nimg,Nimg),255)
for m in xrange(MAX):
  i=int(math.floor(tmax*m*T))
  image.putpixel((int(150*(x[i]+1.5)),int(150*(v[i]+1.5))),0)
image.save(folder+"zad3.png", format="png")
