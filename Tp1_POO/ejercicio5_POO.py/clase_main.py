
from clase_habitacion import Habitacion
from clase_barrio import Barrio
from clase_vivienda import Vivienda

def main ():
    
    barrio = Barrio("Boedo" , "KKK")
    habitacion1 = Habitacion("Cocina" , 30)
    habitacion2 = Habitacion("Cuarto" , 10)
    habitacion3 = Habitacion("Comedor" , 50)
    habitacion4 = Habitacion("Cuarto" , 25)
    vivienda1 = Vivienda("Jose miguel" , 1 , 3 , 1520 , 120.3 )
    vivienda1.agregar_habitacion(habitacion1)        
    vivienda1.agregar_habitacion(habitacion2)
    vivienda1.agregar_habitacion(habitacion3)
    vivienda1.agregar_habitacion(habitacion4)
    vivienda1.agregar_habitacion(habitacion2)
    vivienda2 = Vivienda("san martin" , 2 , 2 , 1200 , 160.5 )
    vivienda2.agregar_habitacion(habitacion1)
    vivienda2.agregar_habitacion(habitacion2)
    
    vivienda3 = Vivienda("Frida Calo" , 3 , 3 , 1528 , 123 )
    vivienda3.agregar_habitacion(habitacion4)
    vivienda3.agregar_habitacion(habitacion1)
    vivienda3.agregar_habitacion(habitacion2)
    
    vivienda4 = Vivienda("belgrano" , 4 , 2 , 1250 , 150 )
    vivienda4.agregar_habitacion(habitacion1)
    vivienda4.agregar_habitacion(habitacion2)
    vivienda4.agregar_habitacion(habitacion2)
    vivienda4.agregar_habitacion(habitacion3)
    vivienda4.agregar_habitacion(habitacion4)
    
    vivienda5 = Vivienda("Messi" , 5 , 3 , 1535 , 130.5 )
    vivienda5.agregar_habitacion(habitacion1)
    vivienda5.agregar_habitacion(habitacion4)
    vivienda5.agregar_habitacion(habitacion3)
    vivienda5.agregar_habitacion(habitacion3)

    barrio.agregar_vivienda(vivienda1)
    barrio.agregar_vivienda(vivienda2)
    barrio.agregar_vivienda(vivienda3)
    barrio.agregar_vivienda(vivienda4)
    barrio.agregar_vivienda(vivienda5)
    
    metros_totales = barrio.getSuperficieTotalTerreno()
    metros_totales_cubierto = barrio.getSuperficieTotalCubierta()
    barrio.getSuperficieTotalXManzana(3)
    print(f"Superficie total de terreno del barrio : " ,metros_totales)
    print(f"Superficie total cubierta del barrio:" , metros_totales_cubierto)
    
    
    
main()    