import math
# 1
def imprimir_hola_mundo2():
    print("Hola Mundo!")
imprimir_hola_mundo2()

# 2
def saludar_usuario2(nombre2):
    return f"Hola {nombre2}!"
nombre_usuario2 = input("Por favor, ingresa tu nombre: ")
saludo_personalizado2 = saludar_usuario2(nombre_usuario2)
print(saludo_personalizado2)

# 3
def informacion_personal3(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
nom = input("Ingresa tu nombre: ")
ape = input("Ingresa tu apellido: ")
eda = input("Ingresa tu edad: ")
resi = input("Ingresa tu lugar de residencia: ")
informacion_personal3(nom, ape, eda, resi)

# 4
def calcular_area_circulo4(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo4(radio):
    return 2 * math.pi * radio

radio_usuario4 = float(input("Ingresa el radio del círculo: "))
area = calcular_area_circulo4(radio_usuario4)
perimetro = calcular_perimetro_circulo4(radio_usuario4)

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

# 5
def segundos_a_horas5(segundos):
   return segundos / 3600

segundos_ingresados5 = int(input("Ingresa la cantidad de segundos: "))

horas_calculadas5 = segundos_a_horas5(segundos_ingresados5)

print(f"{segundos_ingresados5} segundos equivalen a {horas_calculadas5:.4f} horas.")

# 6
def tabla_multiplicar6(numero6):
    print(f"Tabla de multiplicar del {numero6}")
    for i in range(1, 11):
        resultado6 = numero6 * i
        print(f"{numero6} x {i} = {resultado6}")

numero_usuario6 = int(input("Ingresa un número para ver su tabla: "))

tabla_multiplicar6(numero_usuario6)

# 7
def operaciones_basicas7(a, b):
    suma7 = a + b
    resta7 = a - b
    multiplicacion7 = a * b
    division7 = a / b
    return (suma7, resta7, multiplicacion7, division7)

num1 = float(input("Ingresa el primer número (a): "))
num2 = float(input("Ingresa el segundo número (b): "))

resultados7 = operaciones_basicas7(num1, num2)

print(f"Resultados de operar {num1} y {num2}:")
print(f"Suma: {resultados7[0]}")
print(f"Resta: {resultados7[1]}")
print(f"Multiplicación: {resultados7[2]}")
print(f"División: {resultados7[3]}")

# 8
def calcular_imc8(peso8, altura8):
    if altura8 == 0:
        return "Error, la altura tiene que ser mayor a 0"
    imc8 = peso8 / (altura8 ** 2)
    return imc8
peso_kg8 = float(input("Ingresa tu peso en kg: "))
altura_m8 = float(input("Ingresa tu altura en mts: "))

imc_calculado8 = calcular_imc8(peso_kg8, altura_m8)

if isinstance(imc_calculado8, str):
    print(imc_calculado8)
else:
    print(f"Tu IMC es de: {imc_calculado8: }")
    
# 9
def celsius_a_fahrenheit9(celsius9):
    fahrenheit9 = (celsius9 * 9/5) + 32
    return fahrenheit9
tempe_en_celsius9 = float(input("Ingresa la temperatura en celsius: "))

tempe_en_fahrenheit9 = celsius_a_fahrenheit9(tempe_en_celsius9)

print(f"{tempe_en_celsius9}°C es igual a {tempe_en_fahrenheit9:}°F")

# 10
def calcular_promedio10(a, b, c):
    return (a + b + c) / 3
num_1 = float(input("Ingresa el 1° número: "))
num_2 = float(input("Ingresa el 2° número: "))
num_3 = float(input("Ingresa el 3° número: "))

promedio10 = calcular_promedio10(num_1, num_2, num_3)

print(f"El promedio es de: {promedio10: }")