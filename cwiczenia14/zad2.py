#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 14 (dynamika mapy kwantowej Chirikova)
import sys, cmath
import math as mt
import matplotlib.pyplot as plt 
from numpy import *
from scipy import *
from matplotlib.pyplot import *

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/laboratorium/cwiczenia14/"

#stale fizyczne i warunki poczatkowe
liczba=7
M=100
K=2.1
n0=15
l0=5
n=np.arange(M)

#tworzenie rozkladu Gaussa
def gauss(n):
	s=0
	L=-4
	while(L<5):
		s+=mt.exp(-mt.pi*(n-n0-L*M)**2/M)
		L+=1
	return cmath.exp(1j*2*mt.pi*l0*n/M)*s

#tworzenie znormalizowanego rozkladu Gaussa
def gauss_norm(n):
	su=0
	for i in xrange(M):
		su+=gauss(i).conjugate()*gauss(i)
	return gauss(n)/cmath.sqrt(su)

#obliczanie amplitudy prawdopodobienstwa
XX=[gauss_norm(i)*np.exp(-1j*M*K*mt.cos(2*mt.pi*i/M)/2*mt.pi) for i in n]
X=[i.conjugate()*i for i in XX]
X1=XX

wykres=['r','g','b','c','m','y','k']
#obliczanie ewolucji paczki falowej w czasie
for k in xrange(liczba):
	plt.plot(n,X,wykres[k])
	plt.title("Amplituda prawdopodobienstwa funkcji falowej, K="+str(K))
	plt.xlabel("polozenie paczki falowej")
	plt.ylabel("amplituda prawdopodobienstwa")
	plt.grid(True)
	plt.savefig(folder + "mapa2_"+str(k).rjust(1,'0')+".png", format="PNG")
	temp=np.exp(1j*mt.pi*n**2/M)*X1
	X1=np.exp(1j*mt.pi*n**2/M)*np.fft.fft(temp)/cmath.sqrt(M)
	X=[i.conjugate()*i for i in X1]
