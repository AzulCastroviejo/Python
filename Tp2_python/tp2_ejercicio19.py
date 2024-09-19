#19- Cree una clase OperacionMatematica con dos atributos valor1 y valor2 y un 
#atributo de nombre operación.
#Agregue a la clase los siguientes 5 métodos e implemente la lógica correspondiente: 
#sumarNumeros()
#restarNumeros()
#multiplicarNumeros()
#dividirNumeros()
#El quinto método será el siguiente: 
#aplicarOperacion(operacion){ 
#………………….. 
#} 
##Cree una clase Calculo que contenga un método main, donde cree una instancia de la 
#clase OperacionMatematica, asigne 2 valores para las variables de la instancia y 
#ejecute la función aplicarOperacion, pasando como parámetro primero “+”, después “-
#”, a continuación “*” y finalmente “/”. Muestre por pantalla el resultado de las 
#operaciones. 


class OperacionMatematica():
    
    def sumarNumeros(valorA ,valorB):
        suma = valorA + valorB 
        print(f"La suma de los números {valorA} + {valorB} = {suma}")
    
    def restaNumeros(valorA ,valorB):
        resta = valorA - valorB
        print(f"La resta de los números {valorA} - {valorB} = {resta}")
    
 
    def multiplicarNumeros(valorA ,valorB):
        multiplicar = valorA * valorB
        print(f"La multiplicacion de los números {valorA} x {valorB} = {multiplicar}")
    
      
    def dividirNumeros(valorA ,valorB):
        dividir = valorA / valorB 
        print(f"La división de los números {valorA} / {valorB} = {dividir}")
    
        
    def aplicarOperacion(valor1 , valor2 ,operacion):
        match(operacion): 
            case "+":
                sumar = OperacionMatematica.sumarNumeros(valor1,valor2) # type: ignore
            case "-":
                resta = OperacionMatematica.restaNumeros(valor1 , valor2)
            case "*":
                OperacionMatematica.multiplicarNumeros(valor1 , valor2)
            case "/":
                OperacionMatematica.dividirNumeros(valor1 , valor2)
      
class Calculo:
    
    def main():
         valor1= int(input("Ingresa el primer valor de la operación : "))
         valor2= int(input("Ingresa el segundo número de la operación : "))
         operacion= ["+","-","*","/"]
         
         for i in operacion:
            instancia = OperacionMatematica.aplicarOperacion(valor1 , valor2, i)
            
            
Calculo.main()