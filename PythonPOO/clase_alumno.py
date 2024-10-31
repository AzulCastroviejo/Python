#Clase: Alumno 
#Atributos: nombreCompleto(cadena), 
#legajo (entero), lista de objetos notas[] 

class Alumno:
    
    def __init__(self , nombre_completo , legajo , notas) :
        self.nombre_completo = nombre_completo
        self.legajo = legajo
        self.notas = []