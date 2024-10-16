"""
    1. Cargar una Lista de números decimales de tamaño MXN y mostrar los datos
cargados. El tamaño de la Lista debe ser solicitado e ingresado por el usuario,
indicando un valor entero para las filas y un valor entero para las columnas, el
valor mínimo valido debe ser de 3x2, crear la Lista y solicitar los valores
numéricos para cargar de datos en cada posición. La carga de los datos puede ser 
manual, donde los datos serán ingresados por el usuario o aleatoria, donde los 
números serán generados automáticamente, ambos casos en el rango de 1 a 999. 
El sistema preguntara al usuario como quiere hacer la carga de valores. (2.5 ptos)
3. Generar una nueva Lista de N filas por 1 columna que contenga en cada celda de
la columna la sumatoria de las celdas de cada una de las filas de la Lista cargada
en el punto 1. (2 ptos)

    """
import random
import math

filas = int(input("Ingresa las filas que desees tener : "))
columnas = int(input("Ingresa las columnas que desees tener : "))
opcion = int(input("Como deseas ingresar los datos -ingresa el número deseado- : \n 1.Ingresar manualmente \n 2.Ingresar aleatoriamente "))

def main(filas , columnas , opcion):  
    
    num = 0
    matriz = []
    if opcion == 1:
        for i in range(filas):
            filas_actuales= []
            for j in range(columnas):
                num = int(input("Ingresa el número : "))
                while num < 1 or num > 999:
                    print("Número fuera  de rango")
                    num = int(input("Ingresa otro número : "))
                    
                filas_actuales.append(num)
            
            matriz.append(filas_actuales)   

    elif opcion == 2:
        for i in range(filas):
            filas_actuales= []
            for j in range(columnas):
                num = random.randint(1 , 999)
                filas_actuales.append(num)
            
            matriz.append(filas_actuales)  
            
    else:
        print("Opcion incorrecta ")    
        
    return matriz       
   
def suma_lista(matriz) :
    
    matriz_suma = []
    for i in range(filas):
        suma =0
        for j in range(columnas):
            numer= matriz[i][j]  # a numer que va a ser sumado con los elementos d la fila hay que igualalo con la matriz [i][j] hay que dar bien la posicion si no nos tira error
            suma += numer
            
        matriz_suma.append(suma)    
     
    return matriz_suma    
   

def orden_suma(matriz_suma):
        
        matriz_ordenada = [] # Creamos una matriz nueva que tendra la matriz_suma y sus indices
        for i in range(len(matriz_suma)):#inicializamos el for de i hasta el rango de largo de la matriz_suma
            fila_actual =[]
            for j in range(0,1):
               num= matriz_suma[i]
               fila_actual.append([num , i])
             
            matriz_ordenada.append(fila_actual)
             
        suma_con_indices = sorted(matriz_ordenada, reverse=True)    
        
        return suma_con_indices

    
def sumatotal(matriz_suma):
    
    suma_fila=0
    for i in matriz_suma:
        suma_fila +=i
        
    return suma_fila         
     
      

def imprimir_matriz(matriz):
    
    for i in matriz:
        print(i)   


matriz=main(filas,columnas,opcion)        
print("-----Matriz-----")        
imprimir_matriz(matriz)
matriz_suma = suma_lista(matriz)   
print("Matriz con la suma de sus filas suma") 
imprimir_matriz(matriz_suma)      
matriz_ordenada = orden_suma(matriz_suma)  
print("Matriz ordenada de mayor a menor")
imprimir_matriz(matriz_ordenada)
suma= sumatotal(matriz_suma)
print(f"La suma de los elementos de la matriz es = {suma}")
