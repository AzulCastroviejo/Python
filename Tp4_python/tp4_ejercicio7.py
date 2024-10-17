#persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
#a) Cambia el valor de la clave edad a 31.
#b) Agrega una nueva clave profesión con el valor "Ingeniero".
#c) Imprime el diccionario modificado.
persona={"nombre":"Juan", "edad":30 , "ciudad":"Madrid"}
persona["edad"]=31 # modificamos el diccionario tomando la key de referencia
persona["profesion"]= "Ingeniero"

print(persona) # imprimimos todos los datos del diccionario con key y dato incluido