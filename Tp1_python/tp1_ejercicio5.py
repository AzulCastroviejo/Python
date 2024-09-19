#5) Lee un número por teclado e indica si es divisible entre 2 (resto = 0). Si no lo es, 
#también debemos indicarlo.
 

print("Ingresa el número deseado: ")
num1 = input()
num1 = int(num1)
if num1 % 2 == 0:
    print(f"El número {num1} es divisible por 2")
else:
 print(f"El número {num1} no es divisible por 2")

    
