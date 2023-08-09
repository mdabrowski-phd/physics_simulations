#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 9 (algorytm klastrowy Wolffa)
import math as mt
import matplotlib.pyplot as plt 
from numpy import *
import numpy as np
import random
from PIL import Image

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/python/cwiczenia9/"

#stale fizyczne i warunki poczatkowe
L=100
temp=[1,2,2.4,3,4,5]	#tablica temperatur
newspin=0
s=[]
stos=[]
M=4000		#liczba krokow MonteCarlo
Nimg = 512	#rozmiar wykresu pikselowego

#tworzenie nowego klastra spinow
def klaster(L):
	l = list(bin(L))[2:]
	s = array( ['0' for x in xrange(L*L-len(l))]+l,dtype=int32 )
	s = (s*2-1).reshape(L,L)
	return s

#losowanie wezla sieci spinow
def los():
	random.seed()
	return int((random.random())*L)

#petla dla roznych temperatur
for T in temp:
	#inicjalizacja danych poczatkowych
	mag=0
	beta=1./T
	padd=1-exp(-2.0*beta)
	s=klaster(L)
	#wykonywanie kolejnych krokow MonteCarlo
	for k in xrange(M):
		a=los()
		b=los()
		newspin=-s[a][b]
		s[a][b]=-s[a][b]
		stos.append((a,b))
		#algorytm klastrowy Wolffa
		while True:
    			for i in range(len(stos)):
        			a, b = stos.pop()
				newspin=-s[a][b]
        			if s[(a-1)%L, b] == newspin:
	   				p=random.random()
	    				if (p<padd):
						s[(a-1)%L, b]=-s[(a-1)%L, b]
	       	    				stos.append(((a-1)%L, b))
        			if s[(a+1)%L, b] == newspin:
					p=random.random()
	    				if (p<padd):
						s[(a+1)%L, b]=-s[(a+1)%L, b]
	       	    				stos.append(((a+1)%L, b))
        			if s[a, (b-1)%L] == newspin:
					p=random.random()
	    				if (p<padd):
						s[a, (b-1)%L]=-s[a, (b-1)%L]
	       	    				stos.append((a, (b-1)%L))
   	     			if s[a, (b+1)%L] == newspin:
					p=random.random()
	    				if (p<padd):
						s[a, (b+1)%L]=-s[a, (b+1)%L]
	       	    				stos.append((a, (b+1)%L))
    			if len(stos) == 0:
        			break
		#obliczanie magnetyzacji
		if(k>1000):
			mag=mag+abs((sum(s*1.0/L/L)))
		#rysowanie wykresow pikselowych
		if(k%400==0):
			image = Image.new("L",(Nimg, Nimg),255)
			nStr=str(k)		
      			nStr=nStr.rjust(6,'0')	
			for i in range(L):
				for j in range(L):
					if(s[i][j]==1):
						image.putpixel((i, j), 0)
			image.save(folder+"T="+str(T)+"/wolf_T="+str(T)+"_"+nStr+".png")
	#wyswietlanie wynikow na ekranie
	print ("m(T="+str(T)+")="+str(1.0*mag/(M-1000)))
