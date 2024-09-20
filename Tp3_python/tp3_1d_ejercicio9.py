#Ejercicio 9: Lista de Números Primos
#Escribe un programa que permita al usuario ingresar una lista de números y filtre los 
#números primos.
#Pista:
# Usa una función para verificar si un número es primo.

listaP = []
lista = []
num =1
divisor= 0

print("Ingresa los números que desees a la lista , cuando temines ingresa 0")

while num != 0:
    num = int(input("Ingresa el número a la lista : "))
    lista.append(num)
  
for elemento in lista:  
    divisor = elemento  
    x= 0
    while divisor != 0  :
 
         if elemento % divisor == 0:
            x += 1
            
         divisor -= 1    
    
    if x == 2:
        listaP.append(elemento)
        
        
print(f"La lista con los npumeros primos es : {listaP}")
    