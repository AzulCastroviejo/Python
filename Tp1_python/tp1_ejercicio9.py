#9) Muestra los números del 1 al 100 (ambos incluidos) divisibles entre 2 y 3. Utiliza el 
#bucle que desees. 

num1 = 1

for num1 in range(1,101):
    if num1 % 2 == 0:
        if num1 % 3 == 0:
            print(num1)
            num1 = num1 + 1
    else: num1 = num1 + 1
