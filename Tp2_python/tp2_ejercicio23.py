#23- Crea un programa donde se pida el ingreso de una cadena y por medio de 
#recursión mostrar la cadena de forma inversa. 
#Ejemplo: Ingreso “computadora de escritorio” 
#Invertir cadena “oirotircse ed arodatupm oc”



frase=str(input("Ingrese una frase: "))
cont=0
fraseInv=""

def inversa(frase,cont,fraseInv):

    if cont==len(frase):
         fraseInv= fraseInv + ""
    else:
        fraseInv= inversa(frase,cont+1,fraseInv) + frase[cont] 
    return fraseInv

print(inversa(frase,cont,fraseInv))

