#PRIMER EJEMPLO DE ELSE
# num = 24
# if num > 36:
#     print ("El numero es mayor")
# else:
#     print ("El numero es menor")

#MULTIPLES CONDICIONES DE IF 

#EJEMPLO DE COMO PODEMOS TRABAJAR CON MULTIPLES IFS ANIDADOS

# x = 25
# if x > 10:
#     print ("Por encima de diez")
#     if x > 20:
#         print ("Y tambien por encima de 20!")
#     else:
#         print ("pero no por encima de 20")

#SENTENCIA ELIF EJEMPLOS

# edad = int (input("Ingrese su edad: "))

# if edad < 0:
#   print ("No cumple")
# elif edad <= 17:
#   print ("< de edad")
# elif edad > 18:
#   print ("> de edad")  
# elif edad <=101:
#   print ("Edad no valida")
# else:
#   print ("Edad no existe")

#EJERCICIO 1

#PASAR DE MINUSCULAS  AMAYUSCULAS CON IF

# letra= input("Ingrese una vocal ( en minuscula): ")

# if letra == "a":
#   print ("A")

# elif letra == "e":
#   print ("E")

# elif letra == "i":
#   print ("I")

# elif letra == "o":
#   print ("O")

# elif letra == "u":
#   print ("U")

# else:
#   print ("No es una vocal")

#----------¿PARA QUE NOS SIRVE LA SENTENCIA ELIF?
#BASICAMENTE NOS SIRVE PARA PODER DARLE MULTIPLES OPCIONES AL PROGRAMA

# comand = input("Ingrese el comando: ")
# comando = "SALIR"
# if comando == " ENTRAR":
#     print ("BIENVENIDO AL SISTEMA")
# elif comando == "SALUDO":
#     print ("HOLA, COMO ESTAS")
# elif comando == "SALIR":
#     print ("SALIENDO DEL SISTEMA")
# else:
#     print ("NO SE RECONOCE EL COMANDO ")

#EJERCICIOS CON CONDICIONALES Y OPERACIONES MATEMATICAS

#EJERCICIO 1

# num = int (input("Ingrese un numero: "))

# if num >= 1:
#    print ("Es un numero positivo")
# elif num <= 0:
#    print ("Es un numero neativo")
# elif edad == 0:
#    print ("El numero es igual a 0")  

#EJERCICIO 2

# num1 = int (input("Ingrese el primer numero: "))
# num2 = int (input("Ingrese el segundo numero: "))

# if num1 > num2:
#     print (f"El primer numero ({num1}), es mayor que el segundo numero ({num2})")
# elif num2 > num1:
#     print (f"El primer numero ({num2}), es mayor que el segundo numero ({num1})")
# elif num1 == num2: 
#     print (f"Los numeros son iguales")

#EJERCICIO 3

# num1 = int (input("Ingrese el primer numero: "))
# if num1 % 2 == 0:
#     print ("El numero es par")
# else:
#     print ("El numero no es par")

#EJERCICIO 4

# num1 = int (input ("Ingrese un numero: "))

# if num1 >= 10 and num1 <=20:
#   print ("El numero si esta entre 10 y 20")
# else:
#   print ("El numero no esta entre 10 y 20")

#EJERCICIO 5 

# n1= int (input("Ingrese el primer numero: "))
# n2= int (input("Ingrese el segundo numero: "))
# n3= int (input("Ingrese el tercer numero: "))

# if n1 >= n2 and n1 >= n3:
#     print (f"El numero mayor es {n1}")

# if n2 >= n1 and n2 >= n3:
#     print (f"El numero mayor es {n2}")

# if n3 >= n1 and n3 >= n2:
#     print (f"El numero mayor es {n3}")

#EJERCICIO 6

# precio = float(input("Ingresa el precio del producto: "))

# if precio > 100:
#     desc = precio * 0.10
#     preciof = precio - desc
# else:
#     preciof = precio 

# print (f"El precio final es {preciof}")

# EJERCICIO 7

# edad = int(input("ingrese su edad: "))
# if edad > 18:
#     print("si puede votar")
# else:
#     print("no puedes votar")

# EJERCICIO 8


precio = float(input("Ingresa el precio del producto: "))

cliente = input("Ingresa el tipo de cliente (vip o normal): ")

if cliente == "vip":
    descuento = 0.8
    preciof = precio * (descuento)
    print("Si obtienes el descuento del 20%")
else:
    preciof = precio
    print("No obtienes descuento")

print(f"El Precio final es: {preciof}")











