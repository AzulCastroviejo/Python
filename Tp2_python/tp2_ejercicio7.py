#7- Solicite el ingreso de una cadena y determine el tamaño de la misma y cuantas 
#vocales tiene en total
frase = input("Ingrese la frase que desee :")
caracteres = len(frase)
x = 0
sin_espacio = ""
for i in frase:
    if  i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        x+=1
        sin_espacio += i
        
print(f"La cadena tiene {caracteres} caracteres")
print(f"La cadena tiene {len(sin_espacio)} caracteres sin espacios")
print(f"Tiene {x} vocales")