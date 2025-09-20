import random

# 1
for numero1 in range(101):
    print(numero1)
# range arma una secuencia de numeros que comienza en 0
# (por eso el 101, si se ponia un 100 el programa iba a ir de 0 a 99

# 3
numero3_A = int(input("ingrese un numero: "))
numero3_B = int(input("ingrese otro numero: "))

# se realizo la organizacion de los numeros para evitar errores
# ( de mayor a menor)
if numero3_A > numero3_B:
    numero3_A, numero3_B = numero3_B, numero3_A
# variable para la suma
suma3 = 0

for i in range(numero3_A + 1, numero3_B):
    suma3 += i

print(f"La suma de los numeros entre {numero3_A} y {numero3_B} es: {suma3}")

# 4
numero4 = int(input("Ingresa un numero para sumar, si ingresas 0, el ptrograma se detendra : "))
suma4 = 0

# El bucle se va ejecutar hasta que el usuario ingrese un 0
while numero4 != 0:
    suma4 += numero4
# proximo numero para sumar en el bucle
    numero4 = int(input("Ingresa otro numero o un 0: "))

print(f"El total acumulado es: {suma4}")

# 5
numero_random_5 = random.randint(0, 9)

intentos5 = 0

adivinanza5 = -1
# xq es un valor que no esta entre el 0 y el 9

print("adivina el numero entre el 0 y el 9")

while adivinanza5 != numero_random_5:
    intentos5 += 1
    adivinanza5 = int(input(f"Intento #{intentos5}, ingresa el numero que crees correcto: "))

print(f"Adivinaste el numero {numero_random_5} en {intentos5} intentos.")

# 6
for numero6 in range(100, -1, -2):
    print(numero6)
# 100 = numero de inicio
# -1 = el limite, es decir que va restar hasta llegar a 0
# -2 = la resta que se hace sucesivamente para mostrar los numeros pares

# 7
numero7 = int(input("Ingrese un numero entero positivo: "))

suma7 = 0

if numero7 >= 0:
    for i in range(numero7 + 1):
        suma7 += i
    print(f"La suma de todos los numeros entre 0 y {numero7} es: {suma7}")

# 8  
pares8 = 0
impares8 = 0
positivos8 = 0
negativos8 = 0

print("Ingresa 100 numeros enteros:")

for i in range(100):
    numero8 = int(input(f"ingrese eñ numero: {i + 1}: "))    
    # Verifica si es par o impar
    if numero8 % 2 == 0:
        pares8 += 1
    else:
        impares8 += 1            
    # Verifica si es positivo, negativo o cero
    if numero8 > 0:
        positivos8 += 1
    elif numero8 < 0:
        negativos8 += 1

print(f"numeros pares: {pares8}")
print(f"numeros impares: {impares8}")
print(f"numeros positivos: {positivos8}")
print(f"numeros negativos: {negativos8}")

# 9
suma_total9 = 0

cantidad_numeros9 = 15

print(f" ingresa {cantidad_numeros9} números enteros.")

for i in range(cantidad_numeros9):
    numero9 = int(input(f"Ingresa el número {i + 1}: "))
    suma_total9 += numero9

if cantidad_numeros9 > 0:
    # calculO del promedio
    media9 = suma_total9 / cantidad_numeros9
print(f"el promedio de los numeros es: {media9}")

