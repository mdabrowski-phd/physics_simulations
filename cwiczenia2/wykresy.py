#!/usr/bin/env python

import math 
import matplotlib.pyplot as plt 
import numpy as np
xs = np.arange(-math.pi, math.pi, 0.1)
ys1 = np.sin(xs) 
ys2 = np.cos(xs)
plt.plot(xs, ys1, color="r", linestyle="-", linewidth=2)
plt.plot(xs, ys2, "g--", lw=1)
plt.xlabel("$x$",fontsize=14 ) 
plt.ylabel("$y$") 
plt.title("Funkcje: $\sin$ i $\cos$")
plt.grid(True) 
plt.legend(("$\sin(x)$", "$\cos(x)$")) 
plt.show()
