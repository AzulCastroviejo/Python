#2. Buscar un producto por su código.
#4. Eliminar un producto del inventario.

def productos_por_rango_de_precio(inventario):
    min = float(input("Ingresa el rango menor de precio que deseas :"))
    max = float(input("Ingresa el rango mayor de precio que deseas :"))
    
    for i in inventario:
        descripcion, precio = inventario[i]
        if precio >= min and precio <= max:
            print(f"El pruducto {descripcion} que sale ${precio} esta en el rango deseado")
    menu(inventario)
        
def eliminar_producto(inventario):
    codigo = input("Ingresa el código del producto que desea eliminar del inventario : ")
    if codigo in inventario: 
            descripcion,precio = inventario[codigo] #desempaquetar tuplas -> nos permite ponerle nombre y valor a los elementos de la tupla sirve -> _ nos permite agrgarle un nuevo element al espacio
            del inventario[codigo] #Elimina del inventario ese codigo
            print(f"El producto del codigo {codigo} descripcion {descripcion} con precio ${precio} a sido elimindao del inventario")
            menu(inventario)
    else:
            print("El código ingresado no se encuentra en el inventario")
            eliminar_producto(inventario)        
     
def modificar_precio(inventario):
    codigo = input("Ingresa el código del producto que desea modificar : ")
    
    if codigo in inventario:  # busca el codigo en el inventario no es necesario pasar con la i posicion por posicion 
            descripcion,_ = inventario[codigo] #desempaquetar tuplas -> nos permite ponerle nombre y valor a los elementos de la tupla sirve -> _ nos permite agrgarle un nuevo element al espacio
            nuevo_precio= float(input(f"Ingrese el nuevo precio a al producto {descripcion} $"))
            inventario[codigo] = (descripcion, nuevo_precio)# le agregamos el nuevo elemento al codigo "inventario"
            print(f"El producto del codigo {codigo} es {descripcion} y sale ${nuevo_precio}")
            menu(inventario)
    else:
            print("El código ingresado no se encuentra en el inventario")
            modificar_precio(inventario)
            
def buscar_producto(inventario):
    codigo = input("Ingresa el código del producto que desea encontrar : ")
    
    if codigo in inventario:  # busca el codigo en el inventario no es necesario pasar con la i posicion por posicion 
            descripcion, precio = inventario[codigo] #desempaquetar tuplas -> nos permite ponerle nombre y valor a los elementos de la tupla sirve , si ya sabemos el contenido de estas
            print(f"El producto del codigo {codigo} es {descripcion} y sale ${precio}")
            menu(inventario)
    else:
            print("El código ingresado no se encuentra en el inventario")
            buscar_producto(inventario)


def mostrar_inventario(inventario):
    print("El inventario es :  ")

    for i in inventario:
        descripcion, precio = inventario[i]
        print(f"El producto de código {i} descripción -> {descripcion} y precio -> ${precio}")
    
    menu(inventario)

def menu(inventario):
    print("---Menú de acciones de tu inventario---")
    print("-Ingresa el número de la acción que desea hacer-")
    print("1 - Mostrar el inventario")
    print("2 - Buscar un producto específico")
    print("3 - Moficar precio del producto deseado")
    print("4 - Eliminar producto del inventario")
    print("5 - Buscar productos por rango de precios")
    print("0 - Cerrar")
    accion = int(input("Accion deseada : "))
    match accion:
        case 1:
            mostrar_inventario(inventario)
        case 2:
            buscar_producto(inventario)
        case 3: 
            modificar_precio(inventario)    
        case 4:
            eliminar_producto(inventario)
        case 5:
            productos_por_rango_de_precio(inventario)
        case 0:
            print("Cerrar menú")
            
        case _ :
            print("Ingresaste mal la accion")
            menu(inventario)

    
    
    
    
inventario = {
    "AA001": ("Remera black", 18000),
    "AA002": ("Remera white", 20320),
    "AA003": ("Bermuda destiñe", 32000),
    "AA004": ("Jean ancho", 45200),
    "AA005": ("Buzo canguro rojo", 36800),
    "AA006": ("Campera pluma negra", 74020)
}

menu(inventario)
