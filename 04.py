#Suma de los dígitos de un número:
# Recorre cada dígito de un número (convirtiéndolo en una cadena de texto) y
# suma sus valores utilizando un ciclo for.
numero_str = str(1234)
suma = 0
for digito in numero_str:
    print (digito)
    suma += int (digito)
print(f"la suma es: {suma}")