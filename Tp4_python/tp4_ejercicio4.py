#a) Verifica si el color "morado" está presente en la tupla.
#b) Verifica si el color "azul" está presente en la tupla.
#c) Imprime el resultado de ambas verificaciones.

colores = ( "rojo","verde", "azul","amarillo")
morado = "morado" in colores

if "azul" in colores :
    print("Se encuentra el azul en la tupla")
else:
    print("No se encuantra el azul en la tupla")
    
if morado == False :
    print(f"En la tupla no hay morado")
else:
    print("En la tupla hay morado")
    