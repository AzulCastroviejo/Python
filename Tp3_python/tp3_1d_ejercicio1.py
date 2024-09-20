#Ejercicio 1: Suma de Elementos
#Escribe un programa que permita al usuario ingresar una lista de números y calcule la 
#suma de todos los elementos en la lista.
suma =0
lista = []
num =1
print("Se van a sumar todos los números que ingreses a la lista hasta que ingrese el número 0 para mostrar la suma")

while num !=0 :
    num=int(input("Ingrese el número que deseas sumar :"))
    lista.append(num)
    #suma += num
    
for elemento in lista:
    suma+=elemento    
    print(elemento)
    
print(f"La suma de los elementos de la lista es = {suma}")