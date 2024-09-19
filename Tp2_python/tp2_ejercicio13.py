#13- Pedir el ingreso de dos cadenas por por teclado, indicar si la segunda cadena se 
#encuentra dentro de la primera.

cadena_uno=input("Ingresa la primera cadena :")
cadena_dos=input("Ingresa la segunda cadena :")
longitud_dos = len(cadena_dos)
n =list(cadena_uno)
x=list(cadena_dos)
s = 0
m = 0

for i in n:
    if n[s] == x[m]:
        m +=1   
        s += 1
        
        if longitud_dos == m:
           break
    else:
        s += 1
       
if longitud_dos == m:
    print(f"La frase {cadena_dos} esta dentro de la frase {cadena_uno}")
else:
    print(f"la frasse {cadena_dos} no se encuentra dentro de la primera frase -> {cadena_uno}")