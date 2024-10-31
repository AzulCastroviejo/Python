

class Plato:
    
    def __init__(self , nombre_plato , precio , esBebida) :
        self.nombre_plato = nombre_plato
        self.precio  = precio
        self.esBebida = esBebida
        self.lista_ingredientes = []
        
    def agregar_ingrediente(self, ingrediente):
        self.lista_ingredientes.append(ingrediente)