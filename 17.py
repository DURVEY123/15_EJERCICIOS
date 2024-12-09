# Cantidad de vocales en una cadena: Recorre cada carácter de una cadena de texto con un ciclo for
# y cuenta cuántos de ellos son vocales.

texto = "el que no quiso cuando pudo no podra cuando quiere"
contador = 0
for caracter in texto:
       if caracter == "a": 
          contador +=1
       if caracter == "e":
          contador +=1
       if caracter == "i":
          contador +=1
       if caracter == "o":
          contador +=1
       if caracter == "u":
          contador +=1
print (f"La canitidad de vocales en la frase son: {contador}")