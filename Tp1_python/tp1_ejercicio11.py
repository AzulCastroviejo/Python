#11) Escribe una aplicación con una variable que contenga una contraseña cualquiera. 
#Después se te pedirá que introduzcas la contraseña, con 3 intentos. Cuando aciertes ya 
#no pedirá más la contraseña y mostrara un mensaje diciendo “Acceso Correcto”. 
#Piensa bien en la condición de salida (3 intentos y si acierta sale, aunque le queden 
#intentos). Si no acierta en ninguno de los 3 intentos, mostrar el mensaje “El acceso se 
#ha bloqueado después de los 3 intentos”. Fin programa

contrasenia = "flores"
longitudContrasenia= len(contrasenia)
resultado = False
intentos =1
opcion = input("Ingresa la contraseña : ")
i=0
while intentos != 3 and resultado == False:
     
   resultado= contrasenia == opcion
   if resultado == False:
     intentos +=  1
     opcion=input("Ingresa nuevamente la contraseña :")
     
   else:
      
       print("La contraseña es correcta")
       break
       
if intentos == 3 :
    print("LO SENTIMOS")
    print("No tienes más intentos")           
   
        
        
