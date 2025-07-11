#VERIFICA SI EL NUMERO ES POSITIVO, NEGATIVO O CERO

# num1 = float (input("ingrese un numero: "))

# if num1 > 0:
#     print (f"positivo")
# elif num1 < 0 :
#     print (f"es negativo porque es {num1}")
# else:
#     print ("es cero")

# 2 calcula el mayor de los numeros ingresados
# num1= float(input("ingresa el primer numero: "))
# num2= float(input("ingresa el segundo numero: "))
# if num1>num2:
#     print(f"el numero {num1} es mayor que {num2}")
# elif num2>num1:
#      print(f"el numero {num2} es mayor que {num1}")


#----EJERCICIOS CON CONDICIONALES Y OPERACIONES MATEMATICAS 

#VERIFICA SI UN NUMERO ES POSITIVO, NEGATIVO O CERO (1)

# num1 = float (input("ingrese un numero: "))

# if num1 > 0:
#      print ("El numero es positivo")
# elif num1 < 0 :
#      print ("El numero es negativo")
# else:
#      print ("El numero es igual a cero")

# # CALCULA EL MAYOR DE DOS NUMEROS INGRESADOS (2)

# num1= float(input("ingresa el primer numero: "))
# num2= float(input("ingresa el segundo numero: "))
# if num1>num2:
#      print(f"el numero {num1} es mayor que {num2}")
# elif num2>num1:
#       print(f"el numero {num2} es mayor que {num1}")

# DETERMINA SI UN NUMERO ES PAR O IMPAR (3)

# num1= float(input("ingrese un numero: "))
# if num1 == 0:
#     print("El numero es cero que es considerado par")
# elif num1 % 2 == 0:
#     print("El numero es par")
# else:
#     print("El numero es impar")

# #DADO UN NUMERO, VERIFICA SI ESTA ENTRE 10 Y 20 (4)

# if 10 <= num1 <= 20:
#     print("El numero está entre 10 y 20")
# else:
#     print("El numero no está entre 10 y 20")

#DADOS TRES NUMEROS, ENCUENTRA EL MAYOR USANDO CONDICIONALES(5)

# num1 = float(input("Ingresa el primer número: "))
# num2 = float(input("Ingresa el segundo numero: "))
# num3 = float(input("Ingresa el tercer numero: "))

# if num1 >= num2 and num1 >= num3:
#     print("El numero mayor es: " num1)
# elif num2 >= num1 and num2 >= num3:
#     print("El numero mayor es: " num2)
# else:
#     print("El numero mayor es: " num3)

#CALCULA EL PRECIO FINAL CON UN 10% DE DESCUENTO SI EL TOTAL ES MAYOR A $100 (6)

# total = float(input("Ingresa el total de la compra: "))

# if total > 100:
#     descuento = total * 0.10  
#     total_final = total - descuento
#     print(f"Aplicaste un descuento del 10% el precio final es: {total_final:}")
# else:
#     print(f"No aplica descuento el precio final es: {total:}")


#VERIFICA SI UNA PERONA PUEDE VOTAR (MAYOR O IGUAL A 18) (7)

# edad=int(input("Ingresa tu edad: "))

# if edad >= 18:
#     print("Puedes votar")
# else:
#     print("No puedes votar")

#APLICA UN 20% DE DESCUENTO SI EL CLIENTE ES VIP(8)

# precio=float(input("Ingresa el precio del producto: "))
# cliente=input("Eres cliente VIP (si lo eres ingresalo de la siguiente manera -vip-), o normal?: ")

# if cliente == "vip":
#     descuento = precio * 0.20
#     total = precio - descuento
# else:
#     total = precio

# print("El precio final es:", total)

#DETERMINA SI UN NUMERO ES MULTIPLO DE5 Y DE 3 AL MMISMO TIEMPO (9)

# numero=int(input("Ingresa un numero: "))

# if numero % 5 == 0 and numero % 3 == 0:
#     print("Es multiplo de 5 y de 3")
# else:
#     print("No es multiplo de 5 y de 3 al mismo tiempo")

#VERIFICA SI UN NUMERO ES DIVISIBLE ENTRE OTROS DOS  NUMEROS DADOS (10)

# numero=int(input("Ingresa el numero principal: "))
# divisor1=int(input("Ingresa el primer divisor: "))
# divisor2=int(input("Ingresa el segundo divisor: "))

# if numero % divisor1 == 0 and numero % divisor2 == 0:
#     print("El numero es divisible entre los dos divisores")
# else:
#     print("El numero no es divisible entre los dos divisores")

#----------TALLER DESAFIOS LOGICOS DE PYTHON------------------------------------

#PIDE TU EDAD Y MUESTRA SI ERES MENOR DE EDAD, MAYOR DE EDAD O ADULTO MAYOR (65+) (1)

# edad=int(input("ingrese su edad: "))

# if edad <=18:
#     print("eres menor de edad")
# elif edad >= 18 and edad <65:
#     print("eres mayor de edad")
# else:
#     print("eres un adulto mayor")

#SOLICITA TU ESTATURA EN METROS. SI MIDE MENOS DE 1.5 M, ERES CONSIDERADO BAJO; ENTRE 1.5 Y 1.8, ESTATURA MEDIA; MAS DE 1.8 , ALTO (2)

# estatura=float(input("ingrese su estatura en metros (ejemplo 1.50): "))
# if estatura <=1.50:
#      print("eres considerado bajo")
# elif estatura >= 1.50 and estatura <1.80:
#      print("tienes una estatura media")
# else:
#      print("eres una persona alta")

#INGRESA UN NUMERO Y MUESTRA SI ES MULTIPLO DE 2, DE 3 O DE NINGUNO (3)

# num = int(input("Ingresa un numero: "))

# if num % 2 == 0 and num % 3 == 0:
#      print(f"{num} es multiplo de 2 y de 3")
# elif num % 2 == 0:
#      print(f"{num} es multiplo de 2")
# elif num % 3 == 0:
#      print(f"{num} es multiplo de 3")
# else:
#      print(f"{num} no es multiplo de 2 ni de 3")

#PIDE UN NUMERO DECIMAL Y DETERMINA SI TIENE 1, 2 O MAS DE 2 DECIMALES (USA str y split())

# num = float(input("Ingresa un nmero decimal: "))
# partes = str(num).split(".")

# if len(partes) == 1:
#      print("El numero no tiene decimales")
# else:
#      decimales = partes[1]
# if len(decimales) == 1:
#          print("El numero tiene 1 decimal")
# elif len(decimales) == 2:
#          print("El numero tiene 2 decimales")
# else:
#          print("El numero tiene mas de 2 decimales")

#5 Solicita un país y muestra si está en la siguiente tupla: ("Colombia", "Perú", "Argentina", "México").

# paises = ("Colombia", "Peru", "Argentina", "Mexico")

# pais = input("Ingresa un pais, con la primera letra mayuscula: ")

# if pais in paises:
#      print(f"{pais} esta en la lista")
# else:
#      print(f"{pais} no esta en la lista")

# #6 Pide tu tipo de sangre (A, B, AB, O) y muestra tu compatibilidad según un diccionario predefinido.

# compatibilidad = {
#      "A": "A, AB",
#      "B": "B, AB",
#      "AB": "AB",
#      "O": "A, B, AB, O"
#  }

# tipo = input("Tipo de sangre (A, B, AB, O): ")

# if tipo in compatibilidad:
#      print(f"Compatible con: {compatibilidad[tipo]}")
# else:
#      print("Tipo de sangre no válido")

# 7. Ingresa una temperatura en °C. Si es menor de 10, hace frío. Si está entre 10 y
# 25, templado. Más de 25, hace calor.

# temperatura = float(input("Ingresa una temperatura en grados celsius: "))

# if temperatura < 10:
#     print("Hace frio")
# elif temperatura >= 10 and temperatura <= 25:
#     print("Templado")
# else:
#     print("Hace calor")

# 8. Crea un menú con opciones 1. Sumar, 2. Restar, 3. Multiplicar. Pide dos
# números y ejecuta la operación seleccionada.

# print("Menu de opciones")
# print("1 Sumar")
# print("2 Restar")
# print("3 Multiplicar")

# opcion = int(input("Elige una opcion 1 2 o 3 "))

# numero1 = float(input("Ingresa el primer numero "))
# numero2 = float(input("Ingresa el segundo numero "))

# if opcion == 1:
#     resultado = numero1 + numero2
#     print("El resultado es", resultado)
# elif opcion == 2:
#     resultado = numero1 - numero2
#     print("El resultado es", resultado)
# elif opcion == 3:
#     resultado = numero1 * numero2
#     print("El resultado es", resultado)
# else:
#     print("Opcion no valida")

#9. Pide un número entre 1 y 12 y muestra el mes correspondiente usando un
# diccionario.

# meses = {
#     1: "Enero",
#     2: "Febrero",
#     3: "Marzo",
#     4: "Abril",
#     5: "Mayo",
#     6: "Junio",
#     7: "Julio",
#     8: "Agosto",
#     9: "Septiembre",
#     10: "Octubre",
#     11: "Noviembre",
#     12: "Diciembre"
# }

# numero = int(input("Ingresa un numero del 1 al 12 "))

# if numero >= 1 and numero <= 12:
#     print("El mes es", meses[numero])
# else:
#     print("Numero invalido")

# 10. Solicita un número de 4 dígitos y determina si comienza con 1, 2 o cualquier
# otro.

# numero = input("Ingresa un numero de 4 digitos ")

# if len(numero) == 4:
#     if numero[0] == "1":
#         print("Comienza con 1")
#     elif numero[0] == "2":
#         print("Comienza con 2")
#     else:
#         print("Comienza con otro numero que no es ni 1 ni 2")
# else:
#     print("No es un numero de 4 digitos")

#11. Ingresa una palabra. Muestra si su primera letra es vocal, consonante o un
# número.

# texto = input("Escribe una palabra ")
# letra = texto[0]

# if letra in "aeiou":
#     print("Empieza con vocal")
# elif letra.isdigit():
#     print("Empieza con un numero")
# else:
#     print("Empieza con consonante")

# 12. Pide una fruta. Si está en la lista ["manzana", "pera", "piña"], muestra su
# precio. Si no, indica que no está disponible.

# lista_frutas = {
#     "manzana": 1600,
#     "pera": 1300,
#     "pina": 2400
# }

# opcion_fruta = input("Digita una fruta ")

# if opcion_fruta in lista_frutas:
#     print("Cuesta", lista_frutas[opcion_fruta])
# else:
#     print("No esta en la lista")

# 13. Pide tu calificación (0 a 5). Si es menor que 3, reprobado. Entre 3 y 4,
# aprobado. Mayor a 4, excelente.

# nota = float(input("Cuanto sacaste en la materia "))

# if nota < 3:
#     print("Estas reprobado")
# elif nota <= 4:
#     print("Aprobaste")
# else:
#     print("Tu nota es excelente")

#14. Pide un número y muestra si es divisible entre 4, entre 6, o no lo es.

# valor = int(input("Escribe un numero entero "))

# if valor % 4 == 0:
#     print("Divisible entre 4")
# elif valor % 6 == 0:
#     print("Divisible entre 6")
# else:
#     print("No es divisible entre 4 ni 6")

# 15. Crea un sistema de autenticación básico. Pide usuario y clave. Usa un
# diccionario para validar.

# cuentas = {
#     "luis": "abc123",
#     "carla": "clave789",
#     "pedro": "qwerty"
# }

# usuario_ingresado = input("Usuario ")
# clave_ingresada = input("Clave ")

# if usuario_ingresado in cuentas and cuentas[usuario_ingresado] == clave_ingresada:
#     print("Bienvenido")
# else:
#     print("Datos incorrectos")

# 16. Solicita una edad y muestra a qué grupo pertenece: niño (0-12), adolescente
# (13-17), adulto (18-64), mayor (65+)

# edad_persona = int(input("Ingresa tu edad "))

# if edad_persona <= 12:
#     print("Grupo nino")
# elif edad_persona <= 17:
#     print("Grupo adolescente")
# elif edad_persona <= 64:
#     print("Grupo adulto")
# else:
#     print("Grupo mayor")

# 17. Pide el nombre de una ciudad. Si está en una tupla, muestra que es capital; si
# no, muestra “ciudad secundaria”.

# ciudades_capitales = ("tunja", "armenia", "neiva", "pasto")

# nombre_ciudad = input("Escribe una ciudad ").lower()

# if nombre_ciudad in ciudades_capitales:
#     print("Es una capital")
# else:
#     print("Ciudad secundaria")

# 18. Ingresa el valor de una compra. Si es mayor de $200.000 aplica un 15% de
# descuento. Entre $100.000 y $200.000 aplica 10%. Si es menor, no hay
# descuento.

# total_compra = float(input("Valor de la compra "))

# if total_compra > 200000:
#     rebaja = total_compra * 0.15
# elif total_compra >= 100000:
#     rebaja = total_compra * 0.10
# else:
#     rebaja = 0

# pago_final = total_compra - rebaja
# print("Debes pagar", pago_final)

# 19. Pide el nombre y el número de horas trabajadas. Calcula el salario con tarifa
# de $10.000/hora. Si trabajó más de 40 horas, aplica un bono del 20%.

# empleado = input("Nombre del empleado ")
# tiempo = int(input("Horas trabajadas "))

# valor_hora = 10000
# pago = tiempo * valor_hora

# if tiempo > 40:
#     extra = pago * 0.20
#     pago += extra

# print("Salario total de", empleado, "es", pago)

# 20. Ingresa tu puntaje en una prueba (0 a 100). Si es menor a 50, insuficiente. De
# 50 a 79, aceptable. 80 a 100, sobresaliente.

# resultado = int(input("Puntaje obtenido "))

# if resultado < 50:
#     print("Resultado insuficiente")
# elif resultado <= 79:
#     print("Resultado aceptable")
# else:
#     print("Resultado sobresaliente")






