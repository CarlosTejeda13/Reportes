# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:18:06 2020

@author: Carlos Tejeda
"""

import matplotlib.pyplot as plt
import numpy as np

def trapecio(n,x,fx,t):
    sum =0
    for i in range (1,n):
        sum=sum+fx[i]
    I=(x[n]-x[0])*(fx[0]+2*sum+fx[n])/(2*t)
    return I

num = int(input("Numero de datos para analizar " ))
h=float(input("Ancho de los trapecios "))
n= num
x= np.zeros([n])
fx= np.zeros([n])
print("Introduzca los datos ")
for i in range (0,n):
    x[i]=input("x["+str(i)+"]= ")
    fx[i]=input("fx["+str(i)+"]= ")
 #ajuste respecto a la pocision   
n=num-1
t=(x[n]-x[0])/h
print("El valor de la integral: ",trapecio(n,x,fx,t))
#Grafica
plt.plot(x,fx)
plt.ylabel("f(x)")
plt.xlabel("x")
plt.show