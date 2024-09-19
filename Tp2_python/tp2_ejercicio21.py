#21- Codifique un programa que solicite un número entero mayor a cero y que 
#mediante recursión sume todos los números números naturales desde el número 
#ingresado hasta 1. 
#Ejemplo: Ingreso 10 
#El programa debe sumar 10 + 9 + 8 +7 +6 + 5 + 4 + 3 + 2 +1 
num = 0
sumar =0

while num < 1:
    num = int(input("Ingrese un número mayor a 0 :"))
    
def suma(num , sumar):
    
    if num != 0:
        sumar += num 
        #print(sumar)
        return suma(num-1 , sumar)
    else:
        return sumar

print(f" La suma de todos los númerosnaturales de {num} es {suma(num, sumar)}")