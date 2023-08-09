#!/usr/bin/env python

#Michal Dabrowski, cwiczenia 6 (Obliczanie wymiaru pudelkowego)
import math, random
import matplotlib.pyplot as plt 
from matplotlib.patches import Circle
from numpy import *
from scipy import polyfit,linspace
from matplotlib.pyplot import plot, title, show, legend

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/python/cwiczenia6/"

#dane do wytworzenia obrazu fraktalnego
m0=array([0.5, 0, 0, 0.5, 0, 0])
m1=array([0.5, 0, 0, 0.5, 0.5, 0])
m2=array([0.5, 0, 0, 0.5, 0.25, math.sqrt(3.)/4])
p1=1./3.
p2=1./3.
p3=1./3.

#stale fizyczne i warunki poczatkowe
xmin=100.
xmax=-100.
ymin=100.
ymax=-100.
x=[0,0]
c1,c2=[],[]
xdat,ydat=[],[]

#transformacja punktow z poprzedniej iteracji
def transform (x,m) :
    return ([m[0]*x[0]+m[1]*x[1]+m[4],m[2]*x[0]+m[3]*x[1]+m[5]])

i=0
while i < 100000 :
    #losowanie transformacji do tworzenia fraktal
    aux = random.uniform(0,1.)
    if (aux <= p1) :
        m = m0
    elif (aux <= p1+p2) :
        m = m1
    elif (aux <= 1) :
	m = m2
    x = transform(x,m)
    c1.append(x[0])
    c2.append(x[1])
    #dopasowanie rozmiaru obrazka do okna wykresu
    if (x[0]>xmax) :
        xmax=x[0]
    if (x[0]<xmin) :
        xmin=x[0]
    if (x[1]>ymax) :
        ymax=x[1]
    if (x[1]<ymin) :
        ymin=x[1]
    i+=1

#obliczanie wymiaru pudelkowego
r = 1
while r <= 9 :
    N = 2**r
    delx = (xmax-xmin)/N
    dely = (ymax-ymin)/N
    pud = [[0 for col in range(N)] for row in range(N)]
    
    for i in range(100000) :
        d = int((c1[i]-xmin)/delx)
        e = int((c2[i]-ymin)/dely)
        if d==N :
            d=d-1
        if e==N :
            e=e-1
        pud[d][e]=1

    #sumowanie punktow brzegowych fraktali
    Nr = 0
    for i in range(N) :
        for j in range(N) :
            if pud[i][j]==1 :
                Nr += 1
    
    #zapisywanie danych do wykresu
    xdat.append(r*log(2.))
    ydat.append(log(Nr))
    r+=1

#dopasowanie prostej do danych z symulacji
(ar,br)=polyfit(xdat,ydat,1)
yfit=[]
for x in xdat:
  yfit.append(ar*x+br)

#rysowanie wykresu punktowego
plot(xdat,ydat,'k.')
plot(xdat,yfit,'r-')
title('Linear regression, dim='+str(ar))
legend(['noisy data', 'fit'],loc='best')
plt.savefig(folder+"dywan_dim.pdf", format="pdf")
show()
