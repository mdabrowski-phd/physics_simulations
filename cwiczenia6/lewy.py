#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 6 (Metoda IFS tworzenia fraktali)
import sys
import math as mt
import matplotlib.pyplot as plt 
from numpy import *
from scipy import linspace, polyfit, randn
from matplotlib.pyplot import plot, title, show, legend
import numpy as np

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/python/cwiczenia6/"

#stale fizyczne i warunki poczatkowe
T=300000
m4=0.
m5=0.
m1 = [0.5, -0.5, 0.5, 0.5, 0.0, 0.0]
m2 = [0.5, 0.5, -0.5, 0.5, 0.5, 0.5]
p1 = 0.5
p2 = 0.5
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
    return m1
  elif p<(p1+p2):
    return m2

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

#rysowanie wykresu pikselowego
from PIL import Image
Nimg = 512
image = Image.new("L",(Nimg, Nimg),255)
for i in xrange(T):
    image.putpixel((int(punkt[i][0]),int(punkt[i][1])),0)
image.save(folder+"lewy.png","PNG")
show()
