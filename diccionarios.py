#---------------------------DICCIONARIOS-----------------------------------------
# persona={

# "nombre":"Juan",
# "edad": 30,
# "lugarnacimiento":"Palmira"

# }


# auto={
#   "marca":"ford",
#   "modelo" : "mustang",
#   "año": 2022,
#   "color":"azul",
#   "placa":"PLQ-18D",
# }
# #--------------------------------------ACCEDER A VALORES------------------------------------
# print(auto["modelo"]) #resultado: mustang
# #--------------------------------------MODIFICAR VALORES-------------------------------------
# auto[año] = 2023
# #--------------------------------------AÑADIR NUEVOS ELEMENTOS-----------------------------
# auto["color"]="rojo"
# #------------------------------------ELIMINAR ELEMENTOS-------------------------
# del auto["modelo"]
 
# auto.pop("marca")
# 
#------------------------------TALLER-------------------------------------------
# nota1=float(input("ingrese la primera nota: "))
# nota2=float(input("ingrese la segunda nota: "))
# nota3=float(input("ingrese la tercera nota: "))
# lista=[]
# lista.append(nota1)
# lista.append(nota2)
# lista.append(nota3)
# print (lista)
# suma=nota1+nota2+nota3
# promedio=suma/3
# print(f"El promedio de sus calificaciones es {promedio}")
 
#------------------------------EJERCICIO2------------------------------------------------

# productos= {
# "leche":5000,
# "pan":5000,
# "huevos":700
# }
# aumento=float(input("Que porcentaje deseas aumentar: "))
# productos["leche"]+=productos["leche"] * (aumento/ 100)
# productos["pan"]+=productos["pan"] * (aumento/ 100)
# productos["huevos"]+=productos["huevos"] * (aumento/ 100)
# print(productos)

#-------------------------------EJERCICIO3-------------------------------------


# temperatura1=float(input("ingrese la temperatura del primer dia: "))
# temperatura2=float(input("ingrese la temperatura del segundo dia: "))
# temperatura3=float(input("ingrese la temperatura del tercer dia: "))
# temperatura4=float(input("ingrese la temperatura del cuarto dia: "))
# temperatura5=float(input("ingrese la temperatura del quinto dia: "))

# celcius=(temperatura1),(temperatura2),(temperatura3),(temperatura4),(temperatura5)

# operacion1= temperatura1* 9/5+32
# operacion2= temperatura2* 9/5+32
# operacion3=temperatura3* 9/5+32
# operacion4=temperatura4* 9/5+32
# operacion5=temperatura5* 9/5+32

# fahrenheit=(operacion1),(operacion2),(operacion3),(operacion4),(operacion5)

# print("temperatura en °C:", celcius)
# print("temperatura en °F:", fahrenheit)


#---------------------------------EJERCICIO 4-------------------------------
# edades= [int(input("edad1:")),int(input("edad2:")),int(input("edad3:")),int(input("edad4:")),int(input("edad5:"))]
# promedio=sum(edades)/len(edades)
# print(f"Mayor: {max(edades)},Menor: {min(edades)}, promedio: {promedio}")
#----------------------------------EJERCICIO 5---------------------------------------------

frutas= {
"Uva": "El precio por kilo es 2000",
"Limon":"El precio por kilo es 3000",
"Naranja": "El precio por kilo es 4000"
}

print(frutas)

kilo= float(input"Cuantos kilos de Uva quiere: ")
kilo2= float(input"Cuantos kilos de Limon quiere: ") #programa
kilo3= float(input"Cuantos kilos de Naranja quiere: ")









