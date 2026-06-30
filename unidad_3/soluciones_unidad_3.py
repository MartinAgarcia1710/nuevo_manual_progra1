# -*- coding: utf-8 -*-
"""
Soluciones - Unidad 3: Estructuras repetitivas
Programación 1 - UTN - Autor: Martín Alejandro García
"""


def ejercicio_1():
    """Contar de 1 hasta N."""
    n = int(input("N: "))
    for i in range(1, n + 1):
        print(i)


def ejercicio_2():
    """Tabla de multiplicar."""
    n = int(input("Número: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


def ejercicio_3():
    """Sumatoria de 1 a N."""
    n = int(input("N: "))
    suma = 0
    for i in range(1, n + 1):
        suma += i
    print(f"La suma es {suma}")


def ejercicio_4():
    """Factorial con bucle."""
    n = int(input("Número: "))
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    print(f"{n}! = {factorial}")


def ejercicio_5():
    """Contar pares entre 1 y N."""
    n = int(input("N: "))
    cantidad = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            cantidad += 1
    print(f"Hay {cantidad} números pares")


def ejercicio_6():
    """Cuenta regresiva."""
    n = int(input("Desde: "))
    while n > 0:
        print(n)
        n -= 1
    print("¡Despegue!")


def ejercicio_7():
    """Promedio con centinela -1."""
    suma = 0
    cantidad = 0
    numero = float(input("Número (-1 para terminar): "))
    while numero != -1:
        suma += numero
        cantidad += 1
        numero = float(input("Número (-1 para terminar): "))
    if cantidad > 0:
        print(f"Promedio: {suma / cantidad:.2f}")
    else:
        print("No se ingresaron números")


def ejercicio_8():
    """Validar edad entre 0 y 120."""
    edad = int(input("Edad: "))
    while edad < 0 or edad > 120:
        print("Edad inválida.")
        edad = int(input("Edad: "))
    print(f"Edad válida: {edad}")


def ejercicio_9():
    """Suma de los dígitos de un número."""
    n = int(input("Número: "))
    n = abs(n)
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    print(f"Suma de los dígitos: {suma}")


def ejercicio_10():
    """¿Es primo?"""
    n = int(input("Número: "))
    if n < 2:
        print("No es primo")
    else:
        es_primo = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                es_primo = False
                break
        print("Es primo" if es_primo else "No es primo")


def ejercicio_11():
    """Mayor de una serie de números."""
    cantidad = int(input("¿Cuántos números? "))
    mayor = float(input("Número 1: "))
    for i in range(2, cantidad + 1):
        n = float(input(f"Número {i}: "))
        if n > mayor:
            mayor = n
    print(f"El mayor es {mayor}")


def ejercicio_12():
    """Triángulo de asteriscos."""
    n = int(input("Cantidad de filas: "))
    for i in range(1, n + 1):
        print("*" * i)


def ejercicio_13():
    """Fibonacci con bucle."""
    n = int(input("Cantidad de términos: "))
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


def ejercicio_14():
    """Adivinar el número secreto."""
    secreto = 42
    intento = int(input("Adiviná el número (1-100): "))
    while intento != secreto:
        if intento < secreto:
            print("Más alto")
        else:
            print("Más bajo")
        intento = int(input("Probá de nuevo: "))
    print("¡Acertaste!")


def ejercicio_15():
    """Contar positivos, negativos y ceros (10 números)."""
    positivos = negativos = ceros = 0
    for i in range(1, 11):
        n = float(input(f"Número {i}: "))
        if n > 0:
            positivos += 1
        elif n < 0:
            negativos += 1
        else:
            ceros += 1
    print(f"Positivos: {positivos}, Negativos: {negativos}, Ceros: {ceros}")


def ejercicio_16():
    """Potencia con bucle (sin usar **)."""
    base = int(input("Base: "))
    exp = int(input("Exponente: "))
    resultado = 1
    for _ in range(exp):
        resultado *= base
    print(f"{base}^{exp} = {resultado}")


def ejercicio_17():
    """Invertir los dígitos de un número."""
    n = int(input("Número: "))
    n = abs(n)
    invertido = 0
    while n > 0:
        invertido = invertido * 10 + n % 10
        n //= 10
    print(f"Número invertido: {invertido}")


def ejercicio_18():
    """Cuadrados del 1 al 15."""
    for i in range(1, 16):
        print(f"{i}² = {i ** 2}")


def ejercicio_19():
    """Menú repetitivo hasta salir."""
    opcion = ""
    while opcion != "3":
        print("\n1: Saludar  2: Despedir  3: Salir")
        opcion = input("Elegí una opción: ")
        if opcion == "1":
            print("¡Hola!")
        elif opcion == "2":
            print("¡Chau!")
        elif opcion == "3":
            print("Saliendo...")
        else:
            print("Opción inválida")


def ejercicio_20():
    """Cuadrícula de coordenadas con bucles anidados."""
    for fila in range(1, 4):
        for columna in range(1, 4):
            print(f"({fila},{columna})", end=" ")
        print()


if __name__ == "__main__":
    pass
