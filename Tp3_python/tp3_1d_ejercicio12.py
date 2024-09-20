#Ejercicio 12: Sumar Listas Elemento por Elemento
#Escribe un programa que sume dos listas de números elemento por elemento. Las 
#listas deben tener la misma longitud.

lista1 = [2,5,8,96,78]
lista2= [3,8,47,96,125]

def sumarLista(lista):
    sumar = 0
    for elemeto in lista:
        sumar += elemeto
        
    return sumar

def sumarDigito(lista1, lista2):
    lista3= []
    x= 0
    while x != 5:
        suma = lista1[x] + lista2[x]
        lista3.append(suma)
        x+=1
        
    return lista3
    
print(f"La suma de la primera lista es {sumarLista(lista1)}")
print(f"La suma de la primera lista es {sumarLista(lista2)}")
print(f"La suma de los digitos de las listas es {sumarDigito(lista1,lista2)}")