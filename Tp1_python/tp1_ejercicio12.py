#12) Crea una aplicación que nos pida un día de la semana y que nos diga si es un dia 
#laboral o no (siendo sábado y domingo no laborales). Usa un switch para ello. Valida 
#que el número ingresado sea un valor entre 1 y 7, caso contrario solicite el valor 
#nuevamente. 
diaElegido= input("Ingresa un día de la semana para saber si es laboral o no (en números del 1 al 7):")
diaElegido = int(diaElegido)
x = False

while True:
    
    if diaElegido < 8 and diaElegido > 0 :
        match diaElegido:
         case 1:
            print("Es día Lunes")
            print("DIA LABORAL")
            break
         case 2:
            print("Es día martes")
            print("DIA LABORAL")
            break
         case 3:
            print("Es día Miércoles")
            print("DIA LABORAL")
            break
         case 4:
            print("Es día Juves")
            print("DIA LABORAL")
            break
         case 5:
            print("Es día Viernes")
            print("DIA LABORAL")
            break
         case 6:
            print("Es día Sábado")
            print("   NO ES DIA LABORAL ")
            break
         case 7:
            print("Es día Domingo")
            print("   NO ES DIA LABORAL ")    
            break
        
    else: 
        diaElegido= input("Ingresa un día de la semana para saber si es laboral o no (en números del 1 al 7):")
        diaElegido= int(diaElegido)
        

    
    