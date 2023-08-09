#!/usr/bin/env python           

#Michal Dabrowski, cwiczenia 10 (agregacja limitowana dyfuzja, zadanie 2)
import numpy as np
import random
import math
from scipy import linspace, polyfit
import matplotlib.pyplot as plt
from PIL import Image

#folder zapisu rysunkow
folder="C:/Users/michal/Documents/studia/fizyka_komputerowa/symulacje_komputerowe/2012/python/cwiczenia10/"

#stale fizyczne i warunki poczatkowe
dl = 1000	#rozmiar siatki agregatu
delta = dl/2
X = [0]
Y = [0]
R0 = 10.	#promien poczatkowego okregu
R1 = 20.	#promien granicznego okregu
p0 = 0.01

#tworzenie nowego rysunku pikselowego
image = Image.new("L", (dl, dl), 255)
image.putpixel((delta, delta), 0)

#wpuszaczanie kolejnych czastek do ukladu
for i in range(100001):
    P = 2 * math.pi*np.random.rand()	#losowanie polozenia poczatkowego
    x = int(math.ceil(math.cos(P)*R0))
    y = int(math.ceil(math.sin(P)*R0))
    czy = True				#czy czastka aktywna?
    
    while czy:		#jezeli czastka w obszarze agregatu
        ro = math.sqrt(x**2 + y**2)	#aktualne polozenie czastki
        if ro > R1:	
            break
        #algorytm bladzenie losowego
        w = random.randint(1,4)
        xs = x
        ys = y
        if w == 1:
            x = x + 1
        if w == 2:
            x = x - 1
        if w == 3:
            y = y + 1 
        if w == 4: 
            y = y - 1
	#algorytm powiekszania agregatu
        if ro <= R0 + 1:
            p = np.random.rand()
            for z in reversed(range(len(X))):
                if (x == X[z]) and (y == Y[z]):
                    if p <= p0:
                        czy = False
                        X.append(xs)	#przylacz czastke do agregatu
                        Y.append(ys)
                        image.putpixel((xs + delta, ys + delta), 0)
                        if ro > R0:	#powieksz okrag poczatkowy i graniczny
                            R0 = ro + 5
                            R1 = 2*R0
                        break                    
                    else:	#przywroc polozenie z poprzedniego kroku
                        x = xs
                        y = ys
                        break
                        
    #rysowanie wykresu pikselowego
    if i%1000 == 0:
        nazwa = str(i)
        nazwa = nazwa.rjust(6, '0')
        image.save(folder+"/zad2/zad2_" + nazwa + ".png", "PNG")       
