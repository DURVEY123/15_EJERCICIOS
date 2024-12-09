#Verificación de número primo:
# Usa un ciclo for para verificar si un número es divisible por algún número entre 2 y su raíz cuadrada.
# Si no tiene divisores, es primo.
from math import sqrt

print ("ingrese el numero: ")
numero = int (input ())
divisores = 0
sqr=int(sqrt(numero)) 
for i in range(2,sqr+1):
    if numero % i == 0:
        divisores = divisores + 1

if divisores == 0:
    print ("Es primo")
else:
    print ("No es primo")            