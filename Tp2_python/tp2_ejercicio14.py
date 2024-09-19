# 14- Indique si en Python existen o no variables de tipo valor y su contraparte tipo 
#referencia como sucede en otros lenguajes como Java.
# -----------------------------------------------------------------------------
#Objetos inmutable  (como enteros, cadenas, tuplas): Cualquier modificación dentro de la función crea un nuevo objeto, dejando el original sin cambios.
#Objetos mutables (como listas, diccionarios): Las modificaciones dentro de la función afectan al objeto original porque se pasa una referencia al objeto.

#Tipos de Valor: No se modifican cuando son pasados como parámetros, porque la función recibe una copia.

def duplicar_numero(num):
    num += 2
    print("Dentro de la función:", num)

x = 10
duplicar_numero(x)
print("Fuera de la función:", x)  # x sigue siendo 10

#Tipos de Referencia: Sí se modifican cuando son pasados como parámetros, porque la función recibe 
# una copia de la referencia, que apunta a los mismos datos.

def modificar_lista(lista):
    lista.append(4)
    print("Dentro de la función:", lista)

mi_lista = [1, 2, 3]
print(mi_lista)
modificar_lista(mi_lista)
print("Fuera de la función:", mi_lista)  # mi_lista se modifica