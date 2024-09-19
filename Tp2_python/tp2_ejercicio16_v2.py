#16- Codifique un método que reciba como parámetro una cadena y determine si la 
#misma contiene o no números.

def verificacion(cadena):
    n = 0
    
    for i in cadena:
        if i.isdigit():
            n += 1
            
    if n == 0 :
         print(f"La frase {cadena} no tiene números")
    else:
            print(f"La frase {cadena} tiene números")
            
    
frase = input("Ingresa una frase para verificar si en ella hay números: ")
verificacion(frase)