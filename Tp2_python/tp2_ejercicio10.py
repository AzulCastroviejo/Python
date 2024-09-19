#10- Convertir una cadena a mayúsculas o minúsculas, daremos opción a que el usuario 
#pida que se desea hacer (convertir a mayúsculas o convertir a minúsculas) y mostrar el 
#resultado por pantalla. 

frase= input("Ingresa una frase :")

while True:
    
    opc= int(input("Quieres cambiar a mayuscula ingresa 1 y si quieres cambiarla a minuscula ingresa 2 "))
    
    if opc == 1:
        frase = frase.upper()
        break
    
    elif opc == 2 :               
        frase = frase.lower()
        break
    
    else:
        print("La opcion es incorrecta ")

print(frase)