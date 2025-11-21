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
        num = int(input("Ingresa el numero entero positivo (ej: 12233421): "))
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