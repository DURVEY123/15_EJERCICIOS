# Máximo común divisor (MCD): Encuentra el MCD de dos números utilizando el algoritmo de Euclides con un ciclo while, 
# que repite el cálculo del residuo hasta que uno de los números sea cero.
print ( "ingrese el numero a: ")
A = int(input())
print ("ingrese el numero b: ")
B = int(input ())

a, b = A, B

if a<b:
    a, b = b, a
while b > 0: 
    a, b = b, a % b

print (f"mcd {A},{B} = {a}")        
