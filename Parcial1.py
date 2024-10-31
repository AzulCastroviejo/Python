
def main ():
    opcion = 1
    lista_golosinas = crear_lista()
    empleados = crear_diccionario()
    claveTecnico = ("admin", "CCCDDD", "2020")
    golosinasPedidos =crear_lista( )
    for i in range(0,12):
        for j in range(0,2):
            sum =0
            golosinasPedidos[i][2]= sum
              
                
    
    while  opcion != 0:
        print(" ----- MENU -----")
        print("1. Pedir golosinas ")
        print("2. Mostrar golosinas ")
        print("3. Rellenar golosinas ")
        print("4. Apagar maquina ")
        opcion = int(input("Ingresa el número de la opcion que deseas realizar  "))
        
        match(opcion):
            case 1:
                pedir_golosina(lista_golosinas , empleados, golosinasPedidos)
           
            case 2:
                mostrar_golosina(lista_golosinas)
                
            case 3:
                rellenar_golosina(lista_golosinas, claveTecnico)
               
            case 4:
                apagar_maquina(lista_golosinas , golosinasPedidos)
                break
            case _:
                print("Opción incorrecta")    

def crear_lista():
    lista = [
        [1,"KitKat", 20],
        [2,"Chicles" ,50],
        [3, "Caramelos de Menta", 50],
        [4,"Huevo Kindert", 10],
        [5,"Chetoos" ,10],
        [6, "Twix", 10],
        [7,"M&M'S", 10],
        [8,"Papas Lays" ,2],
        [9,"Milkybar " ,10],
        [10, "Alfajor Tofi", 15],
        [11,"Lata Coca", 20],
        [12,"Chitos" ,10]
    ]
    
    return lista

def crear_diccionario():
    empleados = {
        "1100":( "José Alonso"),
        "1200": ( "Federico Pacheco"),
        "1300": ( "Nelson Pereira"),
        "1400": ( "Osvaldo Tejada"),
        "1500": ( "Gastón Garcia")
    }
    
    return empleados

def pedir_golosina(invetario , empleados,pedidos):
    
    legajo = input("Ingresa el legajo del empleado que desea una golosina de forma gratuita ")
    
    if legajo in empleados:  # busca el codigo en el inventario no es necesario pasar con la i posicion por posicion 
            nombre = empleados[legajo] 
            print(f"El empleado del legajo {legajo} es {nombre} y puede consumir golosinas ")
            golosina= int(input("Ingresa el codigo de la golosina que deseas : "))
            inventario , pedidos = decrementar_stock(invetario,golosina ,pedidos, empleados)
            
    else:
            print("El legajo ingresado no pertenece a un empleado ")
            
            
    return pedidos        

def mostrar_golosina(inventario):
    
    for i in inventario:
            print(i)

def rellenar_golosina(inventario, claveTecnico):
    
    clave1= str(input("Ingresa la primera clave : "))    
    clave2= str(input("Ingresa la segunda clave : "))
    clave3= str(input("Ingresa la tercer  clave :  "))
    if clave1 in claveTecnico and clave2 in claveTecnico and clave3 in claveTecnico :
        print("Haz ingresado correctamente")
        golosina = int(input("Ingresa el codgigo de la golosina qu edeseas actualizar : "))
        inventario = incrementar(inventario , golosina)
        mostrar_golosina(inventario)
    else:
        print("Clave ingresada ERRONEA")    
    
    
def incrementar(inventario, codigo):
    x =0 
    for i in range(0, 12):
        
        for j in range(0,2):
            num = inventario[i][0]
            if codigo ==  num and x == 0: 
                sum = int(input("Ingresar la cantidad de stock a agregar : ")) 
                sum += inventario[i][2]
                inventario[i][2]= sum
                
                x +=1
    
    return inventario            
                
def decrementar_stock(inventario,golosina, pedidos, empleados): 
    x =0 
    sum = 0
    agregar = 0
    for i in range(0, 12):
        fila=[]
        for j in range(0,2):
            num = inventario[i][0]
            nombre = inventario[i][1]
            cantidad =inventario[i][2]
            if golosina ==  num and x == 0: 
                sum = (cantidad)-1
                inventario[i][2]= sum
                pedidos[i][2] += 1
                x +=1
                if cantidad == 0 :
                    inventario[i][2]= sum+1
                    print("La golosina elegida no esta disponible ")
                    print("1. Puedes volver a elegir otra golosina ")
                    print("2. Volver al menú")
                    opcion = int(input("Ingresa la opcion que deseeas : "))
                    if opcion == 1:
                        pedir_golosina(inventario ,empleados , pedidos)
                    elif opcion ==2:
                        break
                    else:
                        print("Opcion incorrecta")
                        break
                    
    if x == 0 :
            print("El código no es correcto")      
         
    return inventario , pedidos           
                
def apagar_maquina(inventario, pedidos):
    print("\n   ---Inventario--- \n ")
    mostrar_golosina(inventario)
    print("\n   ---Pedidos--- \n ")
    mostrar_golosina(pedidos)
    
    print("APAGAR MAQUINA")
    

main()