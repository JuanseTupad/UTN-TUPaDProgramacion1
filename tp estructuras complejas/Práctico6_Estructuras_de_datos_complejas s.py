# 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# añadir:
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# 2

# cambio de precios:
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# 3

# ver solo keys:
lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

# 4

contactos = {}

print("Carga de contactos: ")

for i in range(5):
    nombre = input(f"ingresa en nombre del contacto {i + 1}: ")
    numero = input(f"ingresa el numero de {nombre}: ")

    contactos[nombre] = numero
    print(f"Contacto {nombre} guardado")

print("Agenda completa")

print("Buscar contacto: ")
nombre_buscar = input("Ingresa el nombre del contacto que queres consultar: ")

numero_encontrado = contactos.get(nombre_buscar, f"El contacto '{nombre_buscar}' no existe")

print(numero_encontrado)

# 5

frase = input("Ingresá una frase: ")

palabras = frase.lower().split()

palabras_unicas = set(palabras)
print(f"Palabras unicas: {palabras_unicas}")

recuento = {}

for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

print(f"Recuento: {recuento}")

# 6

alumnos = {}

print("Carga de notas de los alumnos: ")

for i in range(3):
    nombre6 = input(f"Ingrese el nombre del alumno {i + 1}: ")
    nota1 = float(input(f"  Ingrese la nota 1 de {nombre6}: "))
    nota2 = float(input(f"  Ingrese la nota 2 de {nombre6}: "))
    nota3 = float(input(f"  Ingrese la nota 3 de {nombre6}: "))

    notas = (nota1, nota2, nota3)
    alumnos[nombre6] = notas

print("Promedio de Alumnos:")

for nombre6, notas_tupla in alumnos.items():
    promedio = sum(notas_tupla) / len(notas_tupla)
    print(f"El promedio de {nombre6} es: {promedio:.2f}")

# 8

stock = {"Manzana": 50, "Banana": 30, "Naranja": 40}

print("Gestión de Inventario")

while True:

    print("Opciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar stock / Añadir nuevo producto")
    print("3. Ver inventario completo")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        producto = input("Ingrese el nombre del producto a consultar: ").capitalize()

        try:
            cantidad = int(input(f"Ingrese la cantidad a agregar: "))

            if cantidad < 0:
                print("Error: No se pueden ingresar números negativos.")
                continue

            if producto in stock:
                stock[producto] += cantidad
                print(f"Stock actualizado. {producto} ahora tiene {stock[producto]} unidades.")
            else:
                stock[producto] = cantidad
                print(f"Nuevo producto agregado. {producto} tiene {cantidad} unidades.")
        except ValueError:
            print("Error: Ingrese una cantidad valida.")

    elif opcion == '3':
        print("Inventario Actual:")
        if not stock:
            print("El inventario esta vacio.")
        else:
            for producto, cantidad in stock.items():
                print(f"- {producto}: {cantidad}")

    elif opcion == '4':
        print("Saliendo del programa...")
        break

    else:
        print("Error: Opcion no valida. Intente de nuevo.")

# 9

agenda = {
    ("lunes", "10:00"): "Reunion",
    ("martes", "15:00"): "Clase de ingles",
    ("miércoles", "09:00"): "Dentista",
    ("viernes", "21:00"): "Cena"
}

print("Consulta de Agenda")
dia_consulta = input("Ingrese el dia a consultar: ").lower()
hora_consulta = input("Ingrese la hora (ej: 10:00): ")

clave_consulta = (dia_consulta, hora_consulta)

evento = agenda.get(clave_consulta, "No hay ninguna actividad programada en ese dia y hora.")

print(f"\nActividad: {evento}")

# 10

original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia", "Uruguay": "Montevideo"}
print(f"Diccionario Original: {original}")

invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais
    
print(f"Diccionario Invertido: {invertido}")
