"""Generar una nueva Lista de N filas por 1 columna que contenga en cada celda de
la columna la sumatoria de las celdas de cada una de las filas de la Lista cargada
en el punto 1. """

def sumatotal(matriz):
    sumatotal = []
    for fila in matriz:
        suma_fila = sum(fila)
        sumatotal.append([suma_fila])
    return sumatotal

def main():
    filas = int(input("Ingrese el número de filas (mínimo 3): "))
    col = int(input("Ingrese el número de columnas (mínimo 2): "))

    if filas < 3 or col < 2:
        print("El tamaño de la matriz debe ser al menos 3x2.")
        return

    matriz = []

    for i in range(filas):
        entrada = input(f"Ingrese los valores de la fila {i + 1} separados por espacios: ")
        fila = list(map(int, entrada.split()))
        if len(fila) != col:
            print(f"Error: La fila {i + 1} debe tener {col} elementos.")
            return
        matriz.append(fila)

    print("\nLa matriz ingresada es:")
    for fila in matriz:
        print(fila)

    sumatoria = sumatotal(matriz)

    print("\nLa sumatoria de las filas es:")
    for fila in sumatoria:
        print(fila)


main()

