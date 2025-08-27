# Práctico 1: Estructuras secuenciales

# 1 =
print("Hola Mundo!")

# 2 = 
nombre_2 = input("Diga su nombre:")
print(f"Hola {nombre_2}!")

# 3 =
nombre_3 = input("diga su nombre: ")
apellido_3 = input("diga su apellido: ")
edad_3 = int(input("diga su edad: "))
residencia_3 = input("diga su residencia: ")
print(f"Soy {nombre_3} {apellido_3}, tengo {edad_3} años, y vivo en {residencia_3}.")

# 4 =
import math
pi = math.pi

radio_4 = int(input("ingrese el radio del circulo: "))
area_4 = (radio_4 ** 2) * pi
perimetro_4 = (pi * 2) * radio_4

print(f"el area del circulo es de {area_4} y el perimetro es de {perimetro_4}.")

# 5 =
segundos5 = int(input("ingrese una cantidad de segundos: "))
horas5 = segundos5 / 3600

print(f"en {segundos5} segundos hay {horas5} horas")

# 6 =
numero6 = int(input("ingrese un numero: "))

x1 = numero6 * 1
x2 = numero6 * 2
x3 = numero6 * 3
x4 = numero6 * 4
x5 = numero6 * 5
x6 = numero6 * 6
x7 = numero6 * 7
x8 = numero6 * 8
x9 = numero6 * 9
x10 = numero6 * 10

print(f"1 X {numero6} = {x1}, 2 X {numero6} = {x2}, 3 X {numero6} = {x3}, 4 X {numero6} = {x4}, 5 X {numero6} = {x5}, 6 X {numero6} = {x6}, 7 X {numero6} = {x7}, 8 X {numero6} = {x8}, 9 X {numero6} = {x9}, 10 X {numero6} = {x10}")

# 7 =
numero7a = int(input(" un número entero distintos del 0: "))
numero7b = int(input(" otro número entero distintos del 0: "))
suma7 = numero7a + numero7b
div7 = numero7a / numero7b
multi7 = numero7a * numero7b
resta7 = numero7a - numero7b

print(f"suma = {suma7}")
print(f"divicion = {div7}")
print(f"multiplicacion = {multi7}")
print(f"resta = {resta7}")

# 8 =
altura8 = float(input("ingrese su altura: "))
peso8 = float(input("ingrese su peso: "))

imc8 = peso8 / (altura8 ** 2)

print(f"su imc es de: {imc8}")

# 9 =
grados_celcius9 = float(input("ingrese una temperatura en grados celsius: "))

grados_fahrenheit9 = (grados_celcius9 * 9/5) + 32

print(f"El equivalente en grados Fahrenheit es: {grados_fahrenheit9}")

# 10 =
numero1_10 = int(input("Ingrese el primer numero: "))
numero2_10 = int(input("Ingrese el segundo numero: "))
numero3_10 = int(input("Ingrese el tercer numero: "))

promedio_10 = (numero1_10 + numero2_10 + numero3_10) / 3

print(f"el promedio de estos numeros es de: {promedio_10}")