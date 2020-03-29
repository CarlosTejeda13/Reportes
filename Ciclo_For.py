# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 08:35:01 2020

@author: Carlos Tejeda
"""
res="Si"
while (res != "No"):
    print ("Ingrese el nombre del alumno")
    nomb=input()
    print ("Cuantas calificaciones va a promediar")
    nucal= input()
    nucal=int(nucal)
    
    suma=0
    for i in range(1,nucal+1):
        print ("Ingresa la ",i,"a. Calificacion")
        calif=input()
        calif=float(calif)
        suma=suma+calif
    promedio =suma/nucal

    if(promedio>=70):
      print ("El alumno", nomb,"tiene un primedio de ",promedio, " y es aprobatorio")
      
    else: 
      print ("El alumno", nomb,"tiene un primedio de ",promedio, " y es reprobatorio \n")
    print ("Desea agregar otro alumno: (Si/No)?")
    res=input()