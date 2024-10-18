#Ejercicio 10: Eliminar un Elemento por su Índice
#Escribe un programa que permita al usuario ingresar una lista de números y eliminar 
#un elemento en un índice especificado.

lista = []
num = ""
print("Ingresa los números que desees a la lista , cuando temines ingresa 0")

while num != 0:
    num = int(input("Ingresa el número a la lista : "))
    if num != 0:
        lista.append(num)  

print(lista)    
indice = (int(input(f"Ingresa el indice del elemento que deseas eliminar hasta el {len(lista)} - "))) -1 
del lista[indice]# ELIMINA EN LISTA POR INDICE

print(lista)