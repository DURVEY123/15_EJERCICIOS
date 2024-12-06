# Media de una lista de números: Recorre cada elemento de una lista con un ciclo for, 
# acumula su suma y divide entre el número total de elementos para calcular la media
numeros = (1,2,3,4,5)
suma = 0 
for numero in numeros:
    suma += numero
media = suma / len(numeros)
print (media)