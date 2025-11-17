# 1
lineas = [
    "Lapicera,120.5,30\n",
    "Cuaderno,350,15\n",
    "Regla,80.75,50\n"
]
with open("productos.txt", "w") as archivo:
    archivo.writelines(lineas)

print("se creo productos.txt")

productos = []
# 4
print("Cargando productos desde 'productos.txt'...")
try:
    with open("productos.txt", "r") as archivo_lectura:
        for linea in archivo_lectura:
            linea_limpia = linea.strip()

            if linea_limpia:
                partes = linea_limpia.split(",")

                if len(partes) == 3:
                    producto_dic = {
                        "nombre": partes[0],
                        "precio": float(partes[1]), 
                        "cantidad": int(partes[2])  
                    }
                    productos.append(producto_dic)
                else:
                    print(f"Omitiendo línea mal formada: {linea_limpia}")

except FileNotFoundError:
    print("\n No se encontro el archivo 'productos.txt'.")
    print("El programa continuará con una lista vacía.\n")
except ValueError:
    print("Error: El archivo contiene datos no numéricos en precio o cantidad.")
except Exception as e:
    print(f"Ocurrio un error al leer el archivo: {e}")


# 2
print("\n Lista de Productos Actuales")
if not productos:
    print("No hay productos cargados en memoria.")
else:
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

# 3
print("\n Agregar Nuevo Producto")
try:
    nuevo_nombre = input("Ingrese el nombre del producto: ")
    nuevo_precio = float(input("Ingrese el precio: "))
    nueva_cantidad = int(input("Ingrese la cantidad: "))
    nuevo_producto_dic = {
        "nombre": nuevo_nombre,
        "precio": nuevo_precio,
        "cantidad": nueva_cantidad
    }
    productos.append(nuevo_producto_dic)

    print("\nProducto agregado exitosamente a la lista")
    print(f"Agregado: Producto: {nuevo_nombre} | Precio: ${nuevo_precio} | Cantidad: {nueva_cantidad}")

except ValueError:
    print("Error: El precio debe ser un número (ej: 150.5) y la cantidad un entero (ej: 10).")
    print("No se pudo agregar el producto.")
except Exception as e:
    print(f"Ocurrió un error inesperado al agregar: {e}")


# 5
print("\n Buscar Producto por Nombre")
if not productos:
    print("No hay productos en la lista para buscar.")
else:
    nombre_buscar = input("Ingrese el nombre del producto que desea buscar: ")
    encontrado = False

    for p in productos:
        if p['nombre'].lower() == nombre_buscar.lower():
            print("\n¡Producto encontrado!")
            print(f"  Nombre: {p['nombre']}")
            print(f"  Precio: ${p['precio']}")
            print(f"  Cantidad: {p['cantidad']}")
            encontrado = True
            break

    if not encontrado:
        print(f"El producto '{nombre_buscar}' no se encuentra en la lista.")

# 6
print("\n Guardando Lista Actualizada en 'productos.txt' ")

if not productos:
    print("La lista de productos está vacía. No se guardará nada.")
else:
    try:
        with open("productos.txt", "w") as archivo_guardar:
            for p in productos:
                linea_guardar = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
                archivo_guardar.write(linea_guardar)

        print("¡Archivo 'productos.txt' actualizado con éxito!")

    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")

print("\n Fin del Programa")