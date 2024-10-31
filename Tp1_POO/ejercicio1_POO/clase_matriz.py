

class Matriz():
    
    def __init__ (self):
        self.matrizcelda =[]
        
    
    def ingresar(self ,celda ):
        for c in self.matrizcelda:
            if c.fila == celda.fila and c.columna == celda.columna:
                print("La celda ya existe ")
                return
        self.matrizcelda.append(celda)
        print("La celda a sido ingresada correctamente ")
            
    def mostrar(self):
        print("LA MATRIZ")
        for celda in self.matrizcelda:
            print(f"Fila : {celda.fila} columna : {celda.columna}  valor : {celda.valor}")
            