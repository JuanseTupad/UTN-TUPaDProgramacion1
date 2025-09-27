# 1
notas1 = [7.5, 8.0, 3.0, 9.0, 2.0, 7.0, 10.0, 6.0, 9.5, 7.0]

print("las notas de los estudiantes son: ", notas1)

suma_notas1 = sum(notas1)
canditdad_notas1 = len(notas1)
promedio1 = suma_notas1/canditdad_notas1

print("el promedio de las notas es de: ", promedio1)

mas_baja1 = min(notas1)
mas_alta1 = max(notas1)

print("la nota mas baja es: ", mas_baja1)
print("y la mas alta es: ", mas_alta1)

# 2
productos2 = []

for i in range(5):
    producto_lista2 = input(f"Ingrese el nombre del producto {i + 1}: ")
    productos2.append(producto_lista2)

productos_ordenados2 = sorted(productos2)
print("lista ordenada alfabeticamente: ", productos_ordenados2)

producto_para_eliminar2 = input("que producto queres eliminar de la lista?: ")

if producto_para_eliminar2 in productos2:
    productos2.remove(producto_para_eliminar2)
    print("lista de productos actualizada:", productos2)
     
# 3
numeros_aleatorios3 = [22, 11, 77, 40, 9, 36, 1, 58, 81, 14, 23, 99, 44, 8, 15]

print("Los numeros son: ", numeros_aleatorios3)

pares3 = []
impares3 = []

for numero3 in numeros_aleatorios3:
    if numero3 % 2 == 0:
        pares3.append(numero3)
    else:
        impares3.append(numero3)
print("Los pares son: ", pares3)
print("Los impares son: ", impares3)

print(f"La cantidad de pares es de: {len(pares3)}")
print(f"la cantidad de impares es de: {len(impares3)}")

# 4
datos4 = [1, 3, 5, 3, 7, 1, 9, 5, 3]

datos4_sin_repetidos = set(datos4)
lista_sin_repetidos4 = list(datos4_sin_repetidos)

print("la lista de datos sin repeticiones es:", lista_sin_repetidos4)

# 5
estudiantes5 = ["Ana", "Juan", "Santiago", "Matias", 
                "Pedro", "Martina", "Tomas", "Emilia"]

print("los estudiantes son: ", estudiantes5)

opcion_agregar5 = "Agregar"
opcion_borrar5 = "Eliminar"

opcion5 = input(f"queres agregar o eliminar? Escribi '{opcion_agregar5}' o '{opcion_borrar5}': ").upper()

if opcion5 == opcion_agregar5:
    nuevo_estudiante5 = input("ingrese el nombre del nuevo estudiante: ")
    estudiantes5.append(nuevo_estudiante5)
elif opcion5 == opcion_borrar5:
    estudiante_a_eliminar5 = input("ingrese el nombre del estudiante a eliminar: ")
    estudiantes5.remove(estudiante_a_eliminar5)

print("la lista final es: ", estudiantes5)

# 7
temperaturas_semana7 = [
    [10, 22],
    [12, 25],
    [8,  20],
    [14, 30],
    [15, 28],
    [11, 23],
    [9,  24]
]
dias7 = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
for i, temp_dia in enumerate(temperaturas_semana7):
    print(f"{dias7[i]}: minima={temp_dia[0]}°, maxima={temp_dia[1]}°")

suma_minimas = 0
suma_maximas = 0
maxima_amplitud = -1
dia_maxima_amplitud = ""

for i, [minima, maxima] in enumerate(temperaturas_semana7):
    suma_minimas += minima
    suma_maximas += maxima
    amplitud_diaria = maxima - minima
    if amplitud_diaria > maxima_amplitud:
        maxima_amplitud = amplitud_diaria
        dia_maxima_amplitud = dias7[i]

num_dias = len(temperaturas_semana7)

promedio_minimas = suma_minimas / num_dias
promedio_maximas = suma_maximas / num_dias

print(f"Promedio de minimas: {promedio_minimas:.2f}°C")
print(f"Promedio de maximas: {promedio_maximas:.2f}°C")

print(f"La mayor amplitud termica fue de {maxima_amplitud}°C y se registro el dia: {dia_maxima_amplitud}")

# 8
notas8 = [
    [7, 8, 6],
    [9, 7, 8],
    [6, 9, 7],
    [8, 6, 9],
    [7, 8, 7]
]

num_estudiantes8 = len(notas8)
num_materias8 = len(notas8[0])

print("Estudiantes vs Materias:")
for i, nota_estudiante8 in enumerate(notas8):
    print(f"Estudiante {i+1}: {nota_estudiante8}")

for i, nota_estudiante8 in enumerate(notas8):
    suma_notas_estudiante8 = sum(nota_estudiante8)
    promedio_estudiante8 = suma_notas_estudiante8 / num_materias8
    print(f"Promedio Estudiante {i+1}: {promedio_estudiante8:.2f}")

for j in range(num_materias8):
    suma_notas_materia8 = 0

    for i in range(num_estudiantes8):
        suma_notas_materia8 += notas8[i][j]
        
    promedio_materia8 = suma_notas_materia8 / num_estudiantes8

    print(f"Promedio Materia {j+1}: {promedio_materia8:.2f}")

# 10
ventas10 = [
    [10, 15, 12, 20, 18, 14, 25],
    [5,  10, 8,  15, 12, 11, 20],
    [2,  5,  4,  6,  7,  3,  10],
    [1,  2,  3,  4,  5,  6,  7]
]

num_productos10 = len(ventas10)
num_dias10 = len(ventas10[0])
dias10 = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

totales_producto10 = []
producto_mas_vendido10 = -1
max_ventas_producto10 = -1

print("Total Vendido por Producto:")
for i, ventas_producto in enumerate(ventas10):
    total_producto = sum(ventas_producto)
    totales_producto10.append(total_producto)

    print(f"Producto {i+1}: {total_producto} unidades.")
    if total_producto > max_ventas_producto10:
        max_ventas_producto10 = total_producto
        producto_mas_vendido10 = i + 1 
    
total_ventas_dia10 = []
dia_mas_vendido_indice10 = -1
max_ventas_dia10 = -1

for j in range(num_dias10):
    total_dia = sum(ventas10[i][j] for i in range(num_productos10))
    total_ventas_dia10.append(total_dia)
    if total_dia > max_ventas_dia10:
        max_ventas_dia10 = total_dia
        dia_mas_vendido_indice10 = j

print(f"Ventas totales por día: {total_ventas_dia10}")
print(f"El dia de mayores ventas fue el {dias10[dia_mas_vendido_indice10]}, con {max_ventas_dia10}")
print(f"El producto mas vendido fue el Producto {producto_mas_vendido10}, con un total de {max_ventas_producto10}")