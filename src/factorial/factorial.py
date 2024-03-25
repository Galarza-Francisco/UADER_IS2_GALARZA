#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 


##if len(sys.argv) == 1:
##   num = int(input("Debe ingresar un numero: ")) 
##else:
##    num = int(sys.argv[1])
##    sys.exit()


if len(sys.argv) == 1:
   min = int(input("Debe ingresar el numero minimo del rango: ")) 
else:
    min = int(sys.argv[1])
   #sys.exit()


for i in range (min,60+1):
    print("Factorial del nro",i, " es: ", factorial(i))