
from clase_vivienda import Vivienda

class Barrio:
    def __init__(self , nombre , empresaConstructora) :
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.viviendas = []
        
    def agregar_vivienda(self , vivienda):
        self.viviendas.append(vivienda)
        
        
    def getSuperficieTotalTerreno(self):
        
        total = 0
        for vivienda in self.viviendas :
            superficie = vivienda.superficieTerreno
            total += superficie
            
        return total
    
    def getSuperficieTotalXManzana(self , manza):
        
        total_manzana = 0
        for vivienda in self.viviendas:
            numero_manzana =  vivienda.manzana 
            if numero_manzana == manza :
                superficie = vivienda.superficieTerreno
                total_manzana += superficie
                
        print(f"La suma de la superficie total de las viviendas en la manzana {manza} es de {total_manzana}")
        
    def getSuperficieTotalCubierta(self):
        
        metros_cubiertos_total = 0
        
        for vivienda in self.viviendas:
            metros_cubiertos  = vivienda.getMetrosCuadradosCubiertos()
            metros_cubiertos_total += metros_cubiertos
            
        return metros_cubiertos_total