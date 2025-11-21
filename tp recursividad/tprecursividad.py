# 1

def calcular_factorial(n: int) -> int:
    if n == 0:
        return 1
    elif n < 0:
        return 0 
    else:
        # n! = n * (n-1)!
        return n * calcular_factorial(n - 1)

def main():
    print("Calculador de Factoriales Recursivo ")

    try:
        # pedir numero al usuario
        max_num = int(input("ingresa un numero entero positivo (N) para calcular N! y todos los anteriores: "))

        if max_num < 1:
            print("por favor, ingresa un numero entero positivo")
            return

        print(f"\nResultados del Factorial (n!) para n desde 1 hasta {max_num}:")

        # Itera desde 1 hasta el numero ingresado
        for i in range(1, max_num + 1):
            resultado = calcular_factorial(i)
            print(f"factorial de {i:2} ({i}!) = {resultado:,}")

    except ValueError:
        print("\n error: ingresa un numero entero.")

if __name__ == "__main__":
    main()

# 2

def calcular_fibonacci(n: int) -> int:
    # Manejo de entrada no válida
    if n < 0:
        raise ValueError("el numero de posicion debe ser entero")

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calcular_fibonacci(n - 1) + calcular_fibonacci(n - 2)

def main():
    print("Calculador de Serie de Fibonacci Recursivo ")

    try:
        max_posicion = int(input("ingresa la posicion maxima (N) para calcular y mostrar la serie de Fibonacci (N >= 1): "))

        if max_posicion < 1:
            print("ingresa un numero entero positivo")
            return

        print(f"\n serie de Fibonacci desde 0 hasta {max_posicion}:")       
        serie = []
        for i in range(max_posicion + 1):
            valor = calcular_fibonacci(i)
            # almacena resultado para mostrar serie completa
            serie.append(str(valor))

        print("Serie Completa:")
        print(" -> ".join(serie))
        print(f"\nEl valor de Fibonacci en la posición {max_posicion} es: {valor:,}")

    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")


if __name__ == "__main__":
    main()

# 3

def calcular_potencia(base: float, exponente: int) -> float:
    # exponente 0
    if exponente == 0:
        return 1.0

    # exponentes negativos, n^-m = 1 / n^m
    elif exponente < 0:
        return 1.0 / calcular_potencia(base, -exponente)

    # recursivo, exponente positivo (m > 0)
    else:
        # formula: n^m = n * n^(m-1)
        return base * calcular_potencia(base, exponente - 1)

def main():
    print(" Calcular potencia recursiva")

    try:
        base = float(input("Ingresa la base (n): "))
        exponente = int(input("Ingresa el exponente (m): "))

        # Caso especial de base 0 (0^m)
        if base == 0 and exponente < 0:
             print("\n error, no se puede elevar 0 a un exponente negativo")
             return

        resultado = calcular_potencia(base, exponente)

        print(f" resultado: {base}^{exponente} = {resultado:,}")

    except ValueError:
        print("\n Error ingresa numeros validos. ")

if __name__ == "__main__":
    main()

# 4

def decimal_a_binario(n: int) -> str:
    if n < 0:
        raise ValueError("solo se admiten numeros enteros positivos ")

    if n == 0:
        return ""
    else:
        cociente = n // 2
        resto = n % 2
        return decimal_a_binario(cociente) + str(resto)


def main():
    print("convertir decimal a binario recursivo:")
    try:
        num_decimal = int(input("ingresa un numero entero positivo en base decimal: "))

        if num_decimal < 0:
            print("por favor, ingresa un numero entero positivo.")
            return

        if num_decimal == 0:
            resultado_binario = "0"
        else:
            resultado_binario = decimal_a_binario(num_decimal)

        print(f" nmero decimal: {num_decimal}")
        print(f" representacion binaria: {resultado_binario}")

    except ValueError as e:
        print(f"\nError: {e}, ingresa un numero entero vvlido.")

if __name__ == "__main__":
    main()

# 5

def es_palindromo(palabra: str) -> bool:
    if len(palabra) <= 1:
        return True
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False
def main():
    print("Detector de Palindromos Recursivo:")
    cadena_original = input("ingrese una palabra o frase (sin considerar espacios o tildes): ")

    palabra_limpia = "".join(c.lower() for c in cadena_original if c.isalpha())

    reemplazos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}

    for tilde, sin_tilde in reemplazos.items():
        palabra_limpia = palabra_limpia.replace(tilde, sin_tilde)

    print(f"cadena original: '{cadena_original}'")
    print(f"cadena limpia: '{palabra_limpia}'")

    if not palabra_limpia:
        print("resultado: la cadena limpia esta vacia.")
        return
    es_p = es_palindromo(palabra_limpia)
    if es_p:
        print("Es un palindromo!")
    else:
        print("No es un Palíndromo")

if __name__ == "__main__":
    main()

# 6

def suma_digitos(n: int) -> int:
    if n < 0:
        n = abs(n)
    # base, si es 0, la suma es 0
    if n == 0:
        return 0
    # recursivo:
    # n % 10 obtiene el ultimo digito.
    # n // 10 obtiene el numero sin el último digito de la recursion
    # sumadigitos(N) = ultimo digito + SumaDígitos
    return (n % 10) + suma_digitos(n // 10)

def main():
    print("Sumar digitos recursivo: ")
    try:
        num = int(input("ingresa un numero entero positivo: "))

        if num < 0:
            print("volve a ingresar un numero valido")
            return

        resultado = suma_digitos(num)
        print(f"el numero ingresado es: {num}")
        print(f"La suma de sus digitos es: {resultado}")

if __name__ == "__main__":
    main()
    
# 8
def contar_digito(numero: int, digito: int) -> int:
    if numero <= 0:
        return 0
    ultimo_digito = numero % 10
    
    coincidencia = 1 if ultimo_digito == digito else 0
    
    numero_reducido = numero // 10
    
    return coincidencia + contar_digito(numero_reducido, digito)

def main():
    print("contador de digitos recursivo")

    try:
        num = int(input("Ingresa el numero entero positivo (ej: 123456789): "))
        digito_buscado = int(input("Ingresa el digito a buscar (0-9): "))

        if num < 0 or digito_buscado < 0 or digito_buscado > 9:
            print("Entrada no válida. Asegurate de que el número sea positivo y el digito este entre el 0 y el 9.")
            return

        resultado = contar_digito(num, digito_buscado)

        print(f"En el numero {num:,}")
        print(f"El digito {digito_buscado} aparece: {resultado} veces")

    except ValueError:
        print("\nError: ingresa numeros enteros validos.")


if __name__ == "__main__":
    main()
