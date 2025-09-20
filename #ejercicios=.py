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