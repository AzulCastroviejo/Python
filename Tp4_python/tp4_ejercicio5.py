#a) Cuenta cuántas veces aparece el número 4 en la tupla.
#b) Imprime el resultado.
tupla = (1,2,2,3,4,4,4,5)
num_cuatro= tupla.count(4)
x=0 

for i in tupla:
    if i == 4:
        x += 1
        
print(f"El número 4 se encuentra {num_cuatro} en la tupla por ciclo for")     
print(f"El número 4 se encuentra {num_cuatro} en la tupla por count()")