# Suma de los dígitos de un número con ciclos: Extrae cada dígito de un número 
# utilizando operaciones matemáticas y acumula su suma dentro de un ciclo.
# Número que deseas procesar
numero = 12345
suma_digitos = 0

while numero > 0:
    digito = numero % 10 
    suma_digitos += digito  
    numero = numero // 10  
print("La suma de los dígitos es:", suma_digitos)