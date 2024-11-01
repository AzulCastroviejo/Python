
from clase_habitacion import Habitacion

class Vivienda:
    def __init__(self , calle , numero , manzana , nroCasa , superficieTerreno ):
        self.calle = calle
        self.numero = numero 
        self.manzana = manzana 
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitaciones = []
        
    def agregar_habitacion(self , habitacion):
        self.habitaciones.append(habitacion)
        
    def getMetrosCuadradosCubiertos(self):
        
        metros_cubiertos = 0
        for habitacion in self.habitaciones:
            metros_habitacion = habitacion.metros_cuadrados
            metros_cubiertos += metros_habitacion
            
        if metros_cubiertos > self.superficieTerreno:
            print("La superficie cubierta no puede ser mayor al terreno , se le sumara el terreno total")
            return self.superficieTerreno 
        else:
            return metros_cubiertos