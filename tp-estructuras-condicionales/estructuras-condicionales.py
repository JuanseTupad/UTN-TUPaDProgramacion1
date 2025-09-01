# tp 3 Estructuras Condicionales
# 1 =
edad_User1 = int(input("Escriba su edad: "))

if edad_User1 > 18:
    print("Es mayor de edad")

# 2 =
nota_user2 = int(input("escriba su nota: "))

if nota_user2 >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
    
# 3 =
numero3 = int(input("ingrese un numero par: "))

if numero3 % 2 == 0:
    print("Ha ingresado un número par")
else: 
    print("Por favor, ingrese un número par")

# 4 =
edad_user4 = int(input("escriba su edad: "))

if edad_user4 < 12:
    print("Niño/a: menor de 12 años.")
elif edad_user4 >= 12 and edad_user4 <= 18:
    print("Adolescente: mayor o igual que 12 años y menor que 18 años")
elif edad_user4 >= 18 and edad_user4 <= 30:
    print("Adulto/a joven: mayor o igual que 18 años y menor que 30 años.")
else:
    print("Adulto/a: mayor o igual que 30 años.")

# 5 = 
contraseña5 = input("ingrese una contraseña: ")

if len(contraseña5) >= 8 and len(contraseña5) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    
# 6 = 
import random
from statistics import mode, median, mean

numeros_aleatorios6 = [random.randint(1, 100) for i in range(50)]

print("los numeros aleatorios son: ", numeros_aleatorios6)
moda = mode(numeros_aleatorios6)
mediana = median(numeros_aleatorios6)
media = mean(numeros_aleatorios6)

print("media:", media)
print("mediana:", mediana)
print("moda:", moda)

if media > mediana:
    print("hay sesgo positivo")
elif media < mediana:
    print("hay sesgo negativo")
elif media == mediana:
    print("no hay sesgo")
    
# 7 =
frase7 = input("ingrese una palabra: ")
ultima_letra7 = frase7[-1]
if ultima_letra7 == "a" or ultima_letra7 == "e" or ultima_letra7 == "i" or ultima_letra7 == "o" or ultima_letra7 == "u":
    print(frase7 + "!")
else:
    print(frase7)
 
# 8 =
nombre_usuario8 = input("ingrese su nombre: ")
opcion_8 = int(input("ingrese la opcion 1, 2 o 3: "))

if opcion_8 == 1: 
    print(nombre_usuario8.upper())
elif opcion_8 == 2:
    print(nombre_usuario8.lower())
elif opcion_8 == 3:
    print(nombre_usuario8.title())

# 9 =
magnitud_terremoto9 = int(input("ingrese el numero de magnitud del terremoto: "))

if magnitud_terremoto9 < 3:
    print("Muy leve")
elif magnitud_terremoto9 >= 3 and magnitud_terremoto9 < 4:
    print("Leve")
elif magnitud_terremoto9 >= 4 and magnitud_terremoto9 < 5: 
    print("Moderado")
elif magnitud_terremoto9 >= 5 and magnitud_terremoto9 < 6:
    print("Fuerte")
elif magnitud_terremoto9 >= 6 and magnitud_terremoto9 < 7:
    print("Muy Fuerte")
else:
    print("extremo")

# 10 =
hemisferio10 = input("ingrese su hemisferio, N o S ")
mes10 = input("ingrese el mes: ")
dia10 = int(input("ingrese el dia: "))

if hemisferio10 == "N":
    if (mes10 == "diciembre" and dia10 >= 21) or (mes10 == "enero") or (mes10 == "febrero") or (mes10 == "marzo" and dia10 <= 20):
        print("Es Invierno")
    elif (mes10 == "marzo" and dia10 >= 21) or (mes10 == "abril") or (mes10 == "mayo") or (mes10 == "junio" and dia10 <= 20):
        print("Es Primavera")
    elif (mes10 == "junio" and dia10 >= 21) or (mes10 == "julio") or (mes10 == "agosto") or (mes10 == "septiembre" and dia10 <= 20):
        print("Es Verano")
    elif (mes10 == "septiembre" and dia10 >= 21) or (mes10 == "octubre") or (mes10 == "noviembre") or (mes10 == "diciembre" and dia10 <= 20):
        print("Es Otoño")
elif hemisferio10 == "S":
    if (mes10 == "diciembre" and dia10 >= 21) or (mes10 == "enero") or (mes10 == "febrero") or (mes10 == "marzo" and dia10 <= 20):
        print("Es Verano")
    elif (mes10 == "marzo" and dia10 >= 21) or (mes10 == "abril") or (mes10 == "mayo") or (mes10 == "junio" and dia10 <= 20):
        print("Es Otoño")
    elif (mes10 == "junio" and dia10 >= 21) or (mes10 == "julio") or (mes10 == "agosto") or (mes10 == "septiembre" and dia10 <= 20):
        print("Es Invierno")
    elif (mes10 == "septiembre" and dia10 >= 21) or (mes10 == "octubre") or (mes10 == "noviembre") or (mes10 == "diciembre" and dia10 <= 20):
        print("Es Primavera")
    
