#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 7 (model perkolacji)
from scipy import linspace, polyfit, randn
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import random
import math

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/python/cwiczenia7/"

#stale fizyczne i warunki poczatkowe
z = 200
p = 0.7
N = []
X = []
Y = []

#inicjalizacja macierzy sasiadow
def Macierz(z):
    M = (-1)*np.ones((z, z))
    for i in range(z):
        M[0, i] = - 2
        M[i, 0] = - 2
        M[z-1, i] = - 2
        M[i, z-1] = - 2    
    return M

#zaznaczanie nieodwiedzonych sasiadow
def Punkt(M, x, y, X, Y, N):
    if random.random() < p:
        M[x, y] = 1
        N.append((x,y))
        X.append(x)
        Y.append(y)   
    else:
        M[x, y] = 0 
    return M, X, Y, N

#wyznaczanie punktu poczatkowego
A = Macierz(z)
A[z/2 - 1, z/2 - 1] = 1
N.append((z/2 - 1,z/2 - 1))
X.append(z/2 - 1)
Y.append(z/2 - 1)

#przeszukiwanie macierzy sasiadow
while True:
    for i in range(len(N)):
        a, b = N.pop()
        if A[a-1, b] == -1:
            Punkt(A, a-1, b, X, Y, N)
        if A[a+1, b] == -1:
            Punkt(A, a+1, b, X, Y, N)
        if A[a, b-1] == -1:
            Punkt(A, a, b-1, X, Y, N)    
        if A[a, b+1] == -1:
            Punkt(A, a, b+1, X, Y, N) 
    if len(N) == 0:
        break

#rysowanie wykresu pikselowego
image = Image.new("L", (z, z), 255)
for i in range(len(X)):
    image.putpixel((X[i], Y[i]), 0)
image.save(folder+"zad1_p="+str(p)+".png", format="png")
