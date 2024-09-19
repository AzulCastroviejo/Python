#1- CASTEO: Codifique un programa que solicite el ingreso de un numero decimal y 
#asigne el mismo a una variable valorDecimal, aplique las operaciones de CASTING para 
#convertir la variable a los siguientes tipos de datos, short, int, long, float investigue las 
#diferentes formas de lograr la conversión. Muestre por pantalla el resultado de las 
#conversiones.

valorDecimal=input("Ingrese un número decimal :")
print(valorDecimal)
valorFloat=float(valorDecimal)
print(f"Número con float {valorFloat}")
#valorShort = short(valorDecimal)
valorInt = int(valorFloat)
print(f"El valor int {valorInt} , en python se utiliza int para todos los enteros hasta los de tamaño largo (long en java)")
valorBool = bool(valorFloat)
print(f"El valor como booleano es {valorBool}")