
#2.

fechaFactura = str
numeroFactura = int
letraFactura = str
totalFactura = float
clienteFactura = str
detallesFactura = [5]

lista_articulos =[
    [101, "Leche" ,250],
    [102, "Gaseosa" ,300],
    [103, "Fideos" ,150],
    [104, "Arroz" ,280],
    [105, "Vino" ,1200],
    [106, "Manteca" ,200],
    [107, "Lavandina" ,180],
    [108, "Detergente" ,460],
    [109, "Jabón en polvo" ,960],
    [110, "Galletas" ,600]
]

clientes = {
    "20110425417": "Rodolfo Fernandez",
    "30527419655": "Los Pollos HnoS",
    "27289425478": "Andrea Pereira",
    "33536549878": "Multimarca Repuestos",
    "20291122568": "Luis Peric"
}

def verificar_cuil(cuil, clientes):
    if cuil in clientes:
        if cuil.startswith(("20", "27", "30", "33")):
            print("Cuil validado")
            
        print("El cuil a sido encontrado en la lista de clientes ")
        nombre = clientes[cuil]
        print(nombre)
            
        return nombre
    else: 
        print("El cuil ingresado no se encuentra en la lista de clientes , por lo tanto se realizara la factura como consumidor final")
        return "Consumidor Final"
    
    
def articulos(lista_articulos, detalleFactura):
    
    articulo = int
    n = 0
    while (articulo != 0000):
        articulo = int(input("Ingresa el código del artículo : "))
        for i in range(0,1):
            for j in range(0, lista_articulos())  :
                print(lista_articulos[0][j])
                
                if (articulo == n):
                    print("esta el articulo")
    
    
print(lista_articulos)
fechaFactura = input("Ingresa la fecha de factura : ")
numeroFactura = input("Ingrese el número de factura : ")
cuil = str(input("Ingresa el cuil deseado : ") )
clienteFactura= verificar_cuil(cuil, clientes)
detallesFactura = articulos(lista_articulos, detallesFactura)