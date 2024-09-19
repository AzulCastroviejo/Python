#13) Pide un número por teclado e indica si es un número primo o no. Un número primo 
#es aquel solo puede dividirse entre 1 y sí mismo. Por ejemplo: 25 no es primo, ya que 
#25 es divisible entre 5, sin embargo, 17 si es primo. Un buen truco para calcular la raíz 
#cuadrada del numero e ir comprobando que si es divisible desde ese número hasta 1. 
#NOTA: Si se introduce un número menor o igual que 1, directamente es no primo.

num1 = input("Ingresa un número para verificar si es un número primo :")
num1 = int(num1)
divisor = num1
resultado = 0

while divisor != 0  :
 
    if num1 % divisor == 0:
        resultado +=1
        
    divisor -= 1    
        
if resultado == 2 :
    print(f"El número {num1} es primo")
   
else:
    print(f"El número {num1} no es un número primo")
       

