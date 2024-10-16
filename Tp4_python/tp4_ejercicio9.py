#texto = "manzana naranja manzana pera pera pera naranja manzana"
#a) Escribe un programa que cuente cuántas veces aparece cada palabra en el 
#texto utilizando un diccionario.
#b) Imprime el diccionario resultante.

texto = "manzana naranja manzana pera pera pera naranja manzana"
texto = texto.split(" ")
cont = {}

for i in texto:
    if i in cont:
       cont[i] += 1
       
    else:
        cont[i] = 1
        
print(cont)