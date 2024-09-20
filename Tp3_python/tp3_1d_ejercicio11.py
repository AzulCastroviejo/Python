#Ejercicio 11: Contar Ocurrencias de un Elemento
#Escribe un programa que permita al usuario ingresar una lista y un número, y cuente 
#cuántas veces aparece ese número en la lista.

lista = []
num = ""
cantidad =0
print("Ingresa los números que desees a la lista , cuando temines ingresa 0")

while num != 0:
    num = int(input("Ingresa el número a la lista : "))
    if num != 0:
        lista.append(num)  
        
x= int(input("Ingrese el número que desea saber cuantas veces se encuentra en la lista : "))

for i in lista:  
    
    if i == x :
        cantidad += 1
       
print(f"Hay {cantidad} de números {x} ")        
          
        
    
   
 
        
