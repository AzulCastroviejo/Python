"""Generar una nueva Lista de tamaño N filas por 2 columnas donde la primer
columna contenga los valores calculados en el punto 3 pero ordenados de
Mayor a Menor, y en la segunda columna asignar el valor de la fila que poseía
originalmente en la Lista del punto 3."""

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



# Dentro del bucle, suma[0] accede al primer elemento de la lista suma.
# i es el índice original de la lista sumatoria.
# Por lo tanto, (suma[0], i) crea una tupla donde el primer elemento es la sumatoria y 
# el segundo elemento es el índice original.
    suma_con_indices = [(suma[0], i) for i, suma in enumerate(sumatoria)]

# Reverse=True indica que la lista debe ser ordenada en orden descendente (de mayor a menor).
    # Forma 1 de hacerlo: suma_con_indices.sort(reverse=True, key=lambda x: x[0])

    #Forma dos de hacerlo:
    suma_con_indices = sorted(suma_con_indices, reverse=True)

        # Crear la nueva lista de tamaño N filas por 2 columnas
    nueva_lista = [[suma, indice] for suma, indice in suma_con_indices]

    print("\nLa nueva lista ordenada es:")
    for fila in nueva_lista:
        print(fila)


main()