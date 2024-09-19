#11- Pedir dos palabras por teclado, indicar si son iguales.
print("Podras comparar dos palabras")
palabra_uno= input("Ingresa la primera palabra: ").lower()
palabra_dos= input("Ingresa la segunda palabra: ").lower()

if palabra_dos == palabra_uno:
    print("Las palabras " + palabra_uno + " son iguales")
    
else:
    print("Las palabras no son iguales")