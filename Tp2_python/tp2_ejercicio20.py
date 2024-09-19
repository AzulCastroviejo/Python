#20- Cree una clase Fracción con dos atributos, numerador y denominador.
#Agregue a la clase los siguientes 4 métodos e implemente los mismos: 
#sumarFracciones(Fraccion f1, Fraccion f2
#restarFracciones(Fraccion f1, Fraccion f2)
#multiplicarFracciones(Fraccion f1, Fraccion f2)
#dividirFracciones(Fraccion f1, Fraccion f2)
#Todos los métodos deben retornar la fracción resultante de la operación.
#Cree una clase OperacionesFraccion que contenga un método main donde se solicite 
#al usuario el ingreso de 4 valores numéricos enteros con los cuales se crearan 2 objetos 
#Fracción y finalizada la creación de los mismos se ejecutaran los 4 métodos 
#implementados anteriormente asignando el resultado a una nueva variable de tipo 
#Fracción y mostrando por pantalla el resultado de las operaciones realizadas. 
#Ejercicios con Recursión

class Fraccion():
    
    def __init__(self,numerador,denominador):
        
        self.numerador = numerador
        self.denominador = denominador
        #print(f"Haz creado la fraccion {self} -> {self.numerador} / {self.denominador}")
        
    def __str__(self):
        return f"{self.numerador} / {self.denominador}"# muestra el objeto correctamente 
    
    def sumarFracciones(f1,f2):
        numerador = f1.numerador * f2.denominador + f2.numerador * f1.denominador
        denominador = f1.denominador * f2.denominador
        return Fraccion(numerador , denominador)
        
    def restarFracciones( f1,f2):
        numerador = f1.numerador * f2.denominador - f2.numerador * f1.denominador
        denominador = f1.denominador * f2.denominador
        return Fraccion(numerador , denominador)
    
    def multiplicarFracciones( f1,f2):
        numerador = f1.numerador * f2.numerador 
        denominador = f1.denominador * f2.denominador
        return Fraccion(numerador , denominador)
        
    def dividirFracciones( f1,f2):
        numerador = f1.numerador * f2.denominador
        denominador = f1.denominador * f2.numerador
        return Fraccion(numerador , denominador)  
    
class OperacionFraccion():
    
    def main():
        f1 = Fraccion(0,0)
        f2 = Fraccion(0,0)
        f1.numerador = int(input("Ingreasa el numerador de la primera fraccion:"))
        f1.denominador = int(input("Ingreasa el denominador de la primera fraccion:"))
        f2.numerador = int(input("Ingreasa el numerador de la segunda fraccion:"))
        f2.denominador = int(input("Ingreasa el denominador de la segunda fraccion:"))
    
        sumar = Fraccion.sumarFracciones(f1, f2)
        print(f"La suma de las fracciones {f1} + {f2} = {sumar}")
        restar = Fraccion.restarFracciones(f1, f2)
        print(f"La resta de las fracciones {f1} - {f2} = {restar}")
        multiplicar = Fraccion.multiplicarFracciones(f1, f2)
        print(f"La multiplicacion de las fracciones {f1} * {f2} = {multiplicar}")
        dividir = Fraccion.dividirFracciones(f1, f2)
        print(f"La division de las fracciones {f1} / {f2} = {dividir}")

        
        
OperacionFraccion.main()