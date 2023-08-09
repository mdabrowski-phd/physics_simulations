#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 13 (automat komorkowy 122R)
import sys, math
import matplotlib.pyplot as plt 
from numpy import *
from pylab import *
from math import *
import Image, ImageDraw

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/laboratorium/cwiczenia13/"

#stale fizyczne i warunki poczatkowe
M=15000
N=500
T=zeros([M,N])
en=zeros(M)
d=5

#ustalanie poczatkowego stanu automatu
for i in xrange(41):
	T[0][N/2-20+i]=1
	T[1][N/2-20+i]=1

#ewolucja automatu komorkowego
for m in range(2,M,1):
#for m in arange(M-2)+2:
	for n in xrange(N):
		T[m][n]=4*T[m-1][(n-1+N)%N]+2*T[m-1][n]+T[m-1][(n+1)%N]
		if(T[m][n]==0 or T[m][n]==2 or T[m][n]==7):
			T[m][n]=T[m-2][n]
		else:
			T[m][n]=(1+T[m-2][n])%2
		#obliczanie gruboziarnistej entropii
	for k in arange(N/d):
		r=sum(T[m][k*d:(k+1)*d])
		en[m]+=log(1.*factorial(d)/(factorial(r)*factorial(d-r)))

#rysowanie ewolucji automatu w czasie
img=Image.new("RGB",(N,M),(255,255,255))
draw = ImageDraw.Draw(img)
for y in range(M):
	for x in range(N):
		if T[y][x]:
			draw.point((x,y),(0,0,0))
img.save(folder+"122R.png")

#rysowanie wykresow entropii w czasie
p=300
en1=zeros(M-p)
for i in xrange(M-p):
	en1[i]=1.*sum(en[i:p+i])/p

plt.subplot(211)
plt.title("Zmiana gruboziarnistej entropii w czasie")
plot(en)
plt.grid(True)
plt.ylabel("aktualna entropia S")
plt.subplot(212)
plot(en1)
plt.grid(True)
plt.xlabel("czas t")
plt.ylabel("usredniona entropia S")
plt.savefig(folder + "entropia.pdf", format="pdf")
plt.show()
