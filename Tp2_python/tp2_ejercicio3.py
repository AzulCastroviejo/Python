#- Codifique un algoritmo que solicite el ingreso de un numero de 3 dígitos (100 - 999) 
#y por medio del uso de las operaciones matemáticas módulo 10 y división por 10 
#efectué la suma de los 3 dígitos del número. Ejemplo ingreso 563, salida del algoritmo 
#14. Plantee el algoritmo planteando métodos para su resolución

num = input("Ingresa un número de 3 dígitos para sumar cada uno de ellos : ")
suma = 0

while True:
    
    if num.isdigit() and len(num)==3:
        num = int(num)
        break
    else:
        num=input(f"Ingrese otro número ya que {num} no es correcto: ")

aux = num
while num > 0:
    
    suma += num % 10
    num //=  10 # Elimina el ultimo digito
    
print(f"La suma de los dígitos del número {aux} es {suma}")