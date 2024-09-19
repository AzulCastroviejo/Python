#16- Codifique un método que reciba como parámetro una cadena y determine si la 
#misma contiene o no números.

def verificacion(cadena):
    count =0 
    for i in cadena:
        if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
            count +=1
         
    if count > 0:
        print(f"En la frase {cadena} hay números")
    else:
        print(f"No hay números en la cadena")
            
        
        
cadena =str(input("Ingresa una frase que desees: "))
verificacion(cadena)