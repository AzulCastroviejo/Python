#Ejercicio 6: Eliminar Duplicados
#Escribe un programa que permita al usuario ingresar una lista de números y elimine los 
#elementos duplicados.
#Pista:
# Utiliza la función set().

lista = []
num =1
print("Ingresa los numeros que desees a la lista , cuando temines ingresa 0")

while num != 0:
    num = int(input("Ingresa el número a la lista : "))
    lista.append(num)
    
lista = set(lista)  # set(lista) elimina duplicados en la lista 
print(f"La lista de números es : {lista}")