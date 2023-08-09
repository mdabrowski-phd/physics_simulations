#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 8 (model Isinga - scisle sumowanie)
import math as mt
import matplotlib.pyplot as plt 
from numpy import *

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/python/cwiczenia8/"

#stale fizyczne i warunki poczatkowe
L=4
Lbig=L
Nbig=L*L

for T in range(1,6):
	beta=1./T
	boltz=[0.0]*2**Nbig
        mag=[0.0]*2**Nbig
	#metoda scislego sumowania w modelu Isinga
	for k in xrange(2**Nbig):
	# przygotuj uklad s
    		l = list(bin(k))[2:]
    		s = array( ['0' for x in xrange(Nbig-len(l))]+l,dtype=int32 )
    		s = (s*2-1).reshape(Lbig,Lbig)
    		# sumuj spiny sasiadow
    		a = roll(s,1,axis=0)
    		a += roll(s,-1,axis=0)
    		a += roll(s,1,axis=1)
    		a += roll(s,-1,axis=1)
    		#oblicz czynnik Boltzmana
    		boltz[k] = exp(beta*sum(s*a)/2.)
    		# oblicz magnetyzacje
    		mag[k] = sum(s*1.0/Nbig)
	#obliczanie magnetyzacji
	Z=sum(boltz)
	m=0.
	m=sum(absolute(mag)*boltz)
	m=m/Z
	print("T = "+str(T)+"    m = "+str(m))
