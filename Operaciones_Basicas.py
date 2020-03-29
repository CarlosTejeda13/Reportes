"""
Created on Sat Mar 28 07:25:51 2020

@author: Carlos Tejeda
"""


opc="1"

while (opc != "0"):
    print ("Que operaciòn deseas realizar:\n")

    print ("1.- Suma")
    print ("2.- Resta")
    print ("3.- Multiplicacion")
    print ("4.- Division")
    print ("5.- Salir")
    opc=input()

    
    if (opc=="1"):
      print ("Ingrese el primer dato a sumar")
      date= input()
      date = int(date)
      print ("Ingrese el segundo dato a sumar")
      date2=input ()
      date2 = int(date2)
      sumaw = date+date2
      print ("El resultado de la suma es:" ,sumaw)
    elif (opc=="2"):
      print ("ingrese el la primer cantidad:")
      numr= input()
      numr = int(numr)
      print ("Ingrese la cantidad a restar")
      restar= input()
      restar=int(restar)
      resta=numr-restar
      print ("La cantidad resatante es: ",resta)
    elif (opc=="3"):
      print ("Ingresa el primer nùmero que va a miltiplicar")
      mul = input()
      mul=int(mul)
      print ("Ingresa el segundo nùmero que va a miltiplicar")
      mul2=input()
      mul2=int(mul2)
      mult=mul*mul2
      print ("El resultado de la multiplicacion es:",mult)
    elif  (opc=="4"):
      print ("Ingresa el dividendo")
      div = input()
      div = int (div)
      print ("Ingresa el divisor")
      div2=input()
      div2=int(div2)
      divis=div/div2
      print ("El resultado de la multiplicaciòn es:",divis)
    elif (opc=="5"):
      print ("Ha seleccionado la opciòn de salir")
      break 