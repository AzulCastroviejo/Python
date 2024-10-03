#texto = "manzana naranja manzana pera pera pera naranja manzana"
#a) Escribe un programa que cuente cuántas veces aparece cada palabra en el 
#texto utilizando un diccionario.
#b) Imprime el diccionario resultante.
texto = "manzana naranja manzana pera pera pera naranja manzana"
dic={"m": "manzana" , "n": "naranja", "p": "pera"}
manzana = texto.count("m")
naranja = texto.count("n")
pera = texto.count("p")
print(f"Hay {manzana} {dic['m']} , {naranja} naranjas y {pera} peras")
n=0
for i in texto:
    if  == "naranja":
        n+=1
        print(i)
        
print(n)