#10) Lee un número por teclado y comprueba que este número es mayor o igual que 
#cero, si no lo es lo volverá a pedir (do while), después muestra ese número por 
#consola. 
num1 = input("Escribe un número: ")
num1 = int(num1)
while True:
    if num1 == 0 or num1 > 0:
         break
    else:
      num1 =input("Escribe otro número :")
      num1= int(num1)
        
       
        
        
    
    
    
    
