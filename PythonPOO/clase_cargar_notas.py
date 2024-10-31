
from clase_alumno import Alumno
from clase_nota import Nota

class CargarNotas:
    
    def __init__(self ) :
        self.alumnos = []
    
    def cargarNotas(self  , alumno):
        self.alumnos.append(alumno)
        
    def imprimirAlumnos(self):
        for alumno in self.alumnos:
            print(f"El alumno {alumno.nombre_completo} ")
            for nota in alumno.notas:
                print(f"En la catedra {nota.catedra} tiene la nota {nota.nota_examen}")
    
def main():
    
    cantidad = int(input("Ingresa la cantidad de alumnos para ingresar sus notas : "))
    alumnos = CargarNotas()
    
    while cantidad != 0:
        
        print(  "INGRESE LOS DATOS DEL ALUMNO" ) 
        nombre_completo= input("Ingresa el nombre completo : ")
        legajo = input("Ingrese el número de legajo : ")
        print("Ingrese las notas que desee (cuando quiera finalizar escriba 0)")
        notas = []
        
        
        while True:
            
            nota_examen  = float(input("Ingrese la nota : "))

            if nota_examen == 0 :
                break
            
            catedra = str(input("Ingresar la catedra : "))
            nota_completo = Nota(catedra , nota_examen)
            notas.append(nota_completo)
        
        alumno = Alumno(nombre_completo , legajo , notas)
        CargarNotas.cargarNotas(alumnos ,alumno)
        cantidad -=1
        
    CargarNotas.imprimirAlumnos(alumnos)    
        

        
main()