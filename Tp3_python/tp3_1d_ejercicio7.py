#Ejercicio 7: Promedio de una Lista
#Escribe un programa que permita al usuario ingresar una lista de números y calcule el 
#promedio de los elementos.

lista = []
num =1
prom = 0
print("Ingresa los números que desees a la lista , cuando temines ingresa 0")

while num != 0:
    num = int(input("Ingresa el número a la lista : "))
    #prom += num
    lista.append(num)  
    
for i in lista :
    num = lista[i] # promedio desde la lista ya creada
    prom += num

prom = prom / (len(lista)-1)
print(f"El promedio de la lista es {prom}")