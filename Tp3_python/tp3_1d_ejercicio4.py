#Ejercicio 4: Contar Elementos Pares e Impares
#Escribe un programa que pida al usuario una lista de números y cuente cuántos de 
#ellos son pares y cuántos son impares.
num = int(input("Ingresa el largo de la lista que deseas :"))
lista =[]
par = 0
impar = 0

for elemento in range(0,num):
    lista.append(int(input(f"Ingresa el número ")))
    
for elemento in lista :
    
    if elemento % 2 == 0 :
        par += 1
    else:
        impar += 1
        
print(f"Hay {par} número pares")
print(f"Hay {impar} número impares")