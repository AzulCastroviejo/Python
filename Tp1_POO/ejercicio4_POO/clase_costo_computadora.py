from clase_computadora import Computadora
from clase_componente_CPU import ComponenteCPU

class CostoComputadora:
    def __init__(self) :
        self.computadoras= []
        
    def agregar(self,computadora):
        self.computadoras.append(computadora)    
        
    def mostrar(self):
        
        print("--- COMPUTADORA ---")
        
        for computadora in self.computadoras:
            suma = 0
            print(f"La computadora marca {computadora.marca} \n Modelo: {computadora.modelo} \n ")
           
            for componente in computadora.componentes_CPU :
                print(f" -Componente- \n Nombre :{componente.componente} \n Marca : {componente.marca} \n Cantidad : {componente.cantidad} \n Precio unitario : {componente.precio} ")
                precio_componente = componente.precio * (float(componente.cantidad))
                suma += precio_componente
            
            if suma < 50000:
                prec = suma + (suma * 0.4)
                print(f"El precio de los componentes es ${suma} el precio propuesto con el 40% es ${prec}")
            else:
                prec = suma + (suma * 0.3)
                print(f"El precio de los componentes es ${suma} el precio propuesto con el 30% es ${prec}")

        
          
def main():
    
    while True:
        
        print(" ")
        marca = str(input("Ingresar la marca de la computadora : "))
        modelo = str(input("Ingresa el modelo de la computadora : "))
        computadora = Computadora(marca , modelo)      
        componente = ""
        print("Ingresalos componenetes que desees al finalizar el ingreso escribe FIN  ")
        
        while True:
            
            print("")
            componente = str(input("Ingresar el componente que desee : "))
            if componente.upper() == "FIN":
                break
            marca =str(input("Ingresa la marca del componente : "))
            cantidad = str(input(f"Ingresa la cantidad de  {componente}  que tiene la computadora : "))
            precio = float(input("Ingresa el precio del componente : "))
            comp = ComponenteCPU(componente , marca , cantidad , precio )
            computadora.agregar_componente(comp)
            
        costo  = CostoComputadora()
        costo.agregar(computadora)
        costo.mostrar()
        
        opc = str(input("Desea agregar una nueva computadora SI / NO : "))
        if opc.upper() == "NO":
            break
        elif opc.upper() == "SI":
            print("Se agregara una nueva computadora")
        else:
            print("Opcion incorrecta se tomara com un SI ")
            
            
main()