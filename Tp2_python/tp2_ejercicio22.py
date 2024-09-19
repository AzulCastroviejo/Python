#22- Suma los dígitos de un número ingresado por el usuario de forma recursiva. 
#Ejemplo: el usuario ingresa 1596 
#El programa debe sumar 1 + 5 + 9 + 6
num = int(input("Ingresa un número para sumar sus digitos :"))
suma = 0

def sumarDigitos(num , suma):
    suma=num % 10
   
    if num>0:
        suma=suma + sumarDigitos(num//10,sum)
        
    else:
        suma = 0

    return suma

print(f"La suma de los digitos de número {num} es { sumarDigitos(num,suma)}")