# Cantidad de dígitos de un número: Usa un ciclo for para recorrer los caracteres
#  de un número convertido  a cadena de texto y cuenta cuántos tiene.
n = str(2380923)
cadena = str(n)
contador= 0
for letras in cadena:
    contador +=1
print(f"la cantidad de digitos en el numero es: {contador} ")