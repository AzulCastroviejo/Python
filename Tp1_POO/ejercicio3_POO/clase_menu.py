from clase_plato import Plato
from clase_ingrediente import Ingrediente

class MenuRestaurant :
    
    def __init__(self) :
        self.platosMenu = []
        
    def agregar_plato(self, plato):
        self.platosMenu.append(plato)
        
    def mostrar(self):
        print("-------MENÚ-------")
        for plato in self.platosMenu:
            print("")
            print(f"Plato {plato.nombre_plato}")
            print(f"Precio ${plato.precio}")
            if plato.esBebida:
                print("--Bebida--")
            else:
                print("--INGREDIENTES--")
                for ingrediente in plato.lista_ingredientes :
                    print(f"Lleva {ingrediente.ingrediente} una cantidad de {ingrediente.cantidad} {ingrediente.unidad_medida}")
        
def main():
    
    menu = MenuRestaurant()
    cantidad_platos = int(input("Ingresa la cantidad de platos que deseas en tú menú : "))             

    while cantidad_platos != 0 :
        print("")
        nombre_plato = str(input("Ingresa el nombre del plato : "))
        precio = float(input("Ingresa el precio de este plato : $"))
        opc =input("Ingrese SI si es una bebida o NO si no lo es : ")
        esBebida = False
        ingrediente  = ""
       
        if opc.lower() == "si":
           esBebida =   True
           print(f"{nombre_plato} es una bebida ")
        
        plato = Plato(nombre_plato , precio , esBebida)

        if esBebida == False:
            print("")
            print("Ingresa los ingredientes necesarios para el plato , cuando termine escribe listo. ")
            
            while True :
                
                print("")
                ingrediente = str(input("Ingrese el ingrediente que lleva : "))
                
                if ingrediente.lower() == "listo":
                    break
                
                cantidad = float(input(f"Ingrese la cantidad de {ingrediente} que lleva el plato : "))
                unidad_medida = str(input("Ingrese la unidad de medida de la cantidad previamente ingresada : "))
                ingrediente_final = Ingrediente(ingrediente , cantidad , unidad_medida)
                plato.agregar_ingrediente(ingrediente_final)
        
        
        menu.agregar_plato(plato)                
        cantidad_platos -= 1
        
    menu.mostrar()    

main()        