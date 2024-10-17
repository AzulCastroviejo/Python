
#EJ3

def sumatotal(matriz):
    sumatotal = []
    for fila in matriz:
        suma_fila = sum(fila)
        sumatotal.append([suma_fila])
    return sumatotal

#EJ 1

import random

def cargar_matriz(filas, columnas, tipo_carga):
    matriz = []
    if tipo_carga == 'manual':
        for i in range(filas):
            fila = []
            for j in range(columnas):
                valor = float(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
                fila.append(valor)
            matriz.append(fila)
    elif tipo_carga == 'aleatoria':
        for i in range(filas):
            fila = [random.uniform(1, 999) for _ in range(columnas)]
            matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join(f"{valor:.2f}" for valor in fila))

def main():
    # Solicitar el tamaño de la matriz
    filas = int(input("Ingrese el número de filas (mínimo 3): "))
    columnas = int(input("Ingrese el número de columnas (mínimo 2): "))

    # Validar el tamaño de la matriz
    if filas < 3 or columnas < 2:
        print("El tamaño de la matriz debe ser al menos 3x2.")
        return

    # Solicitar el tipo de carga
    tipo_carga = input("¿Desea cargar los valores de manera manual o aleatoria? (manual/aleatoria): ").lower()

    # Cargar la matriz
    matriz = cargar_matriz(filas, columnas, tipo_carga)


# Mostrar la matriz cargada
    print("\nMatriz cargada:")
    mostrar_matriz(matriz)

    sumatoria = sumatotal(matriz)

    print("\nLa sumatoria de las filas es:")
    for fila in sumatoria:
        print(fila)

main()


