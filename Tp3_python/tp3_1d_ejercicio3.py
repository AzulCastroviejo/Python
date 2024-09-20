#ejercicio 3: Invertir una Lista
#Escribe un programa que permita al usuario ingresar una lista y la invierta.

num = int(input("Ingresa la cantidad de elementos que ingresaaras el la lista :"))
lista = []

for elemento in range(0,num):
    lista.append(int(input(f"Ingresa el número ")))
    
print(lista)
lista.reverse()
print(f"La lista a la reversa es : {lista}")
    