#5- Solicite el ingreso de una cadena y elimine todos los espacios de la misma, muestre 
#la cadena resultant

cadena = input("Ingrese una frase :")
largo = len(cadena)
espacio = " "
cadena_sin_es= ""

#       cadena_sin remplaza todos los espacios por ninguno
#cadena_sin= cadena.replace(" ", "")
#print(cadena_sin)

#       se crea una nueva cadena nueva sin incluir los espacios
for x in cadena :
    if x != espacio:
        cadena_sin_es += x

print(cadena_sin_es)

