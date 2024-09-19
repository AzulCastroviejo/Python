#4- Desarrolle un programa que ayude a una cajera a determinar el número de billetes y 
#monedas que se necesitan de cada una de las siguientes denominaciones 200, 100, 50, 
#20, 10, 5, 2 y 1, y monedas de 0.50, 0.25, 0.10 y 0.05 centavos para una cantidad de 
#dinero dada. Ejemplo si la cantidad es 1390,55 se necesitan 6 billetes de 200, 1 billete 
#de 100, 1 billete de 50, 2 billetes de 20, 1 moneda de 0.50 y una moneda de 0.05 
#centavos. Plantee el algoritmo planteando métodos para su resolución.
resto =0
cantidad = float(input("Ingrese el precio $"))
falta = cantidad
x = 0
numeros = 200,100,50,20,10,5,2,1,0.50,0.20,0.10,0.05,0
lista = list(numeros)
    
while lista[x]!=0:
    
     num = lista[x]
    
     if lista[x]<=1 :
               billet =int(falta /num)
               falta =falta-(billet * num)+0.01
               x += 1
               print(f"Se usa {billet} monedas de {num}")
             
     else:
               billet =int(falta /num)
               falta =falta-(billet * num)
               x += 1
               print(f"Se usa {billet} billetes de {num}")
          
              
  
        
#print(f"Necesitan {billt } billetes de dosciento y {cien} billetes de cien y {cincuenta} 50 y {veinte} veinte y 10 {diez} y 5 {cinco} 2 {dos} 1 {uno} ")
#print(f"Centavos 0.50 -> {cincuenta_cent}  0.20 -> {veintic_cent}  0.10 -> {diez_cent}  0.1 ->  {un_cent}")

#cantidad = float(input("Ingrese el precio $"))
#doscientos =int( cantidad /200)
#resto =cantidad-(doscientos * 200)
#cien=int(resto / 100)
#resto = resto -(cien *100)
#cincuenta = int(resto/50)
#resto = resto - (cincuenta*50)
#veinte = int(resto / 20)
#resto = resto - (veinte*20)
#diez = int(resto /10)
#resto = resto -(diez * 10)
#cinco = int(resto /5)
#resto= resto - (cinco *5)
#dos = int(resto/2)
#resto= resto -(dos *2)
#uno= int(resto/1)
#resto = resto - (uno *1)
#cincuenta_cent= int(resto/0.5)
#resto = resto - (cincuenta_cent*0.5)
#veintic_cent= int(resto/0.20)
#resto = resto - (veintic_cent*0.20)
#diez_cent= int(resto/0.10)
#resto = resto - (diez_cent *0.10)
#un_cent= int(resto/0.01)
#resto = resto - (un_cent *0.01)
#print(f"Necesitan {doscientos} billetes de dosciento y {cien} billetes de cien y {cincuenta} 50 y {veinte} veinte y 10 {diez} y 5 {cinco} 2 {dos} 1 {uno} ")
#print(f"Centavos 0.50 -> {cincuenta_cent}  0.20 -> {veintic_cent}  0.10 -> {diez_cent}  0.1 ->  {un_cent}")