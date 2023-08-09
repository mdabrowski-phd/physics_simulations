#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 12 (pryzma piasku Baka)
import sys, math
import matplotlib.pyplot as plt 
from numpy import *

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/python/cwiczenia12/"

#stale fizyczne i warunki poczatkowe
N=31
T=10000
c=4

law=zeros((N**2)+1)	#parametry symulacji
s=0
liczba=zeros(T)
M=zeros([N,N])

for i in xrange(T):
	random.seed()
	x=int(random.random()*N)
	y=int(random.random()*N)
	M[x][y]+=1
	flag=True
	s=0
	A=zeros([N,N])
	while flag:
		tabx,taby=nonzero(M>=c)
		n=tabx.size
		if(n==0):
			flag=False
		else:
			for j in xrange(n):
				a=tabx[j]
				b=taby[j]
				A[a][b]=1
				M[a][b]-=4
				if(a+1)<N:
                   			M[a+1][b]+=1
                		if(a-1)>=0:    
                    			M[a-1][b]+=1
                		if(b+1)<N:
                    			M[a][b+1]+=1
                		if(b-1)>=0:
                    			M[a][b-1]+=1
	if i>4000:
		s=sum(A)
        	law[s]+=1
	liczba[i]=sum(M)

#tworzenie i rysowanie wykresow
t=linspace(0,T-1,T)
ss=linspace(0,(N**2),(N**2)+1)
ls=log(ss)
ll=log(law)

plt.subplot(211)
plt.plot(t,liczba,'r-')
plt.title("Liczba ziarenek piasku w funkcji czasu")
plt.xlabel("czas t")
plt.ylabel("liczba ziarenek N")
plt.subplot(212)
plt.plot(ls,ll,'b-')
plt.title("Liczba lawin danego rozmiaru")
plt.xlabel("rozmiar lawiny")
plt.ylabel("liczba lawin")
plt.savefig(folder + "lawiny.pdf", format="pdf")
plt.show()









		



	



