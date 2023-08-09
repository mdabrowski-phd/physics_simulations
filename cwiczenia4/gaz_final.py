#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 4 (gaz dwuwymiarowy + termostat Browna-Clarka
import math
import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.patches import Circle
from numpy import *

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/python/cwiczenia4/final/"

#stale fizyczne i warunki poczatkowe
particleNumber=16
nx=4
ny=4
b=8.0
t=0
en=0
eps=1.0
sigma=1.0
radius=0.5
deltat=0.001
temp=0.7
delta=b/nx
E_p=0
E_k=0
czasy=[]
kin=[]
pot=[]
cal=[]
particles=[]
pred=[]
radials=[]
delg=0.1
bins=np.arange(0,b/2.,delg)

#klasa czastka
class czastka:
    """ Klasa opisujaca pojedyncza czastke gazu"""
    def __init__(self,radius,pos,vel):
        self.promien=radius
        self.r=pos
        self.v=vel
        self.sila=np.array([0.,0.])
        self.vm=0.
        self.vp=0.

#sila Lennarda-Jonesa
def F(R,r):
    f=-48*eps/sigma**2*((sigma/r)**14-1./2*(sigma/r)**8)*R
    return f

#potencjal Lennarda-Jonesa
def U(r):
    u=4*eps*((sigma/r)**12-(sigma/r)**6)
    return u

#inicjalizacja siatki czastek
for i in range(nx):
    for j in range(ny):
        polozenie=np.array([i*delta+1,j*delta+1])
        predkosc=np.array([(random.random()-1./2),(random.random()-1./2)])
        particles.append(czastka(radius,polozenie,predkosc))

#skalowanie temperatury po inicjalizacji
sumv=0.
sumv2=0.
for p in particles:
    sumv=sumv+p.v
sumv=sumv/particleNumber
for p in particles:
    p.v=p.v-sumv
for p in particles:
    sumv2=sumv2+np.dot(p.v,p.v)/2.0
sumv2=sumv2/particleNumber
fs=math.sqrt(temp/sumv2)
for p in particles:
    p.v=p.v*fs

#rozklad predkosci Maxwella
x=np.arange(0.0, 3.0, 0.01)
y=(x/temp)*exp(-x**2/(2.0*temp))

#glowna petla programu
i=0
while t<25:
    for p in particles:
        for k in particles:
            if p<k:
                #periodyczne warunki brzegowe (PDC)
                r_vect=k.r-p.r
                if r_vect[0]>b/2:
                    r_vect[0]=r_vect[0]-b
                elif r_vect[0]<-b/2:
                    r_vect[0]=r_vect[0]+b
                if r_vect[1]>b/2:
                    r_vect[1]=r_vect[1]-b
                elif r_vect[1]<-b/2:
                    r_vect[1]=r_vect[1]+b
		#aktualizacja radialnej funkcji rozkladu
                odl=np.sqrt(np.dot(r_vect,r_vect))
                if t>3:
                    if(en%1000==0):
                        radials.append(odl)
                #obciecie sily Lennarda-Jonesa
                if odl<=2.5*sigma:
                    f=F(r_vect,odl)
                    p.sila=p.sila+f
                    k.sila=k.sila-f
                    if(en%50==0):
                        E_p=E_p+U(odl)
    #krok startowy algorytmu Leapfrog
    if i==0:
        for p in particles:
            p.vp=p.v-1./2*p.sila*deltat
            i=1
    #energia kinetyczna
    sumv2=0.             
    for p in particles:        
        p.vm=p.vp
        p.v=p.vp+1./2*p.sila*deltat
        sumv2=sumv2+np.dot(p.v,p.v)/2.0
    #obliczanie czynnika skalujacego predkosc
    tau=sumv2/(eps*particleNumber)
    eta=np.sqrt(temp/tau)
    #algorytm Leapfrog - termostat Browna-Clarka
    for p in particles:
        p.vp=(2*eta-1)*p.vp+eta*p.sila*deltat
        p.r=p.r+p.vp*deltat 
	#dynamika ukladu czastek (najblizszy obraz)
        if p.r[0]>b:
            p.r[0]-=b
        if p.r[0]<0:
            p.r[0]+=b
        if p.r[1]>b:
            p.r[1]-=b
        if p.r[1]<0:
            p.r[1]+ b
        p.sila=np.array([0.,0.])
        p.v=1./2*(p.vm+p.vp)
        ve=np.dot(p.v,p.v)
	#aktualizacja tablicy predkosci
        if(t>3):
            pred.append(np.sqrt(ve))
	#aktualizacja energii kinetycznej
        if(en%50==0):
            E_k=E_k+1./2*ve
    #aktualizacja wyswietlania danych
    if(en%50==0):
        E_c=E_k+E_p
        czasy.append(t)
        kin.append(E_k)
        pot.append(E_p)
        cal.append(E_c)
        E_p=0.
        E_k=0.
	#rysowanie klatek animacji
        plt.clf()
        A=plt.gcf()
        for a in range(particleNumber):
            p=particles[a]
            a=plt.gca()
            cir=Circle((p.r[0],p.r[1]),radius=p.promien)
            a.add_patch(cir)
            plt.plot()
        plt.xlim((0,b))
        plt.ylim((0,b))
        A.set_size_inches((6,6))
        nStr=str(en)
        nStr=nStr.rjust(5,'0')
        plt.title("Symulacja gazu Lennarda-Jonesa, krok "+nStr)
        plt.savefig(folder+'animacja/img'+nStr+'.png')
        plt.clf()
    #po osiagnieciu stanu rownowagi
    if(t > 3):
        if(en%1000==0):
	    #rysowanie histogramu predkosci
            plt.hist(pred,bins=20,normed=True)
	    plt.plot(x,y,'r-',lw=3)
            plt.title("Symulacja gazu, krok "+nStr)
            plt.savefig(folder+'predkosc/maxwell'+nStr+'.png')
            plt.clf()
            #pred=[]
	    #rysowanie histogramu radialnej funkcji rozkladu
            histp,bin_edges=np.histogram(radials,bins=bins,normed=True)
            histn=[0]*len(histp)
            for i in range(0,len(histp)):
                fg=np.pi*(((i+1)**2-i**2)*delg**2)*particleNumber/(b**2)
                histn[i]=histp[i]/(fg)
            plt.plot(.5*(bin_edges[1:]+bin_edges[:-1]),histn)
            plt.title("Radialna funkcja rozkladu, krok "+nStr)
            plt.savefig(folder+'/rozklad/radial'+nStr+'.png')
            #radials=[]
    #zwiekszenie parametrow na koncu glownej petli
    t=t+deltat
    en=en+1

#rysowanie energii od czasu
plt.clf()
plt.plot(czasy,kin,czasy,pot,czasy,cal)
plt.legend(("T", "V", "T+V"))
plt.savefig(folder+'energia.png')
