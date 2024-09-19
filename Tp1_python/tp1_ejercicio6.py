#6) Lee un número por teclado que pida el precio de un producto (puede tener 
# decimales) y calcule el precio final con IVA. El IVA sera una constante que sera del 21% 

producto = input("Ingrese el precio del producto sin IVA : ")
producto = float(producto) #float se usa para números decimales
productoFinal = producto + (producto*0.21)
print(f"El producto con IVA sale -> ${productoFinal}")