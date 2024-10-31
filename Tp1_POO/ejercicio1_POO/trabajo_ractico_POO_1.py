"""
1. Codifique la clase celda con los atributos: 
fila; //entero 
columna; //entero 
valor; //cadena 
 Crea una clase Matriz que contenga una variable celdas 
celdasMatriz = []; 
 Codifique un programa que solicite al usuario un valor para la celda y que solicite la 
posición donde se desea almacenar el valor, cree una instancia de la clase Celda, 
asigne los valores cargados por el usuario (fila, columna y valor) y agregue la 
instancia a la lista celdasMatriz; repita este proceso hasta que el usuario ingrese 
como valor la cadena “FIN”. Valide que la celda creada ya no exista anteriormente 
es decir si la fila y columna indicados ya fueron cargados en celdasMatriz. 
 Muestre por pantalla los valores cargados en la lista celdas.  
 Codifique un método que reciba como parámetro los valores fila y columna y 
retorne el valor almacenado en la Celda correspondiente, en caso de que la fila y la 
columna no exista retorne el mensaje “La fila y columna indicada no ha sido 
asignada en ninguna celda” 
"""
from clase_celda import Celda
from clase_matriz import Matriz
            
matriz= Matriz()   
print("Ingresar los datos de las celdas que desees ingresar ")
print("Para terminar el ingreso de celdas ingresar FIN")
while True: 
     
    valor = str(input("Ingresa el valor que deseas : "))
    if valor.upper() == "FIN" :
        break  
    fila = int(input("Ingresa la fila en que deseas agregar el valor : "))           
    columna = int(input("Ingresa la columna en que deseas agregar el valor : "))           
    celda = Celda(fila , columna, valor)
    matriz.ingresar(celda)
    
matriz.mostrar()
   
        
