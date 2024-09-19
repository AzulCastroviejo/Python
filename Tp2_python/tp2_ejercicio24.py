# Crea un programa que lea una cadena de texto carácter por carácter usando recursión. 

frase=str(input("Ingrese una frase: "))
cont=0

def unidad(frase,cont):

    if cont!=len(frase):
        print(frase[cont])
        unidad(frase, cont+1)
 
  

print(unidad(frase,cont))







