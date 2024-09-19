#2.- Si se asigna un valor a una variable fuera de rango (mayor de lo establecido) ¿Qué 
#ocurre? ¿Existe alguna forma de resolverlo? Ejemplifique. 

#num = int(input("Ingresa tu edad :"))
#numMax = 18
#if num > numMax :
#    print("Eres muy grande para esta app ")
#else:
#    print("Bienvenido a la app")

#precio = int(input("Ingresa el precio del producto: $"))
#precioMax= 10000  
#while True:
#     if precio > precioMax:
#         precio = int(input("Ingresa otro precio ya que este exedio el máximo "))
#     else:
#         print(f"El precio ${precio} es correcto")
#         break

palabra = input("Ingresa una palabra con máximo 5 letras :")
while True:
     max = int(5)
     cantidad = len(palabra)
     if cantidad > max:
              palabra = input("Ingresa una nueva palabra con máximo 5 letras :")
     else:
         print(f"La palabra {palabra} esta dentro del rango")
         break

