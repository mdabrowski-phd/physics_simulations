#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 6 (Metoda IFS tworzenia fraktali)
import sys
import math as mt
import matplotlib.pyplot as plt 
from numpy import *
from scipy import linspace, polyfit, randn
from matplotlib.pyplot import plot, title, show, legend

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/python/cwiczenia6/"

#stale fizyczne i warunki poczatkowe
T=300000
m4=0.
m5=0.
m0=[ 0.0, 0.0, 0.0, 0.16, 0.0, 0.0] 
m1=[ 0.85, 0.04,-0.04, 0.85, 0.0, 1.6] 
m2=[ 0.2,-0.26, 0.23, 0.22, 0.0, 1.6] 
m3=[-0.15, 0.28, 0.26, 0.24, 0.0, 0.44] 
p1=0.03
p2=0.73
p3=0.13
p4=0.11
punkt=[]
punkt.append(array([m4,m5]))

xmax=-10000.0
xmin=10000.0
ymax=-10000.0
ymin=10000.0

#losowanie transformacji do tworzenia fraktali
def losuj():
  random.seed()
  p=random.random()
  if p<p1:
    return m0
  elif p<(p1+p2):
    return m1
  elif p<(p1+p2+p3):
    return m2
  elif p<1:
    return m3

#transformacja punktow z poprzedniej iteracji
def tran(i):
  m=losuj()
  point=array([0.0,0.0])
  point[0]=punkt[i][0]*m[0]+m[1]*punkt[i][1]+m[4]
  point[1]=punkt[i][0]*m[2]+m[3]*punkt[i][1]+m[5]
  punkt.append(point)

#dopasowanie rozmiaru obrazka do okna wykresu
for i in xrange(T):
  tran(i)
  if punkt[i][0]<xmin:
    xmin=punkt[i][0]
  if punkt[i][1]<ymin:
    ymin=punkt[i][1]

for i in xrange(T):
  punkt[i][0]=punkt[i][0]-xmin
  punkt[i][1]=punkt[i][1]-ymin
  if punkt[i][0]>xmax:
     xmax=punkt[i][0]
  if punkt[i][1]>ymax:
     ymax=punkt[i][1]
  
for i in xrange(T):  
  punkt[i][0]=punkt[i][0]*511/xmax
  punkt[i][1]=punkt[i][1]*511/ymax

#obliczanie wymiaru pudelkowego
ss=2    
ll=10
N =[0]*(ll-ss)
ydat=[0]*(ll-ss)
for l in xrange(ss,ll,1):
  A =[None]*l
  for i in range(l):
      A[i]=[False]*l
  d=512.0/l
  for i in xrange(T):
      k=int(punkt[i][0]/d)
      m=int(punkt[i][1]/d)
      if A[k][m]==False:
        A[k][m]=True
        N[l-ss]=N[l-ss]+1
for i in xrange(ll-ss):
  ydat[i]=mt.log(N[i],2)
        
#dopasowanie prostej do danych z symulacji
x=linspace(ss,ll-1,ll-ss)
a=mt.log(2,2); b=0
(ar,br)=polyfit(x,ydat,1)
yfit= ar*x+br
print('Linear regression using polyfit')
print('parameters: a=%.2f b=%.2f \tregression: a=%.2f b=%.2f' % (a,b,ar,br))
title('Linear regression')
plot(x,ydat,'k.')
plot(x,yfit,'r-')
legend(['noisy data', 'fit'],loc='best')
plt.savefig(folder+"paprotka_dim.pdf", format="pdf")       
            
#rysowanie wykresu pikselowego
from PIL import Image
Nimg = 512
image = Image.new("L",(Nimg, Nimg),255)
for i in xrange(T):
    image.putpixel((int(punkt[i][0]),int(punkt[i][1])),0)
image.save(folder+"paprotka.png","PNG")
show()
