#8- Reemplaza todas las vocales a de una cadena ingresada por teclado por una vocal e

frase = input("Ingrese la frase que desee :")
cadena = ""
for i in frase:

    if  i == "a":
        cadena += i.replace("a","e")
    else:
        cadena += i 
        
print(cadena)