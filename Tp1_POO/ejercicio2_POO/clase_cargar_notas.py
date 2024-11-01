
from clase_alumno import Alumno
from clase_nota import Nota

class CargarNotas:
    
    def __init__(self ) :
        self.alumnos = []
    
    def cargarNotas(self  , alumno):
        self.alumnos.append(alumno)
        
    def imprimirAlumnos(self):
        
        for alumno in self.alumnos:
            
            x = 0
            prom = 0
            print(f"El alumno {alumno.nombre_completo} de legajo {alumno.legajo} ")

            for nota in alumno.notas:
                x += 1
                prom += nota.nota_examen
                print(f"En la catedra {nota.catedra} tiene la nota {nota.nota_examen}")

            prom = prom / x
            print(f"El promedio de las notas de {alumno.nombre_completo} es {prom}")
        
        
def main():
    
    alumnos = CargarNotas()
    
    while True:
        
        print(  "INGRESE LOS DATOS DEL ALUMNO" ) 
        nombre_completo= input("Ingresa el nombre completo : ")
        legajo = input("Ingrese el número de legajo : ")
        print("Ingrese las notas que desee (cuando quiera finalizar escriba 0)")
        
        alumno = Alumno(nombre_completo , legajo )
        
        while True:
            
            nota_examen  = float(input("Ingrese la nota : "))

            if nota_examen == 0 :
                break
            
            catedra = str(input("Ingresar la catedra : "))
            nota_completo = Nota(catedra , nota_examen)
            alumno.sumar_notas(nota_completo)
        
        
        CargarNotas.cargarNotas(alumnos ,alumno)
        opc = str(input("Desea agregar un nuevo alumno SI/NO "))  
        if opc.upper() == "NO":
            break 
       
        
        
        
    CargarNotas.imprimirAlumnos(alumnos)    
        

        
main()