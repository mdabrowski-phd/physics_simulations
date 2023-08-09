#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 13 (dowolny odwracalny automat komorkowy)
import sys, math
import matplotlib.pyplot as plt 
from numpy import *
import Image, ImageDraw

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/laboratorium/cwiczenia13/"

#stale fizyczne i warunki poczatkowe
M=15000
N=500
T=zeros([M,N])

#tworzenie regul na wybranego automatu komorkowego
def automat(nr):
	dic={}
	t=array(list(bin(nr)[2:]))		#konwersja do zapisu binarnego
	t=concatenate([zeros(8-len(t)),t])	#dopelnienie liczby zerami
	for i in xrange(8):
		dic[i]=t[7-i]	#odwrocenie kolejnosci cyfr liczby binarnej
	return dic

#wczytywanie informacji o numerze automatu
nr=int(sys.argv[1])
regula=automat(nr)

#ustalanie poczatkowego stanu automatu
for i in xrange(41):
	T[0][N/2-20+i]=1
	T[1][N/2-20+i]=1

#ewolucja automatu komorkowego
for m in range(2,M,1):
	for n in xrange(N):
		T[m][n]=4*T[m-1][(n-1+N)%N]+2*T[m-1][n]+T[m-1][(n+1)%N]
		T[m][n]=(int(regula[T[m][n]])+T[m-2][n])%2
		#T[m][n]=int(regula[T[m][n]])	#automat nieodwracalny

#rysowanie ewolucji automatu w czasie
img=Image.new("RGB",(N,M),(255,255,255))
draw = ImageDraw.Draw(img)
for y in range(M):
	for x in range(N):
		if T[y][x]:
			draw.point((x,y),(0,0,0))
img.save(folder+"automat_"+str(nr)+"_R.png")
