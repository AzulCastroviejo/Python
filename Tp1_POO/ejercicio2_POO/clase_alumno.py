#Clase: Alumno 
#Atributos: nombreCompleto(cadena), 
#legajo (entero), lista de objetos notas[] 

class Alumno:
    
    def __init__(self , nombre_completo , legajo ) :
        self.nombre_completo = nombre_completo
        self.legajo = legajo
        self.notas = []
        
    def sumar_notas(self, nota_completo):
        self.notas.append(nota_completo)