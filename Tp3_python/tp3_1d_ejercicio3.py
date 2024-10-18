#ejercicio 3: Invertir una Lista
#Escribe un programa que permita al usuario ingresar una lista y la invierta.

num = int(input("Ingresa la cantidad de elementos que ingresaaras el la lista :"))
lista = []

for elemento in range(0,num):
    lista.append(int(input(f"Ingresa el número ")))
"""   
print(lista)
lista.reverse()
"""
lista_reversa = []
x = 0
y = num

for i in range(0,num):#con append
    x = lista[y-1]
    lista_reversa.append(x)
    y -=1
    
"""
y = num
for i in range(0,num):# sin append 
    x = lista[y-1]
    lista_reversa += [x]
    y -= 1
    """
    
print(f"La lista a la reversa es : {lista_reversa}")
    