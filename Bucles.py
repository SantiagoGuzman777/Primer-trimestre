# n= 5
# while n> 0:
#     print (f"{n}")
#     n -=1
# print ("Termino el conteo")

#-----------------------------------------------------------------------

# num = int(input("Ingrese un numero de la tabla de multiplicar: ")) # Pide al usuario un numero y lo convierte a entero


# i = 1 #Inicializamos el contador en 1 (primer multiplicador)

# print (f"\nTabla de multiplicar del {num}: ") #Imprime un titulo para multiplicar

# while i <= 10: #Bucle que se repite mientras i sea menor o igual a 10
#     print (f"{num} * {i} = {num * i}")#Muestra la multiplicacion y sus resultados
#     i += 1 #Incrementa i en 1 en cada itraccion para avanzar e la tabla

#-------------------------------------------------------------------------------------
# i = 1 
# while i <6:
#     print (i)
#     if i == 3:
#         break
#     i += 1
#---------------------------------------------------------------------
# x = 1
# while True: 
#     x -= 1
#     print (x)
#     if x == 0:
#         break
# print ("Fin bucle")

#------EJERCICIOS CON WHILE, CONDICIONALES Y ESTRUCTURAS-------------------

#--------------------------------EJERCICIO 1----------------------------

# Total = 0
# while True:
#    n1 = int (input(f"Ingrese un numero para sumar (Si desea salir del programa ingrese un 0): "))
#    if n1 == 0:
#      break
#    n2 = int (input("Ingrese el segundo valor para la suma (Si desea salir del programa ingrese un 0): "))

#    Total += n1 + n2

# print (f"La suma total es: {Total}")

#-----------------------------EJERCICIO 2----------------------------------------

# contraseña = "Python123"

# while True:
#     con = input("Ingrese la contraseña (hasta que sea correcta): ")
#     if con == "Python123":
#         print ("Contraseña correcta")
#         break

#--------------------------------EJERCICIO 3---------------------------------------
# lista = []
# pro = input("Ingrese producto (Cuando acabes de pedir productos escribe (fin)):  ")  # Se agrega input() para que el usuario ingrese un valor

# while pro.lower() != "fin":
#     lista.append(pro)  # Ahora agregamos el producto a la lista dentro del bucle
#     pro = input("agregar otro productoo escribir ('FIN') para finalizar: ")

# print(lista)  # Al final, mostramos todos los productos ingresados

#------------------------------EJERCCIO 4----------------------------------

# par= 0
# impar=0
# contador=0
   
# while contador <= 10:
#  n1 = int(input ("Ingrese un numero:"))
#  if n1 % 2 == 0:
#     par +=1
#  else:
#     impar += 1
#  contador +=1

# print (f"Numeros pares : {par}")
# print (f"Numeros impares : {impar}")

#------------------------------------------EJERCICIO 5------------------------------------------







