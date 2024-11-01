

class Computadora:
    
    def __init__(self , marca , modelo):
        self.marca = marca
        self.modelo = modelo
        self.componentes_CPU = []
        
    def agregar_componente(self , componente):
        self.componentes_CPU.append(componente)