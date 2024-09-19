#14) Codifique un programa de consola en Java que permita realizar las siguientes 
#acciones: 
#Generar un número aleatorio entre 0 y 100, para ello use la siguiente función:
#random.randint(0, 100)

import random

numAleatorio = random.randint(0,100)
intentos = 1
print(numAleatorio)
print("Descubre el número desconocido")
while True:
    
    num =input("Ingrese el número : ")
    num = int(num)
    if numAleatorio == num:
        print(f"Felicitaciones encontraste el número desconocido -> {numAleatorio}")
        print(f"Lo lograste en el intento {intentos}")
        break
    elif numAleatorio > num:
        print(f"El número desconocido es mayor a {num}")
        intentos += 1
    elif numAleatorio < num:
         print(f"El número desconocido es menor a {num}")
         intentos += 1
        