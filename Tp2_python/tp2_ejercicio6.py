#6- De la siguiente cadena “La lluvia en Mendoza es escasa” indique cual es el tamaño 
#de la cadena es decir su número de caracteres.

frase = "La lluvia en Mendoza es escasa"
print(frase)
caracteres = len(frase)
x = 0
sin_espacio = ""
for i in frase:
    if  i != " ":
        x+=1
        sin_espacio += i
        
print(f"Cantidad de caracteres con los espacios {caracteres}")
print(f"Cantidad de caracteres que ingresan al if {x}")
print(f"Caracteres en cadena nueva sin espacios {len(sin_espacio)}")

