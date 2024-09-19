#15) Dados los siguientes criterios de divisibilidad:
#Criterios de divisibilidad del 2
#Para saber si un número es divisible entre dos hay que comprobar que sea par
#Criterios de divisibilidad del 3
#Sumamos las cifras del número y si el resultado de la suma es un número 
#múltiplo de 3, entonces el número sí es divisible por 3.
#Ejemplo
#Como ya sabemos que 45 es divisible por 3 vamos a comprobar que la suma de 
#sus cifras es un múltiplo de 3.
#Sumamos sus cifras: 45 –> 4 + 5 = 9
#9 es divisible por 3 por lo tanto 45 también es divisible por 3.
#Criterio de divisibilidad del 5
#Para saber si un número es divisible entre 5, dicho número tiene que acabar en 
#0 o 5
#Criterios de divisibilidad del 6
#Si se cumplen los criterios del 2 y del 3, entonces también es divisible por 6
#Criterio de divisibilidad del 9
#Un número es divisible entre 9 cuando la suma de sus dígitos es 9 o múltiplo de 9.
#Por ejemplo, vamos a comprobar si 2610 es un múltiplo de 9.
#2 + 6 + 1 + 0 = 9, por lo tanto 2610 es divisible por 9.
#Criterio de divisibilidad del 10
#Para saber si un número es divisible entre 10, éste tiene que acabar en 0.
#Codifique un programa en Python que solicite el ingreso de un número entero y 
#determine cuáles son los criterios de divisibilidad que cumple
print("Podrás saber porque números es divisible el número que deseas")
num = input("Ingrese un número entero :")
num = int(num)
resultado = " Criterio de divisibilidad que cumple del : "
numCadena = str(num)
suma=0
div6= 0
#DIVISIBILIDAD POR 2
if num % 2 == 0 :
    resultado = resultado + " 2 "
    div6 +=1

# DIVISIBILIDAD POR 3
for digito in numCadena:
    suma += int(digito)
      
if suma % 3 == 0:
      resultado +=  " 3 " 
      div6 += 1
      
#DIVISIBILIDAD POR 5
x = len(numCadena)
#i=int(numCadena[x-1:x])-> otra forma con rango funciona igual 
i=int(numCadena[x-1])
if i== 5 or i  == 0:
      resultado +=  " 5 "       
      
#DIVISIBIILIDAD POR 6
if div6 == 2:
     resultado +=  " 6 "   
     
#DIVISIBILIDAD POR 9     
if suma % 9 == 0:
      resultado +=  " 9 " 
      
#DIVISIBILIDAD POR 10        
if  i  == 0:
      resultado +=  " 10 " 
    
    
print(resultado)          
      