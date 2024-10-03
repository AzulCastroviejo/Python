#1.Crear una Matriz de Números
#Crea una función que reciba dos parámetros: el número de filas y columnas. La función 
#debe generar una matriz de ese tamaño, donde los valores son números enteros 
#consecutivos empezando desde 1.

x = 1
#columnas = int(input("Ingrse el numero de columnas que desea en la matriz :"))
#filas = int(input("Ingrse el numero de filas que desea en la matriz :"))
#matriz=[[x for _ in range(columnas-1)]for _ in range(filas-1)][[
matriz = [[]]
#for i in range(0,filas-1):
 #   print("[",end=" ")
  #  for j in range(0,columnas-1):
   #     #matriz[i][j]= x
    #    matriz.append(x , end=" ")
     #   print(matriz)
      #  x += 1
   
   
#print(matriz)
#for i in range(filas-1):
 #   for j in range(columnas-1):
       
        #matriz[i][j]= x
        #matriz.append(x)
        #print(matriz)
      
    #matriz.append(filas)    
    
filas=int(input("Ingrese el numero de filas: "))
columnas=int(input("Ingrese el numero de columnas: "))
 
x=1
    
for i in  range (0,filas):
   
    for j in range(0,columnas):
        matriz[i].append(x)
        print(x,end=" ")
        x+=1

    
        

    
    
                



   
