#9- Recorre la cadena del ejercicio 6 y transforma cada carácter a su código ASCII. 
#Muéstralos en línea recta, separados por un espacio entre cada carácter.

frase = "La lluvia en Mendoza es escasa"
print(frase)
caracteres = len(frase)
x = 0
codigo =""
for i in frase:
    
    if i != " ":
        codigo += str(ord(i)) + " "
   
        
print(f"La frase {frase} en código ASCII")
print(codigo)