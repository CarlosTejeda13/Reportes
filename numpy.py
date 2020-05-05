# -*- coding: utf-8 -*-
"""
Created on Sat May  2 20:52:09 2020

@author: Carlos Tejeda
"""

import math
import numpy as np
from matplotlib import pyplot as plt

x = np.array(range(100))*0.1
y = np.zeros(len(x))
for i in range(len(x)):
    y[i]=math.sin(x[i])
    
plt.ion()
plt.plot(x,y)
plt.xlabel("Tiempo")
plt.ylabel("Distancia")
