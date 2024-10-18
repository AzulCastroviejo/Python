#Ejercicio 8: Encontrar Elementos Repetidos
#Escribe un programa que identifique y muestre los elementos que se repiten en una 
#lista.
#Pista:
# Utiliza un diccionario o un conjunto (set) para hacer el seguimiento de los 
#elementos.

lista = []
num =1
listaRep =[]
print("Ingresa los números que desees a la lista , cuando temines ingresa 0")

while num != 0:
    num = int(input("Ingresa el número a la lista : "))
    if num != 0:
      lista.append(num)   

listaRep = set(lista) 
duplicado = set()
for elemento in lista:
     if elemento in listaRep:
          listaRep.remove(elemento)
          
     else:
            duplicado.add(elemento)
    
print(f"En la lista {lista} - duplicados {duplicado}")