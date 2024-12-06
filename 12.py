# Número más grande en una lista: Compara los números de una lista uno por uno utilizando un ciclo for
# para encontrar el mayor de ellos.
numeros = (12,68,35,18,95)
maximo = (0)
for numero in numeros: 
   if numero > maximo:
     maximo = numero
print (f"el numero mayor es: {maximo}")