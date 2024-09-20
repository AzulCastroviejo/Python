#ejercicio 2: Encontrar el Mayor y el Menor
#Escribe un programa que pida al usuario una lista de números y encuentre el mayor y 
#el menor de ello



num = int(input("Ingresa la cantidad de números quiere ingresar a la lista :"))
lista = []
    
for elemento in range(0,num):
    num=int(input("Ingrese el número en la lista :"))
    lista.append(num)
    print(elemento)
    
print(f"El npumero mas grande de la lista ingresada es = {max(lista)}")#con solo max(lista) podemos saber el mayor sin tener que comparar cada uno de los números
print(f"El npumero mas grande de la lista ingresada es = {min(lista)}")