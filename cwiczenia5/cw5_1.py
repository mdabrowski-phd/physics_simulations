#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 5 (rownanie Duffinga)
import sys, math, os
import matplotlib.pyplot as plt 
import numpy as np
from numpy import *
from scipy import integrate

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/python/cwiczenia5/"

#stale fizyczne i warunki poczatkowe
a=1.
b=1.
c=0.2
w=2*math.pi*0.2
f=0.2

X0 = array([0, 0.1])
t = linspace(0, 1000, 1000000)


#rozwiazywanie rownania Duffinga
def dX_dt(X, t=0):
  return array([X[1], b*X[0]-a*X[0]**3-c*X[1]+f*math.cos(w*t)])

#obliczanie macierzy Jacobiego
def d2X_dt2(X, t=0):
  return array([[0,1], [b-3*a*X[0]**2,-c]])

    
X = integrate.odeint(dX_dt, X0, t, Dfun=d2X_dt2)
x,v = X.T

#rysowanie wykresow fazowych
plt.plot(x,v, "r-", lw=2)
plt.title("Diagram fazowy rownania Duffinga, f="+str(f))
plt.xlabel("polozenie $x(t)$",fontsize=14)
plt.ylabel("predkosc $v(t)$",fontsize=14)
plt.grid(True)
plt.savefig(folder+"zad1.pdf", format="pdf")
plt.show()


