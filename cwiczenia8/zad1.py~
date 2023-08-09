#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 8 (model Isinga - symulacja MonteCarlo)
import sys
import math as mt
import matplotlib.pyplot as plt 
from numpy import *

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/python/cwiczenia8/"

#stale fizyczne i warunki poczatkowe
L=4
h=1000
g=5000

#PDC + sumowanie po sasiadach
def dE(x,y):
	suma=0
	suma=s[x][(y-1)%L]+s[(x-1)%L][y]+s[(x+1)%L][y]+s[x][(y+1)%L]
	return 2*s[x][y]*suma
	
#generowanie liczb losowych
def los():
	random.seed()
	return int((random.random())*L)

#warunek odwracania spinu
def odw(E):
	random.seed()
	p=random.random()
	if (p<exp(-1.0*beta*E)):
		return True
	else:
		return False

#symulacja MonteCarlo odwracania spinow
def Mc():
	for i in xrange(L):
		for j in xrange(L):
			a=los()
			b=los()
			E=dE(a,b)
			if(E<=0):
				s[a][b]=s[a][b]*(-1)
			else:
				if odw(E):
					s[a][b]=s[a][b]*(-1)
	mag=(sum(s*1.0/L/L))
	return mag

for T in range(1,6):
	s = ones((L,L), dtype=int8) # siec spinow
	magnet=[0.0]*5000
	beta=1./T
	for i in xrange(g+h):
		m=Mc()
		if i>=h:
			magnet[i-h]=m
	wynik=(sum(absolute(magnet)))/(g)
	print("T = "+str(T)+"    m = "+str(wynik))
