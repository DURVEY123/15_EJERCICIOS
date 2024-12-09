# Promedio ponderado: Calcula el promedio ponderado de una lista de calificaciones. 
# Multiplica cada calificación por su peso en un ciclo for y divide entre el total de pesos.

calificaciones=[10, 30, 40, 50]
pesos= [0.1,0.2,0.3,0.4]
promedio_ponderado=0

for i in range (len(calificaciones)) :
      promedio_ponderado += calificaciones[i] * pesos[i]
      
print(f"El promedio ponderado es: {promedio_ponderado}")