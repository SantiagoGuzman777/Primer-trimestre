productos = []

nom1= input("Ingrese el nombre del primer producto: ")
cant1= int(input("Ingrese la cantidad que desea del producto: "))
preu1=  float(input("Ingrese el precio por unidad del produccto: "))
subto1 = cant1 * preu1

if cant1 < 5:
    descuento1 = 0
elif cant1 >=5 and cant1 <=10:
    descuento1= subto1 * 0.05
elif cant1 > 10:
    descuento1 = subto1 * 0.10

total1 = subto1 - descuento1 

productos1 = {
    "Nombre": nom1,
    "Cantidad" : cant1,
    "Precio_unitario" : preu1,
    "Subtotal" : subto1,
    "Descuento" : descuento1,
    "Total" : total1
}

productos.append(productos1)

nom2= input("Ingrese el nombre del segundo producto: ")
cant2= int(input("Ingrese la cantidad que desea del producto: "))
preu2=  float(input("Ingrese el precio por unidad del produccto: "))
subto2 = cant2 * preu2

if cant2 < 5:
    descuento1 = 0
elif cant2 >=5 and cant2 <=10:
    descuento1= subto2 * 0.05
elif cant2 > 10:
    descuento1 = subto2 * 0.10

total2 = subto2 - descuento1 

productos2 = {
    "Nombre": nom2,
    "Cantidad" : cant2,
    "Precio_unitario" : preu2,
    "Subtotal" : subto2,
    "Descuento" : descuento1,
    "Total" : total2
}

productos.append(productos2)


nom3= input("Ingrese el nombre del tercer producto: ")
cant3= int(input("Ingrese la cantidad que desea del producto: "))
preu3=  float(input("Ingrese el precio por unidad del produccto: "))
subto3 = cant3 * preu3

if cant3 < 5:
    descuento1 = 0
elif cant3 >=5 and cant3 <=10:
    descuento1= subto3 * 0.05
elif cant2 > 10:
    descuento1 = subto3 * 0.10

total3 = subto3 - descuento1 

productos3 = {
    "Nombre": nom3,
    "Cantidad" : cant3,
    "Precio_unitario" : preu3,
    "Subtotal" : subto3,
    "Descuento" : descuento1,
    "Total" : total3
}

productos.append(productos3)

print (productos)



    


