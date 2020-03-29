# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 20:58:14 2019

@author: Carlos Tejeda
"""

producto1 ="Cafe"
producto2 ="Cafe con leche"
producto3 ="Chocolate"

precio1= 10
precio2= 15
precio3= 12

opcion ="1"
total=0

#Bucle de repeticion del programa
while (opcion != "0"): #Mientras que la opcion no sea 0
    print ("Seleccione una opcion del Menu  ****--IMPORTE ACTUAL: $",total, "pesos--****\n")
    print ("\t1. ",producto1) # \t hace un salto en el tabulador ... \n un salto de linea
    print ("\t2. ",producto2)
    print ("\t3. ",producto3)
    print ("\t4. Salir ")
    opcion = input() #Haga su eleccion
    
    
    if(opcion == "1"):
        print ("\n Ha elegido ", producto1, "cuesta $ ", precio1, "Pesos" )
        total = total+precio1
    elif(opcion =="2"):
        print ("\n Ha elegido ", producto2, "cuesta $ ", precio2, "Pesos" )
        total = total+precio2
    elif (opcion == "3"):
        print ("\n Ha elegido ", producto3, "cuesta $ ", precio3, "Pesos" )
        total = total+precio3
    elif(opcion =="4"):
        print ("\n Compra finalizada, el costo total es de $ ", total ," pesos\n")
        break #Finalizar el Programa
    else:
        ("\n Opcion no reconocida")
    input("\n\n Presione Enter para continuar")
    

      
    
