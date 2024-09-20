#Ejercicio 5: Multiplicar Elementos por un Valor
#Escribe un programa que multiplique cada elemento de una lista de números por un 
#valor ingresado por el usuario

lista = [1,2,3,4,5,6,7]
listamul= []
num = int(input("Ingresa el número que quiere usar par a multiplicar la lista :"))

for elemento in lista:
    listamul.append(elemento * num)
    
print(f"La lista de números sin multiplicar es : {lista}")
print(f"La lista multiplicada es : {listamul}")

for elemento in lista :
    print(f"El número {elemento} * {num} = {listamul[elemento-1]}")