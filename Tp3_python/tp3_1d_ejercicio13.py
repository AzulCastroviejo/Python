#Ejercicio 13: Explique y ejemplifique la librería NumPy para trabajar con matrices y 
#arrays

# Explique y ejemplifique la librería NumPy para trabajar con matrices y arrays

# NumPy, que significa “Numerical Python”, es una biblioteca de código abierto que proporciona soporte para arreglos 
# multidimensionales (arrays) y una amplia gama de funciones matemáticas de alto rendimiento
# 1_Manipulación de Arrays: Permite crear y manipular arrays de una manera eficiente. Los arrays de NumPy son más rápidos y ocupan 
# menos memoria que las listas de Python1.
# 2_Operaciones Matemáticas: Facilita la realización de operaciones matemáticas complejas, como álgebra lineal, transformaciones 
# de Fourier y generación de números aleatorios2.
# 3_Integración con Otras Bibliotecas: Es la base para muchas otras bibliotecas de Python, como pandas, que se utilizan para el
# análisis de datos2.
# 4_Cálculo Numérico: Ideal para realizar cálculos numéricos en grandes volúmenes de datos, lo que la hace muy útil en campos como 
# la ciencia de datos, la ingeniería y la investigación científica

# Para importar la librería NumPy en Python, primero necesitamos asegurar de que está instalada. Es tan sencillo que solo en el cmd
# debemos escribir el siguiente comando: pip install numpy
# ahora si podemos importar la libreria
import numpy as np

# Definir dos matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Multiplicar las matrices
C = np.dot(A, B)

print(C)

# Utilizamos la función np.dot para multiplicar las matrices A y B. La multiplicación de matrices no es lo mismo que la multiplicación
# elemento a elemento; en este caso, estamos realizando una operación de álgebra lineal.